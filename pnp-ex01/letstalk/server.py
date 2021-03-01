import socket
import selectors 


ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ss.bind(("localhost",8005))
ss.listen()
ss.setblocking(False) 

users = {}

def broadcast(msg,sender = None):
    for sock in users: 
        if sender and sock == sender:
            continue
        sock.send(msg.encode("utf-8"))

def accept(sock):
    conn, addr = sock.accept() 
    conn.setblocking(True)
    username = conn.recv(1024).decode("utf-8")
    conn.setblocking(False) 
    users[conn] = username
    print(f"User {username} has entered room")
    broadcast(f"User {username} has entered room",conn)
    sel.register(conn, selectors.EVENT_READ, read)

def read(sock): 
    msg = sock.recv(1024).decode("utf-8")
    username = users[sock] 
    print(f"User {username} say {msg}") 
    if msg == "/exit": 
        del users[sock]
        sock.close()
        broadcast(f"User {username} left the room")
        print(f"User {username} left")
    else:
        broadcast(f"{username}: {msg}")

sel = selectors.DefaultSelector() 
sel.register(ss,selectors.EVENT_READ,accept)
print("Chat server running...")
while True:
    events = sel.select()
    for key, mask in events:
        key.data(key.fileobj)

