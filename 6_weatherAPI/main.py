import flask
import pandas as pd

app = flask.Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def home():
    df = pd.read_csv("6_weatherAPI/weatherData/stations.txt", skiprows=17)

    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    stations = df[["STAID", "STANAME"]].to_dict(orient="records")
    return flask.render_template("home.html", stations=stations)


def getStationName(_station):
    df = pd.read_csv("6_weatherAPI/weatherData/stations.txt", skiprows=17)

    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    station = str(df.loc[df["STAID"] == int(_station)]["STANAME"].squeeze()).title()
    return station


def getAllTemperature(_station):
    fileToRead = "TG_STAID" + str(_station).zfill(6) + ".txt"

    df = pd.read_csv(
        f"6_weatherAPI/weatherData/{fileToRead}", skiprows=20, parse_dates=["    DATE"]
    )

    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    df = df[["DATE", "TG"]]
    df["TG"] = df["TG"] / 10.0

    df = df.to_dict(orient="records")
    return df


@app.route("/api/<station>")
def station(station):
    temperatures = getAllTemperature(station)
    stationName = getStationName(station)
    return {
        "station": station,
        "stationName": stationName,
        "temperatures": temperatures,
    }


def getDateTemperature(_station, _date):
    fileToRead = "TG_STAID" + str(_station).zfill(6) + ".txt"

    df = pd.read_csv(
        f"6_weatherAPI/weatherData/{fileToRead}", skiprows=20, parse_dates=["    DATE"]
    )

    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    temperature = df.loc[df["DATE"] == _date]["TG"].squeeze() / 10.0
    return temperature


@app.route("/api/<station>/<date>")
def stationDate(station, date):
    temperature = getDateTemperature(station, date)
    stationName = getStationName(station)
    return {
        "station": station,
        "stationName": stationName,
        "date": date,
        "temperature": temperature,
    }


def getFromToTemperature(_station, _fromDate, _toDate):
    fileToRead = "TG_STAID" + str(_station).zfill(6) + ".txt"

    df = pd.read_csv(
        f"6_weatherAPI/weatherData/{fileToRead}", skiprows=20, parse_dates=["    DATE"]
    )

    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    df = df[["DATE", "TG"]]
    df["TG"] = df["TG"] / 10.0

    mask = (df["DATE"] >= pd.to_datetime(_fromDate)) & (
        df["DATE"] <= pd.to_datetime(_toDate)
    )
    df = df.loc[mask]

    df = df.to_dict(orient="records")
    return df


@app.route("/api/<station>/<fromDate>/<toDate>")
def stationFromDateToDate(station, fromDate, toDate):
    temperatures = getFromToTemperature(station, fromDate, toDate)
    stationName = getStationName(station)
    return {
        "station": station,
        "stationName": stationName,
        "temperatures": temperatures,
        "fromDate": fromDate,
        "toDate": toDate,
    }


if __name__ == "__main__":
    app.run(debug=True)
