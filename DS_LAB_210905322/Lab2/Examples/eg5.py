import pandas as pd
import numpy as np

dates=pd.date_range('20130101', periods=100)
df = pd.DataFrame(np.random.randn(100,4), index=dates, columns=list('ABCD'))
'''
#To view first 5 records
print(df.head())
print('')
print("")

#To view last 5 records
print((df.tail()))
print('')
print("")
#To view the index
print(df.index)
print('')
print("")
#To view the column names
print(df.columns)
print('')
print("")
#To transpose the df
print(df.T.head())
print('')
print("")
#Sorting by Axis
print(df.sort_index(axis=1, ascending=False).head())
print('')
print("")
#Sorting by Values
print(df.sort_values(by='B').head())
print('')
print("")
'''
#Slicing the rows
print(df[0:3]) #which slice first 3 records (rows)
print('')
print("")
#Slicing with index name
print(df['20130105':'20130110'])
print('')
print("")
#Slicing with row and column index (like 2D Matrix)
print(df.iloc[0])# will fetch entire 1 st rowprint('')
print("")
print(df.iloc[0,:2])# will fetch 1 st row, first 2 columnsprint('')
print("")
print(df.iloc[0,0])# will fetch 1 st row, 1 st column element (single element)print('')
print("")
print('')
print("")
#Selecting a single column
print(df['A'].head())# which yields a Series
print('')
print("")
#Selecting more than one column
print(df[['A','B']].head())# entire 2 columns
print('')
print("")
#Selecting more than one column, with selected number of records
print(df[['A','B']][:5])# first 5 recordsprint('')
print("")
print(df.loc['20130101':'20130105',['A','B']][:5].head())# first 5 recordsprint('')
print("")