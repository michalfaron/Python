import pandas as pd
import numpy as np

df = pd.DataFrame([[12, 25, 2019, 10], [1, 15, 2020, 11]], columns=["month", "day", "year", "hour"])
pd.to_datetime(df[["month", "day", "year"]])
df.index = pd.to_datetime(df[["month", "day", "year"]])


print(df.head())
