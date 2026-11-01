---
language:
- ko
- en
license: other
license_name: mixed-source-licenses
license_link: https://huggingface.co/datasets/lukakuma/minion-agent-sft-v1/blob/main/README.md
task_categories:
- text-generation
tags:
- function-calling
- tool-use
- web-agent
- korean
- sft
pretty_name: Minion Agent SFT v1
size_categories:
- 1K<n<10K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
  - split: validation
    path: data/validation.jsonl
extra_gated_prompt: 연구 목적의 실험 데이터입니다. 사용 목적을 적어 주시면 검토 후 승인합니다.
extra_gated_fields:
  소속: text
  사용 목적: text
---

# Minion Agent SFT — v1

한국어 웹 에이전트용 소형 모델(Minion GRPO)을 SFT/LoRA 로 추가학습하기 위한 데이터 **v1** 입니다.
다른 버전: [v2](https://huggingface.co/datasets/lukakuma/minion-agent-sft-v2), [v5](https://huggingface.co/datasets/lukakuma/minion-agent-sft-v5)

## 구성

| split | 행 수 |
|---|---:|
| train | 5,000 |
| validation | 500 |

| split | 출처 | `source` (provenance) | 행 수 |
|---|---|---|---:|
| train | Codex 합성 (DOM·위임·도구 호출) | `synthetic` | 5,000 |
| validation | Codex 합성 (DOM·위임·도구 호출) | `synthetic` | 500 |

Codex 로 생성한 **한국어 합성 데이터만** 담은 첫 버전입니다. 외부 공개 데이터는 섞지 않았습니다.

## 만든 방법

### 1. 시나리오 계열(family) 설계 — 생성 전에 고정

먼저 **325개 시나리오 계열**의 유형·split·도메인을 정해 두고 생성했습니다. 서로 다른 split 은 도메인(사이트 종류)이 겹치지
않게 나눴고, 한 계열의 변형은 모두 같은 split 에 들어갑니다.

| 유형 | 내용 | train 계열 | validation 계열 | test 계열 (미공개) |
|---|---|---:|---:|---:|
| DOM 실행 | DOM 관측을 보고 목표에 맞는 행동 후보 하나를 고름 (`route: execute`) | 150 | 15 | 30 |
| 위임 | 관측만으로 판단할 수 없거나 맞는 후보가 없을 때 넘김 (`route: delegate`) | 50 | 5 | 10 |
| 도구 호출 | 제공된 함수 정의(2~3개)로 한국어 요청을 처리하는 호출 생성 | 50 | 5 | 10 |
| **합계** | | **250** | **25** | **50** |

### 2. 계열당 20개 변형 → 행 수

계열마다 **변형 20개**를 만들었습니다. 변형은 목표 문장의 항목 값, 타깃·후보 ID, 후보 순서를 바꾸고 정답을 그에 맞게 다시
연결한 것입니다. 이름·값이 바뀌어도 같은 다음 행동이 정답인 시나리오만 허용했습니다.

| 유형 | train | validation |
|---|---:|---:|
| DOM 실행 | 150 × 20 = 3,000 | 15 × 20 = 300 |
| 위임 | 50 × 20 = 1,000 | 5 × 20 = 100 |
| 도구 호출 | 50 × 20 = 1,000 | 5 × 20 = 100 |
| **합계** | **5,000** | **500** |

따라서 5,000개는 독립적인 원본 시나리오 5,000개가 아니라 **250개 계열의 변형**입니다.
test(50계열 × 20 = 1,000개)는 평가용이라 올리지 않았습니다.

### 3. 자동 검수

1. Codex 가 계열의 blueprint 와 정답을 작성
2. **별도의 Codex 호출**에 정답을 숨기고 계열의 첫·중간·마지막 변형 3개를 풀게 함
3. blind 풀이가 원래 정답과 일치하고 `usable` 판정을 받은 계열만 채택
4. 20개 전체에 대해 관측 ID·후보·타깃 상태·인자·split 을 구조 검사
5. 실패한 계열만 다시 생성(최대 5회), 실패 기록은 모두 보존

사람 검수와 실제 브라우저 실행 검증은 **하지 않았습니다**. DOM 은 실제 사이트에서 수집한 것이 아니라 합성한 compact DOM 입니다.

## 행 예시 구조

- DOM 실행·위임: `system` 지시 / `user` 에 목표·URL·최근 결과·타깃 목록이 든 `gca.dom_decision/v1` JSON /
  `assistant` 에 `gca.dom_choice/v1` JSON (`route`, `candidate_id`). `tools` 는 빈 배열
- 도구 호출: `system`·`user` 요청 / `assistant` 에 도구 호출. `tools` 에 함수 정의 2~3개

## 형식

`data/*.jsonl` (미리보기·`load_dataset` 기본 config)

| 필드 | 타입 | 내용 |
|---|---|---|
| `messages` | list of `{role, content}` | system / user / assistant 대화. 마지막 assistant 의 `content` 가 학습 정답 |
| `tools` | string (JSON) | OpenAI 형식 도구 정의 배열. 도구가 없으면 `"[]"` |

`tools` 는 행마다 파라미터 스키마가 달라 미리보기용 파일에서는 JSON 문자열로 저장했습니다.
학습에 실제로 쓴 원본(`tools` 가 리스트)은 `raw/` 에 그대로 있고 `raw/SHA256SUMS.json` 으로 대조할 수 있습니다.
`raw/provenance.jsonl` 에는 행마다 출처·원본 id·그룹·검수 기록이 있습니다(행 순서는 학습 파일과 다를 수 있음).

```python
import json
from datasets import load_dataset

ds = load_dataset("lukakuma/minion-agent-sft-v1")
row = ds["train"][0]
tools = json.loads(row["tools"])
```

## 출처와 라이선스

- Codex 가 작성한 가상의 한국어 DOM 행동 선택·도구 호출 시나리오 (이 프로젝트에서 생성, 외부 원본 없음)

외부 원본이 없는 Codex 합성 데이터입니다. 행별 생성·검수 기록은 `raw/provenance.jsonl`.

## 한계

- 합성 데이터의 정답은 Codex 의 블라인드 재풀이로만 검수했습니다. 사람 검수·실제 브라우저 실행 검증은 없습니다
- 평가 벤치마크 입력은 학습 데이터에서 제외했지만, 이 데이터로 학습한 모델의 평가 점수는 같은 평가셋을 여러 번 관찰한
  실험 과정에서 나온 것이라 독립 테스트 결과가 아닙니다
- 버전 간 성능 차이를 데이터 구성만 바꾼 통제 실험으로 해석하지 마세요(시작 adapter·학습 설정도 다릅니다)
