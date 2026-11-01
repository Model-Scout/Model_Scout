---
license: unknown
language:
- ko
tags:
- text-to-image
- lora
- korean-typography
- qwen-image
- synthetic
pretty_name: Korean Text Rendering Data
configs:
- config_name: atomic_text
  data_files:
  - split: train
    path: atomic_text/metadata.jsonl
- config_name: diagram
  data_files:
  - split: train
    path: diagram/metadata.jsonl
---

# 한글 텍스트 렌더링 학습 데이터

이미지 안에 정확한 한글 텍스트를 렌더링하는 능력 개선을 위해 만들어진 합성(synthetic) 이미지-프롬프트 데이터셋입니다. 2026년 5월~7월에 걸쳐 진행된 세 차례의 별도 학습 이터레이션에서 나온 데이터를 통합했습니다.

**총 79,460장**, 2개 config(콘텐츠 유형)로 구성. 각 config는 독립적으로 로드할 수 있습니다.

```python
from datasets import load_dataset
ds = load_dataset("<repo_id>", name="diagram")  # 유형별로 필요한 것만
```

> 이 릴리즈는 순수 한글 타이포그래피 학습에 초점을 맞춰 `atomic_text`(99.4% 한글)와
> `diagram`(100% 한글) 두 유형만 포함합니다. 둘 다 **코드·템플릿 기반 결정론적 생성**이라
> 외부 생성형 서비스에 의존하지 않고, 라이선스 문제가 없습니다. "프롬프트 안 인용부호=정답
> 텍스트" 컨벤션은 둘 다 일관됩니다.

## 왜 이런 데이터가 필요한가

일반적인 text-to-image 모델은 이미지 안에 텍스트(특히 한글)를 그릴 때 글자가 깨지거나, 문맥과 무관한 글자를 생성하거나, 일부만 렌더링하는 문제가 흔합니다. 이 데이터셋은 "프롬프트에 명시된 문자열을 정확히, 전부, 다른 글자 섞임 없이" 렌더링하도록 학습시키기 위해 설계된 합성 데이터로, 난이도(단일 단어 → 구조화 다이어그램)를 단계적으로 높여 커리큘럼처럼 구성되어 있습니다.

## Config 목록

