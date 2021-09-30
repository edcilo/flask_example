from flask import Flask


app = Flask(__name__)


import ms.urls
import ms.db
import ms.models
