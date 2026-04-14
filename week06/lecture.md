# 第 6 週教學講義：Linux 使用者、權限與目錄結構

## 本週學習目標

1. 查看自己的身份資訊（使用者、UID、群組）
2. 理解 /etc/passwd 和 /etc/group 的結構
3. 使用 sudo 建立使用者和群組
4. 認識 Linux 目錄結構（FHS）
5. 使用 chown 和 chgrp 管理檔案擁有者

---

## 第一部分：你是誰？查看身份

### 1.1 三個身份查詢指令

SSH 連線到 Linux 環境後，先認識自己的身份：

```bash
# 你是誰？
whoami

# 完整身份資訊（UID、GID、所屬群組）
id

# 你屬於哪些群組？
groups
```

#### 輸出範例

```bash
$ whoami
student101

$ id
uid=1001(student101) gid=1001(student101) groups=1001(student101),27(sudo)

$ groups
student101 sudo
```

#### 三個數字的意義

| 名稱 | 說明 |
|------|------|
| UID（User ID） | 每個使用者的唯一編號。root 是 0，一般使用者從 1000 起算 |
| GID（Group ID） | 使用者主要群組的編號 |
| groups | 使用者所屬的所有群組清單 |

### 1.2 /etc/passwd — 使用者帳號資料庫

Linux 系統中所有使用者的帳號資訊都記錄在 `/etc/passwd` 這個檔案中。

```bash
cat /etc/passwd | grep 你的帳號
```

輸出範例：

```
student101:x:1001:1001:Student 101:/home/student101:/bin/bash
```

這一行用冒號 `:` 分成 **7 個欄位**：

| 欄位 | 範例值 | 說明 |
|------|--------|------|
| 1. 帳號名稱 | student101 | 登入用的使用者名稱 |
| 2. 密碼欄位 | x | 密碼已移到 /etc/shadow，這裡只放 x |
| 3. UID | 1001 | 使用者編號 |
| 4. GID | 1001 | 主要群組編號 |
| 5. 描述 | Student 101 | 使用者的說明文字（可空白） |
| 6. 家目錄 | /home/student101 | 登入後的預設目錄 |
| 7. Shell | /bin/bash | 登入後使用的 Shell 程式 |

#### 課堂練習

```bash
# 查看自己的帳號記錄
cat /etc/passwd | grep $(whoami)

# 看看 root 的記錄
cat /etc/passwd | grep root

# 算一下系統上有多少個使用者
cat /etc/passwd | wc -l
```

### 1.3 /etc/group — 群組資料庫

群組資訊記錄在 `/etc/group` 檔案中。

```bash
cat /etc/group | grep 你的帳號
```

輸出範例：

```
student101:x:1001:
sudo:x:27:student101
```

用冒號 `:` 分成 **4 個欄位**：

| 欄位 | 範例值 | 說明 |
|------|--------|------|
| 1. 群組名稱 | sudo | 群組的名稱 |
| 2. 密碼欄位 | x | 群組密碼（幾乎不使用） |
| 3. GID | 27 | 群組編號 |
| 4. 成員清單 | student101 | 屬於此群組的使用者（逗號分隔） |

---

## 第二部分：使用者與群組管理

### 2.1 為什麼需要多個使用者？

在真實的伺服器環境中，不同的人需要不同的帳號和權限：
- 系統管理員（root）：擁有最高權限
- 一般使用者：只能操作自己家目錄的檔案
- 服務帳號（如 www-data）：專門給特定程式使用

### 2.2 建立新使用者

```bash
# 建立使用者（-m 表示同時建立家目錄）
sudo useradd -m testuser

# 設定密碼
sudo passwd testuser
```

#### 指令說明

| 指令 | 功能 |
|------|------|
| `sudo useradd -m 帳號` | 建立新使用者並建立家目錄 |
| `sudo passwd 帳號` | 設定或修改密碼 |
| `-m` 參數 | 自動在 /home/ 下建立家目錄 |

