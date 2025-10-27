import requests
pyyntö = "https://api.chucknorris.io/jokes/random"
try:
        vastaus = requests.get(pyyntö)
        print(vastaus.json()["value"])
except Exception as e:
    print(e)