__author__ = 'rganesh'

import urllib2
import json


def get_zipcodes_in_radius(zipcode, radius):
    api_key = 'RT90tpWRQOis5I0dWYqsRpOBEAUS4XhWQrWjQSaHGt9LcaY88pB0OpBs0wl5tD1j'
    url = 'https://www.zipcodeapi.com/rest/{}/radius.json/{}/{}/miles'.format(api_key, zipcode, radius)

    try:
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req).read()
    except Exception as exc:
        print 'Failed to query data from to zipappi due to {}'.format(repr(exc))
        return []
    resp_json = json.loads(resp)
    return resp_json['zip_codes']