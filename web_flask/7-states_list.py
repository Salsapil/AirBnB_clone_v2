#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """method to handle"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    state = storage.all('State')
    return render_template('7-states_list.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
