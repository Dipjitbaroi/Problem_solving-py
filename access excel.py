import pandas as pd
df = pd.read_csv("data.csv")
df.drop_duplicates(subset="Full Name", keep="first", inplace=True)

df.to_csv('last updated sheet2.csv')
# df.head(8)
# print(df.to_string())