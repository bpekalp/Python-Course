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
    observations = 8 * forecastDays
    forecast = weatherData["list"][:observations]

    if weatherOpt == "Temperature":
        elements = [element["main"]["temp"] for element in forecast]

    elif weatherOpt == "Sky":
        elements = [element["weather"][0]["main"] for element in forecast]

    return forecast


if __name__ == "__main__":
    temperatures = getData("Istanbul", 2, "Temperature")
    print(temperatures)

    sky = getData("Istanbul", 2, "Sky")
    print(sky)
