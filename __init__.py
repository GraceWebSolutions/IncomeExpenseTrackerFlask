from flask import Flask, redirect
from .config import Config

app = Flask(__name__)

from .controllers import routes