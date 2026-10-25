# Chapter 3 사실 점검(fact-checker, 2026-10-25)

## 1. 결론(필수 1, 권고 5)

원고는 고치지 않았고 보고 문안만 작성했습니다. 확인일은 2026-10-25입니다.

- 필수 1건: Opus 4.7의 "적응형 추론만 지원"은 Anthropic 문서와 맞지 않습니다. 4.7에서 400 오류인 것은 수동 예산 방식(budget_tokens)뿐이고, 추론을 끄는 것은 허용됩니다.
- 권고 5건: Anthropic, OpenAI, CoT 정확도 서술에 인용 위첨자가 없습니다. 생성 설정 절은 2026-10-21 API 버전의 변경도 반영해야 합니다.
- 일치로 확정: Opus 4.6의 적응형 추론 도입과 effort 설정, Opus 4.7의 temperature, top_p, top_k 비기본값 400 오류, 마케팅 안 계산 전부.
- 접속 제한: arxiv.org, doi.org, ar5iv, mlr.press, openai.com 계열은 열리지 않았습니다(ENOTFOUND). 논문과 OpenAI 항목은 검색 결과 요약으로만 확인했습니다.

## 2. 지적 표

| 번호 | 등급 | 위치 | 문제와 근거 | 원문 | 고친 문안 |
|---|---|---|---|---|---|
| 1 | 필수 | src/chapters/ch03.html, 단계별 추론 절 "추론 모델에서의 차이" | 불일치. Thinking 문서 "Configuring thinking" 표(https://platform.claude.com/docs/en/build-with-claude/thinking)에서 Opus 4.7은 adaptive, 수동 enabled+budget_tokens는 400 오류, disabled는 수용. 모델 개요도 수동 방식은 4.6에서 deprecated. 현행 모델은 Opus 5.5, 4.7은 legacy | `Claude Opus 4.7부터는 적응형 추론만 지원합니다.` | `Claude Opus 4.7부터는 추론 예산을 직접 지정하는 방식(budget_tokens)을 받지 않고, 적응형 추론으로 추론량을 정합니다<sup class="cite" data-ref="anthropic-thinking"></sup>.` |
| 2 | 권고 | 같은 절 | 인용 누락. Anthropic 발표 "Claude Opus 4.6"(게시 2026-02-05) "introducing adaptive thinking ... and new effort controls" 일치 | `Anthropic은 Claude Opus 4.6에서 적응형 추론(Adaptive Thinking)을 도입했습니다.` | `Anthropic은 2026년 2월 Claude Opus 4.6에서 적응형 추론(Adaptive Thinking)을 도입했습니다<sup class="cite" data-ref="anthropic-opus-4-6"></sup>.` |
| 3 | 권고 | 같은 절 | 인용 누락. OpenAI "Reasoning best practices"는 검색 결과 요약으로만 확인(방향 일치). 원문 재열람은 작가 확인 | `OpenAI는 추론 모델 안내에서 추론 모델에는 단계별로 생각하라는 지시를 따로 포함하지 않도록 안내했습니다.` | `OpenAI는 추론 모델 활용 안내(Reasoning best practices)에서 … 안내했습니다<sup class="cite" data-ref="openai-reasoning-best-practices"></sup>.` |
| 4 | 권고 | 같은 절 | 인용 누락. Steering thinking 문서와 일치(effort는 soft guidance, low~max) | `사용자는 노력 수준(effort) 설정으로 그 정도를 조절하는 방식입니다.` | 위첨자 anthropic-thinking 추가 |
| 5 | 권고 | 생성 설정 절, 표 3-5 아래 둘째 문단 | 인용 누락과 최신 변경 누락. API 버전 2026-10-21에서는 세 값을 기본값으로 보내도 모든 모델에서 400 오류 | `…프롬프트로 동작을 조정하도록 안내합니다.` | 위첨자 anthropic-model-migration 추가, `API 버전 2026-10-21부터는 모든 모델에서 이 세 값을 기본값으로 보내도 400 오류를 반환합니다<sup class="cite" data-ref="anthropic-api-2026-10-21"></sup>.` 추가 |
| 6 | 권고 | 단계별 추론 절 첫 문단 | 인용 누락(Wei 외 2022 귀속) | `여러 단계를 거치는 계산과 논리 문제에서 정확도가 높아지는 경우가 많습니다.` | 위첨자 wei-2022 추가 |

## 참고(미확인)
- Zhao 외 2021의 "예시 순서와 마지막 예시의 답이 결과에 영향": 직접 열람 못 함.
- Brown, Wei, Kojima: 서지만 확인.
- OpenAI 원문 열람 불가.
- Opus 4.7의 "프롬프트로 조정" 안내: 이전 마이그레이션 가이드 검색 요약으로만 확인.
- "ReAct는 에이전트의 기본 동작 방식이기도 합니다": 1차 출처를 찾지 못함.
- 현행 모델(작가 확인): Opus 5.5는 적응형이 항상 켜져 있고 기본 effort는 medium.

## 3. research 기록 문안
research/ch03-sources.md "2026-10-25 fact-checker 재확인(Chapter 3)"에 옮김. bibliography.json 항목 5개(anthropic-opus-4-6, anthropic-thinking, anthropic-model-migration, anthropic-api-2026-10-21, openai-reasoning-best-practices) 제안.

필수 1, 권고 5, 참고 6, 확인한 사실 문장 31개
