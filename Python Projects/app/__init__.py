#__init__.py is a special file in python that help in organizing and managing packages.
# This file is executed first when a package is imported
# Since we are building a culture of creating a good base structure for writing larger application, this application will exist in a package.
# First, we import the Flask class

from flask import Flask

#Next, we create an instance of that class(object)-> app
#__name__ is a convenient shortcut for the name of the application's package or module.

app = Flask(__name__)


from app import routes
