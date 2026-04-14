# 第 8 週教學講義：MySQL 資料庫基礎

## 本週學習目標

1. 使用 VS Code 連線 WSL 進行開發操作
2. 在 WSL 上安裝並啟動 MySQL
3. 建立資料庫與資料表（CREATE DATABASE / TABLE）
4. 新增、查詢、修改、刪除資料（INSERT / SELECT / UPDATE / DELETE）
5. 使用條件篩選與排序（WHERE / ORDER BY / LIMIT）
6. 使用統計函數與分組（GROUP BY / COUNT / AVG / SUM）
7. 認識多表查詢（LEFT JOIN）

---

## 前置：使用 VS Code 操作 WSL 與 MySQL

> 本週所有操作都在 VS Code 中完成，不需要額外開終端機視窗。

### 為什麼用 VS Code？

| 方式 | 優點 | 缺點 |
|------|------|------|
| Windows CMD / PowerShell | 不用額外安裝 | 無法直接執行 Linux 指令 |
| WSL 終端機 | 原生 Linux 環境 | 獨立視窗，切換不方便 |
| **VS Code + WSL 擴充** | **整合編輯器 + 終端機，一個視窗搞定** | 需安裝擴充套件 |

### Step 1：安裝 WSL 擴充套件

1. 開啟 VS Code
2. 點左側的「擴充功能」圖示（四個方塊的圖示），或按 `Ctrl + Shift + X`
3. 搜尋 **WSL**（發行者：Microsoft）
4. 點「安裝」

### Step 2：從 VS Code 連線到 WSL

**方法 A：從 VS Code 開啟 WSL**
1. 按 `Ctrl + Shift + P` 開啟命令面板
2. 輸入 `WSL: Connect to WSL`
3. VS Code 會重新載入，左下角會顯示 `WSL: Ubuntu`

**方法 B：從 WSL 開啟 VS Code**
1. 開啟 WSL 終端機
2. 進入你想要的目錄，例如 `cd ~`
3. 輸入 `code .`
4. VS Code 會自動開啟並連線到 WSL

### Step 3：在 VS Code 中開啟終端機

1. 連線到 WSL 後，按 `` Ctrl + ` ``（反引號）開啟終端機
2. 終端機會顯示 Linux 的 bash 提示符號（例如 `user@hostname:~$`）
3. 在這裡可以直接執行所有 Linux 指令和 MySQL 指令

```
┌─────────────────────────────────────────────┐
│  VS Code                                     │
│  ┌───────────────────────────────────────┐   │
│  │  編輯區                                │   │
│  │  （可以同時開 .sql 檔案編輯 SQL 語句） │   │
│  │                                       │   │
│  ├───────────────────────────────────────┤   │
│  │  終端機（WSL Ubuntu）                  │   │
│  │  $ sudo service mysql start           │   │
│  │  $ mysql -u root -p                   │   │
│  │  mysql> SELECT * FROM ships;          │   │
│  └───────────────────────────────────────┘   │
│  左下角顯示：WSL: Ubuntu                     │
└─────────────────────────────────────────────┘
```

### Step 4：用 VS Code 編輯 SQL 檔案（進階技巧）

除了在終端機一行行輸入 SQL，你也可以把 SQL 語句寫成檔案：

1. 在 VS Code 建立新檔案 `week08.sql`
2. 寫好 SQL 語句：

```sql
-- week08.sql
CREATE DATABASE IF NOT EXISTS port_db;
USE port_db;

CREATE TABLE ships (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ship_name VARCHAR(100) NOT NULL,
    ship_type VARCHAR(50),
    tonnage INT,
    arrival_date DATE
);

