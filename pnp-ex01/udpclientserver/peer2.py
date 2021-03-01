import socket
from threading import Thread as t

class Receiver(t):
    def run(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        server.bind(("localhost",8006))  
        while(True):
            print(server.recv(128).decode("utf-8"))

rec = Receiver()
rec.start()

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
client.connect(("localhost",8005))

for i in range(100000):
    client.send(f"Peer 1 # {i}".encode("utf-8"))