# 생성형 AI 실전 가이드: 원리, 활용, 위험관리

대학생과 성인을 위한 생성형 AI 안내서입니다. 생성형 AI의 작동 방식, 프롬프트 작성, 분야별 활용, 환각과 윤리, 규제 대응을 다룹니다.

## 온라인으로 읽기

- 표지와 목차: <https://seoulkorea-dev.github.io/ai-book/>
- 위키: <https://seoulkorea-dev.github.io/ai-book/wiki/index.html>
- 태그 인덱스: <https://seoulkorea-dev.github.io/ai-book/tags.html>

## 구성

- 서론, 1부 이해, 2부 원리, 3부 활용, 4부 위험관리, 5부 미래
- 부록 A~E (프롬프트 템플릿, 도구 비교표, 용어 사전, 참고문헌, 자가 진단)
- 위키 (개념, 도구, 사례연구, 보안, 거버넌스, 프롬프트 엔지니어링)

## 폴더 구조

- `index.html` 표지와 목차
- `tags.html` 태그 인덱스
- `chapters/` 장별 원고
- `appendix/` 부록
- `wiki/` 위키
- `assets/style.css` 공통 스타일 (아이보리 단일 테마)
- `assets/fonts/` Pretendard v1.3.9 (SIL Open Font License 1.1, `LICENSE.txt` 포함)
- `STYLE.md` 문체 규칙
- `lint/banned.txt` 금지어 목록

## 자동 점검

커밋 전에 아래 명령을 실행합니다. 결과가 0줄이어야 합니다.

```
grep -nEf lint/banned.txt index.html tags.html chapters/*.html appendix/*.html wiki/*.html
```

## 발표 주체 표시

- O: OpenAI가 발표한 내용
- A: Anthropic이 발표한 내용
- 3: 그 외 기업, 기관, 연구자의 발표

비교는 회사가 아니라 제품 단위로 합니다.
