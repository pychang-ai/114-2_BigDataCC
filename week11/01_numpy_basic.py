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