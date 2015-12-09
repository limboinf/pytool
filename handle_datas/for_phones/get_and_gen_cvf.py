# coding=utf-8
"""
android 通讯录vcf操作
    :copyright: (c) 2015 by fangpeng.
    :license: MIT, see LICENSE for more details.

"""

import re


def utf2unichr(brr):
    binstr=brr[0][4:]
    for i in range(1, len(brr)):
        binstr = binstr + (brr[i][2:])
    return unichr(int(binstr, 2))


def analyse(arr):
    for i in range(len(arr)):
        arr[i] = bin(eval("0x"+arr[i]))[2:]         # [2:]去掉 "0b"

    dst = ""
    print arr
    for i in range(len(arr)):
        if (int(arr[i], 2) < int("10000000", 2)):   # <128 : ASCII char
            dst = dst + chr(int(arr[i], 2))
        elif (arr[i][:4] == '1110'):
            print '...', arr[i: i+3]
            dst = dst + utf2unichr(arr[i: i+3])      #i,i+1,i+2
        elif (arr[i][:2]=='10'):
            pass
        else:
            print "something worng,%s" % arr[i]
    return dst


def gets(filename):
    """解析vcf文件"""
    spec = "FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:="
    with open(filename, 'r') as f:
        cnt = -1
        array = []

        for i in f:
            name = ''           # 名字
            if "BEGIN:" in i:
                cnt += 1
                array.append({})

            if re.search("^FN", i):
                s = i.strip("\n")
                if "FN;" in i:
                    s = s.replace(spec, "")
                    s = s.split("=")
                    name = analyse(s)
                elif "FN:" in i:
                    name = s.replace("FN:", "")
                else:
                    print "something wrong!%s" % i

                array[cnt]['name'] = name

            if "TEL;" in i:
                s = i.strip("\n")
                s = re.sub("TEL;.*;PREF:", "", s)
                PhoneCode = re.sub("-", "", s)
                array[cnt]["tel"] = PhoneCode

        for i in range(len(array)):
            if "name" in array[i]:
                print array[i]['name']
            else:
                pass
            if "tel" in array[i]:
                print array[i]['tel']
            else:
                pass


def gen():
    """批量生成vcf文件"""
    import random
    a = '=E4=B8=80'     # 一
    b = '=E5=8A=A0'     # 加
    c = '=E6=9C=8D'     # 服
    d = '=E5=8A=A1'     # 务
    e = '=E5=8C=85'     # 包
    f = '=E5=85=B8'     # 典
    lis = [a, b, c, d, e, f]
    count = 0
    with open('yidong.txt', 'r') as yd, open('1.vcf', 'a+') as vcf:
        st = """BEGIN:VCARD\nVERSION:2.1\nN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;=E5=8C=85=E5=85=B8=C7;;;\nFN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:%s\nTEL;CELL:%sEND:VCARD\n"""
        for f in yd.readlines():
            count += 1
            c = random.choice(range(1, 10))
            name = ''
            for i in range(c):
                name += random.choice(lis)
            vcf.write(st % (name, f))
            if count == 1000:
                break


if __name__ == '__main__':
    gets('1.vcf')