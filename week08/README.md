# 第 8 週作業：MySQL 資料庫基礎

## 作業資訊

| 項目 | 說明 |
|------|------|
| 對應教科書 | 5-3 MySQL 資料庫、5-4 SQL 語法 |
| 繳交方式 | 在 Fork 的 week08/ 資料夾中建立四個檔案，push 到 Fork |
| 繳交期限 | 下週上課前 |
| PR 標題 | 學號_姓名（僅首次繳交時建立，之後 push 自動更新） |

---

## 繳交步驟

1. 同步老師的最新版本：到你的 Fork 頁面點「**Sync fork**」>「**Update branch**」
2. 本機拉取最新版：`git pull origin main`
3. 建立作業資料夾：`mkdir week08`
4. 完成以下四題，在 week08/ 中建立四個 txt 檔案
5. Push 到你的 Fork：
   ```bash
   git add week08/
   git commit -m "完成第8週作業"
   git push origin main
   ```
6. push 到你的 Fork 即可（W3 已建立的 PR 會自動更新）

---

## 第 1 題：WSL 安裝 MySQL 環境

在 WSL 中完成 MySQL 安裝與設定，將過程存入 `week08/q1_install.txt`：

```
姓名：
學號：

=== 任務 1：確認 WSL 環境 ===
在 Windows PowerShell 中執行：
wsl --list --verbose
（貼上結果）

=== 任務 2：安裝 MySQL ===
進入 WSL 後依序執行，貼上每步結果：

步驟 1：更新套件庫
sudo apt update && sudo apt upgrade -y
（貼上最後幾行結果即可）

步驟 2：安裝 MySQL Server
sudo apt install -y mysql-server
（貼上最後幾行結果即可）

步驟 3：啟動 MySQL 服務
sudo service mysql start
（貼上結果）

步驟 4：確認 MySQL 正在運行
sudo service mysql status
（貼上結果，應顯示 running）

=== 任務 3：登入 MySQL ===

步驟 1：用 sudo 登入 MySQL（WSL 預設不需要密碼）
sudo mysql
（貼上登入成功畫面，應顯示 Welcome to the MySQL monitor）

步驟 2：確認版本
SELECT VERSION();
（貼上結果）

步驟 3：查看預設資料庫
SHOW DATABASES;
（貼上結果）
```

---

## 第 2 題：建立資料庫與資料表

延續第 1 題的 MySQL 環境，建立港口資料庫，將過程存入 `week08/q2_create.txt`：

```
姓名：
學號：

=== 任務 1：建立資料庫 ===
CREATE DATABASE port_db;
SHOW DATABASES;
USE port_db;
（貼上每步結果）

=== 任務 2：建立 ships 資料表 ===
CREATE TABLE ships (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ship_name VARCHAR(100) NOT NULL,
    ship_type VARCHAR(50),
    tonnage INT,
    arrival_date DATE
);
（貼上結果）

查看表結構：
SHOW TABLES;
DESCRIBE ships;
（貼上結果）

=== 任務 3：自己建立第二張表 crew ===
請自行寫出 CREATE TABLE 語句，建立 crew 表，需包含以下欄位：
- id：整數，自動遞增，主鍵
- name：字串，最多 50 字元，不允許空值
- rank：字串，最多 30 字元（職位：Captain / Officer / Engineer / Crew）
- ship_id：整數（對應 ships 表的 id）
- salary：小數（DECIMAL(10,2)）

（貼上你寫的 CREATE TABLE 語句）
（貼上 DESCRIBE crew; 的結果）

請回答：
Q：為什麼 crew 表的 ship_id 要對應 ships 表的 id？這樣設計有什麼好處？
A：
```

---

## 第 3 題：新增與查詢資料

延續第 2 題建立好的表，完成資料操作，將過程存入 `week08/q3_query.txt`：

```
姓名：
學號：

=== 任務 1：新增船舶資料 ===
執行以下指令新增 5 筆船舶資料：

INSERT INTO ships (ship_name, ship_type, tonnage, arrival_date) VALUES
('Ever Given', 'Container', 220940, '2026-04-10'),
('Yang Ming Wish', 'Container', 150000, '2026-04-11'),
('Formosa 1', 'Bulk', 85000, '2026-04-12'),
('Ocean Star', 'Tanker', 95000, '2026-04-13'),
('Kaohsiung Express', 'Container', 180000, '2026-04-14');

SELECT * FROM ships;
（貼上結果）

=== 任務 2：新增船員資料 ===
在 crew 表中插入至少 8 筆船員資料，要求：
- 至少包含 3 種不同的 rank（例如 Captain, Officer, Engineer, Crew）
- ship_id 要對應到 ships 表中存在的船

（貼上你寫的 INSERT INTO 語句）

SELECT * FROM crew;
（貼上結果）

=== 任務 3：條件查詢 ===
請寫出 SQL 並貼上結果：

Q1：查詢噸位大於 100000 的船舶，按噸位由大到小排序
（貼上 SQL 語句）
（貼上結果）

Q2：查詢薪水大於 50000 的船員，按薪水由高到低排序
（貼上 SQL 語句）
（貼上結果）

Q3：查詢所有貨櫃船（ship_type = 'Container'）的船名和噸位
（貼上 SQL 語句）
（貼上結果）

=== 任務 4：修改與刪除 ===

步驟 1：將 Ever Given 的噸位改為 221000
（貼上 UPDATE 語句）
（貼上修改後的查詢結果）

步驟 2：刪除 crew 表中薪水最低的那筆資料
（貼上 DELETE 語句）
（貼上刪除後 SELECT * FROM crew; 的結果）

請回答：
Q：為什麼 UPDATE 和 DELETE 一定要加 WHERE 條件？不加會怎樣？
A：
```

