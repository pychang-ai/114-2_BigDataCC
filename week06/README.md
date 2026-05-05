# 第 6 週作業：Linux 使用者、權限與目錄結構

## 作業資訊

| 項目 | 說明 |
|------|------|
| 對應教科書 | 3-3 使用者與群組管理、3-4 目錄結構 |
| 繳交方式 | 在 Fork 的 week06/ 資料夾中建立四個檔案，push 到 Fork |
| 繳交期限 | 下週上課前 |
| PR 標題 | 學號_姓名（僅首次繳交時建立，之後 push 自動更新） |
| 本週另有 | 教師審查專題提案 |

---

## 繳交步驟

1. 同步老師的最新版本：到你的 Fork 頁面點「**Sync fork**」>「**Update branch**」
2. 本機拉取最新版：`git pull origin main`
3. 建立作業資料夾：`mkdir week06`
4. 完成以下三題，在 week06/ 中建立三個 txt 檔案
5. Push 到你的 Fork：
   ```bash
   git add week06/
   git commit -m "完成第6週作業"
   git push origin main
   ```
6. push 到你的 Fork 即可（W3 已建立的 PR 會自動更新）

---

## 第 1 題：使用者與群組管理

SSH 連線到 Linux 環境，依序完成以下操作，將指令和結果存入 `week06/q1_users.txt`：

```
姓名：
學號：

=== 任務 1：查看自己的身份資訊 ===
請依序執行以下三個指令並貼上結果：

whoami
（貼上結果）

id
（貼上結果）

groups
（貼上結果）

請回答：你的 UID 是多少？你屬於哪些群組？

=== 任務 2：解讀 /etc/passwd ===
執行以下指令：
cat /etc/passwd | grep 你的帳號

（貼上結果）

請將這行用 : 拆成 7 個欄位，逐一說明每個欄位的意義：
欄位 1（帳號名稱）：
欄位 2（密碼欄位）：
欄位 3（UID）：
欄位 4（GID）：
欄位 5（描述）：
欄位 6（家目錄）：
欄位 7（Shell）：

=== 任務 3：建立使用者與群組 ===
請依序執行以下指令並貼上每步的結果：

步驟 1：建立使用者 week06user（-m 建立家目錄）
sudo useradd -m week06user
（貼上結果，或說明「無輸出表示成功」）

步驟 2：建立群組 week06group
sudo groupadd week06group
（貼上結果）

步驟 3：將 week06user 加入 week06group
sudo usermod -aG week06group week06user
（貼上結果）

步驟 4：驗證使用者和群組
id week06user
（貼上結果）

cat /etc/group | grep week06group
（貼上結果）

步驟 5：清理（刪除測試用的使用者和群組）
sudo userdel -r week06user
sudo groupdel week06group
（貼上結果）
```

---

## 第 2 題：目錄結構與檔案擁有者

完成以下操作，將結果存入 `week06/q2_ownership.txt`：

```
姓名：
學號：

=== 任務 1：探索 Linux 目錄結構 ===
執行以下指令：
ls /

（貼上結果）

請從上面的結果中，說明以下 5 個目錄各是做什麼的：
/home：
/etc：
/var：
/tmp：
/usr：

=== 任務 2：查看空間與檔案統計 ===
查看自己家目錄佔用多少空間：
du -sh ~

（貼上結果）

計算自己家目錄下有多少個檔案：
find ~ -type f | wc -l

（貼上結果）

計算自己家目錄下有多少個目錄：
find ~ -type d | wc -l

（貼上結果）

=== 任務 3：chown 與 chgrp 實作 ===
請依序執行以下指令並貼上每步的結果：

步驟 1：建立測試檔案並查看預設擁有者
touch ~/week06_test.txt
echo "Ownership Test" > ~/week06_test.txt
ls -l ~/week06_test.txt
（貼上結果，注意看擁有者和群組欄位）

步驟 2：建立測試用的使用者和群組
sudo useradd -m tempuser
sudo groupadd tempgroup
（貼上結果）

步驟 3：用 chown 改變擁有者
sudo chown tempuser ~/week06_test.txt
ls -l ~/week06_test.txt
（貼上結果，觀察擁有者欄位的變化）

步驟 4：用 chgrp 改變群組
sudo chgrp tempgroup ~/week06_test.txt
ls -l ~/week06_test.txt
（貼上結果，觀察群組欄位的變化）

步驟 5：用 chown 一次改回自己
sudo chown $(whoami):$(whoami) ~/week06_test.txt
ls -l ~/week06_test.txt
（貼上結果，確認擁有者和群組都改回來了）

步驟 6：清理
rm ~/week06_test.txt
sudo userdel -r tempuser
sudo groupdel tempgroup
（貼上結果）
```

---

## 第 3 題：權限綜合觀念題

回答以下問題，存入 `week06/q3_concepts.txt`：

```
姓名：
學號：

Q1：chown 和 chmod 有什麼不同？請分別說明它們的功能，並各舉一個使用情境。
A1：

Q2：你和 3 位同學要合作做專題，需要在 Linux 上建立一個共用資料夾，
    讓組員都能讀寫檔案，但其他人不能存取。
    請寫出你會使用的指令（提示：需要建立群組、設定目錄的群組和權限）。
A2：

Q3：Linux 判斷權限時，是按什麼順序檢查的？
    假設一個檔案的權限是 rwxr-x---，擁有者是 alice，群組是 project。
    請回答以下三個人分別能做什麼操作：
    (a) alice（擁有者）能做什麼？
    (b) bob（屬於 project 群組）能做什麼？
    (c) charlie（不屬於 project 群組）能做什麼？
A3：
```