INSERT INTO ships (ship_name, ship_type, tonnage, arrival_date) VALUES
('Ever Given', 'Container', 220940, '2026-04-10'),
('Yang Ming Wish', 'Container', 150000, '2026-04-11');
```

3. 在終端機中執行整個檔案：

```bash
sudo mysql < week08.sql
```

> 好處：SQL 語句可以保存、修改、重複使用，不用每次重新輸入。

### 常見問題

**Q：左下角沒有顯示 WSL: Ubuntu？**
確認已安裝 WSL 擴充套件，並且用 `Ctrl + Shift + P` → `WSL: Connect to WSL` 連線。

**Q：終端機顯示的是 PowerShell 而非 bash？**
點終端機右上角的下拉選單（`+` 旁邊的 `∨`），選擇 `Ubuntu (WSL)` 或 `bash`。

**Q：`code .` 指令在 WSL 中無法使用？**
首次使用時，VS Code 會自動在 WSL 中安裝 VS Code Server。如果失敗，確認你的 VS Code 是最新版本，並且已安裝 WSL 擴充套件。

**Q：連線 WSL 時卡在 `Installing VS Code Server... Downloading: 0%` 很久？**

這是因為 VS Code 需要從微軟雲端（`update.code.visualstudio.com`）下載 Server 到 WSL 裡（約 50-100MB），不是本機複製。只有首次連線或 VS Code 更新版本後才需要下載，之後就不會再跑了。

常見原因與解法：

| 原因 | 解法 |
|------|------|
| WSL 內 DNS 設定異常 | 在 WSL 終端執行：`sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'`，再重新連線 |
| 網路環境不穩定 | 關閉 VS Code，重新開啟後再試一次 |
| 防火牆阻擋 | 確認防火牆允許 VS Code 連外 |

**如果下載一直跑不動，先這樣操作：**

不需要等 VS Code Server 裝好也能做本週練習。直接從 Windows 開始選單搜尋 `Ubuntu`，開啟 WSL 終端機，就可以操作 MySQL。VS Code 連線讓它之後再處理即可。

---

## 第一部分：WSL 環境設定與 MySQL 安裝

### 1.1 確認 WSL 環境

在 Windows 的 PowerShell 中確認 WSL 已安裝：

```powershell
wsl --list --verbose
```

如果沒有安裝，執行以下指令後重新開機：

```powershell
wsl --install -d Ubuntu
```

### 1.2 確認 MySQL 環境

WSL Ubuntu **預設已內建 MySQL（MariaDB）**，不需要另外安裝，也**不需要設定密碼**。

開啟 WSL 終端機（或在 PowerShell 中輸入 `wsl`），啟動服務即可使用：

```bash
# 啟動 MySQL 服務
sudo service mysql start

# 確認 MySQL 正在運行
sudo service mysql status
```

> 每次開啟 WSL 後，MySQL 服務不會自動啟動，記得先執行 `sudo service mysql start`。

#### 如果你的 WSL 沒有 MySQL

部分版本的 WSL Ubuntu 可能未預裝。如果 `sudo service mysql start` 出現找不到服務的錯誤，手動安裝：

```bash
# 更新套件庫
sudo apt update && sudo apt upgrade -y

# 安裝 MySQL Server
sudo apt install -y mysql-server

# 啟動服務
sudo service mysql start
```

#### 常見問題

| 問題 | 解法 |
|------|------|
| `service mysql start` 失敗 | 執行 `sudo service mysql restart` 重試 |
| WSL 沒有 systemctl | WSL 用 `service` 指令取代 `systemctl` |
| 安裝過程卡住 | 按 Enter 或輸入 Y 確認 |
| `unmet dependencies` 或 `held broken packages` | 可能已有 MariaDB 佔用。先跑 `sudo apt update && sudo apt upgrade -y`，再跑 `sudo apt --fix-broken install`。若仍失敗，直接使用已有的 MariaDB 即可，SQL 語法完全相容 |

### 1.3 登入 MySQL

WSL 上的 MySQL **預設不需要密碼**，直接用 `sudo` 登入：

```bash
sudo mysql
```

登入成功會看到：

```
Welcome to the MySQL monitor.  Commands end with ; or \g.
mysql>
```

> 本學期所有 MySQL 操作都用 `sudo mysql` 登入即可，不需要設定密碼。

#### 選做：設定 root 密碼

> 以下為選做內容。如果你想練習用帳號密碼登入（業界常見做法），可以操作這個區塊，否則跳過即可。

```bash
# 用 sudo 進入 MySQL
sudo mysql
```

```sql
-- 設定 root 密碼
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'bigdata2026';
FLUSH PRIVILEGES;
EXIT;
```

```bash
# 設定後就能用密碼登入
mysql -u root -p
# 輸入密碼：bigdata2026
```

> 設定密碼後，`sudo mysql` 和 `mysql -u root -p` 兩種方式都能登入。

### 1.4 MySQL 基本操作

