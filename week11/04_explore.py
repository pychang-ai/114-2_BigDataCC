import pandas as pd

df = pd.read_csv("students.csv")

# 看前 5 筆（預設）
print(df.head())

# 看後 3 筆
print(df.tail(3))

# 看資料概況：列數、欄位型態、缺失值數
print(df.info())

# 看數值欄位的統計摘要
print(df.describe())

# 看每欄缺失值數量
print(df.isna().sum())

# 看重複列
print("重複列數：", df.duplicated().sum())