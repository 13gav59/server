from threading import Thread
from requests import get

run = True
payload = 101
URL = ''

def sendGetRequests():
    while run:
        get(URL, params=payload)

while True:
    Thread(target=sendGetRequests).start()
