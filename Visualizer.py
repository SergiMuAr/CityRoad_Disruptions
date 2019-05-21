import gmplot 
import configparser

class Gmaps:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('/home/sergi/Documents/config.ini')
        self.gmap = gmplot.GoogleMapPlotter(41.390205, 2.154007, 10,apikey= config['api.keys']['MAPS_API_KEY'])
        self.gmap.draw( "/home/sergi/CityRoad_Disruptions/Proves/Incidencies.html" )


    def visualizeMap (self,incidencies): 

        if (incidencies is not None):
            for incid in incidencies:
                self.gmap.marker(incid[2], incid[3], title=incid[1])        
            self.gmap.draw( "/home/sergi/CityRoad_Disruptions/Proves/Incidencies.html" )

