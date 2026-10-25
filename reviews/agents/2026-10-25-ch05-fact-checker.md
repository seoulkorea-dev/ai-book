# Chapter 5 사실 점검(fact-checker, 2026-10-25)

## 1. 결론(필수 0, 권고 3)
- 숫자와 날짜 모두 맞음. 표 5-6의 12칸 Python 재계산 일치, 주사위 확률 6/36=1/6 일치. Nature, OpenAI, Liang 외(2023) 서술 일치(확인 범위 안에서).
- nature-2023, liang-2023 위첨자는 문장 끝 마침표 앞, bibliography.json에 있음.
- 권고 3: OpenAI 판별기 문장 인용 누락, 문헌 환각 문장 인용 누락, "검색 결과에는 실제로 있는 문헌만" 단정.
- 확인 범위 제한: nature.com, openai.com, doi.org, arxiv.org 직접 열람 실패(getaddrinfo ENOTFOUND). 모두 검색 결과 요약 근거.

## 2. 지적 표

| 번호 | 등급 | 위치 | 문제와 근거 | 원문 | 고친 문안 |
|---|---|---|---|---|---|
| 1 | 권고 | src/chapters/ch05.html, 학술 윤리(#integrity) | 인용 누락. 2023-01-31 공개, 2023-07-20 정확도가 낮다는 이유로 제공 중단(2차 보도가 원 게시물 부기를 전함). 새 키 openai-classifier-2023 | `OpenAI는 2023년 1월 공개한 AI 텍스트 판별기를 정확도가 낮다는 이유로 2023년 7월 20일 제공 중단했습니다.` | `OpenAI는 2023년 1월 공개한 AI 텍스트 판별기를 정확도가 낮다는 이유로 2023년 7월 20일 제공 중단했습니다<sup class="cite" data-ref="openai-classifier-2023"></sup>.` |
| 2 | 권고 | src/chapters/ch05.html, 문헌 확인(#sources) | 인용 누락. Walters, Wilder(2023), Scientific Reports 13: 참고문헌 636개 중 가짜 GPT-3.5 약 55%, GPT-4 약 18%. 새 키 walters-2023 | `대화형 제품은 존재하지 않는 논문 제목, 저자, 쪽수를 생성하기도 합니다.` | `Walters와 Wilder(2023)는 GPT-3.5가 작성한 문헌 검토의 참고문헌 가운데 약 55%, GPT-4가 작성한 것 가운데 약 18%가 존재하지 않는 문헌이었다고 보고했습니다<sup class="cite" data-ref="walters-2023"></sup>.` |
| 3 | 권고 | src/chapters/ch05.html, 문헌 확인(#sources) | 전칭 단정, 1차 출처 없음. 절차에 필요한 범위로 좁힘 | `검색 결과에는 실제로 있는 문헌만 나오기 때문입니다.` | `검색 결과에 나오는 문헌은 출판 기록이 있으므로 존재 여부를 직접 확인할 수 있고, 저자와 연도는 DOI와 원문으로 대조합니다.` |

참고(미확인): "AI가 작성한 글을 사람이 수정하면 탐지하지 못할 수도 있습니다"는 인용 없음, 이번 범위에서 확인 못 함. Nature, OpenAI, Liang 원문 직접 열람 못 함.

## 3. research 기록 문안
research/ch05-sources.md "2026-10-25 fact-checker 재확인(Chapter 5)"에 옮김. 새 키 openai-classifier-2023, walters-2023.

필수 0, 권고 3, 참고 2, 확인한 사실 문장 17개
