__author__ = 'rganesh'

# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
# db = SQLAlchemy(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def home():
    return render_template('index.html')

# Import a module / component using its blueprint handler variable (mod_auth)
from app.views.zipcode import zipcode
from app.views.neighborhood import neighborhood
from app.views.listing import listing


# Register blueprint(s)
app.register_blueprint(zipcode)
app.register_blueprint(listing)
app.register_blueprint(neighborhood)

# Build the database:
# This will create the database file using SQLAlchemy
# db.create_all()