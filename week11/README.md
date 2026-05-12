# 第 11 週教學講義：Pandas 資料清洗

## 本週課本主題

**第 7 章 使用 VS Code 在 WSL 與 GitHub 開發應用程式**

- 7-1 下載與安裝 Visual Studio Code
- 7-2 使用 WSL 2 + Node.js 建立 Web 伺服器
- 7-3 使用 WSL 2 + Python 進行 Web 開發
- 7-4 認識 Git 與 GitHub
- 7-5 使用 GitHub 檔案庫進行 VS Code 專案開發

---

> ⚠️ **本週為書外補充教材**——課本《你的第一本 Linux 入門書》（陳會安，博碩文化）Ch 6 著重 Miniconda 環境與 GPU 配置，**未涵蓋 Pandas 資料處理**。本週為老師補充內容，後續 W12 視覺化會回到課本 6-4 Jupyter Notebook。

---

## 為什麼這週要學 Pandas？

三個現實理由：

1. **期末專題用得到**：你的專題要做海事/海洋資料分析（船舶 AIS、港口進出、氣象觀測），這些都是表格資料——Pandas 是 Python 處理表格的**標準工具**。沒會 Pandas 等於沒做專題。

2. **AI 輔助時的「驗證能力」基礎**：本週起導入 **AI 輔助資料清洗**，但你必須自己會做，才看得出 AI 哪裡寫錯。**先理解再使用**——這是課程 W10 起的核心原則。

3. **海事資料現場**：高雄港船舶資料、中央氣象署海象觀測、海委會公開資料集，全部都是 CSV / Excel 表格——出社會後第一份工作很可能就是「把這份表格清乾淨」。

> 📌 學會 Pandas，你就掌握了「**讀資料 → 清資料 → 看資料**」這個資料分析的起手式。

---

## 本週學習目標

1. 在 W10 建好的 conda 環境中安裝並驗證 Pandas、NumPy
2. 認識 NumPy 一維與二維陣列，理解向量化運算
3. 認識 Pandas 的 Series 與 DataFrame 兩個核心物件
4. 學會讀取 CSV 檔案，並輸出處理後的結果
5. 學會用 head/tail/info/describe 快速探索資料
6. 學會處理缺失值、重複值，並做資料型態轉換
7. 學會用條件篩選與排序取出想要的資料子集

---

## 前置：環境確認與套件安裝

> 本週所有操作都在 W10 建好的 conda 環境中進行，請先確認環境狀態。

### Step 1：啟動 W10 建立的 conda 環境

開啟 VS Code，按 `` Ctrl + ` `` 開啟終端機，執行：

```bash
# 確認環境清單，找出上週建的 bigdatacc 環境
conda env list

# 啟動環境
conda activate bigdatacc

# 確認 Python 版本
python --version
```

啟動後，提示符會出現 `(bigdatacc)` 字樣，代表你已進入該環境。

### Step 2：安裝 pandas 與 numpy

```bash
# 在 bigdatacc 環境中安裝
pip install pandas numpy

# 驗證安裝
python -c "import pandas, numpy; print(pandas.__version__, numpy.__version__)"
```

若看到兩個版本號（例如 `2.2.0 1.26.4`），代表安裝成功。

### Step 3：建立本週工作資料夾

```bash
# 在你習慣的位置建立資料夾
mkdir week11_pandas
cd week11_pandas

# 用 VS Code 開啟資料夾
code .
```

### 課堂操作建議

本週示範以 `.py` 檔搭配 VS Code 的「在終端機執行 Python 檔案」按鈕進行。下週 W12 會導入 Jupyter Notebook，提供更適合資料分析的互動環境。

---

## 1. NumPy 基礎：Pandas 的地基

> NumPy 是 Pandas 底層的運算引擎。先理解 NumPy，後面學 Pandas 會輕鬆很多。

### 1.1 為什麼需要 NumPy

Python 內建的 list 雖然好用，但在處理大量數值時速度慢、語法繁瑣。NumPy 提供 `ndarray` 物件，讓你能以**整批運算**取代 for 迴圈，速度可快上數十倍。

| 任務 | Python list | NumPy array |
|---|---|---|
| 把每個元素 +1 | for 迴圈逐項加 | `arr + 1` 一行搞定 |
| 兩個序列相加 | zip + for | `arr1 + arr2` |
| 算平均、標準差 | 自己寫公式 | `arr.mean()`、`arr.std()` |

### 1.2 建立 NumPy 陣列

新建檔案 `01_numpy_basic.py`：

```python
import numpy as np

