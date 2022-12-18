import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

file = pd.read_csv("nobel.csv")
file = file.loc[:, ['year', 'birth_date']]
file['birth_date'] = file['birth_date'].str[0:4]
file.loc[:, ['year', 'birth_date']] = file.loc[:, ['year', 'birth_date']].apply(pd.to_numeric)
file['age'] = (file['year'] - file['birth_date'])

sns.regplot(x=file['year'], y=file['age'],data=file['age'], scatter= True)

plt.show()