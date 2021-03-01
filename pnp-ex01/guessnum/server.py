import socket
import random

sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sSocket.bind(("localhost",8005))
sSocket.listen()
userSocket,addr = sSocket.accept()

playernumber    = int(userSocket.recv(128).decode("utf-8"))
compnumber      = random.randint(1,5)

if playernumber == compnumber:
    userSocket.send(b"Nice! I guessed that number")
else:
    userSocket.send(f"Wrong! I guessed {compnumber} and you typed {playernumber}".encode("utf-8"))