# 從 list 建立一維陣列
a = np.array([1, 2, 3, 4, 5])
print("一維陣列：", a)
print("形狀：", a.shape)      # (5,)
print("型態：", a.dtype)      # int64

# 建立二維陣列
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print("二維陣列：")
print(b)
print("形狀：", b.shape)      # (2, 3)

# 常用建構函數
zeros = np.zeros((2, 3))      # 全 0 陣列
ones = np.ones((2, 3))        # 全 1 陣列
rng = np.arange(0, 10, 2)     # 0, 2, 4, 6, 8
linspace = np.linspace(0, 1, 5)   # 0 到 1 等分 5 點

print("zeros:", zeros)
print("arange:", rng)
print("linspace:", linspace)
```

### 1.3 向量化運算

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])

# 整批運算，不需要 for 迴圈
print(a + 10)         # [11 12 13 14 15]
print(a * 2)          # [2 4 6 8 10]
print(a ** 2)         # [1 4 9 16 25]

# 統計
print("總和：", a.sum())
print("平均：", a.mean())
print("最大：", a.max())
print("標準差：", a.std())

# 條件篩選
mask = a > 2
print("布林遮罩：", mask)         # [False False True True True]
print("大於 2 的元素：", a[mask])  # [3 4 5]
```

**🤖 AI 使用提示**：若你忘記某個 NumPy 函數，可以問 AI「NumPy 怎麼算陣列的中位數？」，但拿到答案後請先在小資料上驗證再用到正式程式中。

---

## 2. Pandas 核心物件：Series 與 DataFrame

Pandas 在 NumPy 之上多包了兩層。Series 是一維帶索引的陣列，DataFrame 是二維表格。

### 2.1 Series：帶索引的一維資料

新建 `02_pandas_series.py`：

```python
import pandas as pd

# 從 list 建立 Series（會自動產生 0,1,2... 索引）
s1 = pd.Series([10, 20, 30, 40])
print(s1)

# 自訂索引
s2 = pd.Series([85, 92, 78, 64],
               index=["國文", "英文", "數學", "自然"])
print(s2)
print("數學分數：", s2["數學"])
print("平均：", s2.mean())

# 從 dict 建立
score = {"小明": 85, "小華": 92, "小美": 78}
s3 = pd.Series(score)
print(s3)
```

### 2.2 DataFrame：二維表格

```python
import pandas as pd

# 從 dict 建立 DataFrame，dict 的 key 變成欄位名
data = {
    "姓名": ["小明", "小華", "小美", "小強"],
    "年齡": [20, 21, 19, 22],
    "成績": [85, 92, 78, 64],
    "城市": ["高雄", "台北", "高雄", "台中"]
}
df = pd.DataFrame(data)
print(df)
```

輸出：

```
   姓名  年齡  成績  城市
0  小明  20  85  高雄
1  小華  21  92  台北
2  小美  19  78  高雄
3  小強  22  64  台中
```

### 2.3 重要屬性

| 屬性 | 用途 |
|---|---|
| `df.shape` | 形狀（列數、欄數） |
| `df.columns` | 欄位名稱 |
| `df.index` | 列索引 |
| `df.dtypes` | 各欄位資料型態 |
| `df.values` | 底層 NumPy 陣列 |

```python
print("形狀：", df.shape)         # (4, 4)
print("欄位：", df.columns.tolist())  # ['姓名', '年齡', '成績', '城市']
print("型態：")
print(df.dtypes)
```

---

## 3. 讀取與寫入資料

### 3.1 準備一份練習用 CSV

新建檔案 `students.csv`，貼入以下內容：

```csv
學號,姓名,年齡,國文,英文,數學,城市
S001,王小明,20,85,72,90,高雄
S002,陳小華,21,92,88,76,台北
S003,林小美,19,78,,82,高雄
S004,張小強,22,64,71,55,台中
S005,黃小芳,20,,95,88,高雄
S006,李大同,23,80,82,79,台南
S007,周阿仁,19,72,68,71,高雄
S008,吳秀英,21,89,91,93,台北
S008,吳秀英,21,89,91,93,台北
```

注意：第 4、6 列各有一個空白成績（缺失值），最後兩列完全相同（重複值），這是刻意設計來練習資料清洗的。

### 3.2 讀取 CSV

新建 `03_read_data.py`：

```python
import pandas as pd

# 讀取 CSV
df = pd.read_csv("students.csv")
print(df)

# 讀取時可以指定編碼（Windows 常見問題）
# df = pd.read_csv("students.csv", encoding="utf-8")
# df = pd.read_csv("students.csv", encoding="big5")
```

### 3.3 寫出 CSV

