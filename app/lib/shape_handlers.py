__author__ = 'radhikaparthasarathy'

from app.lib import shapefile, zipapi
import json
import fiona
from shapely.geometry import shape, mapping
import rtree


# read the shapefile
def get_polygon_map(shape_file_name):
    reader = shapefile.Reader(shape_file_name)
    fields = reader.fields[1:]
    field_names = [field[0] for field in fields]
    buffer_data = []
    for sr in reader.shapeRecords():
        atr = dict(zip(field_names, sr.record))
        atr['color'] = 'orange'
        geom = sr.shape.__geo_interface__
        buffer_data.append(dict(type="Feature", geometry=geom, properties=atr))
        # import pdb; pdb.set_trace()

    polygon_map = {"type": "FeatureCollection", "features": buffer_data}
    return json.dumps(polygon_map)


def get_neighborhoods_for_zipcode(zipcode, radius):
    zipcodes_in_radius = [data['zip_code'] for data in zipapi.get_zipcodes_in_radius(zipcode, int(radius))]
    intersect_json = get_polygon_map('app/data/intersect/zipcode_neighborhood_intersect.shp')
    intersect_json = json.loads(intersect_json)
    new_json = {'type': intersect_json['type'], 'features': []}
    for (index, entry) in enumerate(intersect_json.get('features')):
        if entry['properties']['ZCTA5CE10'] == zipcode:
            new_json['features'].append(entry)
        elif entry['properties']['ZCTA5CE10'] in zipcodes_in_radius:
            new_json['features'].append(entry)
            new_json['features'][-1]['properties']['color'] = 'green'
    return json.dumps(new_json)


def intersect_neighborhood_with_zipcode():

    bufSHP = 'app/data/zipcode/cb_2014_us_zcta510_500k.shp'
    intSHP = 'app/data/intersect/zipcode_neighborhood_intersect.shp'
    ctSHP = 'app/data/neighborhood/ZillowNeighborhoods-AZ.shp'

    with fiona.open(bufSHP, 'r') as layer1:
        with fiona.open(ctSHP, 'r') as layer2:
            # We copy schema and add the  new property for the new resulting shp
            schema = layer2.schema.copy()
            #import pdb; pdb.set_trace()
            schema['properties']['ZCTA5CE10'] = 'str:5'
            # We open a first empty shp to write new content from both others shp
            with fiona.open(intSHP, 'w', 'ESRI Shapefile', schema) as layer3:
                index = rtree.index.Index()
                for feat1 in layer1:
                    #import pdb; pdb.set_trace()
                    fid = int(feat1['id'])
                    geom1 = shape(feat1['geometry'])
                    index.insert(fid, geom1.bounds)

                for feat2 in layer2:
                    geom2 = shape(feat2['geometry'])
                    for fid in list(index.intersection(geom2.bounds)):
                        if fid != int(feat2['id']):
                            feat1 = layer1[fid]
                            geom1 = shape(feat1['geometry'])
                            if geom1.intersects(geom2):
                                # We take attributes from ctSHP
                                props = feat2['properties']
                                # Then append the uid attribute we want from the other shp
                                props['ZCTA5CE10'] = feat1['properties'].get('ZCTA5CE10')
                                # Add the content to the right schema in the new shp
                                try:
                                    layer3.write({
                                        'properties': props,
                                        'geometry': mapping(geom1.intersection(geom2))
                                    })
                                except Exception as e:
                                    continue