# coding=utf-8
"""
desc..
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import os
import socket
import struct
import select
import time
import argparse


ICMP_ECHO_REQUEST = 8
DEFAULT_TIMEOUT = 2
DEFAULT_COUNT = 4


class Ping(object):
    def __init__(self, target_host, count=DEFAULT_COUNT, timeout=DEFAULT_TIMEOUT):
        self.target_host = target_host
        self.count = count
        self.timeout = timeout

    def do_checksum(self, source_string):
        """
        Verify the packet integritity
        检验和的校验，校验方法如下：
            把校验和字段置为0
            将icmp包（包括header和data）以16bit（2个字节）为一组，并将所有组相加（二进制求和）
            若高16bit不为0，则将高16bit与低16bit反复相加，直到高16bit的值为0，从而获得一个只有16bit长度的值
            将此16bit值进行按位求反操作，将所得值替换到校验和字段

        """
        sum = 0     # 把校验和字段置为0

        max_count = (len(source_string) / 2) * 2        # 取得偶数

        count = 0
        while count < max_count:
            # 分割数据每两字节(16bit)为一组
            # ord字符的ascii 码
            val = ord(source_string[count + 1]) * 256 + ord(source_string[count])
            sum = sum + val
            sum = sum & 0xffffffff
            count = count + 2

        # 如果数据长度为奇数,则将最后一位单独相加
        if max_count < len(source_string):
            sum = sum + ord(source_string[len(source_string) - 1])
            sum = sum & 0xffffffff

        # 将高16位与低16位相加直到高16位为0
        sum = (sum >> 16) + (sum & 0xffff)
        sum = sum + (sum >> 16)
        answer = ~sum
        answer = answer & 0xffff
        answer = answer >> 8 | (answer << 8 & 0xff00)
        return answer       # 返回的是十进制整数


    def receive_pong(self, sock, ID, timeout):
        """
        接受ICMP类型码为8的ICMP回应报文的方法
        Receive ping from the socket.
        """
        time_remaining = timeout
        while True:
            start_time = time.time()
            readable = select.select([sock], [], [], time_remaining)
            time_spent = (time.time() - start_time)
            if readable[0] == []:       # Timeout
                return

            time_received = time.time()
            recv_packet, addr = sock.recvfrom(1024)

            # ICMP报头从IP报头的第160位(即:20字节)开始, 到224位(即:28字节)结尾
            # 由于MTU=1500, 则IP数据报: 20字节IP首部 + 8字节ICMP首部 + 1472字节（数据大小）。
            icmp_header = recv_packet[20: 28]

            (_type,         # 第160-167位: ICMP的类型,标识生成的错误报文
             code,          # 第168-175位: 进一步划分ICMP的类型,该字段用来查找产生错误的原因,值1至15等来表示不同的意思
             checksum,      # 第176-183位: 校验码,包含从ICMP报头和数据部分计算得来的，用于检查错误的数据，其中此校验码字段的值视为0。
             packet_ID,     # 第192-207位: ID - 这个字段包含了ID值，在Echo Reply类型的消息中要返回这个字段。
             sequence       # 第208-224位: 这个字段包含一个序号，同样要在Echo Reply类型的消息中要返回这个字段。
             ) = struct.unpack('bbHHh', icmp_header)

            # reply的校验packet_ID 等于 ID则校验成功
            if packet_ID == ID:
                bytes_In_double = struct.calcsize("d")
                # 获取紧接在ICMP报头的后面（以8位为一组）的填充的数据
                time_sent = struct.unpack("d", recv_packet[28: 28 + bytes_In_double])[0]
                return time_received - time_sent        # 计算从发出去的时间到目前receive的时长

            # 否则就超时处理返回None
            time_remaining = time_remaining - time_spent
            if time_remaining <= 0:
                return


    def send_ping(self, sock, ID):
        """
        Send ping to the target host
        首先获取远程主机的DNS主机名
        然后使用struct模块创建一个ICMP_ECHO_REQUEST数据包，将查验请求的数据发送到目标主机。
        在此发送前也需要进行do_checksum()方法的校验。
        """
        target_addr = socket.gethostbyname(self.target_host)
        my_checksum = 0

        # 创建ICMP报头
        # 不同类型的报文是由类型字段和代码字段来共同决定。下表是各种类型的I C M P报文。
        # ref: http://www.s0nnet.com/archives/icmp-ping
        # 如果类型(Type)为8,那么代码(Code)要设置0 表示请求回显(ping请求)
        header = struct.pack("bbHHh",
                             ICMP_ECHO_REQUEST,     # Type
                             0,                     # Code
                             my_checksum,           # checksum
                             ID,                    # ID
                             1                      # sequence
                             )
        bytes_In_double = struct.calcsize('d')
        data = (192 - bytes_In_double) * "Q"
        data = struct.pack('d', time.time()) + data

        # Get the checksum on the data and the dummy header.
        my_checksum = self.do_checksum(header + data)
        header = struct.pack(
            'bbHHh', ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ID, 1
        )
        packet = header + data
        sock.sendto(packet, (target_addr, 1))

    def ping_once(self):
        """
        Returns the delay (in seconds) or none on timeout.
        向远程主机发送一次查验：将ICMP协议传给socket()方法，创建一个原始的ICMP套接字。
        由于ping程序需要使用SOCK_RAW来构建数据包，所以需要root权限才能运行这个程序。
        """
        # Return the protocol number for the named protocol.  (Rarely used.)
        icmp = socket.getprotobyname('icmp')
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        except socket.error, (errno, msg):
            # 未使用root运行时抛出的异常。
            if errno == 1:
                # Not superuser, so operation not permitted
                msg += "ICMP messages can only be sent from root user processes"
                raise socket.error(msg)
        except Exception, e:
            print "Exception: %s" % e

        my_ID = os.getpid() & 0xFFFF

        self.send_ping(sock, my_ID)
        delay = self.receive_pong(sock, my_ID, self.timeout)
        sock.close()
        return delay

    def ping(self):
        for i in range(self.count):
            print "Ping to %s..." % self.target_host,
            try:
                delay = self.ping_once()
            except socket.gaierror, e:
                print "Ping failed, (socket error:'%s')" % e[1]
                break

            if delay == None:
                print "Ping failed, (timeout within %ssec.)" % self.timeout
            else:
                delay = delay * 1000
                print "Get ping in %0.4fms" % delay


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python ping')
    parser.add_argument('--target-host', action="store", dest="target_host", required=True)
    given_args = parser.parse_args()
    target_host = given_args.target_host
    ping = Ping(target_host=target_host)
    ping.ping()