__author__ = 'rganesh'

import urllib2
import json
API_KEY = 'RT90tpWRQOis5I0dWYqsRpOBEAUS4XhWQrWjQSaHGt9LcaY88pB0OpBs0wl5tD1j'
API_KEY_BACKUP = 'cuVGlnt7LJ2ZgQbunfObcDTM1J1G4hLhLHX74qeQagQq71UugJGtmzfoig5nyQEk'


def get_zipcodes_in_radius(zipcode, radius):

    url = 'https://www.zipcodeapi.com/rest/{}/radius.json/{}/{}/miles'.format(API_KEY, zipcode, radius)

    try:
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req).read()
    except Exception as exc:
        print 'Failed to query data from to zipappi due to {}'.format(repr(exc))
        url = 'https://www.zipcodeapi.com/rest/{}/radius.json/{}/{}/miles'.format(API_KEY_BACKUP, zipcode, radius)
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req).read()
    resp_json = json.loads(resp)
    return resp_json['zip_codes']


def get_lat_lng_for_zipcode(zipcode):
    url = 'https://www.zipcodeapi.com/rest/{}/info.json/{}/degrees'.format(API_KEY, zipcode)
    try:
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req).read()
    except Exception as exc:
        print 'Failed to query data from to zipappi due to {}'.format(repr(exc))
        url = 'https://www.zipcodeapi.com/rest/{}/info.json/{}/degrees'.format(API_KEY_BACKUP, zipcode)
        try:
            req = urllib2.Request(url)
            resp = urllib2.urlopen(req).read()
        except Exception as exc:
            return tuple([33.45, -112.06])
    resp_json = json.loads(resp)
    return tuple([resp_json['lat'], resp_json['lng']])
