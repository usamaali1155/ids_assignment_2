import pandas as pd
import folium

heritage_sites_df = pd.read_csv('./pak-heritage-sites.csv')
map_pakistan = folium.Map(location=[30.3753, 69.3451], zoom_start=5)

for index, row in heritage_sites_df.iterrows():
    folium.Marker([row['lat'], row['lon']], popup=row['site_name']).add_to(map_pakistan)

map_pakistan.save('./pakistan_heritage_sites_map.html')
