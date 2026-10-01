"""그림, 표 번호 검사. 문제가 없으면 아무것도 출력하지 않고 종료 코드 0을 돌려준다.

검사 항목
1. 페이지 안에서 그림, 표 번호가 각각 1부터 빠짐없이 순서대로 매겨졌는지
2. 장 번호-순번 형식(예: 표 3-1)이 여러 페이지에서 중복되지 않는지
3. 본문이 가리키는 번호가 실제로 있는지
4. 본문의 번호 참조에 링크가 걸려 있는지
5. 번호 뒤 조사가 마지막 숫자의 받침과 맞는지(0, 1, 3, 6, 7, 8 뒤에는 은, 이, 을, 과, 나머지 숫자 뒤에는 는, 가, 를, 와)

표지(index.html)는 번호와 캡션을 두지 않으므로 검사하지 않는다.
"""
import glob
import re
import sys

files = sorted(glob.glob("chapters/*.html")) + sorted(glob.glob("appendix/*.html")) + sorted(glob.glob("wiki/*.html"))
CAP = re.compile(r"<figcaption><b>((그림|표) (?:([0-9A-Z]+|부[0-9]+)-)?([0-9]+))\.")
REF = re.compile(r"(?:그림|표) (?:[0-9A-Z]+|부[0-9]+)-[0-9]+")
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
    linked = set(re.findall(r"<a [^>]*>((?:그림|표) (?:[0-9A-Z]+|부[0-9]+)-[0-9]+)</a>", body))
    plain = re.sub(r"<a [^>]*>.*?</a>", "", body, flags=re.S)
    plain = re.sub(r"<[^>]+>", " ", plain)
    for r in sorted(set(REF.findall(re.sub(r"<[^>]+>", " ", body)))):
        if r not in owner:
            errors.append(f"없는 번호 참조: {f} {r}")
    for r in sorted(set(REF.findall(plain))):
        errors.append(f"링크 없는 번호 참조: {f} {r}")

# 5. 번호 뒤 조사: 마지막 숫자를 읽었을 때 받침이 있으면 은/이/을/과, 없으면 는/가/를/와
BATCHIM = set("013678")
PAIR = {"은": "는", "는": "은", "이": "가", "가": "이", "을": "를", "를": "을", "과": "와", "와": "과"}
WITH = set("은이을과")
JOSA = re.compile(r"((?:표|그림) (?:(?:[0-9A-Z]+|부[0-9]+)-)?(\d+))(?:</a>)?([은는이가을를과와])(?![가-힣])")
for f in files:
    body = open(f, encoding="utf-8").read()
    for m in JOSA.finditer(body):
        need_with = m.group(2)[-1] in BATCHIM
        if (m.group(3) in WITH) != need_with:
            errors.append(f"조사 오류: {f} {m.group(1)}{m.group(3)} → {m.group(1)}{PAIR[m.group(3)]}")

idx = open("index.html", encoding="utf-8").read()
if "<figcaption" in idx:
    errors.append("표지에 캡션이 있음: index.html")

for e in errors:
    print(e)
sys.exit(1 if errors else 0)

