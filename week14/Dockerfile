# 1. 使用輕量化基底
FROM python:3.11-slim

# 2. 設定工作目錄，後續指令都會在此目錄執行
WORKDIR /app

# 3. 先複製 requirements.txt (利用快取機制)
# 只要這個檔案沒改，重新 Build 時就不會重新安裝套件，速度極快
COPY requirements.txt .

# 4. 安裝套件
RUN pip install --no-cache-dir -r requirements.txt

# 5. 複製剩餘的程式碼 (例如 app.py)
COPY . .

# 6. 告知容器監聽的埠號 (僅供參考說明用)
EXPOSE 5000

# 7. 啟動指令
CMD ["python", "app.py"]