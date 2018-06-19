import pandas as pd
import gmplot
from IPython.display import display
import sys

raw_data = pd.read_csv("data.csv")
# display(raw_data.head(n=5))
# display(raw_data.info())
lat = raw_data['Lat']
lng = raw_data['Lng']
# print(lat)
# print(lng)
# gmap = gmplot.GoogleMapPlotter(45.5017, -73.5673, 10)
# gmap.heatmap(lat, lng)
# gmap.draw("my_heatmap.html")

print(len(lat))
print(len(lng))
ofile = open("map_code", 'wt')
for i in range (0,len(lat)):
    ofile.write("new google.maps.LatLng(%f, %f), \n" % (lat[i], lng[i]))

ofile.close()

