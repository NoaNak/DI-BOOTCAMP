import requests
import time

url = "http://api.open-notify.org/iss-now.json"

while True:
    response = requests.get(url) # get connect the url 

    print(response)

    data = response.json()

    print(data["iss_position"])

    time.sleep(1) # make the programm sleep in 1 sec