import socket
import time

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("0.0.0.0",8005))
msg = server.recvfrom(16)
print(msg)

# time.sleep(1)

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(("192.168.56.1",8005))
client.send(b"Hello from B")