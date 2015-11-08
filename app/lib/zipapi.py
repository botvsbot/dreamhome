__author__ = 'rganesh'

import urllib2
import json


def get_zipcodes_in_radius(zipcode, radius):
    api_key = 'cuVGlnt7LJ2ZgQbunfObcDTM1J1G4hLhLHX74qeQagQq71UugJGtmzfoig5nyQEk'
    url = 'https://www.zipcodeapi.com/rest/{}/radius.json/{}/{}/miles'.format(api_key, zipcode, radius)

    try:
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req).read()
    except Exception as exc:
        print 'Failed to query data from to zipappi due to {}'.format(repr(exc))
        return []
    resp_json = json.loads(resp)
    return resp_json['zip_codes']