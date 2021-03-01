import socket
import selectors 

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ss.bind(("localhost",8005))
ss.listen()
ss.setblocking(False) 

total = 0

def accept(sock):
    conn, addr = sock.accept()
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(sock):
    global total
    total += 1
    print(sock.recv(1024))
    sock.send(f"HTTP/1.1 200 OK\r\n\r\nTotal requests: {total}".encode("utf-8")) 
    sel.unregister(sock)
    sock.close()

sel = selectors.DefaultSelector() 
sel.register(ss,selectors.EVENT_READ,accept)

while True:
    events = sel.select()
    for key, mask in events:
        key.data(key.fileobj)

