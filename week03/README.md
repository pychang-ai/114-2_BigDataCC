# 第 3 週作業：首次登入 Linux 環境與虛擬化觀念

## 作業資訊

| 項目 | 說明 |
|------|------|
| 對應教科書 | 1-1 認識程式開發的虛擬化技術、1-2 Linux 與 Windows 作業系統、3-1 Linux 常用命令 |
| 繳交方式 | 在 Fork 的 week03/ 資料夾中建立三個檔案，push 到 Fork |
| 繳交期限 | 下週上課前 |
| PR 標題 | 學號_姓名（僅首次繳交時建立，之後 push 自動更新） |

---

## 繳交步驟

1. Fork 老師的課程 Repo（如已 Fork 可跳過）：`https://github.com/pychang-ai/114-2_BigDataCC`
2. Clone 你的 Fork 到本機：
   ```bash
   git clone https://github.com/你的帳號/114-2_BigDataCC.git
   cd 114-2_BigDataCC
   ```
3. 建立作業資料夾：
   ```bash
   mkdir week03
   ```
4. 在 week03/ 中建立三個作答檔案（見下方題目）
5. Push 到你的 Fork：
   ```bash
   git add week03/
   git commit -m "完成第3週作業"
   git push origin main
   ```
6. 首次繳交：到 GitHub 網頁發 PR，標題：`學號_姓名`。之後每週 push 即自動更新，不需再發 PR。
   - 進入你的 Fork 頁面
   - 點選 **Contribute** > **Open pull request**
   - PR 標題填入：`學號_姓名`
   - 點選 **Create pull request**

---

## Linux 練習環境連線資訊

請選擇任一台主機連線：

**主機 1：**
```
主機 IP：54.151.244.27
連接埠：2201
帳號：依帳號分配表
密碼：依帳號分配表
連線指令範例：ssh student101@54.151.244.27 -p 2201
```

**主機 2：**
```
主機 IP：54.255.61.68
連接埠：2202
帳號：依帳號分配表
密碼：依帳號分配表
連線指令範例：ssh student201@54.255.61.68 -p 2202
```

---

## 第 1 題：SSH 連線與基本指令

SSH 連線到 Linux 練習環境，依序執行以下 7 個指令，將結果存入 `week03/q1_basic.txt`：

```
whoami
hostname
pwd
uname -a
date
ls /
ls -la ~
```

q1_basic.txt 格式：

```
姓名：（你的姓名）
學號：（你的學號）

=== whoami ===
（貼上執行結果）

=== hostname ===
（貼上執行結果）

=== pwd ===
（貼上執行結果）

=== uname -a ===
（貼上執行結果）

=== date ===
（貼上執行結果）

=== ls / ===
（貼上執行結果）

=== ls -la ~ ===
（貼上執行結果）
```

---

## 第 2 題：檔案操作實作

在 Linux 環境中依序完成以下操作，將過程與結果存入 `week03/q2_fileops.txt`：

1. `mkdir week03test`
2. `cd week03test`
3. 建立三個檔案：hello.txt、learning.txt、vm.txt
4. `ls -l` 確認檔案
5. `cp hello.txt hello_backup.txt`
6. `mv vm.txt virtualization.txt`
7. 最終 `ls -l` 確認結果

q2_fileops.txt 格式：

```
姓名：（你的姓名）
學號：（你的學號）

=== 步驟 1：mkdir week03test ===
（貼上結果，無輸出則寫「無輸出」）

=== 步驟 2：cd week03test ===
（貼上結果）

=== 步驟 3：建立三個檔案 ===
使用的指令：
（寫出你用的指令）

=== 步驟 4：ls -l ===
（貼上結果）

=== 步驟 5：cp hello.txt hello_backup.txt ===
（貼上結果）

=== 步驟 6：mv vm.txt virtualization.txt ===
（貼上結果）

=== 步驟 7：ls -l（最終結果） ===
（貼上結果）

=== 問答 ===
Q：最終目錄中有哪些檔案？和步驟 4 相比，發生了什麼變化？
A：（用自己的話回答）
```

---

## 第 3 題：虛擬化技術比較

用自己的話回答以下問題，存入 `week03/q3_compare.txt`：

```
姓名：（你的姓名）
學號：（你的學號）

Q1：請用一句話說明什麼是「虛擬化」技術。
A1：（你的回答，至少 2 行）

Q2：你今天使用的練習環境涉及哪兩種虛擬化技術？請簡單說明它們各自的角色。
A2：（你的回答，至少 3 行）

Q3：如果改用傳統虛擬機器來提供同樣的練習環境，你覺得會有什麼不同？
A3：（你的回答，至少 2 行）
```

---

## 繳交 Checklist

- [ ] 已 Fork 老師的課程 Repo
- [ ] week03/q1_basic.txt 包含 7 個指令的結果與姓名學號
- [ ] week03/q2_fileops.txt 包含 7 步操作紀錄與問答
- [ ] week03/q3_compare.txt 包含 3 題觀念回答與姓名學號
- [ ] 已 push 到 Fork（確認 PR 中可看到本週 commit）

---

## 常見問題

**Q：SSH 連不上怎麼辦？**
確認帳號、密碼、主機 IP 和 Port 是否正確。首次連線會詢問是否信任主機，輸入 yes。

**Q：怎麼把 Linux 上的結果帶回本機？**
直接用滑鼠選取終端機中的文字，複製後貼到本機的文字編輯器存檔。

**Q：忘記怎麼發 PR？**
進入你的 Fork 頁面，點選 Contribute > Open pull request > Create pull request。

**Q：PR 發錯了可以修改嗎？**
可以，修改檔案後重新 push，PR 會自動更新內容。不需要重新發 PR。

---

## 🚀 進階挑戰（選做）

> 覺得本週內容太簡單？試試這題，不計分但歡迎挑戰。

**用 SSH Key 免密碼登入 WSL，並設定 `~/.ssh/config` 管理多台主機**

1. 在 Windows 產生 SSH Key pair（`ssh-keygen`）
2. 把公鑰加到 WSL 的 `~/.ssh/authorized_keys`
3. 設定 `~/.ssh/config`，讓你可以用 `ssh mylab` 一個指令就連進 WSL
4. 截圖免密碼登入成功的畫面

想想看：如果未來你管理 3 台雲端伺服器，這個設定能省你多少時間？
