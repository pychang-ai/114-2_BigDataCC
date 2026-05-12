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