import requests
import json

def post_request(url, data):
    print("Request sent to", url, " with data : ", data)
    r = requests.post(url = url, data = data)
    if(r.status_code == 200):
        print("Server answers : ", r.text)
    else:
        print("Something went terribly wrong.")
