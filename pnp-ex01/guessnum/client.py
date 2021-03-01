import socket

playerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
playerSocket.connect(("localhost",8005))
playerSocket.send(bytes(input("Enter number: "),"utf-8"))
print(playerSocket.recv(128).decode("utf-8"))