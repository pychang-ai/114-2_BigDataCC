# 第 5 週教學講義：nano 編輯器與 Shell Script 入門

## 本週學習目標

1. 熟練使用 nano 文字編輯器建立和編輯檔案
2. 了解 Shell Script 的用途和基本語法
3. 學會設定檔案權限並執行 Script
4. 理解 chmod 數字權限表示法

---

## 第一部分：nano 文字編輯器

### 1.1 為什麼要學 nano？

在 Linux 伺服器上，很多時候沒有圖形介面可以用，你只能透過終端機（Terminal）操作。nano 是最簡單的終端機文字編輯器，適合初學者快速上手。

其他常見的編輯器還有 vim 和 emacs，但學習門檻較高，我們先從 nano 開始。

### 1.2 開啟 nano

SSH 連線到 AWS Linux 環境後：

```bash
# 建立新檔案
nano myfile.txt

# 開啟已存在的檔案
nano /etc/hostname
```

開啟後你會看到一個全螢幕的編輯畫面，底部有快捷鍵提示。`^` 符號代表 Ctrl 鍵。

### 1.3 nano 基本操作

#### 輸入文字

直接用鍵盤打字即可，跟記事本一樣。用方向鍵移動游標。

#### 儲存檔案

按 `Ctrl+O`，畫面底部會顯示檔名，按 `Enter` 確認儲存。

#### 離開 nano

按 `Ctrl+X`。如果有未儲存的修改，會詢問是否儲存：
- 按 `Y` 儲存後離開
- 按 `N` 不儲存直接離開
- 按 `Ctrl+C` 取消，回到編輯畫面

#### 常用快捷鍵完整表

| 快捷鍵 | 功能 | 說明 |
|--------|------|------|
| Ctrl+O | 儲存 | Write Out，儲存目前的檔案 |
| Ctrl+X | 離開 | Exit，離開 nano |
| Ctrl+K | 剪下整行 | Cut，剪下游標所在的整行 |
| Ctrl+U | 貼上 | Uncut，貼上剛才剪下的內容 |
| Ctrl+W | 搜尋 | Where Is，搜尋文字 |
| Ctrl+C | 顯示游標位置 | 顯示目前在第幾行第幾欄 |
| Ctrl+G | 顯示說明 | Help，顯示完整快捷鍵說明 |
| Ctrl+A | 移到行首 | 游標跳到該行最前面 |
| Ctrl+E | 移到行尾 | 游標跳到該行最後面 |

### 1.4 課堂練習：用 nano 建立自我介紹

```bash
# 建立檔案
nano ~/intro.txt
```

輸入以下內容（替換為你的真實資訊）：

```
姓名：王小明
學號：C112181101
系所：海事資訊科技系
興趣：打籃球、看電影
修這門課的期望：學會 Linux 和 Docker
```

按 `Ctrl+O` 儲存，按 `Enter` 確認，按 `Ctrl+X` 離開。

確認檔案內容：

```bash
cat ~/intro.txt
```

### 1.5 nano 進階操作練習

開啟剛才的檔案，在最後面新增一行：

```bash
nano ~/intro.txt
```

用方向鍵移到最後一行，按 `Enter` 換行，加上：

```
今天日期：2026-03-24
```

你也可以用 `date` 指令查詢今天日期：

```bash
date
```

儲存離開後確認：

```bash
cat ~/intro.txt
```

---

## 第二部分：Shell Script 入門

### 2.1 什麼是 Shell Script？

Shell Script 就是把多個 Linux 指令寫在一個檔案中，讓電腦一次執行完畢。就像是寫一份工作清單，電腦會按照順序一步步完成。

日常應用場景：
- 每天自動備份資料
- 批次建立多個使用者帳號
- 伺服器開機時自動啟動服務
- 定期清理暫存檔案

### 2.2 第一個 Shell Script

用 nano 建立一個 Script：

```bash
nano ~/hello.sh
```

輸入以下內容：

```bash
#!/bin/bash
echo "Hello, World!"
echo "我的第一個 Shell Script"
echo "目前時間是：$(date)"
```

儲存離開。

