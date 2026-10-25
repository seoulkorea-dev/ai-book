# 작업 안내(Claude Code)

생성형 AI, 묻고 확인하고 활용하기(작동 원리, 프롬프트, 검증, 책임)의 플레이북 기준 정리판 저장소입니다. 원본은 seoulkorea-dev/ai-book이고, 정리 전 상태는 이 저장소의 `original` 브랜치에 그대로 둡니다(비교 기준).

## 먼저 읽을 것(이 순서)
1. NEW_BOOK_PLAYBOOK.md: 원고 원칙과 규칙, 최종 점검표(모든 원고 작업의 기준)
2. BOOK_SPEC.md: 이 책의 선택과 예외
3. HARNESS_SETUP.md: 작업 진행 방식(한 장의 순서, 중단 없이 진행하는 규칙)
4. HANDOFF.md 맨 위 "지금 상태"
5. docs/AUTHOR_QUEUE.md, DECISIONS.md 마지막 10건

- NEW_BOOK_PLAYBOOK.md와 HARNESS_SETUP.md는 seoulkorea-dev/harness-book(커밋 339749d)의 문서를 그대로 옮긴 것입니다. 이 저장소에서 고치지 않고, 이 책에만 해당하는 선택은 BOOK_SPEC.md "예외"에 적습니다.
- 옛 규칙 문서(docs/legacy/CLAUDE-v1.md, docs/legacy/STYLE-v1.md)는 기록으로만 둡니다. 내용이 다르면 플레이북과 설계서를 따릅니다(D-001).

## 이 세션의 역할
- 작성 세션이다. 원고를 고치는 유일한 주체다. main에 직접 commit, push하지 않고 작업 브랜치와 PR로 반영한다.
- 장마다 HARNESS_SETUP.md 3장의 순서로 진행한다(/next, /autopilot).
- 편집 검토는 하위 에이전트 chief-editor가 장마다 1회 한다. 지적은 한 번에 모두 반영하고 다시 검토받지 않는다. 반영하지 못한 필수는 docs/AUTHOR_QUEUE.md의 "작가 검수 목록"에 적는다.
- 점검은 fact-checker(사실), practice-checker(예제가 있을 때), production-checker(그림이 바뀌었을 때)가 한다. 하위 에이전트는 원고를 고치지 않고 보고 문안만 돌려준다.
- 작가만 정할 일(목차, 장의 주장, 핵심 정의, 용어, 그림 방침, 문체 규칙)은 바꾸지 않고 AUTHOR_QUEUE에 질문과 권장안을 적고 진행한다.
- 작가가 확정한 문안은 그대로 둔다. 바꿔야 하면 AUTHOR_QUEUE에 적는다.
- 지시하지 않은 변경은 하지 않는다. 꼭 필요하면 PR 설명에 따로 적는다.

## 원고 규칙
- 원고는 src/만 고친다. 루트의 index.html, chapters/, appendix/는 빌드 결과물이다(python tools/build.py).
- 사실은 원문을 확인한 뒤 쓰고 research/에 출처와 확인 날짜를 남긴다. 인용은 research/bibliography.json의 키로 위첨자를 단다.
- 원고를 넘기기 전에 플레이북 25장 최종 점검표를 확인한다.
- 장 정리를 마치면 그 쪽 이름(index, ch01 등)을 lint/rules_applied.txt에 더한다. 적힌 쪽은 check_all의 위반이 실패, 나머지는 경고다.

## 하위 에이전트 부르기
- 하위 에이전트는 이 대화를 모른다. 부를 때 범위(파일과 절), 기준 문서(플레이북, 설계서, 장 명세), 보고 형식을 넘긴다.
- 보고 문안은 reviews/agents/YYYY-MM-DD-<장>-<에이전트>.md로 저장하고, 처리(반영, 보류, 작가 확인)를 PR 설명에 표로 적는다.
- 의견이 부딪히면 DECISIONS.md와 BOOK_SPEC.md > chief-editor 판정 > 점검 의견 순서로 따른다.

## 끝낼 때
- python tools/check_all.py를 통과시킨다.
- 보고에는 검사 출력 원문을 붙인다.
- HANDOFF.md를 갱신한다. 같은 실패가 두 번째면 FAILURES.md에 적는다.
