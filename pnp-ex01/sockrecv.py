import socket
import time

sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sSocket.bind(("localhost",8005))
sSocket.listen()
print("Listening for connection: ")
conn, addr = sSocket.accept() 

print("Connection received from ", addr)
data = conn.recv(1024)

print("Message from client: \n")
time.sleep(2)  
print(data)
conn.close()
sSocket.close()