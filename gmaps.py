# import gmplot package 
import gmplot 
import configparser
config = configparser.ConfigParser()
config.read('/home/sergi/Documents/config.ini')
def visualizeMap (incidencies): 

    gmap = gmplot.GoogleMapPlotter(41.390205, 2.154007, 13,apikey= config['api.keys']['MAPS_API_KEY'])
    
    for incid in incidencies:
        gmap.marker(incid[2], incid[3], title=incid[1])        
    gmap.draw( "/home/sergi/CityRoad_Disruptions/Proves/Incidencies.html" )

