from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS


load_dotenv()
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


import ms.urls
import ms.config
import ms.commands
