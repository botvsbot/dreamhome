__author__ = 'rganesh'

# Import flask dependencies

from flask import Blueprint, request, render_template, jsonify

# Define the blueprint:
home = Blueprint('home', __name__, url_prefix='/home')


@home.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
        return render_template('index2.html')
    else:
        data = request.json
        return jsonify(zip=data['zipcode_input']+'r'+data['radius'])

