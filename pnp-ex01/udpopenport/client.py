import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(("localhost",8005))
client.sendto(b"Hello")
print(client.recv(128).decode("utf-8"))
client.send(b"Hello again")
print(client.recv(128).decode("utf-8"))