#!/usr/bin/python3
"""Flask class"""
from flask import Flask


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
    """displayin"""
    return "Python %s" % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)