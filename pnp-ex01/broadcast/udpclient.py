import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(("255.255.255.255",8005))
client.send(b"Hello All")