__author__ = 'rganesh'

# Import flask dependencies
from flask import Blueprint, request, render_template, jsonify
from app.lib.shape_handlers import get_polygon_map
from app.lib.zipapi import get_lat_lng_for_zipcode
from app.lib.listing import listing_map
import json

# Define the blueprint:
neighborhood = Blueprint('neighborhood', __name__, url_prefix='/neighborhood')


@neighborhood.route('/<neighborhood_id>')
def neighborhome(neighborhood_id=None):
    # data = [('Sunday', 48), ('Monday', 27), ('Tuesday', 32), ('Wednesday', 42),
            # ('Thursday', 38), ('Friday', 45), ('Saturday', 52)]
    get_listings_for_neighborhood(neighborhood_id)
    return render_template('neighborhood/neighborhood.html',
                           neighborid=neighborhood_id)


def get_listings_for_neighborhood(nid):
    neighbors = get_neighborhood_from_id(nid)
    zipcodes = []
    lat_lng = []
    for region in neighbors['features']:
        zipcodes.append(region['properties']['ZCTA5CE10'])
        lat_lng.append(get_lat_lng_for_zipcode(region['properties']['ZCTA5CE10']))
    print zipcodes
    print lat_lng




def get_neighborhood_from_id(neighborhood_id):
    json_map = json.loads(get_polygon_map('app/data/intersect/zipcode_neighborhood_intersect.shp'))
    neighbor_map = {'type': json_map['type'], 'features': list()}
    for (index, entry) in enumerate(json_map.get('features')):
        if int(entry['properties']['REGIONID']) == int(neighborhood_id):
            neighbor_map['features'].append(entry)
    return neighbor_map


@neighborhood.route('/polygon/<n_id>')
def hood_polygon(n_id):
    neighbor_map = json.dumps(get_neighborhood_from_id(n_id))
    return json.dumps(neighbor_map)

@neighborhood.route('/listing/<n_id>')
def hood_listing(n_id):
    listing = json.dumps(listing_map())
    return json.dumps(listing)
