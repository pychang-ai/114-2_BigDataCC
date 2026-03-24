"""
作業自動批改腳本 v2（Fork + PR 模式）
=====================================
功能：
  1. 從老師的 Repo 自動抓取所有 Pull Request
  2. 用 PR 中的檔案路徑判斷屬於哪一週（不依賴標題）
  3. 自動評分並產出報告
  4. 自動將成績回填到 PR 留言
  5. 支援 GitHub Actions 自動觸發

週次判斷優先順序：
  1. PR 中是否包含 weekXX/ 路徑的檔案（最準）
  2. PR 標題中是否包含 weekXX 或 wXX 關鍵字（次準）
  3. PR 建立日期對應學期行事曆（兜底）

使用方式：
  python grade_github.py --repo pychang-ai/114-2_BigDataCC --week week04
  python grade_github.py --repo pychang-ai/114-2_BigDataCC --week week04 --token ghp_xxx --comment
  python grade_github.py --repo pychang-ai/114-2_BigDataCC --pr 53 --token ghp_xxx --comment

參數說明：
  --repo      老師的 Repo（格式：owner/repo）
  --token     GitHub Personal Access Token
  --week      週次（預設自動偵測，或指定 week03~week08）
  --pr        指定批改單一 PR（用於 Actions 觸發）
  --comment   自動將成績貼到 PR 留言
  --output    評分報告輸出路徑
  --csv       CSV 成績單輸出路徑

事前準備：
  pip install requests
"""

import requests
import csv
import re
import sys
import os
import argparse
from datetime import datetime, timezone


# =============================================================
# 學期行事曆：週次對應日期範圍（兜底用）
# 114-2 學期，週二上課
# =============================================================
SEMESTER_WEEKS = {
    "week01": ("2026-02-23", "2026-03-01"),
    "week02": ("2026-03-02", "2026-03-08"),
    "week03": ("2026-03-09", "2026-03-15"),
    "week04": ("2026-03-16", "2026-03-22"),
    "week05": ("2026-03-23", "2026-03-29"),
    "week06": ("2026-03-30", "2026-04-06"),
    "week07": ("2026-04-14", "2026-04-20"),  # 4/7 校慶補休
    "week08": ("2026-04-21", "2026-04-27"),
    "week09": ("2026-04-28", "2026-05-04"),  # 期中考
    "week10": ("2026-05-05", "2026-05-11"),
    "week11": ("2026-05-12", "2026-05-18"),
    "week12": ("2026-05-19", "2026-05-25"),
    "week13": ("2026-05-26", "2026-06-01"),
    "week14": ("2026-06-02", "2026-06-08"),
    "week15": ("2026-06-09", "2026-06-15"),
    "week16": ("2026-06-16", "2026-06-22"),
    "week17": ("2026-06-23", "2026-06-29"),
    "week18": ("2026-06-30", "2026-07-06"),
}

# =============================================================
# 每週作業的檔案對應表
# =============================================================
WEEK_FILES = {
    "week03": {
        "q1": "week03/q1_basic.txt",
        "q2": "week03/q2_fileops.txt",
        "q3": "week03/q3_compare.txt",
    },
    "week04": {
        "q1": "week04/q1_file_commands.txt",
        "q2": "week04/q2_grep_pipe.txt",
        "q3": "week04/q3_concepts.txt",
    },
    "week05": {
        "q1": "week05/q1_nano.txt",
        "q2": "week05/q2_script.txt",
        "q3": "week05/q3_chmod.txt",
    },
    "week06": {
        "q1": "week06/q1_permissions.txt",
        "q2": "week06/q2_directory.txt",
        "q3": "week06/q3_structure.txt",
    },
    "week07": {
        "q1": "week07/q1_packages.txt",
        "q2": "week07/q2_apache.txt",
        "q3": "week07/q3_concepts.txt",
    },
    "week08": {
        "q1": "week08/q1_create_db.txt",
        "q2": "week08/q2_queries.txt",
        "q3": "week08/q3_sql_concepts.txt",
    },
}

# =============================================================
# 通用評分設定
# =============================================================
COMMON_SCORES = {
    "file_exists": 5,
    "name_id": 5,
}


