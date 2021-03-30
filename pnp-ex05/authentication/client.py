import urllib.request as httpclient
import sys
import re
import base64
from urllib.parse import urlparse
from urllib.error import HTTPError

url = 'http://localhost:8005/protected'  # + sys.argv[1]


req = httpclient.Request(url)
try:
    response = httpclient.urlopen(req).read()
    print(response)
except HTTPError as e:    
    if hasattr(e, 'code') and e.code == 401:
        # we got an error - but not a 401 error
        print("This page requires authentication.")

        authHeader = e.headers['www-authenticate']
        # this gets the www-authenticate line from the headers
        # which has the authentication scheme and realm in it
    
        if " " in authHeader:
            # here we've extracted the scheme from the header
            scheme = authHeader.split(" ")[0]
        else:
            print("Auth Header is malformed")
            sys.exit(-1)

        if scheme.lower() != 'basic':
            print('This example only works with BASIC authentication.')
            sys.exit(1)

        username = input("Username: ")
        password = input("Password: ")
        base64string = base64.b64encode(f"{username}:{password}".encode("ascii")).decode("ascii")
        authheader =  "Basic %s" % base64string
        req.add_header("Authorization", authheader)
        try:
            handle = httpclient.urlopen(req)
        except HTTPError as e:
            # here we shouldn't fail if the username/password is right
            print("It looks like the username or password is wrong.")
            sys.exit(1)
        response = handle.read()
        print(response)