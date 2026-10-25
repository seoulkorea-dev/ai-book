# Chapter 4 사실 점검(fact-checker, 2026-10-25)

## 1. 결론(필수 0, 권고 10)

범위 src/chapters/ch04.html 전체, 기준 일자 2026년 10월.
- 불일치와 낡음 없음. Avianca 날짜, 제재금 액수, 제재 대상 일치. Bard 사례(JWST 답변 오류, 2004년 VLT, Alphabet 주가 하락) 일치. 예제 날짜 2026-11-05, 11-12 모두 목요일(`date -d`).
- 접속 제한: arxiv.org, doi.org, eso.org, courtlistener.com, law.justia.com getaddrinfo 오류. 판정은 모두 검색 결과 요약 근거(Westlaw 사본 헤드노트, 로이터 재배포본, NASA와 ESO 이미지 쪽, arXiv와 SAGE 서지).
- 권고 10: Avianca와 Bard 인용 누락(5건, 새 키 3개), Lewis 인용 범위, Parasuraman 제목 부제, Kalai 외 소속, Ji 외 "제시" 표현, Bard 마지막 문장의 인과 단정.

## 2. 지적 표

| 번호 | 등급 | 위치(src/chapters/ch04.html) | 문제와 근거(확인일 2026-10-25) | 원문 | 고친 문안 |
|---|---|---|---|---|---|
| 1 | 권고 | src/chapters/ch04.html, 절 types, 첫 문단 | ji-2023 서지 일치(ACM Computing Surveys 55, 2023). 이 논문이 구분을 "제시했다"는 근거 미확인, 두 유형으로 정리했다는 점만 확인 | `환각 연구를 정리하며 이 구분을 제시했습니다<sup class="cite" data-ref="ji-2023"></sup>` | `환각을 내재적 환각과 외재적 환각으로 나눠 정리했습니다<sup class="cite" data-ref="ji-2023"></sup>` |
| 2 | 권고 | 절 causes, 마지막 문단 | arXiv:2509.04664 저자 4명 중 3명 OpenAI, Vempala는 Georgia Tech | `OpenAI 연구진(Kalai 외)은 2025년 9월 논문` | `OpenAI와 Georgia Tech 소속 연구진(Kalai 외)은 2025년 9월 논문` |
| 3 | 권고 | 절 measures, 검색 증강 생성 문단 | Lewis 외는 생성 모델과 위키백과 검색 색인 결합을 발표. "조직 내부 문서"는 논문 내용이 아님. 문장을 나누고 위첨자를 발표 문장에 | `Lewis 외가 2020년에 발표했으며, 학습하지 않은 최신 정보나 조직 내부 문서를 다룰 때 사용합니다<sup class="cite" data-ref="lewis-2020"></sup>.` | `Lewis 외가 2020년에 발표했습니다<sup class="cite" data-ref="lewis-2020"></sup>. 학습하지 않은 최신 정보나 조직 내부 문서를 다룰 때 사용합니다.` |
| 4 | 권고 | 절 automation-bias | 정식 제목은 부제 포함(Human Factors 52(3), 381–410, DOI 10.1177/0018720810376055) | `「Complacency and Bias in Human Use of Automation」에서` | `「Complacency and Bias in Human Use of Automation: An Attentional Integration」에서` |
| 5 | 권고 | 절 automation-bias, Avianca 문단 | 인용 누락. 678 F. Supp. 3d 443 헤드노트로 5,000달러 제재, 법률 사무소 연대 책임 확인. 새 키 mata-2023 | `공동으로 5,000달러의 제재금을 부과했습니다` | `공동으로 5,000달러의 제재금을 부과했습니다<sup class="cite" data-ref="mata-2023"></sup>` |
| 6 | 권고 | 같은 문단 | 인용 누락. ChatGPT 질의와 답 대목은 이번 검색에서 확인 못 함. 원문 확인 뒤 위첨자 | `변호사는 ChatGPT에 판례가 실제로 있는지 물었고, ChatGPT는 있다고 답했습니다` | `변호사는 ChatGPT에 판례가 실제로 있는지 물었고, ChatGPT는 있다고 답했습니다<sup class="cite" data-ref="mata-2023"></sup>` |
| 7 | 권고 | Bard 문단 첫 문장 | 인용 누락. Reuters(Coulter, Bensinger, 2023-02-08)가 처음 지적. 새 키 reuters-2023-bard | `Bard의 답변을 보여 주었습니다` | `Bard의 답변을 보여 주었습니다<sup class="cite" data-ref="reuters-2023-bard"></sup>` |
| 8 | 권고 | Bard 문단 둘째 문장 | 인용 누락. 2M1207b, 2004년 ESO VLT(NACO), 2005년 행성 확정. 새 키 eso-2m1207b | `2004년 유럽남방천문대의 VLT였습니다` | `2004년 유럽남방천문대의 VLT였습니다<sup class="cite" data-ref="eso-2m1207b"></sup>` |
| 9 | 권고 | Bard 문단 셋째 문장 | 발표 주체와 인용 없음. 2023-02-08 장중 최대 약 9%, 종가 약 8% 하락 | `오류가 보도된 날 모회사 Alphabet의 주가가 하락했습니다.` | `Reuters가 오류를 보도한 2023년 2월 8일 모회사 Alphabet의 주가가 하락했습니다<sup class="cite" data-ref="reuters-2023-bard"></sup>.` |
| 10 | 권고 | Bard 문단 마지막 문장 | 인과 단정. 같은 날 하락에는 행사 내용, Microsoft 경쟁 발표도 거론 | `공개하기 전에 확인하지 않은 작은 사실 오류가 신뢰와 평판에 큰 영향을 줄 수 있음을 보여 줍니다.` | `공개하기 전에 확인하지 않은 사실 오류가 평판과 시장의 반응에 부담이 될 수 있음을 보여 줍니다. 같은 날의 주가 하락에는 행사 내용과 경쟁사 발표도 거론되었으므로, 오류만이 원인이라고 단정할 수는 없습니다.` |

### 참고(미확인)
- Ji 외의 내재적·외재적 정의 원문 문구(1절 또는 2절) 미확인.
- Avianca 결정문 본문의 연대 책임 문구와 ChatGPT 질의 대목 미확인(헤드노트로는 연대 책임과 5,000달러 확인).
- Lewis 외 학회 게재처, Kalai 외 소속, Reuters 원문 주소는 검색 요약과 재배포본으로만 확인.

## 3. research 기록 문안
research/ch04-sources.md "2026-10-25 fact-checker 재확인(Chapter 4)"에 옮김. bibliography.json 새 키 mata-2023, reuters-2023-bard, eso-2m1207b 제안(주소는 검색 결과 그대로, 원문 주소 확인 시 교체).

필수 0, 권고 10, 참고 3, 확인한 사실 문장 23개
