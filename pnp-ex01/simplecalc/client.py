import socket

cSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cSocket.connect(("localhost",8005))
firstNum = input(cSocket.recv(256).decode("utf-8"))
cSocket.send(bytes(firstNum,"utf-8"))
secondNum = input(cSocket.recv(256).decode("utf-8"))
cSocket.send(bytes(secondNum,"utf-8"))
print("Result is: ", cSocket.recv(256).decode("utf-8"))