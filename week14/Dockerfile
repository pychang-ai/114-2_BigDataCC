# 1. 使用輕量版 Python 3.11 映像檔作為基底
FROM python:3.11-slim

# 2. 設定容器內的工作目錄為 /app
WORKDIR /app

# 3. 先複製套件清單（善用 Docker Layer Cache 快取機制）
COPY requirements.txt .

# 4. 安裝套件
RUN pip install --no-cache-dir -r requirements.txt

# 5. 複製目前目錄下的所有程式碼到容器的工作目錄
COPY . .

# 6. 宣告容器會監聽 5000 埠號
EXPOSE 5000

# 7. 容器啟動時執行的指令
CMD ["python", "app.py"]