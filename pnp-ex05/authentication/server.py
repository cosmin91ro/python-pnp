import socket
import threading
import base64
import authenticator

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
        print(request)
        parts = request.split("\r\n")
        description = parts[0].split(" ")
        resource = description[1].replace("/","")
        method = description[0]
        authRequestHeader = False
        for h in parts:
            if ":" in h and h.split(":")[0] == "Authorization":
                authRequestHeader = h

        code = "200 OK"
        body = authResponseHeader = ""
        
        if(not resource):
            body = "This is not a valid page"
            code = "404 Not Found"
        else:  
            authenticated = False
            if resource == "protected":
                if authRequestHeader:
                    credentialsBase64 = authRequestHeader.split(" ")[-1]
                    credentials = base64.b64decode(credentialsBase64).decode("ascii")
                    uname = credentials.split(":")[0]
                    password = credentials.split(":")[1]
                    if authenticator.authenticated(uname, password):
                        authenticated = True
                    
                if not authRequestHeader or not authenticated:
                    authResponseHeader = 'www-authenticate: Basic realm="portal"\r\n'
                    code = "401 Unauthorized"

            elif resource == "public":
                authenticated = True

            if authenticated:   
                with open(resource) as fin:
                    body = fin.read()
        
        print(F"Returning {body}")
        protocol = "HTTP/1.1"
        self.sock.send(f"{protocol} {code}\r\n{authResponseHeader}\Content-Type: text/html\r\nConnection: Close\r\n\r\n{body}".encode("utf-8")) 
        self.sock.close()


sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sSocket.bind(("0.0.0.0",8005))
sSocket.listen()

while True:
    accept(sSocket)