import socket
import threading
import time

class Heartbeat(threading.Thread):
    def run(self):
        while True:
            time.sleep(5)
            server.sendto(f"{int(time.time())}".encode("utf-8"),clientaddr)
 
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("localhost",8005)) 
data = server.recvfrom(128)
clientaddr = data[1] 
Heartbeat().start() 
while True:
    data = server.recvfrom(128)
    print(data[0].decode("utf-8"))


