---
name: fact-check
description: 사실 문장의 출처 확인 절차와 인용 표기. 사실을 추가하거나 검토할 때 사용.
---
# 사실 확인(요약, 기준은 NEW_BOOK_PLAYBOOK.md 7장과 BOOK_SPEC.md)
- 사실은 원문 확인 후에만 넣는다. 확인하지 못하면 넣지 않고 AUTHOR_QUEUE에 "출간 전 확인"으로 적는다.
- 1차 출처 우선: 발표 기관 원문, 법령, 판결문, 논문, 공식 문서. 보도는 1차 출처를 찾는 단서로만.
- 인용: 문장 끝 마침표 앞에 `<sup class="cite" data-ref="키"></sup>`, 키는 research/bibliography.json에 둔다. 문서 하나에 키 하나.
- 바뀌는 정보(제품 기능, 요금, 모델 이름, 법률 일정)는 BOOK_SPEC의 기준 일자 기준으로 확인하고, 바뀐 사실은 `<aside class="version-note"><b>버전 주석 (YYYY년 M월)</b> …</aside>`로 덧붙인다.
- 기록: research/<장>-sources.md(발표 주체, 제목, URL, 게시일, 확인일, 사용한 내용).
