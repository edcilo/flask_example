from flask import Flask, jsonify
from counter import counter


app = Flask(__name__)


@app.route('/')
def index():
    counter.sum()
    return jsonify({
        "data": {
            "name": "Flask01",
            "requets": counter.c,
        },
        "code": 200
    }), 200


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=5000)
    pass
