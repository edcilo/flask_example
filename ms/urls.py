from flask import jsonify
from ms import app
from ms.counter import counter


@app.route('/')
def index():
    counter.sum()
    return "error :(", 200
