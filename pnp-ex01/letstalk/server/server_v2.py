import socket
import threading
import time

def broadcast(msg):
    for user, sock in users.items(): 
        sock.send(msg.encode("utf-8"))


# Thread to send broadcast messages to advertise the char room
class Advertisor(threading.Thread):
    client = name = None
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    def run(self):
        while True:
            print("Broadcast sent")
            self.client.connect(("255.255.255.255",8005))
            self.client.send(b"8005|" + self.name.encode("utf-8"))
            time.sleep(5)


# Each client connection is handled in a separate thread
class ChatListener(threading.Thread):
    username = ""
    conn = None
    def __init__(self, username, conn):
        super().__init__()
        self.username = username
        self.conn = conn

    def run(self): 
        while True:
            msg = self.conn.recv(1024).decode("utf-8")
            print(f"User {self.username} say {msg}") 
            if msg == "/exit": 
                del users[self.username]
                self.conn.close()
                broadcast(f"User {self.username} left the room")
                print(f"User {self.username} left")
                break
            else:
                broadcast(f"{self.username}: {msg}")

def accept(sock):
    conn, addr = sock.accept() 
    username = conn.recv(1024).decode("utf-8")
    users[username] = conn
    
    chat = ChatListener(username, conn)
    chat.daemon = True
    chat.start()
    
    print(f"User {username} has entered room")
    broadcast(f"User {username} has entered room")

# Dict to hold connected users
users = {}

roomName = input("Enter chat room name: ")

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ss.bind(("0.0.0.0",8005))
ss.listen()
print("Chat server running...")

adv = Advertisor(roomName)
adv.daemon = True
adv.start()

while True:
    accept(ss)

