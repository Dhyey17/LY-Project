import pandas as pd

df = pd.read_excel('dataset.xlsx')
print(df.head(20))

col = ['Sentence', 'Outcome']
df = df[col]
df.columns = ['Sentence', 'Outcome']
df['category_id'] = df['Outcome'].factorize()[0]
category_id_df = df[['Outcome', 'category_id']].drop_duplicates().sort_values('category_id')
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id', 'Outcome']].values)
print(df.head())
