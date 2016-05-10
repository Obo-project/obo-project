import requests
import json
from audio import play

def post_request(url, data):
    print("Request sent to", url, " with data : ", data)
    r = requests.post(url = url, data = data)
    if(r.status_code == 200):
        print("Server answers : ", r.text)
        if(r.text.find("yes") != -1):
            play('sons/coin_coin_fort.wav')
        elif(r.text.find("Non existant") != -1):
            play('sons/coin_coin_inexistant_fort.wav')
        else:
            play('sons/coin_coin_faux_fort.wav')
    else:
        print("Something went terribly wrong.")
