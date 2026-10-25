# Chapter 1 사실 점검(fact-checker)

## 1. 결론(필수 0, 권고 11)

기준일은 2026-10-25입니다. 이 환경은 arxiv.org, aclanthology.org, openai.com, research.google, huggingface.co, ar5iv, semanticscholar, neurips.cc 직접 열기가 모두 막혀 있었습니다(WebFetch는 DNS 오류, curl은 프록시 403). 열린 1차 사이트는 anthropic.com뿐이었습니다. 그래서 논문 판정은 WebSearch가 돌려준 1차 페이지 제목과 초록 요약까지만 근거로 삼았습니다. 이 한계는 아래 표에 "검색 결과 요약 기준"으로 표시했습니다.

- 일치로 판정한 것
  - 트랜스포머는 Vaswani 외의 2017년 논문 「Attention Is All You Need」(arXiv:1706.03762, NIPS 2017)에서 제안한 구조입니다.
  - Liu 외 「Lost in the Middle」의 결론은 본문과 일치합니다. 관련 정보가 입력의 처음이나 끝에 있을 때 정확도가 가장 높고, 중간에 있으면 떨어집니다.
  - InstructGPT는 OpenAI의 연구이고 RLHF를 씁니다. 블로그 게시일은 2022-01-27, 논문은 2022-03(arXiv:2203.02155)입니다.
  - Constitutional AI는 Anthropic이 2022-12-15에 발표했습니다. 이 날짜는 anthropic.com 원문 페이지를 직접 열어 확인했습니다.
- bibliography.json 네 항목의 저자, 제목, arXiv 번호, 연도, URL은 검색 결과와 모두 맞습니다.
- 위첨자 네 곳은 모두 문장 끝 마침표 앞에 있습니다.
- 필수(불일치, 낡음, 출처 없는 수치)는 없습니다. 권고는 근거와 문장 사이의 범위 차이 또는 인용 누락입니다. 미확인은 참고 4건입니다.
- 이 장에 요금, 모델 버전, 컨텍스트 윈도 크기 같은 수치는 없습니다. 한국어 토큰 수도 배수 없이 정성 서술이라 수치 검증 대상이 없습니다.

## 2. 지적 표

