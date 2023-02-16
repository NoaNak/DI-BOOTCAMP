import requests
import time

url = "https://api.chucknorris.io/jokes/categories"

while True:
    response = requests.get(url) 

    print(response)

    data = response.json()

    print(data)

    time.sleep(1)

    