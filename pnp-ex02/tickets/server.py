import socket
import selectors 
import filehandler

def accept(sock):
    conn,addr = sock.accept()
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(sock):
    request = sock.recv(1024).decode("utf-8") 
    parts = request.split("\r\n")

    bodyData = parts[len(parts)-1]  

    description = parts[0].split(" ")
    filename = description[1].replace("/","")
    method = description[0]
    code = "200 OK"
     
    if(not filename):
        body = "This is not a valid page"
        code = "404 Not Found"
    else:  
        if filename == "insert":
            body = filehandler.insertticket()
        elif filename == "checkout": 
            if method.lower() != "post":
                body = "You must use post method on this page"
                code = "405 Method Not Allowed" 
            elif not bodyData: 
                body = "Not a valid body"
                code = "400 Bad Request"
            else: 
                ticketId = -1 
                print(f"Validating ticket {bodyData}")
                try:
                    ticketId = int(bodyData)
                except:
                    body = "Not a valid ticket code"
                    code = "400 Bad Request"
                if ticketId == -1:
                    body = "Not a valid ticket code"
                    code = "400 Bad Request"
                else:
                    body = int(filehandler.checkout(ticketId))
        else:
            body = "Not a valid command"
            code = "400 Bad Request"
        

         
            

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