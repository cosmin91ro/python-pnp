import socket
sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sSocket.bind(("0.0.0.0",8005))
sSocket.listen()
while True: 
    client, addr = sSocket.accept()
    sum = 0
    while True:
        val = client.recv(128).decode("utf-8")
        if val == "#":
            client.send(f"{sum}".encode("utf-8"))
            break
        else:
            sum += int(val) 
    client.close()