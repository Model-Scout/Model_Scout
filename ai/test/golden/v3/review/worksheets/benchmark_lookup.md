# 골든셋 v3 검수 워크시트 — benchmark_lookup (벤치마크 조회)

> 상태: **초안 + 전수 스캔 + 검수 준비 완료**. 아래 점수는 Claude 의 제안이며 정답이 아니다.
>
> 판정 입력: `python test/golden/v3/tools/judge.py <query_id> <model_id> --decision approve|2|1|exclude|hold --reason "…" --by <이름>`

## bl01 — KMMLU 점수가 공개된 한국어 모델들을 보고 싶어요. 같은 기준으로 적힌 점수끼리만 비교해 주세요.

- 사용자 의도: KMMLU 점수 비교
- persona / 표현: researcher / 기술형 · 난이도 hard
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: KMMLU 점수(score)가 저장된 원본 모델
- **1점 기준**: 점수는 있지만 비교 가능성이 낮거나 변환본
- 비교 기준: dataset `^\W*kmmlu\W*(\(ko, knowledge\))?\s*$` · metric `^score$` kmmlu (chat CoT)·kmmlu-direct·KMMLU-Pro 는 다른 평가 설정이라 제외

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 7 | 0 | 4,010 | 0 | 7 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 벤치마크 결과 없음 (`no_benchmark_results`) | 3,723 | codefuse-ai/F2LLM-v2-330M, legraphista/Mistral-Small-Instruct-2409-IMat-GGUF, lmstudio-community/LFM2.5-2.6B-MLX-4bit |
| 다른 benchmark dataset 만 있음 (`other_benchmark_dataset`) | 287 | LiquidAI/LFM2-2.6B, baseten-admin/multilingual-e5-large-instruct-cls, sionic-ai/comsat-embed-ko-8b-preview |

같은 canonical family 후보가 3개 이상: Qwen/Qwen3.6-35B-A3B 3

