import requests

city_name = input('Anna kaupungin nimi: ').capitalize()
API_key = "7221f4d4f4361a21565ba8606a55c7ab"
# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
lang = 'fi'

pyyntö = (f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang={lang}")

try:
    vastaus = requests.get(pyyntö)
    #print("Status code", vastaus.status_code)
    if vastaus.status_code==200:
        data = vastaus.json()
        #print(json.dumps(data, indent=2))
        print(f"Sää kohteessa {city_name}: {data["weather"][0]["description"]}, lämpötila "
              f" {data["main"]["temp"]} astetta celsiusta.")
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")