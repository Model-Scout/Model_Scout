---
license: other
language:
  - ko
tags:
  - computer-use
  - regression-testing
  - office-automation
pretty_name: OneAgent Computer Use Regression Scenarios
---

# OneAgent Computer Use — 리그레션 테스트 데이터셋

OneAgent(컴퓨터유즈)의 앱 조작 기능을 회귀 검증하는 **시드 시나리오 모음**입니다. OneAgent를 수정할 때마다 예전에 되던 기능이 조용히 깨졌는지 자동으로 잡아내는 데 쓰입니다. 매번 이 고정 세트를 심어 반복 검증하므로, 버전 관리(커밋·태그)로 "언제 무엇이 바뀌었는지"를 추적합니다.

## 구성

```
scenarios/            # 앱별 시나리오(각 파일이 그 앱의 테스트 묶음)
  excel.json          # Excel: 입력·함수(SUMIFS/IF)·정렬·필터·조건부서식·드롭다운·차트·피벗·시트관리 등
  word.json           # Word: 입력·서식·찾아바꾸기·저장/PDF
  powerpoint.json     # PowerPoint: 슬라이드·서식·표·차트·이미지·레이아웃/테마 +
                      #   디자인 파이프라인(주제→완성 덱, 사후 교정 polish, Designer 적용,
                      #   모던 커스텀 템플릿) — 전 슬라이드 VLM 디자인 게이트로 판정
  slack.json          # Slack: 메시지 전송
  notion.json         # Notion: 페이지 생성
  notepad.json        # 메모장: 파일 입력·저장
  chain.json          # 연계(다중 앱): Word 보고서 → PPT 발표자료
fixtures/             # 시나리오가 참조하는 고정 파일(변경 금지)
  VRF-IMAGE.png       # PPT 이미지 삽입용
  VRF-TEST.txt        # 메모장 입력용
templates/            # 디자인 시나리오가 적용하는 커스텀 템플릿(변경 금지)
  genon-modern-light.potx   # 모던 라이트 테마(미니멀 화이트·모던 팔레트·Pretendard)
```

## 시나리오 필드

각 시나리오(항목)는 아래 필드로 구성됩니다.

- `num` — 앱별 고정 번호(테스트 선택·리포트 표기에 사용)
- `instruct` — OneAgent에 줄 실제 지시문. `{marker}`는 실행마다 새로 심는 고유 표식(예: `[VRF-T2-...]`)으로 치환
- `background` — 배경(화면 비점유) 수행 여부 측정
- `window_states` — 시작 상태(보임/최소화/닫힘/완전종료)별로 각각 실행
- `meta` — 이 테스트가 무엇을 확인하는지 / 성공·실패가 각각 무슨 의미인지(사람이 읽는 설명)
- `verify` — 정답(무엇을 어떻게 확인하나): engine(com/cdp/file/vlm), 기대 값·서식·개수 등.
  PPT 디자인 시나리오는 `design_check_all`(전 슬라이드를 이미지로 내보내 장마다 VLM 체크리스트 검사),
  `design_votes`, `expect_theme_not_default` 등 디자인 게이트 필드를 추가로 사용
- 후처리 단계(검증기 실행 훅): `apply_theme_file`(커스텀 템플릿 적용) → `auto_polish`(사후 자동 교정)
  → `auto_designer`(PowerPoint Designer 제안 적용, M365 로그인+온라인 필요) 순서로 검증 전에 수행
- `cleanup` — 검증 후 정리(오피스는 결과 저장 후 앱 종료)

> `_readme` 로 시작하는 항목은 문서용이며 실행 대상이 아닙니다.

## 사용 (검증 하네스에서)

```python
from huggingface_hub import snapshot_download
path = snapshot_download("<계정_또는_조직>/oneagent-regression",
                         repo_type="dataset", revision="v1")
# path/scenarios/*.json 를 로드해 실행
```

## 버전 관리

이 저장소는 git 기반이라 업로드(커밋)마다 이력이 남습니다. 릴리스 시점은 태그(`v1`, `v2`, …)로 고정해, 특정 버전을 재현·비교할 수 있습니다. 기능 추가·버그 수정 시 관련 시나리오를 함께 추가하는 것을 원칙으로 합니다.

## 변경 이력

- 이번 릴리스: PowerPoint 디자인 파이프라인 시나리오 확장 — num 25(완성 덱 + polish + **Designer 자동 적용**), num 26(+ **모던 커스텀 템플릿** `apply_theme_file`). `templates/genon-modern-light.potx` 픽스처 신규 추가. 검증기 후처리 훅(apply_theme_file/auto_polish/auto_designer) 필드 도입.
- 이전 릴리스: 앱 6종 + 연계(chain) 시나리오, 오피스 COM 검증(값·서식·차트·피벗), PPT 디자인 게이트(num 21~24), 시작 상태별 실행, 유니크 마커 체계.