| config | 이미지 수 | 난이도/성격 | 생성 방식 요약 |
|---|---:|---|---|
| [`atomic_text`](#atomic_text) | 71,460 | 가장 단순 — 단어 하나 | 어휘 풀 + 템플릿 렌더링 |
| [`diagram`](#diagram) | 8,000 | 중간 — 여러 라벨 + 고정 레이아웃 | HTML 슬롯 템플릿 + 단어 풀 치환 |

---

### `atomic_text`

깨끗한 단색 배경 위에 한글 단어/구 1~2개만 큼직하게 배치한 "가장 원자적인" 텍스트 렌더링 케이스. 배경색, 폰트 굵기/스타일, 텍스트 위치(중앙/상단 등), 도형 유무 등을 조합해 다양성을 확보했습니다.

- **생성 방식**: 행정·학술·기업 문서체 명사 위주 어휘 풀(일상/행정문서/정책/학술/기업/IT 도메인)에서 단어를 뽑아 템플릿에 삽입해 렌더링. "흔한 단어"가 아니라 한글 글리프(음절 조합) 커버리지를 넓히는 게 목표라, 고유어 큐레이션·실문서 채굴·LLM 필터링을 거쳐 최종 4,395단어 (743글리프, KS X 1001 기준 31.6% 커버)까지 확장했습니다.
- 71,460장 중 71,006장(99.4%)이 실제 한글 텍스트, 나머지는 영문/숫자 등.

### `diagram`

flowchart / hierarchy / dashboard / timeline 4가지 레이아웃, **각 2,000장씩 균등 분포**
(총 8,000장). 여러 개의 한글 라벨이 정해진 자리(슬롯)에 들어갑니다.

- **생성 방식**: HTML 슬롯 템플릿에 `atomic_text`와 같은 어휘 풀에서 뽑은 라벨을 채워 넣는
  방식이라 외부 서비스 의존 없이 코드로 결정론적으로 생성됩니다. 프롬프트에 렌더링되는 모든
  라벨이 읽기 순서·큰따옴표로 명시돼 있어 `target_text` 커버리지 100% (제목만 있던 초기
  버전은 품질 문제로 이번 릴리즈에서 제외 — 아래 "제외한 것" 참고).
- **`diagram_type` 필드**로 레이아웃별 필터링 가능: `ds.filter(lambda x: x["diagram_type"] == "flowchart")`.
- 전량 한글.

---

## 스키마 (두 config 공통)

각 config 폴더의 `metadata.jsonl` 한 줄이 이미지 한 장에 대응합니다 (`images/` 하위 실제 파일 참조).

| 필드 | 타입 | 설명 |
|---|---|---|
| `file_name` | str | config 폴더 기준 상대경로 (`images/000000.png`) |
| `prompt` | str | 이미지 생성에 사용된 전체 프롬프트 (텍스트 인코더 입력) |
| `target_text` | list[str] | 이미지 안에 실제로 렌더링되어야 하는 정답 문자열들 (OCR 검증·평가용) |
| `split` | str | `train` 또는 `validation` (일부만 구분 있음, 없으면 전부 `train`으로 취급) |
| `diagram_type` | str | **`diagram`에만 있음** — `flowchart`/`hierarchy`/`dashboard`/`timeline` |
| `sha256` | str | 이미지 파일 해시 (무결성 검증용) |
| `original_prompt` | str | (일부만) 캡션 생성에 쓰인 원본 지시문, 없으면 빈 문자열 |
| `width`, `height` | str | (일부만) 기록된 경우만, 없으면 빈 문자열 |

두 config 모두 `source_generation`/`source_subset`(내부 생성 세대·출처) 없이, 콘텐츠 자체를 설명하는 필드만으로 구성했습니다.

## 사용 방법

```python
from datasets import load_dataset

ds = load_dataset("<repo_id>", name="atomic_text")  # 또는 name="diagram"
print(ds["train"][0])
# {'image': <PIL.Image>, 'prompt': '...', 'target_text': ['무작위 표집'], ...}
```

## 알려진 한계

- `atomic_text` 71,460장 중 454장은 한글이 아닌 텍스트(영문/숫자 등)입니다.

## 이번 릴리즈에서 제외한 것

같은 프로젝트에서 생성된 아래 유형들은 이번 릴리즈에는 포함하지 않았습니다.

- `diagram`의 초기 버전(1,000장, `gen1_shlim/ko_diagrams`) — 프롬프트에 다이어그램 제목만
  있고 실제 렌더링된 라벨 전체가 없어 `target_text` 품질이 개선 버전(8,000장)과 다름. 이미지
  자체는 마스터(`qwen_image_2512/`)에 남아있어 필요하면 다시 추가 가능.
- `text_overlay_illustration`(5,000장), `text_overlay_photoreal`(13,047장) — 카툰/포토리얼
  배경 위 텍스트 오버레이. 73%가 영문 텍스트라 "한글 렌더링" 목적과는 결이 다름.
- **`infographic`(2,247장) — 이미지 자체는 이 릴리즈에 포함하지 않음.** GPT/OpenAI Codex
  구독의 이미지 생성 기능으로 만든 산출물이 전량이라, 그 출력물로 (OpenAI가 아닌) 다른
  모델을 학습시키는 데 재배포하는 것이 해당 서비스 이용약관과 상충할 수 있다고 판단했습니다.
  대신 아래에 **생성 방법론만** 문서로 남겨, 필요한 사람이 자신의 계정으로 직접 재현할 수
  있게 했습니다 (재현된 이미지는 재현한 사람과 해당 서비스 간의 이용관계이지, 이 데이터셋이
  재배포하는 것이 아닙니다).

### `infographic` 재현 방법 (참고용 — 이미지 미포함)

비교형/프로세스형/타임라인형/계층형/관계형/통계형/기타 도표형 등 자유 레이아웃의 복합
인포그래픽. 두 갈래로 생성되었습니다.

1. LLM이 도메인(academic/business/it/operations/policy/daily_civic 등)별 다이어그램 구조
   (제목·노드·라벨)를 먼저 설계 → 그 구조를 프롬프트로 변환해 이미지 생성.
2. 별도 생성기가 주제·요소 수·정보 밀도·레이아웃 문법·팔레트를 프로그램적으로 다양화한
   매니페스트를 만들고, OpenAI Codex 구독(이미지 생성 기능)으로 실제 이미지를 생성.

두 경로 모두 "프롬프트에 인용부호로 명시된 문자열만 정확히 렌더링" 규칙을 강제해, 재현할
경우 `target_text`(정답 텍스트 리스트) 추출도 100% 가능합니다. 예시 프롬프트:

> `16:9 가로형 한국어 프로세스형 인포그래픽. 인포그래픽 유형: 프로세스형. 제목은 "세포 관찰 과정". 순서대로 정확히 5개 단계 배치: 1번 "표본 채취"; 2번 "염색 준비"; ...`

라벨에 쓰인 어휘 자체는 `atomic_text`/`diagram`과 동일한 글리프 커버리지 기준 어휘 풀을
공유합니다 (위 `atomic_text` 참고).

## 버전

이 릴리즈는 `manifest.json`에 기록된 버전을 따릅니다 (`version` 필드). 데이터가 추가/변경되면
새 버전으로 관리됩니다.
