import googlemaps
import configparser
from datetime import datetime
config = configparser.ConfigParser()
config.read('/home/sergi/Documents/config.ini')
apikey = config['api.keys']['MAPS_API_KEY']
# gmaps = googlemaps.Client(key=apikey)

# Geocoding an address
# geocode_result = gmaps.geocode("🚙Continuen les CUES:
# 🚧C-17 de la Llagosta a Montcada -&gt;BCN per obres 
# De B-24 Cervelló a N-340 Vallirana -&gt;Tarragona 
# C-14 entre Montblanc i Pira 
# C-65 a Llambilles, a banda i banda",
#                                 components={'administrative_area_level_1': 'CT'})
# print (geocode_result[0]['geometry']['location'].lat)
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