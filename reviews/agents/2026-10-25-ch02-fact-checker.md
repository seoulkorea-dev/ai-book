# Chapter 2 사실 점검(fact-checker)

## 1. 결론(필수 1, 권고 5)

범위는 src/chapters/ch02.html 전체입니다. 확인일은 모두 2026-10-25입니다.

- 필수 1건: bibliography.json의 `anthropic-xml-tags` 주소와 제목이 낡았습니다. 문장이 말하는 내용(Anthropic이 XML 태그로 프롬프트를 나누도록 권장)은 현재 문서에서도 확인됩니다.
- 권고 5건: 인용이 없는 사실 문장 세 곳(CARE, CO-STAR, 역할 부여), 지침 기능과 시스템 프롬프트의 관계를 뒷받침하는 문서가 없는 문장, "널리 쓰이는"이라는 근거 없는 일반화입니다.
- 날짜와 요일은 일치합니다. 달력으로 계산했고, 문의 예시와 공지문의 요일이 모두 맞습니다. 2026-10-16은 금, 10-17은 토, 9-28은 월, 10-06은 화입니다. 공지문과 표 2-7의 날짜, 요일, 시각도 서로 같습니다.
- 접속 제한: nngroup.com, towardsdatascience.com, tech.gov.sg, media.nngroup.com, aclanthology.org는 DNS 오류(getaddrinfo ENOTFOUND)로 열 수 없었습니다. openai.com과 arxiv.org는 이번에 시도하지 않았고 ch01 기록의 접속 제한을 따랐습니다. 이 사이트들의 내용은 WebSearch 요약으로만 확인했고, 원문 직접 열람이 아닙니다.
- 직접 열람한 곳은 platform.claude.com(Anthropic 문서)과 support.claude.com(도움말)뿐입니다.

## 2. 지적 표

