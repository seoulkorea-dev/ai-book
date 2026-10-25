## 1. 결론(필수 6, 권고 11)

확인 범위와 한계(확인일 2026-10-25):
- 이 환경에서 eur-lex.europa.eu, copyright.gov, orrick.com은 DNS 오류(ENOTFOUND)로 열리지 않았고, curl은 프록시가 CONNECT 403으로 거부했습니다. 법령, 판결문, 기관 원문은 직접 열지 못했습니다. 아래 판정은 WebSearch 결과 요약에 근거하며, 해당 항목마다 "검색 결과 요약"이라고 밝혔습니다. 플레이북 7.1에 따라 원문 미열람 항목은 문장을 바꾸지 않고 참고(미확인)로 두었고, 출간 전에 작가가 원문을 확인할 목록으로 남깁니다.
- 법률 일정은 낡지 않았습니다. 표 8-9와 표 8-10의 날짜는 모두 검색 결과 요약과 일치합니다.
  - Omnibus는 2026-07-08 채택, 2026-07-24 관보 게재, 2026-07-27 발효입니다.
  - 고위험은 부속서 III가 2027-12-02, 부속서 I이 2028-08-02입니다.
  - 제50조는 2026-08-02에 적용됩니다.
  - 제50조 제2항의 기계 판독 표시는 2026-08-02 전에 시장에 나온 생성형 시스템에 한해 2026-12-02까지 유예됩니다.
  - 신설 금지(비동의 성적 이미지, 아동 성착취물)는 2026-12-02부터 적용됩니다.
  - 한국 인공지능기본법은 2026-01-22에 시행됐습니다. 과기정통부는 시행 뒤 1년 이상 계도 기간을 두겠다고 밝혔습니다.
- 불일치 1건은 표시 의무의 주체를 서술한 문장입니다(지적 1, 2).
- 나머지 필수는 날짜와 수치에 위첨자가 없는 경우입니다(지적 3~6).
- 사실 문장은 거의 모두 일치로 보입니다. 지적 17은 Reuters가 쓴 단어를 한글로 옮긴 표현을 정밀하게 맞추는 권고입니다.

## 2. 지적 표

