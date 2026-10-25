---
name: book-structure
description: 책 구성 단위, 장 틀, 번호, id, 링크, 조사 규칙. 장이나 표, 그림을 추가, 이동, 번호 변경할 때 사용.
---
# 책 구조 규칙(요약, 기준은 NEW_BOOK_PLAYBOOK.md 3장, 11장, 12장과 BOOK_SPEC.md)
- 장 틀과 도입부 형식은 플레이북 3장, 장 틀의 예외는 BOOK_SPEC.md "예외"를 따른다.
- 번호: 본문은 `표 N-n`, `그림 N-n`(N은 파일 chNN의 장 번호). 부록 번호 형식은 BOOK_SPEC.md를 따른다. id는 캡션 번호와 같아야 한다.
- 번호를 바꾸면 id, 본문 참조, 다른 쪽 링크를 함께 바꾸고, 번호 뒤 조사(받침 0, 1, 3, 6, 7, 8 뒤 은, 이, 을, 과)를 다시 확인한다. "Chapter N" 뒤 조사도 같다.
- 링크 문구는 도착 절 제목과 같게(목차와 장 전체 요약 링크만 예외). 같은 쪽의 표, 그림 참조는 링크 없음(빌드가 처리).
- 없어지는 쪽은 src/site.json "redirects"에 이동 쪽으로 등록한다.
- 확인: python tools/check_all.py.
