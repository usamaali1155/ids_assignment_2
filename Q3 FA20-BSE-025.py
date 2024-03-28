import pandas as pd
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
