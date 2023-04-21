#!/usr/bin/python3
"""Flask class"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """displaying"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_only():
    """displaying"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """displaying"""
    return "C %s" % text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """displaying"""
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def only_integer(n):
    """displaying only int"""
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def only_integer_html(n):
    """displaying int in html"""
    return render_template("5-number.html", n = n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)