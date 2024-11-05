import flask

app = flask.Flask(__name__, template_folder="templates",
                  static_folder="static")


@app.route("/")
def home():
    return flask.render_template("home.html")


@app.route("/api/<station>/<date>")
def api(station, date):
    return {
        "station": station,
        "date": date,
        "temperature": 40
    }


if __name__ == "__main__":
    app.run(debug=True)
