import requests
import json
from audio import play

def post_request(url, data):
    print("Request sent to", url, " with data : ", data)
    r = requests.post(url = url, data = data)
    if(r.status_code == 200):
        print("Server answers : ", r.text)
    else:
        print("Something went terribly wrong.")
    play('sons/coin_coin_fort.wav')
