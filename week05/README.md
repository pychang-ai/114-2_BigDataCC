# 第 5 週作業：nano 編輯器與 Shell Script 入門

## 作業資訊

| 項目 | 說明 |
|------|------|
| 對應教科書 | 3-2 使用 nano 文字編輯器 |
| 繳交方式 | 在 Fork 的 week05/ 資料夾中建立三個檔案，push 到 Fork |
| 繳交期限 | 下週上課前 |
| PR 標題 | 學號_姓名（僅首次繳交時建立，之後 push 自動更新） |
| 本週另有 | 組內討論投票決定專題題目、繳交專題提案 |

---

## 繳交步驟

1. 同步老師的最新版本：到你的 Fork 頁面點「**Sync fork**」>「**Update branch**」
2. 本機拉取最新版：`git pull origin main`
3. 建立作業資料夾：`mkdir week05`
4. 完成以下三題，在 week05/ 中建立三個 txt 檔案
5. Push 到你的 Fork：
   ```bash
   git add week05/
   git commit -m "完成第5週作業"
   git push origin main
   ```
6. push 到你的 Fork 即可（W3 已建立的 PR 會自動更新）

---

## 第 1 題：使用 nano 編輯器建立檔案

用 nano 建立一個自我介紹檔案，將操作過程和結果存入 `week05/q1_nano.txt`：

```
姓名：
學號：

=== 任務 1：用 nano 建立 intro.txt ===
請用 nano 建立 ~/intro.txt，輸入以下內容（替換為你的真實資訊）：
  姓名：XXX
  學號：XXX
  系所：XXX
  興趣：XXX
  修這門課的期望：XXX

儲存後用 cat 顯示內容：
cat ~/intro.txt

（貼上結果）

=== 任務 2：nano 快捷鍵操作 ===
用 nano 開啟 ~/intro.txt，在最後面新增一行：
  今天日期：（用 date 指令查到的日期）

儲存後用 cat 顯示完整內容：
（貼上結果）

=== 任務 3：說明你使用了哪些 nano 快捷鍵 ===
（例如：Ctrl+O 儲存、Ctrl+X 離開，至少列出 4 個）
```

---

## 第 2 題：撰寫 Shell Script

撰寫一個 Shell Script 並執行，將程式碼和結果存入 `week05/q2_script.txt`：

```
姓名：
學號：

=== 任務 1：建立 Shell Script ===
請用 nano 建立 ~/my_script.sh，內容如下：

#!/bin/bash
echo "========================================="
echo "  系統資訊報告"
echo "========================================="
echo "使用者：$(whoami)"
echo "主機名稱：$(hostname)"
echo "目前日期：$(date)"
echo "目前目錄：$(pwd)"
echo "========================================="
echo "磁碟使用量："
df -h | head -5
echo "========================================="
echo "記憶體使用量："
free -h
echo "========================================="

=== 任務 2：設定權限並執行 ===
chmod +x ~/my_script.sh
（貼上 ls -l ~/my_script.sh 的結果，確認有 x 權限）

=== 任務 3：執行結果 ===
./my_script.sh

（貼上完整的執行結果）
```

---

## 第 3 題：chmod 權限觀念題

回答以下問題，存入 `week05/q3_chmod.txt`：

```
姓名：
學號：

Q1：請說明 chmod 755 代表什麼權限，擁有者、群組、其他人各能做什麼？
A1：

Q2：請說明 chmod 644 代表什麼權限，跟 755 的差異是什麼？
A2：

Q3：為什麼 Shell Script 需要加上執行權限（chmod +x）才能用 ./ 執行？
    如果不加執行權限，還有什麼方式可以執行 Script？
A3：
```

---

## 專題提案（本週另外繳交）

各組已在第 4 週提出個人題目構想，本週請完成以下事項：

1. **組內討論**：分享每位組員的 1-3 個題目
2. **投票決定**：選出一個小組題目
3. **繳交提案**：組長在專題 Repo 的 `proposal/proposal.md` 中填寫正式提案

提案需包含：題目名稱、動機、資料來源、預計使用技術、分工規劃。

---

## 繳交 Checklist

- [ ] week05/q1_nano.txt 包含 nano 操作過程和快捷鍵
- [ ] week05/q2_script.txt 包含 Script 程式碼、權限設定、執行結果
- [ ] week05/q3_chmod.txt 包含三題觀念回答
- [ ] 已 push 到 Fork（確認 PR 中可看到本週 commit）
- [ ] 各組已在專題 Repo 繳交 proposal/proposal.md

---

## 常見問題

**Q：nano 存檔後怎麼確認內容？**
用 `cat 檔案名稱` 查看內容。

**Q：Shell Script 執行時出現 Permission denied？**
確認有執行權限：`chmod +x my_script.sh`，再用 `./my_script.sh` 執行。

**Q：free 指令找不到？**
先安裝：`sudo apt install -y procps`

**Q：專題提案不知道怎麼寫？**
參考專題 Repo 中 `proposal/proposal.md` 的模板，依照欄位填寫即可。

---

## 🚀 進階挑戰（選做）

> 覺得本週內容太簡單？試試這題，不計分但歡迎挑戰。

**寫一個 crontab 排程：每天自動備份指定資料夾並壓縮成 .tar.gz**

1. 寫一個 `backup.sh` 腳本，把指定資料夾壓縮成 `backup_YYYY-MM-DD.tar.gz`
2. 用 `date +%Y-%m-%d` 自動產生日期命名
3. 設定 crontab，每天凌晨 2:00 自動執行備份
4. 加入保留最近 7 天備份的清理邏輯（`find ... -mtime +7 -delete`）

提示：`crontab -e` 編輯排程，格式為 `分 時 日 月 週 指令`
