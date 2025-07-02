# Import FlaskForm from flask_wtf, which is a base class for creating web forms in Flask

from flask_wtf import FlaskForm

# Import standard form fields from WTForms

from wtforms import StringField, PasswordField, BooleanField, SubmitField

# Import validators to apply validation rules to form fields

from wtforms.validators import DataRequired


# Define a login form class by inheriting from FlaskForm
class LoginForm(FlaskForm):
    # A text field for the username with a label 'Username'
    # The DataRequired() validator ensures this field is not submitted empty

    username = StringField('Username', validators=[DataRequired()])

    # A password input field with a label 'Password'
    # DataRequired ensures the password must be entered

    password = PasswordField('Password', validators=[DataRequired()])

    # A checkbox field labeled 'Remember Me'
    # Used to indicate if the user wants to stay logged in (e.g., persistent session)

    remember_me = BooleanField('Remember Me')

    # A submit button labeled 'Sign In' to send the form
    submit = SubmitField('Sign In')

