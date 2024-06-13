import time

import requests
from requests.exceptions import ConnectionError

url = "http://127.0.0.1:8000/add"

payload = {"a": 10, "b": 5}


def faire_requete():
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.status_code)


try:
    faire_requete()
except ConnectionError:
    print("Etes vous certain de bien être connecté à internet ?")
except ConnectionResetError:
    time.sleep(2)
    try:
        faire_requete()
    except ConnectionError:
        print("La connection a échoué durant le calcul")