```python
# 寫出（不要寫出 index 欄）
df.to_csv("students_copy.csv", index=False, encoding="utf-8-sig")

# Excel 也可以（需先 pip install openpyxl）
# df.to_excel("students.xlsx", index=False)
```

**常見錯誤**：Windows 用 Excel 開 UTF-8 CSV 會亂碼。把 `encoding="utf-8-sig"` 帶上即可。

---

## 4. 資料探索：先看資料長什麼樣子

> 拿到任何新資料的第一動作：先用四個指令看清楚它的樣子。

新建 `04_explore.py`：

```python
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
```

| 指令 | 看什麼 |
|---|---|
| `df.head(n)` | 前 n 筆，預設 5 筆 |
| `df.tail(n)` | 後 n 筆 |
| `df.info()` | 列數、欄位型態、非空數量 |
| `df.describe()` | 數值欄的 count/mean/std/min/max/分位數 |
| `df.isna().sum()` | 各欄缺失值數量 |
| `df.duplicated().sum()` | 重複列總數 |

---

## 5. 資料清洗：把髒資料變乾淨

真實資料常有缺失、重複、型態錯誤。這是資料分析中最花時間的環節。

### 5.1 處理缺失值

新建 `05_clean_missing.py`：

```python
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
```

| 場景 | 建議做法 |
|---|---|
| 缺失比例很低 | dropna 直接刪 |
| 數值欄、缺失隨機 | fillna 補平均/中位數 |
| 缺失代表「未發生」 | fillna(0) |
| 缺失有意義 | 保留，並記錄為「未填」類別 |

### 5.2 處理重複值

```python
import pandas as pd

df = pd.read_csv("students.csv")

# 找出重複列
print(df[df.duplicated()])

# 移除重複（保留第一筆）
df_unique = df.drop_duplicates()
print("去重後筆數：", len(df_unique))

# 只看特定欄位重複（例如學號相同就算重複）
df_unique2 = df.drop_duplicates(subset=["學號"])
```

### 5.3 資料型態轉換

```python
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
```

### 5.4 篩選與排序

```python
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
```

| 工具 | 用途 |
|---|---|
| `df[df["欄"] == 值]` | 條件篩選列 |
| `df[(條件1) & (條件2)]` | 多條件，用 `&` 連接（不是 `and`） |
| `df.sort_values("欄")` | 依欄位排序 |
| `df.loc[列條件, 欄清單]` | 同時選列和欄 |
| `df.iloc[列號, 欄號]` | 用整數位置選 |

---

## 6. 綜合練習：一條龍清洗流程

新建 `06_pipeline.py`，把前面學到的串起來：

```python
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
```

跑完後打開 `students_cleaned.csv`，你會得到一份乾淨、可直接用於分析的資料。

---

## 7. 常見錯誤與排錯指引

| 錯誤訊息 | 原因 | 解法 |
|---|---|---|
| `ModuleNotFoundError: pandas` | 沒裝或裝錯環境 | 先 `conda activate bigdatacc`，再 `pip install pandas` |
| `UnicodeDecodeError` | CSV 編碼不對 | `pd.read_csv(..., encoding="big5")` 或 `encoding="utf-8-sig"` |
| `SettingWithCopyWarning` | 對切片做修改 | 改用 `.loc[列, 欄] = 值` 或先 `.copy()` |
| 中文欄位選不到 | 欄名前後有空白 | `df.columns = df.columns.str.strip()` |
| `.mean()` 算出 NaN | 欄位有缺失值且全是 NaN | 先 `fillna` 或檢查資料來源 |

---

## 8. 課堂小挑戰（不計分，課堂練習）

> 本週不需繳交作業。以下三題作為課堂練習，做不出來可以提問或互相討論。

1. **挑戰一**：把 `students.csv` 中數學分數最高的前 3 名印出來，只顯示學號、姓名、數學三欄。
2. **挑戰二**：算出每個城市的平均數學成績（提示：`groupby`，下週會更深入）。
3. **挑戰三**：把所有缺失成績的列獨立存成 `students_missing.csv`，給後續人工補登。

---

## AI 使用建議

- ✅ 卡關時可以問 AI「pandas 怎麼把多個欄位同時 fillna？」並理解後再使用
- ✅ 看不懂錯誤訊息時，把錯誤訊息整段貼給 AI 請它解釋
- ❌ 不要把整題丟給 AI 然後直接抄答案
- ❌ 不要在貼程式碼前先檢查是否有個資（學生資料、API 金鑰）

更深入的 Pandas 進階用法（merge、pivot、time series），會在後續 Docker 部署 + 期末專題實作中視需求補充。