# =============================================================
# GitHub API
# =============================================================
class GitHubAPI:
    def __init__(self, token=None):
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        if token:
            self.headers["Authorization"] = f"token {token}"
        self.api_base = "https://api.github.com"

    def get_pull_requests(self, owner, repo, state="open"):
        prs = []
        page = 1
        while True:
            url = f"{self.api_base}/repos/{owner}/{repo}/pulls"
            params = {"state": state, "per_page": 100, "page": page}
            resp = requests.get(url, headers=self.headers, params=params)
            if resp.status_code != 200:
                print(f"錯誤：無法取得 PR 列表（HTTP {resp.status_code}）")
                break
            data = resp.json()
            if not data:
                break
            prs.extend(data)
            page += 1
        return prs

    def get_single_pr(self, owner, repo, pr_number):
        url = f"{self.api_base}/repos/{owner}/{repo}/pulls/{pr_number}"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code == 200:
            return resp.json()
        return None

    def get_pr_files(self, owner, repo, pr_number):
        """取得 PR 中變更的檔案清單"""
        files = []
        page = 1
        while True:
            url = f"{self.api_base}/repos/{owner}/{repo}/pulls/{pr_number}/files"
            params = {"per_page": 100, "page": page}
            resp = requests.get(url, headers=self.headers, params=params)
            if resp.status_code != 200:
                break
            data = resp.json()
            if not data:
                break
            files.extend(data)
            page += 1
        return files

    def get_file_content(self, owner, repo, filepath, ref="main"):
        url = f"{self.api_base}/repos/{owner}/{repo}/contents/{filepath}"
        params = {"ref": ref}
        resp = requests.get(url, headers=self.headers, params=params)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("encoding") == "base64":
                import base64
                return base64.b64decode(data["content"]).decode("utf-8", errors="replace")
        return None

    def post_comment(self, owner, repo, pr_number, body):
        url = f"{self.api_base}/repos/{owner}/{repo}/issues/{pr_number}/comments"
        resp = requests.post(url, headers=self.headers, json={"body": body})
        return resp.status_code == 201


# =============================================================
# 週次判斷
# =============================================================
def detect_week_from_files(pr_files):
    """從 PR 變更的檔案路徑判斷週次"""
    weeks_found = set()
    for f in pr_files:
        filename = f.get("filename", "")
        match = re.match(r"(week\d{2})/", filename, re.IGNORECASE)
        if match:
            weeks_found.add(match.group(1).lower())
    return sorted(weeks_found)


def detect_week_from_title(title):
    """從 PR 標題判斷週次"""
    title_lower = title.lower().replace(" ", "").replace("-", "").replace("_", "")
    for w in range(18, 0, -1):
        patterns = [f"week{w:02d}", f"week{w}", f"w{w:02d}", f"w{w}"]
        for p in patterns:
            if p in title_lower:
                return f"week{w:02d}"
    return None


def detect_week_from_date(created_at):
    """從 PR 建立日期判斷週次"""
    pr_date = datetime.fromisoformat(created_at.replace("Z", "+00:00")).date()
    for week, (start, end) in SEMESTER_WEEKS.items():
        s = datetime.strptime(start, "%Y-%m-%d").date()
        e = datetime.strptime(end, "%Y-%m-%d").date()
        if s <= pr_date <= e:
            return week
    return None


def detect_week(api, owner, repo, pr):
    """綜合判斷 PR 屬於哪一週"""
    pr_number = pr["number"]

    # 方法 1：檔案路徑（最準）
    pr_files = api.get_pr_files(owner, repo, pr_number)
    weeks_from_files = detect_week_from_files(pr_files)
    if weeks_from_files:
        return weeks_from_files, "files"

    # 方法 2：標題
    week_from_title = detect_week_from_title(pr["title"])
    if week_from_title:
        return [week_from_title], "title"

    # 方法 3：日期
    week_from_date = detect_week_from_date(pr["created_at"])
    if week_from_date:
        return [week_from_date], "date"

    return [], "unknown"


# =============================================================
# 通用評分函式
# =============================================================
def check_name_id(content):
    has_name = False
    has_id = False
    for line in content.split("\n"):
        if "姓名" in line and "???" not in line and "XXX" not in line and len(line.strip()) > 3:
            has_name = True
        if "學號" in line and "???" not in line and "XXX" not in line and len(line.strip()) > 3:
            has_id = True
    return has_name and has_id


