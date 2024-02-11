import logging
from flask import Flask
from backend.db import *


app = Flask(__name__)

# Logging configuration
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler(filename='log/server.log')
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# Connect views
import backend.views
