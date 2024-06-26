# 28 March 24
# CSC461 – Assignment2 – IDS – Data Visualization
# Usama Ali
# FA20-BSE-025
#Question5: [CLO-2] - [Bloom Taxonomy Level: <Applying>]
#The Pakistan heritage sites dataset contains the geo locations of a number of heritage sites across Pakistan.
#Show these sites as markers on a map of the Pakistan. Clicking on a marker should display the name of the
#site. Pick the appropriate location, zoom level and images tiles for the map.

import pandas as pd
import folium

heritage_sites_df = pd.read_csv('./pak-heritage-sites.csv')
map_pakistan = folium.Map(location=[30.3753, 69.3451], zoom_start=5)

for index, row in heritage_sites_df.iterrows():
    folium.Marker([row['lat'], row['lon']], popup=row['site_name']).add_to(map_pakistan)

map_pakistan.save('./pakistan_heritage_sites_map.html')
