import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",8005))
while True:
    val = input("Enter number: ") 
    if val == "":
        client.send("#".encode("utf-8"))
        print(client.recv(128).decode("utf-8"))
        break
    else:
        client.send(val.encode("utf-8"))
client.close()