
# 第 4 週作業：Linux 常用指令與 Bash Shell 基礎

## 作業資訊

| 項目 | 說明 |
|------|------|
| 對應教科書 | 3-1 Linux 常用命令 |
| 繳交方式 | 在 Fork 的 week04/ 資料夾中建立三個檔案，push 到 Fork |
| 繳交期限 | 下週上課前 |
| PR 標題 | 學號_姓名（僅首次繳交時建立，之後 push 自動更新） |
| 本週另有 | 小考 1、每人提出 1-3 個專題題目構想（放在 my-topics/ 資料夾） |

---

## 繳交步驟

1. 同步老師的最新版本：到你的 Fork 頁面點「**Sync fork**」>「**Update branch**」
2. 本機拉取最新版：`git pull origin main`
3. 建立作業資料夾：`mkdir week04`
4. 完成以下三題，在 week04/ 中建立三個 txt 檔案
5. Push 到你的 Fork：
   ```bash
   git add week04/
   git commit -m "完成第4週作業"
   git push origin main
   ```
6. push 到你的 Fork 即可（W3 已建立的 PR 會自動更新）

---

## 第 1 題：檔案操作與內容檢視

SSH 連線到 AWS Linux 環境，依序完成以下操作，將指令和結果存入 `week04/q1_file_commands.txt`：

```
姓名：
學號：

=== 任務 1：建立目錄結構 ===
請執行以下指令並貼上結果：
mkdir -p ~/week04/dir1/subdir1
mkdir -p ~/week04/dir2
touch ~/week04/dir1/file1.txt
touch ~/week04/dir1/subdir1/file2.txt
touch ~/week04/dir2/file3.txt
tree ~/week04

（貼上 tree 的輸出結果）

=== 任務 2：寫入檔案內容 ===
請執行以下指令：
echo "Hello Linux" > ~/week04/dir1/file1.txt
echo "Bash Shell Practice" > ~/week04/dir1/subdir1/file2.txt
echo "Week 04 Assignment" > ~/week04/dir2/file3.txt

用 cat 查看三個檔案的內容並貼上結果：
（貼上結果）

=== 任務 3：檔案內容檢視指令 ===
請執行以下指令並貼上結果：
cat /etc/passwd | head -5
cat /etc/passwd | tail -3
wc -l /etc/passwd

（貼上結果）
```

---

## 第 2 題：搜尋、過濾與管線操作

完成以下搜尋和管線操作，將結果存入 `week04/q2_grep_pipe.txt`：

```
姓名：
學號：

=== 任務 1：grep 搜尋 ===
在 /etc/passwd 中搜尋你的帳號名稱：
grep 你的帳號 /etc/passwd

（貼上結果）

搜尋所有包含 "bash" 的行：
grep bash /etc/passwd

（貼上結果）

=== 任務 2：管線操作 ===
列出 /etc 目錄下的檔案數量：
ls /etc | wc -l

（貼上結果）

列出 /etc 目錄下的前 10 個檔案名稱（按字母排序）：
ls /etc | sort | head -10

（貼上結果）

=== 任務 3：重導向 ===
將 ls -la ~ 的結果存入檔案：
ls -la ~ > ~/week04/home_list.txt
cat ~/week04/home_list.txt

（貼上 cat 的結果）

將目前日期追加到檔案：
date >> ~/week04/home_list.txt
tail -3 ~/week04/home_list.txt

（貼上 tail 的結果）
```

---

## 第 3 題：管線與重導向觀念題

回答以下問題，存入 `week04/q3_concepts.txt`：

```
姓名：
學號：

Q1：請說明管線符號 | 的功能，並舉一個實際使用的例子。
A1：

Q2：請說明 > 和 >> 的差異，各舉一個使用情境。
A2：

Q3：請寫出一行指令，找出 /etc/passwd 中有多少個使用者的 shell 是 /bin/bash。
    提示：可以結合 grep 和 wc 指令。
A3：
```

---

## 繳交 Checklist

- [ ] week04/q1_file_commands.txt 包含三個任務的完整結果
- [ ] week04/q2_grep_pipe.txt 包含搜尋、管線、重導向的結果
- [ ] week04/q3_concepts.txt 包含三題觀念回答
- [ ] 已 push 到 Fork（確認 PR 中可看到本週 commit）

---

## 專題題目構想（本週另外繳交）

請在你的 Fork 中建立 `my-topics/` 資料夾，提出 1-3 個你有興趣的海事海洋相關題目。每個題目建立一個 markdown 檔案：

```
my-topics/
├── topic1_你的題目名稱.md
├── topic2_你的題目名稱.md
└── topic3_你的題目名稱.md
```

每個檔案需包含：
- 題目名稱
- 為什麼對這個題目有興趣（50 字以上）
- 可能使用的資料來源
- 預計使用的技術

題目構想可以跟 week04 作業一起 push。

---

## 常見問題

**Q：tree 指令找不到？**
先安裝：`sudo apt install -y tree`

**Q：grep 搜尋時沒有結果？**
確認搜尋的關鍵字拼寫正確。grep 區分大小寫，如需忽略大小寫可加 -i 參數：`grep -i keyword file`

**Q：重導向 > 寫入後檔案是空的？**
確認指令語法正確，> 前面要有輸出結果的指令。例如 `ls > file.txt` 而非 `> file.txt ls`

**Q：專題題目構想不知道寫什麼？**
參考課程 Repo README 中的「專題題目參考」清單，從海洋資料分析、海事 AI 應用、海事整合應用三個方向選擇或延伸。

---

## 🚀 進階挑戰（選做）

> 覺得本週內容太簡單？試試這題，不計分但歡迎挑戰。

**寫一個 Bash 腳本：自動掃描資料夾中所有 CSV，統計每個檔案的行數並排序輸出**

1. 建立一個 `scan_csv.sh` 腳本
2. 接受一個參數：目標資料夾路徑
3. 自動找出該資料夾中所有 `.csv` 檔案
4. 用 `wc -l` 統計每個檔案的行數
5. 按行數由多到少排序輸出，格式：`行數 檔案名`
6. 最後一行顯示總行數

提示：會用到 `find`、`wc -l`、`sort -rn`、`awk`
