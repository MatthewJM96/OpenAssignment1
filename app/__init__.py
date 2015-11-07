# __init__.py

# Initialises the Flask application with specified configuration.

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views