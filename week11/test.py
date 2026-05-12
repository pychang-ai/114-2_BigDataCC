import os
import pandas as pd

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "students.csv")

df = pd.read_csv(file_path)

# 挑戰一
top3 = df.dropna(subset=["數學"])\
         .sort_values(by="數學", ascending=False)\
         .head(3)

print("=== 數學前3名 ===")
print(top3[["學號", "姓名", "數學"]])

# 挑戰二
print("\n=== 各城市平均數學 ===")
print(df.groupby("城市")["數學"].mean().reset_index())

# 挑戰三
missing_df = df[df.isnull().any(axis=1)]
output_path = os.path.join(base_dir, "students_missing.csv")
missing_df.to_csv(output_path, index=False)