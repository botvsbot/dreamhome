__author__ = 'rganesh'

# Import flask dependencies
from flask import Blueprint, request, render_template

# Define the blueprint:
listing = Blueprint('listing', __name__, url_prefix='/listing')


@listing.route('/')
@listing.route('/<listing_id>')
def listinghome(listing_id=None):
    return render_template('listing/listing.html', listing=get_listing_from_id(listing_id) if listing_id else None)


def get_listing_from_id(listing_id):
    listing_map = {'1': '2BHK Condo',
                   '2': '5BHK Individual Home',
                   '3': 'Studio Apartment with patio'}
    return listing_map[listing_id]