def count_sections(content, marker_prefix="==="):
    """計算內容中有多少個已填寫的區塊"""
    sections = re.split(r"===.*?===", content)
    filled = 0
    for s in sections[1:]:  # 跳過第一段（姓名學號區）
        text = s.strip()
        if text and text != "???" and len(text) > 2:
            lines = [l.strip() for l in text.split("\n") if l.strip()]
            if lines:
                filled += 1
    return filled


def count_answers(content):
    """計算 Q&A 格式中有多少題已回答"""
    answered = 0
    for match in re.finditer(r"A\d+[：:](.+?)(?=Q\d+|$)", content, re.DOTALL):
        answer = match.group(1).strip()
        if answer and answer != "???" and len(answer) >= 5:
            answered += 1
    return answered


def grade_generic(content, week, question_num, config):
    """通用評分：檔案存在 + 姓名學號 + 區塊填寫 + 觀念回答"""
    score = 0
    details = []

    if content is None:
        return 0, [{"item": f"q{question_num} 檔案", "score": 0, "status": "FAIL", "note": "檔案不存在"}]

    # 檔案存在
    score += 5
    details.append({"item": "檔案存在", "score": 5, "status": "PASS", "note": "檔案存在"})

    # 姓名學號
    if check_name_id(content):
        score += 5
        details.append({"item": "姓名學號", "score": 5, "status": "PASS", "note": "已填寫"})
    else:
        details.append({"item": "姓名學號", "score": 0, "status": "FAIL", "note": "未填寫或仍為預設值"})

    if question_num in (1, 2):
        # 第 1、2 題：計算已填寫的區塊數
        total_sections = count_sections(content)
        max_section_score = 30 if question_num == 1 else 30
        section_score = min(total_sections * 5, max_section_score)
        score += section_score
        details.append({"item": "內容填寫", "score": section_score, "status": "PASS" if section_score >= max_section_score else "PARTIAL", "note": f"已填寫 {total_sections} 個區塊"})
    else:
        # 第 3 題：計算觀念題回答數
        answered = count_answers(content)
        answer_score = min(answered * 3, 10)
        score += answer_score
        details.append({"item": "觀念回答", "score": answer_score, "status": "PASS" if answered >= 3 else "PARTIAL", "note": f"已回答 {answered} 題"})

    return score, details


# =============================================================
# 模糊檔名匹配
# =============================================================
def generate_alt_paths(week, key):
    """產生可能的替代檔名"""
    alt = []
    # week03 的檔名被用在 week04
    week03_names = {"q1": "q1_basic.txt", "q2": "q2_fileops.txt", "q3": "q3_compare.txt"}
    if key in week03_names:
        alt.append(f"{week}/{week03_names[key]}")
    # 沒有 .txt 副檔名
    week_files = WEEK_FILES.get(week, {})
    if key in week_files:
        base = week_files[key].replace(".txt", "")
        alt.append(base)
    # 簡化檔名（txt1, txt2, txt3）
    num = {"q1": "1", "q2": "2", "q3": "3"}.get(key, "")
    if num:
        alt.append(f"{week}/txt{num}")
        alt.append(f"{week}/q{num}.txt")
        alt.append(f"{week}/Q{num}.txt")
    return alt


