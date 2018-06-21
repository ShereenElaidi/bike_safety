import pandas as pd
import gmplot
from IPython.display import display
import sys

# A code to change the coordinates of the accident data-points to code for the heatmap.

raw_data = pd.read_csv("data.csv")
print(raw_data.head())
lat = raw_data['Lat']
lng = raw_data['Lng']
count = raw_data['Count']
ofile = open("map_code", 'wt')
for i in range (0,len(lat)):
    ofile.write("   {location: new google.maps.LatLng(%f, %f),weight: %f}, \n" % (lat[i], lng[i], count[i]))
ofile.close()
