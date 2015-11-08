__author__ = 'rganesh'

# Import flask dependencies

from flask import Blueprint, request, render_template, jsonify

# Define the blueprint:
home = Blueprint('home', __name__, url_prefix='/home')


@home.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data = request.json
        print "Here"
        print data['zipcode']
        print data['priorities']
        print data['radius']

        return jsonify(zip=data['zipcode']+'r'+data['radius'])

