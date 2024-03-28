# 28 March 24
# CSC461 – Assignment2 – IDS – Data Visualization
# Usama Ali
# FA20-BSE-025
#Question4: [CLO-2] - [Bloom Taxonomy Level: <Applying>]
#The nuclear waste dataset contains the locations of several nuclear waste storage sites in the US. Use map of
#the US to show these sites as markers on the map. Clicking on a marker should display the name of the site.
#pick the appropriate location, zoom level and images tiles for the map.

import pandas as pd
import folium
nuclear_waste_df = pd.read_csv('./nuclear_waste_sites.csv')
map_us = folium.Map(location=[37.0902, -95.7129], zoom_start=5)
for index, row in nuclear_waste_df.iterrows():
    folium.Marker([row['lat'], row['lon']], popup=row['text']).add_to(map_us)
map_us.save('./nuclear_waste_map.html')
