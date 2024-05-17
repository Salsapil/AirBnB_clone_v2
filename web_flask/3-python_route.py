#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """return string"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def home_message():
    """return string"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def home_message_C(text):
    """return string"""
    no_underscore = text.replace('_', ' ')
    return 'C {}'.format(no_underscore)


@app.route('/python/')
@app.route('/python/<text>')
def home_message_python(text='is cool'):
    """return string"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
