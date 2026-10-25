"""책 저장소 전체 검사: 빌드, 금칙어, lint 3종, 그림 점검(, CI에서는 빌드 결과와 커밋 일치).
사용: python tools/check_all.py [--ci]
모든 항목을 실행한 뒤 요약을 출력하고, 하나라도 실패하면 종료 코드 1.
"""
import glob, html, re, subprocess, sys

CI = "--ci" in sys.argv
STRICT_FIG = "--strict-figures" in sys.argv  # 그림 글자 크기를 실패로 볼지(기본은 경고)
MOBILE_MIN_PX = 11.0      # 모바일에서 보이는 가장 작은 글자(px)
SVG_MIN_WIDTH = 560       # style.css의 .diagram svg min-width
FIG_BANNED = ["Claude"]   # 그림 안에 쓰지 않는 이름(D-095)

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout + r.stderr).strip()

results = []
def add(name, ok, detail=""):
    results.append((name, ok, detail))

# 정비를 마친 쪽(lint/rules_applied.txt)은 위반이 실패, 아직 정비하지 않은 쪽은 경고(HARNESS_SETUP 6.3)
APPLIED = {l.strip() for l in open("lint/rules_applied.txt", encoding="utf-8") if l.strip() and not l.startswith("#")}
def page_of(line):
    m = re.search(r"(?:chapters|appendix)/(\w+)\.html|(?<![\w/])(index)\.html", line)
    return (m.group(1) or m.group(2)) if m else None
def add_split(name, lines):
    strict = [l for l in lines if page_of(l) is None or page_of(l) in APPLIED]
    warn = [l for l in lines if l not in strict]
    add(name, not strict, "\n".join(strict[:30]))
    if warn:
        print(f"[경고] {name}(정비 전 쪽 {len({page_of(l) for l in warn})}곳, {len(warn)}건)\n" + "\n".join(warn[:10]) + "\n")

code, out = run("python tools/build.py")
add("빌드", code == 0, out[-300:])

pats = [l.rstrip("\r\n") for l in open("lint/banned.txt", encoding="utf-8") if l.strip() and not l.startswith("#")]  # 끝 공백도 패턴의 일부
hits = []
for f in ["index.html"] + glob.glob("chapters/*.html") + glob.glob("appendix/*.html"):
    for n, line in enumerate(open(f, encoding="utf-8"), 1):
        for p in pats:
            try:
                if re.search(p, line):
                    hits.append(f"{f}:{n}: {p}")
            except re.error:
                pass
add_split("금칙어", hits)

code, out = run("python lint/check_numbers.py")
add("번호", code == 0, out[-800:])
code, out = run("python lint/check_structure.py")
add_split("구조", [l for l in out.splitlines() if l.strip()]) if code != 0 else add("구조", True)

code, out = run("python lint/check_style.py")
warns = [l for l in out.splitlines() if l.startswith("경고 ")]
add_split("문체", warns)

fig_issues = []
fig_small = []
for f in sorted(glob.glob("chapters/*.html") + glob.glob("appendix/*.html") + ["index.html"]):
    t = open(f, encoding="utf-8").read()
    for m in re.finditer(r'<figure[^>]*id="(fig-[^"]+)"(.*?)</figure>', t, re.S):
        fid, body = m.group(1), m.group(2)
        vb = re.search(r'viewBox="0 0 ([\d.]+) [\d.]+"', body)
        sizes = [float(x) for x in re.findall(r'font-size="([\d.]+)"', body)]
        if vb and sizes:
            w = float(vb.group(1)); shown = min(sizes) * SVG_MIN_WIDTH / w if w > SVG_MIN_WIDTH else min(sizes)
            if round(shown, 1) < MOBILE_MIN_PX:
                fig_small.append(f"{f} {fid}: 가장 작은 글자 {min(sizes)}px, 모바일 약 {shown:.1f}px(기준 {MOBILE_MIN_PX})")
        text = html.unescape(re.sub(r"<[^>]+>", " ", body)) + " " + " ".join(re.findall(r'aria-label="([^"]*)"', body))
        for b in FIG_BANNED:
            if b in text:
                fig_issues.append(f"{f} {fid}: 그림 안에 '{b}'")
add("그림 안 이름", not fig_issues, "\n".join(fig_issues[:30]))

# 그림 체계(D-111, FIGURE_STYLE 7절): 제목 상자(맨 위 둥근 사각형, 파랑 테두리)와 맨 아래 "*" 한 줄
fig_system = []
for f in sorted(glob.glob("chapters/*.html") + glob.glob("appendix/*.html")):
    t2 = open(f, encoding="utf-8").read()
    for m in re.finditer(r'<figure[^>]*id="(fig-[^"]+)"(.*?)</figure>', t2, re.S):
        fid, body = m.group(1), m.group(2)
        svg = re.search(r"<svg.*?</svg>", body, re.S)
        if not svg:
            continue
        s = svg.group(0)
        rects = re.findall(r'<rect x="([\d.]+)" y="([\d.]+)"[^>]*rx="14"[^>]*stroke="#0284c7"', s)
        has_title = any(float(y) <= 24 for _, y in rects)
        has_star = bool(re.search(r">\* [^<]+</text>", s))
        if not has_title or not has_star:
            miss = [n for n, ok in (("제목 상자", has_title), ('"*" 한 줄', has_star)) if not ok]
            fig_system.append(f"{f} {fid}: 기준 시각 체계와 다름({', '.join(miss)} 없음)")
STRICT_SYSTEM = "--strict-figures" in sys.argv
if STRICT_SYSTEM:
    add("그림 체계", not fig_system, "\n".join(fig_system[:30]))
elif fig_system:
    print("[경고] 그림 체계(FIGURE_STYLE 7절, 아직 실패로 보지 않음)\n" + "\n".join(fig_system[:30]) + "\n")
if STRICT_FIG:
    add("그림 글자 크기", not fig_small, "\n".join(fig_small[:30]))
elif fig_small:
    print("[경고] 그림 글자 크기(기준 미달, 아직 실패로 보지 않음)\n" + "\n".join(fig_small[:30]) + "\n")

# 검수 규칙(REVIEW_RULES.md, 이슈 #66): 정비를 마친 장(lint/rules_applied.txt)은 실패, 나머지는 경고
code, out = run("python lint/check_rules.py")
add("검수 규칙", code == 0, "\n".join(l for l in out.splitlines() if l.startswith("실패"))[:3000])
rule_warns = [l for l in out.splitlines() if l.startswith(("경고", "정비 전"))]
if rule_warns:
    print("[경고] 검수 규칙(REVIEW_RULES, 정비 전 장과 경고 규칙)\n" + "\n".join(rule_warns[:20]) + "\n")
if CI:
    code, out = run("git diff --exit-code --stat -- index.html chapters appendix")
    add("빌드 결과와 커밋 일치", code == 0, out[-500:])

print("검사 요약")
for name, ok, _ in results:
    print(f"  {'통과' if ok else '실패'}  {name}")
fails = [r for r in results if not r[1]]
for name, _, detail in fails:
    print(f"\n[{name}]\n{detail}")
sys.exit(1 if fails else 0)
