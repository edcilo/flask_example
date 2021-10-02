from dotenv import load_dotenv
from flask import Flask


load_dotenv()
app = Flask(__name__)


import ms.config
import ms.urls
import ms.db
import ms.models
import ms.commands
