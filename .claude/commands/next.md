---
description: 다음 한 단위(작가 요청 이슈 하나)를 HARNESS_SETUP.md 3장 순서로 끝까지 진행한다
---
다음 한 단위를 끝까지 진행한다. 작가에게 묻지 않고 진행하며, 작가만 정할 일은 docs/AUTHOR_QUEUE.md에 권장안과 함께 적는다. GitHub 작업은 쓸 수 있는 도구(gh CLI 또는 GitHub MCP 도구)로 한다.

0. 준비: main으로 이동해 원격 main을 받는다(git switch main, git pull --ff-only origin main). 실패하면 멈추고 이유를 HANDOFF.md "## 지금 상태"에 적는다.
1. 단위 정하기
   - 열린 PR이 있으면 그 PR을 마무리한다(체크 목록에서 체크하지 않은 첫 단계부터).
   - 없으면 라벨 request가 붙은 열린 이슈 가운데 번호가 가장 작은 것 하나.
   - 둘 다 없으면 "열린 요청 없음"이라고 보고하고 끝낸다.
2. 시작(HARNESS_SETUP 3장 1번)
   - 작업 브랜치를 만들고(main에서 commit하지 않음), HANDOFF.md "## 지금 상태" 맨 위에 "진행 중: <단위>, 초안 PR(<브랜치>)"을 적어 commit, push한다.
   - 초안 PR을 연다. 설명에 HARNESS_SETUP 부록 D의 단계 체크 목록을 둔다. 해당하지 않는 단계는 "해당 없음".
   - 요청 이슈에 "작업 시작"(대상, 초안 PR 번호) 댓글.
3. 명세: docs/specs/<장>-spec.md(플레이북 부록 B 서식). 사실 조사가 필요하면 researcher를 부르고 결과를 research/<장>-sources.md와 research/bibliography.json에 반영.
4. 그림: 구조를 새로 정하는 그림은 시안 두 개를 reviews/agents/YYYY-MM-DD-<장>-figures.html에 만들고 편집장 검토 때 선택을 받는다(문구만 고치면 생략하고 이유 기록).
5. 원고: src/만 고친다. 플레이북 3장 장 틀, 5장 용어, 7장 인용, 9~12장 표, 그림, 캡션, 링크를 따른다. 작가가 확정한 문안(BOOK_SPEC와 DECISIONS에 적힌 것)은 바꾸지 않고 AUTHOR_QUEUE에 적는다.
6. 자동 검사: python tools/check_all.py 통과. 정리를 마친 쪽 이름을 lint/rules_applied.txt에 더하고 다시 통과시킨다.
7. 점검: fact-checker, 예제가 있으면 practice-checker를 동시에. 그림이 바뀌었으면 production-checker. 부를 때 범위(파일과 절), 기준 문서, 보고 형식을 넘긴다. 보고는 reviews/agents/YYYY-MM-DD-<장>-<에이전트>.md로 저장하고 지적을 반영, 보류, 작가 확인으로 나눠 처리한다. research 기록 문안은 research/에 덧붙인다.
8. 편집장 검토 1회: chief-editor. 보고를 저장하고 지적을 한 번에 모두 반영한다. 다시 검토받지 않는다. 반영하지 못한 필수는 docs/AUTHOR_QUEUE.md "작가 검수 목록"에.
9. 반영 확인: 플레이북 21장 체크리스트, python tools/check_all.py 통과.
10. 기록: HANDOFF.md "## 지금 상태"의 진행 중 줄을 결과 줄로 바꾼다(한 일, 점검 건수, 편집장 비율, 작가 확인 번호, 다음 단위). 같은 실패가 두 번째면 FAILURES.md. DASHBOARD.md의 그 장 행.
11. PR 설명: 단계 체크 목록, 바뀐 곳, 점검 처리 표, 고칠 문장 비율, 반영하지 못한 필수, 지시 밖 변경, 검사 출력 원문.
12. CI: 마지막 commit에서 CI가 통과했는지 확인(그 commit 뒤에 시작한 검사인지 확인). 실패하면 원인을 고쳐 다시 push. 같은 원인 세 번이면 초안으로 두고 이슈에 "멈춤: 이유".
13. 병합: 초안을 해제하고 병합(merge commit). 이슈에 결과 댓글(PR 주소, 바꾼 절과 표와 그림, 장 밖 변경, 작가 확인 번호)을 남기고 닫는다.
14. 한 줄 보고: 단위, PR 주소, 병합 여부, 작가 확인 추가 수.
