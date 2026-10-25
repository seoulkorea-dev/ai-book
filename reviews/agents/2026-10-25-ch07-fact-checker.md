# Chapter 7 사실 점검(fact-checker, 2026-10-25)

## 1. 결론(필수 1, 권고 2)
- 필수 1: 표 7-5의 Google NotebookLM이 낡음. 2026-07-16 Google이 NotebookLM을 Gemini Notebook으로 이름을 변경(검색 결과 요약: blog.google, workspaceupdates.googleblog.com, TechCrunch, 9to5Google. 원문은 이 환경에서 열리지 않음).
- 권고 2: 버전 주석의 "다른 회사 제품도 MCP 지원"에 인용 없음(같은 인용 문서가 뒷받침, 원문 직접 확인). 머리말 실험 언급에 발표 주체 없음(내용은 src/index.html skill-gap 절과 일치).
- 일치: MCP 공개(Anthropic 2024-11-25 원문), AAIF 기부(Anthropic 2025-12-09 원문), "MCP has been adopted by ChatGPT, Cursor, Gemini, Microsoft Copilot, Visual Studio Code"(같은 원문), support.claude.com과 platform.claude.com/docs 주소 유효(HTTP 200).
- 미확인: help.openai.com, platform.openai.com/docs, support.google.com/gemini, ai.google.dev(접속 거부, DNS 실패). 제품 존재와 이름은 Claude Code 공식 쪽만 직접 열람, 나머지는 검색 결과 요약.

## 2. 지적 표

| 번호 | 등급 | 위치 | 문제와 근거 | 원문 | 고친 문안 |
|---|---|---|---|---|---|
| 1 | 필수 | src/chapters/ch07.html, 특화 도구(표 7-5 문서 기반 조사 행) | 낡음. 2026-07-16 NotebookLM → Gemini Notebook(https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/, 검색 결과 요약) | `<td>Google NotebookLM</td>` | `<td>Gemini Notebook(옛 이름 NotebookLM)</td>` |
| 2 | 권고 | src/chapters/ch07.html, MCP 버전 주석 | 인용 누락, 발표 주체 | `ChatGPT, Gemini 등 다른 회사 제품도 MCP 연결을 지원합니다.</aside>` | `Anthropic은 같은 발표에서 ChatGPT, Gemini 등이 MCP를 채택했다고 밝혔습니다<sup class="cite" data-ref="anthropic-mcp-aaif-2025"></sup>.</aside>` |
| 3 | 권고 | src/chapters/ch07.html, 활용 역량 | 발표 주체 누락(Dell'Acqua 외) | `<a href="../index.html#skill-gap">머리말</a>의 실험에서 AI를 사용한 집단은` | `<a href="../index.html#skill-gap">머리말</a>에서 소개한 Dell'Acqua 외의 실험에서 AI를 사용한 집단은` |

참고(미확인): index.html skill-gap 단락에 인용이 없고 bibliography.json에 Dell'Acqua 외 항목이 없음(시작하며 범위). 공식 안내 주소 4개 미확인(platform.openai.com/docs는 developers.openai.com으로 옮겨졌을 가능성, 3차 출처 단서). 표 7-3, 7-4의 ChatGPT, Gemini 기능은 2차 출처만. gpt-oss는 2025-08-05 공개(검색 요약). Codex가 2026-07 ChatGPT 데스크톱 앱 안으로 통합되었다는 2차 출처(본문과 충돌 없음).

## 3. research 기록 문안
research/ch07-sources.md "2026-10-25 fact-checker 재확인(Chapter 7)"에 옮김. 새 키 google-notebooklm-gemini-notebook-2026(원문 확인 후 확정).

필수 1, 권고 2, 참고 6, 확인한 사실 문장 28개
