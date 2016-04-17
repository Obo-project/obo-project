import requests

def post_request(url, data):
    r = requests.post(url = url, data = data)
    if(r.status_code == 200):
        print("Good for you\n" + r.text)
    else:
        print("Something went terribly wrong")
