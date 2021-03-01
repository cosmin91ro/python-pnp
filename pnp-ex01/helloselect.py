import socket
import select 

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ss.bind(("localhost",8005))
ss.listen()
ss.setblocking(False) 

inputs      = [ss]
outputs     = [] 
clients     = {} 
total       = 0

while True:
    r,w,e = select.select(inputs,outputs,inputs)
    for sock in r:
        if sock is ss:
            cc,addr = sock.accept()
            cc.setblocking(False) 
            inputs.append(cc)
            clients[cc] = []
            outputs.append(cc)
        else:
            total+=1
            sock.recv(1024)
            clients[sock].append(f"HTTP/1.1 200 OK\r\n\r\nTotal {total}")
            print(f"Total {total}",end="\r")

    for sock in w:
        if sock is not ss: 
            if clients[sock]:
                msg = clients[sock].pop(0)
                sock.send(msg.encode("utf-8"))
                outputs.remove(sock)
                inputs.remove(sock)
                del clients[sock]
                sock.close()