| 번호 | 등급 | 위치 | 문제와 근거 | 원문 | 고친 문안 |
|---|---|---|---|---|---|
| 1 | 필수 | src/chapters/ch08.html, 투명성 > 의무의 주체 | 불일치. EU 인공지능법 제50조의 표시 의무는 둘로 나뉩니다. 제2항은 합성 콘텐츠를 생성하는 시스템의 제공자에게, 제4항은 딥페이크를 만든 시스템을 사용하는 배포자(deployer)에게 있습니다. 두 법 모두 "AI 서비스를 제공하는 사업자"에게만 있다는 문장은 EU에 맞지 않습니다. 근거는 검색 결과 요약(Commission 제50조 지침 해설: 제2항 제공자 기계 판독 표시, 제4항 배포자 딥페이크 고지, 2026-10-25 확인)입니다. 제50조 원문(EUR-Lex)은 열지 못했으므로 작가가 원문으로 확인해야 합니다. 한국은 과기정통부 지침이 "이용자에게 AI 제품·서비스를 직접 제공하는 인공지능사업자"를 주체로 정리했습니다(korea.kr 보도자료 요약, 같은 날 확인). | `두 법의 표시 의무는 AI 서비스를 제공하는 사업자에게 있습니다.` | `한국 인공지능기본법의 표시 의무는 AI 서비스를 제공하는 사업자에게 있고, EU 인공지능법 제50조의 표시 의무는 시스템 제공자와 딥페이크를 업무에 사용하는 배포자에게 있습니다.` |
| 2 | 필수 | src/chapters/ch08.html, 투명성 > 의무의 주체 | 지적 1과 같은 근거입니다. 개인이 의무자에서 빠지는 범위는 EU에서 "개인적, 비전문적 활동" 사용으로 좁습니다. 검색 결과 요약(Commission 지침 해설): 개인 계정 게시는 가능하지만 직업과 연결된 계정은 해당하지 않을 수 있습니다. 한국은 지침이 사업자와 이용자를 나눕니다(검색 결과 요약). 따라서 "개인 사용자"를 일반화한 문장은 조건이 필요합니다. | `따라서 개인 사용자가 법적 의무자가 되지는 않습니다.` | `따라서 업무가 아닌 개인적 사용만 하는 사용자는 두 법의 의무자가 되지 않습니다.` |
| 3 | 필수 | src/chapters/ch08.html, 투명성 > 법률이 정한 AI 생성물 표시 의무 | 출처 없는 수치("1년 이상"). 과기정통부가 시행 뒤 최소 1년 이상 계도 기간을 둔다고 밝힌 내용은 입법예고 단계(2025-11)와 2026-01-21 전후 보도, 지침 보도자료 요약에서 확인됩니다(검색 결과 요약, 2026-10-25). research/legacy-references.html의 ref-msit-2026a(2026-01-20 브리핑) 원문은 열지 못했습니다. 위첨자가 필요합니다. | `시행 뒤 1년 이상 사실조사와 과태료 부과를 유예하는 계도 기간을 두었습니다.` | `시행 뒤 1년 이상 과태료 부과를 유예하고 사실조사는 중대한 사회적 문제가 생긴 예외적인 경우에만 하는 계도 기간을 운영하겠다고 밝혔습니다<sup class="cite" data-ref="msit-ai-act-2026"></sup>.` |
| 4 | 필수 | src/chapters/ch08.html, 권리 > 학습 데이터 소송 | 출처 없는 수치와 날짜(15억 달러, 2025-09, 2026-07-20). 검색 결과 요약으로는 일치합니다. 2026-07-20 최종 승인은 Authors Guild, AAP, Locus, JURIST가 보도했고, 판사는 Alsup 퇴임 뒤 Martínez-Olguín입니다. 예비 승인(2025-09-25)은 BetaNews 단독이라 법원 기록으로 재확인해야 합니다. research/ch08-sources.md에 "주소 미확정"으로 남은 항목입니다. | `이후 15억 달러 규모의 합의가 이루어졌고, 법원은 2025년 9월 예비 승인, 2026년 7월 20일 최종 승인을 했습니다.` | `이후 15억 달러 규모의 합의가 이루어졌고, 법원은 2025년 9월 예비 승인, 2026년 7월 20일 최종 승인을 했습니다<sup class="cite" data-ref="bartz-settlement-2026"></sup>.` |
| 5 | 필수 | src/chapters/ch08.html, 규제 > 표 8-9 도입 | 표 8-9의 날짜 8건에 근거가 없습니다. 검색 결과 요약으로는 모두 일치하고 낡지 않았습니다(2026-10-25). EU 일정은 Regulation (EU) 2024/1689와 2026/1744, 한국은 시행일입니다. 위첨자는 문장 끝에 둡니다. | `표 8-9는 EU 인공지능법과 한국 인공지능기본법의 주요 적용 일정입니다.` | `표 8-9는 EU 인공지능법과 한국 인공지능기본법의 주요 적용 일정입니다<sup class="cite" data-ref="eu-ai-act-2024"></sup><sup class="cite" data-ref="eu-omnibus-2026"></sup><sup class="cite" data-ref="kr-ai-basic-act"></sup>.` |
| 6 | 필수 | src/chapters/ch08.html, 규제 > Digital Omnibus 문단 | 개정 규정 번호와 발효일(2026-07-27)에 위첨자가 없습니다. 검색 결과 요약(EUR-Lex 검색 기록 요약, Cuatrecasas, Garrigues 등): 2026-07-08 채택, 2026-07-24 관보 게재, 제4조에 따라 3일 뒤인 2026-07-27 발효로 일치합니다. 고위험 연기와 신설 금지도 요약상 일치합니다. | `EU 인공지능법은 Regulation (EU) 2026/1744(Digital Omnibus on AI) 개정으로 2026년 7월 27일부터 일부 내용이 변경되었습니다.` | `EU 인공지능법은 Regulation (EU) 2026/1744(Digital Omnibus on AI) 개정으로 2026년 7월 27일부터 일부 내용이 변경되었습니다<sup class="cite" data-ref="eu-omnibus-2026"></sup>.` |
| 7 | 권고 | src/chapters/ch08.html, 투명성 > 의무의 주체 | 발표 주체는 문장에 있으나 위첨자가 없습니다. 의무 주체 서술은 검색 결과 요약(korea.kr 보도자료, 2026-01)과 일치합니다. | `투명성 의무의 주체를 이용자에게 AI 제품이나 서비스를 직접 제공하는 사업자로 정리했습니다.` | `투명성 의무의 주체를 이용자에게 AI 제품이나 서비스를 직접 제공하는 사업자로 정리했습니다<sup class="cite" data-ref="msit-guideline-2026"></sup>.` |
| 8 | 권고 | src/chapters/ch08.html, 투명성 > 법률이 정한 AI 생성물 표시 의무(EU) | 기계 판독 표시 의무의 주체(제공자)가 문장에 없습니다. 근거는 지적 1과 같은 검색 결과 요약(제50조 제2항)입니다. | `인공지능법 제50조는 AI가 생성한 합성 콘텐츠를 기계가 읽을 수 있는 방식으로 표시하도록 규정합니다.` | `인공지능법 제50조는 합성 콘텐츠를 생성하는 AI 시스템의 제공자가 결과물을 기계가 읽을 수 있는 방식으로 표시하도록 규정합니다.` |
| 9 | 권고 | src/chapters/ch08.html, 투명성 > 법률이 정한 AI 생성물 표시 의무(EU) | 적용일(2026-08-02)과 유예(2026-12-02)는 검색 결과 요약상 일치합니다(유예는 2026-08-02 전에 시장에 나온 생성형 시스템의 제공자에 한정되고, 제50조 제4항 배포자 의무는 연장되지 않음). 인용이 없습니다. | `그 전에 시장에 나온 시스템의 기계 판독 표시 의무는 2026년 12월 2일까지 유예됩니다.` | `그 전에 시장에 나온 시스템의 기계 판독 표시 의무는 2026년 12월 2일까지 유예됩니다<sup class="cite" data-ref="eu-omnibus-2026"></sup>.` |
| 10 | 권고 | src/chapters/ch08.html, 투명성 > 법률이 정한 AI 생성물 표시 의무(한국) | 법률 내용(제31조 투명성 확보 의무)은 검색 결과 요약과 일치하나 인용이 없습니다. 법령 원문(국가법령정보센터)은 열지 못했습니다. | `인공지능기본법은 생성형 AI 결과물임을 표시하고, 실제와 구분하기 어려운 결과물은 이용자가 명확히 인식하도록 고지하는 의무를 규정합니다.` | `인공지능기본법은 생성형 AI 결과물임을 표시하고, 실제와 구분하기 어려운 결과물은 이용자가 명확히 인식하도록 고지하는 의무를 규정합니다<sup class="cite" data-ref="kr-ai-basic-act"></sup>.` |
| 11 | 권고 | src/chapters/ch08.html, 권리 > 학습 데이터 소송(Getty) | 2025-11-04 판결의 기각, 가중치는 침해 복제물이 아님, 상표 침해 일부 인정은 검색 결과 요약(Ropes & Gray, Bird & Bird, Cleary, Dentons)과 일치합니다. 판결문(사건번호 [2025] EWHC 2863 (Ch)) 원문은 열지 못했고 인용이 없습니다. | `영국 고등법원은 2025년 11월 4일 Getty 사건 판결에서 2차 저작권 침해 주장을 기각했습니다.` | `영국 고등법원은 2025년 11월 4일 Getty 사건 판결에서 2차 저작권 침해 주장을 기각했습니다<sup class="cite" data-ref="getty-v-stability-2025"></sup>.` |
| 12 | 권고 | src/chapters/ch08.html, 권리 > 학습 데이터 소송(Bartz) | 2025-06 공정 이용 판단(구매한 책으로 학습은 공정 이용, 불법 복제본 보관은 아님)은 기록과 검색 결과에서 모순이 없습니다. 판단 문서 인용이 없습니다. | `불법 복제본을 모아 보관한 부분은 공정 이용으로 보지 않았습니다.` | `불법 복제본을 모아 보관한 부분은 공정 이용으로 보지 않았습니다<sup class="cite" data-ref="bartz-fair-use-2025"></sup>.` |
| 13 | 권고 | src/chapters/ch08.html, 권리 > 학습 데이터 소송(표 8-2 도입) | 표 8-2의 제기 시점과 쟁점에 근거가 없습니다. NYT 2023-12(S.D.N.Y. 1:23-cv-11195)와 Bartz 2024-08은 소장으로 확인할 사항입니다. Getty 미국 2023-02는 미확인입니다(참고 3). | `표 8-2는 소송 사례 가운데 일부입니다.` | `표 8-2는 소송 사례 가운데 일부입니다<sup class="cite" data-ref="getty-v-stability-2025"></sup><sup class="cite" data-ref="nyt-v-openai-2023"></sup><sup class="cite" data-ref="bartz-fair-use-2025"></sup>.` |
| 14 | 권고 | src/chapters/ch08.html, 권리 > AI 결과물의 저작권 | 저작권법 제2조 제1호 정의는 널리 알려진 조문과 같습니다. 이번 세션에서 법령 원문은 열지 못했고 인용이 없습니다. | `저작권법 제2조 제1호는 저작물을 인간의 사상 또는 감정을 표현한 창작물로 정의합니다.` | `저작권법 제2조 제1호는 저작물을 인간의 사상 또는 감정을 표현한 창작물로 정의합니다<sup class="cite" data-ref="kr-copyright-act"></sup>.` |
| 15 | 권고 | src/chapters/ch08.html, 규제 > 위험 등급(표 8-10 도입) | 위험 등급 서술에 인용이 없습니다. 고위험 사례(채용, 신용, 교육)와 투명성 의무 사례는 검색 결과 요약과 모순이 없습니다. | `EU 인공지능법은 AI 시스템을 위험 수준에 따라 네 등급으로 나누고, 등급마다 다른 의무를 부과합니다.` | `EU 인공지능법은 AI 시스템을 위험 수준에 따라 네 등급으로 나누고, 등급마다 다른 의무를 부과합니다<sup class="cite" data-ref="eu-ai-act-2024"></sup>.` |
| 16 | 권고 | src/chapters/ch08.html, 규제 > 표 8-11 도입 | 표 8-11의 "Agentic AI Foundation, 2025년 12월 출범"은 일치합니다. 출처는 Anthropic 발표(2025-12-09)와 MCP 프로젝트 블로그이고, Linux Foundation 직접 발표는 열리지 않았습니다. 같은 표의 OWASP 2025와 Omnibus 행도 이 문장에서 함께 인용합니다. | `표 8-11은 법률, 보안 표준, 규격 관리 기구의 주요 변화와 시점입니다.` | `표 8-11은 법률, 보안 표준, 규격 관리 기구의 주요 변화와 시점입니다<sup class="cite" data-ref="eu-omnibus-2026"></sup><sup class="cite" data-ref="owasp-llm-2025"></sup><sup class="cite" data-ref="anthropic-aaif-2025"></sup>.` |
| 17 | 권고 | src/chapters/ch08.html, 편향 | Reuters 기사는 "women's"(예: women's chess club captain)라는 단어가 포함된 이력서에 감점했다고 쓴 것으로 검색 결과 요약(CNBC, HR Reporter 재배포본)에서 확인됩니다. "여성"이라는 단어로 옮기면 범위가 더 넓게 읽힙니다. 학습 데이터(10년, 대부분 남성)와 팀 해체는 일치합니다. | `'여성'이라는 단어가 포함된 이력서` | `'women's'(여성의)라는 단어가 포함된 이력서` |

참고(미확인과 확인 중 남은 점, 문장은 바꾸지 않음):
1. 표 8-9 2025-02-02 행의 `금지 관행, AI 리터러시 조항 적용`: 적용 사실 자체는 맞습니다. 다만 검색 결과 요약상 Omnibus가 제4조를 완화했습니다(제공자와 배포자가 AI 리터러시 "조치를 취하는" 의무로 바뀌고, 위원회와 회원국의 지원 의무가 추가됨). 개정 조문 원문은 열지 못해 미확인입니다. 작가가 EUR-Lex로 확인한 뒤 "2025년 2월 시점 적용 사항" 취지로 둘지 정해야 합니다. 찾은 범위는 ISMS Lite, trail-ml, ActuIA 요약입니다.
2. 신설 금지 조항(제5조, 비동의 성적 이미지와 아동 성착취물 생성, 2026-12-02): 다수 검색 결과(Cooley, CSA, complexdiscovery)가 일치합니다. 일부 요약은 "기존 의무를 바꾼 것은 날짜 이동뿐"이라고 해 결과가 갈립니다. 효과적인 기술적 안전장치가 있으면 적용되지 않는 예외가 있다는 요약이 있고, 호수 번호는 (1)(ba), (bb)로 보도되었으나 미검증입니다. 원고의 "금지(제5조 신설)" 표현은 요약상 맞습니다. EUR-Lex 원문 확인 전까지 조건(예외)은 원고에 쓰이지 않았습니다.
3. Getty 사건: (a) 원고의 철회 이유 `학습이 영국 밖에서 이루어졌다는 이유로 Getty가 재판 중에 철회했습니다.`는 검색 결과 요약에서 "영국에서 학습이 이루어졌다는 증거가 없어 철회"로 표현됩니다. 판결문 문단으로 표현을 맞추는 것이 안전합니다. (b) 2025-12-17에 항소 허가가 났다는 요약이 있어(2차 침해 부분), 원고의 "항소가 이어질 수 있으므로"는 현재 상태와 맞는지 법원 기록으로 확인해야 합니다. (c) 표 8-2의 "2023년 1월 영국, 2023년 2월 미국" 제기 시점은 소장을 찾지 못해 미확인입니다.
4. Bartz 합의 범위: `합의는 과거의 불법 복제본 취득과 복제에 대한 청구만 해결합니다.`는 법률사무소 요약(Kilpatrick Townsend)이 "2025-08-25까지의 행위에 대한 청구"를 해결한다고 하나, 합의서의 면책(release) 문구는 찾지 못했습니다. 미확인입니다. 또한 최종 승인 뒤 항소(수수료 부분 등)가 제기됐다는 요약이 있고 출처가 엇갈립니다. 미확인입니다.
5. 한국 계도 기간: 요약 자료마다 종료 시점이 다르게 적혀 있어(2026-12, 2027 초 등) 원고의 "1년 이상"만 확인했습니다. 시행령 시행일이 2026-08-20이라는 요약도 있으나 미확인입니다. 시행 후 사실조사와 과태료 부과 건수 보도는 원고와 무관합니다.
6. 미국 저작권청 Zarya(2023-02-21)와 등록 안내(2023-03-16, Federal Register): 날짜, 텍스트와 이미지 배치 보호, Midjourney 이미지 제외, AI 생성 부분 명시 의무는 검색 결과 요약(Ropes & Gray, Skadden, Volokh)과 일치합니다. copyright.gov 원문은 열지 못했습니다. 기존 위첨자는 그대로 둡니다.
7. IEA(2025-04-10) 415TWh(2024)와 945TWh(2030): IEA 보고서 요약 페이지 검색 결과와 일치합니다. 원문 직접 열람은 못했습니다.
8. Lee 외 2025(CHI 2025, 319명, AI 신뢰가 높을수록 비판적 사고 감소, 자기 신뢰가 높을수록 증가): 논문 요약 검색 결과와 일치합니다. 소속은 Lee가 카네기멜런대, Sarkar 등이 Microsoft Research입니다.
9. OWASP 2025(LLM01 프롬프트 인젝션, LLM06 과도한 권한): 벤더 해설서 검색 결과로만 확인했습니다. OWASP 원문은 열지 못했습니다. 기존 위첨자는 그대로 둡니다.
10. Anthropic Building effective agents(2024-12, 워크플로와 에이전트 구분, 가장 단순한 방식부터 시작): 이번 세션에서 재확인하지 못했습니다. research/legacy-references.html의 기록과 기존 위첨자만 있습니다.
11. 표 8-10의 네 등급은 위원회 설명 방식이며, 범용 AI 모델은 별도 체계입니다. 원고에서 문제가 되지는 않지만 등급 수를 법 조문으로 단정하는 문장은 아닙니다.

## 3. research 기록 문안(research/ch08-sources.md에 덧붙임)

```
## 2026-10-25 fact-checker 재확인(Chapter 8)

확인 한계: eur-lex.europa.eu, copyright.gov, orrick.com 등은 DNS 오류, 프록시 403으로 직접 열지 못함. 아래 "검색 결과 요약"은 WebSearch가 돌려준 요약으로, 원문 대조가 필요한 항목은 작가 확인 목록.

- 유럽연합(European Parliament, Council), Regulation (EU) 2026/1744 (Digital Omnibus on AI), https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng, 2026-07-08 채택, 2026-07-24 관보 게재, 2026-07-27 발효, 확인 2026-10-25(검색 결과 요약). 사용: 고위험 2027-12-02(부속서 III), 2028-08-02(부속서 I), 제50조 제2항 기계 판독 표시 유예 2026-12-02, 제5조 신설 금지(2026-12-02).
- 유럽연합, Regulation (EU) 2024/1689 (AI Act), https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng, 2024-07-12 관보 게재, 확인 2026-10-25(검색 결과 요약). 사용: 발효 2024-08-01, 금지 관행과 AI 리터러시 2025-02-02, 범용 AI 모델 2025-08-02, 제50조 2026-08-02.
- 과학기술정보통신부, 인공지능 투명성 확보 안내 지침(가이드라인) 공개 보도자료, https://www.korea.kr/briefing/pressReleaseView.do?newsId=156740669, 2026-01, 확인 2026-10-25(검색 결과 요약). 사용: 투명성 의무 주체는 이용자에게 AI 제품, 서비스를 직접 제공하는 인공지능사업자, 1년 이상 계도 기간.
- 인공지능기본법 제31조(국가법령정보센터), 시행 2026-01-22, 확인 2026-10-25(검색 결과 요약).
- High Court of Justice (England and Wales), Getty Images (US) Inc & Ors v Stability AI Ltd [2025] EWHC 2863 (Ch), 2025-11-04, 확인 2026-10-25(검색 결과 요약: Ropes & Gray, Bird & Bird, Cleary, Dentons). 사용: 2차 침해 기각, 가중치는 침해 복제물이 아님, 상표 침해 일부 인정, 1차 침해 철회, 2025-12-17 항소 허가(요약).
- Bartz v. Anthropic PBC, No. 3:24-cv-05417 (N.D. Cal.), 확인 2026-10-25(검색 결과 요약: Authors Guild, AAP, Locus, JURIST, BetaNews). 사용: 2026-07-20 최종 승인(Martínez-Olguín 판사), 예비 승인 2025-09-25(BetaNews 단독), 2025-08-25까지 행위 청구 해결(Kilpatrick Townsend). 법원 기록 주소 미확정.
- Reuters(Dastin, J.), Amazon scraps secret AI recruiting tool that showed bias against women, 2018-10-10, 확인 2026-10-25(CNBC, HR Reporter 재배포본의 검색 결과 요약). 사용: "women's" 단어 감점, 10년치 이력서, 팀 해체.
- IEA, Energy and AI, 2025-04-10, https://www.iea.org/reports/energy-and-ai/executive-summary, 확인 2026-10-25(검색 결과 요약). 사용: 2024년 약 415TWh, 2030년 약 945TWh.
- Lee, H.-P. 외, The Impact of Generative AI on Critical Thinking, CHI 2025, DOI 10.1145/3706598.3713778, 확인 2026-10-25(검색 결과 요약). 사용: 319명, 신뢰와 비판적 사고의 관계.
- Anthropic, Donating the Model Context Protocol and establishing the Agentic AI Foundation, 2025-12-09, https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation, 확인 2026-10-25(검색 결과 요약). 사용: AAIF 출범 2025년 12월.
- OWASP Top 10 for LLM Applications 2025: LLM01, LLM06 (벤더 해설서 검색 결과로만 확인, 원문 미열람).
- U.S. Copyright Office Zarya 서신(2023-02-21), Registration Guidance(2023-03-16): 언론, 법률사무소 요약으로 확인, 원문 미열람.
- 미확인: 표 8-9의 AI 리터러시 조항 현행 문구, 신설 금지 조항의 예외 조건과 항 번호, Bartz 합의 면책 범위, 최종 승인 뒤 항소 상태, Getty 항소 진행 상태, Getty 미국 소송 제기 시점, 한국 계도 기간 종료 시점, Anthropic Building effective agents 재확인.
```

새 bibliography.json 항목 문안(url이 빈 항목은 작성 세션이 법원 기록 주소를 확인한 뒤 기입. 이 상태로는 빌드가 거부할 수 있음):

```
"eu-ai-act-2024": {"type": "web", "author": "European Parliament, Council of the European Union", "title": "Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act)", "venue": "EUR-Lex (Official Journal, 2024-07-12)", "url": "https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng", "date": "2024-07-12"},
"eu-omnibus-2026": {"type": "web", "author": "European Parliament, Council of the European Union", "title": "Regulation (EU) 2026/1744 (Digital Omnibus on AI), amending Regulations (EU) 2024/1689, 2018/1139 and 2023/1230", "venue": "EUR-Lex (Official Journal, 2026-07-24)", "url": "https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng", "date": "2026-07-24"},
"kr-ai-basic-act": {"type": "web", "author": "대한민국", "title": "인공지능 발전과 신뢰 기반 조성 등에 관한 기본법", "venue": "국가법령정보센터 (2026-01-22 시행)", "url": "https://www.law.go.kr/법령/인공지능발전과신뢰기반조성등에관한기본법", "date": "2026-01-22"},
"kr-copyright-act": {"type": "web", "author": "대한민국", "title": "저작권법", "venue": "국가법령정보센터", "url": "https://www.law.go.kr/법령/저작권법"},
"msit-guideline-2026": {"type": "web", "author": "과학기술정보통신부", "title": "인공지능 투명성 확보 안내 지침(가이드라인) 공개", "venue": "정책브리핑 보도자료", "url": "https://www.korea.kr/briefing/pressReleaseView.do?newsId=156740669", "date": "2026-01"},
"getty-v-stability-2025": {"type": "web", "author": "High Court of Justice (England and Wales)", "title": "Getty Images (US) Inc & Ors v Stability AI Ltd [2025] EWHC 2863 (Ch)", "venue": "판결 2025-11-04", "url": "https://caselaw.nationalarchives.gov.uk/ewhc/ch/2025/2863", "date": "2025-11-04"},
"nyt-v-openai-2023": {"type": "web", "author": "The New York Times Company", "title": "The New York Times Co. v. Microsoft Corp. and OpenAI, No. 1:23-cv-11195 (S.D.N.Y.) 소장", "venue": "S.D.N.Y. (2023-12-27)", "url": "", "date": "2023-12-27"},
"bartz-fair-use-2025": {"type": "web", "author": "U.S. District Court, N.D. Cal.", "title": "Bartz v. Anthropic PBC, No. 3:24-cv-05417, 공정 이용 판단 명령", "venue": "N.D. Cal. (2025-06)", "url": "", "date": "2025-06"},
"bartz-settlement-2026": {"type": "web", "author": "U.S. District Court, N.D. Cal.", "title": "Bartz v. Anthropic PBC, No. 3:24-cv-05417, 합의 최종 승인", "venue": "N.D. Cal. (2026-07-20)", "url": "", "date": "2026-07-20"},
"anthropic-aaif-2025": {"type": "web", "author": "Anthropic", "title": "Donating the Model Context Protocol and establishing the Agentic AI Foundation", "venue": "Anthropic (2025-12-09)", "url": "https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation", "date": "2025-12-09"}
```

필수 6, 권고 11, 참고 11, 확인한 사실 문장 58개
