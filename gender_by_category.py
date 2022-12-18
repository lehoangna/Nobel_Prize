import pandas as pd
import os
import matplotlib.pyplot as plt

file = pd.read_csv("nobel.csv")
female_winners = file.loc[file['sex'] == 'Female', ['year', 'category']].reset_index(drop= True)
female_winners['year'] = (female_winners['year'] // 10) * 10
female_winners = female_winners.groupby(['year', 'category']).size().reset_index(name= 'count')
# female_winners['year'] = pd.to_numeric(female_winners['year'])
print(female_winners.head())
female_winners = female_winners.pivot(index= 'year', columns= 'category', values= 'count').fillna(0)
female_winners.plot()
plt.ylabel('female_winners')
plt.yticks()

plt.show()

# print(female_winners.head())
