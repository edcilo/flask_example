from dotenv import load_dotenv
from flask import Flask


load_dotenv()
app = Flask(__name__)


import ms.urls
import ms.config
