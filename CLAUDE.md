# ai-book 작업 안내 (Claude Code용)

생성형 AI 실전 가이드 원고 저장소입니다. 배포: https://seoulkorea-dev.github.io/ai-book/ (GitHub Pages, main 브랜치 루트)

## 구조

- `src/` 원고 원본. 페이지별 본문 조각(HTML)과 목차 설정 `src/site.json`
- `tools/build.py` `src/`를 읽어 루트의 `index.html`, `chapters/`, `appendix/`, `wiki/`를 만든다
- 루트의 `index.html`, `chapters/`, `appendix/`, `wiki/`는 빌드 결과물이다. 직접 고치지 않고 `src/`를 고친 뒤 빌드한다
- `assets/style.css` 스타일, `STYLE.md` 문체 규칙, `lint/` 검사 도구

## 작업 절차

1. `git pull --rebase origin main` (웹에서 고친 커밋이 있을 수 있음)
2. `src/`의 조각을 고친다. 목차, 페이지 제목, 설명은 `src/site.json`
3. `python3 tools/build.py`
4. 검사를 실행하고 출력을 그대로 보고한다
   - `grep -nEf lint/banned.txt index.html chapters/*.html appendix/*.html wiki/*.html` 출력 없어야 함
   - `python3 lint/check_numbers.py` 출력 없어야 함
   - `python3 lint/check_style.py | tail -1` 경고 합계만 보고
5. 커밋과 푸시는 사용자가 요청할 때만 한다. 커밋 메시지는 `docs: ...` 형식
6. 푸시 후 배포 확인 (sleep은 5초 이하)

```bash
git fetch -q origin
LOCAL=$(git rev-parse --short HEAD); REMOTE=$(git rev-parse --short origin/main)
DEPLOY=$(curl -s "https://api.github.com/repos/seoulkorea-dev/ai-book/deployments?environment=github-pages&per_page=1" | grep -m1 '"sha"' | cut -d'"' -f4 | cut -c1-7)
echo "로컬 $LOCAL / 원격 $REMOTE / 배포 $DEPLOY"
```

로컬, 원격, 배포 세 값이 같으면 배포 완료다. 배포가 다르면 5초 간격으로 다시 확인한다.

## 원고 규칙 요약 (자세한 내용은 STYLE.md)

- 합니다체. 항목 나열은 가운뎃점 대신 쉼표
- 그림과 표: 본문, 부록, 위키는 번호, 제목, 개조식 캡션 설명(1~2줄, 명사로 끝맺음, `<ul class="capnote">`). 표지와 머리말은 번호와 캡션 없음
- 번호는 chapter 번호-순번(표 3-1, 그림 8-1). 부록은 표 A-1, 위키는 페이지마다 표 1부터. 번호를 바꾸면 `id`(`tbl-3-1`, `fig-8-1`)와 본문 참조도 함께 바꾼다
- 표 열 이름의 "예"는 "예제"
- 프롬프트 5요소: 목적, 역할, 맥락, 출력 형식, 제약 조건 (이 순서)
- 출처 유형 표시(배지)는 쓰지 않는다. 출처는 문장 안에 주체와 제목으로 밝힌다
- 사실 추가는 원문 확인 후. 확인하지 못한 사실은 넣지 않고 사용자에게 알린다

## 진행 중인 작업

1. 목차 개편 (Part 4, Chapter 8, 부록 F): 완료
2. 표 형식 변경: 기준 합의 완료, 적용 전
   - 영문 병기는 기술 용어 열에만 (예: 계층 (Layer), 역할 (Role), 예제 (Examples))
   - 첫 열 번호는 계층, 단계, 절차처럼 순서가 있는 표에만
   - 설명 열은 첫 열만으로 뜻이 불분명한 표에만
   - 빗금(/) 쓰지 않음
   - 표 2-1은 사용자 쪽 계층부터: 1. 애플리케이션, 2. 에이전트, 3. 연동, 4. API, 5. 모델 (2장 본문 설명 순서도 함께 변경)
3. B 배제어 치환 (`lint/check_style.py` 경고 260건): 프롬프트 예제에도 적용, 검사는 경고만. 치환표는 사용자 확인 대기