#### 1. [FINAL-Bench/Darwin-4B-David](https://huggingface.co/FINAL-Bench/Darwin-4B-David) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | FINAL-Bench/Darwin-4B-David (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.996 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.89 |
| 벤치마크 근거 | KMMLU / score = 48.46 (self_reported=True, safe_same_source, readme:table[3].row[136].column[3]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model is designed for text generation tasks. |
| README 인용 | pipeline_tag: text-generation library_name: transformers model-index: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 95248bc713d35b3616b865d64714859e59225de9 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [NCSOFT/VARCO-VISION-2.0-1.7B](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-1.7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.124 / 40960 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit, readme:korean_explicit_phrase |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 3.96 |
| 벤치마크 근거 | KMMLU / score = 10.4 (self_reported=True, safe_same_source, readme:table[4].row[104].column[4]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | All inputs in a batch must have the same modality structure—for example, text-only with text-only, single-image with single-image, and multi-image with multi-image—to ensure correct batch inference. |
| README 인용 | <details> <summary>Batch inference</summary> All inputs in a batch must have the same modality structure—for example, text-only with text-only, single-image with single-image, and multi-image with multi-image—to ensure correct batch inferen… |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | ed09f37445518b1564d1ef3c6e26fbd7c1b2c818 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [NCSOFT/VARCO-VISION-2.0-14B](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-14B) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-14B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 15.196 / 40960 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit, readme:korean_explicit_phrase |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 28.3 |
| 벤치마크 근거 | KMMLU / score = 57.5 (self_reported=True, safe_same_source, readme:table[4].row[104].column[5]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | All inputs in a batch must have the same modality structure—for example, text-only with text-only, single-image with single-image, and multi-image with multi-image—to ensure correct batch inference. |
| README 인용 | <details> <summary>Batch inference</summary> All inputs in a batch must have the same modality structure—for example, text-only with text-only, single-image with single-image, and multi-image with multi-image—to ensure correct batch inferen… |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 3a4fc8d47ec642e87ad9bb65d41f39f062270950 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [hossain0909/Keural-Nova-v1.2-experimental](https://huggingface.co/hossain0909/Keural-Nova-v1.2-experimental) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.6-35B-A3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 35.952 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 66.97 |
| 벤치마크 근거 | **KMMLU** (ko, knowledge) / score = 63.5 (self_reported=True, safe_same_source, readme:table[1].row[55].column[5]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Data includes a cleaned, balanced Korean/English/code/replay mix. |
| README 인용 | - **Data:** ~162k examples — a cleaned, balanced Korean/English/code/replay mix |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 0535e93ffa81ff5f60c5048e470db752d8000d69 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [mkd-ai-dev/Keural-Nova-v1.2-experimental](https://huggingface.co/mkd-ai-dev/Keural-Nova-v1.2-experimental) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.6-35B-A3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 35.952 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 66.97 |
| 벤치마크 근거 | **KMMLU** (ko, knowledge) / score = 63.5 (self_reported=True, safe_same_source, readme:table[1].row[55].column[5]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Designed for text generation tasks. |
| README 인용 | pipeline_tag: text-generation library_name: transformers tags: |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | c3332b8d9c5eaa5e061330d2a530ffd5bf23fe80 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [mkd-dev/Keural-Nova-v1.2-experimental](https://huggingface.co/mkd-dev/Keural-Nova-v1.2-experimental) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.6-35B-A3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 35.952 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 66.97 |
| 벤치마크 근거 | **KMMLU** (ko, knowledge) / score = 63.5 (self_reported=True, safe_same_source, readme:table[1].row[55].column[5]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Data includes a cleaned, balanced Korean/English/code/replay mix. |
| README 인용 | - **Data:** ~162k examples — a cleaned, balanced Korean/English/code/replay mix |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 2c6ed6402f0f306c0970c97bd169ed993188fe0a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [trillionlabs/Trida-7B](https://huggingface.co/trillionlabs/Trida-7B) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | trillionlabs/Trida-7B (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.527 / 4096 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit, readme:korean_explicit_phrase |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.02 |
| 벤치마크 근거 | KMMLU / score = 50.28 (self_reported=True, safe_same_source, readme:table[2].row[175].column[2]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Trida-7B is designed for text generation tasks. |
| README 인용 | pipeline_tag: text-generation library_name: transformers extra_gated_fields:   Full Name: text   Email: text   Organization: text --- |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | c37755e81222de0aff69ee481f5299a99928b105 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## bl02 — GPQA Diamond 정확도(accuracy)가 README 에 적힌 모델을 찾아 줘.

- 사용자 의도: GPQA Diamond accuracy 비교
- persona / 표현: ml_engineer / 기술형 · 난이도 hard
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: GPQA Diamond accuracy 점수가 저장된 원본
- **1점 기준**: 점수가 있으나 변환본이거나 비교 가능성 낮음
- 비교 기준: dataset `gpqa.?diamond` · metric `^accuracy$` metric 이 score 로만 적힌 GPQA Diamond 결과는 다른 metric 으로 본다

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 13 | 0 | 4,004 | 0 | 13 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 벤치마크 결과 없음 (`no_benchmark_results`) | 3,723 | CohereLabs/aya-expanse-8b, DavidAU/Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning, mradermacher/YanoljaNEXT-Rosetta-20B-i1-GGUF |
| 다른 benchmark dataset 만 있음 (`other_benchmark_dataset`) | 274 | EleutherAI/polyglot-ko-12.8b, Goekdeniz-Guelmez/Josiefied-Qwen2.5-7B-Instruct-abliterated-v2, NC-AI-consortium-VAETKI/VAETKI |
| 같은 dataset 이지만 다른 metric (`other_metric`) | 7 | ATH-MaaS/Marco-Nano-Instruct, FINAL-Bench/Darwin-27B-RSI, arcee-ai/Trinity-Large-Preview |

#### 1. [21world/Darwin-35B-A3B-Opus](https://huggingface.co/21world/Darwin-35B-A3B-Opus) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Jackrong/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 35.952 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 66.97 |
| 벤치마크 근거 | GPQA Diamond / accuracy = 90.0 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model improves inference throughput with multi-token prediction. |
| README 인용 | - **Multi-Token Prediction**: Improved inference throughput |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 2eab6a37576dcfc8607c2c22af57596bfb8dbd30 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [FINAL-Bench/Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | FINAL-Bench/Darwin-180B-RSI (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 180.0 / 262144 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 335.28 |
| 벤치마크 근거 | GPQA Diamond / accuracy = 94.44 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | It knows before it answers |
| README 인용 | \| `ztc/usage.py` \| minimal example \| |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | a9d26c2db1eb6366fe6a2c559df8c95e9e082692 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [FINAL-Bench/Darwin-218B-Delphi](https://huggingface.co/FINAL-Bench/Darwin-218B-Delphi) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | CohereLabs/command-a-plus-05-2026-bf16 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 218.75 / 5000000 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 407.46 |
| 벤치마크 근거 | GPQA Diamond / accuracy = 88.1 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model is designed for chemistry-related tasks, leveraging high-quality chemistry CoT examples across multiple sub-domains. |
| README 인용 | library_name: transformers pipeline_tag: text-generation tags: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 9d828785ff796d063bc8c19d7af334865e858605 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [FINAL-Bench/Darwin-28B-Opus](https://huggingface.co/FINAL-Bench/Darwin-28B-Opus) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | FINAL-Bench/Darwin-28B-Opus (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 27.781 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 51.75 |
| 벤치마크 근거 | GPQA Diamond / accuracy = 88.89 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Recommended for text generation tasks. |
| README 인용 | library_name: transformers pipeline_tag: text-generation tags: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 12bb42033c8c6aaf6bb43d2c42c347fb07594fce |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [FINAL-Bench/Darwin-28B-REASON](https://huggingface.co/FINAL-Bench/Darwin-28B-REASON) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | FINAL-Bench/Darwin-28B-REASON (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 26.896 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 50.1 |
| 벤치마크 근거 | GPQA Diamond / accuracy = 89.39 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model is used in conjunction with the Darwin-DELPHI test-time reasoning engine. |
| README 인용 | **Darwin-DELPHI** is a proprietary test-time engine applied at inference. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | aa4ad8d8d1a949a4404bb4394001a2ef19fcbd7b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [FINAL-Bench/Darwin-31B-Opus](https://huggingface.co/FINAL-Bench/Darwin-31B-Opus) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | FINAL-Bench/Darwin-31B-Opus (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 31.273 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 58.25 |
| 벤치마크 근거 | GPQA Diamond / accuracy = 85.9 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used for question-answering tasks. |
| README 인용 | type: question-answering       name: Question Answering     dataset:       name: GPQA Diamond       type: Idavidrein/gpqa       config: gpqa_diamond     metrics: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 8a08a18086848adc046cd2842b0c7fd072818af2 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [FINAL-Bench/Darwin-36B-Opus](https://huggingface.co/FINAL-Bench/Darwin-36B-Opus) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | FINAL-Bench/Darwin-36B-Opus (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 34.661 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 64.56 |
| 벤치마크 근거 | GPQA Diamond / accuracy = 88.4 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used for generating responses in a conversational format. |
| README 인용 | ## Usage |
| provenance status | verified 13, not_applicable 3, documented 5, unknown 1, inferred 1 |
| revision | ebc6cbeb96b67e47617825134add4a6747f732fc |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [FINAL-Bench/Darwin-398B-JGOS](https://huggingface.co/FINAL-Bench/Darwin-398B-JGOS) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | FINAL-Bench/Darwin-398B-JGOS (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 403.398 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 751.39 |
| 벤치마크 근거 | GPQA Diamond / accuracy = 90.9 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Usage with vLLM for serving the model. |
| README 인용 | ```bash vllm serve FINAL-Bench/Darwin-398B-JGOS --tensor-parallel-size 2 --pipeline-parallel-size 3 --dtype bfloat16 --trust-remote-code ``` |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | c2d610f342280339d89c9a4a9dd6aedbe12bc862 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [FINAL-Bench/Darwin-4B-David](https://huggingface.co/FINAL-Bench/Darwin-4B-David) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | FINAL-Bench/Darwin-4B-David (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.996 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.89 |
| 벤치마크 근거 | GPQA Diamond / accuracy = 85.0 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model is designed for text generation tasks. |
| README 인용 | pipeline_tag: text-generation library_name: transformers model-index: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 95248bc713d35b3616b865d64714859e59225de9 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [FINAL-Bench/Darwin-60B-DUO](https://huggingface.co/FINAL-Bench/Darwin-60B-DUO) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | FINAL-Bench/Darwin-60B-DUO (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 108.35 |
| 벤치마크 근거 | GPQA Diamond / accuracy = 88.38 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Bilingual Korean-English assistants that require both Korean fluency and high-quality English reasoning. |
| README 인용 | - **Bilingual Korean-English assistants** that require both Korean fluency and high-quality English reasoning. |
| provenance status | verified 9, not_applicable 3, documented 5, unknown 6 |
| revision | e1af756470b517cc3b691378a5781acb448cb3c4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [FINAL-Bench/Darwin-9B-NEG](https://huggingface.co/FINAL-Bench/Darwin-9B-NEG) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | FINAL-Bench/Darwin-9B-NEG (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 9.653 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 18.0 |
| 벤치마크 근거 | GPQA Diamond / accuracy = 84.34 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model operates inside a single decoding loop, lifting reasoning accuracy by more than 12 percentage points at 1× inference cost. |
| README 인용 | Unlike external multi-turn iteration (MTI) techniques that require 3×–8× extra inference, NEG operates *inside* the single decoding loop and activates in fewer than 5 % of generation steps, lifting reasoning accuracy **by more than 12 perce… |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 820a39a50d2a40bccd6f244c08edbe4a931bd8e6 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [FINAL-Bench/Darwin-9B-Opus](https://huggingface.co/FINAL-Bench/Darwin-9B-Opus) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | FINAL-Bench/Darwin-9B-Opus (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 9.653 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 17.98 |
| 벤치마크 근거 | GPQA Diamond / accuracy = 82.5 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used for text generation tasks. |
| README 인용 | pipeline_tag: text-generation library_name: transformers model-index: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | e736587b1c85cc597208257fddd3697fef8cef5e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [FINAL-Bench/Ourbox-35B-JGOS](https://huggingface.co/FINAL-Bench/Ourbox-35B-JGOS) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | FINAL-Bench/Ourbox-35B-JGOS (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 34.661 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 64.56 |
| 벤치마크 근거 | GPQA Diamond / accuracy = 86.36 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used for Korean-language reasoning and generation tasks. |
| README 인용 | ```python from transformers import AutoTokenizer, AutoModelForCausalLM import torch  tok = AutoTokenizer.from_pretrained("FINAL-Bench/Ourbox-35B-JGOS", trust_remote_code=True) model = AutoModelForCausalLM.from_pretrained(     "FINAL-Bench/O… |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 11f3a1598fe981752b18ea2e87dc278e525c86ca |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## bl03 — 음성 인식 모델을 고를 때 Common Voice 11.0 WER 를 기준으로 삼으려고 해요. 그 점수가 있는 모델을 알려 주세요.

- 사용자 의도: Common Voice 11.0 WER 비교
- persona / 표현: backend_dev / 혼합형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `tasks` | automatic-speech-recognition | 음성 인식 모델 | 예 |

- **2점 기준**: Common Voice 11.0 WER 가 저장된 원본
- **1점 기준**: 변환본이거나 비교 가능성 낮음
- 비교 기준: dataset `common voice 11` · metric `^wer$`

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 321 | 13 | 0 | 308 | 0 | 13 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 벤치마크 결과 없음 (`no_benchmark_results`) | 281 | handy-computer/whisper-medium-gguf, yeowon/qwen3_asr_1.7b_ko-MLX-4bit, younghan-meta/Voxtral-Mini-4B-Realtime-2602-ExecuTorch-Metal |
| 다른 benchmark dataset 만 있음 (`other_benchmark_dataset`) | 27 | FunAudioLLM/Fun-ASR-MLT-Nano-2512, longlenai-team/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B, sorika-labs/vaani1-lite-asr-turbo |

같은 canonical family 후보가 3개 이상: openai/whisper-base 3, openai/whisper-small 3

#### 1. [RedHatAI/whisper-tiny](https://huggingface.co/RedHatAI/whisper-tiny) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | RedHatAI/whisper-tiny (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.038 / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.14 |
| 벤치마크 근거 | Common Voice 11.0 / wer = 141.0 (self_reported=True, safe_same_source, readme:model-index[0].results[2].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | While Whisper models cannot be used for real-time transcription out of the box – their speed and size suggest that others may be able to build applications on top of them that allow for near-real-time speech recognition and translation. |
| README 인용 | While Whisper models cannot be used for real-time transcription out of the box – their speed and size suggest that others may be able to build applications on top of them that allow for near-real-time speech recognition and translation. |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | e7fee2b7d940f52b0b504fab1b651db90515ef16 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [binant/whisper-small](https://huggingface.co/binant/whisper-small) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | binant/whisper-small (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.242 / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.9 |
| 벤치마크 근거 | Common Voice 11.0 / wer = 87.3 (self_reported=True, safe_same_source, readme:model-index[0].results[2].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | With chunking enabled, the pipeline can be run with batched inference. |
| README 인용 | With chunking enabled, the pipeline  can be run with batched inference. |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 0e9b81dbb92fd332be7110106711001b6375d1e4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [neurlang/ipa-whisper-base](https://huggingface.co/neurlang/ipa-whisper-base) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.073 / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.27 |
| 벤치마크 근거 | Common Voice 11.0 / wer = 99999999999999.0 (self_reported=True, safe_same_source, readme:model-index[0].results[2].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". |
| README 인용 | The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 949f7c4e4ee374b5202bc5886f6e4552e5ae2371 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [neurlang/ipa-whisper-medium](https://huggingface.co/neurlang/ipa-whisper-medium) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-medium (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.764 / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 2.85 |
| 벤치마크 근거 | Common Voice 11.0 / wer = 99999999999999.0 (self_reported=True, safe_same_source, readme:model-index[0].results[2].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | While Whisper models cannot be used for real-time transcription out of the box – their speed and size suggest that others may be able to build applications on top of them that allow for near-real-time speech recognition and translation. |
| README 인용 | While Whisper models cannot be used for real-time transcription out of the box – their speed and size suggest that others may be able to build applications on top of them that allow for near-real-time speech recognition and translation. |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 083e0d4d36ce29df01640de61cb3634f35523336 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [neurlang/ipa-whisper-small](https://huggingface.co/neurlang/ipa-whisper-small) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-small (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.242 / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.9 |
| 벤치마크 근거 | Common Voice 11.0 / wer = 99999999999999.0 (self_reported=True, safe_same_source, readme:model-index[0].results[2].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". |
| README 인용 | The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 445b3d23500d2ade1dc79fbfa5e9c23249268e4a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [openai/whisper-base](https://huggingface.co/openai/whisper-base) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-base (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.073 / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.27 |
| 벤치마크 근거 | Common Voice 11.0 / wer = 131.0 (self_reported=True, safe_same_source, readme:model-index[0].results[2].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | While Whisper models cannot be used for real-time transcription out of the box – their speed and size suggest that others may be able to build applications on top of them that allow for near-real-time speech recognition and translation. |
| README 인용 | While Whisper models cannot be used for real-time transcription out of the box – their speed and size suggest that others may be able to build applications on top of them that allow for near-real-time speech recognition and translation. |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | e37978b90ca9030d5170a5c07aadb050351a65bb |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [openai/whisper-large](https://huggingface.co/openai/whisper-large) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-large (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.543 / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 5.75 |
| 벤치마크 근거 | Common Voice 11.0 / wer = 54.8 (self_reported=True, safe_same_source, readme:model-index[0].results[2].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". |
| README 인용 | The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 4ef9b41f0d4fe232daafdb5f76bb1dd8b23e01d7 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-medium (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.764 / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 2.85 |
| 벤치마크 근거 | Common Voice 11.0 / wer = 53.87 (self_reported=True, safe_same_source, readme:model-index[0].results[2].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". |
| README 인용 | The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | abdf7c39ab9d0397620ccaea8974cc764cd0953e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [openai/whisper-small](https://huggingface.co/openai/whisper-small) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-small (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.242 / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.9 |
| 벤치마크 근거 | Common Voice 11.0 / wer = 87.3 (self_reported=True, safe_same_source, readme:model-index[0].results[2].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | With chunking enabled, the pipeline can be run with batched inference. |
| README 인용 | With chunking enabled, the pipeline  can be run with batched inference. |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 973afd24965f72e36ca33b3055d56a652f456b4d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-tiny (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.038 / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.14 |
| 벤치마크 근거 | Common Voice 11.0 / wer = 141.0 (self_reported=True, safe_same_source, readme:model-index[0].results[2].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | With chunking enabled, the pipeline can be run with batched inference. |
| README 인용 | With chunking enabled, the pipeline  can be run with batched inference. |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 169d4a4341b33bc18d8881c4b69c2e104e1cc0af |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [unsloth/whisper-base](https://huggingface.co/unsloth/whisper-base) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.073 / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.27 |
| 벤치마크 근거 | Common Voice 11.0 / wer = 131.0 (self_reported=True, safe_same_source, readme:model-index[0].results[2].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". |
| README 인용 | The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 1b1ea2954a4ae79a1eba54616524bc5a3942b5fe |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [unsloth/whisper-small](https://huggingface.co/unsloth/whisper-small) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-small (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.242 / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.9 |
| 벤치마크 근거 | Common Voice 11.0 / wer = 87.3 (self_reported=True, safe_same_source, readme:model-index[0].results[2].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". |
| README 인용 | The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 023f354567bbe9a875605cb8e7ef40ff9629653a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [unsloth/whisper-tiny](https://huggingface.co/unsloth/whisper-tiny) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-tiny (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.038 / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.14 |
| 벤치마크 근거 | Common Voice 11.0 / wer = 141.0 (self_reported=True, safe_same_source, readme:model-index[0].results[2].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". |
| README 인용 | The model is informed of which task to perform (transcription or translation) by passing the appropriate "context tokens". |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 34457cb234c8624f23ac716000773b367000df6e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## bl04 — 한영·영한 번역 품질을 FLORES-101 devtest BLEU 로 비교해 보고 싶어요. 그 점수가 있는 번역 모델이 있나요?

- 사용자 의도: FLORES-101 BLEU 비교
- persona / 표현: korean_service_planner / 혼합형 · 난이도 hard
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: flores101-devtest BLEU 가 저장된 원본
- **1점 기준**: 변환본
- 비교 기준: dataset `flores101-devtest` · metric `^bleu$` FLORES-200 은 다른 dataset 으로 본다

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 3 | 0 | 4,014 | 0 | 3 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 벤치마크 결과 없음 (`no_benchmark_results`) | 3,723 | Jackrong/Negentropy-claude-opus-4.7-4B-GGUF, codefuse-ai/F2LLM-v2-0.6B, metterian/kullm-polyglot-12.8b-v1 |
| 다른 benchmark dataset 만 있음 (`other_benchmark_dataset`) | 291 | aididian/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B, baseten-admin/multilingual-e5-large-instruct-cls, unsloth/LFM2-1.2B |

#### 1. [Helsinki-NLP/opus-mt-tc-big-en-ko](https://huggingface.co/Helsinki-NLP/opus-mt-tc-big-en-ko) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Helsinki-NLP/opus-mt-tc-big-en-ko (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.209 / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-4.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.39 |
| 벤치마크 근거 | flores101-devtest / bleu = 13.7 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | translation |
| README 인용 | - translation |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | ae8606b7b29a495f31ce679cee2007f536a3a5ce |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [Helsinki-NLP/opus-mt-tc-big-ko-en](https://huggingface.co/Helsinki-NLP/opus-mt-tc-big-ko-en) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Helsinki-NLP/opus-mt-tc-big-ko-en (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.209 / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-4.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.39 |
| 벤치마크 근거 | flores101-devtest / bleu = 27.7 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | translation |
| README 인용 | - translation |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | fa26583a41d95346933f26b4cb8f9b700da0d445 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [quickmt/quickmt-en-ko](https://huggingface.co/quickmt/quickmt-en-ko) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | quickmt/quickmt-en-ko (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-4.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.67 |
| 벤치마크 근거 | flores101-devtest / bleu = 27.03 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[1]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used for translating English to Korean. |
| README 인용 | - translation |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | a32fa395ebc7b722a0c021e213ca5fec4065c5df |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## bl05 — MTEB STS17 한국어(ko-ko) cosine Spearman 점수가 있는 임베딩 모델을 찾고 있어요.

- 사용자 의도: 한국어 STS 점수가 있는 임베딩
- persona / 표현: ml_engineer / 기술형 · 난이도 hard
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: STS17 (ko-ko) cos-sim-spearman 이 저장된 원본
- **1점 기준**: 재업로드·변환본
- 비교 기준: dataset `sts17 \(ko-ko\)` · metric `cos-sim-spearman`

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 2 | 0 | 4,015 | 0 | 2 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 벤치마크 결과 없음 (`no_benchmark_results`) | 3,723 | IsValorum/XYZ-Aquila-mini-APEX-I-MiniPlus-V2.1-GGUF, Outlier-Ai/Outlier-10B-V3.2, heegyu/kogpt-neox-small |
| 다른 benchmark dataset 만 있음 (`other_benchmark_dataset`) | 292 | OrionStarAI/Orion-14B-LongChat, Verm1ion/injection-sentry-xlmr, ysmeta/EVE-Embed-1.1-Legal |

#### 1. [Alibaba-NLP/gte-multilingual-base](https://huggingface.co/Alibaba-NLP/gte-multilingual-base) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Alibaba-NLP/gte-multilingual-base (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.305 / 32768 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.57 |
| 벤치마크 근거 | MTEB STS17 (ko-ko) / cos-sim-spearman = 81.58650681159105 (self_reported=True, safe_same_source, readme:model-index[0].results[242].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Usage via Docker and Text Embeddings Inference (TEI). |
| README 인용 | Usage via Docker and [Text Embeddings Inference (TEI)](https://github. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 9bbca17d9273fd0d03d5725c7a4b0f6b45142062 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [alibaba-nlp-community/gte-multilingual-base](https://huggingface.co/alibaba-nlp-community/gte-multilingual-base) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | alibaba-nlp-community/gte-multilingual-base (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.305 / 32768 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.57 |
| 벤치마크 근거 | MTEB STS17 (ko-ko) / cos-sim-spearman = 81.58650681159105 (self_reported=True, safe_same_source, readme:model-index[0].results[242].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Usage via Docker and Text Embeddings Inference (TEI). |
| README 인용 | Usage via Docker and [Text Embeddings Inference (TEI)](https://github. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | fdaec56c6a50d6ebcf691f616ee83a166346b76c |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## bl06 — 한국어 질문으로 문서를 찾는 검색 품질을 숫자로 확인하고 싶어요. Ko-StrategyQA 점수가 나와 있는 임베딩 모델이 있을까요?

- 사용자 의도: 한국어 검색 벤치마크 점수가 있는 임베딩
- persona / 표현: startup_dev / 목적형 · 난이도 hard
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: Ko-StrategyQA score 가 저장된 원본
- **1점 기준**: 변환본
- 비교 기준: dataset `ko-?strategyqa` · metric `^score$`

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 2 | 0 | 4,015 | 0 | 2 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 벤치마크 결과 없음 (`no_benchmark_results`) | 3,723 | bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF, lmstudio-community/aya-expanse-8b-GGUF, setu4993/LEALLA-base |
| 다른 benchmark dataset 만 있음 (`other_benchmark_dataset`) | 292 | ATH-MaaS/Marco-Mini-Base, Karmukilan/multilingual-e5-base, beomi/Yi-Ko-6B |

#### 1. [SamilPwC-AXNode-GenAI/PwC-Embedding_expr](https://huggingface.co/SamilPwC-AXNode-GenAI/PwC-Embedding_expr) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | SamilPwC-AXNode-GenAI/PwC-Embedding_expr (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.56 / 514 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 2.09 |
| 벤치마크 근거 | Ko-StrategyQA / score = 0.8 (self_reported=True, safe_same_source, readme:table[1].row[31].column[2]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model was evaluated on the Korean subset of MTEB. |
| README 인용 | PwC-Embedding_expr was evaluated on the Korean subset of MTEB. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 6c5196980c685db45b58f67bd3be2f79d794351e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [dragonkue/snowflake-arctic-embed-l-v2.0-ko](https://huggingface.co/dragonkue/snowflake-arctic-embed-l-v2.0-ko) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Snowflake/snowflake-arctic-embed-l-v2.0 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.568 / 8194 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 2.12 |
| 벤치마크 근거 | Ko-StrategyQA / score = 0.80498 (self_reported=True, safe_same_source, readme:table[1].row[202].column[9]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | pipeline_tag: sentence-similarity |
| README 인용 | pipeline_tag: sentence-similarity library_name: sentence-transformers --- |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 55ec6e9358a56d56af759bc8372e970caf8c305f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## bl07 — IFEval 0-shot strict accuracy 가 기록된 모델들을 같은 기준으로 비교해 주세요.

- 사용자 의도: IFEval 0-shot 비교
- persona / 표현: researcher / 기술형 · 난이도 hard
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: IFEval (0-Shot) strict acc 가 저장된 원본
- **1점 기준**: 변환본이거나 비교 가능성 낮음
- 비교 기준: dataset `ifeval \(0-shot\)` · metric `strict-acc`

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 4 | 3 | 4,010 | 0 | 7 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 벤치마크 결과 없음 (`no_benchmark_results`) | 3,723 | classla/ParlaCAP-Topic-Classifier, lmstudio-community/LFM2.5-1.2B-Instruct-MLX-4bit, shoumenchougou/RWKV7-G1j-1.5B-GGUF |
| 다른 benchmark dataset 만 있음 (`other_benchmark_dataset`) | 287 | bigscience/mt0-xxl, hajkis-glami/multilingual-e5-base-embeddings, unsloth/Devstral-Small-2505 |

#### 1. [Goekdeniz-Guelmez/Josiefied-Qwen2.5-14B-Instruct-abliterated-v4](https://huggingface.co/Goekdeniz-Guelmez/Josiefied-Qwen2.5-14B-Instruct-abliterated-v4) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-14B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=abliterat) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 14.77 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 27.51 |
| 벤치마크 근거 | IFEval (0-Shot) / inst-level-strict-acc-and-prompt-level-strict-acc = 82.92 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used for text generation tasks. |
| README 인용 | 5-14B-Instruct/blob/main/LICENSE pipeline_tag: text-generation model-index: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 0f26269d41342a692c70281a4213895ff08c4985 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [Goekdeniz-Guelmez/Josiefied-Qwen2.5-7B-Instruct-abliterated-v2](https://huggingface.co/Goekdeniz-Guelmez/Josiefied-Qwen2.5-7B-Instruct-abliterated-v2) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=abliterat) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 7.616 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.19 |
| 벤치마크 근거 | IFEval (0-Shot) / inst-level-strict-acc-and-prompt-level-strict-acc = 78.41 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used for various tasks requiring intelligent assistance. |
| README 인용 | 5-7B-Instruct/blob/main/LICENSE pipeline_tag: text-generation model-index: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 43b9adb8f95756f5ea2c55186752d00176196047 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [OpenBuddy/openbuddy-llama3-70b-v21.2-32k](https://huggingface.co/OpenBuddy/openbuddy-llama3-70b-v21.2-32k) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | OpenBuddy/openbuddy-llama3-70b-v21.2-32k (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 70.554 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 131.42 |
| 벤치마크 근거 | IFEval (0-Shot) / inst-level-strict-acc-and-prompt-level-strict-acc = 70.1 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used in scenarios such as chatbots and other text generation applications. |
| README 인용 | GitHub and Usage Guide: [https://github. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | a4552b09f1b34142087defbb1f7ae2d6698b65d4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [OpenBuddy/openbuddy-qwen2.5llamaify-7b-v23.1-200k](https://huggingface.co/OpenBuddy/openbuddy-qwen2.5llamaify-7b-v23.1-200k) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-7B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 7.615 / 200000 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.18 |
| 벤치마크 근거 | IFEval (0-Shot) / inst-level-strict-acc-and-prompt-level-strict-acc = 56.73 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used in scenarios requiring text generation, such as chatbots. |
| README 인용 | GitHub and Usage Guide: [https://github. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | dfd25d5c3d8dd2bd45bf0e12fe13d121f9e512ce |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [Orion-zhen/Qwen2.5-7B-Instruct-Uncensored](https://huggingface.co/Orion-zhen/Qwen2.5-7B-Instruct-Uncensored) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-7B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Uncensored) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 7.616 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gpl-3.0 / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.19 |
| 벤치마크 근거 | IFEval (0-Shot) / inst-level-strict-acc-and-prompt-level-strict-acc = 72.04 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used for text generation tasks. |
| README 인용 | pipeline_tag: text-generation model-index: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | ddc094207b8d785af31b9eaf47848e5ff55a87ef |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [Sakalti/ultiima-72B](https://huggingface.co/Sakalti/ultiima-72B) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-72B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 72.706 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 135.43 |
| 벤치마크 근거 | IFEval (0-Shot) / inst-level-strict-acc-and-prompt-level-strict-acc = 71.4 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model is licensed under the name 'qwen'. |
| README 인용 | license_name: qwen inference: true model-index: |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | f194962be52eca89314b841ede0858994c194263 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [oxyapi/oxy-1-small](https://huggingface.co/oxyapi/oxy-1-small) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-14B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 14.77 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 27.51 |
| 벤치마크 근거 | IFEval (0-Shot) / inst-level-strict-acc-and-prompt-level-strict-acc = 62.45 (self_reported=True, safe_same_source, readme:model-index[0].results[0].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | To utilize Oxy 1 Small for text generation in role-play scenarios, you can load the model using the Hugging Face Transformers library. |
| README 인용 | To utilize Oxy 1 Small for text generation in role-play scenarios, you can load the model using the Hugging Face Transformers library: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 39cfc26910608246f35416cfd3d5fe91343c8584 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## bl08 — 코드 생성도 할 수 있는 한국어 LLM 을 찾는데, HumanEval 점수가 README 에 있는 것만 보고 싶어요.

- 사용자 의도: HumanEval 점수가 있는 LLM
- persona / 표현: startup_dev / 혼합형 · 난이도 hard
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: HumanEval score 가 저장된 원본
- **1점 기준**: 변환본이거나 비교 가능성 낮음
- 비교 기준: dataset `^\W*humaneval\W*(\(code\))?\s*$` · metric `^score$` pass@k·f1 로 적힌 HumanEval 은 다른 metric 으로 본다

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 6 | 0 | 4,011 | 0 | 6 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 벤치마크 결과 없음 (`no_benchmark_results`) | 3,723 | Horizon-Labs/multilingual-sentiment-small, mobilint/kanana-nano-2.1b-instruct, unsloth/Qwen2.5-7B-Instruct-unsloth-bnb-4bit |
| 다른 benchmark dataset 만 있음 (`other_benchmark_dataset`) | 287 | FINAL-Bench/Darwin-27B-RSI, bezzam/Qwen3-ASR-0.6B-hf, kiwi-farm/kiwi-coco-lm-base-generator |
| 같은 dataset 이지만 다른 metric (`other_metric`) | 1 | bigscience/mt0-xl |

같은 canonical family 후보가 3개 이상: Qwen/Qwen3.6-35B-A3B 3

#### 1. [Motif-Technologies/Motif-2-12.7B-Reasoning](https://huggingface.co/Motif-Technologies/Motif-2-12.7B-Reasoning) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Motif-Technologies/Motif-2-12.7B-Base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 12.704 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 47.33 |
| 벤치마크 근거 | HumanEval / score = 93.2 (self_reported=True, safe_same_source, readme:table[1].row[45].column[4]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Can be used to run a VLLM API server for chat completions. |
| README 인용 | ```bash # run vllm api server VLLM_ATTENTION_BACKEND=DIFFERENTIAL_FLASH_ATTN \ vllm serve Motif-Technologies/Motif-2-12.7B-Reasoning \     --trust-remote-code \     --max-model-len 65536 \     --tensor-parallel-size 8  # sending requests wi… |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 02d060835415f43d57dc6bee72b1e2779d8e57e5 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [Motif-Technologies/Motif-3-Base](https://huggingface.co/Motif-Technologies/Motif-3-Base) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Motif-Technologies/Motif-3-Base (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 314.842 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 586.44 |
| 벤치마크 근거 | HumanEval / score = 73.7 (self_reported=True, safe_same_source, readme:table[1].row[97].column[3]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The architecture and distributed training framework used for Motif 3 are available at MotifTechnologies/motif3-training-example. |
| README 인용 | NOTE] > The architecture and distributed training framework used for Motif 3 are available at [MotifTechnologies/motif3-training-example](https://github. |
| provenance status | verified 13, not_applicable 3, documented 5, unknown 2 |
| revision | 7f7531c7f2b0259b527477c72715ed1805dd95ce |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [hossain0909/Keural-Nova-v1.2-experimental](https://huggingface.co/hossain0909/Keural-Nova-v1.2-experimental) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.6-35B-A3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 35.952 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 66.97 |
| 벤치마크 근거 | **HumanEval** (code) / score = 68.29 (self_reported=True, safe_same_source, readme:table[1].row[59].column[5]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Data includes a cleaned, balanced Korean/English/code/replay mix. |
| README 인용 | - **Data:** ~162k examples — a cleaned, balanced Korean/English/code/replay mix |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 0535e93ffa81ff5f60c5048e470db752d8000d69 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [mkd-ai-dev/Keural-Nova-v1.2-experimental](https://huggingface.co/mkd-ai-dev/Keural-Nova-v1.2-experimental) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.6-35B-A3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 35.952 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 66.97 |
| 벤치마크 근거 | **HumanEval** (code) / score = 68.29 (self_reported=True, safe_same_source, readme:table[1].row[59].column[5]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Designed for text generation tasks. |
| README 인용 | pipeline_tag: text-generation library_name: transformers tags: |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | c3332b8d9c5eaa5e061330d2a530ffd5bf23fe80 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [mkd-dev/Keural-Nova-v1.2-experimental](https://huggingface.co/mkd-dev/Keural-Nova-v1.2-experimental) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.6-35B-A3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 35.952 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 66.97 |
| 벤치마크 근거 | **HumanEval** (code) / score = 68.29 (self_reported=True, safe_same_source, readme:table[1].row[59].column[5]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Data includes a cleaned, balanced Korean/English/code/replay mix. |
| README 인용 | - **Data:** ~162k examples — a cleaned, balanced Korean/English/code/replay mix |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 2c6ed6402f0f306c0970c97bd169ed993188fe0a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [trillionlabs/Trida-7B](https://huggingface.co/trillionlabs/Trida-7B) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | trillionlabs/Trida-7B (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.527 / 4096 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit, readme:korean_explicit_phrase |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.02 |
| 벤치마크 근거 | HumanEval / score = 35.98 (self_reported=True, safe_same_source, readme:table[3].row[188].column[2]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Trida-7B is designed for text generation tasks. |
| README 인용 | pipeline_tag: text-generation library_name: transformers extra_gated_fields:   Full Name: text   Email: text   Organization: text --- |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | c37755e81222de0aff69ee481f5299a99928b105 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## bl09 — 아이 수학 숙제를 도와줄 모델을 고르는데, 수학 문제 풀이 실력을 GSM8K 점수로 확인할 수 있는 모델이 있나요?

- 사용자 의도: GSM8K 점수가 있는 모델
- persona / 표현: local_user / 목적형 · 난이도 hard
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: GSM8K score 가 저장된 원본
- **1점 기준**: 변환본이거나 비교 가능성 낮음
- 비교 기준: dataset `^gsm8k$` · metric `^score$` GSM8K (EM)·5-shot accuracy 등 설정이 적힌 결과는 다른 dataset 표기로 본다

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 5 | 3 | 4,009 | 0 | 8 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 벤치마크 결과 없음 (`no_benchmark_results`) | 3,723 | alex-and-the/Qwen3.5-9B-Uncensored-MLX, mradermacher/Tencent-Hy-30B-A3B-uncensored-heretic-GGUF, slvrfivo/qwen3-4b-writing-eval-v1-merged |
| 다른 benchmark dataset 만 있음 (`other_benchmark_dataset`) | 285 | LiquidAI/LFM2-1.2B, cnmoro/snowflake-arctic-embed-m-v2.0-cpu, unsloth/LFM2-1.2B |
| 같은 dataset 이지만 다른 metric (`other_metric`) | 1 | hiwaifu-research/WaifuGemma4-26b-a4b-v1 |

같은 canonical family 후보가 3개 이상: LiquidAI/LFM2.5-2.6B 3

#### 1. [CohereLabs/c4ai-command-r-plus](https://huggingface.co/CohereLabs/c4ai-command-r-plus) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | CohereLabs/c4ai-command-r-plus (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 103.811 / — |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / auto |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 193.36 |
| 벤치마크 근거 | GSM8k / score = 70.7 (self_reported=True, safe_same_source, readme:table[1].row[382].column[8]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Command R+ is optimized for a variety of use cases including reasoning, summarization, and question answering. |
| README 인용 | Command R+ is optimized for a variety of use cases including reasoning, summarization, and question answering. |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 3de12c88b4c6c882389a6f424cc2074383aa17d8 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [FINAL-Bench/Darwin-27B-RSI](https://huggingface.co/FINAL-Bench/Darwin-27B-RSI) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | FINAL-Bench/Darwin-27B-Opus (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 26.896 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 50.1 |
| 벤치마크 근거 | GSM8K / score = 0.97 (self_reported=True, safe_same_source, readme:table[2].row[110].column[3]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Darwin-27B-RSI is a thinking model. |
| README 인용 | Darwin-27B-RSI is a thinking model. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 08d44a01bbe4762fbc95171c952f0536bd5d46c6 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [Justbackup/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS](https://huggingface.co/Justbackup/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/LFM2.5-2.6B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=UNCENSORED) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.697 / 128000 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 5.03 |
| 벤치마크 근거 | GSM8K / score = 69.45 (self_reported=True, safe_same_source, readme:table[5].row[120].column[6]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Application-specific systems that validate outputs and enforce their own policy layer. |
| README 인용 | - Application-specific systems that validate outputs and enforce their own policy layer |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 970090cf65dd9287c4959532c08850dc333b0475 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [Motif-Technologies/Motif-2-12.7B-Reasoning](https://huggingface.co/Motif-Technologies/Motif-2-12.7B-Reasoning) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Motif-Technologies/Motif-2-12.7B-Base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 12.704 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 47.33 |
| 벤치마크 근거 | GSM8K / score = 95.53 (self_reported=True, safe_same_source, readme:table[1].row[32].column[4]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Can be used to run a VLLM API server for chat completions. |
| README 인용 | ```bash # run vllm api server VLLM_ATTENTION_BACKEND=DIFFERENTIAL_FLASH_ATTN \ vllm serve Motif-Technologies/Motif-2-12.7B-Reasoning \     --trust-remote-code \     --max-model-len 65536 \     --tensor-parallel-size 8  # sending requests wi… |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 02d060835415f43d57dc6bee72b1e2779d8e57e5 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [Motif-Technologies/Motif-3-Base](https://huggingface.co/Motif-Technologies/Motif-3-Base) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Motif-Technologies/Motif-3-Base (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 314.842 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 586.44 |
| 벤치마크 근거 | GSM8K / score = 93.93 (self_reported=True, safe_same_source, readme:table[1].row[95].column[3]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The architecture and distributed training framework used for Motif 3 are available at MotifTechnologies/motif3-training-example. |
| README 인용 | NOTE] > The architecture and distributed training framework used for Motif 3 are available at [MotifTechnologies/motif3-training-example](https://github. |
| provenance status | verified 13, not_applicable 3, documented 5, unknown 2 |
| revision | 7f7531c7f2b0259b527477c72715ed1805dd95ce |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [PhillyLabs/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS](https://huggingface.co/PhillyLabs/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/LFM2.5-2.6B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=UNCENSORED) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.697 / 128000 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 5.03 |
| 벤치마크 근거 | GSM8K / score = 69.45 (self_reported=True, safe_same_source, readme:table[5].row[120].column[6]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Application-specific systems that validate outputs and enforce their own policy layer. |
| README 인용 | - Application-specific systems that validate outputs and enforce their own policy layer |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 58da61d00219436934ef98d76989ea94b7b28a47 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [swartbwoy/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS](https://huggingface.co/swartbwoy/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/LFM2.5-2.6B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=UNCENSORED) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.697 / 128000 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 5.03 |
| 벤치마크 근거 | GSM8K / score = 69.45 (self_reported=True, safe_same_source, readme:table[5].row[120].column[6]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Application-specific systems that validate outputs and enforce their own policy layer. |
| README 인용 | - Application-specific systems that validate outputs and enforce their own policy layer |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | bd4611efde19c99f2eda638dacd666f29370182e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [trillionlabs/Trida-7B](https://huggingface.co/trillionlabs/Trida-7B) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | trillionlabs/Trida-7B (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.527 / 4096 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit, readme:korean_explicit_phrase |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.02 |
| 벤치마크 근거 | GSM8k / score = 65.13 (self_reported=True, safe_same_source, readme:table[4].row[195].column[2]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | Trida-7B is designed for text generation tasks. |
| README 인용 | pipeline_tag: text-generation library_name: transformers extra_gated_fields:   Full Name: text   Email: text   Organization: text --- |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | c37755e81222de0aff69ee481f5299a99928b105 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## bl10 — MMLU-PRO 5-shot accuracy 가 기록된 모델만 모아서 비교하고 싶습니다.

- 사용자 의도: MMLU-PRO 5-shot 비교
- persona / 표현: ml_engineer / 기술형 · 난이도 hard
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: MMLU-PRO (5-shot) accuracy 가 저장된 원본
- **1점 기준**: 변환본이거나 비교 가능성 낮음
- 비교 기준: dataset `mmlu-pro \(5-shot\)$` · metric `^accuracy$`

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 4 | 3 | 4,010 | 0 | 7 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 벤치마크 결과 없음 (`no_benchmark_results`) | 3,723 | batiai/Qwen3-Embedding-0.6B-GGUF, facebook/mms-1b-l1107, mradermacher/CURE-MED-7B-i1-GGUF |
| 다른 benchmark dataset 만 있음 (`other_benchmark_dataset`) | 287 | BalaRajesh1/mmbert-small-nli, NC-AI-consortium-VAETKI/VAETKI, dragonkue/colbert-ko-0.1b |

#### 1. [Goekdeniz-Guelmez/Josiefied-Qwen2.5-14B-Instruct-abliterated-v4](https://huggingface.co/Goekdeniz-Guelmez/Josiefied-Qwen2.5-14B-Instruct-abliterated-v4) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-14B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=abliterat) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 14.77 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 27.51 |
| 벤치마크 근거 | MMLU-PRO (5-shot) / accuracy = 44.65 (self_reported=True, safe_same_source, readme:model-index[0].results[5].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used for text generation tasks. |
| README 인용 | 5-14B-Instruct/blob/main/LICENSE pipeline_tag: text-generation model-index: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 0f26269d41342a692c70281a4213895ff08c4985 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [Goekdeniz-Guelmez/Josiefied-Qwen2.5-7B-Instruct-abliterated-v2](https://huggingface.co/Goekdeniz-Guelmez/Josiefied-Qwen2.5-7B-Instruct-abliterated-v2) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=abliterat) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 7.616 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.19 |
| 벤치마크 근거 | MMLU-PRO (5-shot) / accuracy = 34.76 (self_reported=True, safe_same_source, readme:model-index[0].results[5].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used for various tasks requiring intelligent assistance. |
| README 인용 | 5-7B-Instruct/blob/main/LICENSE pipeline_tag: text-generation model-index: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 43b9adb8f95756f5ea2c55186752d00176196047 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [OpenBuddy/openbuddy-llama3-70b-v21.2-32k](https://huggingface.co/OpenBuddy/openbuddy-llama3-70b-v21.2-32k) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | OpenBuddy/openbuddy-llama3-70b-v21.2-32k (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 70.554 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 131.42 |
| 벤치마크 근거 | MMLU-PRO (5-shot) / accuracy = 42.58 (self_reported=True, safe_same_source, readme:model-index[0].results[5].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used in scenarios such as chatbots and other text generation applications. |
| README 인용 | GitHub and Usage Guide: [https://github. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | a4552b09f1b34142087defbb1f7ae2d6698b65d4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [OpenBuddy/openbuddy-qwen2.5llamaify-7b-v23.1-200k](https://huggingface.co/OpenBuddy/openbuddy-qwen2.5llamaify-7b-v23.1-200k) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-7B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 7.615 / 200000 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.18 |
| 벤치마크 근거 | MMLU-PRO (5-shot) / accuracy = 32.75 (self_reported=True, safe_same_source, readme:model-index[0].results[5].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used in scenarios requiring text generation, such as chatbots. |
| README 인용 | GitHub and Usage Guide: [https://github. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | dfd25d5c3d8dd2bd45bf0e12fe13d121f9e512ce |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [Orion-zhen/Qwen2.5-7B-Instruct-Uncensored](https://huggingface.co/Orion-zhen/Qwen2.5-7B-Instruct-Uncensored) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-7B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Uncensored) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 7.616 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gpl-3.0 / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.19 |
| 벤치마크 근거 | MMLU-PRO (5-shot) / accuracy = 38.07 (self_reported=True, safe_same_source, readme:model-index[0].results[5].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model can be used for text generation tasks. |
| README 인용 | pipeline_tag: text-generation model-index: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | ddc094207b8d785af31b9eaf47848e5ff55a87ef |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [Sakalti/ultiima-72B](https://huggingface.co/Sakalti/ultiima-72B) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-72B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 72.706 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 135.43 |
| 벤치마크 근거 | MMLU-PRO (5-shot) / accuracy = 54.51 (self_reported=True, safe_same_source, readme:model-index[0].results[5].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | The model is licensed under the name 'qwen'. |
| README 인용 | license_name: qwen inference: true model-index: |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | f194962be52eca89314b841ede0858994c194263 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [oxyapi/oxy-1-small](https://huggingface.co/oxyapi/oxy-1-small) — Claude 제안: **2점**

- 제안 이유: 같은 dataset·metric 점수가 저장돼 있음
- 근거 위치: `benchmark_metadata` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-14B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 14.77 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 27.51 |
| 벤치마크 근거 | MMLU-PRO (5-shot) / accuracy = 44.45 (self_reported=True, safe_same_source, readme:model-index[0].results[5].metrics[0]; 같은 dataset·metric 결과 1건) |
| 의미 claim (use_cases) | To utilize Oxy 1 Small for text generation in role-play scenarios, you can load the model using the Hugging Face Transformers library. |
| README 인용 | To utilize Oxy 1 Small for text generation in role-play scenarios, you can load the model using the Hugging Face Transformers library: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 39cfc26910608246f35416cfd3d5fe91343c8584 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______
