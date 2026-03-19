# 第 5 週作業：Branch + PR 協作練習與專題提案

## 作業資訊

| 項目 | 說明 |
|------|------|
| 對應教科書 | 3-2 使用 nano 文字編輯器 |
| 繳交方式 | 第 1、2 題：個人 Fork 的 week05/ 發 PR 繳交、第 3 題：在專題 Repo 中用 Branch + PR 完成 |
| 繳交期限 | 下週上課前 |
| PR 標題格式 | 個人作業：學號_姓名_week05、專題 Repo：見第 3 題說明 |

---

## 第 1 題：使用 nano 編輯器建立檔案（40 分）

SSH 連線到 AWS Linux 環境，用 nano 建立檔案，將操作過程和結果存入 `week05/q1_nano.txt`：

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

### 評分標準

| 項目 | 配分 |
|------|------|
| 檔案存在且格式正確 | 5 分 |
| 任務 1 用 nano 建立檔案並顯示內容 | 15 分 |
| 任務 2 成功新增內容 | 10 分 |
| 任務 3 列出至少 4 個快捷鍵 | 10 分 |

---

## 第 2 題：撰寫 Shell Script（40 分）

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

（貼上你的 Shell Script 完整內容）

=== 任務 2：設定權限並執行 ===
chmod +x ~/my_script.sh
ls -l ~/my_script.sh

（貼上 ls -l 的結果，確認有 x 權限）

=== 任務 3：執行結果 ===
~/my_script.sh

（貼上完整的執行結果）
```

### 評分標準

| 項目 | 配分 |
|------|------|
| 檔案存在且格式正確 | 5 分 |
| 任務 1 Script 內容正確 | 15 分 |
| 任務 2 權限設定正確 | 10 分 |
| 任務 3 執行結果完整 | 10 分 |

---

## 第 3 題：Branch + PR 協作練習（20 分）

本題在你的**專題 Repo**（114-2_BigDataCC-G01 等）中完成，不是個人 Fork。這是一個小組協作練習，同時完成專題提案的討論。

### 練習目標

學習業界標準的 Git 協作流程：每人從 main 建立自己的 Branch，完成工作後發 PR 回 main，由組長 Review 後 Merge。

### 操作步驟

#### 每位組員都要做：

**步驟 1：Clone 專題 Repo**

```bash
git clone https://github.com/組長帳號/114-2_BigDataCC-G01.git
cd 114-2_BigDataCC-G01
```

**步驟 2：建立自己的 Branch**

Branch 命名規則：`topic/學號`

```bash
git checkout -b topic/C112181101
```

**步驟 3：建立你的題目構想檔案**

在 `my-topics/` 資料夾中建立你的題目構想：

```bash
mkdir -p my-topics
```

用 nano 或 VS Code 建立 `my-topics/C112181101_陳璽安.md`（替換為你的學號和姓名），內容如下：

```
# 題目構想

## 題目名稱

（填入你想到的題目名稱）

## 為什麼對這個題目有興趣？

（50 字以上，說明你的動機）

## 可能使用的資料來源

| 資料名稱 | 來源網址 | 資料格式 |
|---------|---------|---------|
| | | |

## 預計使用的技術

- [ ] Python + Pandas 資料分析
- [ ] Matplotlib / Seaborn 視覺化
- [ ] Jupyter Notebook
- [ ] Keras 預訓練模型
- [ ] Gradio 互動介面
- [ ] MySQL 資料庫
- [ ] Docker 容器部署
- [ ] 其他：__________

## 預期成果

