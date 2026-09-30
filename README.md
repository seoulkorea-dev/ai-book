# 생성형 AI 실전 가이드: 원리, 활용, 위험 관리

대학생과 성인을 위한 생성형 AI 안내서입니다. 생성형 AI의 작동 방식, 프롬프트 작성, 분야별 활용, 환각과 윤리, 규제 대응을 다룹니다.

## 온라인으로 읽기

- 표지와 목차: <https://seoulkorea-dev.github.io/ai-book/>
- 위키: <https://seoulkorea-dev.github.io/ai-book/wiki/index.html>
- 태그 인덱스: <https://seoulkorea-dev.github.io/ai-book/tags.html>

## 구성

- 머리말(표지), 1부 생성형 AI의 원리와 도구, 2부 프롬프트 작성과 개선, 3부 분야별 활용, 4부 검증과 책임, 5부 AI 활용 역량과 기술 변화
- 부록 A~E (프롬프트 템플릿, 도구 점검표, 용어 사전, 참고문헌, 자가 진단)
- 위키 (개념, 도구, 사례 연구, 보안, 거버넌스), 프롬프트 엔지니어링 항목은 웹 전용

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

## 출처 유형 표시

- 논문: 학술 논문, 연구 보고서
- 법령: 법률, 규정, 판결, 소송
- 기업: 기업의 발표, 제품 문서, 보도
- 기관: 정부, 국제기구, 학술지, 표준 단체 등 기관의 발표

비교는 회사가 아니라 제품 단위로 합니다.
