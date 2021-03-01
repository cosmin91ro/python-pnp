import socket 

cSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cSocket.connect(("localhost",8005))

cSocket.send(b"Hey man, what's up?") 
cSocket.sendall(b"Are you there?") 
 
cSocket.close()