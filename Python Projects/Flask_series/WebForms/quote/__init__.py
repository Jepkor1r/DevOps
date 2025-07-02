#__init__.py is a special file in python that help in organizing and managing packages.
# Any directory containing any __init__.py can be treated as a package and imported. Thus, we have now quote package which will be imported in various file in this project
# This file is executed first when a package is imported
# Since we are building a culture of creating a good base structure for writing larger application, this application will exist in a package.

# We import the Flask class from flask package

from flask import Flask

# Import the Config class from the config module(config.py)
# This class contains all the configuration settings for our Flask app (e.g., SECRET_KEY)
from config import Config

#Create an instance of that class(object)-> app
# The __name__ variable helps Flask identify the root path of the application,
# which is important for locating templates, static files, etc.

app = Flask(__name__)

# Load configuration values from the Config class
# Apply the configuration settings to the Flask app instance

app.config.from_object(Config)

# routes defines url endpoints of the application
# Using quote package(the package contains our application files e.g routes.py), we import routes. This allows Flask class to know which function to be executed when a specific url is accessed
from quote import routes