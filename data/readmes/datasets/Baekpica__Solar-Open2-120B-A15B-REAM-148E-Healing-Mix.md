---
license: other
license_name: upstage-solar-license
task_categories:
- text-generation
language:
- en
- ko
- ja
- pt
- hi
pretty_name: Solar-Open2-120B REAM 148E Healing Mix
size_categories:
- 10K<n<100K
tags:
- solar
- solar-open2
- ream
- reap
- healing
- moe
- expert-merging
configs:
- config_name: mixed
  default: true
  data_files:
  - split: train
    path: data-mixed/train-*.parquet
- config_name: long
  data_files:
  - split: train
    path: data-long/train-*.parquet
---

# Solar-Open2-120B-A15B-REAM-148E Healing Mix

`Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16` 의 REAM 병합 손상을 복구하기 위한
비공개 결정론적 힐링 믹스입니다. 모든 시퀀스는 **Solar Open 2 chat template로
사전 렌더·토크나이즈**되어 있고 **assistant 턴에만 loss 마스크**가 열려 있습니다.

## 왜 만들었나

계보는 `upstage/Solar-Open2-250B` → REAP(184E) → REAM(148E) 입니다.
REAM 이후 고정 프롬프트 A/B 관찰에서 다음이 확인됐습니다.

- 한국어 응답에서 **반복 붕괴** (예: 동일 3-gram이 출력의 88.6% 차지)
- 지시 준수·포맷 이탈, typo
- 도메인·언어에 따라 편차가 큰 열화 (일부 프롬프트는 정상)

손상은 **라우터**(184→148 centroid slice)와 **병합된 expert 가중치**에 집중돼
있으므로, 지식 추가가 아니라 **capability 회복**을 목표로 SFT 데이터만 사용했습니다.
RL·GenRM 계열은 의도적으로 제외했습니다 (SFT 이후 단계이며 style만 바꾸고
capability는 돌아오지 않을 위험).

## 구성

| 버킷 | 소스 | 행 | 토큰 | 실제 비중 | 목표 | 길이 min/med/max | 목적 |
|---|---|---:|---:|---:|---:|---:|---|
| `if_chat` | nvidia/Nemotron-SFT-Instruction-Following-Chat-v2 | 10,623 | 15.40M | 22.0% | 22% | 48/1245/4096 | instruction following · 포맷 · completeness |
| `cascade1_reasoning` | nvidia/Nemotron-Cascade-SFT-Stage-1 | 5,404 | 11.20M | 16.0% | 16% | 149/1897/4096 | RL 이전 reasoning (general/science/math/code) |
| `cascade2_reasoning` | nvidia/Nemotron-Cascade-SFT-Stage-2 | 5,948 | 11.20M | 16.0% | 16% | 50/1687/4095 | instruction following · tool call · SWE reasoning |
| `ko` | nvidia/Nemotron-SFT-Multilingual-v2 (ko) | 5,407 | 11.20M | 16.0% | 16% | 179/1995/4095 | 한국어 capability 회복 |
| `multilingual_other` | nvidia/Nemotron-SFT-Multilingual-v2 (ja/pt/hi) | 4,009 | 8.40M | 12.0% | 12% | 172/1971/4096 | 일본어·포르투갈어·힌디어 |
| `finance` | nvidia/Nemotron-SpecializedDomains-Finance-v1 | 647 | 4.21M | 6.0% | 6% | 3863/6505/8192 | 표·수치·금융 분석 (장문) |
| `swe_agentic` | nvidia/Nemotron-SFT-SWE-v2 | 1,407 | 4.20M | 6.0% | 6% | 783/3071/4096 | 에이전틱 코딩 (OpenAI tool 포맷) |
| `code_algo` | nvidia/Nemotron-SFT-Competitive-Programming-v2 | 1,796 | 4.20M | 6.0% | 6% | 336/2117/4096 | 알고리즘 추론 · SQL |

- 총 행: **35,241**
- 총 토큰: **70,012,295** (70.01M)
- 학습 대상(assistant) 토큰: **54,421,225** (77.7%)
- 길이 min/median/p90/max: **48 / 1,782 / 3,653 / 8,192**
- 중복 행: **33** (0.09%)
- 시드: `42`

