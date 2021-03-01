import socket
import threading 
import sys

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

class ChatListener(threading.Thread):
    username = ""
    def __init__(self, username):
        super().__init__()
        self.username = username
    def run(self): 
        client.connect(("127.0.0.1",8005))
        client.send(self.username.encode("utf-8"))
        while True:
            res = client.recv(1024).decode("utf-8")
            if res != "":
                print(res)     


username = input("Enter username: ")    

chat = ChatListener(username)
chat.daemon = True
chat.start()
while True:
    print("Enter message: ")
    msg = input()  
    client.send(msg.encode("utf-8"))
    if msg == "/exit":
        print("Bye bye")
        sys.exit()
        break


