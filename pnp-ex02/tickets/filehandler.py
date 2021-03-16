import os 
import datetime
import shutil

TicketFileName = "tickets.txt"
LastTicket = -1 
FileLocked = False
def getlineparts(line):
    return line.split("|")

def getlastticket(): 
    global LastTicket
    if(LastTicket > 0):
        return LastTicket 
    global FileLocked
    while FileLocked: pass
    FileLocked = True 
    global TicketFileName
    try:
        ticketfile = open(TicketFileName,"r") 
        ln = ticketfile.readline()
        while ln != "": 
            id,_,_ = getlineparts(ln) 
            ln = ticketfile.readline() 
        ticketfile.close()
        LastTicket = int(id)
        FileLocked = False
        return LastTicket
    except:
        print("Tickets file does not exist") 
        LastTicket = 0
        FileLocked = False
        return LastTicket

def insertticket():
    newTicketId = getlastticket() + 1
    global FileLocked
    global LastTicket
    global TicketFileName
    while FileLocked: pass
    FileLocked = True 
    ticketfile = open(TicketFileName, "a")
    print(f"Inserting ticket {newTicketId}")
    ticketfile.write(f"{newTicketId}|{datetime.datetime.now()}|0\n")   
    ticketfile.close() 
    FileLocked = False
    LastTicket = newTicketId
    return newTicketId

def checkout(code):
    ticket_valid = False
    global TicketFileName
    global FileLocked
    while FileLocked: pass
    FileLocked = True 
    try: 
        ticketfile  = open(TicketFileName, "r")
    except:
        print("ERROR: Cannot open the tickets file")
        FileLocked = False
        return False
    tmpfile     = open("ticketstmp.txt", "w")
    ln = ticketfile.readline()
    while ln: 
        parts = getlineparts(ln)
        if int(parts[0]) == code:
            if parts[2].strip() == "0":
                tmpfile.writelines(f"{parts[0]}|{parts[1]}|1\n")
                ticket_valid = True
            else:
                tmpfile.writelines(ln)
        else:
            tmpfile.writelines(ln)
        ln = ticketfile.readline() 
    ticketfile.close()
    tmpfile.close()
    shutil.move("ticketstmp.txt",TicketFileName)
    FileLocked = False
    return ticket_valid