### 길이 정책

`finance` 를 제외한 전 버킷은 **최대 4,096 토큰**입니다.
`Nemotron-SpecializedDomains-Finance-v1` 은 median 32,770 토큰의 장문 문서라
4,096 캡에서 표본이 전량 탈락했습니다. 이 버킷만 **8,192 캡**으로 따로 빌드한 뒤
목표 비중(6%)에 맞춰 다운샘플했습니다.

`Nemotron-SFT-SWE-v2/swe.jsonl` 은 median 44,710 토큰(110 턴)이고 system+tools
블록만으로도 8,192를 넘겨 turn 단위 절단으로도 예산에 맞출 수 없었습니다.
해당 버킷은 `agentless.jsonl` 만으로 채웠습니다.

### 다국어

`Nemotron-SFT-Multilingual-v1` 에는 **한국어가 없습니다** (de/es/fr/it/ja/zh).
한국어는 전량 `Nemotron-SFT-Multilingual-v2` (hi/ja/ko/pt)에서 가져왔습니다.

## `long` config — 장문맥 확장

`mixed` 와 **행 단위로 겹치지 않는** 4,097~16,341 토큰 전용 세트입니다.
소스 파일에서 `mixed` 빌드가 읽은 줄 수 이후 구간만 사용했고, `input_ids`
해시 대조로 중복 0건을 확인했습니다.

- 행: **4,291** / 토큰 **32,061,182** / assistant **19,270,528** (60.1%)
- 길이 min/median/p90/max: **4,097 / 6,771 / 12,142 / 16,341**
- 최소 길이 필터: 8K 파트 4,097 · 16K 파트 8,193

| 버킷 | 행 |
|---|---:|
| finance | 1,206 |
| swe_agentic | 899 |
| cascade1_reasoning | 674 |
| code_algo | 444 |
| cascade2_reasoning | 429 |
| ko | 424 |
| multilingual_other | 215 |

`Nemotron-SFT-SWE-v2/swe.jsonl` 은 median 44,710 토큰이고 system+tools 블록만으로
8K를 넘겨 16,384 캡에서도 한 건도 통과하지 못했습니다. 이 버킷은 전량
`agentless.jsonl` 입니다.

assistant 비율이 `mixed`(77.7%)보다 낮은 60.1%인 이유는 finance 때문입니다 —
장문 금융 문서는 대부분이 입력이고 답변이 짧아 16K 파트의 finance target 비율은
11% 수준입니다. 장문맥 학습의 구조적 특성이며, 예산은 **assistant 토큰 기준**으로
잡아야 합니다.

## 포맷

### `data-mixed/` (parquet, 기본 config)

| 컬럼 | 타입 | 설명 |
|---|---|---|
| `input_ids` | `list<int32>` | Solar Open 2 토크나이저 (vocab 196,608) |
| `labels` | `list<int32>` | `-100` 은 loss 제외 |
| `bucket` | `string` | 위 표의 버킷 이름 |

### `healing_mix_35241_ragged.safetensors`

패딩 없이 저장한 동일 데이터입니다. 행 `i` 는
`input_ids[offsets[i]:offsets[i+1]]` 입니다.

| 텐서 | dtype | shape |
|---|---|---|
| `input_ids` | int32 | `[70,012,295]` |
| `labels` | int32 | `[70,012,295]` |
| `offsets` | int64 | `[35,242]` |

SHA-256: `input_ids` `c7ed9b39d2435c0971cacbf56aa20d2c998a2d6d956b9e26235f8077b07a846e`, `labels` `0b202a4bc73b894a529791d229e53aaee57cb915ee480e68fdc41376599f2744`

## 렌더링 규약

`chat_template.jinja` 의 기본값을 그대로 따릅니다
(`provider_system_prompt=false`, `think_render_option="interleaved"`,
`add_generation_prompt=false`).

