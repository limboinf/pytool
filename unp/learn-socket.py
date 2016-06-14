# coding=utf-8
# encoding: utf-8
# module _socket
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/_socket.so
# by generator 1.138
"""
Implementation module for socket operations.

See the socket module for documentation.
"""
# no imports

# Variables with simple values

AF_APPLETALK = 16
AF_DECnet = 12
AF_INET = 2
AF_INET6 = 30
AF_IPX = 23
AF_ROUTE = 17
AF_SNA = 11
AF_UNIX = 1
AF_UNSPEC = 0

AI_ADDRCONFIG = 1024
AI_ALL = 256
AI_CANONNAME = 2
AI_DEFAULT = 1536
AI_MASK = 5127
AI_NUMERICHOST = 4
AI_NUMERICSERV = 4096
AI_PASSIVE = 1
AI_V4MAPPED = 2048

AI_V4MAPPED_CFG = 512

EAI_ADDRFAMILY = 1
EAI_AGAIN = 2
EAI_BADFLAGS = 3
EAI_BADHINTS = 12
EAI_FAIL = 4
EAI_FAMILY = 5
EAI_MAX = 15
EAI_MEMORY = 6
EAI_NODATA = 7
EAI_NONAME = 8
EAI_OVERFLOW = 14
EAI_PROTOCOL = 13
EAI_SERVICE = 9
EAI_SOCKTYPE = 10
EAI_SYSTEM = 11

has_ipv6 = True

INADDR_ALLHOSTS_GROUP = 3758096385

INADDR_ANY = 0
INADDR_BROADCAST = 4294967295
INADDR_LOOPBACK = 2130706433

INADDR_MAX_LOCAL_GROUP = 3758096639

INADDR_NONE = 4294967295

INADDR_UNSPEC_GROUP = 3758096384

IPPORT_RESERVED = 1024
IPPORT_USERRESERVED = 5000

IPPROTO_AH = 51
IPPROTO_DSTOPTS = 60
IPPROTO_EGP = 8
IPPROTO_EON = 80
IPPROTO_ESP = 50
IPPROTO_FRAGMENT = 44
IPPROTO_GGP = 3
IPPROTO_GRE = 47
IPPROTO_HELLO = 63
IPPROTO_HOPOPTS = 0
IPPROTO_ICMP = 1
IPPROTO_ICMPV6 = 58
IPPROTO_IDP = 22
IPPROTO_IGMP = 2
IPPROTO_IP = 0
IPPROTO_IPCOMP = 108
IPPROTO_IPIP = 4
IPPROTO_IPV4 = 4
IPPROTO_IPV6 = 41
IPPROTO_MAX = 256
IPPROTO_ND = 77
IPPROTO_NONE = 59
IPPROTO_PIM = 103
IPPROTO_PUP = 12
IPPROTO_RAW = 255
IPPROTO_ROUTING = 43
IPPROTO_RSVP = 46
IPPROTO_TCP = 6
IPPROTO_TP = 29
IPPROTO_UDP = 17
IPPROTO_XTP = 36

IPV6_CHECKSUM = 26

IPV6_JOIN_GROUP = 12

IPV6_LEAVE_GROUP = 13

IPV6_MULTICAST_HOPS = 10
IPV6_MULTICAST_IF = 9
IPV6_MULTICAST_LOOP = 11

IPV6_RECVTCLASS = 35

IPV6_RTHDR_TYPE_0 = 0

IPV6_TCLASS = 36

IPV6_UNICAST_HOPS = 4

IPV6_V6ONLY = 27

IP_ADD_MEMBERSHIP = 12

IP_DEFAULT_MULTICAST_LOOP = 1
IP_DEFAULT_MULTICAST_TTL = 1

IP_DROP_MEMBERSHIP = 13

IP_HDRINCL = 2

IP_MAX_MEMBERSHIPS = 4095

IP_MULTICAST_IF = 9
IP_MULTICAST_LOOP = 11
IP_MULTICAST_TTL = 10

IP_OPTIONS = 1
IP_RECVDSTADDR = 7
IP_RECVOPTS = 5
IP_RECVRETOPTS = 6
IP_RETOPTS = 8
IP_TOS = 3
IP_TTL = 4

