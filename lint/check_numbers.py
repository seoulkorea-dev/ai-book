"""그림, 표 번호 검사. 문제가 없으면 아무것도 출력하지 않고 종료 코드 0을 돌려준다.

검사 항목
1. 페이지 안에서 그림, 표 번호가 각각 1부터 빠짐없이 순서대로 매겨졌는지
2. 장 번호-순번 형식(예: 표 3-1)이 여러 페이지에서 중복되지 않는지
3. 본문이 가리키는 번호가 실제로 있는지
4. 본문의 번호 참조에 링크가 걸려 있는지
"""
import glob
import re
import sys

files = ["index.html"] + sorted(glob.glob("chapters/*.html")) + sorted(glob.glob("appendix/*.html")) + sorted(glob.glob("wiki/*.html"))
CAP = re.compile(r"<figcaption><b>((그림|표) (?:([0-9A-Z]+)-)?([0-9]+))\.")
REF = re.compile(r"(?:그림|표) [0-9A-Z]+-[0-9]+")
errors = []
owner = {}

for f in files:
    html = open(f, encoding="utf-8").read()
    seq = {}
    for full, kind, prefix, n in CAP.findall(html):
        seq.setdefault((kind, prefix), []).append(int(n))
        if prefix:
            if full in owner:
                errors.append(f"중복 번호: {full} ({owner[full]}, {f})")
            owner[full] = f
    for (kind, prefix), nums in seq.items():
        if nums != list(range(1, len(nums) + 1)):
            errors.append(f"순서, 누락 이상: {f} {kind} {prefix or ''} {nums}")

for f in files:
    html = open(f, encoding="utf-8").read()
    body = re.sub(r"<(figcaption|pre|svg)[^>]*>.*?</\1>", "", html, flags=re.S)
    linked = set(re.findall(r"<a [^>]*>((?:그림|표) [0-9A-Z]+-[0-9]+)</a>", body))
    plain = re.sub(r"<a [^>]*>.*?</a>", "", body, flags=re.S)
    plain = re.sub(r"<[^>]+>", " ", plain)
    for r in sorted(set(REF.findall(re.sub(r"<[^>]+>", " ", body)))):
        if r not in owner:
            errors.append(f"없는 번호 참조: {f} {r}")
    for r in sorted(set(REF.findall(plain))):
        errors.append(f"링크 없는 번호 참조: {f} {r}")

for e in errors:
    print(e)
sys.exit(1 if errors else 0)
