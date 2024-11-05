import flask

app = flask.Flask("flaskApp",
                  template_folder="6_weatherAPI/templates",
                  static_folder="6_weatherAPI/static")


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


app.run(debug=True)
