import socket

sServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sServer.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sServer.bind(("localhost",8005))
sServer.listen()
client,addr = sServer.accept()
client.send(b"Enter number 1: ")
firstNumber = int(client.recv(32).decode("utf-8"))
client.send(b"Enter number 2: ")
secondNumber = int(client.recv(32).decode("utf-8"))
res = format(firstNumber + secondNumber)
client.send(bytes(res,"utf-8"))
