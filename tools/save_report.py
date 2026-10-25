"""하위 에이전트의 보고 문안을 reviews/agents/에 저장한다(HARNESS_SETUP 8장).
사용: python tools/save_report.py <에이전트 출력 파일 경로> <저장할 .md 경로> "<제목>"
에이전트 출력 파일(JSONL)에서 가장 긴 보고(SubagentHandback 메시지 또는 마지막 assistant 글)를 꺼내 제목과 함께 저장한다.
"""
import json, sys
src, out, title = sys.argv[1], sys.argv[2], sys.argv[3]
best = ""
for line in open(src, encoding="utf-8"):
    try:
        o = json.loads(line)
    except ValueError:
        continue
    content = o.get("message", {}).get("content")
    if not isinstance(content, list):
        continue
    for b in content:
        if not isinstance(b, dict):
            continue
        if b.get("type") == "tool_use" and b.get("name") == "SubagentHandback":
            m = b["input"].get("message", "")
        elif b.get("type") == "text" and o.get("message", {}).get("role") == "assistant":
            m = b.get("text", "")
        else:
            continue
        if len(m) > len(best):
            best = m
open(out, "w", encoding="utf-8").write("# " + title + "\n\n" + best.strip() + "\n")
print(f"{out}: {len(best)}자")
