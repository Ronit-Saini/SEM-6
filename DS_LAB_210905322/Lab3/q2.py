import pandas as pd


df = pd.DataFrame({'a': [10,20],'b':[100,200]})

df.loc['Column_Total']= df.sum(numeric_only=True, axis=0)
df.loc[:,'Row_Total'] = df.sum(numeric_only=True, axis=1)

print(df)


'''
import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
rowSum = np.sum(A, axis = 1)
print('Row Sum is ', rowSum)
colSum = np.sum(A, axis = 0)
print('Column Sum is ', colSum)'''