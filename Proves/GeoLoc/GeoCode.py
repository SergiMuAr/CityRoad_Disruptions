from arcgis.gis import GIS
from arcgis.geocoding import *
gis = GIS()
hola = get_geocoders(gis)
single_line_address = "N-340 Vallirana"
# single_line_address = "71 Arc de Sant Martí, Barcelona, 8032"
# single_line_address = "B-24 Cervelló"
loc = geocode(single_line_address)[0]
print (loc["location"])
