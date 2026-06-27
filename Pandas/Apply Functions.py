import pandas as pd

df = pd.DataFrame({'val':[1,2,3]})
df['sq'] = df['val'].apply(lambda x: x**2)
print(df)