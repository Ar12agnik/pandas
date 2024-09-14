import pandas as pd

df = pd.read_csv('data2.csv')

df['Date'] = pd.to_datetime(df['Date'],format='mixed')

print(df.to_string())

df.dropna(subset = ['Date'],inplace = True )
print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df.duplicated())
print(df.corr())