# 第 14 週作業：Docker 基本操作與 Dockerfile

## 作業資訊

| 項目 | 說明 |
|------|------|
| 對應教科書 | 10-1 ~ 10-5 Docker 操作、12-1 認識 Dockerfile |
| 繳交方式 | 在 Fork 的 week14/ 資料夾中建立四個檔案，push 到 Fork |
| 繳交期限 | 下週上課前（6/2 上課前） |
| PR 標題 | 學號_姓名（已建立的 PR 會自動更新，不需重新建立） |

---

## 繳交步驟

1. 同步老師的最新版本：到你的 Fork 頁面點「**Sync fork**」>「**Update branch**」
2. 本機拉取最新版：`git pull origin main`
3. 建立作業資料夾：`mkdir week14`
4. 完成以下四題，在 `week14/` 中建立對應檔案
5. Push 到你的 Fork：
   ```bash
   git add week14/
   git commit -m "完成第14週作業"
   git push origin main
   ```
6. push 後 PR 會自動更新，不需重新開 PR

---

## 第 1 題：Docker 映像檔操作

> 練習環境：AWS EC2 或本機 Docker Desktop（已在 W13 安裝）

完成以下操作並將結果貼入 `week14/q1_images.txt`：

```
姓名：
學號：

=== 任務 1：確認 Docker 環境 ===

執行以下指令，確認 Docker 正常運作：
docker version

（貼上 Client 和 Server 的版本號，只需貼出 Version 那行即可）
Client Version:
Server Engine Version:

=== 任務 2：拉取映像檔 ===

依序拉取以下三個映像檔：
docker pull ubuntu:22.04
docker pull python:3.11-slim
docker pull nginx:alpine

（每個 pull 完成後，貼上最後一行輸出，例如 "Status: Downloaded newer image ..." 或 "Status: Image is up to date ..."）

ubuntu:22.04：
python:3.11-slim：
nginx:alpine：

=== 任務 3：列出映像檔 ===

執行：docker images
（貼上完整輸出）

=== 任務 4：刪除映像檔 ===

執行以下指令刪除 ubuntu:22.04：
docker rmi ubuntu:22.04

（貼上刪除後的輸出）

執行 docker images，確認 ubuntu:22.04 已移除：
（貼上刪除後的 docker images 輸出）

=== 觀念題 ===
Q1：映像檔（Image）和容器（Container）有什麼不同？
A1：

Q2：為什麼刪除映像檔前需要先刪除使用該映像檔的容器？
A2：
```

---

## 第 2 題：Docker 容器操作

完成以下操作並將結果貼入 `week14/q2_containers.txt`：

```
姓名：
學號：

=== 任務 1：啟動 nginx 容器 ===

執行以下指令，在背景啟動 nginx 並對應埠號：
docker run -d --name my-nginx -p 8080:80 nginx:alpine

（貼上輸出的容器 ID，例如 a1b2c3d4...）

=== 任務 2：查看容器狀態 ===

執行：docker ps
（貼上完整輸出，確認 my-nginx 的 STATUS 是 Up，PORTS 顯示 0.0.0.0:8080->80/tcp）

=== 任務 3：測試 nginx 服務 ===

在 AWS EC2 上執行：
curl http://localhost:8080

（貼上回傳的 HTML 內容，應包含 "Welcome to nginx!"）

=== 任務 4：進入容器 ===

執行：docker exec -it my-nginx sh

進入後執行以下指令並貼上結果：
1. hostname          （查看容器的 hostname）
2. ls /etc/nginx     （查看 nginx 設定目錄內容）
3. cat /etc/nginx/nginx.conf  （查看 nginx 設定，只貼前 10 行即可）

（hostname 輸出）：
（ls /etc/nginx 輸出）：

輸入 exit 離開容器。

=== 任務 5：查看容器 log ===

執行：docker logs my-nginx
（貼上最後 5 行 log 輸出）

=== 任務 6：停止並刪除容器 ===

docker stop my-nginx
docker rm my-nginx

執行 docker ps -a，確認 my-nginx 已移除：
（貼上 docker ps -a 輸出，確認清單中沒有 my-nginx）

=== 觀念題 ===
Q1：docker run -d 和 docker run -it 的使用時機有什麼不同？
A1：

Q2：-p 8080:80 的意思是什麼？如果把主機的 8080 改成 9090，應用程式的行為會有什麼不同？
A2：
```

---

## 第 3 題：撰寫 Dockerfile

> 本題要求你從頭建立一個 Python Flask 應用程式並 Docker 化。

在 `week14/` 目錄下建立以下三個檔案：

### 3.1 建立 `week14/app.py`

