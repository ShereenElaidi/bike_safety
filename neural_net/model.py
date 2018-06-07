# import statements
import pandas as pd
import csv
import time
import requests


addresses = []
counts = []
date = []
year = []
data_time = []

# loading the data set
data_set = pd.read_csv("data.csv")

addresses = data_set['Geocoding address']
counts = data_set['Duplicate count']
date = data_set['Date']
year = data_set['Year']
data_time = data_set['Time']



# a function to obtain the latitude and longitude of a given address.
# Input: a string containing the address
# Output: latitude, longitude of the address
def get_coordinates(address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?key=[API_KEY_HERE]'    #API key removed for privacy reasons
    params = {'sensor': 'false', 'address': address}
    r = requests.get(url, params=params)
    results = r.json()['results']
    location = results[0]['geometry']['location']
    lat = str(location['lat'])
    lng = str(location['lng'])
    # print(lat + " " + lng)
    return lat, lng

coordinates = []
coordinates.append([])
coordinates.append([])

# A function that will convert the entire dataset from address/intersection
# to longitude and latitude.
# Input: a list of addresses
# Output: A list containing the latitude and longitude of each address.
def address_to_coordinates(addresses):
    m = len(list(csv.reader(open('data.csv'))))
    data_base = open("data_base.txt", "w")
    header = "Year\tDate\tTime\tCount\tLat\t\tLng\n"
    data_base.write(header)
    print(header)
    for i in range (0,m):
        t0 = time.time()            # Take note of the initial time
        try:
            curr_lat, curr_long = get_coordinates(addresses[i])
            coordinates[0].append(curr_lat)
            coordinates[1].append(curr_long)
            curr_entry = str(year[i]) + "\t" + str(date[i]) + "\t" + str(data_time[i]) + "\t" + str(counts[i]) + "\t" + \
                         str(curr_lat) + "\t" + str(curr_long) + "\n"
            print(curr_entry)
            data_base.write(curr_entry)
            time.sleep(2)
        except AttributeError:
            print("Not an address.")
        except IndexError:
            data_base.write("NaN" + "\n")
            print("NaN")

        tf = time.time()            # Take note of the final time

        if i%100==0:
            print('Iteration: {}'.format(i))
            print('Time {} s'.format(tf - t0))

print("TESTING ADDRESS TO COOORDINATES FUNCTION")
print("Converting data...")
address_to_coordinates(addresses)


# lat = []
# long = []
#
# for ....
#     curr_lat, curr_long = find_coordinates(addresses[i])
#     lat.append(curr_lat)
#     long.append(curr_long)
#     if i%100 == 0:
#         save list ...
#         print(i)
