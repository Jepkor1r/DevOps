#Rendering means converting a template into a compete HTML page
#render_template is a function in flask framework that takes a template filename and a variable list of template arguments, and returns the same template, but with all the placeholders in it replaced with actual values
from flask import render_template
# Import the Flask application instance `app` from the `quote` package.
from quote import app
# Import the LoginForm class from the `forms.py` module inside the `quote` package.
# WHY not just `forms.py`? Python needs the full path (package.module) to find `forms.py` inside the `quote` package.
from quote.forms import LoginForm
# `flash()` is used to show short messages to the user (e.g., "You logged in successfully")
from flask import flash
# `redirect()` sends the user to another URL after some action.
from flask import redirect

# Maps the root URL (http://localhost:5000/) to this function.
@app.route('/') 
# Maps the URL http://localhost:5000/login to this function.
# It allows both GET and POST requests.  
# - GET is used when the page first loads.  
# - POST is used when the user submits the login form.
@app.route('/login', methods=['GET', 'POST']) 


# When the browser requests http://localhost:5000/login:
#Flask sees the @app.route('/login') decorator and calls the login() function.
#login() creates a LoginForm instance.
#render_template() loads login.html, replaces {{ title }} and {{ form }} with real values, and returns a full HTML page.
#Browser displays that HTML page.

def login():
    form = LoginForm() # Create a new instance of the LoginForm

    # If the form was submitted (POST) and all fields validated correctly:
    if form.validate_on_submit():
        # Show a temporary message to the user with their username and remember-me choice
        flash('Login requested for user {}, remember={}'.format(
            form.username.data, # The username entered in the form.
            form.remember_me.data # The remember-me checkbox value.
        ))
        # After showing the flash message, send the user to the '/index' page.
        return redirect('/index')


    # Pass variables to the template:
    # - 'title' will be accessible as {{ title }} inside login.html
    # - 'form' will be accessible as {{ form }} inside login.html
    #
    # The **first 'form'** (left side of =) is the name of the variable in the template.
    # The **second 'form'** (right side of =) is the Python variable holding the actual LoginForm instance.
    # This is how Python variables are mapped into Jinja template variables.

    return render_template('login.html', title='Sign In', form=form)