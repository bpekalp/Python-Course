import flask
import pandas as pd

app = flask.Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def home():
    df = pd.read_csv("bonus/dictionaryAPI/datas/dictionary.csv")
    words = df.to_dict(orient="records")
    return flask.render_template("home.html", words=words)


@app.route("/api/word/<id>")
def api(id):
    df = pd.read_csv("bonus/dictionaryAPI/datas/dictionary.csv")

    row = df.loc[df["ID"] == int(id)]

    if not row.empty:
        word = row["Word"].values[0]
        description = row["Description"].values[0]

    result = {"id": int(id), "word": word, "description": description}

    return result


if __name__ == "__main__":
    app.run(debug=True)