```python
from flask import Flask, jsonify

app = Flask(__name__)

# 高雄港船舶資料（簡化版）
ships = [
    {"id": 1, "name": "Ever Given", "type": "Container", "tonnage": 220940, "port": "Kaohsiung"},
    {"id": 2, "name": "Formosa 1", "type": "Bulk", "tonnage": 85000, "port": "Kaohsiung"},
    {"id": 3, "name": "Ocean Star", "type": "Tanker", "tonnage": 95000, "port": "Taichung"},
]

@app.route("/")
def index():
    return jsonify({"message": "高雄港船舶資料 API", "version": "1.0", "total_ships": len(ships)})

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
    app.run(host="0.0.0.0", port=5000, debug=False)
```

### 3.2 建立 `week14/requirements.txt`

```
flask==3.0.0
```

### 3.3 建立 `week14/Dockerfile`

根據講義 Part 5 的說明，撰寫 Dockerfile，需符合以下要求：

- 使用 `python:3.11-slim` 作為基底映像檔
- 工作目錄設為 `/app`
- **先複製 requirements.txt，安裝套件後，再複製其他程式碼**（善用 build cache）
- 容器監聽 5000 埠
- 啟動指令：`python app.py`

### 3.4 Build 並測試

```bash
# 在 week14/ 目錄下執行
docker build -t ship-api:v1 .
docker run -d --name ship-api -p 8080:5000 ship-api:v1

# 測試
curl http://localhost:8080/
curl http://localhost:8080/ships
curl http://localhost:8080/ships/1
```

完成後，將以下結果貼入 `week14/q3_dockerfile.txt`：

```
姓名：
學號：

=== 我撰寫的 Dockerfile 內容 ===
（貼上你寫的 Dockerfile 完整內容）

=== docker build 輸出 ===
（貼上 docker build 的最後 5 行，應出現 "Successfully built ..." 或 "naming to docker.io/..."）

=== docker images 確認 ===
（貼上 docker images | grep ship-api 的結果，確認映像檔存在）

=== API 測試結果 ===

curl http://localhost:8080/ 輸出：

curl http://localhost:8080/ships 輸出：

curl http://localhost:8080/ships/2 輸出：

=== 清理 ===
docker stop ship-api
docker rm ship-api

（執行完成後貼上 docker ps -a | grep ship-api 的結果，確認已清除）

=== 觀念題 ===
Q1：Dockerfile 中 RUN 和 CMD 有什麼不同？分別在什麼時候執行？
A1：

Q2：為什麼要先 COPY requirements.txt 安裝套件，再 COPY . . 複製程式碼？
   如果反過來，每次改 app.py 時會多做什麼事？
A2：
```

---

## 第 4 題：AI 輔助 Dockerfile

> 本題練習使用 AI 工具輔助撰寫 Dockerfile，並培養驗證 AI 產出的能力。

### 情境

你要為期末專題建立一個 Docker 化的資料分析應用，包含：
- Python 3.11
- 套件：pandas、numpy、matplotlib、seaborn
- 一個 Python 腳本 `analysis.py`，讀取 CSV 並產出圖表（儲存為 PNG，不需要 Flask）
- 啟動指令：`python analysis.py`

### 步驟

**Step 1：對 ChatGPT 或 Copilot 下達 Prompt**

使用以下 Prompt（可以修改），請 AI 撰寫 Dockerfile：

```
我要建立一個 Docker 容器來執行 Python 3.11 的資料分析腳本。
需要的套件：pandas、numpy、matplotlib、seaborn
程式碼只有一個檔案 analysis.py，啟動指令是 python analysis.py
資料輸入從 /app/data/ 目錄讀取 CSV 檔，分析結果的圖表存到 /app/output/ 目錄

請幫我寫一個 Dockerfile，注意：
1. 使用輕量化的 python:3.11-slim 作為基底
2. requirements.txt 和程式碼分開複製，善用 build cache
3. 加上必要的說明（用 # 開頭的註解）
```

**Step 2：在 `week14/q4_ai_dockerfile.txt` 記錄以下內容：**

