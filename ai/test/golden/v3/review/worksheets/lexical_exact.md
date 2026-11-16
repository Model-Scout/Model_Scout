# 골든셋 v3 검수 워크시트 — lexical_exact (모델명 지목)

> 상태: **초안 + 전수 스캔 + 검수 준비 완료**. 아래 점수는 Claude 의 제안이며 정답이 아니다.
>
> 판정 입력: `python test/golden/v3/tools/judge.py <query_id> <model_id> --decision approve|2|1|exclude|hold --reason "…" --by <이름>`

## lx01 — BM-K 의 KoSimCSE-roberta 모델이 있나요?

- 사용자 의도: 이름으로 특정 임베딩 모델 찾기
- persona / 표현: ml_engineer / 기술형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: BM-K/KoSimCSE-roberta 원본
- **1점 기준**: 같은 모델의 변환·재업로드
- 비교 계열: KoSimCSE-roberta (`kosimcse-roberta(?!-multitask)`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 1 | 0 | 4,016 | 0 | 1 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 질문이 지목한 모델 이름이 아님 (`not_named_model`) | 4,016 | joeblowma/Qwopus3.5-9B-Coder-MTP-GGUF, ngquocvinh/LFM3-1.7B-GGUF, thelamapi/next-1b |

#### 1. [BM-K/KoSimCSE-roberta](https://huggingface.co/BM-K/KoSimCSE-roberta) — Claude 제안: **2점**

- 제안 이유: KoSimCSE-roberta 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | BM-K/KoSimCSE-roberta (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.111 / 514 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.41 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Users can download the pre-trained models and inference right away. |
| README 인용 | You can download the pre-trained models and inference right away, also it provides environments where individuals can train models. |
| provenance status | verified 14, not_applicable 3, documented 2, unknown 4 |
| revision | f8ef6974a7d130d24190641f5dc14c246ea85bb4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## lx02 — 카카오가 공개한 kanana-2 임베딩 모델로 사내 검색을 만들어 보려는데, 어떤 걸 받으면 되나요?

- 사용자 의도: kanana-2 embedding 계열 찾기
- persona / 표현: backend_dev / 혼합형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: kakaocorp 의 kanana-2 embedding 원본
- **1점 기준**: 같은 모델의 GGUF 등 변환본
- 비교 계열: kanana-2 embedding (`kanana-2-[\d.]+b-embedding`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 2 | 2 | 4,013 | 0 | 4 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 질문이 지목한 모델 이름이 아님 (`not_named_model`) | 4,013 | DevQuasar-13/Qwen.Qwen2.5-3B-GGUF, batiai/Qwen3.5-9B-GGUF, mradermacher/next2.5-i1-GGUF |

#### 1. [kakaocorp/kanana-2-1.3b-embedding](https://huggingface.co/kakaocorp/kanana-2-1.3b-embedding) — Claude 제안: **2점**

- 제안 이유: kanana-2 embedding 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | kakaocorp/kanana-2-1.3b-embedding (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.291 / 4096 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 2.41 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is used for sentence similarity tasks. |
| README 인용 | --- library_name: sentence-transformers pipeline_tag: sentence-similarity license: other license_name: kanana-open-license license_link: https://huggingface. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 107b09b19ea3628acbd42615ee9ad59b82f604a3 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [kakaocorp/kanana-2-3b-embedding](https://huggingface.co/kakaocorp/kanana-2-3b-embedding) — Claude 제안: **2점**

- 제안 이유: kanana-2 embedding 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | kakaocorp/kanana-2-3b-embedding (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 3.181 / 4096 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 5.92 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The kanana-2-3b-embedding model is used for sentence similarity tasks. |
| README 인용 | --- library_name: sentence-transformers pipeline_tag: sentence-similarity license: other license_name: kanana-open-license license_link: https://huggingface. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 2c85dbe61af8ff033d2c9d46a686c665153069aa |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [mykor/kanana-2-1.3b-embedding-GGUF](https://huggingface.co/mykor/kanana-2-1.3b-embedding-GGUF) — Claude 제안: **1점**

- 제안 이유: kanana-2 embedding 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | kakaocorp/kanana-2-1.3b-embedding (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.291 / 4096 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.64 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for sentence similarity tasks. |
| README 인용 | --- library_name: gguf pipeline_tag: sentence-similarity license: other license_name: kanana-open-license license_link: https://huggingface. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 7f5de108cb2ee1f754a3fef792496d3e75c890a1 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [mykor/kanana-2-3b-embedding-GGUF](https://huggingface.co/mykor/kanana-2-3b-embedding-GGUF) — Claude 제안: **1점**

- 제안 이유: kanana-2 embedding 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | kakaocorp/kanana-2-3b-embedding (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 3.181 / 4096 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.46 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is used for sentence similarity tasks. |
| README 인용 | --- library_name: gguf pipeline_tag: sentence-similarity license: other license_name: kanana-open-license license_link: https://huggingface. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 8f33dd3a54c308dca5dff244972f5765e7a32db4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## lx03 — EXAONE-4.0-1.2B 원본이랑 양자화 버전들을 한 번에 보고 싶어요.

- 사용자 의도: 특정 모델과 그 양자화본
- persona / 표현: ml_engineer / 기술형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: LGAI-EXAONE/EXAONE-4.0-1.2B 원본
- **1점 기준**: 같은 모델의 공식·비공식 양자화본
- 비교 계열: EXAONE-4.0-1.2B (`exaone-4\.0-1\.2b`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 1 | 9 | 4,007 | 0 | 10 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 질문이 지목한 모델 이름이 아님 (`not_named_model`) | 4,007 | aimeri/Ministral-3-3B-Base-2512-text, saidutta69/Qwen3.5-4B-heretic, sartifyllc/African-Cross-Lingua-Embeddings-Model |

같은 canonical family 후보가 3개 이상: LGAI-EXAONE/EXAONE-4.0-1.2B 9

#### 1. [LGAI-EXAONE/EXAONE-4.0-1.2B](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-1.2B) — Claude 제안: **2점**

- 제안 이유: EXAONE-4.0-1.2B 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-4.0-1.2B (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.279 / 65536 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 2.38 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is designed for on-device applications. |
| README 인용 | 2B** model designed for on-device applications. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 3abf2810673c7c0778df64a73c2d52eab32d91c4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [LGAI-EXAONE/EXAONE-4.0-1.2B-AWQ](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-1.2B-AWQ) — Claude 제안: **1점**

- 제안 이유: EXAONE-4.0-1.2B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-4.0-1.2B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=AWQ) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.279 / 65536 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.91 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is designed for on-device applications. |
| README 인용 | 2B** model designed for on-device applications. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 36ce90d2e13443cea0cdc1eb18abeda7b60144a0 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [LGAI-EXAONE/EXAONE-4.0-1.2B-FP8](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-1.2B-FP8) — Claude 제안: **1점**

- 제안 이유: EXAONE-4.0-1.2B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-4.0-1.2B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=FP8) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.279 / 65536 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.39 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is designed for on-device applications. |
| README 인용 | 2B** model designed for on-device applications. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 7a81ddc21b34a54777679de80f2e159c588be076 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [LGAI-EXAONE/EXAONE-4.0-1.2B-GGUF](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-1.2B-GGUF) — Claude 제안: **1점**

- 제안 이유: EXAONE-4.0-1.2B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-4.0-1.2B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.279 / 65536 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.7 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is designed for on-device applications. |
| README 인용 | 2B** model designed for on-device applications. |
| provenance status | verified 13, not_applicable 4, documented 5, unknown 1 |
| revision | 162446400ea4596377a3ce1d3ddffa32971af0a6 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [LGAI-EXAONE/EXAONE-4.0-1.2B-GPTQ-Int8](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-1.2B-GPTQ-Int8) — Claude 제안: **1점**

- 제안 이유: EXAONE-4.0-1.2B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-4.0-1.2B (variant=true, 종류=gptq, 관계 근거=base_model_tag, 변환 표지=GPTQ) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.279 / 65536 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.41 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is designed for on-device applications. |
| README 인용 | 2B** model designed for on-device applications. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | cc2875371f86e25460139bfdcd8feb5b2f37b314 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [Mungert/EXAONE-4.0-1.2B-GGUF](https://huggingface.co/Mungert/EXAONE-4.0-1.2B-GGUF) — Claude 제안: **1점**

- 제안 이유: EXAONE-4.0-1.2B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Mungert/EXAONE-4.0-1.2B-GGUF (variant=false, 종류=—, 관계 근거=self, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.279 / 65536 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.54 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is designed for on-device applications. |
| README 인용 | 2B** model designed for on-device applications. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | c89b69bf8a3e8a7c5d485ff3c89b1175af84d9c2 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [Open4bits/EXAONE-4.0-1.2B-gguf](https://huggingface.co/Open4bits/EXAONE-4.0-1.2B-gguf) — Claude 제안: **1점**

- 제안 이유: EXAONE-4.0-1.2B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-4.0-1.2B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=4bit) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.279 / 65536 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.72 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | 2B model converted to GGUF format, published by Open4bits to enable efficient local inference with reduced memory usage and broad CPU compatibility. |
| README 인용 | 2B model converted to GGUF format**, published by Open4bits to enable efficient local inference with reduced memory usage and broad CPU compatibility. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 3158881f6e2c14dc79b1cbbdb5a6577694c255f2 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [lmstudio-community/EXAONE-4.0-1.2B-MLX-4bit](https://huggingface.co/lmstudio-community/EXAONE-4.0-1.2B-MLX-4bit) — Claude 제안: **1점**

- 제안 이유: EXAONE-4.0-1.2B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-4.0-1.2B (variant=true, 종류=mlx, mlx_quantized, 관계 근거=base_model_tag, 변환 표지=MLX) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.279 / 65536 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.67 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is intended for text generation tasks. |
| README 인용 | pipeline_tag: text-generation library_name: transformers base_model: LGAI-EXAONE/EXAONE-4. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | da095e728aab942c3ade54860b76f510be4054f4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [mlx-community/exaone-4.0-1.2b-4bit](https://huggingface.co/mlx-community/exaone-4.0-1.2b-4bit) — Claude 제안: **1점**

- 제안 이유: EXAONE-4.0-1.2B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-4.0-1.2B (variant=true, 종류=mlx, 관계 근거=base_model_tag, 변환 표지=mlx) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.279 / 65536 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.67 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for text generation tasks. |
| README 인용 | pipeline_tag: text-generation library_name: mlx base_model: LGAI-EXAONE/EXAONE-4. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 6dbf5f06dcb9526a7c328f692b1e08d35e17bff2 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [mobilint/EXAONE-4.0-1.2B](https://huggingface.co/mobilint/EXAONE-4.0-1.2B) — Claude 제안: **1점**

- 제안 이유: EXAONE-4.0-1.2B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-4.0-1.2B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.21 / 16384 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.78 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for various text generation applications. |
| README 인용 | pipeline_tag: text-generation base_model: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | d09550186db15797cd1a9519c1da9d94df2e701d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## lx04 — KT 에서 나온 믿음 2.0 Mini 를 써 보라는 얘기를 들었어요. 이 모델 어디서 받을 수 있나요?

- 사용자 의도: Midm-2.0-Mini 찾기(한국어 표기)
- persona / 표현: korean_service_planner / 목적형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: K-intelligence/Midm-2.0-Mini-Instruct 원본
- **1점 기준**: 같은 모델의 변환본
- 비교 계열: Midm-2.0-Mini (`midm-2\.0-mini`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 1 | 1 | 4,015 | 0 | 2 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 질문이 지목한 모델 이름이 아님 (`not_named_model`) | 4,015 | bigscience/mt0-small, cnfusion/QwenPhi-4-0.5b-Draft-mlx-fp16, schift-io/schift-ocr-1-beta |

#### 1. [K-intelligence/Midm-2.0-Mini-Instruct](https://huggingface.co/K-intelligence/Midm-2.0-Mini-Instruct) — Claude 제안: **2점**

- 제안 이유: Midm-2.0-Mini 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | K-intelligence/Midm-2.0-Mini-Instruct (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.306 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 4.29 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is suitable for real-world applications that require both performance and versatility. |
| README 인용 | It extends an 8B-scale model by applying the Depth-up Scaling (DuS) method, making it suitable for real-world applications that require both performance and versatility. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 383eb221c52a32278f1985257b264ade8d982e60 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [mykor/Midm-2.0-Mini-Instruct-gguf](https://huggingface.co/mykor/Midm-2.0-Mini-Instruct-gguf) — Claude 제안: **1점**

- 제안 이유: Midm-2.0-Mini 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | K-intelligence/Midm-2.0-Mini-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.306 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.91 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | It extends an 8B-scale model by applying the Depth-up Scaling (DuS) method, making it suitable for real-world applications that require both performance and versatility. |
| README 인용 | It extends an 8B-scale model by applying the Depth-up Scaling (DuS) method, making it suitable for real-world applications that require both performance and versatility. |
| provenance status | verified 13, not_applicable 4, documented 5, unknown 1 |
| revision | 152690816d5f03763fa32869c651c99a6d7c300f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## lx05 — EleutherAI polyglot-ko-5.8b 를 베이스로 실험하려고 합니다. 이 모델이 등록돼 있나요?

- 사용자 의도: 특정 베이스 모델 찾기
- persona / 표현: researcher / 기술형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: EleutherAI/polyglot-ko-5.8b 원본
- **1점 기준**: 같은 가중치의 변환·재업로드(파인튜닝은 아님)
- 비교 계열: polyglot-ko-5.8b (`polyglot-ko-5\.8b`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 1 | 0 | 4,016 | 0 | 1 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 질문이 지목한 모델 이름이 아님 (`not_named_model`) | 4,015 | CollectionStudio/AFM-4.5B, oroboros-labs/claude-opus-9-undecillion-v, utter-project/EuroMoE-2.6B-A0.6B-Instruct-Preview |
| variant 관계가 질문과 맞지 않음 (`variant_mismatch`) | 1 | beomi/KoAlpaca-Polyglot-5.8B |

#### 1. [EleutherAI/polyglot-ko-5.8b](https://huggingface.co/EleutherAI/polyglot-ko-5.8b) — Claude 제안: **2점**

- 제안 이유: polyglot-ko-5.8b 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | EleutherAI/polyglot-ko-5.8b (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 6.003 / 2048 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit, readme:korean_explicit_phrase |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 11.07 |
| 벤치마크 근거 | 점수 5건 저장 |
| 의미 claim (use_cases) | The model's evaluation results vary with the number of few-shot examples. |
| README 인용 | The following tables show the results when the number of few-shot examples differ. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 581a4c3eebfac23536b3c9676bcfb05c6a97baa2 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## lx06 — KURE-v1 임베딩을 ONNX 버전으로 받을 수 있을까요? 서버에서 ONNX Runtime 으로 돌릴 거예요.

- 사용자 의도: 특정 모델의 ONNX 버전
- persona / 표현: backend_dev / 혼합형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `require_artifact` | onnx | ONNX 버전으로 … ONNX Runtime | 예 |

- **2점 기준**: KURE-v1 의 ONNX 변환본(요청 포맷)
- **1점 기준**: KURE-v1 계열이지만 다른 버전·용도
- 비교 계열: KURE-v1 (`kure-v1`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 189 | 1 | 0 | 188 | 0 | 1 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 질문이 지목한 모델 이름이 아님 (`not_named_model`) | 188 | Horizon-Labs/multilingual-emotions-small, leewaay/klue-roberta-base-klueNLI-klueSTS-MSL128, onnx-community/content-safety-guard-small-ONNX |

#### 1. [rokrokss/KURE-v1-onnx](https://huggingface.co/rokrokss/KURE-v1-onnx) — Claude 제안: **2점**

- 제안 이유: KURE-v1 계열이며 요청한 포맷
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | nlpai-lab/KURE-v1 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=onnx) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 8194 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx / 0.67 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for feature extraction in various applications. |
| README 인용 | ```js import { pipeline } from '@huggingface/transformers';  const embed = await pipeline('feature-extraction', '<this repository>', { dtype: 'q8' }); const output = await embed(['눈이 내리는 밤', 'A snowy night'], { pooling: 'cls', normalize: tr… |
| provenance status | verified 12, not_applicable 3, documented 4, unknown 4 |
| revision | 7da86b48a3618513e041d6084a5cff2ea20a88d0 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## lx07 — SenseVoice Small 을 whisper.cpp 처럼 로컬에서 돌리려고 하는데 GGUF 로 변환된 게 있나요?

- 사용자 의도: SenseVoiceSmall GGUF
- persona / 표현: local_user / 혼합형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `require_artifact` | gguf | GGUF 로 변환된 | 예 |

- **2점 기준**: SenseVoice Small 의 GGUF 변환본(요청 포맷)
- **1점 기준**: 같은 계열의 다른 변형
- 비교 계열: SenseVoiceSmall (`sense-?voice-?small`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 1,643 | 4 | 0 | 1,639 | 0 | 4 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 질문이 지목한 모델 이름이 아님 (`not_named_model`) | 1,639 | TheBloke/OpenBuddy-Llama2-13B-v11.1-GGUF, TheBloke/Synatra-7B-v0.3-RP-GGUF, tensorblock/ko-platypus-kiwi-13B-GGUF |

#### 1. [FunAudioLLM/SenseVoiceSmall-GGUF-audiocpp](https://huggingface.co/FunAudioLLM/SenseVoiceSmall-GGUF-audiocpp) — Claude 제안: **2점**

- 제안 이유: SenseVoiceSmall 계열이며 요청한 포맷
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | FunAudioLLM/SenseVoiceSmall-audiocpp (variant=true, 종류=gguf, 관계 근거=name_heuristic, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.234 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.24 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Usage |
| README 인용 | ## Usage |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 5c3fcfe748a8714216bc135476d5863084fddb72 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [cstr/sensevoice-small-GGUF](https://huggingface.co/cstr/sensevoice-small-GGUF) — Claude 제안: **2점**

- 제안 이유: SenseVoiceSmall 계열이며 요청한 포맷
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | FunAudioLLM/SenseVoiceSmall (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.234 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.13 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | transcription |
| README 인용 | - transcription |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | e1ad67de9d05137a6a0b02beba1fd66e28df6ae4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [handy-computer/SenseVoiceSmall-gguf](https://huggingface.co/handy-computer/SenseVoiceSmall-gguf) — Claude 제안: **2점**

- 제안 이유: SenseVoiceSmall 계열이며 요청한 포맷
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | FunAudioLLM/SenseVoiceSmall (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.234 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.14 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can take a 16 kHz mono WAV (capped at 30 seconds per call) and produces a transcript. |
| README 인용 | Takes a 16 kHz mono WAV (capped at 30 seconds per call, per upstream's direct-inference contract) and produces a transcript. |
| provenance status | verified 12, not_applicable 4, documented 5, unknown 2 |
| revision | ff8f085a8fa2e5ccae0e849ef19ebc6dc18e608b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [voconly-org/sensevoice-small-gguf](https://huggingface.co/voconly-org/sensevoice-small-gguf) — Claude 제안: **2점**

- 제안 이유: SenseVoiceSmall 계열이며 요청한 포맷
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | voconly-org/sensevoice-small-gguf (variant=false, 종류=—, 관계 근거=self, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.234 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.16 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Speech-to-text, subtitle generation, meeting transcription, multilingual transcription |
| README 인용 | - **Use Cases**: Speech-to-text, subtitle generation, meeting transcription, multilingual transcription |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 6394f6d5b1ca5d7b03e6bb7ac6f64d18f082c19e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## lx08 — Helsinki-NLP 의 opus-mt-ko-en 을 쓰려고 해요. 원본이랑 바로 쓸 수 있는 변환본이 있으면 알려 주세요.

- 사용자 의도: 특정 번역 모델과 변환본
- persona / 표현: startup_dev / 기술형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: Helsinki-NLP/opus-mt-ko-en 원본
- **1점 기준**: 같은 모델의 ONNX·CTranslate2 변환본
- 비교 계열: opus-mt-ko-en (`opus-mt-ko-en`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 1 | 2 | 4,014 | 0 | 3 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 질문이 지목한 모델 이름이 아님 (`not_named_model`) | 4,014 | DevQuasar-14/Qwen.Qwen2.5-7B-Instruct-GGUF, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, TheCluster/Gemma-4-26B-A4B-Heretic-MLX-mxfp4 |

#### 1. [Helsinki-NLP/opus-mt-ko-en](https://huggingface.co/Helsinki-NLP/opus-mt-ko-en) — Claude 제안: **2점**

- 제안 이유: opus-mt-ko-en 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Helsinki-NLP/opus-mt-ko-en (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.29 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is suitable for translation tasks. |
| README 인용 | - translation |
| provenance status | verified 11, not_applicable 3, documented 4, unknown 5 |
| revision | e42d1f41b66194e6d10512f8a27bebc1f4f5097e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [Xenova/opus-mt-ko-en](https://huggingface.co/Xenova/opus-mt-ko-en) — Claude 제안: **1점**

- 제안 이유: opus-mt-ko-en 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Helsinki-NLP/opus-mt-ko-en (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | stage1:korean_translation_pair |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | onnx / 3.8 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for translation tasks. |
| README 인용 | js pipeline_tag: translation --- |
| provenance status | verified 11, not_applicable 3, documented 1, unknown 8 |
| revision | d9fa1ac6008242100fecb4fff9b0a5917a1be81f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [gaudi/opus-mt-ko-en-ctranslate2](https://huggingface.co/gaudi/opus-mt-ko-en-ctranslate2) — Claude 제안: **1점**

- 제안 이유: opus-mt-ko-en 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | gaudi/opus-mt-ko-en-ctranslate2 (variant=false, 종류=—, 관계 근거=self, 변환 표지=ctranslate) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | translation (matched: translation) |
| 한국어 근거 | stage1:korean_translation_pair |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.14 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | CTranslate2 is a C++ and Python library for efficient inference with Transformer models. |
| README 인용 | net/CTranslate2/) is a C++ and Python library for efficient inference with Transformer models. |
| provenance status | verified 9, not_applicable 3, documented 3, unknown 8 |
| revision | ef4065ab94ebb50339607271df7746d5dfdb207e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## lx09 — 엔씨소프트가 OCR 전용으로 낸 바르코 비전 1.7B 모델이 있다던데, 그 모델을 찾아 주세요.

- 사용자 의도: VARCO-VISION-2.0-1.7B-OCR 찾기(한국어 표기)
- persona / 표현: backend_dev / 목적형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: NCSOFT/VARCO-VISION-2.0-1.7B-OCR 원본
- **1점 기준**: 같은 모델의 재업로드
- 비교 계열: VARCO-VISION-2.0-1.7B-OCR (`varco-vision-2\.0-1\.7b-ocr`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 1 | 1 | 4,015 | 0 | 2 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 질문이 지목한 모델 이름이 아님 (`not_named_model`) | 4,015 | RedHatAI/Voxtral-Mini-4B-Realtime-2602, mradermacher/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS-GGUF, xtools-at/LFM3-1.7B-AgentOrange-Claude-Code-2xMerge |

#### 1. [NCSOFT/VARCO-VISION-2.0-1.7B-OCR](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B-OCR) — Claude 제안: **2점**

- 제안 이유: VARCO-VISION-2.0-1.7B-OCR 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-1.7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.124 / 40960 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 3.96 |
| 벤치마크 근거 | 점수 3건 저장 |
| 의미 claim (use_cases) | Image-text-to-text pipeline tag. |
| README 인용 | pipeline_tag: image-text-to-text language: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 5c83a19639613ee6ea8bc24070ca1b38305aae69 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [OpenLLM-Korea/VARCO-VISION-2.0-1.7B-OCR](https://huggingface.co/OpenLLM-Korea/VARCO-VISION-2.0-1.7B-OCR) — Claude 제안: **1점**

- 제안 이유: VARCO-VISION-2.0-1.7B-OCR 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-1.7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.124 / 40960 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 3.96 |
| 벤치마크 근거 | 점수 3건 저장 |
| 의미 claim (use_cases) | Image-text-to-text pipeline tag. |
| README 인용 | pipeline_tag: image-text-to-text language: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | f740294ba9becc880f68cefb17e85d403d1eaf95 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## lx10 — llama-3.2-Korean-Bllossom-3B 원본과 GGUF 버전을 같이 찾아 주세요.

- 사용자 의도: 특정 모델과 GGUF 변환본
- persona / 표현: local_user / 기술형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: Bllossom/llama-3.2-Korean-Bllossom-3B 원본
- **1점 기준**: 같은 모델의 GGUF 변환본
- 비교 계열: Bllossom-3B (`llama-3\.2-korean-bllossom-3b`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 1 | 3 | 4,013 | 0 | 4 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 질문이 지목한 모델 이름이 아님 (`not_named_model`) | 4,013 | K-intelligence/Midm-2.0-Base-Instruct, TheCluster/Qwen3.5-9B-Claude-4.6-HighIQ-INSTRUCT-HERETIC-UNCENSORED-MLX-mxfp8, aixk/BAAR8.1-9M |

같은 canonical family 후보가 3개 이상: Bllossom/llama-3.2-Korean-Bllossom-3B 4

#### 1. [Bllossom/llama-3.2-Korean-Bllossom-3B](https://huggingface.co/Bllossom/llama-3.2-Korean-Bllossom-3B) — Claude 제안: **2점**

- 제안 이유: Bllossom-3B 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Bllossom/llama-3.2-Korean-Bllossom-3B (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 3.213 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | llama3.2 / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 5.98 |
| 벤치마크 근거 | 없음 |
| 의미 claim (documented_strengths) | Supported by AICA |
| README 인용 | ## Supported by |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | e68fbb0d9c2a4031b0d61b14014eac1a4810ac2e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [bartowski/llama-3.2-Korean-Bllossom-3B-GGUF](https://huggingface.co/bartowski/llama-3.2-Korean-Bllossom-3B-GGUF) — Claude 제안: **1점**

- 제안 이유: Bllossom-3B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Bllossom/llama-3.2-Korean-Bllossom-3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 3.213 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | llama3.2 / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.27 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Good quality, default size for must use cases, recommended. |
| README 인용 | \| [llama-3.2-Korean-Bllossom-3B-Q4_K_M.gguf](https://huggingface.co/bartowski/llama-3.2-Korean-Bllossom-3B-GGUF/blob/main/llama-3.2-Korean-Bllossom-3B-Q4_K_M.gguf) \| Q4_K_M \| 2.02GB \| false \| Good quality, default size for must use cas… |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 329499d275a426205221cae3916ff63cc5d51f64 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [gaianet/llama-3.2-Korean-Bllossom-3B-GGUF](https://huggingface.co/gaianet/llama-3.2-Korean-Bllossom-3B-GGUF) — Claude 제안: **1점**

- 제안 이유: Bllossom-3B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Bllossom/llama-3.2-Korean-Bllossom-3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 3.213 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | llama3.2 / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.27 |
| 벤치마크 근거 | 없음 |
| 의미 claim (—) | — |
| README 인용 | — |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | c2f348676272f1e9bf0991c9d9899c0dc7f24664 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [second-state/llama-3.2-Korean-Bllossom-3B-GGUF](https://huggingface.co/second-state/llama-3.2-Korean-Bllossom-3B-GGUF) — Claude 제안: **1점**

- 제안 이유: Bllossom-3B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Bllossom/llama-3.2-Korean-Bllossom-3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 3.213 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | llama3.2 / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.27 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Quantized GGUF Models |
| README 인용 | \| Name \| Quant method \| Bits \| Size \| Use case \| |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 20072ecf6772ff27dce757b07fc0018c80ea01f7 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______
