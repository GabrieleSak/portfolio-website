"""
COLORS:
blue: #151A4A
purple: #A262A3
pink: #FCE9E9

"""

from flask_bootstrap import Bootstrap5
from flask import Flask, render_template

app = Flask(__name__)

bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
