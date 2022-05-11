from flask import Flask
from .config import config_options
from flask_sqlalchemy import SQLAlchemy

# flask instance
app = Flask(__name__)
app.config.from_object(config_options['dev'])
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/pitch.db'


db=SQLAlchemy(app)
from . import forms,views