| 번호 | 등급 | 위치 | 문제와 근거 | 원문 | 고친 문안 |
|---|---|---|---|---|---|
| 1 | 필수(낡음) | research/bibliography.json `anthropic-xml-tags` (본문: src/chapters/ch02.html, "지시와 입력 자료의 구분") | 기록된 주소 `docs.claude.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags`를 열면 302로 `platform.claude.com/.../use-xml-tags`로 넘어가고, 내용은 "Prompting best practices" 페이지(`https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices`)가 나옵니다. 기록된 제목 "Use XML tags to structure your prompts"는 지금 독립 페이지가 아닙니다. 문장 내용은 같은 페이지의 절 "Structure prompts with XML tags"가 뒷받침합니다. 이 절은 "XML tags help Claude parse complex prompts unambiguously, especially when your prompt mixes instructions, context, examples, and variable inputs"라고 쓰고 `<instructions>`, `<context>`, `<input>` 태그를 예로 듭니다. 확인일 2026-10-25(직접 열람). 게시일은 페이지에 표시되지 않았습니다. 본문 문장은 고치지 않아도 됩니다. | bibliography.json의 `"title": "Use XML tags to structure your prompts"` | `"title": "Prompting best practices"`, `"url": "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices"` (3절 항목 문안 참조. 본문에 절 이름을 밝히려면 "프롬프트 작성 안내의 'Structure prompts with XML tags' 절") |
| 2 | 권고(인용 누락, 확인 범위 한정) | src/chapters/ch02.html, "프롬프트 프레임워크와 구성 요소의 대응" CARE 문단 | 문장에 인용이 없습니다. 원문 직접 열람은 못 했습니다. 검색 결과(nngroup.com 페이지 제목 "CARE: Structure for Crafting AI Prompts - NN/G", 주소 `https://www.nngroup.com/articles/careful-prompts/`)의 요약으로는 Context, Ask, Rules, Examples 네 요소이고 모든 프롬프트에 세부를 다 넣을 필요는 없다고 합니다. 이 내용은 본문 서술과 일치합니다. 작성자와 연도는 research/legacy-references.html의 기록(Moran, K., 2024)을 따랐고, 게시 월일은 미확인입니다. 요약에 따르면 Ask 설명에는 챗봇의 역할, 필요한 결과물, 개수, 단계, 형식이 포함될 수 있습니다. 그렇다면 표 2-2에서 Ask를 "목적"에만 대응시킨 것은 단순화입니다. 원문 직접 확인 전에는 판정하지 않고 작가 확인 목록에 둡니다. | `CARE는 사용자 경험 연구 기관인 Nielsen Norman Group이 생성형 AI 프롬프트 작성법으로 제시한 틀입니다. 맥락(Context), 요청(Ask), 지켜야 할 규칙(Rules), 원하는 결과의 예시(Examples)를 담게 하고, 모든 대화에 이만큼 자세한 프롬프트가 필요하지는 않다는 점도 함께 설명합니다.` | `CARE는 사용자 경험 연구 기관인 Nielsen Norman Group이 생성형 AI 프롬프트 작성법으로 제시한 틀입니다. 맥락(Context), 요청(Ask), 지켜야 할 규칙(Rules), 원하는 결과의 예시(Examples)를 담게 하고, 모든 대화에 이만큼 자세한 프롬프트가 필요하지는 않다는 점도 함께 설명합니다<sup class="cite" data-ref="moran-2024"></sup>.` (새 키 moran-2024, 3절) |
| 3 | 권고(인용 누락) | src/chapters/ch02.html, 같은 절 CO-STAR 문단 | 문장에 인용이 없습니다. 검색 결과로 확인한 사실: Sheila Teo의 글 "How I Won Singapore's GPT-4 Prompt Engineering Competition"은 Towards Data Science에 2023-12-29 게시됐고, 첫 절이 CO-STAR(Context, Objective, Style, Tone, Audience, Response)입니다. 대회는 GovTech의 싱가포르 첫 GPT-4 프롬프트 엔지니어링 대회(Prompt Royale)이고 Teo가 우승했다는 보도가 있습니다(Medium 해설글, 2차). "GovTech 데이터 과학, AI 팀이 만들었다"는 서술은 2차 글(기계지심, 302.AI 등)에서만 확인했고, Teo의 글 원문에서는 못 열었습니다. GovTech 공식 페이지(tech.gov.sg)도 열지 못했습니다. 본문의 "팀"과 달리 한 요약은 "Division"이라고 합니다. 따라서 "만든 주체", "2023년", "우승자" 서술은 인용을 달고 작가가 출간 전에 원문을 직접 확인할 목록에 둡니다. | `Sheila Teo가 글로 소개하면서 알려졌습니다.` | `Sheila Teo가 2023년 12월 Towards Data Science에 올린 글로 소개하면서 알려졌습니다<sup class="cite" data-ref="teo-2023"></sup>.` (새 키 teo-2023, 3절. 이 변경으로 문단 끝 문장 하나에만 위첨자가 달리므로 CO-STAR 문단 첫 두 문장의 근거도 같은 글임을 작가가 확인) |
| 4 | 권고(근거 없는 일반화) | src/chapters/ch02.html, 같은 절 CRAFT와 RTF 문단 | "교육 자료와 실무 안내서에서 널리 쓰이는"은 근거가 없는 일반화입니다(플레이북 7.3). 확인한 범위는 블로그, 뉴스레터, 대학 안내 페이지 수준입니다. CRAFT와 RTF 어느 쪽도 만든 기관이나 사람을 밝힌 글을 찾지 못했습니다. 이 점은 본문 서술("분명하지 않습니다")과 일치합니다. CRAFT의 다섯째 요소는 자료마다 Tone, Audience를 쓰거나 Target Audience를 쓰며(Context, Role, Action, Format 뒤), 본문 서술과 일치합니다. 일부 자료는 Action 자리에 Audience를 쓰는 변형도 있습니다. 출처가 없는 변형이라 판정에 쓰지 않았습니다. RTF는 Role, Task, Format으로 일치합니다. 검색 근거는 모두 2차 글(뉴스레터, 블로그)이라 단서로만 씁니다. | `CRAFT와 RTF는 교육 자료와 실무 안내서에서 널리 쓰이는 약어이며, 처음 만든 기관이나 사람은 분명하지 않습니다.` | `CRAFT와 RTF는 블로그와 교육 자료에서 쓰이는 약어이며, 처음 만든 기관이나 사람은 분명하지 않습니다.` |
| 5 | 권고(인용 누락, 뒷받침 범위) | src/chapters/ch02.html, "역할 부여의 효과와 한계" | "모델에게 없는 전문 지식을 추가하지는 않는다"에 근거가 없습니다. Anthropic 문서는 "Setting a role in the system prompt focuses Claude's behavior and tone for your use case"라고만 해서 관점과 어조를 정한다는 쪽만 뒷받침합니다(직접 열람, claude-prompting-best-practices). 지식을 더하지 않는다는 쪽은 Zheng 외의 논문(arXiv 2311.10054, Findings of EMNLP 2024)이 뒷받침합니다. 검색 요약에 따르면 시스템 프롬프트에 역할을 넣어도 사실 질문의 정확도가 역할 없는 대조군보다 높아지지 않았습니다. 이 논문은 arxiv.org와 aclanthology.org를 열 수 없어 원문 직접 열람은 못 했습니다. 이 근거는 사실 질문의 정확도에 한정되므로 문장을 "정확도를 높이지 않았다"로 좁혀 씁니다. 표 2-8의 "역할은 관점만 정하고 지식을 더하지 않음"도 같은 근거를 씁니다. | `역할은 설명의 관점을 정할 뿐이고, 모델에게 없는 전문 지식을 추가하지는 않습니다.` | `역할은 설명의 관점을 정할 뿐이고, 모델에게 없는 전문 지식을 추가하지는 않습니다. Zheng 외는 2024년 논문에서 시스템 프롬프트에 역할을 넣어도 사실 질문의 정확도가 역할이 없을 때보다 높아지지 않았다고 보고했습니다<sup class="cite" data-ref="zheng-2024"></sup>.` (새 키 zheng-2024, 3절) |
| 6 | 권고(인용 누락, 뒷받침 문서 없음) | src/chapters/ch02.html, "작성자에 따른 프롬프트의 종류" 표 아래 문단 | 문장 "사용자 지정 지침과 프로젝트 지침 기능은 시스템 프롬프트와 비슷한 역할을 합니다"는 제품 공식 문서가 직접 뒷받침하지 않습니다. support.claude.com/en/articles/10185728(직접 열람)은 계정 전체 지침("Any instructions you add here will be applied to all of your conversations with Claude")과 프로젝트 지침("only apply to chats within that project")의 적용 범위만 설명하고 시스템 프롬프트는 언급하지 않습니다. "시스템 프롬프트와 같은 역할"은 wikidocs 등 2차 글에서만 확인했습니다. ChatGPT의 사용자 지정 지침과 프로젝트 지침은 help.openai.com 페이지가 검색에 나오지 않아 미확인입니다(DataCamp 블로그의 2차 설명만 확인). 공식 문서로 확인되는 범위로 좁히고, 제품이 이 지침을 모델에 어떻게 전달하는지는 단정하지 않습니다. 제품 기능은 변하므로 확인일 2026-10-25를 기록합니다. | `대화형 제품의 사용자 지정 지침과 프로젝트 지침 기능은 시스템 프롬프트와 비슷한 역할을 합니다.` | `Claude 도움말은 계정 전체 지침은 모든 대화에, 프로젝트 지침은 그 프로젝트 안의 대화에만 적용된다고 설명합니다<sup class="cite" data-ref="claude-help-instructions"></sup>. 이처럼 대화 전체에 적용되는 지침 기능은 시스템 프롬프트와 비슷한 역할을 합니다.` (새 키 claude-help-instructions, 3절. 둘째 문장의 "비슷한 역할"은 근거를 찾지 못한 작가의 해석이므로 유지하려면 작가 확인) |

