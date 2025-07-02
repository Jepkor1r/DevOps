#Rendering means converting a template into a compete HTML page
#render_template is a function in flask framework that takes a template filename and a variable list of template arguments, and returns the same template, but with all the placeholders in it replaced with actual values
from flask import render_template
from quote import app
from quote.forms import LoginForm


@app.route('/')  # Maps the root URL (http://localhost:5000/) to this function.

@app.route('/login') # Maps the URL http://localhost:5000/login to this function.


def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)