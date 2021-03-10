import socket
import time

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(("192.168.56.101",8005))
client.send(b"Hello from A")

# time.sleep(1)

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("0.0.0.0",8005))
msg = server.recvfrom(16)
print(msg)