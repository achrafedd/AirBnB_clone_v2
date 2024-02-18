#!/usr/bin/python3
"""
    Flask App
"""
from flask import Flask, render_template

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


@app.route('/c/<text>')
def c(text):
    """
        C Route
    """
    return f"C {text.replace('_', ' ')}"


@app.route('/python', defaults={"text": "is_cool"})
@app.route('/python/<text>')
def python(text):
    """
        Python Route
    """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def number(n):
    """
        Number Route
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """
        number_template Route
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
        number_odd_or_even Route
    """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
