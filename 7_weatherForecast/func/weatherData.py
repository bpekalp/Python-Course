import requests
import json

with open("secrets/weatherapi.json") as file:
    credentials = file.read()

credentials = json.loads(credentials)
email = credentials["email"]
apikey = credentials["apikey"]


def getData(location, forecastDays, weatherOpt):
    url = (
        f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={apikey}"
    )
    response = requests.get(url)
    weatherData = response.json()
    return weatherData


if __name__ == "__main__":
    weather = getData("Istanbul", 1, 1)
    print(weather)
