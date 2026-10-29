---
name: originality-check
description: 비교 도서와의 겹침 점검(제목, 틀 이름, 주 예제 소재, 문장 유사도). 목차 확정 뒤와 출간 전에 사용.
---
# 독창성
PLAYBOOK 1장의 8(비교 도서)을 따릅니다. 비교 도서와 겹치면 안 되는 것은 BOOK_SPEC의 비교 도서 절에 있습니다.
- 장 제목, 부록 이름, 핵심 틀 이름, 주 예제 소재가 비교 도서와 같은 것이 0개인지 확인합니다.
- 책 저장소 맨 위에서 `python ../book-kit/book/tools/similarity_check.py --ab src --gb <비교 도서 경로>`를 실행합니다(처음 한 번 `pip install scikit-learn`). 끝난 조건: 일치도 0.95 이상인 문장이 고유 표기 외 0건.
- 비교 도서의 문장, 예제, 표를 참고해 다시 쓰지 않습니다.
- 비교 도서에 접속하지 못해 측정하지 못하면 temp/docs/AUTHOR_QUEUE.md에 적습니다.