建立後驗證：

```bash
# 確認使用者已建立
id testuser

# 在 /etc/passwd 中查看
cat /etc/passwd | grep testuser

# 確認家目錄已建立
ls -la /home/testuser
```

### 2.3 建立群組與加入成員

```bash
# 建立新群組
sudo groupadd testgroup

# 將使用者加入群組（-aG = append to Group）
sudo usermod -aG testgroup testuser
```

#### 指令說明

| 指令 | 功能 |
|------|------|
| `sudo groupadd 群組名` | 建立新群組 |
| `sudo usermod -aG 群組 帳號` | 將帳號加入指定群組 |
| `-a` 參數 | 追加模式，保留原有群組（不加 -a 會覆蓋） |
| `-G` 參數 | 指定附加群組 |

驗證：

```bash
# 確認群組已建立
cat /etc/group | grep testgroup

# 確認使用者已加入群組
id testuser
groups testuser
```

### 2.4 刪除使用者與群組

```bash
# 刪除使用者（-r 表示同時刪除家目錄）
sudo userdel -r testuser

# 刪除群組
sudo groupdel testgroup
```

### 2.5 課堂練習：建立使用者並驗證

```bash
# 1. 建立使用者 alice，設定密碼 abc123
sudo useradd -m alice
sudo passwd alice

# 2. 建立群組 project
sudo groupadd project

# 3. 將 alice 加入 project 群組
sudo usermod -aG project alice

# 4. 驗證
id alice
cat /etc/passwd | grep alice
cat /etc/group | grep project
```

---

## 第三部分：Linux 目錄結構（FHS）

### 3.1 什麼是 FHS？

FHS（Filesystem Hierarchy Standard，檔案系統階層標準）定義了 Linux 系統中各個目錄的用途。就像一棟大樓每層樓有不同的功能，Linux 的每個目錄也有固定的職責。

```bash
ls /
```

### 3.2 重要目錄說明

| 目錄 | 用途 | 類比 |
|------|------|------|
| `/` | 根目錄，所有目錄的起點 | 大樓的地基 |
| `/home` | 使用者的家目錄（每人一個資料夾） | 每個人的房間 |
| `/etc` | 系統設定檔（passwd、group、網路設定等） | 大樓的管理辦公室 |
| `/var` | 變動資料（log 記錄、郵件、網頁資料） | 大樓的倉庫 |
| `/tmp` | 暫存檔案（重開機後可能被清除） | 大樓的回收區 |
| `/usr` | 系統程式和共用資源（大部分軟體裝在這） | 大樓的公共設施 |
| `/bin` | 基本指令（ls、cp、cat 等） | 工具箱（每個人都能用） |
| `/sbin` | 系統管理指令（需要 root 權限） | 管理員的工具箱 |
| `/root` | root 使用者的家目錄 | 大樓管理員的房間 |

### 3.3 查看磁碟與檔案統計

#### du — 查看目錄佔用空間

```bash
# 查看自己家目錄的總大小（-s 摘要，-h 人類可讀）
du -sh ~

# 查看家目錄下各子目錄的大小
du -sh ~/*
```

| 參數 | 說明 |
|------|------|
| `-s` | summary，只顯示總計 |
| `-h` | human-readable，用 K/M/G 顯示 |

#### find — 搜尋檔案

```bash
# 算自己家目錄下有幾個檔案
find ~ -type f | wc -l

# 算自己家目錄下有幾個目錄
find ~ -type d | wc -l
```

| 參數 | 說明 |
|------|------|
| `~` | 搜尋範圍（家目錄） |
| `-type f` | 只找檔案（file） |
| `-type d` | 只找目錄（directory） |
| `\| wc -l` | 搭配管線計算行數 |

### 3.4 課堂練習：探索系統目錄

