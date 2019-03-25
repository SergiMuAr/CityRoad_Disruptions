# import gmplot package 
import gmplot 
  
# GoogleMapPlotter return Map object 
# Pass the center latitude and 
# center longitude 
gmap = gmplot.GoogleMapPlotter(30.3164945, 78.03219179999999, 13) 
gmap.marker(30.3164945, 78.03219179999999, title="A street corner in Seattle")
gmap.draw( "/home/sergi/CityRoad_Disruptions/Proves/map2.html" )