| 번호 | 등급 | 위치 | 문제와 근거(주소, 확인 위치, 확인 날짜) | 원문 | 고친 문안 |
|---|---|---|---|---|---|
| 1 | 권고 | src/chapters/ch01.html, 대규모 언어 모델이 문장을 만드는 과정 | 인용이 없는 "모두" 단정입니다. GPT-4 기술 보고서(OpenAI, arXiv:2303.08774, 2023)의 초록이 "GPT-4 is a Transformer-based model pre-trained to predict the next token"이라고 밝힙니다(검색 결과 요약 기준, 2026-10-25). Gemini 기술 보고서(Gemini Team, Google, arXiv:2312.11805, 2023)의 Model Architecture 절은 "build on top of Transformer decoders (Vaswani et al., 2017)"라고 합니다. 이 인용문은 제3자 미러(hackernoon)에서 본 것이라 원문 PDF로 작가가 재확인해야 합니다. Claude 계열은 3번 항목을 보세요. 발표 주체도 문장에 없습니다. 아래 고친 문안은 Claude를 뺀 안입니다. | `대화형 AI 제품의 바탕인 GPT 계열, Claude 계열, Gemini 계열 모델은 모두 이 구조를 기반으로 합니다.` | `OpenAI의 GPT-4 기술 보고서는 GPT-4를 트랜스포머 기반 모델이라고 밝히고, Google의 Gemini 기술 보고서는 Gemini 모델이 트랜스포머 디코더를 바탕으로 한다고 밝힙니다<sup class="cite" data-ref="openai-2023"></sup><sup class="cite" data-ref="gemini-2023"></sup>.` (키 두 개는 3절에 항목 문안이 있습니다. 위첨자 두 개를 문장 끝에 붙이는 방식이 BOOK_SPEC D-006에 맞는지는 작가 확인이 필요합니다.) |
| 2 | 참고(미확인) | 같은 절 | Claude 계열이 트랜스포머 기반이라는 Anthropic 공식 문서를 현행 모델에서는 찾지 못했습니다. 찾은 범위는 다음과 같습니다. Claude 2 모델 카드(anthropic.com/claude-2-model-card)에 "transformer architecture"가 나온다는 것은 검색 결과 요약으로만 보았습니다. 카드 PDF는 assets.claude.com, www-cdn.anthropic.com이 막혀 못 열었습니다. Anthropic Transparency Hub 모델 보고서(anthropic.com/transparency/model-report, 2026-10-02)는 앞 10만 자를 읽었고 트랜스포머 언급이 없었습니다(뒤 8만 자는 읽지 못함). 확인 전에는 Claude 계열을 "모두" 안에 넣지 않는 쪽으로 위 1번 문안을 제안했습니다. 문장을 바꾸지 않고 두려면 작가 확인 목록에 올립니다. | (1번과 같음) | (1번 문안 사용. 작가 확인: 현행 Claude 모델 카드에서 트랜스포머 언급 확인) |
| 3 | 참고(미확인) | 같은 절 | 「GPT = Generative Pre-trained Transformer」 약자의 1차 출처를 찾지 못했습니다. 검색 결과 요약에 따르면 OpenAI의 2018년 GPT-1 논문 제목은 "Improving Language Understanding by Generative Pre-Training"입니다. 풀어쓴 이름은 제3자 사이트에서만 나옵니다. openai.com을 열 수 없어 OpenAI 공식 설명 페이지는 확인하지 못했습니다. 이 약자는 널리 쓰이는 표기라 문장은 그대로 두고 작가 확인 목록에만 올립니다. | `GPT라는 이름도 Generative Pre-trained Transformer의 약자입니다.` | (변경 없음. 출간 전에 OpenAI 문서에서 확인) |
| 4 | 권고 | 컨텍스트 윈도와 긴 입력의 처리 | 인용이 원문 범위보다 넓습니다. Liu 외(arXiv:2307.03172, TACL 2024)의 초록은 다중 문서 질의응답과 키-값 검색 실험에서 관련 정보가 처음이나 끝에 있을 때 성능이 가장 높고 중간에 있으면 크게 떨어진다고 보고합니다(검색 결과 요약 기준, 2026-10-25). 본문은 실험 과제를 밝히지 않은 채 "모델이 덜 활용한다"고 일반화합니다. | `Liu 외는 2023년 논문 「Lost in the Middle」에서 긴 입력의 중간에 놓인 정보를 모델이 앞과 끝의 정보보다 덜 활용한다고 보고했습니다` | `Liu 외는 2023년 논문 「Lost in the Middle」에서 다중 문서 질의응답과 키-값 검색 실험 결과, 관련 정보가 긴 입력의 중간에 있을 때 앞이나 끝에 있을 때보다 정확도가 떨어진다고 보고했습니다` |
| 5 | 권고 | 언어에 따라 달라지는 토큰 수 | 토크나이저와 한국어 토큰 수 문장에 인용이 없습니다. Petrov 외(NeurIPS 2023, arXiv:2305.15425)는 같은 텍스트의 토큰 수가 언어마다 크게 다르다고 보고합니다. 17개 토크나이저에서 최대 약 15배 차이가 났고 이는 요금과 사용 가능한 컨텍스트 감소로 이어집니다(검색 결과 요약 기준, 2026-10-25). 다만 초록에는 한국어 수치가 없어 "한국어가 더 많다"는 구체 문장은 미확인입니다. 한국어 부분은 제품 토큰 계산 도구로 실측해서 쓰거나 이 문장을 일반 표현으로 좁히는 것이 안전합니다. | `토크나이저가 영어 텍스트를 중심으로 만들어진 경우, 같은 뜻의 한국어 문장이 더 많은 토큰으로 나뉠 수 있습니다.` | `Petrov 외는 2023년 논문에서 같은 텍스트라도 언어에 따라 토큰 수가 크게 달라진다고 보고했습니다<sup class="cite" data-ref="petrov-2023"></sup>. 토크나이저가 영어 텍스트를 중심으로 만들어진 경우, 같은 뜻의 한국어 문장이 더 많은 토큰으로 나뉠 수 있습니다.` (기존 한국어 문장은 작가가 실측으로 보강하기 전까지 미확인으로 둠) |
| 6 | 권고 | 대화형 제품이 되기까지의 학습 단계, 선호 학습 문단 | InstructGPT(OpenAI, 2022)는 사람이 쓴 시연으로 지도 미세 조정을 하고, 사람의 비교 순위로 보상 모델을 학습한 뒤, 그 보상 모델로 강화 학습합니다(검색 결과 요약 기준, 2026-10-25). 본문의 "비교 평가를 보상으로 사용"은 보상 모델 단계를 빼 단순화했습니다. 이 연구는 지시 학습(지도 미세 조정)도 포함하는데 "선호 학습의 대표 방법"으로만 소개합니다. "대표"를 뒷받침하는 근거도 없습니다. | `선호 학습의 대표 방법은 두 가지입니다.` | `선호 학습에 쓰는 방법으로 두 연구가 있습니다.` |
| 6a | 권고 | 같은 문단 | 위 6번에 이어지는 같은 문제로, RLHF 설명을 InstructGPT 방법에 맞게 바꿉니다. | `이 방법은 사람의 비교 평가를 보상으로 사용하는 사람 피드백 기반 강화 학습(Reinforcement Learning from Human Feedback, RLHF)입니다.` | `이 방법은 사람의 비교 평가로 보상 모델을 학습하고 그 보상 모델의 점수로 강화 학습하는 사람 피드백 기반 강화 학습(Reinforcement Learning from Human Feedback, RLHF)입니다.` |
| 7 | 권고 | 같은 문단 | Constitutional AI 설명이 일부만 담겼습니다. Anthropic 원문(https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback, 게시일 2022-12-15, 직접 열어 확인한 2026-10-25)은 두 단계라고 설명합니다. 지도 단계에서는 모델이 원칙에 따라 자기 답변을 비평하고 수정해 그 수정본으로 미세 조정합니다. 강화 학습 단계에서는 모델이 두 답변 중 원칙에 더 맞는 쪽을 고른 AI 선호로 선호 모델을 학습시켜 보상 신호로 씁니다(RLAIF). 본문은 앞 단계만 쓰는데, 이 문단은 "선호 학습"의 예이므로 선호를 만드는 두 번째 단계가 빠진 것이 문제입니다. | `Anthropic은 2022년 12월, 원칙 목록을 기준으로 AI가 자기 답변을 평가하고 수정하게 하는 Constitutional AI 방법을 발표했습니다` | `Anthropic은 2022년 12월, 원칙 목록을 기준으로 AI가 자기 답변을 평가하고 수정한 데이터로 모델을 학습한 뒤, AI가 두 답변 가운데 원칙에 더 맞는 쪽을 고른 선호로 강화 학습하는 Constitutional AI 방법을 발표했습니다` |
| 8 | 권고 | 같은 절 첫 문장 | 세 단계가 모든 대화형 제품에 적용된다는 일반화에 근거가 없습니다. 근거는 InstructGPT의 순서(사전 학습, 지도 미세 조정, RLHF)입니다. Anthropic 문서는 사전 학습 후 RLHF와 Constitutional AI(Claude 2 모델 카드, 검색 결과 요약 기준), RLHF와 RLAIF(Claude Opus 4.6 시스템 카드, 2026-02, 검색 결과 요약 기준)로 설명할 뿐 "지시 학습"이라는 별도 단계를 명시하지 않습니다. 장의 핵심 정의에 가까워 작가 확인이 필요합니다. | `다음 토큰을 예측하는 모델이 사용자의 지시를 따르는 대화형 제품이 되기까지는 세 단계의 학습을 거칩니다.` | `다음 토큰을 예측하는 모델이 사용자의 지시를 따르는 대화형 제품이 되는 과정은 사전 학습, 지시 학습, 선호 학습의 세 단계로 설명할 수 있습니다.` (제품별 단계 구분은 공개 문서마다 다름) |
| 9 | 권고 | 생성형 AI의 강점과 약점 | 인용 없는 인과 단정입니다("때문", "그대로"). 학습 데이터 편향이 결과에 반영된다는 점은 널리 보고되지만, 원문 인용 없이 "사람에 대한 판단에 약한 이유 전부"로 쓸 수 없습니다. 근거를 찾지 못해 단정을 좁히는 안을 냅니다. | `사람에 대한 판단에 약한 것은 학습 데이터의 불균형이 결과에 그대로 반영되는 편향(Bias) 때문입니다.` | `사람에 대한 판단에 약한 이유 가운데 하나는 학습 데이터의 불균형이 결과에 반영되는 편향(Bias)입니다.` |
| 10 | 권고 | 표 1-6, 정확한 계산 행 | 인과 단정입니다. Singh·Strouse(arXiv:2402.14903, 2024)는 GPT-3.5와 GPT-4에서 숫자 토큰화 방향만 바꿔도 덧셈 정확도가 올라갔고(GPT-3.5 75.6%에서 97.8%, GPT-4 84.4%에서 98.9%), 모델이 클수록 차이가 줄어든다고 보고합니다(검색 결과 요약 기준, 2026-10-25). 토큰화가 원인 중 하나임은 뒷받침되지만 "자릿수와 자리올림을 놓침"이라는 일반 단정은 범위를 넘습니다. | `숫자를 토큰 단위로 처리해 자릿수와 자리올림을 놓침` | `숫자를 토큰 단위로 처리하므로 토큰이 나뉘는 방식에 따라 자릿수 계산에서 오류가 생김` |
| 11 | 권고 | 표 1-6, 분류와 정보 추출 행 | 같은 장 안에서 같은 장치의 힘이 다릅니다(플레이북 7.2). 표 1-7과 그림 1-2는 같은 요청도 실행마다 결과가 달라진다고 쓰는데, 이 칸은 "일정하게 출력"이라고 단정합니다. | `기준과 예시를 제공하면 정해진 형식으로 일정하게 출력` | `기준과 예시를 제공하면 정해진 형식에 맞춰 출력` |
| 12 | 권고 | 입력과 출력 형태에 따른 생성형 AI 분류 | 멀티모달 통합 문장에 발표 주체와 시점이 없습니다. 확인한 것은 OpenAI GPT-4 기술 보고서(2023)가 이미지와 텍스트 입력, 텍스트 출력 모델이라고 밝힌 부분(검색 결과 요약 기준)뿐입니다. 음성 대화와 영상 생성 기능이 "한 제품 안에 통합"되었다는 서술은 제품 공식 문서로 확인하지 못했습니다(미확인). 제품 기능은 기준 일자 2026년 10월에 바뀔 수 있습니다. | `초기 대화형 AI는 텍스트만 처리했지만, 이후 이미지 인식, 음성 대화, 이미지와 영상 생성 기능이 한 제품 안에 통합되었습니다.` | `초기 대화형 AI는 텍스트만 처리했지만, OpenAI의 GPT-4 기술 보고서(2023)는 이미지와 텍스트를 입력으로 받는 모델을 소개했습니다<sup class="cite" data-ref="openai-2023"></sup>. 이후 대화형 AI에 음성 대화와 이미지, 영상 생성 기능이 더해졌습니다.` (둘째 문장은 제품 공식 문서로 작가가 확인하거나, 확인 전에는 삭제) |
| 13 | 권고 | 같은 절 | 이미지와 음성 입력에서도 환각이 생긴다는 문장에 인용이 없습니다. Rohrbach 외, "Object Hallucination in Image Captioning"(EMNLP 2018, D18-1437)은 이미지 캡션 모델이 이미지에 없는 물체를 묘사한다고 보고합니다. Koenecke 외, "Careless Whisper: Speech-to-Text Hallucination Harms"(FAccT 2024, arXiv:2402.08021)는 OpenAI의 Whisper 전사 중 약 1%에 통째로 지어낸 문구가 있었다고 보고합니다(둘 다 검색 결과 요약 기준, 2026-10-25). 후자는 2023년 시점 결과이고 이후 개선되었다는 저자 코멘트가 있어 시점을 밝혀야 합니다. | `이미지와 음성 입력에서도 사실이 아닌 내용을 사실처럼 만드는 환각(Hallucination)이 생길 수 있으므로, 결과는 원본 이미지나 녹음과 대조합니다.` | `이미지 설명 모델이 이미지에 없는 물체를 묘사한 사례<sup class="cite" data-ref="rohrbach-2018"></sup>와, 음성 인식 모델 Whisper의 전사에 말하지 않은 문구가 들어간 사례<sup class="cite" data-ref="koenecke-2024"></sup>가 논문으로 보고되어 있습니다. 이미지와 음성 입력에서도 사실이 아닌 내용을 사실처럼 만드는 환각(Hallucination)이 생길 수 있으므로, 결과는 원본 이미지나 녹음과 대조합니다.` (위첨자가 문장 중간에 오므로 BOOK_SPEC과 플레이북 7.4의 "문장 끝, 마침표 앞" 규칙과 충돌합니다. 사례를 두 문장으로 나눠 각각 끝에 위첨자를 두는 안을 작가가 선택하세요.) |
| 14 | 참고(미확인) | 표 1-6, 긴 문제 풀이 행과 코드 작성 행 | 두 이유 칸의 근거를 찾지 못했습니다. 찾은 범위는 이 장의 인용 네 편과 위 검색입니다. 「단계가 길수록 오류가 누적」과 「공개 코드로 학습했고」는 1차 출처를 확인하지 않았습니다. 문장은 바꾸지 않았고, 근거를 붙이거나 작가가 확인하는 목록에 올립니다. | `단계가 길수록 오류가 누적되고, 긴 입력의 중간 정보를 덜 활용` | (변경 없음) |
| 15 | 참고 | bibliography.json, liu-2023 등 | 서지 정확성은 모두 일치합니다. 저자, 제목, arXiv 번호, URL, 연도가 검색 결과의 1차 페이지 정보와 같습니다. 다만 플레이북 7.4는 논문의 "학술지나 학회"를 쓰게 합니다. Liu 외는 TACL 2024(DOI 10.1162/tacl_a_00638), Vaswani 외는 NIPS 2017, Ouyang 외는 NeurIPS 2022로 출판되었고, 현재 venue는 arXiv입니다. 연도도 본문 문장("2023년 논문")과 맞는 arXiv 연도입니다. 어느 쪽을 쓸지는 작가가 정합니다. | (bibliography.json 항목) | (변경 없음, 선택 사항) |

