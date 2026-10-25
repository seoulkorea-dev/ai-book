"""점검 보고의 지적 표를 원고에 한 번에 반영한다(HARNESS_SETUP 3장 7, 9).
사용: python tools/apply_review.py <보고 .md> [건너뛸 번호,쉼표로]
- "지적 표" 절의 표 행에서 위치 칸의 src/ 경로, 원문과 고친 문안 칸의 backtick 문자열을 읽는다.
- 원문이 그 파일에 정확히 한 번 있을 때만 바꾼다. 원문 칸 문자열이 하나가 아니거나 찾지 못하면 "수동"으로 알린다.
- 원문과 고친 문안의 "⏎"는 줄바꿈으로 읽는다.
- 고친 문안 칸에 backtick 문자열이 여럿이면 줄바꿈으로 이어 붙인다("(줄바꿈)" 표시는 무시).
결과: 반영한 번호와 수동 처리할 번호. 반영 뒤 python tools/check_all.py로 확인한다.
"""
import re, sys
report = open(sys.argv[1], encoding="utf-8").read()
skip = {int(x) for x in (sys.argv[2].split(",") if len(sys.argv) > 2 and sys.argv[2] else [])}
m = re.search(r"#+\s*\d*\.?\s*지적 표(.*?)(?=\n#+\s|\Z)", report, re.S)
section = m.group(1) if m else report
texts, done, manual, cur = {}, [], [], None
for line in section.splitlines():
    line = line.strip()
    mm = re.match(r"\|\s*(\d+)\s*\|", line)
    if not mm:
        continue
    n = int(mm.group(1))
    cells = [c.strip() for c in line.strip("|").split(" | ")]
    pm = re.search(r"(src/\S+?\.(?:html|json))", " ".join(cells[:4]))
    if pm:
        cur = pm.group(1)
    if n in skip:
        continue
    if cur is None or len(cells) < 6:
        manual.append((n, "형식")); continue
    old = re.findall(r"`([^`]+)`", cells[-2]); new = [x for x in re.findall(r"`([^`]+)`", cells[-1]) if x != "(줄바꿈)"]
    if len(old) != 1 or not new:
        manual.append((n, f"원문 {len(old)}개, 고친 문안 {len(new)}개")); continue
    if cur not in texts:
        texts[cur] = open(cur, encoding="utf-8").read()
    o, w = old[0].replace("<\\", "<").replace("⏎", "\n"), "\n".join(new).replace("<\\", "<").replace("⏎", "\n")
    c = texts[cur].count(o)
    if c != 1:
        manual.append((n, f"원문 {c}회")); continue
    texts[cur] = texts[cur].replace(o, w); done.append(n)
for f, t in texts.items():
    open(f, "w", encoding="utf-8").write(t)
print("반영", done)
print("수동", manual)
