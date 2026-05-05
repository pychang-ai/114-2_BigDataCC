import pandas as pd

# Step 1：讀取
df = pd.read_csv("students.csv")
print(f"原始資料：{df.shape}")

# Step 2：去除重複
df = df.drop_duplicates()
print(f"去重後：{df.shape}")

# Step 3：補缺失值（國文、英文用平均補）
for col in ["國文", "英文", "數學"]:
    df[col] = df[col].fillna(df[col].mean())

# Step 4：新增「總分」與「平均」欄位
df["總分"] = df["國文"] + df["英文"] + df["數學"]
df["平均"] = df["總分"] / 3

# Step 5：依平均排序
df = df.sort_values("平均", ascending=False)

# Step 6：輸出乾淨資料
df.to_csv("students_cleaned.csv", index=False, encoding="utf-8-sig")
print("已輸出 students_cleaned.csv")
print(df)