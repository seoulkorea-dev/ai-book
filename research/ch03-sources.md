# Chapter 3 출처

작성 세션 기록(2026-10-25). 논문 서지는 research/legacy-references.html(원본 부록 D) 기준이며 arxiv.org는 접속 제한으로 직접 열람하지 않음. fact-checker 재확인 결과는 아래에 덧붙임.

- Brown 외(2020), Wei 외(2022), Kojima 외(2022), Wang 외(2022), Yao 외(2023, Tree of Thoughts), Yao 외(2022, ReAct), Wu 외(2022, AI Chains), Zhao 외(2021), Holtzman 외(2019): 표 3-1 아래 출처 목록과 본문 위첨자. 서지는 bibliography.json.
- Anthropic, Claude Opus 4.6 적응형 추론(Adaptive Thinking), 노력 수준(effort) 설정, Claude Opus 4.7부터 적응형 추론만 지원, Opus 4.7에서 temperature, top_p, top_k 기본값 외 값은 400 오류: 원본 원고 기록(2026-09-30 기준) 그대로. fact-checker 확인 필요.
- OpenAI 추론 모델 안내의 "단계별로 생각하라는 지시를 따로 포함하지 않도록" 안내: 원본 원고 기록 그대로. fact-checker 확인 필요.
- 마케팅 안 예시 계산(작성 세션 계산): A안 1인 도달 비용 50원, 예상 구매 500건, 건당 1만 원. B안 53.3원, 1,200건, 6,667원. C안 300원, 600건, 5,000원. 예산 1,000만 원 안 조합: A 500, B 1,200, C 600, A+C 1,100(800만 원). B+C, A+B는 예산 초과. 예상 구매 최대는 B안 단독 1,200건.

## 2026-10-25 fact-checker 재확인(Chapter 3)

- Anthropic, "Claude Opus 4.6", https://www.anthropic.com/news/claude-opus-4-6, 게시 2026-02-05, 확인 2026-10-25. "introducing adaptive thinking ... and new effort controls". 사용: Opus 4.6의 적응형 추론 도입(2026년 2월). 일치.
- Anthropic, "Thinking", Claude Docs, https://platform.claude.com/docs/en/build-with-claude/thinking, 확인 2026-10-25. "Configuring thinking" 표: Opus 4.7과 4.8은 adaptive 가능, 수동 enabled+budget_tokens는 400 오류, disabled는 추론 꺼짐으로 수용. Opus 4.6은 adaptive 가능, 수동은 deprecated. 사용: "Opus 4.7부터 적응형 추론만 지원" 불일치 판정. sampling 절: Opus 4.7, 4.8, 5, 5.5 등에서 temperature, top_p, top_k 비기본값은 400 오류. API 버전 2026-10-21부터는 어떤 값이든 모든 모델에서 400 오류.
- Anthropic, "Steering thinking", https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost, 확인 2026-10-25. effort는 soft guidance, 단계 low, medium, high, xhigh, max. 사용: 노력 수준 설정 서술.
- Anthropic, "Models overview", https://platform.claude.com/docs/en/models/overview, 확인 2026-10-25. 현행 모델 Fable 5.1, Opus 5.5(적응형 항상 켜짐), Sonnet 5.5, Haiku 5.5. 수동 extended thinking은 4.6에서 deprecated. Opus 4.7, 4.8은 legacy.
- Anthropic, "Claude Opus 4.7", https://platform.claude.com/docs/en/models/opus-4-7/overview, 확인 2026-10-25. 출시 2026-04-16, legacy, Thinking 열 Adaptive.
- Anthropic, "Claude Haiku 5.5 migration guide", https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide, 확인 2026-10-25. "Remove sampling parameters": 세 값을 빼고 프롬프트로 유도. 사용: "프롬프트로 조정" 안내.
- Anthropic, "Migrating to API version 2026-10-21", https://platform.claude.com/docs/en/api/migration-2026-10-21, 확인 2026-10-25. "Sampling parameters are removed": 세 값은 기본값이어도 400 오류. 사용: 생성 설정 절 추가 문장.
- Anthropic, 모델 마이그레이션 가이드(Opus 4.7 항목), 검색 결과 요약으로만 확인(2026-10-25): "Starting with Claude Opus 4.7, setting temperature, top_p, or top_k to any non-default value will return a 400 error ... use prompting". 본문 직접 열람 못 함.
- OpenAI, "Reasoning best practices", https://developers.openai.com/api/docs/guides/reasoning-best-practices, 검색 결과 요약으로만 확인(2026-10-25). openai.com 계열 열람 불가. 사용: "단계별로 생각하라는 지시를 포함하지 않도록 안내".
- 논문 귀속: Holtzman 외(arXiv 1904.09751, ICLR 2020) Nucleus Sampling 제안은 검색 요약으로 확인. Wu 외(CHI 2022)는 dblp와 UW IDL 검색 요약. Wang, Yao(ToT, ReAct)는 검색 요약. Brown, Wei, Kojima는 서지 정보만. 미확인: Zhao 외 2021(열람 불가), arXiv 원문 전부(접속 제한).
- "ReAct는 에이전트의 기본 동작 방식": 1차 출처 없음 → 정의에서 따라 나오는 문장(판단과 도구 사용의 반복)으로 바꿈.
- 마케팅 안 계산: 재계산 일치.

- 원문 확인(2026-10-29, Q-064 반영 뒤 닫음, 직접 열람): Opus 4.7 이후 temperature, top_p, top_k 비기본값 400 오류 — Anthropic Thinking 문서 sampling 절(https://platform.claude.com/docs/en/build-with-claude/thinking). 123행 위첨자를 anthropic-thinking으로 교체. budget_tokens 400(같은 문서 표), '프롬프트로 조정'(Haiku 5.5, Opus 5.5 migration guide) 일치.
- 원문 미열람(2026-10-29, Q-064 일부 유지): OpenAI Reasoning best practices(developers.openai.com), Zhao 외(2021, arxiv) 접속 차단. 출간 전 작가 열람 목록.
- 원문 확인(2026-10-29, Q-067 닫음): Turpin 외(2023) 초록(저자 저장소 https://raw.githubusercontent.com/milesaturpin/cot-unfaithfulness/main/README.md, "CoT explanations can systematically misrepresent the true reason for a model's prediction"), Anthropic "Reasoning models don't always say what they think"(https://www.anthropic.com/research/reasoning-models-dont-say-think, 2025-04-03). 33행 끝에 한계 문장과 위첨자 추가.
