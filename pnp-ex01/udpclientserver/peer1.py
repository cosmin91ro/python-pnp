import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("localhost",8005)) 

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

i = 0
while True:
    data = server.recv(128)
    print(data.decode("utf-8"))
    try:
        client.send(f"Peer 1 response # {i}".encode("utf-8"))
    except:
        client.connect(("localhost",8006))
        client.send(f"Peer 1 response # {i}".encode("utf-8"))
    i+=1


