import socket

multicast_group = ('224.0.0.1', 1001)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
sent = sock.sendto(b'Hey all!', multicast_group)