import socket
import threading


def broadcast(msg):
    for user, sock in users.items(): 
        sock.send(msg.encode("utf-8"))


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
    #conn.setblocking(True)
    username = conn.recv(1024).decode("utf-8")
    #conn.setblocking(False) 
    users[username] = conn
    
    chat = ChatListener(username, conn)
    chat.daemon = True
    chat.start()
    
    print(f"User {username} has entered room")
    broadcast(f"User {username} has entered room")


# Dict to hold connected users
users = {}

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ss.bind(("localhost",8005))
ss.listen()
print("Chat server running...")

while True:
    accept(ss)