---

## 第 4 題：WSL 操作實作

完成以下 WSL 操作，將結果存入 `week06/q4_wsl.txt`：

```
姓名：
學號：

=== 任務 1：查看 WSL 環境資訊 ===
請在 Windows 的 PowerShell 或 CMD 中執行以下指令，貼上結果：

wsl --list --verbose
（貼上結果）

wsl --version
（貼上結果）

請回答：你的 WSL 版本是多少？安裝的 Linux 發行版叫什麼名稱？

=== 任務 2：檔案互通 — 從 WSL 存取 Windows ===
以下操作在 WSL 終端機中執行：

步驟 1：查看 Windows 桌面的檔案
ls /mnt/c/Users/你的Windows帳號/Desktop/ | head -10
（貼上結果，只需列前 10 個）

步驟 2：查看 Windows 和 WSL 的路徑對應
請將你自己 Windows 桌面的路徑，用兩種格式寫出來：
Windows 路徑：（例如 C:\Users\小明\Desktop）
WSL 路徑：（例如 /mnt/c/Users/小明/Desktop）

=== 任務 3：檔案互通 — 從 WSL 建立檔案到 Windows ===

步驟 1：在 WSL 中建立一個檔案到 Windows 桌面
echo "我的學號是 你的學號，這個檔案從 WSL 建立" > /mnt/c/Users/你的Windows帳號/Desktop/wsl_hello.txt
（貼上指令，若無輸出表示成功）

步驟 2：在 WSL 中確認檔案已建立
cat /mnt/c/Users/你的Windows帳號/Desktop/wsl_hello.txt
（貼上結果）

步驟 3：從 WSL 打開 Windows 檔案總管查看家目錄
explorer.exe ~
（截圖或描述你看到了什麼）

步驟 4：清理 — 刪除桌面上的測試檔案
rm /mnt/c/Users/你的Windows帳號/Desktop/wsl_hello.txt
（貼上指令）
```

---

## 繳交 Checklist

- [ ] week06/q1_users.txt 包含身份查詢、passwd 解讀、建立使用者群組的完整結果
- [ ] week06/q2_ownership.txt 包含目錄結構說明、空間統計、chown/chgrp 操作結果
- [ ] week06/q3_concepts.txt 包含三題觀念回答
- [ ] week06/q4_wsl.txt 包含 WSL 環境資訊和檔案互通操作結果
- [ ] 已 push 到 Fork（確認 PR 中可看到本週 commit）

---

## 常見問題

**Q：useradd 出現 Permission denied？**
指令前面要加 `sudo`：`sudo useradd -m week06user`

**Q：passwd 設定密碼時畫面沒有反應？**
Linux 輸入密碼時不會顯示任何字元（連 * 都沒有），直接輸入完按 Enter 即可。

**Q：groupdel 刪不掉群組？**
如果群組是某個使用者的主要群組，要先刪除使用者（`sudo userdel -r 帳號`），再刪群組。

**Q：chown 出現 Operation not permitted？**
chown 需要 sudo 權限：`sudo chown 新擁有者 檔案名`

**Q：find 指令跑很久沒有結果？**
`find` 會搜尋目錄下的所有檔案，如果目錄很大會比較慢。搭配 `| wc -l` 只會顯示最終數字，請耐心等候。

**Q：任務 3 清理時出錯怎麼辦？**
如果刪除使用者或群組時出錯，可以嘗試：
```bash
# 確認使用者是否存在
id week06user
# 如果存在，強制刪除
sudo userdel -r week06user
# 確認群組是否存在
cat /etc/group | grep week06group
# 如果存在，刪除
sudo groupdel week06group
```

**Q：Q4 不知道自己的 Windows 帳號名稱？**
在 WSL 中執行：`cmd.exe /c "echo %USERNAME%" 2>/dev/null`，顯示的就是你的 Windows 帳號。或者直接在 Windows 的檔案總管網址列看 `C:\Users\` 下你的資料夾名稱。

**Q：`wsl --list --verbose` 沒有輸出？**
確認你是在 Windows 的 PowerShell 或 CMD 執行，不是在 WSL 裡面。WSL 裡面不能執行 `wsl --list`。

**Q：`/mnt/c/` 底下什麼都沒有？**
確認 WSL 已正確掛載 Windows 磁碟。執行 `ls /mnt/` 看看有哪些磁碟。如果沒有 c，嘗試重新啟動 WSL：在 Windows 中執行 `wsl --shutdown`，然後重新開啟。

**Q：`explorer.exe .` 無法開啟？**
確認指令中有加 `.exe`（WSL 中呼叫 Windows 程式必須加副檔名）。如果仍然失敗，可以跳過這步，手動在 Windows 檔案總管輸入 `\\wsl$\Ubuntu\home\你的帳號` 來存取。

---

## 🚀 進階挑戰（選做）

> 覺得本週內容太簡單？試試這題，不計分但歡迎挑戰。

**建立一個多使用者共享環境**

1. 建立 2 個使用者（`dev1`、`dev2`）和 1 個群組（`project`）
2. 建立 `/home/shared/` 共享資料夾
3. 設定權限：只有 `project` 群組的成員能讀寫，其他人完全不能存取
4. 用 `dev1` 建立一個檔案，切換到 `dev2` 確認能讀寫
5. 建立一個不在群組內的 `dev3`，確認無法存取

提示：`chmod 770`、`chgrp`、`setfacl`（進階可用 ACL 做更細緻的控制）
