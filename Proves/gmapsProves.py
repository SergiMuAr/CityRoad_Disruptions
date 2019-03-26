# import gmplot package 
import gmplot 
import configparser

config = configparser.ConfigParser()
config.read('/home/sergi/Documents/config.ini')
gmap = gmplot.GoogleMapPlotter(41.390205, 2.154007, 13,apikey= config['api.keys']['MAPS_API_KEY'])

for 
gmap.marker(, , title="A street corner in Seattle")
gmap.draw( "/home/sergi/CityRoad_Disruptions/Proves/map2.html" )

