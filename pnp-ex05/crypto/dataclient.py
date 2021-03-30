from typing import TextIO
import urllib.request as httclient
import json
from urllib.error import URLError

API_SERVER = "https://api1.binance.com/api/v3"

def test():
    try:
        httclient.urlopen(f"{API_SERVER}/ping")
        return True
    except URLError as err:
        print(f"ERROR: {err}")
        return False

def getInfo():
    try:
        resp = httclient.urlopen(f"{API_SERVER}/exchangeInfo").read()
        return json.loads(resp)
    except URLError as err:
        print(f"ERROR: {err}")

def getSymbols():
    symbols = []
    info = getInfo()
    if info != None:
        for symbol in info["symbols"]:
            symbols.append(symbol["symbol"])
    return symbols
    
def getTrades(symbol):
    try:
        response = httclient.urlopen(f"{API_SERVER}/trades?symbol={symbol}").read()
        return json.loads(response)
    except URLError as err:
        print(f"ERROR: {err}")
        return []




if __name__ == "__main__":
    # print(getSymbols())
    print(getTrades("BTCUSDT"))
    # print(test())