#### 第一行 `#!/bin/bash` 是什麼？

這一行叫做 shebang，告訴系統要用哪個程式來執行這個 Script。`/bin/bash` 就是 Bash Shell 的路徑。每個 Shell Script 的第一行都要寫這個。

#### `echo` 指令

`echo` 的功能是印出文字到螢幕上：

```bash
echo "Hello"           # 印出 Hello
echo "我的名字是小明"    # 印出中文也可以
echo ""                # 印出空行
```

#### `$(指令)` 語法

`$(指令)` 會先執行括號中的指令，再把結果插入到字串中：

```bash
echo "使用者：$(whoami)"     # 印出目前的使用者名稱
echo "主機名稱：$(hostname)"  # 印出主機名稱
echo "目前目錄：$(pwd)"      # 印出目前所在目錄
echo "今天日期：$(date)"     # 印出目前日期時間
```

### 2.3 執行 Shell Script

#### 方法 1：用 bash 指令執行

```bash
bash ~/hello.sh
```

這種方式不需要設定執行權限，直接就能跑。

#### 方法 2：用 ./ 執行

```bash
./hello.sh
```

如果出現 `Permission denied`，表示檔案沒有執行權限。需要先加上權限：

```bash
chmod +x ~/hello.sh
./hello.sh
```

### 2.4 課堂練習：系統資訊報告 Script

建立一個比較完整的 Script：

```bash
nano ~/my_script.sh
```

輸入以下內容：

```bash
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
```

儲存後設定權限並執行：

```bash
chmod +x ~/my_script.sh
ls -l ~/my_script.sh
./my_script.sh
```

#### 指令說明

| 指令 | 功能 |
|------|------|
| `df -h` | 顯示磁碟使用量，`-h` 表示人類可讀格式 |
| `head -5` | 只顯示前 5 行 |
| `free -h` | 顯示記憶體使用量 |
| `\|` | 管線，把前一個指令的輸出傳給後一個指令 |

### 2.5 Shell Script 中使用變數

```bash
#!/bin/bash

# 定義變數（等號前後不能有空格）
NAME="王小明"
ID="C112181101"
COURSE="巨量資料與雲端運算"

# 使用變數（前面加 $）
echo "姓名：$NAME"
echo "學號：$ID"
echo "課程：$COURSE"

# 把指令結果存入變數
TODAY=$(date +%Y-%m-%d)
echo "今天是：$TODAY"
```

注意事項：
- 定義變數時，等號前後不能有空格。`NAME="小明"` 正確，`NAME = "小明"` 錯誤
- 使用變數時，前面加 `$` 符號
- 建議用大寫命名變數，跟指令區分

---

## 第三部分：檔案權限與 chmod

### 3.1 查看檔案權限

```bash
ls -l ~/my_script.sh
```

輸出範例：

```
-rwxr-xr-x 1 student101 student101 350 Mar 24 10:00 my_script.sh
```

權限欄位 `-rwxr-xr-x` 拆解如下：

```
-    rwx    r-x    r-x
|    |      |      |
|    |      |      └── 其他人（Others）的權限
|    |      └── 群組（Group）的權限
|    └── 擁有者（Owner）的權限
└── 檔案類型（- 一般檔案，d 目錄）
```

### 3.2 三種權限

| 符號 | 權限 | 對檔案的意義 | 對目錄的意義 |
|------|------|------------|------------|
| r | 讀取（Read） | 可以查看檔案內容 | 可以列出目錄內容 |
| w | 寫入（Write） | 可以修改檔案內容 | 可以在目錄中建立或刪除檔案 |
| x | 執行（Execute） | 可以執行檔案 | 可以進入目錄 |
| - | 無權限 | 不可操作 | 不可操作 |

### 3.3 chmod 數字表示法

每種權限對應一個數字：

| 權限 | 數字 |
|------|------|
| r（讀取） | 4 |
| w（寫入） | 2 |
| x（執行） | 1 |
| 無權限 | 0 |

三個數字分別代表：擁有者、群組、其他人。把需要的權限數字加起來。

### 3.4 常見權限組合

