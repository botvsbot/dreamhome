__author__ = 'rganesh'

# Import flask dependencies

from flask import Blueprint, request, render_template, jsonify
from app.lib.shape_handlers import get_polygon_map, get_neighborhoods_for_zipcode
import json

# Define the blueprint:
zipcode = Blueprint('zipcode', __name__, url_prefix='/zipcode')


@zipcode.route('/', methods=['GET', 'POST'])
@zipcode.route('/<zip_id>', methods=['GET', 'POST'])
def ziphome(zip_id=None):
    if request.method == 'GET':
        zips = zip_id
        return render_template('zipcode/zipcode.html', zipcode=str(zips) if zips else None)
    else:
        data = request.json
        print data
        return jsonify(zip=data['zipcode_input']+'r'+data['radius'])


def get_zipcode_from_id(zip_id):
    zip_map = get_zip_map()
    return zip_map[zip_id]


@zipcode.route('/zip_hood_data/<zip_code>')
def ziphood_shapedata(zip_code):
    json_map = get_neighborhoods_for_zipcode(zip_code.split('r')[0], int(zip_code.split('r')[1]))
    # from app.views.neighborhood import get_neighborhood_from_id
    # json_map = json.dumps(get_neighborhood_from_id(275040))
    return json.dumps(json_map)


@zipcode.route('/shpdata')
def neighborhood_shapedata():
    json_map = get_polygon_map('app/data/neighborhood/ZillowNeighborhoods-AZ.shp')
    return json.dumps(json_map)


@zipcode.route('/zipshpdata')
def zipcode_shapedata():
    json_map = get_polygon_map('app/data/zipcode/cb_2014_us_zcta510_500k.shp')
    return json.dumps(json_map)


@zipcode.route('/intersectshpdata')
def intersect_shape_data():
    #  intersect_neighborhood_with_zipcode()
    json_map = get_polygon_map('app/data/intersect/zipcode_neighborhood_intersect.shp')
    return json.dumps(json_map)


def get_zip_map():
    return {'1': '94086',
            '2': '94115',
            '3': '95134'}

bufSHP = 'app/data/neighborhood/ZillowNeighborhoods-AZ.sh'
intSHP = 'app/data/intersect/zipcode_neighborhood_intersect.shp'
ctSHP = 'app/data/zipcode/cb_2014_us_zcta510_500k.shp'

def get_id_from_zipcode(zip_id):
    ids = get_zip_map().keys()
    zips = get_zip_map().values()
    idmap = {}
    for (index, uuid) in enumerate(ids):
        idmap[zips[index]] = uuid
    return idmap[zip_id]
