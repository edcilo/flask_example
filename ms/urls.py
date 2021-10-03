from flask import jsonify
from ms import app
from ms.helpers.counter import counter


@app.route('/')
def index():
    counter.sum()
    return jsonify({
        "data": {
            "name": "Flask01",
            "requets": counter.c,
            "version": "1.0.4",
        },
        "code": 200
    }), 200
