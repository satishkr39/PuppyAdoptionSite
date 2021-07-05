# __init__.py it is used to set up db and our application
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import  SQLAlchemy
from flask_migrate import Migrate
import os


# setting our flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# register bluprint is done once after db is being found by our application.
from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprints

app.register_blueprint(owners_blueprints, url_prefix='/owners')  # url_prefix is used in URL bar of browser.
app.register_blueprint(puppies_blueprint, url_prefix='/puppies')
