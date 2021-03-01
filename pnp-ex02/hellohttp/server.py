import socket
import selectors

def accept(sock):
    conn,addr = sock.accept()
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(sock):
    request = sock.recv(1024).decode("utf-8") 
    parts = request.split("\r\n")
    description = parts[0].split(" ")
    filename = description[1].replace("/","")
    code = "200 OK"
    
    if(not filename):
        body = "This is not a valid page, my friend"
        code = "404 Not Found"
    else:
        body = filename
    

    protocol = "HTTP/1.1"
    sock.send(f"{protocol} {code}\r\nContent-Type: text/html\r\nConnection: Close\r\n\r\n{body}".encode("utf-8")) 
    sock.close()
    sel.unregister(sock)

sel = selectors.DefaultSelector()
sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sSocket.bind(("localhost",8005))
sSocket.listen()
sSocket.setblocking(False)
sel.register(sSocket, selectors.EVENT_READ, accept)


while True:
    evt = sel.select()
    for k,m in evt:
        k.data(k.fileobj)