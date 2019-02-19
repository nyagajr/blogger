from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, BooleanField, SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Enter your Email', validators=[Required(), Email()])
    password = PasswordField('Enter Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
class RegistrationForm(FlaskForm):
    email = StringField('Enter your Email Address', validators = [Required(), Email()])
    username = StringField('Enter your Username', validators=[Required()])
    password = PasswordField('enter password', validators=[Required(), EqualTo('password_confirm', message='⛔ password mismatch!!')])
    password_confirm = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')
