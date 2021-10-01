from flask import jsonify
from ms import app
from ms.counter import counter


@app.route('/')
def index():
    counter.sum()
    # return jsonify({
    #     "data": {
    #         "name": "Flask01",
    #         "requets": counter.c,
    #         "version": "1.0.2",
    #     },
    #     "code": 200
    # }), 200
    return "hello world", 200
