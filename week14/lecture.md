# 第 14 週教學講義：Docker 基本操作與 Dockerfile

## 本週學習目標

1. 能夠執行 Docker 映像檔的拉取、列表、刪除操作
2. 能夠啟動、進入、停止、刪除 Docker 容器
3. 理解 Docker 容器的網路設定與埠號對應
4. 能夠撰寫基本 Dockerfile 並 build 自訂映像檔
5. 使用 AI 工具輔助撰寫 Dockerfile，並驗證正確性

---

## Part 1：確認 Docker 環境

在開始之前，先確認 Docker 正常運作：

```bash
docker version
docker info
```

`docker version` 會列出 Client 和 Server（Engine）版本。如果 Server 部分出現 `Cannot connect`，代表 Docker Desktop 還沒啟動。

```bash
# 執行一個測試容器，確認 Docker 完全正常
docker run hello-world
```

看到 `Hello from Docker!` 就代表環境 OK。

---

## Part 2：Docker 映像檔操作

映像檔（Image）是容器的「模板」，就像安裝光碟。容器從映像檔啟動，映像檔本身不會被修改。

### 2.1 拉取映像檔

```bash
# 從 Docker Hub 拉取 Ubuntu 映像檔（最新版）
docker pull ubuntu

# 拉取指定版本
docker pull ubuntu:22.04
docker pull python:3.11-slim
docker pull nginx:alpine
```

> **alpine** 是一個超小型 Linux 發行版（約 5MB），常用於製作輕量容器。`nginx:alpine` 比 `nginx:latest` 小很多。

### 2.2 列出映像檔

```bash
docker images
# 或
docker image ls
```

輸出欄位說明：

| 欄位 | 說明 |
|------|------|
| REPOSITORY | 映像檔名稱 |
| TAG | 版本標籤（latest = 最新版） |
| IMAGE ID | 映像檔的唯一識別碼（取前 12 碼） |
| CREATED | 建立時間 |
| SIZE | 映像檔大小 |

### 2.3 刪除映像檔

```bash
# 用名稱刪除
docker rmi nginx:alpine

# 用 IMAGE ID 刪除（ID 只要能識別唯一即可，不用全打）
docker rmi abc123

# 刪除所有沒被使用的映像檔（清理空間用）
docker image prune
```

> 如果映像檔正在被某個容器使用（即使是已停止的容器），直接刪除會失敗。要先刪容器，再刪映像檔。

---

## Part 3：Docker 容器操作

容器（Container）是映像檔的「執行實例」。從同一個映像檔可以同時跑多個容器，彼此獨立。

### 3.1 啟動容器

```bash
# 基本格式
docker run [選項] 映像檔名稱 [指令]

# 互動模式：進入容器的 bash shell（-i 互動 -t 終端機）
docker run -it ubuntu:22.04 bash

# 背景執行模式（Detached）：容器在背景跑，不佔用終端機
docker run -d nginx

# 同時命名容器（方便後續操作）
docker run -d --name my-nginx nginx

# 埠號對應：將主機的 8080 對應到容器的 80（外部存取容器服務用）
docker run -d --name my-nginx -p 8080:80 nginx
```

> `-p 主機埠:容器埠`：讓外部（你的瀏覽器）能透過主機的 8080 埠存取容器內跑在 80 埠的服務。

### 3.2 查看容器狀態

```bash
# 查看執行中的容器
docker ps

# 查看所有容器（包含已停止的）
docker ps -a
```

`docker ps` 輸出欄位：

| 欄位 | 說明 |
|------|------|
| CONTAINER ID | 容器的唯一識別碼 |
| IMAGE | 使用的映像檔 |
| COMMAND | 容器執行的指令 |
| CREATED | 建立時間 |
| STATUS | 狀態（Up = 執行中，Exited = 已停止） |
| PORTS | 埠號對應 |
| NAMES | 容器名稱 |

### 3.3 進入執行中的容器

```bash
# exec 進入已在背景執行的容器（-it 互動終端機）
docker exec -it my-nginx bash

# 在容器裡執行單一指令，不進入 shell
docker exec my-nginx nginx -v
```

> `exec` 和 `run` 的差異：`run` 是從映像檔新建並啟動一個容器，`exec` 是在**已執行的容器**裡再執行一個指令。

### 3.4 停止與刪除容器

```bash
# 停止容器（發送 SIGTERM，讓容器程序正常結束）
docker stop my-nginx

# 強制停止（發送 SIGKILL，立即終止）
docker kill my-nginx

# 刪除容器（容器必須先停止才能刪）
docker rm my-nginx

# 強制刪除執行中的容器
docker rm -f my-nginx

# 一次清除所有已停止的容器
docker container prune
```

### 3.5 查看容器 log

```bash
# 查看容器的輸出 log
docker logs my-nginx

# 即時追蹤 log（類似 tail -f）
docker logs -f my-nginx
```

---

## Part 4：Docker 容器網路

容器的網路隔離讓多個服務可以共存在同一台主機上，彼此不干擾。

```bash
# 列出所有 Docker 網路
docker network ls

# 預設有三個內建網路
# bridge：容器預設使用，同一個 bridge 網路的容器可以互通
# host：容器直接使用主機的網路（無隔離）
# none：沒有網路
```

### 埠號對應（Port Mapping）

```bash
# 將主機 8080 對應到容器 80（HTTP）
docker run -d -p 8080:80 nginx

# 對應多個埠
docker run -d -p 8080:80 -p 8443:443 nginx

# 主機任意埠（讓 Docker 自動選擇）
docker run -d -p 80 nginx
docker port <容器ID>  # 查詢 Docker 選了哪個埠
```

