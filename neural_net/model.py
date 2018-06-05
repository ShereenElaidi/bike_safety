# import statements
import csv
from geopy.geocoders import Nominatim

addresses = []
counts = []
# loading the dataset
with open('data.csv', 'rt') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        addresses.append(row[12])
        counts.append(row[11])


# a function to obtain the latitude and longitude of a given address.
# Input: a string containing the address
# Output: latitude, longitude of the address
def find_coordinates(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    return location.latitude, location.longitude

# DEBUGGING
# address = "805 Sherbrooke St E, Montreal"
# lat, long = find_coordinates(address)
# print("Data for: " + address)
# print('Latitude is: {:.5f}'.format(lat))
# print('Longitude is: {:.5f}'.format(long))
# a function to convert all the addresses to their lat and long
# Input: a vector of string addresses (n*1)
# Output: a matrix of lat and long (n*2)
coordinates = []
# converts all the addresses in an array to an array of lat
# and long.
def address_to_lat_long(addresses):
    for string in addresses:
        (coordinates[0], coordinates[1]).append(find_coordinates(string))

# debugging
address_to_lat_long(addresses)
print(coordinates)