# =============================================================
# PR 批改
# =============================================================
def grade_pr(api, pr, target_week, owner, repo):
    """批改單一 PR"""
    fork_owner = pr["head"]["repo"]["owner"]["login"] if pr["head"]["repo"] else None
    fork_repo = pr["head"]["repo"]["name"] if pr["head"]["repo"] else None
    fork_branch = pr["head"]["ref"]
    pr_title = pr["title"]
    pr_number = pr["number"]
    pr_user = pr["user"]["login"]
    pr_created = pr["created_at"]

    # 從標題解析學號和姓名
    student_id = ""
    student_name = ""
    parts = re.split(r"[_\s/]+", pr_title)
    for p in parts:
        if re.match(r"[Cc]\d{9}", p):
            student_id = p.upper()
        elif re.match(r"[\u4e00-\u9fff]{2,5}", p):
            student_name = p

    result = {
        "pr_number": pr_number,
        "pr_title": pr_title,
        "pr_user": pr_user,
        "pr_created": pr_created,
        "student_id": student_id,
        "student_name": student_name,
        "week": target_week,
        "fork": f"{fork_owner}/{fork_repo}" if fork_owner else "unknown",
        "total_score": 0,
        "q1_score": 0,
        "q2_score": 0,
        "q3_score": 0,
        "details": {},
        "file_contents": {},
        "errors": [],
    }

    if not fork_owner or not fork_repo:
        result["errors"].append("無法取得 Fork 資訊，可能 Fork 已刪除")
        return result

    # 取得對應週次的檔案路徑
    week_files = WEEK_FILES.get(target_week)
    if not week_files:
        result["errors"].append(f"不支援的週次：{target_week}")
        return result

    # 抓取檔案並評分（先嘗試標準檔名，再嘗試模糊匹配）
    contents = {}
    for key, path in week_files.items():
        content = api.get_file_content(fork_owner, fork_repo, path, ref=fork_branch)
        if not content:
            # 模糊匹配：嘗試不同的檔名格式
            alt_paths = generate_alt_paths(target_week, key)
            for alt in alt_paths:
                content = api.get_file_content(fork_owner, fork_repo, alt, ref=fork_branch)
                if content:
                    result["file_contents"][alt] = content
                    break
        if content:
            contents[key] = content
            if path not in result["file_contents"]:
                result["file_contents"][path] = content
        else:
            contents[key] = None

    q1_score, q1_details = grade_generic(contents["q1"], target_week, 1, None)
    q2_score, q2_details = grade_generic(contents["q2"], target_week, 2, None)
    q3_score, q3_details = grade_generic(contents["q3"], target_week, 3, None)

    result["q1_score"] = q1_score
    result["q2_score"] = q2_score
    result["q3_score"] = q3_score
    result["total_score"] = q1_score + q2_score + q3_score
    result["details"] = {
        "第1題": q1_details,
        "第2題": q2_details,
        "第3題": q3_details,
    }

    return result


# =============================================================
# 產生 PR 留言
# =============================================================
def generate_pr_comment(result):
    week_display = result["week"].replace("week", "第 ") + " 週"
    lines = []
    lines.append(f"## {week_display}自動批改結果")
    lines.append("")
    lines.append(f"| 題目 | 分數 |")
    lines.append(f"|------|------|")
    lines.append(f"| 第 1 題 | {result['q1_score']} / 40 |")
    lines.append(f"| 第 2 題 | {result['q2_score']} / 40 |")
    lines.append(f"| 第 3 題 | {result['q3_score']} / 20 |")
    lines.append(f"| **總分** | **{result['total_score']} / 100** |")
    lines.append("")

    for section_name, detail_list in result["details"].items():
        lines.append(f"### {section_name}")
        for d in detail_list:
            icon = {"PASS": ":white_check_mark:", "PARTIAL": ":warning:", "FAIL": ":x:"}[d["status"]]
            lines.append(f"- {icon} {d['item']}: **{d['score']} 分** - {d['note']}")
        lines.append("")

    if result["total_score"] >= 60:
        lines.append("> :tada: 通過！做得好！")
    else:
        lines.append("> :memo: 未達 60 分，請修改後重新 push，分數會自動更新。")

    lines.append("")
    lines.append(f"*自動批改時間：{datetime.now().strftime('%Y-%m-%d %H:%M')}*")

    return "\n".join(lines)


