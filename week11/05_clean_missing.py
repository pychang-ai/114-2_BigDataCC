import pandas as pd

df = pd.read_csv("students.csv")

# 找出哪些 cell 是缺失值
print(df.isna())

# 各欄缺失值數量
print(df.isna().sum())

# 方法一：直接刪除有缺失的列
df_drop = df.dropna()
print("刪除後筆數：", len(df_drop))

# 方法二：用平均值補缺失值（適合數值欄）
df_fill_mean = df.copy()
df_fill_mean["國文"] = df_fill_mean["國文"].fillna(df_fill_mean["國文"].mean())
df_fill_mean["英文"] = df_fill_mean["英文"].fillna(df_fill_mean["英文"].mean())
print(df_fill_mean)

# 方法三：用固定值補（例如 0 分代表缺考）
df_fill_zero = df.fillna(0)
print(df_fill_zero)

import pandas as pd

df = pd.read_csv("students.csv")

# 找出重複列
print(df[df.duplicated()])

# 移除重複（保留第一筆）
df_unique = df.drop_duplicates()
print("去重後筆數：", len(df_unique))

# 只看特定欄位重複（例如學號相同就算重複）
df_unique2 = df.drop_duplicates(subset=["學號"])

import pandas as pd

df = pd.read_csv("students.csv")
print(df.dtypes)

# 把年齡轉成 float
df["年齡"] = df["年齡"].astype(float)

# 把學號當字串處理（避免被當數字）
df["學號"] = df["學號"].astype(str)

# 文字欄位的清洗
df["城市"] = df["城市"].str.strip()       # 去除前後空白
df["姓名"] = df["姓名"].str.upper()       # 全部轉大寫（範例）

import pandas as pd

df = pd.read_csv("students.csv").drop_duplicates()

# 條件篩選：高雄的學生
df_kh = df[df["城市"] == "高雄"]
print(df_kh)

# 多條件：高雄且數學 > 80
df_kh_high = df[(df["城市"] == "高雄") & (df["數學"] > 80)]
print(df_kh_high)

# 排序：依數學成績由高到低
df_sorted = df.sort_values("數學", ascending=False)
print(df_sorted)

# 用 loc 同時選列和欄
print(df.loc[df["城市"] == "高雄", ["姓名", "數學"]])