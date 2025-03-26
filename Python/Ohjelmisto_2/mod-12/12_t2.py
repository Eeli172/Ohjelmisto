import requests

api_key = "55c711f6d57383bc1d3e3c07b019180d"


location = input("Sijainti: ")
request = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={api_key}"
try: 
    answer = requests.get(request)
    if answer.status_code == 200:
        answer_json = answer.json()[0]
        print(f'\nHaetaan säätiedot seuraavaan sijaintiin: {answer_json["name"]}, {answer_json["country"]}\n')
        lat = answer_json["lat"]
        lon = answer_json["lon"]

    else: print(answer.status_code)

except requests.exceptions.RequestException as e:
    print(f"Hakua ei voitu suorittaa. {answer.status_code}")


request = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}"
try: 
    answer = requests.get(request)
    if answer.status_code == 200:
        answer_json = answer.json()
        weather = f'Sää:          {answer_json["weather"][0]["main"]}\n'
        weather += f'Kuvaus:       {answer_json["weather"][0]["description"]}\n'
        weather += f'Lämpötila:    {answer_json["main"]["temp"]} °C\n'
        weather += f'Tuntuu kuin:  {answer_json["main"]["feels_like"]} °C'
        print(weather)
    else: print(answer.status_code)

except requests.exceptions.RequestException as e:
    print(f"Hakua ei voitu suorittaa. {answer.status_code}")