MSG_CTRUNC = 32
MSG_DONTROUTE = 4
MSG_DONTWAIT = 128
MSG_EOR = 8
MSG_OOB = 1
MSG_PEEK = 2
MSG_TRUNC = 16
MSG_WAITALL = 64

NI_DGRAM = 16
NI_MAXHOST = 1025
NI_MAXSERV = 32
NI_NAMEREQD = 4
NI_NOFQDN = 1
NI_NUMERICHOST = 2
NI_NUMERICSERV = 8

SHUT_RD = 0
SHUT_RDWR = 2
SHUT_WR = 1

SOCK_DGRAM = 2
SOCK_RAW = 3
SOCK_RDM = 4
SOCK_SEQPACKET = 5
SOCK_STREAM = 1

SOL_IP = 0
SOL_SOCKET = 65535
SOL_TCP = 6
SOL_UDP = 17

SOMAXCONN = 128
SO_ACCEPTCONN = 2
SO_BROADCAST = 32
SO_DEBUG = 1
SO_DONTROUTE = 16
SO_ERROR = 4103
SO_KEEPALIVE = 8
SO_LINGER = 128
SO_OOBINLINE = 256
SO_RCVBUF = 4098
SO_RCVLOWAT = 4100
SO_RCVTIMEO = 4102
SO_REUSEADDR = 4
SO_REUSEPORT = 512
SO_SNDBUF = 4097
SO_SNDLOWAT = 4099
SO_SNDTIMEO = 4101
SO_TYPE = 4104
SO_USELOOPBACK = 64

TCP_KEEPCNT = 258
TCP_KEEPINTVL = 257
TCP_MAXSEG = 2
TCP_NODELAY = 1

# functions


def fromfd(fd, family, type, proto=None):  # real signature unknown; restored from __doc__
    """
    fromfd(fd, family, type[, proto]) -> socket object

    Create a socket object from a duplicate of the given
    file descriptor.
    The remaining arguments are the same as for socket().
    """
    return socket


def getaddrinfo(
        host,
        port,
        family=None,
        socktype=None,
        proto=None,
        flags=None):
    """
    getaddrinfo(host, port [, family, socktype, proto, flags])
        -> list of (family, socktype, proto, canonname, sockaddr)

    解决主机和端口addrinfo结构。
    """
    return []


def getdefaulttimeout():  # real signature unknown; restored from __doc__
    """
    getdefaulttimeout() -> timeout

    Returns the default timeout in seconds (float) for new socket objects.
    A value of None indicates that new socket objects have no timeout.
    When the socket module is first imported, the default is None.
    """
    return timeout


def gethostbyaddr(host):  # real signature unknown; restored from __doc__
    """
    gethostbyaddr(host) -> (name, aliaslist, addresslist)

    Return the true host name, a list of aliases, and a list of IP addresses,
    for a host.  The host argument is a string giving a host name or IP number.
    """
    pass


def gethostbyname(host):  # real signature unknown; restored from __doc__
    """
    gethostbyname(host) -> address

    Return the IP address (a string of the form '255.255.255.255') for a host.
    """
    pass


def gethostbyname_ex(host):  # real signature unknown; restored from __doc__
    """
    gethostbyname_ex(host) -> (name, aliaslist, addresslist)

    Return the true host name, a list of aliases, and a list of IP addresses,
    for a host.  The host argument is a string giving a host name or IP number.
    """
    pass


def gethostname():  # real signature unknown; restored from __doc__
    """
    gethostname() -> string

    Return the current host name.
    """
    return ""


def getnameinfo(sockaddr, flags):  # real signature unknown; restored from __doc__
    """
    getnameinfo(sockaddr, flags) --> (host, port)

    Get host and port for a sockaddr.
    """
    pass


def getprotobyname(name):  # real signature unknown; restored from __doc__
    """
    getprotobyname(name) -> integer

    Return the protocol number for the named protocol.  (Rarely used.)
    """
    return 0


