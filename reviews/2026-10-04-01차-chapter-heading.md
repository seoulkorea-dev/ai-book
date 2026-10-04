# 장 제목 형식 변경: 번호(작게, 청록색) + 여백 + 제목(크게, 여러 줄)

- 차수: 2026-10-04 01차 (Claude), 누적 72차
- 이전 문서: 2026-10-03-17차-chapter-openings.md
- 기준 커밋: 4a13804

## 0. 배경과 사용자 결정
- 사용자 지적: 지금 제목 "Chapter 1 생성형 AI의 기본 원리와 한계"는 번호와 제목이 같은 크기로 한 줄에 붙어 어색함
- 사용자가 참고 형식 두 가지를 보여 줌. 두 번째 형식(왼쪽 정렬, 구분선 없음, 작은 번호 위에 큰 제목 여러 줄)으로 결정
- 검수 쪽 미리 보기(가. 번호 진한 회색, 나. 번호 청록색) 가운데 **나(청록색)**로 결정
- 제목 줄바꿈: 화면 폭에 맡김(검수 권장안. 제목마다 줄바꿈 위치를 따로 관리하지 않음)

## 1. 마크업
번호와 제목을 **같은 h1 안에서** 두 줄로 나눕니다. 화면 낭독기와 검색은 지금처럼 하나의 제목으로 읽습니다.

| 쪽 | 현재 | 변경 |
|---|---|---|
| Chapter 1~8 | `<h1>Chapter 1 생성형 AI의 기본 원리와 한계</h1>` | `<h1><span class="h-num">Chapter 1</span> <span class="h-title">생성형 AI의 기본 원리와 한계</span></h1>` |
| 부록 1~3 | `<h1>부록 2. 용어 풀이</h1>` | `<h1><span class="h-num">Appendix 2</span> <span class="h-title">용어 풀이</span></h1>` |
| 시작하며(표지), 마치며 | `<h1>생성형 AI, 묻고 확인하고 활용하기</h1>`, `<h1>마치며: 묻고 확인하는 습관</h1>` | 번호 없이 `<h1><span class="h-title">…</span></h1>`(같은 제목 크기) |
- 번호 글자는 원고에 "Chapter 1", "Appendix 2"로 두고, 화면에서만 대문자로 보이게 합니다(CSS `text-transform: uppercase`). 화면 낭독기가 "C-H-A-P-T-E-R"처럼 철자를 읽지 않게 하기 위해서입니다.
- 두 span 사이의 공백 한 칸은 그대로 둡니다(복사하거나 검색할 때 "Chapter 1 생성형…"으로 이어지게).
- 부록 번호를 영어("Appendix")로 할지, 한국어("부록 2")로 할지: 장 번호와 형식을 맞춰 "Appendix"로 둡니다. 사이트 목차, 본문의 "부록 1" 참조는 그대로입니다.

## 2. CSS(assets/style.css)
현재 `h1 { font-size: 40px; line-height: 1.3; … }`(모바일 32px)을 아래처럼 바꿉니다.
```css
h1 { margin: 0 0 1.25rem; }
h1 .h-num { display: block; font-size: 15px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: var(--link); margin-bottom: 1.25rem; }
h1 .h-title { display: block; font-size: 40px; font-weight: 700; line-height: 1.22; letter-spacing: -0.01em; word-break: keep-all; }
@media (max-width: 720px) { h1 .h-num { font-size: 13px; margin-bottom: 0.9rem; } h1 .h-title { font-size: 28px; } }
```
- 청록색은 책의 링크색(`--link: #1f5a66`, 표지와 그림의 청록 계열)을 씁니다. 별도 색을 만들지 않습니다.
- `word-break: keep-all`: 한국어 제목이 어절 중간에서 끊기지 않게 합니다.
- 모바일 기준 폭(720px)은 지금 스타일의 미디어 쿼리 기준에 맞춥니다(현재 값이 다르면 그 값을 따름).
- 구분선은 두지 않습니다(사용자가 고른 형식).

## 3. 함께 확인할 것
| 위치 | 확인 |
|---|---|
| src/site.json 쪽 제목(title) | 바꾸지 않음. 브라우저 탭 제목, 목차는 지금처럼 "Chapter 1 생성형 AI의 기본 원리와 한계" |
| tools/build.py 목차 처리 | 목차는 site.json을 쓰므로 영향 없음. h1을 읽는 곳이 있으면 span을 고려 |
| lint | check_numbers의 "Chapter N" 조사 검사는 본문 대상이라 영향 없음. 제목 일치 검사가 h1 글자를 비교한다면 span 안 글자를 합쳐 비교(공백 한 칸 포함) |
| 이동 쪽, 표지 | 이동 쪽은 그대로. 표지는 번호 없는 형식 |

## 4. 반영 확인 기준
- 빌드와 lint 통과, 끊긴 링크 0
- 13쪽 모두 h1이 1절 형식(장 8, 부록 3은 번호와 제목, 표지와 마치며는 제목만)
- 검수 쪽에서 데스크톱과 모바일 폭으로 1장, 5장(가장 긴 제목), 부록 1, 마치며를 캡처해 확인

## 5. 함께 반영할 문서
- 2026-10-03-17차(누적 71차) 여덟 장 첫 문단 교체: 아직 미반영(원격 4a13804 기준). 이 zip에 함께 수록

## 6. 미결정
- 없음
