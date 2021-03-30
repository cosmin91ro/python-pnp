import socket
import hashlib
import base64

def sendmsg(data): 
        msg = [0b10000001] 
        msg.append(len(data)) 
        full_msg = bytearray(msg) + data
        global sock
        sock.send(full_msg)

def parseframe(msgbts): 
    print("Msg fin and opcode:","{0:b}".format(msgbts[0]))  
    mask = msgbts[1]>>7
    print("Msg mask:","{0:b}".format(mask))  
    dataunmasked = bytearray()  
    if mask == 1:
        datalen = msgbts[1] - 128
        print("Msg len:","{0:b}".format(datalen)) 
        mask = msgbts[2:6]
        data = msgbts[6:6+datalen] 
        for i in range(datalen):
            decoded = data[i]^mask[i%4] 
            dataunmasked.append(decoded)
    else: 
        datalen = msgbts[1]
        print("Msg len:","{0:b}".format(datalen)) 
        dataunmasked = msgbts[2:2+datalen] 
 
    print("Clean message:")
    print(dataunmasked.decode("utf-8"))
    unmstring = dataunmasked.decode("utf-8") 
    sendmsg(f"Indeed {unmstring}".encode("utf-8"))

ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ser.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ser.bind(("localhost",8005))
ser.listen()
sock,addr = ser.accept()  
headers = sock.recv(1024).decode("utf-8").splitlines()
wsguid = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
hashedkey = "" 
for h in headers:
    kvp = h.split(":")
    if len(kvp) > 1:
        key = kvp[0].strip()
        val = kvp[1].strip()
        if key == 'Sec-WebSocket-Key':  
            fk = f"{val}{wsguid}" 
            fk = hashlib.sha1(fk.encode("utf-8"))  
            hashedkey = base64.encodebytes(fk.digest()).decode("utf-8")

sock.send(f"HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: {hashedkey}\r\n".encode("utf-8"))

while True:
    msg = sock.recv(1024).strip() 
    if msg: 
        msgbts = bytearray(msg)
        parseframe(msgbts)