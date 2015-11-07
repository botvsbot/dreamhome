__author__ = 'rganesh'

# Import flask dependencies
from flask import Blueprint, request, render_template
from app.lib.shape_handlers import jsonmap
import json
# Define the blueprint:
zipcode = Blueprint('zipcode', __name__, url_prefix='/zipcode')


@zipcode.route('/')
@zipcode.route('/<zip_id>')
def hello(zip_id=None):
    return render_template('zipcode/zipcode.html')


def get_zipcode_from_id(zip_id):
    zip_map = {'1': 94086,
               '2': 94115,
               '3': 95134}
    return zip_map[zip_id]

@zipcode.route('/shpdata')
def shapedata():
    json_map = jsonmap()
    return json.dumps(json_map)


