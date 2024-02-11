from flask import Flask
from backend.db import *


app = Flask(__name__)

# Connect views
import backend.views