---

## Part 5：Dockerfile 入門

Dockerfile 是建立自訂映像檔的「食譜」，描述從哪個基底映像檔開始、要安裝什麼、要執行什麼。

### 5.1 基本語法

| 指令 | 用途 | 範例 |
|------|------|------|
| `FROM` | 指定基底映像檔（第一行必須有） | `FROM python:3.11-slim` |
| `WORKDIR` | 設定容器內的工作目錄 | `WORKDIR /app` |
| `COPY` | 複製本機檔案到容器內 | `COPY . .` |
| `RUN` | 在 build 時執行指令（安裝套件等） | `RUN pip install flask` |
| `EXPOSE` | 宣告容器監聽的埠號（文件用途） | `EXPOSE 5000` |
| `CMD` | 容器啟動後執行的預設指令 | `CMD ["python", "app.py"]` |
| `ENV` | 設定環境變數 | `ENV PORT=5000` |

### 5.2 範例：Python Flask 海事資料 API

**專案結構：**
```
ship-api/
├── Dockerfile
├── requirements.txt
└── app.py
```

**app.py：**
```python
from flask import Flask, jsonify

app = Flask(__name__)

ships = [
    {"id": 1, "name": "Ever Given", "type": "Container", "tonnage": 220940},
    {"id": 2, "name": "Formosa 1", "type": "Bulk", "tonnage": 85000},
    {"id": 3, "name": "Ocean Star", "type": "Tanker", "tonnage": 95000},
]

@app.route("/")
def index():
    return jsonify({"message": "高雄港船舶資料 API", "version": "1.0"})

@app.route("/ships")
def get_ships():
    return jsonify(ships)

@app.route("/ships/<int:ship_id>")
def get_ship(ship_id):
    ship = next((s for s in ships if s["id"] == ship_id), None)
    if ship:
        return jsonify(ship)
    return jsonify({"error": "找不到此船舶"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

**requirements.txt：**
```
flask==3.0.0
```

**Dockerfile：**
```dockerfile
# Step 1：從輕量 Python 3.11 映像檔開始
FROM python:3.11-slim

# Step 2：設定容器內工作目錄
WORKDIR /app

# Step 3：先複製 requirements.txt（利用 Docker cache 加速 build）
COPY requirements.txt .

# Step 4：安裝 Python 套件（build time 執行）
RUN pip install --no-cache-dir -r requirements.txt

# Step 5：複製所有程式碼到容器
COPY . .

# Step 6：宣告此容器使用 5000 埠
EXPOSE 5000

# Step 7：容器啟動後執行 Flask
CMD ["python", "app.py"]
```

### 5.3 Build 與執行

```bash
# 在 Dockerfile 所在目錄執行 build
# -t 指定映像檔名稱與標籤，. 表示當前目錄
docker build -t ship-api:v1 .

# 查看剛 build 好的映像檔
docker images

# 啟動容器，將主機 8080 對應到容器 5000
docker run -d --name ship-api -p 8080:5000 ship-api:v1

# 測試 API（在主機上執行）
curl http://localhost:8080/
curl http://localhost:8080/ships
```

### 5.4 Docker Build Cache

Docker 在 build 時會快取每個 `RUN`/`COPY` 步驟。如果某行指令的輸入沒變，就直接用快取，大幅縮短 build 時間。

> **最佳實踐**：先複製 `requirements.txt` 並安裝套件，再複製其他程式碼。這樣只要套件清單沒變，`pip install` 就能用快取，只有程式碼改變時才重新複製。

```dockerfile
# 好的寫法（善用 cache）
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# 不好的寫法（每次改任何程式碼都要重新 pip install）
COPY . .
RUN pip install -r requirements.txt
```

---

## Part 6：AI 輔助 Docker

本週導入 AI 工具輔助撰寫 Dockerfile。

### 6.1 有效的 Prompt 技巧

**給 AI 的資訊：**
1. 程式語言與版本
2. 應用程式的功能
3. 需要的套件
4. 監聽的埠號
5. 啟動指令

**範例 Prompt：**
```
我有一個 Python 3.11 的 Flask 應用程式，分析高雄港 AIS 船舶資料。
requirements.txt 中有 flask、pandas、numpy。
應用程式監聽 5000 埠，啟動指令是 python app.py。
請幫我寫一個使用 python:3.11-slim 基底映像的 Dockerfile，要善用 build cache。
```

### 6.2 驗證 AI 產出的原則

AI 寫出來的 Dockerfile **不一定正確**，使用前必須：

1. **理解每一行的用途** — 能解釋每個指令為什麼需要
2. **實際 Build 確認** — `docker build` 沒報錯才算可用
3. **測試功能** — `docker run` 後確認服務正常回應
4. **檢查安全性** — 避免把秘密（API key、密碼）寫進 Dockerfile 或 image

> **核心原則：先理解再使用。** 無法解釋的程式碼不應該提交。

---

## 本週重點回顧

| 指令 | 功能 |
|------|------|
| `docker pull <image>` | 拉取映像檔 |
| `docker images` | 列出本機映像檔 |
| `docker rmi <image>` | 刪除映像檔 |
| `docker run -d -p 8080:80 --name xxx <image>` | 背景啟動容器並對應埠號 |
| `docker ps -a` | 查看所有容器 |
| `docker exec -it <name> bash` | 進入執行中的容器 |
| `docker stop / rm <name>` | 停止 / 刪除容器 |
| `docker logs <name>` | 查看容器 log |
| `docker build -t <name>:<tag> .` | 從 Dockerfile 建立映像檔 |
| `docker container prune` | 清除已停止的容器 |
