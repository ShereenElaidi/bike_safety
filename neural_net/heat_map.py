import pandas as pd
import gmplot
from IPython.display import display
import sys

# A code to change the coordinates of the accident data-points to code for the heatmap.

raw_data = pd.read_csv("data.csv")
lat = raw_data['Lat']
lng = raw_data['Lng']
ofile = open("map_code", 'wt')
for i in range (0,len(lat)):
    ofile.write("new google.maps.LatLng(%f, %f), \n" % (lat[i], lng[i]))
ofile.close()
