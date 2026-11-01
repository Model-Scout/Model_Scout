---
language:
- ko
- en
license: other
license_name: mixed-source-licenses
license_link: https://huggingface.co/datasets/lukakuma/minion-agent-sft-v2/blob/main/README.md
task_categories:
- text-generation
tags:
- function-calling
- tool-use
- web-agent
- korean
- sft
pretty_name: Minion Agent SFT v2
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

# Minion Agent SFT — v2

한국어 웹 에이전트용 소형 모델(Minion GRPO)을 SFT/LoRA 로 추가학습하기 위한 데이터 **v2** 입니다.
다른 버전: [v1](https://huggingface.co/datasets/lukakuma/minion-agent-sft-v1), [v5](https://huggingface.co/datasets/lukakuma/minion-agent-sft-v5)

## 구성

| split | 행 수 |
|---|---:|
| train | 24,110 |
| validation | 850 |

| split | 출처 | `source` (provenance) | 행 수 |
|---|---|---|---:|
| train | SmolTalk smol-constraints 지시 따르기 | `constraints` | 10,000 |
| train | GSM8K 수학 | `math` | 7,110 |
| train | Ko-Agent-Trajectories 도구 호출 | `ko-agent` | 6,000 |
| train | Codex 합성 DOM (v1 코퍼스에서 추출) | `dom` | 1,000 |
| validation | Ko-Agent-Trajectories 도구 호출 | `ko-agent` | 250 |
| validation | SmolTalk smol-constraints 지시 따르기 | `constraints` | 250 |
| validation | GSM8K 수학 | `math` | 250 |
| validation | Codex 합성 DOM (v1 코퍼스에서 추출) | `dom` | 100 |

v1 의 DOM 합성 데이터에 공개 학습 데이터를 섞은 **혼합 데이터**입니다. v1 처럼 DOM 만 학습하면 일반 능력(수학·지시 따르기)이
떨어질 수 있어서, 도구 호출(Ko-Agent)·지시 따르기(SmolTalk constraints)·수학(GSM8K)을 함께 넣었습니다.

## 만든 방법

네 출처를 **같은 순서의 필터**에 통과시킨 뒤, 출처별 **고정 할당량**만큼 무작위(seed 42)로 뽑았습니다.

### 1. 출처별 변환

| 출처 | 가져온 범위 | 변환 |
|---|---|---|
| Ko-Agent | 공개 train shard 중 앞 16개 파일 = 16,000개 대화 | 첫 사용자 요청 → 첫 assistant 도구 호출만 한 쌍으로. system 은 짧은 실행 지시로 바꾸되 사용자 프로필은 유지, 도구 정의는 원본 그대로 |
| SmolTalk constraints | train 34,424개 | 첫 user / assistant 쌍만 (뒤 턴을 정답으로 바꾸지 않음) |
| GSM8K | 공식 train 7,473개 | 문제 → 원본 풀이(`#### 정답` 포함) 그대로 |
| DOM | v1 코퍼스의 DOM 실행·위임 행만 (도구 호출 행은 제외) | v1 과 같은 형식 |

### 2. 제외 필터 (모든 출처 공통, 순서대로)

1. **평가셋 겹침** — GSM8K test, IFEval, ARC-Challenge test, KMMLU test 입력과 이전 평가에 쓴 IFEval 프롬프트,
   총 38,012개의 정규화 해시와 같은 사용자 입력 제외. Ko-Agent 는 평가 split 의 도구 시그니처와 겹치는 것도 제외
2. **중복** — 모든 출처를 통틀어 정규화한 사용자 입력이 이미 나온 것 제외
3. **길이** — Minion 토크나이저 기준 2,048 토큰 초과 제외 (실제 최대 1,877 토큰)

### 3. train / validation 나누기

같은 그룹(같은 원본 대화·같은 프롬프트)은 한 split 에만 들어가도록 **그룹 해시 % 20 == 0 이면 validation**(약 5%),
나머지는 train 후보로 나눴습니다. DOM 은 v1 의 split 을 그대로 따릅니다.

### 4. 출처별 개수가 나온 과정

| 출처 | 원본 | 제외 | 남은 후보 | 할당량 (train / val) | 최종 train | 최종 val |
|---|---:|---|---:|---|---:|---:|
| Ko-Agent | 16,000 | 정답 참조 누락·무효 2,293 · 평가 겹침 49 · 중복 46 | 13,612 | 6,000 / 250 | 6,000 | 250 |
| SmolTalk constraints | 34,424 | 중복 2,478 | 31,946 | 10,000 / 250 | 10,000 | 250 |
| GSM8K | 7,473 | 없음 | 7,473 (train 7,110 · val 363) | 10,000 / 250 | **7,110** | 250 |
| DOM (v1) | 4,000 / 400 | 없음 | 4,000 / 400 | 1,000 / 100 | 1,000 | 100 |
| **합계** | | | | | **24,110** | **850** |

- **constraints 10,000** 은 남은 후보 약 3만 개 중 할당량 10,000 개를 seed 42 로 무작위 추출한 것입니다
- **GSM8K 7,110** 은 할당량(10,000)보다 후보가 적어서 train 후보 **전부**가 들어간 숫자입니다
  (GSM8K train 7,473개 중 해시 분할로 363개가 validation 후보로 빠짐)
- **DOM 1,000** 은 v1 train 의 DOM 실행 3,000 + 위임 1,000 중에서 뽑았고, 결과는 실행 743 · 위임 257 입니다
  (validation 100 = 실행 77 · 위임 23)
- 최종 train/validation 파일 안의 행 순서는 seed 42 로 섞었습니다

공개 데이터의 정답은 원본 라벨 그대로이며, 새로 사람이 검수하거나 실제 도구를 실행해 확인하지 않았습니다.
의미가 같은 다른 표현의 중복까지 제거했다고 주장하지 않습니다.

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

ds = load_dataset("lukakuma/minion-agent-sft-v2")
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
