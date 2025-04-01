# Import the Flask application instance `app` from the `quote` package.
from quote import app

# Define a route using the `app.route()` decorator.
# The decorator associates a URL path ('/' or '/index') with the `index` function below.
# Either of the url will trigger the same function, making the routes more flexible and user-friendly.

@app.route('/')  # Maps the root URL (http://localhost:5000/) to this function.

@app.route('/index') # Maps the URL http://localhost:5000/index to this function.


# This function is executed when a user visits the specified routes.
# It returns a complete HTML page to be displayed in the browser(expanding from earlier's simple string-Hello World!)

def index():
    user = {'username' : 'Lagat'}
    return """
        <html>
        <head>
        <title> Home Page - Welcome to QuoteBlog! </title>
        </head>
        <body>
            <h1> Hello """ + user['username'] + """!</h1>
            <h2> I have tasted dating. I have tasted friendships. I have tasted singlehood. I highly recommend God! </h2>
        </body>
        </html>
        """