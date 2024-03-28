# 28 March 24
# CSC461 – Assignment2 – IDS – Data Visualization
# Usama Ali
# FA20-BSE-025
#Question2: [CLO-2] - [Bloom Taxonomy Level: <Applying>]
#Using the world population dataset (from Q1)
#• Show the population of 10 least populous countries in 2015 using a chart.
#• Calculate the change in population of Pakistan, India, United States, and United Kingdom from 1970
#to 2010 and show the population change (in millions) using a chart.
#• Calculate the Pakistan population growth between 2010-2020 and then show the data using a chart.

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
