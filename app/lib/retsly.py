__author__ = 'rganesh'

import urllib2
import json
API_KEY = '2785c5f6ec2ca043f01e9015726a39c2'
VENDOR = 'armls'
from app.lib.zipapi import get_lat_lng_for_zipcode


def randomize_flag(media, default=False):
    if default:
        if media.get('shortDescription', ''):
            if 'front' in media.get('shortDescription', '').lower() \
                    or 'porch' in media.get('shortDescription', '').lower():
                return True
    else:
        return False


def get_media_for_zipcode(zipcode, count=1):
    # (lat, lng) = get_lat_lng_for_zipcode(zipcode)
    (lat, lng) = tuple([33.45, -112.06])
    base_url = 'https://rets.io/api/v1/{}/listings?access_token={}'.format(VENDOR, API_KEY)
    query = '&limit=25&sortBy=yearBuilt&near={}%2C{}'.format(lat, lng)
    url = base_url + query

    try:
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req).read()
    except Exception as exc:
        print 'Failed to query data from to retsly due to {}'.format(repr(exc))
        return ''
    resp_json = json.loads(resp)
    if not resp_json['success']:
        print 'Retsly returned error with status {}'.format(resp_json['status'])
        return ''
    media_list = []
    for data in resp_json['bundle']:
        if data['media']:
            for media in data['media']:
                if len(media_list) == count:
                    if count == 1:
                        return media_list[0]
                    else:
                        return media_list
                if randomize_flag(media):
                    media_list.append(media['url'])
                    continue
                else:
                    media_list.append(media['url'])
                    # if len(media_of_interest) > 10:
                    #     return media_of_interest[randint(0, len(media_of_interest)-1)]
