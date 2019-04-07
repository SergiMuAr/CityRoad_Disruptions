import googlemaps
import configparser
from datetime import datetime

class Geocoder:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('/home/sergi/Documents/config.ini')
        apikey = config['api.keys']['MAPS_API_KEY']
        self.gmaps = googlemaps.Client(key=apikey)

    def geoCode(self,tweet):
        # Geocoding an address
        geocode_result = self.gmaps.geocode(tweet, components={'administrative_area_level_1': 'CT'})
        if geocode_result:
            return geocode_result[0]['geometry']['location']

    def preprocess(self,tweet):
        tweets = tweet.split("\n")
        return tweets
