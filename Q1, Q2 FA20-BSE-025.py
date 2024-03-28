# 28 March 24
# CSC461 – Assignment2 – IDS – Data Visualization
# Usama Ali
# FA20-BSE-025
# Question1: [CLO-2] - [Bloom Taxonomy Level: <Applying>]
#The world population dataset provides population data from 1960 to 2020 for countries around the world.
#Compare the populations of top 10 highest populated countries (in 2020) over the entire period using a chart.
#Make appropriate modifications to the chart title, axis titles, legend, figure size, font size, colors etc. to make
#the chart readable and visually appealing.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./world_pop.csv')
df_melted = df.melt(id_vars=['country'], var_name='year', value_name='population')
df_melted['year'] = df_melted['year'].str.extract('(\d+)$').astype(int)

# Question 1: Compare populations of top 10 highest populated countries from 1960 to 2020
top_countries_2020 = df_melted[df_melted['year'] == 2020].nlargest(10, 'population')
top_countries_over_time = df_melted[df_melted['country'].isin(top_countries_2020['country'])]
pivot_df = top_countries_over_time.pivot(index='year', columns='country', values='population')

plt.figure(figsize=(14, 8))
pivot_df.plot(kind='line', marker='o')
plt.title('Population Growth of Top 10 Populated Countries (1960-2020)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Question 2: Part 1 - Show the population of the 10 least populous countries in 2015
least_countries_2015 = df_melted[df_melted['year'] == 2015].nsmallest(10, 'population')

plt.figure(figsize=(10, 6))
plt.bar(least_countries_2015['country'], least_countries_2015['population'], color='skyblue')
plt.title('10 Least Populous Countries in 2015')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Question 2: Part 2 - Calculate and show the population change for specified countries from 1970 to 2010
countries_of_interest = ['Pakistan', 'India', 'United States', 'United Kingdom']
df_interest = df_melted[(df_melted['country'].isin(countries_of_interest)) & (df_melted['year'].isin([1970, 2010]))]
pivot_interest = df_interest.pivot(index='country', columns='year', values='population')
pivot_interest['change_in_millions'] = (pivot_interest[2010] - pivot_interest[1970]) / 1e6

plt.figure(figsize=(10, 6))
pivot_interest['change_in_millions'].plot(kind='bar', color='orange')
plt.title('Population Change from 1970 to 2010 (in millions)')
plt.xlabel('Country')
plt.ylabel('Population Change (in millions)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Question 2: Part 3 - Calculate the Pakistan population growth between 2010-2020
pakistan_growth = df_melted[(df_melted['country'] == 'Pakistan') & (df_melted['year'].isin([2010, 2020]))]
pakistan_growth.set_index('year', inplace=True)
pakistan_growth_diff = (pakistan_growth.loc[2020, 'population'] - pakistan_growth.loc[2010, 'population']) / 1e6

print(f'Pakistan Population Growth from 2010 to 2020: {pakistan_growth_diff} million')
