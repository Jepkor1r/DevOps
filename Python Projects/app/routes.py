# Import the Flask application instance `app` from the `app` package.

from app import app

# We then use the route() decorator to tell Flask what URL should trigger our function.
# Define a route using the `route()` decorator.
# The decorator associates a URL path ('/' or '/index') with the `index` function below.

@app.route('/')  # Maps the root URL (http://localhost:5000/) to this function.

@app.route('/index') # Maps the URL http://localhost:5000/index to this function.

# This function is executed when a user visits the specified routes.
# It returns the string "Hello World!" to be displayed in the browser.

def index():
    return "Hello World!"