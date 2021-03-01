import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("localhost",8005))
msg = server.recvfrom(16)
print(msg)