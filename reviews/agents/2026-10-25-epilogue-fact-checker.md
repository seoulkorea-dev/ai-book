## 1. 결론(필수 1, 권고 1)

범위: src/chapters/epilogue.html 전체.

- 한국 인공지능기본법: "2026년 1월 시행"은 맞습니다. research/ch08-sources.md에 시행일 2026-01-22로 기록되어 있고, bibliography.json의 kr-ai-basic-act(venue에 2026-01-22 시행), msit-ai-act-2026(제목 '인공지능기본법' 22일 시행)과도 같습니다. 다만 이 문장에는 인용이 없습니다(권고).
- EU 투명성 의무: "2026년 8월부터"는 제50조 전체에 대해서는 부정확합니다. 같은 research 기록에 따르면 Regulation (EU) 2026/1744(Digital Omnibus on AI, 2026-07-27 발효)가 제50조 제2항의 기계 판독 표시를 2026-12-02까지 유예했습니다. 이 문장은 원 규정(eu-ai-act-2024)만 인용하고 개정 규정(eu-omnibus-2026)은 인용하지 않습니다(필수, 낡음).
- 에이전트 설명: 일치합니다. epilogue는 "목표를 받아 도구 호출과 결과 확인을 반복하며 작업을 수행하는 에이전트"라고 씁니다. ch03.html 65행과 ch08.html 4행, 155행의 정의는 "목표를 받아 도구 호출, 결과 확인, 다음 행동 결정을 반복하는 AI 시스템"입니다. 반복 구조와 사람 확인 없이 실행되는 범위라는 취지가 같고, 링크 앵커도 ch08.html#agents로 알맞습니다.
- 장별 원칙 문장: 8개 모두 해당 장의 p.principle과 글자까지 같습니다. ch01~ch08.html의 `<p class="principle">` 본문과 epilogue 목록의 문장을 대조했습니다.
- 링크 앵커: 모두 있습니다. #principle은 ch01~ch08의 h2에 있습니다. ch02#elements, ch04#checklist, ch04#record, ch06#data, ch07#self-assessment, ch08#policy, ch08#agents, ch08#tbl-8-10(표 8-10 주요 AI 법률 적용 일정)이 모두 있습니다.

## 2. 지적 표

| 번호 | 등급 | 위치 | 문제와 근거 | 원문 | 고친 문안 |
|---|---|---|---|---|---|
| 1 | 필수 | src/chapters/epilogue.html, "앞으로의 변화" | 낡음. 원 규정 제50조는 2026-08-02 적용이 맞지만, 개정 규정 Regulation (EU) 2026/1744가 제50조 제2항의 기계 판독 표시를 2026-12-02로 유예했습니다. 근거는 research/ch08-sources.md "2026-10-25 fact-checker 재확인(Chapter 8)"의 EU 두 항목이고, 확인일은 2026-10-25입니다. 개정 규정은 인용되어 있지 않습니다. 개정 규정 원문은 직접 열지 못했습니다(아래 참고). | `EU 인공지능법은 2026년 8월부터 투명성 의무를 적용합니다<sup class="cite" data-ref="eu-ai-act-2024"></sup>` | `EU 인공지능법은 2026년 8월 2일부터 투명성 의무(제50조)를 적용하되, 기계 판독 표시 의무(제50조 제2항)는 2026/1744 개정 규정으로 2026년 12월 2일까지 유예되었습니다<sup class="cite" data-ref="eu-ai-act-2024"></sup><sup class="cite" data-ref="eu-omnibus-2026"></sup>` |
| 2 | 권고 | src/chapters/epilogue.html, "앞으로의 변화" | 인용 누락. 한국 법 시행일 문장에 위첨자가 없습니다. kr-ai-basic-act(국가법령정보센터, 2026-01-22 시행)가 bibliography.json에 이미 있습니다. 시행일을 2026-01-22로 구체화하면 표 8-10과도 맞습니다. | `한국 인공지능기본법은 2026년 1월 시행되었고,` | `한국 인공지능기본법은 2026년 1월 22일 시행되었고<sup class="cite" data-ref="kr-ai-basic-act"></sup>,` |

참고(미확인)
- Regulation (EU) 2026/1744와 2024/1689 원문은 이 환경에서 직접 열지 못했습니다. 판정은 research/ch08-sources.md에 이미 있는 2026-10-25 기록(WebSearch 요약)에 기댄 것입니다. 지적 1의 "제50조 제2항만 유예"라는 범위는 원문 대조가 필요합니다. 제50조의 다른 항도 개정되었는지는 확인하지 못했습니다.
- ch08.html의 표 8-10은 "2026년 8월 2일 투명성 의무(제50조) 적용"만 적고 제2항 유예는 적지 않았습니다. 이 점검 범위 밖이어서 판정하지 않았고, 8장 쪽에서 확인하도록 기록합니다.

## 3. research 기록 문안

```
## 2026-10-25 fact-checker 재확인(마치며)

확인 한계: 이미 기록된 Chapter 8 출처를 근거로 삼았고 원문 주소는 다시 열지 못함(eur-lex 접근 불가, 검색 요약 기반).

- 유럽연합(European Parliament, Council), Regulation (EU) 2026/1744 (Digital Omnibus on AI), https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng, 2026-07-24 관보 게재, 2026-07-27 발효, 확인 2026-10-25(research/ch08-sources.md 기록 대조). 사용: 제50조 제2항 기계 판독 표시 유예 2026-12-02.
- 유럽연합, Regulation (EU) 2024/1689 (AI Act), https://eur-lex.europa.eu/eli/reg/2024/1689/oj, 2024-07-12 관보 게재, 확인 2026-10-25(기록 대조). 사용: 제50조 투명성 의무 2026-08-02 적용.
- 대한민국, 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법, 국가법령정보센터, 시행 2026-01-22, 확인 2026-10-25(기록 대조). 사용: 시행일.
- 내부 대조(2026-10-25): epilogue의 장별 원칙 8문장은 ch01~ch08 p.principle과 일치. 앵커 9종(principle, elements, checklist, data, policy, self-assessment, record, agents, tbl-8-10) 존재. 에이전트 정의는 ch03:65, ch08:4와 일치.
- 미확인: 제50조 제2항 외 조항의 Omnibus 개정 여부, 한국 과태료 유예 종료 시점.

새 인용 키: 없음(kr-ai-basic-act, eu-omnibus-2026은 bibliography.json에 이미 있음).
```

필수 1, 권고 1, 참고 2, 확인한 사실 문장 12개