```bash
# 列出根目錄
ls /

# 看看 /etc 裡有什麼設定檔
ls /etc | head -20

# 看看 /home 裡有哪些使用者
ls /home

# 查看自己佔了多少空間
du -sh ~

# 算自己有幾個檔案
find ~ -type f | wc -l
```

---

## 第四部分：檔案擁有者管理（chown 與 chgrp）

### 4.1 複習：ls -l 看到的擁有者資訊

```bash
ls -l ~/my_script.sh
```

```
-rwxr-xr-x 1 student101 student101 350 Mar 24 10:00 my_script.sh
               ^^^^^^^^^^  ^^^^^^^^^^
               擁有者       所屬群組
```

每個檔案都有兩個身份標記：
- **擁有者（Owner）**：通常是建立檔案的人
- **所屬群組（Group）**：通常是擁有者的主要群組

### 4.2 chown — 更改擁有者

```bash
# 改變檔案的擁有者
sudo chown 新擁有者 檔案名

# 同時改變擁有者和群組
sudo chown 新擁有者:新群組 檔案名
```

#### 實作範例

```bash
# 建立測試檔案
touch ~/test_chown.txt
ls -l ~/test_chown.txt
# 預設擁有者是你自己

# 把擁有者改成 root
sudo chown root ~/test_chown.txt
ls -l ~/test_chown.txt
# 現在擁有者變成 root 了

# 同時改擁有者和群組
sudo chown root:root ~/test_chown.txt
ls -l ~/test_chown.txt
```

### 4.3 chgrp — 更改所屬群組

```bash
# 只改變檔案的所屬群組
sudo chgrp 新群組 檔案名
```

#### 實作範例

```bash
# 接續上面的檔案，把群組改成 sudo
sudo chgrp sudo ~/test_chown.txt
ls -l ~/test_chown.txt

# 改回自己
sudo chown $(whoami):$(whoami) ~/test_chown.txt
ls -l ~/test_chown.txt
```

### 4.4 chown vs chmod — 很容易搞混的兩個指令

| 項目 | chown | chmod |
|------|-------|-------|
| 全名 | **Ch**ange **Own**er | **Ch**ange **Mod**e |
| 功能 | 改變「誰擁有」這個檔案 | 改變「能做什麼」（讀/寫/執行） |
| 改變的是 | 擁有者、所屬群組 | rwx 權限 |
| 需要 sudo | 通常需要 | 擁有者可以自己改 |
| 範例 | `sudo chown alice file.txt` | `chmod 755 file.txt` |
| 類比 | 把鑰匙交給別人 | 換一把不同功能的鎖 |

### 4.5 課堂練習：擁有者管理實作

```bash
# 1. 建立測試檔案和使用者
touch ~/ownership_test.txt
echo "Hello Ownership" > ~/ownership_test.txt
sudo useradd -m demouser

# 2. 查看目前擁有者
ls -l ~/ownership_test.txt

# 3. 改擁有者為 demouser
sudo chown demouser ~/ownership_test.txt
ls -l ~/ownership_test.txt

# 4. 建立群組並改群組
sudo groupadd demogroup
sudo chgrp demogroup ~/ownership_test.txt
ls -l ~/ownership_test.txt

# 5. 一次改回自己
sudo chown $(whoami):$(whoami) ~/ownership_test.txt
ls -l ~/ownership_test.txt

# 6. 清理
sudo userdel -r demouser
sudo groupdel demogroup
```

---

## 第五部分：權限與擁有者的綜合應用

### 5.1 情境：多人協作目錄

假設你和同學要一起做專題，需要一個共用資料夾，大家都能讀寫。

```bash
# 1. 建立共用目錄
sudo mkdir /home/shared_project

# 2. 建立專案群組
sudo groupadd project_team

# 3. 把需要的人加入群組
sudo usermod -aG project_team $(whoami)

# 4. 設定目錄的群組
sudo chgrp project_team /home/shared_project

# 5. 設定權限：擁有者和群組可讀寫執行，其他人不能存取
sudo chmod 770 /home/shared_project

# 6. 驗證
ls -la /home/shared_project
```

