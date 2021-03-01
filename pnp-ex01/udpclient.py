import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(("localhost",8005))
client.send(b"Hello world")