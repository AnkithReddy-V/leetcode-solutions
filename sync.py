import os
import sys
import time
import requests

SESSION = os.environ["LEETCODE_SESSION"]
CSRF = os.environ["LEETCODE_CSRF_TOKEN"]

HEADERS = {
    "Content-Type": "application/json",
    "Cookie": f"csrftoken={CSRF}; LEETCODE_SESSION={SESSION}",
    "x-csrftoken": CSRF,
    "Origin": "https://leetcode.com",
    "Referer": "https://leetcode.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

GRAPHQL_URL = "https://leetcode.com/graphql"

LANG_EXT = {
    "python3": "py", "python": "py", "java": "java",
    "cpp": "cpp", "c": "c", "javascript": "js",
    "typescript": "ts", "go": "go", "rust": "rs",
    "kotlin": "kt", "swift": "swift", "ruby": "rb",
    "scala": "scala", "csharp": "cs", "mysql": "sql",
    "mssql": "sql", "oraclesql": "sql"
}

# Read args: python sync.py --folder DSA
# or:        python sync.py --folder SQL --lang sql
folder = "DSA"
lang_filter = None

for i, arg in enumerate(sys.argv[1:]):
    if arg == "--folder":
        folder = sys.argv[i + 2]
    if arg == "--lang":
        lang_filter = sys.argv[i + 2].lower()

os.makedirs(folder, exist_ok=True)


def get_all_submissions():
    submissions = []
    
    # First get your username
    profile_query = {
        "query": """
        query globalData {
          userStatus {
            username
          }
        }
        """
    }
    resp = requests.post(GRAPHQL_URL, json=profile_query, headers=HEADERS)
    resp_json = resp.json()
    print("Profile response:", resp_json)
    
    username = resp_json["data"]["userStatus"]["username"]
    print(f"Logged in as: {username}")

    # Use recentAcSubmissionList instead
    query = {
        "query": """
        query recentAcSubmissions($username: String!, $limit: Int!) {
          recentAcSubmissionList(username: $username, limit: $limit) {
            id
            title
            titleSlug
            lang
            timestamp
          }
        }
        """,
        "variables": {"username": username, "limit": 100}
    }

    resp = requests.post(GRAPHQL_URL, json=query, headers=HEADERS)
    resp_json = resp.json()
    print("Submissions response:", resp_json)

    subs = resp_json.get("data", {}).get("recentAcSubmissionList") or []
    for sub in subs:
        sub["statusDisplay"] = "Accepted"
        submissions.append(sub)

    return submissions


def get_submission_code(submission_id):
    query = {
        "query": """
        query submissionDetails($submissionId: Int!) {
          submissionDetails(submissionId: $submissionId) {
            code
            lang { name }
          }
        }
        """,
        "variables": {"submissionId": int(submission_id)}
    }
    resp = requests.post(GRAPHQL_URL, json=query, headers=HEADERS)
    time.sleep(0.5)
    return resp.json()["data"]["submissionDetails"]


def get_problem_details(slug):
    query = {
        "query": """
        query questionData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            difficulty
            content
          }
        }
        """,
        "variables": {"titleSlug": slug}
    }
    resp = requests.post(GRAPHQL_URL, json=query, headers=HEADERS)
    time.sleep(0.5)
    return resp.json()["data"]["question"]


seen_slugs = set()
submissions = get_all_submissions()
print(f"Found {len(submissions)} accepted submissions")

for sub in submissions:
    slug = sub["titleSlug"]
    lang = sub["lang"].lower()

    # Apply language filter if set (e.g. SQL workflow only wants sql)
    if lang_filter and lang_filter not in lang:
        continue

    if slug in seen_slugs:
        continue
    seen_slugs.add(slug)

    print(f"Processing: {sub['title']}")

    try:
        details = get_problem_details(slug)
        code_data = get_submission_code(sub["id"])

        if not code_data:
            print(f"  Skipping {slug} — could not fetch code")
            continue

        problem_id = details["questionFrontendId"].zfill(4)
        title = details["title"]
        difficulty = details["difficulty"]
        ext = LANG_EXT.get(lang, "txt")
        url = f"https://leetcode.com/problems/{slug}/"
        code = code_data["code"]

        problem_folder = os.path.join(folder, f"{problem_id}-{slug}")
        os.makedirs(problem_folder, exist_ok=True)

        readme_path = os.path.join(problem_folder, "README.md")
        if not os.path.exists(readme_path):
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(f"# {problem_id}. {title}\n\n")
                f.write(f"**Difficulty:** {difficulty}  \n")
                f.write(f"**URL:** [{url}]({url})\n\n")
                f.write(f"## Problem\n\n")
                f.write(details.get("content", "_Description not available_"))

        solution_path = os.path.join(problem_folder, f"solution.{ext}")
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write(code)

        print(f"  Saved → {problem_folder}/")

    except Exception as e:
        print(f"  Error on {slug}: {e}")

print("Sync complete.")
