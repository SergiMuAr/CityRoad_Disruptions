import googlemaps
import configparser
from datetime import datetime
config = configparser.ConfigParser()
config.read('/home/sergi/Documents/config.ini')
apikey = config['api.keys']['MAPS_API_KEY']
print (apikey)
gmaps = googlemaps.Client(key=str(apikey))

# Geocoding an address
geocode_result = gmaps.geocode("Cues a Sant Boi de Llobregat per exhibicionistes provoquen un accident",
                                components={'administrative_area_level_1': 'CT'})
print (geocode_result[0]['geometry']['location'])
# gmaps.geocode

# def test_geocode_with_region_biasing(self):
#     responses.add(responses.GET,
#                     'https://maps.googleapis.com/maps/api/geocode/json',
#                     body='{"status":"OK","results":[]}',
#                     status=200,
#                     content_type='application/json')

#     results = self.client.geocode('Toledo', region='es')

#     self.assertEqual(1, len(responses.calls))
#     self.assertURLEqual('https://maps.googleapis.com/maps/api/geocode/json?'
#                         'region=es&key=%s&address=Toledo' % self.key,
#                         responses.calls[0].request.url)