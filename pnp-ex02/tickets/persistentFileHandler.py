import os 
import datetime
import json

DATABASEFILE = "database.json"


def deserialize():
    tickets = {}
    if os.path.exists(DATABASEFILE) and os.stat(DATABASEFILE).st_size > 0:
        fin = open(DATABASEFILE)
        tickets = json.load(fin)
        fin.close()
    return tickets


def serialize(tickets):
    fout = open(DATABASEFILE, "w")
    json.dump(tickets, fout)
    fout.close()


def insertticket():
    tickets = deserialize()
    newTicketId = len(tickets.items()) + 1
    tickets[newTicketId] = {
        "date": str(datetime.datetime.now()),
        "used": False
    }
    serialize(tickets)
    return newTicketId


def checkout(id):
    tickets = deserialize()
    ticketValid = False
    if id in tickets.keys():
        if not tickets[id]["used"]:
            tickets[id]["used"] = True
            ticketValid = True
    serialize(tickets)
    return ticketValid