#### 為什麼不用 777？

`777` 表示任何人都能讀、寫、執行：
- 不相關的使用者也能修改你的檔案
- 不相關的使用者也能刪除你的檔案
- 完全沒有存取控制，等於沒上鎖

正確做法：用**群組**控制誰能存取，搭配 `770` 或 `775`。

### 5.2 權限判斷流程

當一個使用者想操作一個檔案時，Linux 按以下順序檢查：

```
使用者是檔案的擁有者嗎？
  ├── 是 → 套用「擁有者」的權限（第一組 rwx）
  └── 否 → 使用者屬於檔案的群組嗎？
              ├── 是 → 套用「群組」的權限（第二組 rwx）
              └── 否 → 套用「其他人」的權限（第三組 rwx）
```

---

## 第六部分：WSL 指令練習

### 6.1 什麼是 WSL？

WSL（Windows Subsystem for Linux）讓你在 Windows 上直接跑 Linux，不需要另外開虛擬機或連線到遠端伺服器。你這學期用的 Linux 環境就是 WSL。

```
┌─────────────────────────────────────┐
│           Windows 11                │
│                                     │
│  ┌──────────┐    ┌───────────────┐  │
│  │ 檔案總管  │    │ WSL (Ubuntu)  │  │
│  │ VS Code  │◄──►│ bash 終端機   │  │
│  │ Chrome   │    │ Linux 指令    │  │
│  └──────────┘    └───────────────┘  │
│       ▲                 ▲           │
│       │    檔案互通      │           │
│       └────────────────┘           │
└─────────────────────────────────────┘
```

WSL 的重點：
- Windows 和 Linux **同時運作**在同一台電腦上
- 兩邊的檔案可以**互相存取**
- 從 Windows 可以用 `wsl` 指令操作 Linux
- 從 Linux 可以透過 `/mnt/c/` 存取 Windows 的 C 槽

### 6.2 WSL 管理指令（在 Windows 終端機或 PowerShell 執行）

以下指令在 **Windows 的 PowerShell 或 CMD** 中執行，不是在 WSL 裡面：

```powershell
# 查看已安裝的 Linux 發行版
wsl --list --verbose

# 查看 WSL 版本資訊
wsl --version

# 查看目前 WSL 狀態
wsl --status
```

#### 輸出範例

```
$ wsl --list --verbose
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

| 欄位 | 說明 |
|------|------|
| NAME | 安裝的 Linux 發行版名稱 |
| STATE | 狀態：Running（執行中）或 Stopped（已停止） |
| VERSION | WSL 版本（1 或 2，目前主流是 WSL 2） |
| `*` 星號 | 預設的發行版 |

#### 其他常用管理指令

| 指令 | 功能 | 使用時機 |
|------|------|---------|
| `wsl --shutdown` | 關閉所有 WSL 執行個體 | WSL 卡住或想釋放記憶體時 |
| `wsl -d Ubuntu` | 啟動指定的發行版 | 有多個發行版時選擇啟動哪一個 |
| `wsl --update` | 更新 WSL 核心 | 系統提示需要更新時 |

### 6.3 檔案系統互通

WSL 最實用的功能之一是 Windows 和 Linux 之間可以互相存取檔案。

#### 方向 1：從 Linux 存取 Windows 檔案

Windows 的 C 槽掛載在 WSL 的 `/mnt/c/`：

```bash
# 在 WSL 中查看 Windows 桌面的檔案
ls /mnt/c/Users/你的Windows帳號/Desktop/

# 在 WSL 中讀取 Windows 的文字檔
cat /mnt/c/Users/你的Windows帳號/Documents/notes.txt