- system/tools: `<|im:start|>system<|im:content|>## System Prompt … ## Tools …<|im:end|>`
- user: `<|im:start|>user<|im:content|>…<|im:end|>`
- assistant: `<|im:start|>assistant<|im:content|><|think:start|>…<|think:end|>…<|im:end|>`
- tool call: `<|tool_call:start|>name\n<|tool_arg:start|>k<|tool_arg:value|>v<|tool_arg:end|>\n<|tool_call:end|>`
- tool 응답: `<|im:start|>tool<|im:content|><|tool_response:start|>…<|tool_response:end|>\n<|im:end|>`

`interleaved` 규약상 **마지막 user 메시지 이전의 assistant 턴은 reasoning이
비워집니다**(`<|think:start|><|think:end|>`). 추론 시 동작과 동일합니다.

**loss 마스크는 `<|im:start|>assistant<|im:content|>` 직후부터 `<|im:end|>\n`
까지**입니다. think 블록과 tool call도 학습 대상이며, 종료 토큰을 배우도록
`<|im:end|>` 를 포함합니다.

### 소스 방언 정규화

| 소스 방언 | 처리 |
|---|---|
| `reasoning_content` / `reasoning` 필드 | 그대로 think 블록으로 |
| `<think>…</think>` 인라인 (Cascade) | 추출해 think 블록으로 |
| OpenAI `tool_calls` (SWE-v2) | Solar tool-call 문법으로 변환, `arguments` JSON 문자열 파싱 |
| Qwen 인라인 `<tool_call>{…}</tool_call>` | 파싱 후 동일 변환 |
| Qwen system `<tools>…</tools>` | OpenAI tool 스펙으로 추출, system 텍스트에서 제거 |
| `<tool_response>…</tool_response>` | 래퍼 제거 |
| `tool_call_id` 누락 | 직전 assistant tool_call 순서로 매칭, 실패 시 행 폐기 |

## 검증

`scripts/verify_renderer.py` 는 수동 렌더러 출력이 `tokenizer.apply_chat_template`
(jinja) 결과와 **바이트 단위로 일치**하는지 확인합니다. 7개 소스에서 뽑은
318개 표본이 전부 일치했고, 조각별 인코딩 concat이 전체 인코딩과 동일함도
확인했습니다.

`scripts/package_dataset.py` 의 감사는 다음을 검사합니다: offsets 정합성,
토큰 ID 범위, **마스킹되지 않은 label == input_ids**, 행당 최소 학습 토큰,
최소 길이, 중복 행, 텐서 SHA-256. 결과는 `audit.json` 에 있고 이 릴리스는
`passed: true` 입니다.

## 재현

```bash
uv pip install "git+https://github.com/UpstageAI/transformers.git@v5.14.1-solar-open2"
python scripts/build_healing_mix.py --total-tokens 70e6 --workers 128 \
  --cap-per-file 600000 --chunk-lines 4096 --out ./healing_mix
python scripts/build_healing_mix.py --total-tokens 70e6 --only finance \
  --max-len 8192 --cap-per-file 200000 --out ./healing_finance
python scripts/package_dataset.py
```

## 라이선스와 출처

파생 학습 데이터는 각 NVIDIA Nemotron 소스 데이터셋의 라이선스를 따릅니다
(대부분 CC-BY-4.0 / ODC-By). 토크나이저와 chat template은
`upstage/Solar-Open2-250B` 에서 왔으며 Upstage Solar License가 적용됩니다.
비공개 저장소이며 재배포 시 원 라이선스를 확인해야 합니다.

## 연관 아티팩트

| 역할 | 저장소 |
|---|---|
| 원본 | [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B) |
| REAP parent | [Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16](https://huggingface.co/Baekpica/Solar-Open2-148B-A15B-REAP-184E-BF16) |
| REAM (힐링 전) | [Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16](https://huggingface.co/Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16) |
| 힐링 BF16 | Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2 |
| 힐링 NVFP4A16 | Baekpica/Solar-Open2-120B-A15B-REAM-148E-NVFP4-v2 |
| REAM 구현 | [Baekpica/solar-ream](https://github.com/Baekpica/solar-ream) |
