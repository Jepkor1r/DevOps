#__init__.py is a special file in python that help in organizing and managing packages.
# Any directory containing any __init__.py can be treated as a package and imported. Thus, we have now app package which will be imported in various file in this project
# This file is executed first when a package is imported
# Since we are building a culture of creating a good base structure for writing larger application, this application will exist in a package.
# First, we import the Flask class

from flask import Flask

#Next, we create an instance of that class(object)-> app
#__name__ is a convenient shortcut for the name of the application's package or module.

app = Flask(__name__)

# routes defines url endpoints of the application
# Using quote package(the package contains our application files e.g routes.py), we import routes. This allows Flask class to know which function to be executed when a specific url is accessed
from quote import routes