# real signature unknown; restored from __doc__
def getservbyname(servicename, protocolname=None):
    """
    getservbyname(servicename[, protocolname]) -> integer

    Return a port number from a service name and protocol name.
    The optional protocol name, if given, should be 'tcp' or 'udp',
    otherwise any protocol will match.
    """
    return 0


# real signature unknown; restored from __doc__
def getservbyport(port, protocolname=None):
    """
    getservbyport(port[, protocolname]) -> string

    Return the service name from a port number and protocol name.
    The optional protocol name, if given, should be 'tcp' or 'udp',
    otherwise any protocol will match.
    """
    return ""


def htonl(integer):  # real signature unknown; restored from __doc__
    """
    htonl(integer) -> integer

    Convert a 32-bit integer from host to network byte order.
    """
    return 0


def htons(integer):  # real signature unknown; restored from __doc__
    """
    htons(integer) -> integer

    Convert a 16-bit integer from host to network byte order.
    """
    return 0


def inet_aton(string):  # real signature unknown; restored from __doc__
    """
    inet_aton(string) -> packed 32-bit IP representation

    Convert an IP address in string format (123.45.67.89) to the 32-bit packed
    binary format used in low-level network functions.
    """
    pass


def inet_ntoa(packed_ip):  # real signature unknown; restored from __doc__
    """
    inet_ntoa(packed_ip) -> ip_address_string

    Convert an IP address from 32-bit packed binary format to string format
    """
    pass


def inet_ntop(af, packed_ip):  # real signature unknown; restored from __doc__
    """
    inet_ntop(af, packed_ip) -> string formatted IP address

    Convert a packed IP address of the given family to string format.
    """
    return ""


def inet_pton(af, ip):  # real signature unknown; restored from __doc__
    """
    inet_pton(af, ip) -> packed IP address string

    Convert an IP address from string format to a packed string suitable
    for use with low-level network functions.
    """
    pass


def ntohl(integer):  # real signature unknown; restored from __doc__
    """
    ntohl(integer) -> integer

    Convert a 32-bit integer from network to host byte order.
    """
    return 0


def ntohs(integer):  # real signature unknown; restored from __doc__
    """
    ntohs(integer) -> integer

    Convert a 16-bit integer from network to host byte order.
    """
    return 0


def setdefaulttimeout(timeout):  # real signature unknown; restored from __doc__
    """
    setdefaulttimeout(timeout)

    Set the default timeout in seconds (float) for new socket objects.
    A value of None indicates that new socket objects have no timeout.
    When the socket module is first imported, the default is None.
    """
    pass


# real signature unknown; restored from __doc__
def socketpair(family=None, type=None, proto=None):
    """
    socketpair([family[, type[, proto]]]) -> (socket object, socket object)

    Create a pair of socket objects from the sockets returned by the platform
    socketpair() function.
    The arguments are the same as for socket() except the default family is
    AF_UNIX if defined on the platform; otherwise, the default is AF_INET.
    """
    pass

# classes


class error(IOError):
    # no doc

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    __weakref__ = property(
        lambda self: object(),
        lambda self,
        v: None,
        lambda self: None)  # default
    """list of weak references to the object (if defined)"""


class gaierror(error):
    # no doc

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass


class herror(error):
    # no doc

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass


