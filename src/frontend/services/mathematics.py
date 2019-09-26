import requests
from frontend import cfg

def getRandomValue():
    url = cfg["externalServices"]["mathematics"]["url"] + cfg["externalServices"]["mathematics"]["endpoints"]["random"]
    response = requests.get(url)
    data = response.json()
    return data["value"]

print " ~ Loaded mathematics service"