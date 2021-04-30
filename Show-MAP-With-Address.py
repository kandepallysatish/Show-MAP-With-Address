#  SHOW MAP FULL ADDRESS

# MODULES TO INSTALL
from geopy.geocoders import Nominatim
import folium

#  METHOD TO SHOW MAP WITH FULL ADDRESS
locator = Nominatim(user_agent="myGeocoder")

#  ENTER THE ADDRESS YOU WANT TO SEARCH EXAMPLE YOUR COLLEGE NAME, OFFICE NAME,...
inp = input("Enter the address you want to search ")
location = locator.geocode(inp)
print(location.address)

# MARK INPUT LOCATION WITH LATITUDE AND LONGITUDE
print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
m = folium.Map(location=[location.latitude, location.longitude])
folium.Marker(
                location=[location.latitude, location.longitude],  # COORDINATES FOR THE MARKER
                icon=folium.Icon()
              ).add_to(m)
