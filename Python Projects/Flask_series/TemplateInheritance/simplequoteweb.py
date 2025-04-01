#This is the main entry of the application
# Import the Flask application instance `app` from the `quote` package and start the Flask development server when the script executed

from quote import app

if __name__ == '__main__':
    app.run(debug=True)