# =============================================================
# 報告產生
# =============================================================
def generate_report(all_results, repo_name, week):
    lines = []
    lines.append("=" * 70)
    lines.append(f"{week} 作業自動評分報告")
    lines.append(f"課程 Repo：{repo_name}")
    lines.append(f"產出時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"PR 總數：{len(all_results)}")
    lines.append("=" * 70)
    lines.append("")

    lines.append("【成績總覽】")
    lines.append(f"{'PR#':<5} {'GitHub帳號':<18} {'學號':<14} {'姓名':<8} {'週次':<8} {'Q1':>4} {'Q2':>4} {'Q3':>4} {'總分':>6}")
    lines.append("-" * 80)
    for r in all_results:
        lines.append(f"#{r['pr_number']:<4} {r['pr_user']:<18} {r['student_id']:<14} {r['student_name']:<8} {r['week']:<8} {r['q1_score']:>4} {r['q2_score']:>4} {r['q3_score']:>4} {r['total_score']:>4}")
    lines.append("")

    scores = [r["total_score"] for r in all_results]
    if scores:
        lines.append(f"人數：{len(scores)}  最高：{max(scores)}  最低：{min(scores)}  平均：{sum(scores)/len(scores):.1f}")
        lines.append("")

    for r in all_results:
        lines.append("=" * 70)
        lines.append(f"PR #{r['pr_number']}：{r['pr_title']}")
        lines.append(f"GitHub 帳號：{r['pr_user']}  Fork：{r['fork']}  週次：{r['week']}")
        lines.append(f"繳交時間：{r['pr_created']}")
        lines.append(f"總分：{r['total_score']} / 100（Q1:{r['q1_score']} Q2:{r['q2_score']} Q3:{r['q3_score']}）")

        if r["errors"]:
            lines.append(f"錯誤：{'; '.join(r['errors'])}")
            lines.append("")
            continue

        lines.append("-" * 50)

        for section_name, detail_list in r["details"].items():
            lines.append(f"\n  {section_name}")
            for d in detail_list:
                icon = {"PASS": "V", "PARTIAL": "~", "FAIL": "X"}[d["status"]]
                lines.append(f"    [{icon}] {d['item']}: {d['score']} 分 - {d['note']}")

        if r["file_contents"]:
            lines.append(f"\n  檔案內容：")
            for filepath, content in r["file_contents"].items():
                lines.append(f"  --- {filepath} ---")
                for line in content.strip().split("\n")[:30]:
                    lines.append(f"    {line}")
                total_lines = len(content.strip().split("\n"))
                if total_lines > 30:
                    lines.append(f"    ...（共 {total_lines} 行，僅顯示前 30 行）")
        lines.append("")

    lines.append("=" * 70)
    lines.append("【給 Claude 的複審指示】")
    lines.append("請根據以上報告協助複審：")
    lines.append("1. 第 3 題觀念題：檢查回答品質，是否用自己的話表達")
    lines.append("2. 抄襲檢查：比對各學生的第 3 題，標記高度相似的")
    lines.append("3. 第 1、2 題：確認輸出內容是否合理（非亂填）")
    lines.append("4. 請輸出最終成績表：PR# | GitHub帳號 | 學號 | 姓名 | Q1 | Q2 | Q3 | 最終總分 | 備註")
    lines.append("=" * 70)

    return "\n".join(lines)


def generate_csv(all_results, output_path):
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["PR#", "GitHub帳號", "學號", "姓名", "週次", "繳交時間", "第1題", "第2題", "第3題", "總分", "備註"])
        for r in all_results:
            errors = "; ".join(r["errors"]) if r["errors"] else ""
            writer.writerow([
                r["pr_number"], r["pr_user"], r["student_id"], r["student_name"],
                r["week"], r["pr_created"], r["q1_score"], r["q2_score"], r["q3_score"],
                r["total_score"], errors
            ])


