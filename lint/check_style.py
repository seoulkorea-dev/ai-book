"""B 배제어 경고 검사. 한자어 치환 후보를 출력만 하고 종료 코드는 항상 0이다.

치환 기준은 STYLE.md의 어휘 선택 절차를 따른다. 코드 상자 속 프롬프트도 검사한다. 뜻에 따라 바꿀 말이 다르므로
자동으로 고치지 않고, 위치와 문맥만 보여 준다.
"""
import glob
import re
import html
from collections import Counter

# 치환 대상 동사는 어간 뒤 모든 어미를 잡는다(관형형, 과거형, 연결형). 앞에 한글이 붙으면 다른 낱말(원고를, 덧붙이다)이라 제외
B = re.compile(
    r"(?<![가-힣])(?:쓰[고지기며면는]|써[도서야 ]|썼|씁|쓸 |쓴 |쓰십시오)"
    r"|(?<![가-힣])넣[고기어으을은었지는습]"
    r"|(?<![가-힣])(?:바꾸|바꿉|바꿔|바뀌|바꾼|바꿀|바꿨)"
    r"|(?<![가-힣])(?:고르|고릅|고른|골라|골랐|고를)"
    r"|(?<![가-힣])(?:고치|고칩|고친|고쳐|고칠|고쳤)"
    r"|(?<![가-힣])(?:붙이|붙입|붙인|붙일|붙여|붙였)"
    r"|(?<![가-힣])(?:틀리|틀린|틀릴|틀렸)"
    r"|알아채|잘하는|못하는|좋아지|나빠지|만들어 내|찾아내|끄는"
)
# 정상 예외: 고르지 않다, 고르게(균등하다 뜻), 붙여 넣다, 읽기와 쓰기(권한 이름), 일부러 보인 나쁜 예(개선 전 프롬프트)
EXCEPT = re.compile(r"고르지 않|고르게|붙여 넣|읽기와 쓰기|나와\. 고쳐 줘|자기소개서 써 줘")
files = ["index.html"] + sorted(glob.glob("chapters/*.html")) + sorted(glob.glob("appendix/*.html"))
total = Counter()
for f in files:
    body = open(f, encoding="utf-8").read()
    # 표의 예제 열(작성 예제, 적용 예제, 요청 예제) 셀 속 프롬프트 말투도 "~해 줘"
    for t in re.findall(r"<table.*?</table>", body, flags=re.S):
        heads = re.findall(r"<th>(.*?)</th>", t)
        cols = [i for i, h in enumerate(heads) if h in ("작성 예제", "적용 예제", "요청 예제")]
        for row in re.findall(r"<tr>(.*?)</tr>", t, flags=re.S):
            cells = re.findall(r"<td[^>]*>(.*?)</td>", row, flags=re.S)
            for i in cols:
                if i < len(cells) and "십시오" in cells[i]:
                    total["표 예제 십시오"] += 1
                    print(f"경고 {f}: 표 예제 칸 '십시오' | {re.sub('<[^>]+>', '', cells[i])[:40]}")
    # 코드 상자 속 프롬프트 예제는 예외(STYLE.md 배제어). 줄 번호를 유지하도록 줄바꿈만 남긴다
    # 코드 상자 속 프롬프트 말투는 "~해 줘"(STYLE.md). "십시오"가 남으면 따로 경고
    for m in re.finditer(r"<pre.*?</pre>", body, flags=re.S):
        # 입력 자료 태그(&lt;공지문&gt; 등) 안의 원문은 원래 문체를 유지하므로 제외
        k = re.sub(r"&lt;([^&/]+)&gt;.*?&lt;/\1&gt;", "", m.group(0), flags=re.S).count("십시오")
        if k:
            total["코드 상자 십시오"] += k
            print(f"경고 {f}: 코드 상자 속 '십시오' {k}건")
    # 본문 큰따옴표 안의 인용 프롬프트 말투도 "~해 줘"(코드 상자, 표 제외). 인용 프롬프트인지는 사람이 판단
    prose = re.sub(r"<(pre|table|svg)\b.*?</\1>", " ", body, flags=re.S)
    for q in re.findall(r'"([^"<>]*십시오[^"<>]*)"', re.sub(r"<[^>]+>", "", prose.replace("&quot;", '"'))):
        total["인용 십시오"] += 1
        print(f"경고 {f}: 큰따옴표 인용 '십시오' | {q[:40]}")
    for n, line in enumerate(body.split("\n"), 1):
        text = re.sub(r"<svg.*?</svg>|<[^>]+>", " ", line)
        for m in B.finditer(text):
            if EXCEPT.search(text[max(0, m.start() - 10):m.end() + 10]):
                continue
            total[m.group(0)] += 1
            print(f"경고 {f}:{n}: {m.group(0)} | {text[max(0, m.start() - 20):m.end() + 15].strip()}")
# 문장 원칙(2026-10-02): 100자 넘는 문장, 문장 첫머리 "그리고, 다만, 또한, 특히"를 경고(표, 그림, 코드 상자, 참고 자료 서지 제외)
for f in files:
    if f.endswith("references.html"):
        continue
    body = re.sub(r"<(pre|table|svg|figure)\b.*?</\1>", " ", open(f, encoding="utf-8").read(), flags=re.S)
    for para in re.findall(r"<(?:p|li)\b[^>]*>(.*?)</(?:p|li)>", body, flags=re.S):
        text = html.unescape(re.sub(r"<[^>]+>", "", para)).strip()
        for sent in re.split(r"(?<=[.?!])\s+(?=[^)\s])", text):
            sent = sent.strip()
            if len(sent) > 100:
                total["100자 초과 문장"] += 1
                print(f"경고 {f}: 100자 초과({len(sent)}자) | {sent[:40]}")
            if re.match(r"(그리고|다만|또한|특히)[ ,]", sent):
                total["첫머리 접속어"] += 1
                print(f"경고 {f}: 첫머리 접속어 | {sent[:40]}")

if total:
    print("B 배제어 경고 합계:", sum(total.values()), dict(total.most_common()))
