#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>')
def home_number(n):
    """return integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def home_number_str(n):
    """return template"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