참고(미확인, 판정 보류)

| 번호 | 등급 | 위치 | 내용과 찾은 범위 |
|---|---|---|---|
| 7 | 참고 | ch02.html, "작성자에 따른 프롬프트의 종류"와 표 2-3 | 시스템 프롬프트, 사용자 프롬프트, 어시스턴트 메시지의 세 구분과 "사용자 메시지보다 앞에 놓임"은 Chapter 1에서 정의한 내용입니다. Anthropic best-practices 페이지에서 "system prompt"의 존재(역할을 시스템 프롬프트에 둔다)만 확인했고 세 종류 구분과 순서는 열람한 문서에서 확인하지 못했습니다. Messages API 문서는 열지 않았습니다. 작가가 1차 문서를 지정할 필요가 있습니다. |
| 8 | 참고 | ch02.html, "지시와 입력 자료의 구분" 마지막 문단 | 프롬프트 인젝션 정의(입력에 숨긴 문장으로 AI가 지시로 따르게 하는 공격)에 인용이 없습니다. 이 책은 정의를 8장에서 한다고 정해 두었습니다(BOOK_SPEC 6절). 1차 출처(OWASP 등)는 이번에 찾지 않았습니다. "모델이 입력 자료 속 문장을 지시로 처리할 수 있다"는 Anthropic 문서의 "reduces misinterpretation"과 방향은 같지만 같은 문장은 아닙니다. |
| 9 | 참고 | ch02.html 전체, 예제의 가상 값 | BOOK_SPEC 7절은 예제 사실을 docs/example-facts.md에 모으고 표와 글자까지 같게 쓰라고 합니다. 이 파일은 저장소에 없습니다(docs/에는 AUTHOR_QUEUE.md, DOCUMENTS.md, legacy, specs만 있음). 값 자체는 본문 안에서 서로 일치합니다. 공지문 날짜(2026년 기준 금요일 10월 16일)는 기준 일자(2026년 10월 31일)보다 앞이지만 "가상의 예"로 밝혀 두어 사실 오류는 아닙니다. 연도는 본문에 적혀 있지 않습니다. |
| 10 | 참고 | ch02.html, 첫 문단과 "입력 자료의 길이에 따른 위치" | "긴 입력의 중간 정보를 덜 활용한다"는 Chapter 1에서 `liu-2023`(Liu 외, 2023)로 다룹니다. ch02에는 위첨자 없이 "Chapter 1에서 본 것처럼"으로 가리키기만 합니다. ch01-sources.md가 liu-2023 기록을 갖고 있어 재인용은 필수가 아닙니다. 작가가 장 안에서도 인용을 원하면 `liu-2023`을 쓸 수 있습니다. |

