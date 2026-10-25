"""Claude Code PostToolUse 훅: 원고(src/)를 고치면 빌드와 lint를 바로 실행한다.
문제가 있으면 종료 코드 2와 함께 오류를 stderr로 보내 Claude가 즉시 고치게 한다.
"""
import os, json, subprocess, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 저장소 루트 기준으로 실행(F-14)

data = json.load(sys.stdin)
path = (data.get("tool_input") or {}).get("file_path", "")
if "/src/" not in path.replace("\\", "/") and not path.replace("\\", "/").startswith("src/"):
    sys.exit(0)
PAGE = os.path.splitext(os.path.basename(path))[0]  # 고친 쪽(ch05 등)의 문제만 알림: 정비 전 다른 쪽의 경고로 막지 않음

steps = [
    ["python", "tools/build.py"],
    ["python", "lint/check_numbers.py"],
    ["python", "lint/check_structure.py"],
    ["python", "lint/check_style.py"],
]
errors = []
for cmd in steps:
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = (r.stdout + r.stderr).strip()
    mine = [l for l in out.splitlines() if f"/{PAGE}.html" in l or l.startswith(("Traceback", "SystemExit")) or "Error" in l]
    if cmd[1] == "tools/build.py" and r.returncode != 0:
        mine = mine or [out[-800:]]
    if mine:
        errors.append(f"[{' '.join(cmd)}] exit={r.returncode}\n" + "\n".join(mine[-30:]))
g = subprocess.run("git grep -nE -f lint/banned.txt -- index.html chapters appendix",
                   shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
hits = [l for l in g.stdout.splitlines() if f"/{PAGE}.html" in l or l.startswith(f"{PAGE}.html")]
if hits:
    errors.append("[금칙어]\n" + "\n".join(hits[:30]))
if errors:
    print("\n\n".join(errors), file=sys.stderr)
    sys.exit(2)
sys.exit(0)
