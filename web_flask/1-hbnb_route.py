#!/usr/bin/python3
"""
    Flask App
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """
        Hello Route
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():

    """
        HBNB Route
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)