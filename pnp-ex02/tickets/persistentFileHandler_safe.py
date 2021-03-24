import os 
import datetime
import json
import threading

DATABASEFILE = "database.json"
locker = threading.Lock()

def deserialize():
    tickets = {}
    if os.path.exists(DATABASEFILE) and os.stat(DATABASEFILE).st_size > 0:
        # locker.acquire()
        fin = open(DATABASEFILE)
        tickets = json.load(fin)
        fin.close()
        # locker.release()
    return tickets


def serialize(tickets):
    # locker.acquire()
    fout = open(DATABASEFILE, "w")
    json.dump(tickets, fout)
    fout.close()
    # locker.release()

def insertticket():
    try:
        locker.acquire()
        tickets = deserialize()
        newTicketId = len(tickets.items()) + 1
        tickets[newTicketId] = {
            "date": str(datetime.datetime.now()),
            "used": False
        }
        serialize(tickets)
        locker.release()
        return newTicketId
    except Exception as ex:
        print(f"ERROR in {threading.currentThread().getName()}: {ex}")


def checkout(id):
    tickets = deserialize()
    ticketValid = False
    if id in tickets.keys():
        if not tickets[id]["used"]:
            tickets[id]["used"] = True
            ticketValid = True
    serialize(tickets)
    return ticketValid
