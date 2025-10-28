import requests

pyyntö = "https://api.chucknorris.io/jokes/random"

input("Paina enter kuullaksesi Chuck Norris -vitsin:")
vastaus = requests.get(pyyntö)
json_vastaus = vastaus.json()
print(json_vastaus["value"])

