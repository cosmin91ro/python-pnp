import socket


while True: 
    input("Press enter to get a ticket code:")
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("localhost",8005))
    client.send("GET /insert HTTP/1.1\r\n\r\n".encode("utf-8")) 
    parts = client.recv(1024).decode("utf-8").splitlines()
    description = parts[0].split(" ")
    statusCode = description[1]
    if statusCode != "200":
        print("Invalid server response")
    else:
        ticketToken = parts[len(parts)-1]
        print("Your ticket code: ", ticketToken) 
    client.close()