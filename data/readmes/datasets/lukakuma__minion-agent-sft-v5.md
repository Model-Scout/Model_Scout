---
language:
- ko
- en
license: other
license_name: mixed-source-licenses
license_link: https://huggingface.co/datasets/lukakuma/minion-agent-sft-v5/blob/main/README.md
task_categories:
- text-generation
tags:
- function-calling
- tool-use
- web-agent
- korean
- sft
pretty_name: Minion Agent SFT v5
size_categories:
- 10K<n<100K
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

# Minion Agent SFT — v5

한국어 웹 에이전트용 소형 모델(Minion GRPO)을 SFT/LoRA 로 추가학습하기 위한 데이터 **v5** 입니다.
다른 버전: [v1](https://huggingface.co/datasets/lukakuma/minion-agent-sft-v1), [v2](https://huggingface.co/datasets/lukakuma/minion-agent-sft-v2), [v6](https://huggingface.co/datasets/lukakuma/minion-agent-sft-v6)

## 구성

| split | 행 수 |
|---|---:|
| train | 10,187 |
| validation | 970 |

| split | 출처 | `source` (provenance) | 행 수 |
|---|---|---|---:|
| train | Ko-Agent-Trajectories 도구 호출 | `ko-agent` | 3,684 |
| train | Codex 합성 도구 호출 (v5 신규 1·2차, 시나리오당 1개) | `codex-tools-new` | 2,003 |
| train | SmolTalk smol-constraints 지시 따르기 | `constraints` | 2,000 |
| train | GSM8K 수학 | `math` | 2,000 |
| train | Codex 합성 DOM 실행·위임 (v1 코퍼스, 계열당 2개) | `dom` | 400 |
| train | Codex 합성 도구 호출 (v1 코퍼스, 계열당 2개) | `codex-tools-existing` | 100 |
| validation | SmolTalk smol-constraints 지시 따르기 | `constraints` | 250 |
| validation | GSM8K 수학 | `math` | 250 |
| validation | Ko-Agent-Trajectories 도구 호출 | `ko-agent` | 220 |
| validation | Codex 합성 도구 호출 (v5 신규 1·2차, 시나리오당 1개) | `codex-tools-new` | 200 |
| validation | Codex 합성 DOM 실행·위임 (v1 코퍼스, 계열당 2개) | `dom` | 40 |
| validation | Codex 합성 도구 호출 (v1 코퍼스, 계열당 2개) | `codex-tools-existing` | 10 |

**같은 내용의 반복을 없애고 시나리오 다양성을 높인** 버전입니다. 합성 도구 호출 시나리오는 시나리오당 1개이고,
Ko-Agent·지시 따르기·수학 데이터는 서로 가장 다른 행부터 골랐습니다.

## 만든 방법

### 1. 신규 Codex 도구 호출 시나리오 (`codex-tools-new`) — 두 생성기

| 생성기 | 개수 | 방식 |
|---|---|---|
| 1차 (`sparse_tool_corpus`) | train 약 1,000 | 기술 20종 × 도메인 10 × 업무 의도 10 계획. 원래 `{item}` 자리에 "고정 이름 + 도메인 명사"가 들어가 어색했기 때문에, Codex 에게 각 자리의 역할(메뉴명·상품명·문의 제목 등)에 맞는 이름을 따로 받아 다시 펼쳤습니다. 이름 뒤 조사도 맞췄습니다 |
| 2차 (`scenario_corpus`) | train 약 1,000 · validation 약 200 | 기술 **24종**(단위 변환, 비슷한 도구 중 고르기, 한글 숫자, 기준일 상대 날짜 추가) × 새 도메인 **train 25 / validation 5** × 말투 12 × 업무 의도 15 × 제공 도구 **1~4개**(쓰지 않는 도구는 비슷한 방해 도구). 값은 Codex 가 직접 구체적으로 작성 |

모든 출처 공통 정답 형식 검사: 도구 호출이 파싱되고, 제공된 도구를 부르며, 그 도구의 JSON Schema(Draft 2020-12)를 만족해야 합니다. DOM 정답은 gca.dom_choice/v1 형식이고 실제 후보를 가리켜야 합니다.

합성 데이터 검수: 스키마 타입·enum·필수 인자·기술별 규칙 검사 → 정답을 숨긴 별도 Codex 호출이 다시 풀어 일치한 것만 채택.
2차 생성기는 요청에 없는 문자열 인자(덧붙이거나 바꿔 쓴 값)를 코드로 거절하고, 이전 모든 코퍼스와 시나리오 요약이 비슷하거나(단어 bigram Jaccard ≥ 0.5) 도구 이름이 같은 것을 거절합니다.

### 2. 나머지 출처

| 출처 (`source`) | 가져온 방법 |
|---|---|
| `ko-agent` | v3 혼합 데이터의 Ko-Agent 31,929행(공개 train 128 shard 중 난도 L1/L2·제공 도구 1개 이하)중 **정답의 모든 인자가 요청 문구·enum·기본값·불리언으로 정해지는 행**(13,150행)만 남긴 뒤, 정답(호출 이름+인자)이 서로 다른 행 **전부**. 배경지식(종목코드·지역 추론 등)이 필요한 행은 제외 |
| `dom`, `codex-tools-existing` | v1 코퍼스 250계열(DOM 실행 150·위임 50·도구 호출 50)에서 **계열당 2개**. 각 행은 역할에 맞는 서로 다른 이름으로 다시 펼침 |
| `constraints`, `math` | v3 혼합 데이터의 후보(constraints 6,000 · GSM8K 4,000)에서 요청 문장과 답변이 서로 가장 다른 것부터 train 각 **2,000개**, validation 은 전부 |

### 3. 제외 필터 (모든 출처 공통)

평가셋 입력과 겹치는 것(v2 와 같은 벤치마크 목록 + Ko-Agent 평가 split 시그니처), 정규화한 사용자 입력이 중복인 것,
2,048 토큰 초과를 제외했습니다. 같은 그룹이 train 과 validation 에 함께 들어가면 실행을 중단하도록 검사합니다.

## 이 데이터로 학습한 모델의 평가

| 모델 | 스키마 | 도구명·개수 | 인자 엄격 | **주어진 문항 엄격** | 기본값 보완 | IFEval | GSM8K | DOM 선택 | 합성 도구 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minion_grpo | 89.2% | 81.2% | 11.4% | **14.9%** | 26.2% | 53.2% | 71.1% | 0.0% | 20.5% |
| exaone | 98.8% | 83.8% | 26.8% | **41.2%** | 34.6% | 75.4% | 79.8% | 0.0% | 73.5% |
| v1 | 94.8% | 82.4% | 16.0% | **25.2%** | 34.0% | 51.9% | 69.5% | 98.6% | 90.0% |
| v2 | 99.6% | 86.2% | 58.2% | **64.9%** | 63.8% | 53.0% | 53.6% | 55.6% | 20.0% |
| v5 | 99.0% | 83.8% | 36.0% | **58.4%** | 42.8% | 51.4% | 54.6% | 98.1% | 30.0% |

vLLM 백엔드. Ko-Agent 500 (주어진 문항 n=262: 정답이 요청·enum·기본값·불리언으로만 정해지는 문항), IFEval prompt-level strict, GSM8K flexible-extract, 합성 고정 test 1,000 (DOM 800 / 도구 200).


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

ds = load_dataset("lukakuma/minion-agent-sft-v5")
row = ds["train"][0]
tools = json.loads(row["tools"])
```

## 출처와 라이선스

- Codex 가 작성한 가상의 한국어 DOM 행동 선택·도구 호출 시나리오 (이 프로젝트에서 생성, 외부 원본 없음)
- [Ko-Agent-Trajectories-1.0](https://huggingface.co/datasets/taejoon89/Ko-Agent-Trajectories-1.0) (taejoon89, rev `58419e5`, **CC BY 4.0**) — train split 만 사용
- [SmolTalk smol-constraints](https://huggingface.co/datasets/HuggingFaceTB/smoltalk) (HuggingFaceTB, rev `5feaf2f`, **Apache 2.0**) — train split
- [GSM8K](https://huggingface.co/datasets/openai/gsm8k) (OpenAI, rev `740312a`, **MIT**) — 공식 train split 만

공개 데이터는 원본 라이선스를 따르며, 이 레포가 원본 내용을 다시 라이선스하지 않습니다. 행별 출처는 `raw/provenance.jsonl`.

## 한계

- 합성 데이터의 정답은 Codex 의 블라인드 재풀이로만 검수했습니다. 사람 검수·실제 브라우저 실행 검증은 없습니다
- 평가 벤치마크 입력은 학습 데이터에서 제외했지만, 이 데이터로 학습한 모델의 평가 점수는 같은 평가셋을 여러 번 관찰한
  실험 과정에서 나온 것이라 독립 테스트 결과가 아닙니다
- 버전 간 성능 차이를 데이터 구성만 바꾼 통제 실험으로 해석하지 마세요(시작 adapter·학습 설정도 다릅니다)
