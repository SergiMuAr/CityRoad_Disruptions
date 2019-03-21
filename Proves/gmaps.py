# import gmplot package 
import gmplot 
  
# GoogleMapPlotter return Map object 
# Pass the center latitude and 
# center longitude 
gmap = gmplot.GoogleMapPlotter(41.390205, 2.154007, 13 ) 
  
# Pass the absolute path 
gmap.draw( "/home/sergi/CityRoad_Disruptions/Proves/map.html" ) 