# =============================================================
# 主程式
# =============================================================
def main():
    parser = argparse.ArgumentParser(description="作業自動批改腳本 v2（Fork + PR 模式）")
    parser.add_argument("--repo", required=True, help="老師的 Repo（格式：owner/repo）")
    parser.add_argument("--token", default=None, help="GitHub Personal Access Token")
    parser.add_argument("--week", default=None, help="指定批改的週次（如 week04），不指定則自動偵測")
    parser.add_argument("--pr", type=int, default=None, help="指定批改單一 PR 編號（用於 Actions）")
    parser.add_argument("--comment", action="store_true", help="自動將成績貼到 PR 留言")
    parser.add_argument("--output", default=None, help="評分報告輸出路徑")
    parser.add_argument("--csv", default=None, help="CSV 成績單輸出路徑")
    args = parser.parse_args()

    # 從環境變數取得 token（Actions 用）
    if not args.token:
        args.token = os.environ.get("GITHUB_TOKEN")

    # 解析 repo
    repo_parts = args.repo.split("/")
    if len(repo_parts) != 2:
        print("錯誤：--repo 格式應為 owner/repo")
        sys.exit(1)
    owner, repo = repo_parts

    api = GitHubAPI(token=args.token)

    # 模式 1：批改單一 PR（Actions 觸發）
    if args.pr:
        print(f"批改單一 PR #{args.pr}...")
        pr = api.get_single_pr(owner, repo, args.pr)
        if not pr:
            print(f"錯誤：找不到 PR #{args.pr}")
            sys.exit(1)

        weeks, method = detect_week(api, owner, repo, pr)
        if not weeks:
            print(f"無法判斷 PR #{args.pr} 的週次")
            sys.exit(0)

        target_week = weeks[0]
        print(f"偵測到週次：{target_week}（依據：{method}）")

        result = grade_pr(api, pr, target_week, owner, repo)
        print(f"PR #{result['pr_number']} {result['pr_user']}: {result['total_score']} 分")

        if args.comment:
            comment_body = generate_pr_comment(result)
            success = api.post_comment(owner, repo, result["pr_number"], comment_body)
            print(f"留言：{'成功' if success else '失敗'}")

        return

    # 模式 2：批次批改（手動執行）
    target_week = args.week

    if not args.output:
        args.output = f"{target_week or 'all'}_report.txt"
    if not args.csv:
        args.csv = f"{target_week or 'all'}_scores.csv"

    print(f"課程 Repo：{owner}/{repo}")
    print(f"目標週次：{target_week or '自動偵測'}")
    print("")

    # 取得所有 open PR
    print("正在取得 Pull Request 列表...")
    prs = api.get_pull_requests(owner, repo, state="open")
    print(f"找到 {len(prs)} 個 open PR")
    print("")

    if not prs:
        print("沒有找到任何 open PR")
        sys.exit(0)

    # 逐一判斷週次並批改
    all_results = []
    skipped = 0
    for i, pr in enumerate(prs, 1):
        # 偵測週次
        weeks, method = detect_week(api, owner, repo, pr)

        if not weeks:
            print(f"[{i}/{len(prs)}] PR #{pr['number']} - {pr['title']}: 無法判斷週次，跳過")
            skipped += 1
            continue

        pr_week = weeks[0]

        # 如果指定了週次，只要 PR 包含該週的檔案就批改
        if target_week and target_week not in weeks:
            continue
        
        # 使用目標週次，或 PR 中第一個偵測到的週次
        if target_week and target_week in weeks:
            pr_week = target_week

        print(f"[{i}/{len(prs)}] PR #{pr['number']} - {pr['title']} ({pr['user']['login']}) [{pr_week}/{method}]...", end=" ")
        result = grade_pr(api, pr, pr_week, owner, repo)
        all_results.append(result)
        if result["errors"]:
            print(f"錯誤: {result['errors'][0]}")
        else:
            print(f"{result['total_score']} 分（Q1:{result['q1_score']} Q2:{result['q2_score']} Q3:{result['q3_score']}）")

    if not all_results:
        print(f"\n沒有找到{f' {target_week} 的' if target_week else '可批改的'} PR")
        sys.exit(0)

    # 產出報告
    report = generate_report(all_results, f"{owner}/{repo}", target_week or "all")
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n評分報告：{args.output}")

    # 匯出 CSV
    generate_csv(all_results, args.csv)
    print(f"成績單：{args.csv}")

    # 自動留言到 PR
    if args.comment:
        print("\n正在將成績貼到 PR 留言...")
        for r in all_results:
            comment_body = generate_pr_comment(r)
            success = api.post_comment(owner, repo, r["pr_number"], comment_body)
            status = "已留言" if success else "留言失敗"
            print(f"  PR #{r['pr_number']} {r['pr_user']}: {status}")

    # 統計
    scores = [r["total_score"] for r in all_results]
    if scores:
        print(f"\n--- 統計 ---")
        print(f"人數：{len(scores)}  最高：{max(scores)}  最低：{min(scores)}  平均：{sum(scores)/len(scores):.1f}")
        if skipped:
            print(f"跳過（無法判斷週次）：{skipped} 個")

    print(f"\n請將 {args.output} 的內容貼到 Claude 進行複審")


if __name__ == "__main__":
    main()
