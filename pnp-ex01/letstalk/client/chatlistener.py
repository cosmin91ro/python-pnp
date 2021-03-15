import threading

# Thread to listen for chat messages
class ChatListener(threading.Thread):
    username = ip = sock = None
    def __init__(self, username, ip, sock):
        super().__init__()
        self.username = username
        self.ip = ip
        self.sock = sock
    def run(self): 
        self.sock.connect((self.ip,8005))
        self.sock.send(self.username.encode("utf-8"))
        while True:
            res = self.sock.recv(1024).decode("utf-8")
            if res != "":
                print(f"\r\n{res}")   
                print("Enter message: ", end="", flush=True)  