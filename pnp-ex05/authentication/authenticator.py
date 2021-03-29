

USERNAME = "johnny"
PASSWORD = "passw0rd"  

def authenticated(uname, password):
    if uname == USERNAME and password == PASSWORD:
        return True
    return False