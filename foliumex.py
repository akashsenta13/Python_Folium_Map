import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# function to get lat and lang from address
def do_geocode(address):
    try:
        return nom.geocode(address, timeout=10)
    except GeocoderTimedOut:
        return do_geocode(address)


nom = Nominatim()

# map object from folium
map = folium.Map(location=[23.13, 72.53])


f = open('kotaatm.txt', 'r')

cordinates = []

for line in f.readlines():
    location = do_geocode(line)
    if location != None:
        cordinates.append([location.latitude, location.longitude])

f.close()

print(cordinates)

fg = folium.FeatureGroup(name='MyMap')


for cord in cordinates:
    fg.add_child(folium.Marker(
        location=cord, popup='Kotak ATM', icon=folium.Icon(color='red')))

map.add_child(fg)

# map save with html format
map.save('map.html')

print('map is saved')
