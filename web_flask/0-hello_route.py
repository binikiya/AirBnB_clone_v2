#!/usr/bin/python3
"""Flask class"""
from flask import Flask
"""Flast class"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """displaying """
    return "Hello HBNB!"


if __name__ == "__main__":
    """starting server"""
    app.run(host='0.0.0.0', port=5000)