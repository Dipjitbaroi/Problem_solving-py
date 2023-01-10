import pandas as pd
data = pd.read_excel("Books1.xlsx")
data.drop_duplicates(subset="Marks",keep="first",inplace=True)
df = data
df.to_excel("Books1_Updated.xlsx")