| chmod | 權限 | 擁有者 | 群組 | 其他人 | 常用情境 |
|-------|------|--------|------|--------|---------|
| 755 | rwxr-xr-x | 讀寫執行 | 讀和執行 | 讀和執行 | Shell Script、可執行程式 |
| 644 | rw-r--r-- | 讀寫 | 只讀 | 只讀 | 一般文字檔案、設定檔 |
| 700 | rwx------ | 讀寫執行 | 無 | 無 | 私人 Script |
| 600 | rw------- | 讀寫 | 無 | 無 | 密碼檔、私密資料 |
| 777 | rwxrwxrwx | 全部 | 全部 | 全部 | 不建議使用，安全風險高 |

### 3.5 chmod 計算範例

以 755 為例：

```
擁有者：7 = 4(r) + 2(w) + 1(x) = rwx
群  組：5 = 4(r) + 0    + 1(x) = r-x
其他人：5 = 4(r) + 0    + 1(x) = r-x
```

以 644 為例：

```
擁有者：6 = 4(r) + 2(w) + 0    = rw-
群  組：4 = 4(r) + 0    + 0    = r--
其他人：4 = 4(r) + 0    + 0    = r--
```

### 3.6 chmod 實作練習

```bash
# 建立測試檔案
touch ~/test_permission.txt

# 查看預設權限
ls -l ~/test_permission.txt

# 改為 755（加上執行權限）
chmod 755 ~/test_permission.txt
ls -l ~/test_permission.txt

# 改為 644（移除執行權限）
chmod 644 ~/test_permission.txt
ls -l ~/test_permission.txt

# 改為 600（只有自己能讀寫）
chmod 600 ~/test_permission.txt
ls -l ~/test_permission.txt
```

觀察每次 `ls -l` 顯示的權限欄位變化。

### 3.7 為什麼 Script 需要執行權限？

Linux 的安全設計：檔案預設只有讀寫權限，不能直接執行。這是為了防止不小心執行到惡意程式。

你必須明確地用 `chmod +x` 或 `chmod 755` 加上執行權限，Linux 才會允許你用 `./` 來執行它。

如果不想加執行權限，也可以用 `bash script.sh` 的方式執行。這是因為你執行的是 `bash` 程式，而 Script 只是被 `bash` 讀取的文字檔，不需要自己有執行權限。

```bash
# 方式 1：需要執行權限
chmod +x my_script.sh
./my_script.sh

# 方式 2：不需要執行權限
bash my_script.sh
```

---

## 第四部分：綜合練習

### 練習 1：用 nano 建立自我介紹

```bash
nano ~/intro.txt
# 輸入姓名、學號、系所、興趣、期望
# Ctrl+O 儲存 → Ctrl+X 離開
cat ~/intro.txt
```

### 練習 2：撰寫系統資訊 Script

```bash
nano ~/my_script.sh
# 輸入講義中的系統資訊報告內容
# Ctrl+O 儲存 → Ctrl+X 離開
chmod +x ~/my_script.sh
./my_script.sh
```

### 練習 3：觀察權限變化

```bash
touch ~/test.txt
ls -l ~/test.txt        # 看預設權限
chmod 755 ~/test.txt
ls -l ~/test.txt        # 看變化
chmod 644 ~/test.txt
ls -l ~/test.txt        # 看變化
chmod 600 ~/test.txt
ls -l ~/test.txt        # 看變化
```

---

## 本週重點回顧

1. nano 是 Linux 中最簡單的終端機文字編輯器，Ctrl+O 儲存、Ctrl+X 離開
2. Shell Script 把多個指令寫在一個檔案中，讓電腦按順序執行
3. 第一行 `#!/bin/bash` 告訴系統用 Bash 來執行
4. `$(指令)` 可以在字串中插入指令的執行結果
5. chmod 用數字設定權限：r=4、w=2、x=1，三個數字分別代表擁有者、群組、其他人
6. 755 代表「擁有者可讀寫執行，其他人可讀和執行」
7. 644 代表「擁有者可讀寫，其他人只能讀」
8. Script 需要執行權限才能用 `./` 執行，或者用 `bash script.sh` 繞過權限限制