```
姓名：
學號：

=== 我使用的 AI 工具 ===
（例如：ChatGPT GPT-4o / GitHub Copilot / Claude）

=== 我使用的 Prompt ===
（貼上你實際使用的 Prompt，可以是自己修改過的版本）

=== AI 產出的 Dockerfile ===
（貼上 AI 產出的完整 Dockerfile）

=== 逐行解釋 ===
請用自己的話，逐行解釋 AI 產出的 Dockerfile 中每一行的用途：
（每行一個說明，例如：
  FROM python:3.11-slim → 使用輕量版 Python 3.11 映像檔作為基礎，比完整版小約 80%
  WORKDIR /app → 設定容器內的工作目錄為 /app，之後的指令都在這個目錄下執行
  ...）

=== AI 產出是否有問題？ ===
請回答以下問題：

Q1：AI 有沒有把 requirements.txt 和程式碼分開複製？（有/沒有）
    如果沒有，這樣會有什麼問題？
A1：

Q2：AI 產出的 Dockerfile 中，有沒有使用 EXPOSE 指令？
    這個腳本需要 EXPOSE 嗎？為什麼？
A2：

Q3：AI 有沒有建立 /app/data/ 和 /app/output/ 目錄？
    如果沒有，容器執行時可能會出現什麼問題？如何解決？
A3：

=== 你的修改（如果有的話） ===
如果你覺得 AI 的輸出有問題或不夠好，寫出你修改了什麼、為什麼修改：
（沒有修改則填「AI 產出無需修改」）

=== 心得 ===
Q：使用 AI 輔助撰寫 Dockerfile 和自己從頭寫相比，有什麼優缺點？
   什麼情況下 AI 特別有幫助？什麼情況下需要特別小心驗證？
A：
```

---

## 繳交 Checklist

- [ ] `week14/q1_images.txt`：Docker 映像檔操作（pull / images / rmi）+ 觀念題
- [ ] `week14/q2_containers.txt`：Docker 容器操作（run / exec / logs / stop / rm）+ 觀念題
- [ ] `week14/app.py`：Flask 船舶 API 程式碼
- [ ] `week14/requirements.txt`：套件清單
- [ ] `week14/Dockerfile`：自行撰寫的 Dockerfile
- [ ] `week14/q3_dockerfile.txt`：Build 過程、API 測試結果、觀念題
- [ ] `week14/q4_ai_dockerfile.txt`：AI 輔助 Dockerfile + 逐行解釋 + 驗證分析
- [ ] 已 push 到 Fork（確認 PR 中可看到本週 commit）

---

## 常見問題

**Q：`docker: command not found`？**
Docker Desktop 沒啟動。Windows 上找到 Docker Desktop 圖示並開啟，等待底部出現「Engine running」。AWS EC2 上執行 `sudo systemctl start docker`，若出現權限問題加上 `sudo`。

**Q：`docker build` 出現 `permission denied` 或 `Cannot connect to the Docker daemon`？**
AWS EC2 上可能需要 `sudo docker build ...`，或將你的帳號加入 docker 群組：
```bash
sudo usermod -aG docker $USER
newgrp docker
```

**Q：`curl http://localhost:8080/` 沒有回應？**
1. 確認容器有在跑：`docker ps`
2. 確認埠號對應正確：PORTS 欄位應顯示 `0.0.0.0:8080->5000/tcp`
3. 查看 log 找錯誤：`docker logs ship-api`

**Q：`docker build` 出現 `No such file or directory: requirements.txt`？**
你不在 Dockerfile 所在的目錄。確認你的終端機在 `week14/` 目錄下再執行 build，或者把 `requirements.txt` 和 `Dockerfile` 放在同一個目錄。

**Q：Flask 啟動後出現 `Address already in use`？**
5000 埠被另一個服務佔用。先停止其他容器：`docker ps` 找到佔用的容器，`docker stop <name>`，或改用別的主機埠：`-p 8090:5000`。

**Q：q4 的 AI Dockerfile 看不懂某一行？**
可以再問 AI：「Dockerfile 中的 `RUN mkdir -p /app/data /app/output` 這行有什麼作用？在我的應用場景中是否必要？」AI 能解釋每一行，但你要確保自己真的理解後才使用。

---

## 與期末專題的連結

本週學的 Dockerfile 技能，直接用於期末專題的 Docker 部署。**期末專題評分 Docker 部署佔 8%**（教師評分 40% 中的項目之一）。

期末專題 Dockerfile 需求：
- 容器可以正常 build（`docker build` 不報錯）
- 容器可以正常執行（`docker run` 後服務正常回應）
- Dockerfile 結構合理，有善用 build cache
- `requirements.txt` 完整，列出所有使用到的套件

---

## 🚀 進階挑戰（選做）

> 覺得本週內容太簡單？試試這題，不計分但歡迎挑戰。

**將期末專題的資料分析程式 Docker 化**

1. 在你的期末專題 Repo 中建立 `Dockerfile` 和 `requirements.txt`
2. 確保 `docker build` 成功，`docker run` 後程式正常執行
3. 在專題 Repo 的 `README.md` 中加入 Docker 使用說明：
   - 如何 build 映像檔
   - 如何執行容器
   - 如何存取服務（埠號）
4. 把你的映像檔推到 Docker Hub：
   ```bash
   docker login
   docker tag ship-api:v1 你的DockerHub帳號/ship-api:v1
   docker push 你的DockerHub帳號/ship-api:v1
   ```

完成後在 PR 說明中附上你的 Docker Hub 連結。
