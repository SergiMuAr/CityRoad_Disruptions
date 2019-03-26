# import gmplot package 
import gmplot 
import configparser

def init(): 
    config = configparser.ConfigParser()
    config.read('/home/sergi/Documents/config.ini')
    gmap = gmplot.GoogleMapPlotter(41.390205, 2.154007, 13,apikey= config['api.keys']['MAPS_API_KEY'])

def addMarker(lat, long, text):
    for 
    gmap.marker(lat, long, title=text)
    gmap.draw( "/home/sergi/CityRoad_Disruptions/Proves/map2.html" )

