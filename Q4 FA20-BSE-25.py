import pandas as pd
import folium
nuclear_waste_df = pd.read_csv('./nuclear_waste_sites.csv')
map_us = folium.Map(location=[37.0902, -95.7129], zoom_start=5)
for index, row in nuclear_waste_df.iterrows():
    folium.Marker([row['lat'], row['lon']], popup=row['text']).add_to(map_us)
map_us.save('./nuclear_waste_map.html')