## 3. research 기록 문안

research/ch02-sources.md에 추가할 문안입니다.

```
# Chapter 2 출처

## 2026-10-25 fact-checker 재확인(ch02)
접속 제한: nngroup.com, media.nngroup.com, towardsdatascience.com, tech.gov.sg, aclanthology.org는 DNS 오류(getaddrinfo ENOTFOUND)로 열 수 없었음. arxiv.org와 openai.com은 시도하지 않음(ch01 기록의 접속 제한 따름). 아래 중 "검색 결과 요약"은 WebSearch가 돌려준 1차 페이지 제목과 요약이며 원문 직접 열람이 아님. 직접 열람은 platform.claude.com, support.claude.com 페이지뿐.

- Anthropic, "Prompting best practices"(구 "Use XML tags to structure your prompts"), https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices, 게시일 페이지에 표시 없음, 확인일 2026-10-25(직접 열람). 이전 주소 https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags는 302로 platform.claude.com의 같은 경로로 넘어간 뒤 이 페이지 내용으로 연결됨. 사용: 절 "Structure prompts with XML tags"의 "XML tags help Claude parse complex prompts unambiguously, especially when your prompt mixes instructions, context, examples, and variable inputs", 절 "Give Claude a role"의 "Setting a role in the system prompt focuses Claude's behavior and tone for your use case".
- Anthropic, Claude 도움말 "Personalizing Claude"류 문서(주소 번호 10185728), https://support.claude.com/en/articles/10185728, 게시일 표시 없음, 확인일 2026-10-25(직접 열람). 사용: 계정 전체 지침은 모든 대화에 적용, 프로젝트 지침은 그 프로젝트 안의 채팅에만 적용. 시스템 프롬프트와의 관계는 문서에 없음. 문서 안에서 프로젝트 지침이 유료 전용이라는 서술과 프로젝트가 전 사용자에게 열려 있다는 서술이 충돌하므로 플랜 조건은 쓰지 않음. 문서 제목은 페이지 본문에서 확인하지 못함(미확인).
- Nielsen Norman Group, "CARE: Structure for Crafting AI Prompts", https://www.nngroup.com/articles/careful-prompts/, 2024(작성자 Moran, K.는 research/legacy-references.html 기록 기준, 게시 월일 미확인), 확인일 2026-10-25(검색 결과 요약). 사용: Context, Ask, Rules, Examples 네 요소, 모든 프롬프트에 세부를 다 넣을 필요는 없다는 설명. 요약에 따르면 Ask에는 역할, 결과물, 개수, 단계, 형식이 포함될 수 있음(표 2-2 대응이 단순화인지 원문으로 확인 필요).
- Teo, S., "How I Won Singapore's GPT-4 Prompt Engineering Competition", Towards Data Science, 2023-12-29(검색 결과 요약), https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41/, 확인일 2026-10-25(검색 결과 요약). 사용: CO-STAR의 여섯 요소 Context, Objective, Style, Tone, Audience, Response, 글이 대회 우승 경험을 다룸. 미확인: 글 안의 "GovTech 데이터 과학 및 AI 팀이 만든 틀"이라는 서술 원문, 대회 개최일(2차 글은 2023년 11월 8일이라 하나 1차 확인 못 함).
- GovTech Singapore 공식 기술 소식 "Mastering the art of prompt engineering with Empower", https://www.tech.gov.sg/media/technews/mastering-the-art-of-prompt-engineering-with-empower, 확인일 2026-10-25. 열람 실패(DNS). 검색 결과 요약상 CO-STAR를 설명하는 GovTech 문서이나 내용은 미확인.
- Zheng, M. 외, "When 'A Helpful Assistant' Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models", arXiv:2311.10054(2023-11), Findings of EMNLP 2024(ACL Anthology 2024.findings-emnlp.888), https://arxiv.org/abs/2311.10054, 확인일 2026-10-25(검색 결과 요약). 사용: 4개 모델 계열, 162개 역할, 사실 질문 2,410개에서 시스템 프롬프트의 역할이 역할 없는 대조군보다 정확도를 높이지 않음. 성별, 역할 유형, 분야에 따라 결과 차이가 있음(요약). 수치는 원문 직접 열람 후 사용할 것.
- CRAFT, RTF: 만든 기관이나 사람을 밝힌 글을 찾지 못함(블로그, 뉴스레터, 대학 안내 페이지 수준의 2차 글만 확인, 판정 근거로 쓰지 않음). CRAFT 다섯째 요소는 Tone, Target Audience, Audience 변형이 있어 본문의 "자료마다 다름"과 방향이 같음. RTF는 Role, Task, Format.
- 날짜 계산(2026-10-25, 달력 계산): 2026-10-16 금, 2026-10-17 토, 2026-09-28 월, 2026-10-06 화. 공지문, 표 2-7, 문의 예시의 요일과 일치.
- 미확인(찾은 범위): 시스템 프롬프트, 사용자 프롬프트, 어시스턴트 메시지 세 종류 구분의 1차 문서(Anthropic best-practices 페이지에서 시스템 프롬프트 존재만 확인). ChatGPT의 사용자 지정 지침과 프로젝트 지침 공식 문서(help.openai.com은 검색 결과에 나오지 않음). 프롬프트 인젝션 정의의 1차 출처.
```

