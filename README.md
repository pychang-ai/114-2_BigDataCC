# 114-2 巨量資料與雲端運算

## 目錄

- [課程資訊](#課程資訊)
- [課程說明](#課程說明)
- [作業繳交方式](#作業繳交方式)
- [課程進度表](#課程進度表)
- [期末專題](#期末專題)
- [課程工具對應表](#課程工具對應表)
- [評分比例](#評分比例)
- [Git 基本流程](#git-基本流程)
- [Git 基本指令](#git-基本指令)
- [作業資料夾結構](#作業資料夾結構)
- [課程軟體下載](#課程軟體下載)
- [Linux 練習環境連線資訊](#linux-練習環境連線資訊)
- [注意事項](#注意事項)

---

## 課程資訊

| 項目 | 說明 |
|------|------|
| 課程名稱 | 巨量資料與雲端運算 |
| 學期 | 114 學年度第 2 學期 |

| 實作環境 | AWS EC2 + Docker 容器、GitHub、VS Code |

## 課程說明

本課程涵蓋 Linux 作業系統操作、虛擬化技術、Docker 容器、Git 版本控制、雲端部署與 Python 大數據分析應用等主題。透過 AWS 雲端主機提供每位同學獨立的 Linux 練習環境，搭配 GitHub 進行作業繳交與版本管理。

### 課程核心主題

**Linux 與雲端基礎**：學習 Linux 系統操作、Bash Shell 指令、使用者與權限管理，並透過 AWS EC2 雲端主機進行實作，掌握雲端運算的基本架構。

**虛擬化與容器技術**：認識傳統虛擬機器、WSL、Docker 容器三種虛擬化技術的差異與應用場景，學習使用 Dockerfile 建立自訂開發與部署環境。

**版本控制與協作開發**：使用 Git 與 GitHub 進行版本控制，學習 Fork、Pull Request 等團隊協作流程，培養業界標準的開發習慣。

**Python 大數據分析應用**：使用 Python 搭配 Pandas、NumPy 等套件進行資料清洗、轉換與統計分析。透過 Jupyter Notebook 進行互動式資料探索與視覺化，並結合 Matplotlib、Seaborn 等工具將分析結果圖表化呈現。課程後期將導入機器學習基礎概念，使用 Keras 預訓練模型體驗影像辨識與自然語言處理的實際應用，並透過 Gradio 建立 AI 互動介面進行模型部署。

**AI 工具輔助開發**：從第 10 週起導入 AI 工具於資料分析與程式開發流程中。學習 Prompt Engineering 技巧，掌握如何對 ChatGPT、Copilot 等 AI 工具下達有效指令。實作中運用 AI 輔助資料清洗、程式碼產生、視覺化圖表製作與 Dockerfile 撰寫，同時培養驗證 AI 產出正確性的能力。核心原則為「先理解再使用」，確保學生具備獨立判斷與修正 AI 產出的能力。

## 作業繳交方式

本課程採用 **Fork + Pull Request** 流程繳交作業：

1. Fork 本 Repo 到你的 GitHub 帳號
2. 在你的 Fork 中完成每週作業
3. 發 Pull Request 回本 Repo 繳交

每週作業放在對應的資料夾中，例如 `week03/`、`week04/`。

---

## 課程進度表

| 週次 | 主題 | 對應教科書 |
|------|------|-----------|
| 第 1 週 | 課程導論、Git 與 GitHub 基礎、機器學習概述 | 7-4 |
| 第 2 週 | VS Code 與 GitHub 實作強化 | 7-1、7-5 |
| 第 3 週 | 虛擬化技術與 Linux、首次 SSH 連線、Fork/PR 教學、**專題分組與組長建立專題 Repo**、**公布專題題目參考清單** | 1-1、1-2 |
| 第 4 週 | Linux 常用指令與 Bash Shell 基礎、**小考 1**、**每人提出 1-3 個題目構想** | 3-1 |
| 第 5 週 | nano 編輯器與 Shell Script 入門、**組內討論投票決定專題題目、繳交專題提案** | 3-2 |
| 第 6 週 | Linux 使用者、權限與目錄結構、**教師審查專題提案** | 3-3、3-4 |
| 第 7 週 | Linux 套件管理與 Web 伺服器基礎、**確定小組專題題目** | 4-1、5-1 |
| 第 8 週 | MySQL 資料庫基礎 | 5-3、5-4 |
| 第 9 週 | **期中考** | |
| 第 10 週 | Python 開發環境與基礎語法、**AI 工具：Prompt Engineering 入門** | 6-1、6-2 |
| 第 11 週 | Pandas 資料清洗與轉換、**AI 工具：AI 輔助資料清洗** | |
| 第 12 週 | Jupyter Notebook 與資料視覺化、**小考 2+3**、**AI 工具：AI 輔助視覺化** | 6-4 |
| 第 13 週 | 認識 Docker 與安裝設定 | 9-1、9-2、9-5 |
| 第 14 週 | Docker 基本操作與 Dockerfile、**AI 工具：AI 輔助 Docker** | 10-1～10-5、12-1 |
| 第 15 週 | Python 大數據分析綜合實作、**AI 工具：AI 輔助完整分析流程** | |
| 第 16 週 | 機器學習基礎與預訓練模型、**小考 4**、**AI 工具：Prompt Engineering 進階** | 8-3、8-4 |
| 第 17 週 | Gradio AI 互動介面與模型部署、繳交期末報告 | 8-1、8-2 |
| 第 18 週 | **期末專題發表** | |

### 小考說明

| 次數 | 週次 | 範圍 |
|------|------|------|
| 小考 1 | 第 4 週 | Git 操作、虛擬化觀念、SSH 連線、Linux 基本指令 |
| 小考 2 | 第 12 週 | Linux 進階指令、權限管理、Shell Script、Web 伺服器、SQL 語法 |
| 小考 3 | 第 12 週 | Python 基礎、Pandas 資料分析、Jupyter Notebook、資料視覺化 |
| 小考 4 | 第 16 週 | Docker 觀念與操作、Dockerfile、機器學習基礎、預訓練模型 |

---

## 期末專題

### 專題說明

本課程包含分組期末專題，要求使用 Docker 容器部署一個與**海事或海洋**相關的資料分析或 AI 應用。

### 專題時程

| 週次 | 階段 | 說明 |
|------|------|------|
| 第 3 週 | 分組與建立 Repo | 公布分組名單和專題題目參考清單，組長從專題模板建立小組 Repo，邀請組員、老師、助教為 Collaborator |
| 第 4 週 | 個人題目探索 | 每人在自己的 Fork 中建立 `my-topics/` 資料夾，提出 1-3 個題目構想 |
| 第 5 週 | 決定題目與提案 | 各組從所有成員的題目中討論、投票，選出小組題目，組長繳交 proposal/proposal.md |
| 第 6 週 | 提案審查 | 教師審查提案，提供修改建議 |
| 第 7 週 | 確定題目與前期研究 | 確定小組專題題目、資料來源確認、初步資料收集與探索 |
| 第 8 週 | 前期研究 | 資料收集與清理 |
| 第 10-11 週 | 資料分析 | 資料清洗、統計分析、視覺化 |
| 第 12-13 週 | 系統開發 | 應用程式開發、模型訓練 |
| 第 14-15 週 | Docker 部署 | 撰寫 Dockerfile、容器化部署、整合測試 |
| 第 16 週 | 整合測試 | 確保 Docker 部署正常、修正問題 |
| 第 17 週 | 準備發表 | 繳交期末報告和投影片 |
| 第 18 週 | 期末發表 | 口頭報告 + Demo |

### 專題 Repo 建立方式（組長操作）

1. 前往專題模板：`https://github.com/pychang-ai/114-2_BigDataCC-project-template`
2. 點選「**Use this template**」>「**Create a new repository**」
3. Repository name 填入 `114-2_BigDataCC-G01`（替換為組別編號）
4. 設為 **Public**，點選 **Create repository**
5. 進入 Settings > Collaborators > Add people，依序加入：
   - 所有組員（權限：Write）
   - 老師 `pychang-ai`（權限：Write）
   - 助教帳號（權限：Write）
6. 被邀請的人需到 GitHub 通知中點選「**Accept invitation**」才能存取

### 專題評分標準

專題採用四維評分架構，綜合教師、同學與 AI 的多角度評量：

#### 評分維度總覽

| 維度 | 評量對象 | 配分 | 評分方式 |
|------|---------|------|---------|
| 教師評分 | 整組 | 40% | 教師依下方細項給分 |
| 組間互評 | 整組 | 20% | 期末發表時各組互評 |
| 組內互評 | 個人 | 20% | Google 表單匿名評分 |
| AI 評分 | 個人 | 20% | Python 腳本分析 GitHub 數據 |

#### 教師評分細項（40%）

| 項目 | 配分 | 說明 |
|------|------|------|
| 專題提案 | 5% | 題目合理性、可行性、創新性 |
| 資料分析品質 | 10% | 資料清洗完整、分析有洞察、圖表清楚 |
| 程式碼品質 | 8% | 結構清楚、有註解、可讀性高 |
| Docker 部署 | 8% | Dockerfile 正確、容器可正常執行 |
| 口頭報告與 Demo | 5% | 表達清楚、Demo 順暢、回答提問 |
| 文件完整度 | 4% | README、報告、投影片齊全 |

#### 組間互評（20%）

期末發表時，每組對其他所有組進行評分：

| 評分項目 | 說明 |
|---------|------|
| 簡報表達 | 報告邏輯清楚、Demo 順暢 |
| 技術難度 | 使用技術的深度與廣度 |
| 實用價值 | 專題的實際應用性與創意 |
| 整體完成度 | 整體品質與完整性 |

每項 1-5 分，取各組評分的平均值。

#### 組內互評（20%）

每位組員匿名評分其他組員的貢獻度：

| 評分項目 | 說明 |
|---------|------|
| 工作投入 | 是否按時完成分工、主動參與 |
| 技術貢獻 | 程式碼、分析、部署的實際貢獻 |
| 團隊合作 | 溝通協調、配合度 |

每人有 100 分分配給其他組員（不含自己）。例如 5 人組，每人將 100 分分配給其他 4 人，偏離平均值過大的將被標記審查。

#### AI 評分（20%）

透過 Python 腳本自動分析每位組員在 GitHub 上的實際貢獻：

| 檢查項目 | 說明 |
|---------|------|
| Commit 次數 | 每位組員的 commit 數量與頻率 |
| Commit 時間分布 | 是否穩定開發，而非截止前集中趕工 |
| 程式碼貢獻行數 | 每人新增與修改的程式碼量 |
| Commit 訊息品質 | 訊息是否具描述性 |
| 檔案覆蓋範圍 | 是否參與多個模組，而非只改同一個檔案 |
| 專題結構完整度 | proposal、src、docker、docs 各資料夾是否齊全 |
| Docker 部署可行性 | Dockerfile 是否存在且內容合理 |

AI 評分結果將結合組內互評交叉比對，確保評分公平。若 AI 偵測到貢獻度明顯偏低的組員，教師將個別確認後調整該組員的個人分數。

#### AI 評分報告範例

以下為腳本自動產出的分析報告範例：

```
=== 第 1 組 114-2_BigDataCC-G01 ===
專題名稱：高雄港船舶進出資料分析與視覺化

組員貢獻分析：
                          Commits   新增行數   修改檔案範圍         開發期間
  林海翔（A11218001）：   42        1,250     src/ + docker/      穩定，跨 6 週
  陳思涵（A11218002）：   38        980       src/ + notebooks/   穩定，跨 5 週
  王柏宇（A11218003）：   15        320       docs/               僅參與文件
  張雅婷（A11218004）：   8         150       src/                集中在最後 2 天
  黃冠霖（A11218005）：   35        890       data/ + src/        穩定，跨 6 週

Commit 訊息品質：
  V 林海翔：訊息具描述性（例：「新增港口船舶月統計折線圖」）
  V 陳思涵：訊息具描述性（例：「完成缺失值處理與資料型態轉換」）
  X 王柏宇：訊息過於簡略（例：「update」「修改」）
  X 張雅婷：訊息過於簡略（例：「fix」「test」）
  V 黃冠霖：訊息具描述性（例：「清洗 AIS 原始資料並匯出 CSV」）

貢獻度警示：
  ! 王柏宇：commit 數偏低，僅參與文件撰寫，未參與程式開發
  ! 張雅婷：commit 集中在截止前 2 天，疑似趕工，程式碼貢獻量低

專題結構完整度：
  [V] proposal/proposal.md 存在且內容完整
  [V] src/ 有程式碼（12 個 .py 檔案）
  [V] data/ 有資料集（3 個 CSV 檔案）
  [V] notebooks/ 有分析筆記（2 個 .ipynb）
  [V] docker/Dockerfile 存在
  [V] docs/report.md 存在
  [X] requirements.txt 為空，需補上套件清單

AI 評分建議：
  林海翔：A（貢獻突出，穩定開發，涵蓋核心模組與部署）
  陳思涵：A（貢獻良好，穩定開發，負責分析核心）
  王柏宇：C（貢獻偏低，建議教師確認實際參與度）
  張雅婷：C（開發集中於截止前，建議教師確認實際參與度）
  黃冠霖：A（貢獻良好，穩定開發，負責資料處理）
```

此報告將貼到 Claude 進行複審，結合組內互評結果交叉比對後，由教師確認最終個人分數。

---

## 課程工具對應表

| 工具/平台 | 導入週次 | 使用範圍 |
|----------|---------|---------|
| GitHub + Git | 第 1 週 | 全學期作業繳交與版本控制 |
| VS Code | 第 1 週 | 全學期程式開發 IDE |
| Fork + Pull Request | 第 3 週 | 全學期作業繳交方式 |
| AWS EC2 + Docker 容器 | 第 3 週 | Linux 練習環境 |
| Apache + PHP + MySQL | 第 7-8 週 | Web 伺服器與資料庫實作 |
| Python + Miniconda | 第 10 週 | Python 開發與資料分析 |
| ChatGPT / Copilot | 第 10 週 | AI 輔助程式開發與資料分析 |
| Pandas + NumPy | 第 10 週 | 資料清洗、轉換、統計分析 |
| Jupyter Notebook | 第 12 週 | 互動式資料分析與視覺化 |
| Matplotlib + Seaborn | 第 12 週 | 資料視覺化 |
| Docker Desktop + Dockerfile | 第 13 週 | 容器化技術與部署 |
| Keras + KerasNLP | 第 16 週 | 機器學習與預訓練模型 |
| Gradio | 第 17 週 | AI 模型部署互動介面 |

## 評分比例

| 項目 | 比例 |
|------|------|
| 平時作業（每週 Fork + PR） | 20% |
| 小考（4 次） | 20% |
| 期中考 | 20% |
| 期末專題 | 20% |
| 課堂參與 | 20% |

> **作業評分方式**：每週作業採 **通過／不通過（Pass / Fail）** 制。完成所有要求項目即為通過，不另計分數。未繳交或明顯不完整為不通過。

---

## Git 基本流程

### 首次設定（只需做一次）

安裝 Git 後，設定你的姓名和 Email：

```bash
git config --global user.name "你的姓名"
git config --global user.email "你的Email"
```

### Fork + Clone（每學期做一次）

1. 在老師的 Repo 頁面右上角點選 **Fork**，將 Repo 複製到你的帳號下
2. Clone 你的 Fork 到本機：

```bash
git clone https://github.com/你的帳號/114-2_BigDataCC.git
cd 114-2_BigDataCC
```

### 每週作業流程

```
建立作業資料夾 → 編輯檔案 → add → commit → push → 發 PR
```

Step 1：建立當週作業資料夾並完成作業

```bash
mkdir week03
cd week03
# 建立作業檔案，完成作業內容
```

Step 2：將作業加入版本控制並推送

```bash
git add .
git commit -m "完成第3週作業"
git push origin main
```

Step 3：到 GitHub 網頁發 Pull Request

1. 進入你的 Fork 頁面
2. 點選 **Contribute** > **Open pull request**
3. 確認內容後點選 **Create pull request**
4. PR 標題格式：`學號_姓名_week03`

### 同步老師的最新版本

當老師更新了課程 Repo（例如新增每週作業說明），你的 Fork 不會自動更新。請依照以下步驟取得最新版本：

1. 進入你的 Fork 頁面：`https://github.com/你的帳號/114-2_BigDataCC`
2. 頁面上方會出現提示：`This branch is X commits behind pychang-ai:main`
3. 點選「**Sync fork**」按鈕
4. 點選「**Update branch**」
5. 回到本機，執行：
   ```bash
   cd 114-2_BigDataCC
   git pull origin main
   ```

這樣你的 Fork 和本機都會更新到最新版本。你自己建立的作業資料夾不受影響。

---

## Git 基本指令

### 版本控制基礎指令

| 指令 | 功能 | 使用範例 |
|------|------|---------|
| `git clone <url>` | 複製遠端 Repo 到本機 | `git clone https://github.com/user/repo.git` |
| `git status` | 查看目前檔案狀態 | `git status` |
| `git add <file>` | 將檔案加入暫存區 | `git add week03/q1_basic.txt` |
| `git add .` | 將所有變更加入暫存區 | `git add .` |
| `git commit -m "訊息"` | 提交變更並附上說明 | `git commit -m "完成第3週作業"` |
| `git push origin main` | 將本機提交推送到 GitHub | `git push origin main` |
| `git pull origin main` | 從 GitHub 拉取最新版本 | `git pull origin main` |
| `git log` | 查看提交歷史紀錄 | `git log --oneline` |

### Fork 與 Pull Request 指令

| 指令 | 功能 | 使用範例 |
|------|------|---------|
| Fork | 在 GitHub 網頁上操作，複製老師的 Repo 到你的帳號 | 點選 Repo 右上角 Fork 按鈕 |
| Pull Request | 在 GitHub 網頁上操作，將你的作業提交回老師的 Repo | 點選 Contribute > Open pull request |

### 常用輔助指令

| 指令 | 功能 | 使用範例 |
|------|------|---------|
| `git diff` | 查看檔案變更的內容 | `git diff` |
| `git log --oneline` | 用精簡格式查看歷史紀錄 | `git log --oneline -5` |
| `git remote -v` | 查看遠端 Repo 的連結 | `git remote -v` |
| `git branch` | 查看目前所在的分支 | `git branch` |

---

## 作業資料夾結構

```
114-2_BigDataCC/
├── README.md
├── my-topics/             ← 個人題目探索（第 5-6 週）
│   ├── topic1_xxx.md
│   └── topic2_xxx.md
├── week03/
│   ├── q1_basic.txt
│   ├── q2_fileops.txt
│   └── q3_compare.txt
├── week04/
│   └── ...
└── ...
```

## 課程軟體下載

本課程所需軟體已整理於 Dropbox 共用資料夾，請自行下載安裝：

下載連結：[課程軟體 Dropbox](https://www.dropbox.com/scl/fo/u4y9l6q0hyb3pnnd2hykm/AOtzjdBUuiPzwx9q_5ur-i0?rlkey=i7y0hmz2dch4zdf4qoexzgyj4&dl=0)

主要軟體清單：

| 軟體 | 用途 |
|------|------|
| Git | 版本控制 |
| VS Code | 程式開發 IDE |
| MobaXterm | SSH 連線工具（Windows） |
| Python / Miniconda | Python 開發環境 |
| Docker Desktop | 容器化技術 |

---

## Linux 練習環境連線資訊

| 項目 | 主機 1 | 主機 2 |
|------|--------|--------|
| IP | 54.151.244.27 | 54.255.61.68 |
| Port | 2201 | 2202 |
| 帳號 | 依帳號分配表 | 依帳號分配表 |
| 密碼 | 依帳號分配表 | 依帳號分配表 |

連線指令範例：
```bash
ssh student101@54.151.244.27 -p 2201
```

Windows 可使用 MobaXterm、PuTTY 或 PowerShell 連線。

## 注意事項

1. 首次 SSH 連線會詢問是否信任主機，請輸入 `yes`
2. 輸入密碼時畫面不會顯示任何字元，這是正常的
3. 輸入 `exit` 即可離開 Linux 環境
4. 每週作業請在截止日前發 PR 繳交
5. PR 標題請統一格式：`學號_姓名_weekXX`
