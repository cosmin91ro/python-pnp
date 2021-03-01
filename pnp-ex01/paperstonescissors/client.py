import socket

playerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
playerSocket.connect(("localhost",8005))
print("Choose object: ")
print(playerSocket.recv(1024).decode("utf-8"))
selectedObject = input("Your selection: ") 
playerSocket.send(bytes(selectedObject,'utf-8'))
print(playerSocket.recv(1024).decode("utf-8"))