```sql
-- 查看 MySQL 版本
SELECT VERSION();

-- 查看目前有哪些資料庫
SHOW DATABASES;

-- 離開 MySQL
EXIT;
```

---

## 第二部分：建立資料庫與資料表

### 2.1 為什麼需要資料庫？

| 方式 | 優點 | 缺點 |
|------|------|------|
| CSV / Excel | 簡單直覺 | 資料量大時很慢、無法多人同時存取 |
| 資料庫（MySQL） | 查詢快速、支援多人、資料安全 | 需要學 SQL 語法 |

巨量資料的核心：**儲存大量資料，並能快速查詢出需要的部分**。

### 2.2 關聯式資料庫核心概念

| 術語 | 說明 | 類比 |
|------|------|------|
| Database | 資料庫，一個獨立的資料空間 | 一本 Excel 檔案 |
| Table | 資料表，存放同類資料 | Excel 的一個工作表 |
| Row（列） | 一筆資料 | Excel 的一行 |
| Column（欄） | 資料的欄位 | Excel 的一欄 |
| Primary Key | 主鍵，每筆資料的唯一編號 | 學號、身分證字號 |

### 2.3 建立資料庫

```sql
-- 建立名為 port_db 的資料庫
CREATE DATABASE port_db;

-- 查看資料庫是否建立成功
SHOW DATABASES;

-- 切換到 port_db
USE port_db;
```

### 2.4 建立資料表

```sql
CREATE TABLE ships (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ship_name VARCHAR(100) NOT NULL,
    ship_type VARCHAR(50),
    tonnage INT,
    arrival_date DATE
);
```

#### 常用資料型態

| 型態 | 說明 | 範例 |
|------|------|------|
| INT | 整數 | 220940 |
| VARCHAR(N) | 可變長度字串，最多 N 字元 | 'Ever Given' |
| DATE | 日期 | '2026-04-14' |
| DECIMAL(M,D) | 小數，M 位數 D 位小數 | 35.50 |
| TEXT | 長文字 | 備註說明 |

#### 欄位屬性

| 屬性 | 說明 |
|------|------|
| PRIMARY KEY | 主鍵，每筆資料的唯一識別 |
| AUTO_INCREMENT | 自動遞增編號（1, 2, 3...） |
| NOT NULL | 不允許空值，必填欄位 |

### 2.5 查看資料表結構

```sql
-- 查看目前有哪些表
SHOW TABLES;

-- 查看 ships 表的欄位結構
DESCRIBE ships;
```

---

## 第三部分：新增與查詢資料

### 3.1 新增資料（INSERT）

```sql
-- 新增一筆
INSERT INTO ships (ship_name, ship_type, tonnage, arrival_date)
VALUES ('Ever Given', 'Container', 220940, '2026-04-10');

-- 一次新增多筆
INSERT INTO ships (ship_name, ship_type, tonnage, arrival_date) VALUES
('Yang Ming Wish', 'Container', 150000, '2026-04-11'),
('Formosa 1', 'Bulk', 85000, '2026-04-12'),
('Ocean Star', 'Tanker', 95000, '2026-04-13'),
('Kaohsiung Express', 'Container', 180000, '2026-04-14');
```

> 注意：id 欄位不用手動填，AUTO_INCREMENT 會自動產生。

### 3.2 查詢資料（SELECT）

```sql
-- 查詢所有資料
SELECT * FROM ships;

-- 只查詢特定欄位
SELECT ship_name, tonnage FROM ships;
```

### 3.3 條件篩選（WHERE）

```sql
-- 噸位大於 10 萬的船
SELECT * FROM ships WHERE tonnage > 100000;

-- 船型是貨櫃船
SELECT * FROM ships WHERE ship_type = 'Container';

-- 複合條件：貨櫃船且噸位大於 15 萬
SELECT * FROM ships WHERE ship_type = 'Container' AND tonnage > 150000;

-- 4 月 12 日之後到港的船
SELECT * FROM ships WHERE arrival_date > '2026-04-12';
```

### 3.4 排序（ORDER BY）

```sql
-- 按噸位由大到小排序
SELECT * FROM ships ORDER BY tonnage DESC;

-- 按到港日期由早到晚
SELECT * FROM ships ORDER BY arrival_date ASC;

-- 只取前 3 筆
SELECT * FROM ships ORDER BY tonnage DESC LIMIT 3;
```