bibliography.json 항목 문안입니다.

수정(키 `anthropic-xml-tags`):
```
"anthropic-xml-tags": {
  "type": "web",
  "author": "Anthropic",
  "title": "Prompting best practices",
  "venue": "Claude Docs",
  "url": "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices"
}
```

추가:
```
"moran-2024": {
  "type": "web",
  "author": "Moran, K.",
  "title": "CARE: Structure for Crafting AI Prompts",
  "venue": "Nielsen Norman Group",
  "url": "https://www.nngroup.com/articles/careful-prompts/",
  "date": "2024"
},
"teo-2023": {
  "type": "web",
  "author": "Teo, S.",
  "title": "How I Won Singapore's GPT-4 Prompt Engineering Competition",
  "venue": "Towards Data Science",
  "url": "https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41/",
  "date": "2023-12-29"
},
"zheng-2024": {
  "type": "paper",
  "author": "Zheng, M. 외",
  "title": "When \"A Helpful Assistant\" Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models",
  "venue": "Findings of EMNLP 2024 (arXiv:2311.10054)",
  "url": "https://arxiv.org/abs/2311.10054",
  "date": "2024"
},
"claude-help-instructions": {
  "type": "web",
  "author": "Anthropic",
  "title": "Claude 도움말 개인 설정 지침과 프로젝트 지침 문서(주소 번호 10185728)",
  "venue": "Claude Help Center",
  "url": "https://support.claude.com/en/articles/10185728"
}
```
- `claude-help-instructions`의 title은 페이지 본문에서 제목을 확인하지 못해 임시 문구입니다. 작가나 작성 세션이 페이지 제목을 열어 확인한 뒤 바꿔야 합니다.
- `moran-2024`와 `teo-2023`의 date는 legacy-references.html과 검색 결과 요약 기준이며, 출간 전에 원문에서 월일을 확인할 목록에 둡니다.

필수 1, 권고 5, 참고 4, 확인한 사실 문장 17개
