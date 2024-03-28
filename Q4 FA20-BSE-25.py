# 28 March 24
# CSC461 – Assignment2 – IDS – Data Visualization
# Usama Ali
# FA20-BSE-025
#Question3: [CLO-2] - [Bloom Taxonomy Level: <Applying>]
#The diamonds dataset contains 53,000 records with various attributes like carat, cut, color, clarity, price etc.
#Plot the relationship between ‘carat’ and ‘price’ of diamonds using a chart. Because it’s a large dataset, just
#plot the diamonds with a ‘clarify’ = ‘SI2’ and ‘color’ = ‘E’. Use the values of the ‘cut’ for colors in the plot.
#Make appropriate modifications to the chart title, axis titles, legend, figure size, font size, colors etc. to make
#the chart readable and visually appealing.

import pandas as pd
import folium
nuclear_waste_df = pd.read_csv('./nuclear_waste_sites.csv')
map_us = folium.Map(location=[37.0902, -95.7129], zoom_start=5)
for index, row in nuclear_waste_df.iterrows():
    folium.Marker([row['lat'], row['lon']], popup=row['text']).add_to(map_us)
map_us.save('./nuclear_waste_map.html')
