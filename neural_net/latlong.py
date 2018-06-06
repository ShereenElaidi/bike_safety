import requests


# Using Google's API key
response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyBvxoPEoxEx8Ym-mwg0CTk36JMdO7uS6hg')

address = response.json()
# print(address['results'][0]['geometry']['location'])
data_base = open("addresses.txt", "w")
curr_lat = str(address['results'][0]['geometry']['location']['lat'])
curr_long = str(address['results'][0]['geometry']['location']['lng'])
entry = curr_lat + " " + curr_long
data_base.write(entry)
# data_base.write(str(address['results'][0]['geometry']['location']['lat']))