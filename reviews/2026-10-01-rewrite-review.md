# 검수본(ai-book-rewrite.zip) 반영 검토

## 1. 기준 커밋
- editorial-2 b4a1e8f 위에 검수본 src 29개를 얹어 검토
- 검토 후 반영 커밋: b3692f4 (당시 사용자 지시로 Claude가 직접 커밋)

## 2. 검수 범위
- 검수본 src 29개(표지, Chapter 1~8, 부록 6개, 위키 14쪽) 전체
- 빌드 일치, 검사 4종, 표 렌더링(1148px), 이전 결정 유지 여부, 새로 들어온 사실 정보

## 3. 검사 출력 원문 (검수본 그대로)
```
pages: 29 / build exit=0
빌드 결과물이 zip 안의 결과물과 같은지: 다른 파일 수 0
grep -nEf lint/banned.txt ... → exit=1 (적중 없음)
python3 lint/check_numbers.py → exit=0
python3 lint/check_structure.py → exit=1
  chapters/ch02.html: 그림 2-1이 요약하는 표 2-1보다 뒤에 있음
  chapters/ch08.html: 그림 8-1이 요약하는 표 8-7보다 뒤에 있음
  appendix/f-trends.html: 그림 F-1이 요약하는 표 F-2보다 뒤에 있음
  wiki/index.html, pe-agents.html, pe-evaluation.html, pe-foundations.html: 절 제목 바로 뒤에 그림 또는 표
python3 lint/check_style.py | tail -1 → 합계: 50 (이전 259)
표 렌더링 1148px: 문제 셀 26, 넘침 0, 가로 스크롤 1 (표 2-1, 표 폭 940px)
```

## 4. 판정
### 좋아진 점
- 배제어 경고 259건에서 50건으로 감소, 금칙어 0건
- Chapter 2 첫 절이 "주장, 이유, 항목별 설명, 하위 기준" 흐름을 따름. 표 2-1을 선택 기준 3개와 추가 확인 3개로 나눔
- 논문 인용에 저자, 연도, 제목을 밝힘. 분량은 장별로 13~42% 증가

### 새로 생긴 문제
| 위치 | 문제 | 처리 |
|---|---|---|
| 표 2-1 | 가로 스크롤. 원인은 병합 셀(rowspan)로 둘째, 셋째 행에서 설명 칸이 둘째 열이 되어 fit-2(줄바꿈 금지)가 걸린 것 | 클래스를 fit-1로, 설명 열 비율 지정 삭제 |
| 그림 2-1 하단 | "공통 확인: 데이터 정책, 계정 유형, 파일 처리, 연동, 비용"이 새 표 2-1 구분과 어긋남 | 두 줄로 분리: "선택 기준 확인: 데이터 정책, 연동 범위 (표 2-1)", "추가 확인: 계정 유형, 파일 처리, 비용" |

### 이전 결정이 되돌아간 곳 (사용자 결정: editorial-2 기준으로 재적용)
- ch08 "표 8-3은 대표 사례입니다." → "소송 사례 가운데 일부입니다."
- ch01 절 제목 "강점과 약점", "한계와 대응" → "생성형 AI의 …"
- 그림 8-1, 그림 F-1을 같은 절의 표보다 앞으로
- 위키 4쪽 절 첫 문장 복원

### 검수 Agent의 오판 1건
- "부록 F 제목이 `부록 F.`로 되돌아감"으로 보고했으나 실제로는 상단 표시 `부록`과 제목 `F. 주요 기술 변화`가 따로 있었음. 태그를 지운 텍스트에서 둘이 붙어 보인 것

### 검사 도구 조정
- 구조 검사의 요약 그림 규칙을 "같은 절 안의 표"로 좁힘(그림 2-1은 다른 절의 표 2-1을 적용하는 절차 그림이라 제외)
- 병합 셀이 있는 표에 fit-2 이상을 쓰면 경고하는 항목 추가

### 반영 후 검사 (b3692f4)
```
build exit=0 / banned grep exit=1 / check_numbers exit=0 / check_structure exit=0 / check_style 합계: 50
표 렌더링 1148px: 넘침 0, 가로 스크롤 0, 줄바꿈 25 (표 2-9 23, F-2 2)
```

## 5. 사실 대조 출처 (새로 들어온 사실 9건, 모두 일치)
| 항목 | 확인 내용 | 출처 |
|---|---|---|
| Lost in the Middle (Liu 외 2023) | 2023년 7월 arXiv, TACL 2024 게재 | arxiv.org/abs/2307.03172 |
| Calibrate Before Use (Zhao 외 2021) | ICML 2021, 예시 순서에 따라 정확도가 크게 변함 | arxiv.org/abs/2102.09690 |
| Curious Case of Neural Text Degeneration (Holtzman 외 2019) | 2019년 4월 arXiv, nucleus sampling 제안 | arxiv.org/abs/1904.09751 |
| Survey of Hallucination in NLG (Ji 외 2023) | 내재적, 외재적 환각 구분 | arxiv.org/abs/2202.03629 |
| Parasuraman과 Manzey (2010) | Human Factors 52(3) | doi:10.1177/0018720810376055 |
| Lee 외 (CHI 2025) | 지식 노동자 319명, 카네기멜런대와 Microsoft Research | doi:10.1145/3706598.3713778 |
| Dell'Acqua 외 | BCG 컨설턴트 758명. 2026년 Organization Science 게재 | aiinstitute.hbs.edu, doi:10.1287/orsc.2025.21838 |
| Gemini 1.5 Pro | 2024년 2월 15일 발표, 기본 128K, 일부 대상 시험 공개에서 최대 100만 토큰 | blog.google/technology/ai/long-context-window-ai-models |
| Kalai 외 (2025) | arXiv:2509.04664, 2025년 9월 4일 | arxiv.org/abs/2509.04664 |

## 6. 미결정
- 없음 (모두 b3692f4, f08a407에서 처리)
