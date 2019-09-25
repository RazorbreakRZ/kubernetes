import requests

PROTOCOL = "http"
HOST = "localhost"
PORT = "5000"
ENDPOINT = "/api/v1/random"

def getRandomValue():  
    URL = PROTOCOL + "://" + HOST + ":" + PORT + ENDPOINT
    PARAMS = {}
    response = requests.get(url = URL, params = PARAMS)
    data = response.json()
    return data["value"]

print " ~ Loaded mathematics service"