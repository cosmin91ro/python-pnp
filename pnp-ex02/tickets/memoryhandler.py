import os 
import datetime

tickets = {}

def insertticket():
    newTicketId = len(tickets.items())+ 1
    tickets[str(newTicketId)] = {
        "date": datetime.datetime.now(),
        "used": False
    }
    return newTicketId

def checkout(id):
    if id in tickets.keys():
        if not tickets[id]["used"]:
            tickets[id]["used"] = True
            return True
    return False
