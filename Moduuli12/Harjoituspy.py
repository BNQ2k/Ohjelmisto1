import requests
nimi = input("Mikä sinun nimesi on: ")
pyyntö = f"https://api.agify.io?name={nimi}"
try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        print(vastaus.json()["age"])
except Exception as e:
    print(e)