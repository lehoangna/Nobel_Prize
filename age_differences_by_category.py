import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

file = pd.read_csv("nobel.csv")
file = file.loc[:, ['year', 'category', 'birth_date']]
file['birth_date'] = file['birth_date'].str[0:4]
file.loc[:, ['year', 'birth_date']] = file.loc[:, ['year', 'birth_date']].apply(pd.to_numeric)
file['age'] = (file['year'] - file['birth_date'])

chemistry = file.loc[file.category == 'Chemistry', :]
literature = file.loc[file.category == 'Literature', :]
medicine = file.loc[file.category == 'Medicine', :]
peace = file.loc[file.category == 'Peace', :]
physics = file.loc[file.category == 'Physics', :]
economics = file.loc[file.category == 'Economics', :]

fig = plt.figure()
fig, axes = plt.subplots(2, 3, figsize= (16,12))

plt.xlim((1850, 2060))

sns.regplot(ax=axes[0,0], x=chemistry['year'], y=chemistry['age'], data=chemistry['age'], scatter_kws={'s':16}, truncate= False).set(title='Chemistry', xlim=(1850, 2060), ylim=(10,95))
sns.regplot(ax=axes[0,1], x=literature['year'], y=literature['age'], data=literature['age'], scatter_kws={'s':16}, truncate= False).set(title='Literature', xlim=(1850, 2060), ylim=(10,95))
sns.regplot(ax=axes[0,2], x=medicine['year'], y=medicine['age'], data=medicine['age'], scatter_kws={'s':16}, truncate= False).set(title='Medicine', xlim=(1850, 2060), ylim=(10,95))
sns.regplot(ax=axes[1,0], x=peace['year'], y=peace['age'], data=peace['age'], scatter_kws={'s':16}, truncate= False).set(title='Peace', xlim=(1850, 2060), ylim=(10,95))
sns.regplot(ax=axes[1,1], x=physics['year'], y=physics['age'], data=physics['age'], scatter_kws={'s':16}, truncate= False).set(title='Physics', xlim=(1850, 2060), ylim=(10,95))
sns.regplot(ax=axes[1,2], x=economics['year'], y=economics['age'], data=economics['age'], scatter_kws={'s':16}, truncate= False).set(title='Economics', xlim=(1850, 2060), ylim=(10,95))

plt.xlim(1850, 2060)
plt.show()
# print(file.head())