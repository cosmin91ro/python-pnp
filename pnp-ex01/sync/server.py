import socket
sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sSocket.bind(("localhost",8005)) 
sSocket.listen()
conn, addr = sSocket.accept() 
conn.send(b"Hello and welcome")
print("Client said: ", conn.recv(256).decode("utf-8"))  
conn.send(b"Thank you")
sSocket.close()


