import flask

app = flask.Flask("flaskApp", template_folder="6_weatherAPI/templates")


@app.route("/")
def home():
    return flask.render_template("home.html")


app.run(debug=True)
