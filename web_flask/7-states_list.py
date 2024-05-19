#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def close_storage():
    """method to handle @app.teardown_appcontext"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def state_list():
    state = storage.all(State)
    render_template('7-states_list.html', state = state)