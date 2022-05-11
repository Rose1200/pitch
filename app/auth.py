from flask import Blueprint, render_template, redirect
from.forms import LogIn, Signup
from app import app

auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    return render_template('login.html', form=LogIn)

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    return render_template("signup.html", form=Signup)    
