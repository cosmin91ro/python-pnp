import socket

sClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sClient.connect(("127.0.0.1",8005))
sClient.close()