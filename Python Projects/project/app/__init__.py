from flask import Flask

from config import Config

app = Flask(__name__)

app.config.from_object(Config)

# routes defines url endpoints of the application
# Using app package(here app(the directory) is the package containing our application files e.g routes.py) we import routes. This allows Flask class to know which function to be executed when a specific url is accessed
from app import routes
