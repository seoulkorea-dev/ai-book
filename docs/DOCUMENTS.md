# 문서 현황(genai-book)

저장소의 문서와 설정을 역할과 기준 여부로 정리한 목록입니다(2026-10-25, 1단계 체계 PR 기준). 원고와 빌드 결과물(src/, chapters/, appendix/, index.html, assets/)은 목록에서 뺐습니다.

상태 구분
- **기준**: 지금 작업의 기준이 되는 문서. 내용이 부딪히면 이 문서를 따릅니다.
- **기록**: 작업 결과와 결정을 남기는 문서.
- **보조**: 기준 문서를 쓰기 위한 도구, 서식, 설정.
- **옛 문서**: 원본 ai-book 시절의 문서. 기록으로만 두고, 다르면 플레이북과 설계서를 따릅니다(D-001, D-002).

## 1. 기준 문서(읽는 순서)

| 순서 | 문서 | 역할 | 상태 |
|---|---|---|---|
| 1 | NEW_BOOK_PLAYBOOK.md | 원고 원칙과 규칙, 최종 점검표(25장). harness-book 339749d에서 그대로 옮김, 이 저장소에서 고치지 않음 | 기준 |
| 2 | BOOK_SPEC.md | 이 책의 선택(목차, 용어표, 예제, 그림, 비교 도서)과 플레이북 예외 | 기준(초안, 작가 확인 대기) |
| 3 | HARNESS_SETUP.md | 작업 진행 방식. harness-book 339749d에서 그대로 옮김 | 기준 |
| 4 | CLAUDE.md | 작성 세션 안내(읽을 순서, 역할, 끝낼 때) | 기준 |
| 5 | DECISIONS.md | 작가 결정(D-001~D-004: 전면 정리, 플레이북 기준 통일, 기준 일자 10월, 진행 방식) | 기준, 기록 |

## 2. 기록 문서

| 문서 | 역할 | 상태 |
|---|---|---|
| HANDOFF.md | 인계 메모. 맨 위 "지금 상태" | 기록(새로 만듦) |
| docs/AUTHOR_QUEUE.md | 작가 확인 목록(원본 규칙 가운데 플레이북과 다른 것 포함), 작가 검수 목록 | 기록(새로 만듦) |
| DASHBOARD.md | 쪽별 진행 표 | 기록(새로 만듦) |
| FAILURES.md | 두 번째 나온 실패와 추가한 장치 | 기록(새로 만듦, 비어 있음) |
| research/bibliography.json | 인용 키(위첨자 인용과 참고 문헌 생성) | 기록(비어 있음, 장마다 채움) |
| docs/specs/ | 장 명세, 그림 명세 | 기록(장마다 만듦) |
| reviews/agents/ | 하위 에이전트 보고 | 기록(장마다 만듦) |
| reviews/(64개, 2026-10-01~10-04) | 원본 ai-book의 검수 기록(01차~, 누적 차수) | 옛 문서(기록) |
| README.md | 책 소개, 구성, 만든 과정 | 옛 문서(원본 내용 그대로, 정리 뒤 갱신 필요) |

## 3. 작업 도구와 설정

### 3.1 에이전트(.claude/agents/), 명령(.claude/commands/), 스킬(.claude/skills/)

| 이름 | 역할 | 상태 |
|---|---|---|
| chief-editor | 편집장. 장마다 1회 통독 판정 | 기준 |
| fact-checker | 사실 점검(제품, 요금, 법령, 연구, 사례) | 기준 |
| practice-checker | 예제 점검(프롬프트 예제와 결과 예시) | 기준 |
| production-checker | 제작 점검(그림 규격, 화면, 표, 링크) | 기준 |
| researcher | 1차 출처 조사 | 기준 |
| /next, /autopilot, /handoff | 한 단위 진행, 반복 진행, 인계 메모 갱신 | 기준 |
| 스킬 book-structure, fact-check, ko-book-style, originality-check | 플레이북과 설계서 요약(기준은 플레이북) | 보조 |
| .claude/settings.json | 권한(일상 작업 허용, main push와 강제 push 금지), 훅 | 보조 |

### 3.2 도구(tools/, lint/, .github/)

| 파일 | 역할 | 상태 |
|---|---|---|
| tools/build.py | src/로 쪽 파일 빌드, 위첨자 인용과 참고 문헌 생성 | 기준(harness-book 판, 제목만 이 책으로) |
| tools/check_all.py | 전체 검사 7항목. lint/rules_applied.txt에 적힌 쪽은 실패, 정비 전 쪽은 경고 | 기준 |
| lint/(check_numbers, check_structure, check_style, check_rules, banned.txt, rules_applied.txt) | check_all이 부르는 검사 | 기준 |
| tools/hooks/(session_start, pre_bash, stop_check), tools/hook_lint.py | 훅. hook_lint는 고친 쪽의 문제만 알림 | 기준 |
| tools/similarity_check.py | 비교 도서(zakedu/genai-book) 유사도 | 보조 |
| .github/workflows/check.yml, verify-site.yml, tools/verify_site.py | PR마다 check_all, 배포 확인 | 기준 |

## 4. 옛 문서(원본 ai-book)

| 문서 | 내용 | 대체한 곳 |
|---|---|---|
| docs/legacy/CLAUDE-v1.md | 원본 작업 안내와 작가 결정(재구성 계획, 규칙 요약, 문장 원칙) | CLAUDE.md, BOOK_SPEC.md, DECISIONS.md(플레이북과 다른 결정은 AUTHOR_QUEUE) |
| docs/legacy/STYLE-v1.md | 원본 문체 규칙 | 플레이북 6장, BOOK_SPEC.md 표기 절 |
| wiki/(14개) | 옛 위키 쪽. 모두 이동 쪽(meta refresh로 index.html) | 원본에서 이미 본문으로 합침(23차) |
| original 브랜치 | 정리 전 원본 전체(seoulkorea-dev/ai-book 0fcb8f2) | 정리 전후 비교 기준 |
