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


def getStationId(_station):
    df = pd.read_csv("6_weatherAPI/weatherData/stations.txt", skiprows=17)
    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    station = df.loc[df["STANAME"] == str(_station).upper()]["STAID"].squeeze()

    return station


def getTemperature(_station, _date):
    station = getStationId(_station)

    fileToRead = "TG_STAID" + str(station).zfill(6) + ".txt"

    df = pd.read_csv(f"6_weatherAPI/weatherData/{fileToRead}", skiprows=20)
    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    temperature = df.loc[df["DATE"] == int(_date)]["TG"].squeeze() / 10.0

    return temperature


@app.route("/api/<station>/<date>")
def api(station, date):

    temperature = getTemperature(station, date)
    return {"station": station, "date": date, "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