class SocketType(object):
    """
    socket([family[, type[, proto]]]) -> socket object

    Open a socket of the given type.  The family argument specifies the
    address family; it defaults to AF_INET.  The type argument specifies
    whether this is a stream (SOCK_STREAM, this is the default)
    or datagram (SOCK_DGRAM) socket.  The protocol argument defaults to 0,
    specifying the default protocol.  Keyword arguments are accepted.

    A socket object represents one endpoint of a network connection.

    Methods of socket objects (keyword arguments not allowed):

    accept() -- accept a connection, returning new socket and client address
    bind(addr) -- bind the socket to a local address
    close() -- close the socket
    connect(addr) -- connect the socket to a remote address
    connect_ex(addr) -- connect, return an error code instead of an exception
    dup() -- return a new socket object identical to the current one [*]
    fileno() -- return underlying file descriptor
    getpeername() -- return remote address [*]
    getsockname() -- return local address
    getsockopt(level, optname[, buflen]) -- get socket options
    gettimeout() -- return timeout or None
    listen(n) -- start listening for incoming connections
    makefile([mode, [bufsize]]) -- return a file object for the socket [*]
    recv(buflen[, flags]) -- receive data
    recv_into(buffer[, nbytes[, flags]]) -- receive data (into a buffer)
    recvfrom(buflen[, flags]) -- receive data and sender's address
    recvfrom_into(buffer[, nbytes, [, flags])
      -- receive data and sender's address (into a buffer)
    sendall(data[, flags]) -- send all data
    send(data[, flags]) -- send data, may not send all of it
    sendto(data[, flags], addr) -- send data to a given address
    setblocking(0 | 1) -- set or clear the blocking I/O flag
    setsockopt(level, optname, value) -- set socket options
    settimeout(None | float) -- set or clear the timeout
    shutdown(how) -- shut down traffic in one or both directions

     [*] not available on all platforms!
    """

    def accept(self):  # real signature unknown; restored from __doc__
        """
        accept() -> (socket object, address info)

        Wait for an incoming connection.  Return a new socket representing the
        connection, and the address of the client.  For IP sockets, the address
        info is a pair (hostaddr, port).
        """
        pass

    def bind(self, address):  # real signature unknown; restored from __doc__
        """
        bind(address)

        Bind the socket to a local address.  For IP sockets, the address is a
        pair (host, port); the host must refer to the local host. For raw packet
        sockets the address is a tuple (ifname, proto [,pkttype [,hatype]])
        """
        pass

    def close(self):  # real signature unknown; restored from __doc__
        """
        close()

        Close the socket.  It cannot be used after this call.
        """
        pass

    def connect(self, address):  # real signature unknown; restored from __doc__
        """
        connect(address)

        Connect the socket to a remote address.  For IP sockets, the address
        is a pair (host, port).
        """
        pass

    def connect_ex(self, address):  # real signature unknown; restored from __doc__
        """
        connect_ex(address) -> errno

        This is like connect(address), but returns an error code (the errno value)
        instead of raising an exception when an error occurs.
        """
        pass

    def dup(self):  # real signature unknown; restored from __doc__
        """
        dup() -> socket object

        Return a new socket object connected to the same system resource.
        """
        return socket

    def fileno(self):  # real signature unknown; restored from __doc__
        """
        fileno() -> integer

        Return the integer file descriptor of the socket.
        """
        return 0

    def getpeername(self):  # real signature unknown; restored from __doc__
        """
        getpeername() -> address info

        Return the address of the remote endpoint.  For IP sockets, the address
        info is a pair (hostaddr, port).
        """
        pass

    def getsockname(self):  # real signature unknown; restored from __doc__
        """
        getsockname() -> address info

        Return the address of the local endpoint.  For IP sockets, the address
        info is a pair (hostaddr, port).
        """
        pass

    # real signature unknown; restored from __doc__
    def getsockopt(self, level, option, buffersize=None):
        """
        getsockopt(level, option[, buffersize]) -> value

        Get a socket option.  See the Unix manual for level and option.
        If a nonzero buffersize argument is given, the return value is a
        string of that length; otherwise it is an integer.
        """
        pass

    def gettimeout(self):  # real signature unknown; restored from __doc__
        """
        gettimeout() -> timeout

        Returns the timeout in seconds (float) associated with socket
        operations. A timeout of None indicates that timeouts on socket
        operations are disabled.
        """
        return timeout

    def listen(self, backlog):  # real signature unknown; restored from __doc__
        """
        listen(backlog)

        Enable a server to accept connections.  The backlog argument must be at
        least 0 (if it is lower, it is set to 0); it specifies the number of
        unaccepted connections that the system will allow before refusing new
        connections.
        """
        pass

    # real signature unknown; restored from __doc__
    def makefile(self, mode=None, buffersize=None):
        """
        makefile([mode[, buffersize]]) -> file object

        Return a regular file object corresponding to the socket.
        The mode and buffersize arguments are as for the built-in open() function.
        """
        return file('/dev/null')

    def recv(self, buffersize, flags=None):  # real signature unknown; restored from __doc__
        """
        recv(buffersize[, flags]) -> data

        Receive up to buffersize bytes from the socket.  For the optional flags
        argument, see the Unix manual.  When no data is available, block until
        at least one byte is available or until the remote end is closed.  When
        the remote end is closed and all data is read, return the empty string.
        """
        pass

    # real signature unknown; restored from __doc__
    def recvfrom(self, buffersize, flags=None):
        """
        recvfrom(buffersize[, flags]) -> (data, address info)

        Like recv(buffersize, flags) but also return the sender's address info.
        """
        pass

    # real signature unknown; restored from __doc__
    def recvfrom_into(self, buffer, nbytes=None, flags=None):
        """
        recvfrom_into(buffer[, nbytes[, flags]]) -> (nbytes, address info)

        Like recv_into(buffer[, nbytes[, flags]]) but also return the sender's address info.
        """
        pass

    # real signature unknown; restored from __doc__
    def recv_into(self, buffer, nbytes=None, flags=None):
        """
        recv_into(buffer, [nbytes[, flags]]) -> nbytes_read

        A version of recv() that stores its data into a buffer rather than creating
        a new string.  Receive up to buffersize bytes from the socket.  If buffersize
        is not specified (or 0), receive up to the size available in the given buffer.

        See recv() for documentation about the flags.
        """
        pass

    def send(self, data, flags=None):  # real signature unknown; restored from __doc__
        """
        send(data[, flags]) -> count

        Send a data string to the socket.  For the optional flags
        argument, see the Unix manual.  Return the number of bytes
        sent; this may be less than len(data) if the network is busy.
        """
        pass

    def sendall(self, data, flags=None):  # real signature unknown; restored from __doc__
        """
        sendall(data[, flags])

        Send a data string to the socket.  For the optional flags
        argument, see the Unix manual.  This calls send() repeatedly
        until all data is sent.  If an error occurs, it's impossible
        to tell how much data has been sent.
        """
        pass

    # real signature unknown; NOTE: unreliably restored from __doc__
    def sendto(self, data, flags=None, *args, **kwargs):
        """
        sendto(data[, flags], address) -> count

        Like send(data, flags) but allows specifying the destination address.
        For IP sockets, the address is a pair (hostaddr, port).
        """
        pass

    def setblocking(self, flag):  # real signature unknown; restored from __doc__
        """
        setblocking(flag)

        Set the socket to blocking (flag is true) or non-blocking (false).
        setblocking(True) is equivalent to settimeout(None);
        setblocking(False) is equivalent to settimeout(0.0).
        """
        pass

    # real signature unknown; restored from __doc__
    def setsockopt(self, level, option, value):
        """
        setsockopt(level, option, value)

        Set a socket option.  See the Unix manual for level and option.
        The value argument can either be an integer or a string.
        """
        pass

    def settimeout(self, timeout):  # real signature unknown; restored from __doc__
        """
        settimeout(timeout)

        Set a timeout on socket operations.  'timeout' can be a float,
        giving in seconds, or None.  Setting a timeout of None disables
        the timeout feature and is equivalent to setblocking(1).
        Setting a timeout of zero is the same as setblocking(0).
        """
        pass

    def shutdown(self, flag):  # real signature unknown; restored from __doc__
        """
        shutdown(flag)

        Shut down the reading side of the socket (flag == SHUT_RD), the writing side
        of the socket (flag == SHUT_WR), or both ends (flag == SHUT_RDWR).
        """
        pass

    def __getattribute__(self, name):  # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    @staticmethod  # known case of __new__
    def __new__(S, *more):  # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    family = property(
        lambda self: object(),
        lambda self,
        v: None,
        lambda self: None)  # default
    """the socket family"""

    proto = property(
        lambda self: object(),
        lambda self,
        v: None,
        lambda self: None)  # default
    """the socket protocol"""

    timeout = property(
        lambda self: object(),
        lambda self,
        v: None,
        lambda self: None)  # default
    """the socket timeout"""

    type = property(
        lambda self: object(),
        lambda self,
        v: None,
        lambda self: None)  # default
    """the socket type"""


socket = SocketType


class timeout(error):
    # no doc

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass


# variables with complex values

CAPI = None  # (!) real value is ''
