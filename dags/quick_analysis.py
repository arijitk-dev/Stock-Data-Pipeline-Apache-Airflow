import pandas as pd  

df = pd.read_csv("assessment/data/Mastercard_stock.csv")

print(df.head())
print(df.info())
print(df.describe())