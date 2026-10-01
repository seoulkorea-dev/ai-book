"""B 배제어 경고 검사. 한자어 치환 후보를 출력만 하고 종료 코드는 항상 0이다.

치환 기준은 STYLE.md의 어휘 선택 절차를 따른다. 코드 상자(<pre>) 속 프롬프트 예제는 검사하지 않는다. 뜻에 따라 바꿀 말이 다르므로
자동으로 고치지 않고, 위치와 문맥만 보여 준다.
"""
import glob
import re
from collections import Counter

B = re.compile(r"고르[^게]|고릅|고른|골라|고치|고칩|고친|고쳐|바꾸|바꿉|바꿔|바뀌|넣[어으습지는]|붙여|붙이|붙입|틀린|틀리|알아채|잘하는|못하는|좋아지|나빠지|만들어 내|찾아내|씁니다|쓰십시오|쓰는|쓰면|끄는")
files = ["index.html"] + sorted(glob.glob("chapters/*.html")) + sorted(glob.glob("appendix/*.html")) + sorted(glob.glob("wiki/*.html"))
total = Counter()
for f in files:
    body = open(f, encoding="utf-8").read()
    # 코드 상자 속 프롬프트 예제는 예외(STYLE.md 배제어). 줄 번호를 유지하도록 줄바꿈만 남긴다
    body = re.sub(r"<pre.*?</pre>", lambda m: "\n" * m.group(0).count("\n"), body, flags=re.S)
    for n, line in enumerate(body.split("\n"), 1):
        text = re.sub(r"<svg.*?</svg>|<[^>]+>", " ", line)
        for m in B.finditer(text):
            total[m.group(0)] += 1
            print(f"경고 {f}:{n}: {m.group(0)} | {text[max(0, m.start() - 20):m.end() + 15].strip()}")
if total:
    print("B 배제어 경고 합계:", sum(total.values()), dict(total.most_common()))
