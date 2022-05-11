from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,Email

class Signup(FlaskForm):
    username = StringField(label='Enter username', validators=[DataRequired(),Length(min=3,max=20)])
    email = EmailField(label='Enter your email', validators=[DataRequired(),Email()])
    password = PasswordField(label='Enter password', validators=[DataRequired(),Length(min=5,max=15)])
    confirm_password = PasswordField(label='Confirm password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(label='Sign up')

class LogIn(FlaskForm):
    username = StringField(label='Enter username', validators=[DataRequired(),Length(min=3,max=20)])
    password = PasswordField(label='Enter password', validators=[DataRequired(),Length(min=5,max=15)])  
    submit = SubmitField(label='Log In')