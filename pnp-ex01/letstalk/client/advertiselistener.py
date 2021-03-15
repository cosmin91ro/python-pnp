import threading
import socket

# Thread to listen for chat rooms advertisements
class AdvertiseListener(threading.Thread):
    udpAvd = None
    rooms = {}
    stop = False
    def __init__(self):
        super().__init__()
        self.udpAdv = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.udpAdv.bind(("0.0.0.0",8005))
    def run(self):
        while True:
            if self.stop:
                break
            data, addr = self.udpAdv.recvfrom(16)
            chatIP = addr[0]
            if chatIP in self.rooms: continue
            chatPort = chatName = None
            if "|" in data.decode("utf-8"):
                chatPort = data.decode("utf-8").split("|")[0]
                chatName = data.decode("utf-8").split("|")[1]
            self.rooms[chatIP] = {"id": len(self.rooms.items()) + 1, "port": chatPort, "name": chatName}