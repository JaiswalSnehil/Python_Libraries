import pandas as pd

df = pd.DataFrame({'team':['A','A','B'],
                   'score':[10,20,30]})
print(df.groupby('team')['score'].sum())