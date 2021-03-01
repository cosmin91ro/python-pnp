import socket 

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("localhost",8005)) 
data = server.recvfrom(128)
print(data[0].decode("utf-8")) 

server.connect(data[1])
server.send(b"Hello from me also")
data = server.recvfrom(128)
print(data[0].decode("utf-8"))
server.send(b"Woow..we speak on the edge")

