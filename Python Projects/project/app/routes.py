#Rendering means converting a template into a compete HTML page
#render_template is a function in flask framework that takes a template filename and a variable list of template arguments, and returns the same template, but with all the placeholders in it replaced with actual values
from flask import render_template

# Import the Flask application instance `app` from the `app` package.
from app import app

# Define a route using the `app.route()` decorator.
# The decorator associates a URL path ('/' or '/index') with the `index` function below.
# Either of the url will trigger the same function, making the routes more flexible and user-friendly.

@app.route('/')  # Maps the root URL (http://localhost:5000/) to this function.

@app.route('/index') # Maps the URL http://localhost:5000/index to this function.

# This function is executed when a user visits the specified routes.
# It returns the string "Hello World!" to be displayed in the browser.

def index():
    user = {'username': 'Lagat'}
    return render_template('index.html', title='Home', user=user)