import os 
import datetime
import shutil

tickets = {}

def insertticket():
    newTicketId = len(tickets.items())
    tickets[newTicketId] = {
        "date": datetime.datetime.now(),
        "valid": True
    }
    return newTicketId

def checkout(id):
    if id in tickets.keys():
        if tickets[id]["valid"]:
            tickets[id]["valid"] = False
            return True
    return False