---

## 第 4 題：統計與多表查詢

延續前面的資料，完成統計查詢，將過程存入 `week08/q4_stats.txt`：

```
姓名：
學號：

=== 任務 1：統計函數 ===
請寫出 SQL 並貼上結果：

Q1：查詢船舶總數、平均噸位、最大噸位、最小噸位
（貼上 SQL 語句）
（貼上結果）

Q2：查詢噸位最大的前 3 艘船（使用 ORDER BY + LIMIT）
（貼上 SQL 語句）
（貼上結果）

=== 任務 2：GROUP BY 分組統計 ===

Q3：統計每種船型（ship_type）的船舶數量和平均噸位
（貼上 SQL 語句）
（貼上結果）

Q4：統計每種職位（rank）的船員人數和平均薪水
（貼上 SQL 語句）
（貼上結果）

=== 任務 3：LEFT JOIN 多表查詢 ===

Q5：查詢每位船員的姓名、職位、薪水，以及他所屬的船名
提示：用 LEFT JOIN 把 crew 和 ships 接起來
（貼上 SQL 語句）
（貼上結果）

Q6：找出沒有任何船員的船舶
提示：LEFT JOIN + WHERE ... IS NULL
（貼上 SQL 語句）
（貼上結果）

請回答：
Q：LEFT JOIN 和直接查兩張表（SELECT * FROM crew, ships WHERE ...）有什麼不同？
   提示：想想「沒有船員的船」在兩種寫法下會不會出現。
A：
```

---

## 繳交 Checklist

- [ ] week08/q1_install.txt 包含 WSL 確認、MySQL 安裝啟動、密碼設定、版本確認
- [ ] week08/q2_create.txt 包含建立 port_db、ships 表、自行設計 crew 表、觀念回答
- [ ] week08/q3_query.txt 包含新增資料、3 題條件查詢、修改刪除、觀念回答
- [ ] week08/q4_stats.txt 包含統計函數、GROUP BY、LEFT JOIN、觀念回答
- [ ] 已 push 到 Fork（確認 PR 中可看到本週 commit）

---

## 常見問題

**Q：安裝 MySQL 時出現 `unmet dependencies` 或 `held broken packages`？**
這是 WSL 套件庫版本衝突，常見於長時間沒更新的環境。依序嘗試：
```bash
# 步驟 1：完整更新套件庫
sudo apt update && sudo apt upgrade -y

# 步驟 2：修復相依性
sudo apt --fix-broken install

# 步驟 3：重新安裝
sudo apt install -y mysql-server
```
如果仍然失敗，可能是 Ubuntu 版本太舊。執行 `lsb_release -a` 確認版本，建議使用 Ubuntu 22.04 以上。若版本過舊，在 Windows PowerShell 中重裝 WSL：
```powershell
wsl --install -d Ubuntu-22.04
```

**Q：WSL 中 `sudo service mysql start` 出現錯誤？**
嘗試 `sudo service mysql restart`。如果仍然失敗，執行 `sudo apt install --reinstall mysql-server` 重新安裝。

**Q：`mysql -u root -p` 輸入密碼後顯示 Access denied？**
WSL 上的 MySQL 預設不使用密碼，請用 `sudo mysql` 登入（不需要 `-u root -p`）。執行 .sql 檔案也一樣用 `sudo mysql < week08.sql`。

**Q：每次開 WSL 都要重新啟動 MySQL 嗎？**
是的。WSL 中的服務不會自動啟動，每次開啟 WSL 後要執行 `sudo service mysql start`。

**Q：INSERT 時出現 ERROR 1062 Duplicate entry？**
表示 id 重複了。如果用了 AUTO_INCREMENT，INSERT 時不要手動指定 id 值。如果已經出錯，可以用 `TRUNCATE TABLE ships;` 清空重來（會重設 id 計數器）。

**Q：中文在 MySQL 中顯示亂碼？**
建立資料庫時指定 UTF-8 編碼：
```sql
CREATE DATABASE port_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**Q：不小心 UPDATE 沒加 WHERE，全部資料被改了？**
如果還記得原始值，用 UPDATE 逐筆改回。建議操作前先 `SELECT` 確認要改的資料。

**Q：LEFT JOIN 結果中出現 NULL 是什麼意思？**
表示左邊的表有這筆資料，但右邊的表沒有對應的資料。例如某艘船沒有船員，JOIN 後船員相關欄位就會顯示 NULL。

---

## 🚀 進階挑戰（選做）

> 覺得本週內容太簡單？試試這題，不計分但歡迎挑戰。

**設計一個「高雄港船舶進出管理系統」**

1. 設計至少 3 張關聯表（例如：ships 船舶、berths 泊位、voyages 航次）
2. 每張表至少 5 筆以上的測試資料
3. 建立至少 1 個 VIEW：例如「目前停靠中的船舶清單」
4. 寫至少 1 個子查詢：例如「找出平均停靠時間最長的船型」
5. 畫出你的資料表關聯圖（手繪或用工具都行）

想想看：真實的港口管理系統還需要哪些表？（貨物、船員、領港、拖船...）
