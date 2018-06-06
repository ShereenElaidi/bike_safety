# import statements
from geopy.geocoders import Nominatim
import pandas as pd
import csv
import time

addresses = []
counts = []

# loading the data set
data_set = pd.read_csv("data.csv")

# obtaining the duplicate count and geocoding address
addresses = data_set['Geocoding address']
counts = data_set['Duplicate count']
print(addresses)
print(counts)

# a function to obtain the latitude and longitude of a given address.
# Input: a string containing the address
# Output: latitude, longitude of the address
def find_coordinates(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address, timeout = 10)
    return location.latitude, location.longitude

coordinates = []
coordinates.append([])
coordinates.append([])
print(data_set.head())


def address_to_lat_long(addresses):
    m = len(list(csv.reader(open('data.csv'))))
    data_base = open("data_base.txt", "w")
    for i in range (0,m):
        try:
            curr_lat, curr_long = find_coordinates(addresses[i])
            coordinates[0].append(curr_lat)
            coordinates[1].append(curr_long)
            curr_entry = str(curr_lat) + " " + str(curr_long)
            print(curr_entry)
            data_base.write(curr_entry + "\n")
            time.sleep(1)
        except AttributeError:
            print("Not an address.")

print("Testing address_to_lat_long...")
address_to_lat_long(addresses)
print(coordinates)