# 路徑對照
# Windows: C:\Users\小明\Desktop\report.txt
# WSL:     /mnt/c/Users/小明/Desktop/report.txt
```

**路徑轉換規則**：

| Windows 路徑 | WSL 路徑 |
|---|---|
| `C:\` | `/mnt/c/` |
| `D:\` | `/mnt/d/` |
| `C:\Users\小明\Desktop` | `/mnt/c/Users/小明/Desktop` |

注意：反斜線 `\` 變成正斜線 `/`，磁碟機代號變成 `/mnt/` 下的小寫字母。

#### 方向 2：從 Windows 存取 WSL 檔案

在 Windows 的檔案總管網址列輸入：

```
\\wsl$\Ubuntu\home\你的Linux帳號
```

或者在 WSL 中用指令打開檔案總管：

```bash
# 用 Windows 檔案總管打開目前目錄
explorer.exe .

# 用 Windows 檔案總管打開家目錄
explorer.exe ~
```

### 6.4 在 WSL 中執行 Windows 程式

WSL 可以直接呼叫 Windows 的程式（.exe）：

```bash
# 在 WSL 中打開 Windows 記事本
notepad.exe

# 用記事本打開 Linux 中的檔案
notepad.exe ~/hello.txt

# 用 VS Code 打開目前目錄
code .

# 查看 Windows 的 IP 設定
ipconfig.exe
```

### 6.5 實用小技巧

#### 快速進入 WSL

在 Windows 的任何資料夾中，按住 Shift 點右鍵，選擇「在此處開啟 Linux shell」。

或者在檔案總管的網址列輸入 `wsl`，直接在該目錄開啟 WSL。

#### Windows Terminal 分頁切換

Windows Terminal 可以同時開多個分頁：
- 一個分頁跑 PowerShell（Windows）
- 另一個分頁跑 Ubuntu（WSL）
- 用 `Ctrl+Shift+1/2/3` 快速開新分頁

### 6.6 課堂練習：WSL 檔案互通

```bash
# 練習 1：在 WSL 中查看 Windows 桌面有什麼檔案
ls /mnt/c/Users/$(cmd.exe /c "echo %USERNAME%" 2>/dev/null | tr -d '\r')/Desktop/

# 練習 2：在 WSL 建立檔案，從 Windows 打開
echo "Hello from WSL!" > ~/wsl_test.txt
notepad.exe ~/wsl_test.txt

# 練習 3：在 WSL 中建立檔案到 Windows 桌面
echo "This file was created from WSL" > /mnt/c/Users/$(cmd.exe /c "echo %USERNAME%" 2>/dev/null | tr -d '\r')/Desktop/from_wsl.txt
# 回到 Windows 桌面看看有沒有出現 from_wsl.txt

# 練習 4：用 explorer.exe 打開 WSL 的家目錄
explorer.exe ~
```

---

## 本週重點回顧

1. `whoami` 查看帳號名、`id` 查看 UID/GID/群組、`groups` 查看所屬群組
2. `/etc/passwd` 記錄使用者帳號，7 個欄位用 `:` 分隔
3. `/etc/group` 記錄群組資訊，4 個欄位用 `:` 分隔
4. `sudo useradd -m` 建使用者、`sudo groupadd` 建群組、`sudo usermod -aG` 加入群組
5. Linux 目錄結構（FHS）：`/home` 使用者家目錄、`/etc` 設定檔、`/var` 變動資料、`/tmp` 暫存、`/usr` 程式
6. `du -sh` 查看空間使用、`find ~ -type f | wc -l` 計算檔案數量
7. `chown` 改擁有者、`chgrp` 改群組，兩者都需要 sudo
8. `chown` 改的是「誰擁有」，`chmod` 改的是「能做什麼」
9. 多人協作用群組管理存取權限，不要用 777
10. WSL 讓 Windows 和 Linux 共存，`/mnt/c/` 存取 Windows 檔案，`\\wsl$\` 存取 WSL 檔案
11. WSL 中可以執行 Windows 程式（`notepad.exe`、`explorer.exe`、`code`）
