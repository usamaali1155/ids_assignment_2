# 28 March 24
# CSC461 – Assignment2 – IDS – Data Visualization
# Usama Ali
# FA20-BSE-025
#Question3: [CLO-2] - [Bloom Taxonomy Level: <Applying>]
#The diamonds dataset contains 53,000 records with various attributes like carat, cut, color, clarity, price etc.
#Plot the relationship between ‘carat’ and ‘price’ of diamonds using a chart. Because it’s a large dataset, just
#plot the diamonds with a ‘clarify’ = ‘SI2’ and ‘color’ = ‘E’. Use the values of the ‘cut’ for colors in the plot.
#Make appropriate modifications to the chart title, axis titles, legend, figure size, font size, colors etc. to make
#the chart readable and visually appealing

import matplotlib.pyplot as plt
import seaborn as sns

diamonds_df = pd.read_csv('./diamonds.csv')
filtered_diamonds = diamonds_df[(diamonds_df['clarity'] == 'SI2') & (diamonds_df['color'] == 'E')]
plt.figure(figsize=(10, 6))
sns.scatterplot(data=filtered_diamonds, x='carat', y='price', hue='cut', palette='Set1')
plt.title('Relationship Between Carat and Price of Diamonds (Clarity=SI2, Color=E)')
plt.xlabel('Carat')
plt.ylabel('Price')
plt.legend(title='Cut')
plt.tight_layout()
plt.show()
