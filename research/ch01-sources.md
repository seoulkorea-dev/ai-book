# Chapter 1 출처

## 2026-10-25 fact-checker 재확인(ch01)
접속 제한: arxiv.org, aclanthology.org, openai.com, research.google, huggingface.co, ar5iv, semanticscholar, neurips.cc는 열 수 없었음(DNS 오류 또는 프록시 403). 아래 중 "검색 결과 요약"은 WebSearch가 돌려준 1차 페이지 제목과 초록 요약이며, 원문 직접 열람이 아님. 직접 열람은 anthropic.com 페이지만.

- Anthropic, "Constitutional AI: Harmlessness from AI feedback", https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback, 게시일 2022-12-15, 확인일 2026-10-25(직접 열람). 사용: Constitutional AI 발표 시점(2022년 12월), 지도 단계(자기 비평과 수정)와 강화 학습 단계(AI 선호, RLAIF).
- Vaswani 외, "Attention Is All You Need", https://arxiv.org/abs/1706.03762, 2017(NIPS 2017), 확인일 2026-10-25(검색 결과 요약). 사용: 트랜스포머 제안, 재귀와 합성곱 없이 어텐션만 사용. Google 연구진 소속 세부는 원문 직접 열람 미확인.
- Liu 외, "Lost in the Middle: How Language Models Use Long Contexts", https://arxiv.org/abs/2307.03172, arXiv 2023-07, TACL 2024(DOI 10.1162/tacl_a_00638), 확인일 2026-10-25(검색 결과 요약). 사용: 다중 문서 질의응답과 키-값 검색에서 관련 정보가 처음이나 끝일 때 성능이 가장 높고 중간이면 하락.
- Ouyang 외, "Training language models to follow instructions with human feedback", https://arxiv.org/abs/2203.02155, 2022-03(OpenAI 블로그 "Aligning language models to follow instructions" 2022-01-27), 확인일 2026-10-25(검색 결과 요약). 사용: InstructGPT, 시연 기반 지도 미세 조정, 비교 순위로 보상 모델 학습, RLHF.
- Bai 외, "Constitutional AI: Harmlessness from AI Feedback", https://arxiv.org/abs/2212.08073, 2022-12, 확인일 2026-10-25(anthropic.com 페이지가 이 주소를 논문으로 연결).
- OpenAI, "GPT-4 Technical Report", https://arxiv.org/abs/2303.08774, 2023-03, 확인일 2026-10-25(검색 결과 요약). 사용: Transformer 기반 모델, 이미지와 텍스트 입력, 텍스트 출력.
- Gemini Team, Google, "Gemini: A Family of Highly Capable Multimodal Models", https://arxiv.org/abs/2312.11805, 2023-12, 확인일 2026-10-25(제3자 미러만 확인, 원문 PDF 미확인). 사용: "build on top of Transformer decoders".
- Petrov 외, "Language Model Tokenizers Introduce Unfairness Between Languages", https://arxiv.org/abs/2305.15425, NeurIPS 2023, 확인일 2026-10-25(검색 결과 요약). 사용: 언어별 토큰 수 차이(최대 약 15배, 17개 토크나이저). 한국어 수치는 초록에 없음.
- Singh, Strouse, "Tokenization counts: the impact of tokenization on arithmetic in frontier LLMs", https://arxiv.org/abs/2402.14903, 2024-02, 확인일 2026-10-25(검색 결과 요약). 사용: 숫자 토큰화 방향에 따른 덧셈 정확도 차이.
- Rohrbach 외, "Object Hallucination in Image Captioning", https://aclanthology.org/D18-1437/, EMNLP 2018, 확인일 2026-10-25(검색 결과 요약). 사용: 이미지 캡션 모델의 존재하지 않는 물체 묘사.
- Koenecke 외, "Careless Whisper: Speech-to-Text Hallucination Harms", https://arxiv.org/abs/2402.08021, FAccT 2024, 확인일 2026-10-25(검색 결과 요약). 사용: Whisper 전사의 약 1%에서 통째로 지어낸 문구(2023년 시점).
- Anthropic Transparency Hub 모델 보고서, https://www.anthropic.com/transparency/model-report, 2026-10-02, 확인일 2026-10-25(앞 10만 자 직접 열람). 트랜스포머 언급 없음.
- 미확인: GPT 약자의 OpenAI 1차 출처, Claude 현행 모델의 트랜스포머 기반 공식 문서(Claude 2 모델 카드는 검색 결과 요약으로만), 표 1-6의 "단계가 길수록 오류 누적"과 "공개 코드 학습", 이미지 음성 통합 제품 기능의 공식 문서.

- 원문 확인(2026-10-29, Q-055 닫음, 직접 열람): 종료 조건(끝 토큰 또는 길이 상한) — OpenAI OpenAPI 명세 finish_reason(stop, length; https://raw.githubusercontent.com/openai/openai-openapi/master/openapi.yaml), Anthropic Stop reasons 문서(end_turn, max_tokens; https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons), Hugging Face transformers eos_token_id 설명. 원문은 사용자 지정 중지 문자열도 종료 조건으로 두나 본문은 단순화.
- 원문 확인(2026-10-29, Q-055, 직접 열람): 한도 초과 동작 — Anthropic Context windows 문서(https://platform.claude.com/docs/en/build-with-claude/context-windows): claude.ai의 선입선출 관리, API의 400 'prompt is too long' 거부, compaction 요약.
- 원문 확인(2026-10-29, Q-055, 직접 열람): 토큰 계산 도구 — Anthropic Token counting 문서(https://platform.claude.com/docs/en/build-with-claude/token-counting), OpenAI tiktoken README(https://raw.githubusercontent.com/openai/tiktoken/main/README.md).
- 원문 미열람(2026-10-29, Q-050 유지): 표 1-3 '단계가 길수록 오류 누적'(Dziri 외 2023), '공개 코드로 학습'(Chen 외 2021), 37행 음성·이미지·영상 기능 추가(OpenAI 2023-09-25 공지, DALL·E 3 공지, Google 2025-04-15 공지). arxiv.org, openai.com, blog.google 접속 차단. 출간 전 작가 열람 목록.
