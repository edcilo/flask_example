from flask import jsonify
from ms import app
from ms.counter import counter
from ms.middlewares import auth


@app.route('/')
@auth.auth
def index():
    counter.sum()
    return jsonify({
        "data": {
            "name": "Flask01",
            "requets": counter.c,
            "version": "1.0.5",
        },
        "code": 200
    }), 200
