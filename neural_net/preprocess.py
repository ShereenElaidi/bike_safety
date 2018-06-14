import pandas as pd

df = pd.read_csv("raw_data.csv")

road_1 = df['RUE_ACCDN']
road_2 = df['ACCDN_PRES_DE']


df.RUE_ACCDN = df.RUE_ACCDN.str.replace('\d+', '')
df.ACCDN_PRES_DE = df.ACCDN_PRES_DE.str.replace('\d+', '')

print(df)

df = df.drop_duplicates(subset='RUE_ACCDN', keep = 'first')
print(df)
df = df.drop_duplicates(subset='ACCDN_PRES_DE', keep = 'first')
print(df)
