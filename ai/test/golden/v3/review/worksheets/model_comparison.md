# 골든셋 v3 검수 워크시트 — model_comparison (모델 비교)

> 상태: **초안 + 전수 스캔 + 검수 준비 완료**. 아래 점수는 Claude 의 제안이며 정답이 아니다.
>
> 판정 입력: `python test/golden/v3/tools/judge.py <query_id> <model_id> --decision approve|2|1|exclude|hold --reason "…" --by <이름>`

## mc01 — 한국어 문장 임베딩으로 KoSimCSE 와 ko-sroberta 중 뭘 쓸지 비교해 보고 싶어요.

- 사용자 의도: 두 임베딩 계열 비교
- persona / 표현: ml_engineer / 기술형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: 각 계열의 원본 모델
- **1점 기준**: 각 계열의 변형·재업로드
- 비교 계열: KoSimCSE (`kosimcse`), ko-sroberta (`ko-sroberta`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 6 | 0 | 4,011 | 0 | 6 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 지정한 모델 계열이 아님 (`other_family`) | 4,011 | heegyu/kogpt-j-large, hossain0909/Keural-Nova-v1.0, seongmin0127/nero-qwen3-asr-ko-gguf |

#### 1. [BM-K/KoSimCSE-bert](https://huggingface.co/BM-K/KoSimCSE-bert) — Claude 제안: **2점**

- 제안 이유: KoSimCSE 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | BM-K/KoSimCSE-bert (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.111 / 512 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.41 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Users can download the pre-trained models and inference right away. |
| README 인용 | You can download the pre-trained models and inference right away, also it provides environments where individuals can train models. |
| provenance status | verified 14, not_applicable 3, documented 2, unknown 4 |
| revision | 82a53454def3f1a62896fd93d149e52d16dd742d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [BM-K/KoSimCSE-bert-multitask](https://huggingface.co/BM-K/KoSimCSE-bert-multitask) — Claude 제안: **2점**

- 제안 이유: KoSimCSE 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | BM-K/KoSimCSE-bert-multitask (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.111 / 512 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.41 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Users can download the pre-trained models and inference right away. |
| README 인용 | You can download the pre-trained models and inference right away, also it provides environments where individuals can train models. |
| provenance status | verified 14, not_applicable 3, documented 2, unknown 4 |
| revision | 3aa54365eb9557f3b8ee1e39cff87306451abfae |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [BM-K/KoSimCSE-roberta](https://huggingface.co/BM-K/KoSimCSE-roberta) — Claude 제안: **2점**

- 제안 이유: KoSimCSE 원본 모델
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

#### 4. [BM-K/KoSimCSE-roberta-multitask](https://huggingface.co/BM-K/KoSimCSE-roberta-multitask) — Claude 제안: **2점**

- 제안 이유: KoSimCSE 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | BM-K/KoSimCSE-roberta-multitask (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.111 / 514 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.41 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Users can download pre-trained models and inference right away, also it provides environments where individuals can train models. |
| README 인용 | You can download the pre-trained models and inference right away, also it provides environments where individuals can train models. |
| provenance status | verified 14, not_applicable 3, documented 2, unknown 4 |
| revision | c83e4efdf7ee6647e62498ce8738e4efe10e5def |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [jhgan/ko-sroberta-multitask](https://huggingface.co/jhgan/ko-sroberta-multitask) — Claude 제안: **2점**

- 제안 이유: ko-sroberta 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | jhgan/ko-sroberta-multitask (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.111 / 514 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.41 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is used for sentence similarity tasks. |
| README 인용 | --- pipeline_tag: sentence-similarity tags: |
| provenance status | verified 14, not_applicable 3, documented 2, unknown 4 |
| revision | 8fca7c9c98c26599be0e14b9916b11a756a26f19 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [jhgan/ko-sroberta-nli](https://huggingface.co/jhgan/ko-sroberta-nli) — Claude 제안: **2점**

- 제안 이유: ko-sroberta 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | jhgan/ko-sroberta-nli (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 514 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.41 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for sentence similarity tasks. |
| README 인용 | --- pipeline_tag: sentence-similarity tags: |
| provenance status | verified 12, not_applicable 3, documented 2, unknown 6 |
| revision | c4e15f24df2aceadfc931e2a57094726b2409861 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## mc02 — 2B 남짓한 소형 한국어 챗봇으로 EXAONE 3.5 2.4B 와 kanana 1.5 2.1B 중 하나를 고르려고 해요. 둘 다 보여 주세요.

- 사용자 의도: 소형 LLM 두 계열 비교
- persona / 표현: startup_dev / 혼합형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: 각 계열의 원본 instruct 모델
- **1점 기준**: 각 계열의 양자화·변환·재업로드
- 비교 계열: EXAONE-3.5-2.4B (`exaone-3\.5-2\.4b`), kanana-1.5-2.1b (`kanana-1\.5-2\.1b`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 3 | 21 | 3,993 | 0 | 24 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 지정한 모델 계열이 아님 (`other_family`) | 3,992 | cadazar/han2han-it, mlx-community/LFM2.5-24B-A2B-Preview-8bit, nvidia/nemotron-3.5-asr-streaming-0.6b |
| variant 관계가 질문과 맞지 않음 (`variant_mismatch`) | 1 | LGAI-EXAONE/EXAONE-Deep-2.4B |

같은 canonical family 후보가 3개 이상: LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct 12, kakaocorp/kanana-1.5-2.1b-instruct-2505 6

#### 1. [JJS0321/kanana-1.5-2.1b-instruct-2505-gguf](https://huggingface.co/JJS0321/kanana-1.5-2.1b-instruct-2505-gguf) — Claude 제안: **1점**

- 제안 이유: kanana-1.5-2.1b 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | kakaocorp/kanana-1.5-2.1b-instruct-2505 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.317 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.42 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for text generation tasks. |
| README 인용 | pipeline_tag: text-generation --- |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 06c3480f487f59b545975c774a9c53d5dbbfa945 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct) — Claude 제안: **2점**

- 제안 이유: EXAONE-3.5-2.4B 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.405 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 8.96 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Each model demonstrates state-of-the-art performance in real-world use cases and long-context understanding, while remaining competitive in general domains compared to recently released models of similar sizes. |
| README 인용 | Each model demonstrates state-of-the-art performance in real-world use cases and long-context understanding, while remaining competitive in general domains compared to recently released models of similar sizes. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | ccce25bd39c141fe053e0bc75818a8f5fe962802 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct-AWQ](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct-AWQ) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct-AWQ (variant=false, 종류=—, 관계 근거=self, 변환 표지=AWQ) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.667 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 2.01 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Each model demonstrates state-of-the-art performance in real-world use cases and long-context understanding. |
| README 인용 | Each model demonstrates state-of-the-art performance in real-world use cases and long-context understanding, while remaining competitive in general domains compared to recently released models of similar sizes. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 0e45bc0d031c944f1e1073f59b20b02967bff288 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct-GGUF](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct-GGUF) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct-GGUF (variant=false, 종류=—, 관계 근거=self, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.667 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.41 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model demonstrates state-of-the-art performance in real-world use cases and long-context understanding. |
| README 인용 | Each model demonstrates state-of-the-art performance in real-world use cases and long-context understanding, while remaining competitive in general domains compared to recently released models of similar sizes. |
| provenance status | verified 13, not_applicable 4, documented 5, unknown 1 |
| revision | 142acae803a41c206e8d0fa978c6102c748911bb |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [Mungert/EXAONE-Deep-2.4B-GGUF](https://huggingface.co/Mungert/EXAONE-Deep-2.4B-GGUF) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `canonical_model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.405 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.63 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Quantization reduces model size and memory usage while maintaining as much accuracy as possible. |
| README 인용 | Quantization reduces model size and memory usage while maintaining as much accuracy as possible. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | cba4c35a6cb8a97390e2120642442a629eba743f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [QuantFactory/EXAONE-Deep-2.4B-GGUF](https://huggingface.co/QuantFactory/EXAONE-Deep-2.4B-GGUF) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `canonical_model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Quant) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.667 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.02 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Ensure the model starts with `<thought>\n` for reasoning steps to maintain output quality. |
| README 인용 | 1. Ensure the model starts with `<thought>\n` for reasoning steps. The model's output quality may be degraded when you omit it. You can easily apply this feature by using `tokenizer.apply_chat_template()` with `add_generation_prompt=True`. … |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | f63c9008ce8c64eb8facd38dd8efd98345019226 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [TaeyoungLeeJack/kanana-1.5-2.1b-instruct-2505-Q4_K_M-GGUF](https://huggingface.co/TaeyoungLeeJack/kanana-1.5-2.1b-instruct-2505-Q4_K_M-GGUF) — Claude 제안: **1점**

- 제안 이유: kanana-1.5-2.1b 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | kakaocorp/kanana-1.5-2.1b-instruct-2505 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Q4_) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.317 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.42 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used directly through the provided usage steps. |
| README 인용 | Note: You can also use this checkpoint directly through the [usage steps](https://github. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 9a6c4bf9e13fea91c3100a891e7312dd9911f098 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [ThomasBaruzier/EXAONE-3.5-2.4B-Instruct-GGUF](https://huggingface.co/ThomasBaruzier/EXAONE-3.5-2.4B-Instruct-GGUF) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | ThomasBaruzier/EXAONE-3.5-2.4B-Instruct-GGUF (variant=false, 종류=—, 관계 근거=self, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.667 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.68 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Each model demonstrates state-of-the-art performance in real-world use cases and long-context understanding, while remaining competitive in general domains compared to recently released models of similar sizes. |
| README 인용 | Each model demonstrates state-of-the-art performance in real-world use cases and long-context understanding, while remaining competitive in general domains compared to recently released models of similar sizes. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | ef5b82f1ddc1a118755fbcb8fc4ff201613372d4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [bartowski/EXAONE-3.5-2.4B-Instruct-GGUF](https://huggingface.co/bartowski/EXAONE-3.5-2.4B-Instruct-GGUF) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.667 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.95 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Good quality, default size for most use cases, *recommended*. |
| README 인용 | \| [EXAONE-3.5-2.4B-Instruct-Q4_K_M.gguf](https://huggingface.co/bartowski/EXAONE-3.5-2.4B-Instruct-GGUF/blob/main/EXAONE-3.5-2.4B-Instruct-Q4_K_M.gguf) \| Q4_K_M \| 1.64GB \| false \| Good quality, default size for most use cases, *recomme… |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 21324b511a882f496db1ef4e3f2ec25ac4da9b40 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [beomi/EXAONE-3.5-2.4B-Instruct-Llamafied](https://huggingface.co/beomi/EXAONE-3.5-2.4B-Instruct-Llamafied) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | beomi/EXAONE-3.5-2.4B-Instruct-Llamafied (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.667 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 4.97 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for various text generation applications. |
| README 인용 | pipeline_tag: text-generation library_name: transformers --- |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 4fefa7c23639a248ca9b1d9fc42f5239b530d29b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [gaianet/EXAONE-3.5-2.4B-Instruct-GGUF](https://huggingface.co/gaianet/EXAONE-3.5-2.4B-Instruct-GGUF) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.405 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.94 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for various text generation applications. |
| README 인용 | pipeline_tag: text-generation library_name: transformers --- |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 99a6695ae47d8ae210e6ec1a55f7511669bc9ee9 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [kakaocorp/kanana-1.5-2.1b-base](https://huggingface.co/kakaocorp/kanana-1.5-2.1b-base) — Claude 제안: **2점**

- 제안 이유: kanana-1.5-2.1b 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | kakaocorp/kanana-1.5-2.1b-base (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.087 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 3.89 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model presents substantial enhancements in coding, mathematics, and function calling capabilities, enabling broader application to more complex real-world problems. |
| README 인용 | 5`, a newly introduced version of the Kanana model family, presents substantial enhancements in **coding, mathematics, and function calling capabilities** over the previous version, enabling broader application to more complex real-world pr… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 83fdd4426138b2becb3b33197126de2e4f5dfcd3 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [kakaocorp/kanana-1.5-2.1b-instruct-2505](https://huggingface.co/kakaocorp/kanana-1.5-2.1b-instruct-2505) — Claude 제안: **2점**

- 제안 이유: kanana-1.5-2.1b 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | kakaocorp/kanana-1.5-2.1b-instruct-2505 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.317 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 4.32 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model enables broader application to more complex real-world problems. |
| README 인용 | 5`, a newly introduced version of the Kanana model family, presents substantial enhancements in **coding, mathematics, and function calling capabilities** over the previous version, enabling broader application to more complex real-world pr… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 7df4bc35ccd610e451809d7106e1c3cf82bfd44c |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 14. [lmstudio-community/EXAONE-3.5-2.4B-Instruct-GGUF](https://huggingface.co/lmstudio-community/EXAONE-3.5-2.4B-Instruct-GGUF) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.667 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.36 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | quantized_by: bartowski |
| README 인용 | --- quantized_by: bartowski pipeline_tag: text-generation license_name: exaone language: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 347ad15365d7e4c4fb0d206e07b87bdefe9e67d9 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 15. [mobilint/EAGLE3-EXAONE-3.5-2.4B-Instruct](https://huggingface.co/mobilint/EAGLE3-EXAONE-3.5-2.4B-Instruct) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.524 / 16384 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.47 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for various text generation applications. |
| README 인용 | pipeline_tag: text-generation base_model: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | ac501afca86f37bb1fd61884792002d5704bcdf0 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 16. [mobilint/EXAONE-3.5-2.4B-Instruct](https://huggingface.co/mobilint/EXAONE-3.5-2.4B-Instruct) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.262 / 16384 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.98 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for various text generation applications. |
| README 인용 | pipeline_tag: text-generation tags: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | a3a71cb4b1d01cd6fefee4446707e2692473c63b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 17. [mobilint/EXAONE-3.5-2.4B-Instruct-Batch16](https://huggingface.co/mobilint/EXAONE-3.5-2.4B-Instruct-Batch16) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.262 / 4096 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.98 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is suitable for text-generation tasks. |
| README 인용 | pipeline_tag: text-generation tags: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 11e61f4539a10b3aa0e1aa4313e846a0b012f7ce |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 18. [mobilint/EXAONE-3.5-2.4B-Instruct-regulus-rb-usb](https://huggingface.co/mobilint/EXAONE-3.5-2.4B-Instruct-regulus-rb-usb) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.262 / 4096 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.98 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is tagged for text-generation tasks. |
| README 인용 | pipeline_tag: text-generation tags: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 52492a3ff0eff2b8293c2c4bc86c2b580ef56a3f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 19. [mobilint/kanana-1.5-2.1b-instruct-2505](https://huggingface.co/mobilint/kanana-1.5-2.1b-instruct-2505) — Claude 제안: **1점**

- 제안 이유: kanana-1.5-2.1b 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | kakaocorp/kanana-1.5-2.1b-instruct-2505 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.23 / 16384 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.86 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for various text generation applications. |
| README 인용 | pipeline_tag: text-generation base_model: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 0e19dcdfc0cda0838fa43579cacb46cc77bd51ff |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 20. [mobilint/kanana-1.5-2.1b-instruct-2505-regulus-rb-usb](https://huggingface.co/mobilint/kanana-1.5-2.1b-instruct-2505-regulus-rb-usb) — Claude 제안: **1점**

- 제안 이유: kanana-1.5-2.1b 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | kakaocorp/kanana-1.5-2.1b-instruct-2505 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.23 / 4096 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.86 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for text generation tasks. |
| README 인용 | pipeline_tag: text-generation base_model: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | cac09b7585c5e001e3bfaab3faae6dc9b26ee06a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 21. [second-state/EXAONE-3.5-2.4B-Instruct-GGUF](https://huggingface.co/second-state/EXAONE-3.5-2.4B-Instruct-GGUF) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.405 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.94 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used in various applications as indicated in the quantized models table. |
| README 인용 | \| Name \| Quant method \| Bits \| Size \| Use case \| |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 3667916343c8f88cc6c2b4da3e417262a1db31c8 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 22. [tensorblock/EXAONE-3.5-2.4B-Instruct-GGUF](https://huggingface.co/tensorblock/EXAONE-3.5-2.4B-Instruct-GGUF) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.405 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.94 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for text generation tasks. |
| README 인용 | pipeline_tag: text-generation library_name: transformers base_model: LGAI-EXAONE/EXAONE-3. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 0ae05bf5e5fe58e93619ae86e53e329d2af85a14 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 23. [tensorblock/EXAONE-3.5-2.4B-Instruct-Llamafied-GGUF](https://huggingface.co/tensorblock/EXAONE-3.5-2.4B-Instruct-Llamafied-GGUF) — Claude 제안: **1점**

- 제안 이유: EXAONE-3.5-2.4B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | beomi/EXAONE-3.5-2.4B-Instruct-Llamafied (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.667 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.02 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for text generation tasks. |
| README 인용 | pipeline_tag: text-generation library_name: transformers base_model: beomi/EXAONE-3. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | bfb5638cb6e3dd33c1d3e737481381387999ac58 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 24. [tensorblock/kakaocorp_kanana-1.5-2.1b-instruct-2505-GGUF](https://huggingface.co/tensorblock/kakaocorp_kanana-1.5-2.1b-instruct-2505-GGUF) — Claude 제안: **1점**

- 제안 이유: kanana-1.5-2.1b 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | kakaocorp/kanana-1.5-2.1b-instruct-2505 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.317 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.94 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is suitable for text generation tasks. |
| README 인용 | 0 pipeline_tag: text-generation model_id: kakaocorp/kanana-1. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 5ac0a0997ecec6c74a171daeccca1e3e0e8af8c5 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## mc03 — 다국어 번역 서버를 띄우려는데 NLLB-200 distilled 600M 이랑 M2M100 418M 을 비교하고 싶어요.

- 사용자 의도: 두 번역 모델 비교
- persona / 표현: backend_dev / 기술형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: 각 모델의 원본
- **1점 기준**: 각 모델의 CTranslate2·ONNX 등 변환본
- 비교 계열: nllb-200-distilled-600M (`nllb-200-distilled-600m`), m2m100_418M (`m2m100.?418m`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 1 | 10 | 4,006 | 0 | 11 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 지정한 모델 계열이 아님 (`other_family`) | 4,006 | Dollaronthetoes/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic, Horizon-Labs/prompt-injection-guard-base, facebook/fasttext-ko-vectors |

같은 canonical family 후보가 3개 이상: facebook/nllb-200-distilled-600M 4

#### 1. [JustFrederik/nllb-200-distilled-600M-ct2](https://huggingface.co/JustFrederik/nllb-200-distilled-600M-ct2) — Claude 제안: **1점**

- 제안 이유: nllb-200-distilled-600M 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | JustFrederik/nllb-200-distilled-600M-ct2 (variant=false, 종류=—, 관계 근거=self, 변환 표지=ct2) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 2.3 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | translation |
| README 인용 | - translation |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 3800669f1c0c25eec9eab315374a0c6d2ade709c |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [JustFrederik/nllb-200-distilled-600M-ct2-float16](https://huggingface.co/JustFrederik/nllb-200-distilled-600M-ct2-float16) — Claude 제안: **1점**

- 제안 이유: nllb-200-distilled-600M 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | JustFrederik/nllb-200-distilled-600M-ct2-float16 (variant=false, 종류=—, 관계 근거=self, 변환 표지=ct2) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 1.15 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | translation |
| README 인용 | - translation |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 9a293c97317609fe6a1782c672a7f51443086549 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [JustFrederik/nllb-200-distilled-600M-ct2-int8](https://huggingface.co/JustFrederik/nllb-200-distilled-600M-ct2-int8) — Claude 제안: **1점**

- 제안 이유: nllb-200-distilled-600M 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | JustFrederik/nllb-200-distilled-600M-ct2-int8 (variant=false, 종류=—, 관계 근거=self, 변환 표지=ct2) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.58 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | translation |
| README 인용 | - translation |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 302d78f00e6fdb50a1064059df7c392b735e9d05 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [Rohith04/ct2fast_m2m100_418M](https://huggingface.co/Rohith04/ct2fast_m2m100_418M) — Claude 제안: **1점**

- 제안 이유: m2m100_418M 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Rohith04/ct2fast_m2m100_418M (variant=false, 종류=—, 관계 근거=self, 변환 표지=ct2) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.45 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is optimized for fast inference using CTranslate2. |
| README 인용 | co/facebook/m2m100_418M) from Facebook AI, optimized for fast inference using CTranslate2. |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 433124554a6591f9b40da435e2f8c39c183cd53a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [Xenova/nllb-200-distilled-600M](https://huggingface.co/Xenova/nllb-200-distilled-600M) — Claude 제안: **1점**

- 제안 이유: nllb-200-distilled-600M 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | facebook/nllb-200-distilled-600M (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | onnx / 31.88 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for multilingual translation tasks. |
| README 인용 | js pipeline_tag: translation language: |
| provenance status | verified 11, not_applicable 3, documented 4, unknown 5 |
| revision | 261c31d1a5732c67cdd16d80e8d6088507c7ccea |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [entai2965/m2m100-418M-ctranslate2](https://huggingface.co/entai2965/m2m100-418M-ctranslate2) — Claude 제안: **1점**

- 제안 이유: m2m100_418M 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | facebook/m2m100_418M (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=ctranslate) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / — |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 1.81 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | M2M100 is a multilingual encoder-decoder (seq-to-seq) model trained for Many-to-Many multilingual translation. |
| README 인용 | M2M100 is a multilingual encoder-decoder (seq-to-seq) model trained for Many-to-Many multilingual translation. |
| provenance status | verified 9, not_applicable 3, documented 4, unknown 7 |
| revision | 85e2e73f4250c62a14504486d4c7b24ce0cff7ad |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [entai2965/nllb-200-distilled-600M-ctranslate2](https://huggingface.co/entai2965/nllb-200-distilled-600M-ctranslate2) — Claude 제안: **1점**

- 제안 이유: nllb-200-distilled-600M 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | facebook/nllb-200-distilled-600M (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=ctranslate) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 2.3 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | NLLB-200 allows for single sentence translation among 200 languages. |
| README 인용 | - Primary intended uses: NLLB-200 is a machine translation model primarily intended for research in machine translation, - especially for low-resource languages. It allows for single sentence translation among 200 languages. Information on … |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 86876131d0a16b17ced0a5c558fdc3e4613ae545 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M) — Claude 제안: **2점**

- 제안 이유: nllb-200-distilled-600M 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | facebook/nllb-200-distilled-600M (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 2.29 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | NLLB-200 allows for single sentence translation among 200 languages. |
| README 인용 | - Primary intended uses: NLLB-200 is a machine translation model primarily intended for research in machine translation, - especially for low-resource languages. It allows for single sentence translation among 200 languages. Information on … |
| provenance status | verified 12, not_applicable 3, documented 4, unknown 4 |
| revision | f8d333a098d19b4fd9a8b18f94170487ad3f821d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [huggingworld/m2m100_418M](https://huggingface.co/huggingworld/m2m100_418M) — Claude 제안: **1점**

- 제안 이유: m2m100_418M 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Xenova/m2m100_418M (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx / 0.59 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used to translate text from Hindi to French. |
| README 인용 | ```js import { pipeline } from '@huggingface/transformers';  // Create a translation pipeline const translator = await pipeline('translation', 'huggingworld/m2m100_418M');  // Translate text from Hindi to French const output = await transla… |
| provenance status | verified 11, not_applicable 3, documented 4, unknown 5 |
| revision | 48f06c0fec544323fcf1546e312a617d962d3653 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [mijuanlo/nllb-200-distilled-600M-ct2-int8](https://huggingface.co/mijuanlo/nllb-200-distilled-600M-ct2-int8) — Claude 제안: **1점**

- 제안 이유: nllb-200-distilled-600M 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | mijuanlo/nllb-200-distilled-600M-ct2-int8 (variant=false, 종류=—, 관계 근거=self, 변환 표지=ct2) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.58 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Machine translation for various languages. |
| README 인용 | - translation |
| provenance status | verified 12, not_applicable 3, documented 4, unknown 4 |
| revision | 16bc5ff0482f9f1c0d35bdef950721ce58640789 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [xxliam/koubox-nllb-600m-ja-en-ko-zh-oral-ct2](https://huggingface.co/xxliam/koubox-nllb-600m-ja-en-ko-zh-oral-ct2) — Claude 제안: **1점**

- 제안 이유: nllb-200-distilled-600M 계열의 변환·양자화·재업로드
- 근거 위치: `canonical_model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | facebook/nllb-200-distilled-600M (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=ct2) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 1.15 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Translation tasks |
| README 인용 | base_model: facebook/nllb-200-distilled-600M pipeline_tag: translation --- |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 24305bd8f83166289e19283306c84b9af620b289 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## mc04 — 해외 고객 문의를 한국어로 옮기는 기능에 구글 MADLAD 번역 모델과 헬싱키대 opus-mt 한영 모델 중 무엇이 나을지 비교 자료가 필요해요.

- 사용자 의도: MADLAD-400 과 opus-mt ko-en 비교
- persona / 표현: korean_service_planner / 목적형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: 각 계열의 원본(google/madlad400-*-mt, Helsinki-NLP/opus-mt-*ko-en)
- **1점 기준**: 각 계열의 변환·양자화·재업로드
- 비교 계열: MADLAD-400 (`madlad400-\d+b-mt`), opus-mt ko-en (`opus-mt-(tc-big-)?ko-en`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 6 | 19 | 3,992 | 0 | 25 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 지정한 모델 계열이 아님 (`other_family`) | 3,992 | bartowski/aya-23-35B-GGUF, litert-community/Qwen3-ASR-0.6B, tencent/HY-MT1.5-7B-FP8 |

같은 canonical family 후보가 3개 이상: google/madlad400-3b-mt 7

#### 1. [Abu-Dju/madlad400-10b-mt](https://huggingface.co/Abu-Dju/madlad400-10b-mt) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Abu-Dju/madlad400-10b-mt (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 10.713 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 13.8 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: translation |
| README 인용 | pipeline_tag: translation |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 09a3da57c6ea0a57eb6af3534469c2f6170d54c4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [Helsinki-NLP/opus-mt-ko-en](https://huggingface.co/Helsinki-NLP/opus-mt-ko-en) — Claude 제안: **2점**

- 제안 이유: opus-mt ko-en 원본 모델
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

#### 3. [Helsinki-NLP/opus-mt-tc-big-ko-en](https://huggingface.co/Helsinki-NLP/opus-mt-tc-big-ko-en) — Claude 제안: **2점**

- 제안 이유: opus-mt ko-en 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Helsinki-NLP/opus-mt-tc-big-ko-en (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.209 / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-4.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.39 |
| 벤치마크 근거 | 점수 4건 저장 |
| 의미 claim (use_cases) | translation |
| README 인용 | - translation |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | fa26583a41d95346933f26b4cb8f9b700da0d445 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [Heng666/madlad400-3b-mt-ct2-int8](https://huggingface.co/Heng666/madlad400-3b-mt-ct2-int8) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Heng666/madlad400-3b-mt-ct2-int8 (variant=false, 종류=—, 관계 근거=self, 변환 표지=ct2) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / — |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 2.75 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: translation |
| README 인용 | pipeline_tag: translation metrics: |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | b963b846ca4a5c106b7c64b863802599993e5f3b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [Nextcloud-AI/madlad400-3b-mt-ct2-int8](https://huggingface.co/Nextcloud-AI/madlad400-3b-mt-ct2-int8) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Nextcloud-AI/madlad400-3b-mt-ct2-int8 (variant=false, 종류=—, 관계 근거=self, 변환 표지=ct2) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / — |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 2.75 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: translation |
| README 인용 | pipeline_tag: translation |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | aa32bbdeba7880eff2096ec044cb155a340a9400 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [Nextcloud-AI/madlad400-3b-mt-ct2-int8_float32](https://huggingface.co/Nextcloud-AI/madlad400-3b-mt-ct2-int8_float32) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Nextcloud-AI/madlad400-3b-mt-ct2-int8_float32 (variant=true, 종류=int8, 관계 근거=name_heuristic, 변환 표지=ct2) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 2.75 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: translation |
| README 인용 | pipeline_tag: translation |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | b8da9b9ff845763271d2d494128daf27de122ed3 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [NostraEmpire/mirror-madlad400-3b-mt](https://huggingface.co/NostraEmpire/mirror-madlad400-3b-mt) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | NostraEmpire/mirror-madlad400-3b-mt (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.94 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 3.62 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: translation |
| README 인용 | pipeline_tag: translation |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 861cfd34cd0d5a1afcacbd917f85b8a5158df55e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [Xenova/opus-mt-ko-en](https://huggingface.co/Xenova/opus-mt-ko-en) — Claude 제안: **1점**

- 제안 이유: opus-mt ko-en 계열의 변환·양자화·재업로드
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

#### 9. [enacimie/madlad400-3b-mt-Q4_K_M-GGUF](https://huggingface.co/enacimie/madlad400-3b-mt-Q4_K_M-GGUF) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | google/madlad400-3b-mt (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Q4_) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.94 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.73 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Can be used for translation tasks. |
| README 인용 | pipeline_tag: translation widget: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | dc0d3d90f915b094abf0be27fd6d168aec2995c0 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [enacimie/madlad400-7b-mt-Q4_K_M-GGUF](https://huggingface.co/enacimie/madlad400-7b-mt-Q4_K_M-GGUF) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | google/madlad400-7b-mt (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Q4_) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 8.297 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 4.84 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Can be used for translation tasks. |
| README 인용 | pipeline_tag: translation widget: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 4e2c4a5fe3c509eb3d260d9dce49ce28e96a71d5 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [fernandoruiz/madlad400-3b-mt-Q4_K_S-GGUF](https://huggingface.co/fernandoruiz/madlad400-3b-mt-Q4_K_S-GGUF) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | google/madlad400-3b-mt (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Q4_) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.94 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.61 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for translating text to English. |
| README 인용 | example_title: Translation to English |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 729a608ecde19c586df74775843a0e57f7dda969 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [gaudi/opus-mt-ko-en-ctranslate2](https://huggingface.co/gaudi/opus-mt-ko-en-ctranslate2) — Claude 제안: **1점**

- 제안 이유: opus-mt ko-en 계열의 변환·양자화·재업로드
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

#### 13. [google/madlad400-10b-mt](https://huggingface.co/google/madlad400-10b-mt) — Claude 제안: **2점**

- 제안 이유: MADLAD-400 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | google/madlad400-10b-mt (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 10.713 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 13.8 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: translation |
| README 인용 | pipeline_tag: translation |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 9f2797629c31e69617186dbe5f0ca43bf662f36d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 14. [google/madlad400-3b-mt](https://huggingface.co/google/madlad400-3b-mt) — Claude 제안: **2점**

- 제안 이유: MADLAD-400 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | google/madlad400-3b-mt (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.94 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 3.62 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: translation |
| README 인용 | pipeline_tag: translation |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | fa184c675da0b5c9e1c8694fccd4e12e2d422094 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 15. [google/madlad400-7b-mt](https://huggingface.co/google/madlad400-7b-mt) — Claude 제안: **2점**

- 제안 이유: MADLAD-400 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | google/madlad400-7b-mt (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 8.297 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 10.69 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: translation |
| README 인용 | pipeline_tag: translation |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 1ff63ce7ddd571a69d45cad9672c553428419671 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 16. [google/madlad400-7b-mt-bt](https://huggingface.co/google/madlad400-7b-mt-bt) — Claude 제안: **2점**

- 제안 이유: MADLAD-400 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | google/madlad400-7b-mt-bt (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 8.297 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 10.69 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: translation |
| README 인용 | pipeline_tag: translation |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 1259294dcefa2a4d8e0167ad418fdb47cfaeeca3 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 17. [jbochi/madlad400-10b-mt](https://huggingface.co/jbochi/madlad400-10b-mt) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | jbochi/madlad400-10b-mt (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 10.713 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 13.8 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: translation |
| README 인용 | pipeline_tag: translation |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 584d043bba2b760b7c4b7ad3fe07573607156cc5 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 18. [jbochi/madlad400-3b-mt](https://huggingface.co/jbochi/madlad400-3b-mt) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | jbochi/madlad400-3b-mt (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.94 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 3.62 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: translation |
| README 인용 | pipeline_tag: translation |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | bb45f1851bf13a0b8f4fcd9ecadf2cdb7cf22439 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 19. [jbochi/madlad400-7b-mt](https://huggingface.co/jbochi/madlad400-7b-mt) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | jbochi/madlad400-7b-mt (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 8.297 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 10.69 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: translation |
| README 인용 | pipeline_tag: translation |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | db6c36620e757fc56e37f578c3bed31414725a56 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 20. [jbochi/madlad400-7b-mt-bt](https://huggingface.co/jbochi/madlad400-7b-mt-bt) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | jbochi/madlad400-7b-mt-bt (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 8.297 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 10.69 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: translation |
| README 인용 | pipeline_tag: translation |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | ad65e3d0e133396588a24c53949875f790edc403 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 21. [mtsdurica/madlad400-3b-mt-Q4_0-GGUF](https://huggingface.co/mtsdurica/madlad400-3b-mt-Q4_0-GGUF) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | google/madlad400-3b-mt (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Q4_) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.94 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.61 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for translating text to English. |
| README 인용 | example_title: Translation to English |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 458174c8fbbf9448ee5df42d5e095688138a7478 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 22. [mtsdurica/madlad400-3b-mt-Q4_K_M-GGUF](https://huggingface.co/mtsdurica/madlad400-3b-mt-Q4_K_M-GGUF) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | google/madlad400-3b-mt (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Q4_) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.94 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.73 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for translating text to English. |
| README 인용 | example_title: Translation to English |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 7f55e827c4c2fd1fdc52893879e18966d2867dba |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 23. [mtsdurica/madlad400-7b-mt-Q4_K_M-GGUF](https://huggingface.co/mtsdurica/madlad400-7b-mt-Q4_K_M-GGUF) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | jbochi/madlad400-7b-mt (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Q4_) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 8.297 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 4.84 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for translating text to English. |
| README 인용 | example_title: Translation to English |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 5cd6a17969e501252ef6e684fe2c4da27cbd8e58 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 24. [notjjustnumbers/madlad400-3b-mt-Q4_K_M-GGUF](https://huggingface.co/notjjustnumbers/madlad400-3b-mt-Q4_K_M-GGUF) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | google/madlad400-3b-mt (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Q4_) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.94 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.73 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for translating text to English. |
| README 인용 | example_title: Translation to English |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | b325d397b871d944f12cd98ddff3a969cc8fec6e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 25. [snowkitties/madlad400-3b-mt-Q4_K_M-GGUF](https://huggingface.co/snowkitties/madlad400-3b-mt-Q4_K_M-GGUF) — Claude 제안: **1점**

- 제안 이유: MADLAD-400 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | google/madlad400-3b-mt (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Q4_) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.94 / 512 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.73 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Can be used for translation tasks. |
| README 인용 | pipeline_tag: translation widget: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 557727216c9d764908660bc6b803014739bdfb78 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## mc05 — 저사양 PC 용으로 믿음 2.0 Mini 랑 EXAONE 4.0 1.2B 를 비교해 보고 싶어요.

- 사용자 의도: 소형 한국어 LLM 두 개 비교
- persona / 표현: limited_gpu / 혼합형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: 각 모델의 원본
- **1점 기준**: 각 모델의 양자화·변환본
- 비교 계열: Midm-2.0-Mini (`midm-2\.0-mini`), EXAONE-4.0-1.2B (`exaone-4\.0-1\.2b`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 2 | 10 | 4,005 | 0 | 12 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 지정한 모델 계열이 아님 (`other_family`) | 4,005 | LoneStriker/openbuddy-deepseek-10b-v17.1-4k-GGUF, TheCluster/Qwen3.5-122B-A10B-Heretic-v2-MLX-mixed-3.8bit, mradermacher/CURE-MED-14B-GGUF |

같은 canonical family 후보가 3개 이상: LGAI-EXAONE/EXAONE-4.0-1.2B 9

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

#### 2. [LGAI-EXAONE/EXAONE-4.0-1.2B](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-1.2B) — Claude 제안: **2점**

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

#### 3. [LGAI-EXAONE/EXAONE-4.0-1.2B-AWQ](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-1.2B-AWQ) — Claude 제안: **1점**

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

#### 4. [LGAI-EXAONE/EXAONE-4.0-1.2B-FP8](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-1.2B-FP8) — Claude 제안: **1점**

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

#### 5. [LGAI-EXAONE/EXAONE-4.0-1.2B-GGUF](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-1.2B-GGUF) — Claude 제안: **1점**

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

#### 6. [LGAI-EXAONE/EXAONE-4.0-1.2B-GPTQ-Int8](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-1.2B-GPTQ-Int8) — Claude 제안: **1점**

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

#### 7. [Mungert/EXAONE-4.0-1.2B-GGUF](https://huggingface.co/Mungert/EXAONE-4.0-1.2B-GGUF) — Claude 제안: **1점**

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

#### 8. [Open4bits/EXAONE-4.0-1.2B-gguf](https://huggingface.co/Open4bits/EXAONE-4.0-1.2B-gguf) — Claude 제안: **1점**

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

#### 9. [lmstudio-community/EXAONE-4.0-1.2B-MLX-4bit](https://huggingface.co/lmstudio-community/EXAONE-4.0-1.2B-MLX-4bit) — Claude 제안: **1점**

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

#### 10. [mlx-community/exaone-4.0-1.2b-4bit](https://huggingface.co/mlx-community/exaone-4.0-1.2b-4bit) — Claude 제안: **1점**

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

#### 11. [mobilint/EXAONE-4.0-1.2B](https://huggingface.co/mobilint/EXAONE-4.0-1.2B) — Claude 제안: **1점**

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

#### 12. [mykor/Midm-2.0-Mini-Instruct-gguf](https://huggingface.co/mykor/Midm-2.0-Mini-Instruct-gguf) — Claude 제안: **1점**

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

## mc06 — 한국어 검색용 임베딩으로 KURE-v3 와 bge-m3-korean 을 비교하려고 합니다.

- 사용자 의도: 두 한국어 임베딩 비교
- persona / 표현: ml_engineer / 기술형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: 각 모델의 원본
- **1점 기준**: 각 모델의 GGUF 등 변환본
- 비교 계열: KURE-v3 (`kure-v3`), bge-m3-korean (`bge-m3-korean`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 2 | 2 | 4,013 | 0 | 4 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 지정한 모델 계열이 아님 (`other_family`) | 4,013 | fla-hub/rwkv7-0.4B-world, kwkwkwkwpark/klue-roberta-base-klue-sts-mrc, lmstudio-community/Mistral-Large-Instruct-2407-GGUF |

#### 1. [mradermacher/KURE-v3-GGUF](https://huggingface.co/mradermacher/KURE-v3-GGUF) — Claude 제안: **1점**

- 제안 이유: KURE-v3 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | nlpai-lab/KURE-v3 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.141 / 262144 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.51 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface. |
| README 인용 | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 6bbe4e93f6eb212054343b99e68311e7a8cd2993 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [mradermacher/KURE-v3-i1-GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF) — Claude 제안: **1점**

- 제안 이유: KURE-v3 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | nlpai-lab/KURE-v3 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.141 / 262144 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.35 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface. |
| README 인용 | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 69c6ba8dfa49c8e2c714e849fbb5ea83bc85dafd |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [nlpai-lab/KURE-v3](https://huggingface.co/nlpai-lab/KURE-v3) — Claude 제안: **2점**

- 제안 이유: KURE-v3 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | nvidia/Nemotron-3-Embed-1B-BF16 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.141 / 262144 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 2.13 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | base_model: nvidia/Nemotron-3-Embed-1B-BF16 |
| README 인용 | base_model: nvidia/Nemotron-3-Embed-1B-BF16 pipeline_tag: sentence-similarity library_name: sentence-transformers license: apache-2. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 73d5e710bc0b1f324a60746922cbad6d38f480d4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [upskyy/bge-m3-korean](https://huggingface.co/upskyy/bge-m3-korean) — Claude 제안: **2점**

- 제안 이유: bge-m3-korean 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | BAAI/bge-m3 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.568 / 8194 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 2.12 |
| 벤치마크 근거 | 점수 10건 저장 |
| 의미 claim (use_cases) | The model can be used for sentence similarity tasks. |
| README 인용 | ```python from sentence_transformers import SentenceTransformer  # Download from the 🤗 Hub model = SentenceTransformer("upskyy/bge-m3-korean")  # Run inference sentences = [     '아이를 가진 엄마가 해변을 걷는다.',     '두 사람이 해변을 걷는다.',     '한 남자가 해변에서 개… |
| provenance status | verified 14, not_applicable 3, documented 2, unknown 4 |
| revision | 069ae0627320935e4b2879522edbb54650b59bf5 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## mc07 — 회의 녹음 받아쓰기에 SenseVoice Small 을 쓸지, 한국어로 파인튜닝된 Whisper large-v3-turbo 를 쓸지 고민이에요. 두 쪽 후보를 다 보여 주세요.

- 사용자 의도: 두 STT 계열 비교
- persona / 표현: korean_service_planner / 목적형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `tasks` | automatic-speech-recognition | 받아쓰기(음성 인식) | 예 |

- **2점 기준**: 각 계열의 원본(FunAudioLLM/SenseVoiceSmall, 한국어 파인튜닝 whisper-large-v3-turbo)
- **1점 기준**: 각 계열의 변환·양자화본
- 비교 계열: SenseVoiceSmall (`sense-?voice-?small`), whisper-large-v3-turbo-korean (`whisper.{0,3}large.{0,3}v3.{0,3}turbo.{0,3}kor`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 321 | 3 | 9 | 309 | 0 | 12 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 지정한 모델 계열이 아님 (`other_family`) | 309 | Edge0/ARK-ASR-0.6B, avericaai/Fun-ASR-MLT-Nano-2512-gguf, viethang/cohere-transcribe-03-2026 |

같은 canonical family 후보가 3개 이상: FunAudioLLM/SenseVoiceSmall 6, openai/whisper-large-v3-turbo 3

#### 1. [DennisHuang648/SenseVoiceSmall-onnx](https://huggingface.co/DennisHuang648/SenseVoiceSmall-onnx) — Claude 제안: **1점**

- 제안 이유: SenseVoiceSmall 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | DennisHuang648/SenseVoiceSmall-onnx (variant=false, 종류=—, 관계 근거=self, 변환 표지=onnx) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx / 0.22 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | This model is designed to be used with `onnxruntime` + `kaldi-native-fbank` + `sentencepiece` for lightweight inference without the full FunASR/PyTorch stack. |
| README 인용 | This model is designed to be used with `onnxruntime` + `kaldi-native-fbank` + `sentencepiece` for lightweight inference without the full FunASR/PyTorch stack. |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 0e0d0a81fe03a27c0d56329ff6fc2dcc3fe01f7e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [FluidInference/sensevoice-small-coreml](https://huggingface.co/FluidInference/sensevoice-small-coreml) — Claude 제안: **1점**

- 제안 이유: SenseVoiceSmall 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | FunAudioLLM/SenseVoiceSmall (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 1.53 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | for on-device inference on Apple Silicon |
| README 인용 | co/FunAudioLLM/SenseVoiceSmall) for on-device inference on Apple Silicon, intended for [FluidInference/FluidAudio](https://github. |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 74bdbe74b2258f25b5400db72f6cbfbef7c74ded |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [FunAudioLLM/SenseVoiceSmall](https://huggingface.co/FunAudioLLM/SenseVoiceSmall) — Claude 제안: **2점**

- 제안 이유: SenseVoiceSmall 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | FunAudioLLM/SenseVoiceSmall (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.87 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for automatic speech recognition in various languages. |
| README 인용 | ```python from funasr import AutoModel from funasr.utils.postprocess_utils import rich_transcription_postprocess  model_dir = "FunAudioLLM/SenseVoiceSmall"   model = AutoModel(     model=model_dir,     vad_model="fsmn-vad",     vad_kwargs={… |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 3847d57b6bdf2dd8875cb1508d2af43d80a16bf7 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [FunAudioLLM/SenseVoiceSmall-GGUF-audiocpp](https://huggingface.co/FunAudioLLM/SenseVoiceSmall-GGUF-audiocpp) — Claude 제안: **1점**

- 제안 이유: SenseVoiceSmall 계열의 변환·양자화·재업로드
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

#### 5. [cstr/sensevoice-small-GGUF](https://huggingface.co/cstr/sensevoice-small-GGUF) — Claude 제안: **1점**

- 제안 이유: SenseVoiceSmall 계열의 변환·양자화·재업로드
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

#### 6. [ghost613/faster-whisper-large-v3-turbo-korean](https://huggingface.co/ghost613/faster-whisper-large-v3-turbo-korean) — Claude 제안: **1점**

- 제안 이유: whisper-large-v3-turbo-korean 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-large-v3-turbo (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 3.01 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for automatic speech recognition tasks. |
| README 인용 | pipeline_tag: automatic-speech-recognition --- |
| provenance status | verified 8, not_applicable 3, documented 2, unknown 10 |
| revision | 24ac9326be16e128adb4c855f5a91cf457deb856 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [ghost613/whisper-large-v3-turbo-korean](https://huggingface.co/ghost613/whisper-large-v3-turbo-korean) — Claude 제안: **2점**

- 제안 이유: whisper-large-v3-turbo-korean 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-large-v3-turbo (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.809 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 3.01 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is designed for automatic speech recognition. |
| README 인용 | pipeline_tag: automatic-speech-recognition --- |
| provenance status | verified 13, not_applicable 3, documented 2, unknown 5 |
| revision | eddbfbef75b14ff0106c8275ddf5ad2b00f0b0a4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [handy-computer/SenseVoiceSmall-gguf](https://huggingface.co/handy-computer/SenseVoiceSmall-gguf) — Claude 제안: **1점**

- 제안 이유: SenseVoiceSmall 계열의 변환·양자화·재업로드
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

#### 9. [imTak/whisper_large_v3_turbo_Korean2](https://huggingface.co/imTak/whisper_large_v3_turbo_Korean2) — Claude 제안: **2점**

- 제안 이유: whisper-large-v3-turbo-korean 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-large-v3-turbo (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.809 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 3.01 |
| 벤치마크 근거 | 없음 |
| 의미 claim (documented_strengths) | Automatic Speech Recognition |
| README 인용 | name: Automatic Speech Recognition       type: automatic-speech-recognition     dataset:       name: Zeroth-Korean       type: Bingsu/zeroth-korean       args: 'config: ko, split: test'     metrics: |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | abb25dab77fa0f97db31e523bb6b6964cd695b8f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [litert-community/SenseVoiceSmall](https://huggingface.co/litert-community/SenseVoiceSmall) — Claude 제안: **1점**

- 제안 이유: SenseVoiceSmall 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | FunAudioLLM/SenseVoiceSmall (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | — / — |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is designed for automatic speech recognition tasks. |
| README 인용 | pipeline_tag: automatic-speech-recognition --- |
| provenance status | verified 7, not_applicable 3, documented 4, unknown 9 |
| revision | 17eeff4365b003a518bf8a7ba0302af14a712de6 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [litert-community/SenseVoiceSmall-ko-zeroth](https://huggingface.co/litert-community/SenseVoiceSmall-ko-zeroth) — Claude 제안: **1점**

- 제안 이유: SenseVoiceSmall 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | FunAudioLLM/SenseVoiceSmall (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | — / — |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for automatic speech recognition tasks. |
| README 인용 | pipeline_tag: automatic-speech-recognition --- |
| provenance status | verified 7, not_applicable 3, documented 4, unknown 9 |
| revision | 238206ca4edf365459eeedd32dd3b2fee5edf1a8 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [voconly-org/sensevoice-small-gguf](https://huggingface.co/voconly-org/sensevoice-small-gguf) — Claude 제안: **1점**

- 제안 이유: SenseVoiceSmall 계열의 변환·양자화·재업로드
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

## mc08 — 한영 번역용으로 Tri-1.8B-Translation 과 NLLB-200 distilled 1.3B 를 비교해 보고 싶어요.

- 사용자 의도: 두 번역 모델 비교
- persona / 표현: startup_dev / 기술형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: 각 모델의 원본
- **1점 기준**: 각 모델의 GGUF·CTranslate2 변환본
- 비교 계열: Tri-1.8B-Translation (`tri-1\.8b-translation`), nllb-200-distilled-1.3B (`nllb-200-distilled-1\.3b`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 2 | 9 | 4,006 | 0 | 11 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 지정한 모델 계열이 아님 (`other_family`) | 4,005 | circulus/koelectra-wellness-v1, donghanasd/Huihui-Qwen3.8-27B-Coder390-EfficientThink-abliterated-KO-Ridge-3.7bpw-GGUF, oxalis-ink/shamrock-0-e2b |
| variant 관계가 질문과 맞지 않음 (`variant_mismatch`) | 1 | raxtemur/SONAR_200_text_decoder |

같은 canonical family 후보가 3개 이상: trillionlabs/Tri-1.8B-Translation 3

#### 1. [JustFrederik/nllb-200-distilled-1.3B-ct2](https://huggingface.co/JustFrederik/nllb-200-distilled-1.3B-ct2) — Claude 제안: **1점**

- 제안 이유: nllb-200-distilled-1.3B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | JustFrederik/nllb-200-distilled-1.3B-ct2 (variant=false, 종류=—, 관계 근거=self, 변환 표지=ct2) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 5.11 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | translation |
| README 인용 | - translation |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | c9478c22635768dadab7cc9c2a7f5b6c72b93587 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [JustFrederik/nllb-200-distilled-1.3B-ct2-float16](https://huggingface.co/JustFrederik/nllb-200-distilled-1.3B-ct2-float16) — Claude 제안: **1점**

- 제안 이유: nllb-200-distilled-1.3B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | JustFrederik/nllb-200-distilled-1.3B-ct2-float16 (variant=false, 종류=—, 관계 근거=self, 변환 표지=ct2) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 2.56 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | translation |
| README 인용 | - translation |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 68395fbf719c4e7b0f34003f5fdec748cb9d04bc |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [JustFrederik/nllb-200-distilled-1.3B-ct2-int8](https://huggingface.co/JustFrederik/nllb-200-distilled-1.3B-ct2-int8) — Claude 제안: **1점**

- 제안 이유: nllb-200-distilled-1.3B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | JustFrederik/nllb-200-distilled-1.3B-ct2-int8 (variant=false, 종류=—, 관계 근거=self, 변환 표지=ct2) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 1.29 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | translation |
| README 인용 | - translation |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 30c36268408177b0fce2bfcfa205d877accd327d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [OpenNMT/nllb-200-distilled-1.3B-ct2-int8](https://huggingface.co/OpenNMT/nllb-200-distilled-1.3B-ct2-int8) — Claude 제안: **1점**

- 제안 이유: nllb-200-distilled-1.3B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | OpenNMT/nllb-200-distilled-1.3B-ct2-int8 (variant=false, 종류=—, 관계 근거=self, 변환 표지=ct2) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 1.28 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | NLLB-200 is a research model and is not released for production deployment. |
| README 인용 | - Out-of-scope use cases: NLLB-200 is a research model and is not released for production deployment. NLLB-200 is trained on general domain text data and is not intended to be used with domain specific texts, such as medical domain or legal… |
| provenance status | verified 12, not_applicable 3, documented 4, unknown 4 |
| revision | 70f572adafa4794890ce7826156a4209717855af |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [entai2965/nllb-200-distilled-1.3B-ctranslate2](https://huggingface.co/entai2965/nllb-200-distilled-1.3B-ctranslate2) — Claude 제안: **1점**

- 제안 이유: nllb-200-distilled-1.3B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | facebook/nllb-200-distilled-1.3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=ctranslate) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 5.11 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | NLLB-200 is a machine translation model primarily intended for research in machine translation. |
| README 인용 | - Primary intended uses: NLLB-200 is a machine translation model primarily intended for research in machine translation, - especially for low-resource languages. It allows for single sentence translation among 200 languages. Information on … |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 19b46b1e266e3e385e1286cf67779fc14c541f3d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [facebook/nllb-200-distilled-1.3B](https://huggingface.co/facebook/nllb-200-distilled-1.3B) — Claude 제안: **2점**

- 제안 이유: nllb-200-distilled-1.3B 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | facebook/nllb-200-distilled-1.3B (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 5.11 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | NLLB-200 is primarily intended for research in machine translation, especially for low-resource languages. |
| README 인용 | - Primary intended uses: NLLB-200 is a machine translation model primarily intended for research in machine translation, - especially for low-resource languages. It allows for single sentence translation among 200 languages. Information on … |
| provenance status | verified 12, not_applicable 3, documented 4, unknown 4 |
| revision | 7be3e24664b38ce1cac29b8aeed6911aa0cf0576 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [michaelfeil/ct2fast-nllb-200-distilled-1.3B](https://huggingface.co/michaelfeil/ct2fast-nllb-200-distilled-1.3B) — Claude 제안: **1점**

- 제안 이유: nllb-200-distilled-1.3B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | michaelfeil/ct2fast-nllb-200-distilled-1.3B (variant=false, 종류=—, 관계 근거=self, 변환 표지=ct2) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 1.28 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | NLLB-200 is primarily intended for research in machine translation, especially for low-resource languages. |
| README 인용 | - Primary intended uses: NLLB-200 is a machine translation model primarily intended for research in machine translation, - especially for low-resource languages. It allows for single sentence translation among 200 languages. Information on … |
| provenance status | verified 12, not_applicable 3, documented 4, unknown 4 |
| revision | 22233c601101b8db896035d967f95c413d5abdea |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [mradermacher/Tri-1.8B-Translation-GGUF](https://huggingface.co/mradermacher/Tri-1.8B-Translation-GGUF) — Claude 제안: **1점**

- 제안 이유: Tri-1.8B-Translation 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | trillionlabs/Tri-1.8B-Translation (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.809 / 16384 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.73 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for translation tasks. |
| README 인용 | - translation |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 2ea0edd4dac13a06e3acfd9cf01ebbf591420628 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [mradermacher/Tri-1.8B-Translation-i1-GGUF](https://huggingface.co/mradermacher/Tri-1.8B-Translation-i1-GGUF) — Claude 제안: **1점**

- 제안 이유: Tri-1.8B-Translation 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | trillionlabs/Tri-1.8B-Translation (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.809 / 16384 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.51 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is suitable for translation tasks. |
| README 인용 | - translation |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | a66dfad6b422038229aca565d91861f288683cc3 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [trillionlabs/Tri-1.8B-Translation](https://huggingface.co/trillionlabs/Tri-1.8B-Translation) — Claude 제안: **2점**

- 제안 이유: Tri-1.8B-Translation 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | trillionlabs/Tri-1.8B-Translation (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.809 / 16384 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 6.74 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used to translate text from Korean to English. |
| README 인용 | ```python from transformers import AutoTokenizer, AutoModelForCausalLM  model_name = "trillionlabs/Tri-1.8B-Translation" tokenizer = AutoTokenizer.from_pretrained(model_name) model = AutoModelForCausalLM.from_pretrained(model_name, device_m… |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 7f64c04dbd69381a8c240a8afa7e6b51ddcd661e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [winstxnhdw/nllb-200-distilled-1.3B-ct2-int8](https://huggingface.co/winstxnhdw/nllb-200-distilled-1.3B-ct2-int8) — Claude 제안: **1점**

- 제안 이유: nllb-200-distilled-1.3B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | winstxnhdw/nllb-200-distilled-1.3B-ct2-int8 (variant=false, 종류=—, 관계 근거=self, 변환 표지=ct2) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 1.29 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for translation tasks. |
| README 인용 | - translation |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 5d67ab73ef26497a7964712d7df01dfa1569dd04 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## mc09 — 한국어 이미지 이해 기능에 VARCO-VISION 2.0 1.7B 와 kanana-1.5-v-3b 중 뭐가 나을지 비교하고 싶어요.

- 사용자 의도: 두 소형 VLM 비교
- persona / 표현: backend_dev / 혼합형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: 각 모델의 원본
- **1점 기준**: 각 모델의 변형·재업로드
- 비교 계열: VARCO-VISION-2.0-1.7B (`varco-vision-2\.0-1\.7b(?!-ocr)`), kanana-1.5-v-3b (`kanana-1\.5-v-3b`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 2 | 0 | 4,015 | 0 | 2 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 지정한 모델 계열이 아님 (`other_family`) | 4,015 | TheBloke/openbuddy-mistral-7B-v13.1-GGUF, ThomasBaruzier/EXAONE-3.5-2.4B-Instruct-GGUF, localdeel/ko-hand-ocr-vl-GGUF |

#### 1. [NCSOFT/VARCO-VISION-2.0-1.7B](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B) — Claude 제안: **2점**

- 제안 이유: VARCO-VISION-2.0-1.7B 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-1.7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.124 / 40960 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit, readme:korean_explicit_phrase |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 3.96 |
| 벤치마크 근거 | 점수 40건 저장 |
| 의미 claim (use_cases) | All inputs in a batch must have the same modality structure—for example, text-only with text-only, single-image with single-image, and multi-image with multi-image—to ensure correct batch inference. |
| README 인용 | <details> <summary>Batch inference</summary> All inputs in a batch must have the same modality structure—for example, text-only with text-only, single-image with single-image, and multi-image with multi-image—to ensure correct batch inferen… |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | ed09f37445518b1564d1ef3c6e26fbd7c1b2c818 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [kakaocorp/kanana-1.5-v-3b-instruct](https://huggingface.co/kakaocorp/kanana-1.5-v-3b-instruct) — Claude 제안: **2점**

- 제안 이유: kanana-1.5-v-3b 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | kakaocorp/kanana-1.5-v-3b-instruct (variant=false, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 3.668 / 32768 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 6.83 |
| 벤치마크 근거 | 점수 4건 저장 |
| 의미 claim (use_cases) | pipeline_tag: image-text-to-text |
| README 인용 | pipeline_tag: image-text-to-text library_name: transformers --- |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 2e00ef13ccec2e99459a8eada18a1bfd05bff44b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## mc10 — Llama 3 기반 8B 한국어 모델인 Bllossom 8B 와 Llama-VARCO-8B-Instruct 를 비교하려고 합니다.

- 사용자 의도: Llama 3 기반 8B 한국어 모델 두 개 비교
- persona / 표현: researcher / 기술형 · 난이도 easy
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: 각 모델의 원본
- **1점 기준**: 각 모델의 GGUF 등 변환본
- 비교 계열: Bllossom-8B (`llama-3-korean-bllossom-8b`), Llama-VARCO-8B (`llama-varco-8b`)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 2 | 1 | 4,014 | 0 | 3 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 지정한 모델 계열이 아님 (`other_family`) | 4,014 | 2264K/ktransfer-27b-kd-dynamic-s400, TheCluster/Darwin-35B-A3B-Opus-MLX-bf16, cointegrated/SONAR_200_text_encoder |

#### 1. [MLP-KTLim/llama-3-Korean-Bllossom-8B](https://huggingface.co/MLP-KTLim/llama-3-Korean-Bllossom-8B) — Claude 제안: **2점**

- 제안 이유: Bllossom-8B 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | meta-llama/Meta-Llama-3-8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 8.03 / 8192 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit, readme:korean_explicit_phrase |
| license / commercial_status / gated | llama3 / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.96 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Inference-Code-Link |
| README 인용 | - [Inference-Code-Link](https://colab.research.google.com/drive/1fBOzUVZ6NRKk_ugeoTbAOokWKqSN47IG?usp=sharing) |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | ed9647c18477ee09a03690c613c859eddca24362 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [NCSOFT/Llama-VARCO-8B-Instruct](https://huggingface.co/NCSOFT/Llama-VARCO-8B-Instruct) — Claude 제안: **2점**

- 제안 이유: Llama-VARCO-8B 원본 모델
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | meta-llama/Llama-3.1-8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 8.03 / 8192 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | llama3.1 / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.96 |
| 벤치마크 근거 | 점수 1건 저장 |
| 의미 claim (benchmarks) | The score includes only the 0-shot evaluation provided in the default. |
| README 인용 | The score includes only the 0-shot evaluation provided in the default. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | fe2d9358a2d35451c04e4589b47e361cfacd350d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [joongi007/llama-3-Korean-Bllossom-8B-20240809-GGUF](https://huggingface.co/joongi007/llama-3-Korean-Bllossom-8B-20240809-GGUF) — Claude 제안: **1점**

- 제안 이유: Bllossom-8B 계열의 변환·양자화·재업로드
- 근거 위치: `model_id` — —

| 항목 | 값 |
|---|---|
| canonical model | MLP-KTLim/llama-3-Korean-Bllossom-8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 8.03 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | llama3.1 / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 2.96 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is designed for text generation tasks. |
| README 인용 | pipeline_tag: text-generation model-index: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | c0aea104629016caf78dd3a4dd9c7cfd03459c4a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______