## 3. research 기록 문안

```
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
```

새 인용 키 항목 문안(채택하는 경우만):

```json
"openai-2023": {"type": "paper", "author": "OpenAI", "title": "GPT-4 Technical Report", "venue": "arXiv:2303.08774", "url": "https://arxiv.org/abs/2303.08774", "date": "2023"},
"gemini-2023": {"type": "paper", "author": "Gemini Team, Google", "title": "Gemini: A Family of Highly Capable Multimodal Models", "venue": "arXiv:2312.11805", "url": "https://arxiv.org/abs/2312.11805", "date": "2023"},
"petrov-2023": {"type": "paper", "author": "Petrov, A. 외", "title": "Language Model Tokenizers Introduce Unfairness Between Languages", "venue": "NeurIPS 2023 (arXiv:2305.15425)", "url": "https://arxiv.org/abs/2305.15425", "date": "2023"},
"rohrbach-2018": {"type": "paper", "author": "Rohrbach, A. 외", "title": "Object Hallucination in Image Captioning", "venue": "EMNLP 2018", "url": "https://aclanthology.org/D18-1437/", "date": "2018"},
"koenecke-2024": {"type": "paper", "author": "Koenecke, A. 외", "title": "Careless Whisper: Speech-to-Text Hallucination Harms", "venue": "FAccT 2024 (arXiv:2402.08021)", "url": "https://arxiv.org/abs/2402.08021", "date": "2024"}
```

필수 0, 권고 11, 참고 4, 확인한 사실 문장 38개