（簡述做出來會是什麼樣子，30 字以上）
```

**步驟 4：Commit 並 Push 你的 Branch**

```bash
git add my-topics/
git commit -m "新增題目構想：你的題目名稱"
git push origin topic/C112181101
```

**步驟 5：到 GitHub 發 Pull Request**

1. 到專題 Repo 頁面，GitHub 會提示你剛 push 了新 Branch
2. 點選「**Compare & pull request**」
3. 確認方向：`main` ← `topic/C112181101`
4. PR 標題：`學號_姓名_題目構想`
5. 在 PR 描述中簡短說明你提出的題目
6. 點選「**Create pull request**」

#### 組長額外要做：

**步驟 6：Review 組員的 PR**

1. 到專題 Repo 的 Pull requests 頁面
2. 點進每位組員的 PR
3. 查看 Files changed，瀏覽組員的題目構想
4. 可以在 PR 中留言討論
5. 確認內容沒問題後，點選「**Merge pull request**」

**步驟 7：組內討論後建立正式提案**

所有組員的題目構想都 Merge 到 main 後：

1. 從 main 建立提案 Branch：
   ```bash
   git checkout main
   git pull origin main
   git checkout -b proposal/final
   ```

2. 編輯 `proposal/proposal.md`，填入討論後決定的專題提案

3. Push 並發 PR：
   ```bash
   git add proposal/
   git commit -m "繳交專題提案"
   git push origin proposal/final
   ```

4. 到 GitHub 發 PR，標題：`第X組_專題提案`
5. 自己 Merge 即可

### 作答內容

請在個人 Fork 的 `week05/q3_branch_pr.txt` 中記錄你的操作過程：

```
姓名：
學號：
組別：第 __ 組
專題 Repo 網址：

=== 步驟 1：你建立的 Branch 名稱 ===
（例如：topic/C112181101）

=== 步驟 2：你建立的題目構想檔案名稱 ===
（例如：my-topics/C112181101_陳璽安.md）

=== 步驟 3：你的 PR 網址 ===
（貼上你在專題 Repo 發的 PR 連結）

=== 步驟 4：PR 是否已被 Merge ===
（是/否）

=== 步驟 5：心得 ===
Branch + PR 的協作流程跟之前直接 push 到 main 有什麼不同？
你覺得這種方式有什麼好處？
（至少寫 3 行）
```

### 評分標準

| 項目 | 配分 |
|------|------|
| 成功建立 Branch 並 Push | 5 分 |
| 題目構想檔案內容完整 | 5 分 |
| 成功發 PR 並附上連結 | 5 分 |
| 心得回答合理 | 5 分 |

---

## 繳交 Checklist

### 個人作業（在個人 Fork 中）
- [ ] week05/q1_nano.txt 包含三個任務的完整結果
- [ ] week05/q2_script.txt 包含 Script 內容、權限設定、執行結果
- [ ] week05/q3_branch_pr.txt 包含 Branch + PR 練習紀錄
- [ ] 已 push 到自己的 Fork
- [ ] 已發 PR，標題：學號_姓名_week05

### 專題 Repo（小組協作）
- [ ] 在專題 Repo 建立了自己的 Branch
- [ ] 建立了題目構想檔案在 my-topics/
- [ ] 在專題 Repo 發了 PR
- [ ] 組長已 Review 並 Merge 所有組員的 PR
- [ ] 組長已繳交正式專題提案 proposal/proposal.md

---

## 常見問題

**Q：git checkout -b 時出現錯誤？**
確認你已經在專題 Repo 的目錄中，且已經 clone 成功。

**Q：push 時被拒絕？**
確認你 push 的是自己的 Branch 名稱，不是 main。例如：`git push origin topic/C112181101`

**Q：PR 方向搞錯了？**
PR 應該是從你的 Branch 合併到 main，確認頁面顯示 `main ← topic/你的學號`。

**Q：組長怎麼 Merge？**
在 PR 頁面最下方，點選「Merge pull request」>「Confirm merge」即可。

**Q：我是組長，要先 Merge 別人的還是先寫提案？**
先 Merge 所有組員的題目構想，看完大家的想法後再討論決定題目，最後建立 proposal Branch 繳交提案。

**Q：Branch + PR 跟之前直接 push 有什麼不同？**
直接 push 是每個人的修改立刻進入 main，可能互相衝突。Branch + PR 讓每個人在自己的分支上工作，完成後由組長檢查再合併，更安全也更有條理。這就是業界軟體開發團隊每天在用的協作方式。
