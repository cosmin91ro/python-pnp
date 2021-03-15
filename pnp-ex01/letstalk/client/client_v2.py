import socket
import threading 
import sys
import os
from advertiselistener import AdvertiseListener
from utils import *
from chatlistener import ChatListener

# main socket for the chat communication
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

chatServerIP = None

# Starting the advertise listener in a separate thread
# to keep the user input() in the main thread
adv = AdvertiseListener()
adv.daemon = True
adv.start()

# Loop to list the available chat rooms
# User enters the chat room ID he choose to join
# Loop ends when the user makes a valid choice
while True:
    os.system("cls")
    print("Available chat rooms:\n")
    for k,v in adv.rooms.items():
        print("{0}. Chat server {1} available on port {2}".format(v["id"], v["name"], v["port"]))
    
    id = input_with_timeout("Which room you want to join? ", 5)
    if id != None and id.isnumeric() and int(id) <= len(adv.rooms.items()):
        for k,v in adv.rooms.items():
            if int(id) == v["id"]: 
                chatServerIP = k
                adv.stop = True
                break
    if chatServerIP != None: break

if chatServerIP is not None:
    username = input("Enter username: ")    
    # Starting the chat listener in a separate thread
    # to keep the user input() in the main thread
    chat = ChatListener(username, chatServerIP, client)
    chat.daemon = True
    chat.start()

    # Infinite loop to handle the user chat messages
    while True:
        msg = input("Enter message: ")
        client.send(msg.encode("utf-8"))
        if msg == "/exit":
            print("Bye bye")
            sys.exit()

