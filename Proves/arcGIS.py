from arcgis.gis import GIS
from arcgis.geocoding import *
gis = GIS()
hola = get_geocoders(gis)
single_line_address = "🚗🛵Cues als accessos nord a BCN: ➡️C-58 Terrassa Centre-Badia/Montcada -&gt; BCN Montcada-Ripollet/Sant Quirze -&gt; Terrassa ➡️C-16 Rubí-Valldoreix/peatge-boca nord Túnel Vallvidrera  ➡️B-20 Santa Coloma-Nus Trinitat ➡️C-31 a Badalona"
# single_line_address = "71 Arc de Sant Martí, Barcelona, 8032"
# single_line_address = "B-24 Cervelló"
loc = geocode(single_line_address)[0]
print (loc["location"])

