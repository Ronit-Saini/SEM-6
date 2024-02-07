import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df.head())
print(df[df.A > 0])
df['F'] = ['Male', 'Female', 'Female', 'Male', 'Female', 'Female']
print(df[0:3])
df.loc[:, 'D'] = np.array([5] * len(df))
print(df.head())