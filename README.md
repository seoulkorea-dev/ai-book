# 생성형 AI 실전 가이드: 원리, 활용, 위험 관리

대학생과 성인을 위한 생성형 AI 안내서입니다. 생성형 AI의 작동 방식과 도구 선택, 프롬프트 작성, 학업과 업무에서의 역할 분담, 결과물 검증과 위험 관리를 다룹니다.

## 온라인으로 읽기

- 표지와 목차: <https://seoulkorea-dev.github.io/ai-book/>
- 위키: <https://seoulkorea-dev.github.io/ai-book/wiki/index.html>

## 구성

- 머리말(표지), Part 1 생성형 AI의 이해와 도구 선택, Part 2 프롬프트 작성, Part 3 학업과 업무에서 AI와 사람의 역할 분담, Part 4 결과물 검증과 위험 관리 (Chapter 1~8)
- 부록 A~F (프롬프트 템플릿, 도구 점검표, 용어 사전, 참고문헌, 자가 진단, 주요 기술 변화)
- 위키 (개념, 도구, 사례 연구, 보안, 거버넌스), 프롬프트 엔지니어링 항목은 웹 전용

## 폴더 구조

- `src/` 원고 원본 (페이지별 본문 조각, 목차 설정 `site.json`)
- `tools/build.py` 빌드 스크립트. `python3 tools/build.py`로 아래 결과물을 만듭니다
- `index.html`, `chapters/`, `appendix/`, `wiki/` 빌드 결과물 (직접 고치지 않음)
- `CLAUDE.md` Claude Code 작업 안내
- `assets/style.css` 공통 스타일 (아이보리 단일 테마)
- `assets/fonts/` Pretendard v1.3.9 (SIL Open Font License 1.1, `LICENSE.txt` 포함)
- `STYLE.md` 문체 규칙
- `lint/banned.txt` 금지어 목록

## 자동 점검

원고를 고친 뒤 `python3 tools/build.py`로 빌드하고, 커밋 전에 아래 명령을 실행합니다. 앞의 두 명령은 출력이 없어야 합니다. 세 번째 명령은 경고만 출력합니다.

```
grep -nEf lint/banned.txt index.html chapters/*.html appendix/*.html wiki/*.html
python3 lint/check_numbers.py
python3 lint/check_style.py
```

`check_numbers.py`는 그림, 표 번호의 순서, 누락, 중복, 없는 번호 참조, 링크 없는 번호 참조를 검사합니다. 문제가 없으면 아무것도 출력하지 않습니다.

`check_style.py`는 고유어 동사 등 한자어 치환 후보(B 배제어)를 위치와 함께 경고로 출력합니다. 종료 코드는 항상 0입니다.
