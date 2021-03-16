import socket
import threading 
import memoryhandler
import filehandler

def accept(sock):
    conn, addr = sock.accept()
    hh = HttpHandler(conn)
    hh.daemon = True
    hh.start()

class HttpHandler(threading.Thread):
    sock = None
    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        request = self.sock.recv(1024).decode("utf-8") 
        parts = request.split("\r\n")

        bodyData = parts[len(parts)-1]  

        description = parts[0].split(" ")
        resource = description[1].replace("/","")
        method = description[0]
        code = "200 OK"
        
        if(not resource):
            body = "This is not a valid page"
            code = "404 Not Found"
        else:  
            if resource == "insert":
                body = memoryhandler.insertticket()
            elif resource == "checkout":
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
                        body = memoryhandler.checkout(ticketId)
            else:
                body = "Not a valid command"
                code = "400 Bad Request"
        
            print(F"Returning {body}")
            protocol = "HTTP/1.1"
            self.sock.send(f"{protocol} {code}\r\nContent-Type: text/html\r\nConnection: Close\r\n\r\n{body}".encode("utf-8")) 
            self.sock.close()


sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sSocket.bind(("localhost",8005))
sSocket.listen()

while True:
    accept(sSocket)