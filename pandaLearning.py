import pandas as pd


data = pd.read_csv("C:\\Users\\Harshg\\Downloads\\archive\\weather.csv")
#print(data)
data.fillna(0, inplace=True)
print(data["MinTemp"].max())
print(data["MaxTemp"][data["MinTemp"] > 19.0])
print(data["MinTemp"].mean())

data.to