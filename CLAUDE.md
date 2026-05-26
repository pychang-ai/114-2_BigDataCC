# CLAUDE.md

本文件提供給 Claude Code（claude.ai/code）在此 Repo 工作時的操作指引。

## Repo 用途

這是 **114-2 巨量資料與雲端運算** 的教師端課程 Repo。學生 Fork 此 Repo，在 `weekXX/` 資料夾完成每週文字作業後，以 Pull Request 方式繳交。教師執行 `grade_github.py` 自動批改 PR，並可選擇將結果回填為 PR 留言。

## 執行批改腳本

先安裝唯一的相依套件：

```bash
pip install requests
```

批次批改某週所有 open PR（輸出報告 `week04_report.txt` 和成績單 `week04_scores.csv`）：

```bash
python grade_github.py --repo pychang-ai/114-2_BigDataCC --week week04 --token ghp_xxx
```

批改並自動將成績貼到 PR 留言：

```bash
python grade_github.py --repo pychang-ai/114-2_BigDataCC --week week04 --token ghp_xxx --comment
```

批改單一 PR（GitHub Actions 使用的模式）：

```bash
python grade_github.py --repo pychang-ai/114-2_BigDataCC --pr 53 --token ghp_xxx --comment
```

`--token` 也可省略，腳本會自動讀取環境變數 `GITHUB_TOKEN`，在 Actions 中不需額外設定 Secrets。

## `grade_github.py` 架構

**週次判斷**（三層 fallback，由最準到兜底）：
1. PR 變更的檔案路徑 — 比對 `weekXX/` 前綴
2. PR 標題關鍵字 — 正規表示式比對 `week04`、`w04` 等
3. PR 建立日期 — 對照 `SEMESTER_WEEKS` 學期行事曆字典

**評分邏輯** — 每題皆呼叫 `grade_generic()`：
- 檔案存在 +5、填寫姓名學號 +5
- 第 1、2 題：每個填寫的 `=== 區塊 ===` +5（上限 30 分）
- 第 3 題：每個有效的 `AX：` 觀念回答 +3（上限 10 分）
- 三題滿分：40 + 40 + 20 = 100 分

**模糊檔名比對** — `generate_alt_paths()` 自動嘗試學生常見的命名錯誤（缺少 `.txt`、週次前綴用錯、簡化成 `q1.txt` 等）。

**報告尾端** — 產出的 `.txt` 報告最後附有給 Claude 複審的指示，包含：第 3 題觀念回答品質判斷、跨學生抄襲比對。預設工作流程是將整份報告貼入 Claude 進行人工+AI 雙重複審。

## 每週作業結構

每個 `weekXX/` 資料夾包含：
- `README.md` — 作業說明、繳交步驟、Checklist、常見問題
- 作答模板（`q1_*.txt`、`q2_*.txt`、`q3_*.txt`）— 學生在自己的 Fork 中填寫

第 1–8 週涵蓋 Linux、Git、SSH、MySQL（純文字作業）；第 10–18 週轉為 Python、Pandas、Docker、機器學習（部分週次含 `.ipynb` 和 `images/`）。`midterm/` 和 `final/` 目前僅有 `.gitkeep`。

要新增某週的批改支援，在 `grade_github.py` 的 `WEEK_FILES` 字典中新增對應的週次與檔案路徑即可。

## GitHub Actions

`.github/workflows/auto-grade.yml` 在 PR 被開啟或更新（`pull_request_target: opened, synchronize`）時自動觸發，checkout `main`、安裝 `requests`，並以 `--pr` + `--comment` 模式執行腳本。使用內建的 `GITHUB_TOKEN`，無需額外設定 Secrets。

## PR 標題格式

學生以 `學號_姓名` 格式命名 PR（如 `A11218001_林海翔`）。腳本以 `[Cc]\d{9}` 解析學號、`[一-鿿]{2,5}` 解析中文姓名。
