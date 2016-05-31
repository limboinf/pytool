# coding=utf-8
"""
desc..
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import select
import socket
import sys
import signal
import cPickle
import struct
import argparse

SERVER_HOST = '192.168.1.101'
CHAT_SERVER_NAME = 'server'


def send(channel, *args):
    buffer = cPickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack('L', value)
    channel.send(size)
    channel.send(buffer)


def receive(channel):
    size = struct.calcsize('L')
    size = channel.recv(size)
    try:
        size = socket.ntohl(struct.unpack('L', size)[0])
    except struct.error, e:
        return ''

    buf = ''
    while (len(buf)) < size:
        buf += channel.recv(size-len(buf))
    return cPickle.loads(buf)[0]


class ChatServer(object):
    def __init__(self, port, backlog=5):
        self.clients = 0
        self.clientmap = {}
        self.outputs = []           # list output sockets
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((SERVER_HOST, port))
        print "Server listen to part:%s..." % port
        self.server.listen(backlog)

        # Catch keyboard interrupts
        signal.signal(signal.SIGINT, self.sighandler)

    def sighandler(self, signum, frame):
        """Clean up client outputs"""
        print "Shutting down server..."
        for output in self.outputs:
            output.close()
        self.server.close()


    def get_client_name(self, client):
        """Return the name of the client"""
        info = self.clientmap[client]
        host, name = info[0][0], info[1]
        return "@".join((name, host))

    def run(self):
        inputs = [self.server, sys.stdin]
        self.outputs = []
        running = True
        while running:
            try:
                readable, writeable, exceptional = select.select(inputs, self.outputs, [])
            except select.error, e:
                break

            for sock in readable:
                if sock == self.server:
                    # handle the server socket
                    client, address = self.server.accept()
                    print "Chat server: got connection %d from %s" % (client.fileno(), address)

                    # Read the login name
                    cname = receive(client).split('NAME: ')[1]

                    # Compute client name and send back
                    self.clients += 1
                    send(client, 'CLIENT: ' + str(address[0]))
                    inputs.append(client)
                    self.clientmap[client] = (address, cname)

                    # Send joining information to other clients
                    msg = "\n(欢迎新用户上线:(%d) from %s)" % (self.clients, self.get_client_name(client))
                    for output in self.outputs:
                        send(output, msg)
                    self.outputs.append(client)

                elif sock == sys.stdin:
                    # handle standard input
                    junk = sys.stdin.readline()
                    running = False

                else:
                    # handle all other sockets
                    try:
                        data = receive(sock)
                        if data:
                            # Send as new client's message..
                            msg = '\n#[' + self.get_client_name(sock) + ']>>说: ' + data
                            # Send data to all except ourself
                            for output in self.outputs:
                                if output != sock:
                                    send(output, msg)
                        else:
                            print "Chat server: %d hung up" % sock.fileno()
                            self.clients -= 1
                            sock.close()
                            inputs.remove(sock)
                            self.outputs.remove(sock)

                            # Sending client leaving information to others
                            msg = "\n(下线: %s)" % (self.get_client_name(sock))
                            for output in self.outputs:
                                send(output, msg)
                    except socket.error, e:
                        # Remove
                        inputs.remove(sock)
                        self.outputs.remove(sock)

        self.server.close()


class ChatClient(object):
    def __init__(self, name, port, host=SERVER_HOST):
        self.name = name
        self.port = port
        self.host = host
        # Initial prompt
        self.prompt = '[' + '@'.join((name, socket.gethostname().split('.')[0])) + ']>'
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, self.port))
            print "New connected to chat server@port:%d" % self.port
            self.connected = True

            # Send my name..
            send(self.sock, 'NAME: ' + self.name)
            data = receive(self.sock)

            # Contains client address, set it
            addr = data.split('CLIENT: ')[1]
            self.prompt = '[' + '@'.join((self.name, addr)) + ']>'
        except socket.error, e:
            print "Failed to connect to chat server @ port %d" % self.port
            sys.exit(1)

    def run(self):
        """Chat client main loop"""
        while self.connected:
            try:
                sys.stdout.write(self.prompt)
                sys.stdout.flush()
                # Wait for input from stdin and socket
                inputs = [0, self.sock]
                readable, writeable, exceptional = select.select(inputs, [], [])
                for sock in readable:
                    if sock == 0:
                        data = sys.stdin.readline().strip()
                        if data:
                            send(self.sock, data)
                    elif sock == self.sock:
                        data = receive(self.sock)
                        if not data:
                            print "Client shutting down."
                            self.connected = False
                            break
                        else:
                            sys.stdout.write(data + '\n')
                            sys.stdout.flush()
            except KeyboardInterrupt:
                print "Client interrupted"
                self.sock.close()
                break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Socket Server Example with Select")
    parser.add_argument('--name', action="store", dest="name", required=True)
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    parser.add_argument('--host', action="store", dest="host", required=False)

    args = parser.parse_args()
    port = args.port
    name = args.name
    host = args.host
    if name == CHAT_SERVER_NAME:
        server = ChatServer(port)
        server.run()
    else:
        if host:
            client = ChatClient(name, port, host)
        else:
            client = ChatClient(name, port)
        client.run()
