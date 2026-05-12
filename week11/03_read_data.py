import pandas as pd

# 讀取 CSV
df = pd.read_csv("students.csv")
print(df)
df.to_csv("students_copy.csv", index=False, encoding="utf-8-sig")