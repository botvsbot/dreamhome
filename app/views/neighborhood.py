__author__ = 'rganesh'

# Import flask dependencies
from flask import Blueprint, request, render_template

# Define the blueprint:
neighborhood = Blueprint('neighborhood', __name__, url_prefix='/neighborhood')


@neighborhood.route('/')
@neighborhood.route('/<neighborhood_id>')
def hello(neighborhood_id=None):
    return render_template('neighborhood/neighborhood.html',
                           neighbor=get_neighborhood_from_id(neighborhood_id) if neighborhood_id else None)


def get_neighborhood_from_id(neiborhood_id):
    neighbor_map = {'1': 'Palm Springs',
               '2': 'San Francisco',
               '3': 'Alameda'}
    return neighbor_map[neiborhood_id]
