import flask

app = flask.Flask("flaskApp",
                  template_folder="6_weatherAPI/templates",
                  static_folder="6_weatherAPI/static")


@app.route("/")
def home():
    return flask.render_template("home.html")


app.run(debug=True)