### 3.5 修改資料（UPDATE）

```sql
-- 修改 Ever Given 的泊位資訊（假設未來加了 berth 欄位）
UPDATE ships SET tonnage = 221000 WHERE ship_name = 'Ever Given';

-- 確認修改結果
SELECT * FROM ships WHERE ship_name = 'Ever Given';
```

> 重要：UPDATE 一定要加 WHERE 條件，否則會改到所有資料！

### 3.6 刪除資料（DELETE）

```sql
-- 刪除特定資料
DELETE FROM ships WHERE id = 5;

-- 確認刪除結果
SELECT * FROM ships;
```

> 重要：DELETE 也一定要加 WHERE，否則會刪掉整張表的資料！

---

## 第四部分：統計與多表查詢

### 4.1 統計函數

| 函數 | 功能 | 範例 |
|------|------|------|
| COUNT(*) | 計算筆數 | 有幾艘船？ |
| SUM(欄位) | 加總 | 總噸位是多少？ |
| AVG(欄位) | 平均 | 平均噸位？ |
| MAX(欄位) | 最大值 | 最大噸位？ |
| MIN(欄位) | 最小值 | 最小噸位？ |

```sql
-- 全部統計
SELECT COUNT(*) AS 船舶數量, AVG(tonnage) AS 平均噸位, MAX(tonnage) AS 最大噸位
FROM ships;
```

### 4.2 分組統計（GROUP BY）

```sql
-- 每種船型有幾艘、平均噸位多少
SELECT ship_type, COUNT(*) AS 數量, AVG(tonnage) AS 平均噸位
FROM ships
GROUP BY ship_type;
```

#### 執行結果範例

```
+-----------+------+----------+
| ship_type | 數量 | 平均噸位 |
+-----------+------+----------+
| Bulk      |    1 | 85000.00 |
| Container |    3 |183646.67 |
| Tanker    |    1 | 95000.00 |
+-----------+------+----------+
```

### 4.3 建立第二張表

```sql
CREATE TABLE crew (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    rank VARCHAR(30),
    ship_id INT,
    salary DECIMAL(10,2)
);

INSERT INTO crew (name, rank, ship_id, salary) VALUES
('Chen Wei', 'Captain', 1, 85000),
('Lin Jia', 'Officer', 1, 55000),
('Wang Ming', 'Captain', 2, 82000),
('Zhang Yu', 'Engineer', 2, 60000),
('Li Hao', 'Officer', 3, 53000),
('Huang Kai', 'Engineer', 3, 58000),
('Wu Cheng', 'Captain', 4, 88000),
('Xu Dong', 'Crew', 1, 35000);
```

### 4.4 多表查詢（LEFT JOIN）

```sql
-- 查詢每位船員和他所屬的船名
SELECT c.name, c.rank, c.salary, s.ship_name
FROM crew c
LEFT JOIN ships s ON c.ship_id = s.id;
```

#### LEFT JOIN 是什麼？

```
crew 表              ships 表
+----+--------+      +----+------------+
| id | ship_id| ---> | id | ship_name  |
+----+--------+      +----+------------+
```

LEFT JOIN 用 `ship_id = id` 把兩張表「接起來」，讓每位船員的資料旁邊顯示對應的船名。

```sql
-- 找出沒有船員的船（LEFT JOIN + IS NULL）
SELECT s.ship_name
FROM ships s
LEFT JOIN crew c ON s.id = c.ship_id
WHERE c.id IS NULL;
```

---

## 重點整理

| SQL 指令 | 功能 | 記憶口訣 |
|----------|------|---------|
| CREATE DATABASE | 建資料庫 | 開新檔案 |
| CREATE TABLE | 建資料表 | 開新工作表 |
| INSERT INTO | 新增資料 | 填入一筆 |
| SELECT ... FROM | 查詢資料 | 讀出來看 |
| WHERE | 條件篩選 | 只要符合的 |
| ORDER BY | 排序 | 排隊站好 |
| GROUP BY | 分組統計 | 分類計算 |
| UPDATE | 修改資料 | 改一下 |
| DELETE | 刪除資料 | 丟掉 |
| LEFT JOIN | 合併兩張表 | 左邊為主接右邊 |

> **UPDATE 和 DELETE 一定要加 WHERE！** 不加 WHERE = 全部修改 / 全部刪除。
