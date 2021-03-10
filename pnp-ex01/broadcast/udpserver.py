import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("0.0.0.0",8005))
msg = server.recvfrom(16)
print(msg)