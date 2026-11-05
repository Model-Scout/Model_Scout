# structured_constraint 판정 워크시트

**숫자 검증은 명령 한 줄이 전부 합니다.**

```bash
cd ai && ../.venv/bin/python test/golden/v2/tools/verify.py structured_constraint
```

## 정훈님이 판단할 것

| | 질문 | 아니라면 |
|---|---|---|
| **①** | 조건이 질의문이 요구한 것을 넘지 않나? | 조건을 뺀다 |
| **②** | 🚩 의 제안 등급(2점/1점)이 맞나? | 고친다 |
| **③** | ⚠️ 중에 정답이 섞여 있나? | 정답으로 올린다 |

③이 재현율 방어선입니다. 빠진 정답은 걸러낸 쪽에 숨어 있으므로 🚩만 보면
영원히 못 찾습니다. ✅ 더미는 소분류 이유만 읽고 넘기시면 됩니다.

### 등급 기준 (유형 공통)

| 등급 | 뜻 |
|---:|---|
| **2** | 질의의 모든 조건을 데이터로 확인 + 용도가 정확히 일치 |
| **1** | 조건은 충족하나 도메인이 넓거나 좁음 / 근거 미확인 / 변환본·재업로드 |
| **0** | 기록하지 않음 — 라벨에 없으면 오답 |

코퍼스 3872행 · 2026-10-31 기준 · 질의 10개 · 사람이 볼 것 **169개**

---

### `sc01` ≤3.0B · summarization · easy

> 3B 이하 한국어 요약 모델을 찾고 있어.

조건 → 질의문 근거

- `tasks=["summarization"]` ← 요약
- `korean_required=true` ← 한국어
- `max_parameters_billion=3.0` ← 3B 이하

판정 규칙 (판정 전에 고정)

- **must** 요약 용도가 model_id / filter_metadata / claim에서 확인된다
- **2점** 한국어 요약 전용으로 학습·파인튜닝된 모델
- **1점** 다국어 요약 모델이거나, 요약이 부가 기능인 범용 생성 모델

후보 14개 전수 스캔 → 🚩 14 / ⚠️ 0 / ✅ 0

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `QyrouNnet-AI/QNS-2-ReLearn-Preview` | 2점 | filter_metadata에서 summar, sum |  |
| `ainize/kobart-news` | 2점 | filter_metadata에서 summar, sum |  |
| `ncls-p/Qwen2.5-3B-blog-key-points` | 2점 | filter_metadata에서 summar, sum |  |
| `ncls-p/Qwen2.5-7B-blog-key-points` | 2점 | filter_metadata에서 summar, sum |  |
| `EbanLee/kobart-summary-v3` | 2점 | model_id에서 summar, sum |  |
| `csebuetnlp/mT5_m2m_crossSum` | 2점 | model_id에서 crosssum, sum |  |
| `csebuetnlp/mT5_m2m_crossSum_enhanced` | 2점 | model_id에서 crosssum, sum |  |
| `csebuetnlp/mT5_m2o_english_crossSum` | 2점 | model_id에서 crosssum, sum |  |
| `csebuetnlp/mT5_multilingual_XLSum` | 2점 | model_id에서 xlsum, sum |  |
| `data-silence/any-news-sum` | 2점 | model_id에서 sum |  |
| `eenzeenee/t5-base-korean-summarization` | 2점 | model_id에서 summar, sum |  |
| `eenzeenee/t5-small-korean-summarization` | 2점 | model_id에서 summar, sum |  |
| `mskayacioglu/mbart50-xlsum` | 2점 | model_id에서 xlsum, sum |  |
| `psyche/KoT5-summarization` | 2점 | model_id에서 summar, sum |  |


### `sc02` ≤1.0B · question-answering · easy

> 파라미터 1B 이하인 한국어 질의응답 모델이 필요해.

조건 → 질의문 근거

- `tasks=["question-answering"]` ← 질의응답
- `korean_required=true` ← 한국어
- `max_parameters_billion=1.0` ← 파라미터 1B 이하

판정 규칙 (판정 전에 고정)

- **must** 질의응답 용도가 model_id / filter_metadata / claim에서 확인된다
- **2점** KorQuAD 등 한국어 QA 데이터로 학습된 전용 모델
- **1점** 다국어 QA 모델이거나, QA가 부가 기능인 범용 인코더

후보 17개 전수 스캔 → 🚩 17 / ⚠️ 0 / ✅ 0

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `monologg/koelectra-base-v3-finetuned-korquad` | 2점 | model_id에서 korquad |  |
| `monologg/koelectra-small-v2-distilled-korquad-384` | 2점 | model_id에서 korquad |  |
| `FreedomIntelligence/Apollo-MoE-0.5B` | 1점 | filter_metadata에서 question |  |
| `QuantFactory/Apollo2-2B-GGUF` | 1점 | filter_metadata에서 question |  |
| `QuantFactory/Apollo2-7B-GGUF` | 1점 | filter_metadata에서 question |  |
| `QuantFactory/Apollo2-9B-GGUF` | 1점 | filter_metadata에서 question |  |
| `cgus/Apollo2-7B-iMat-GGUF` | 1점 | filter_metadata에서 question |  |
| `mradermacher/IoGPT-A1-Instruct-GGUF` | 1점 | filter_metadata에서 question |  |
| `mradermacher/IoGPT-A1-Instruct-i1-GGUF` | 1점 | filter_metadata에서 question |  |
| `mradermacher/Korean-Gemma-2B-Instruct-GGUF` | 1점 | filter_metadata에서 question |  |
| `mradermacher/Prototype-Virus-1B-GGUF` | 1점 | filter_metadata에서 question |  |
| `mradermacher/Prototype-Virus-1B-i1-GGUF` | 1점 | filter_metadata에서 question |  |
| `mradermacher/next-12b-GGUF` | 1점 | filter_metadata에서 question |  |
| `mradermacher/next-12b-i1-GGUF` | 1점 | filter_metadata에서 question |  |
| `mradermacher/next-1b-GGUF` | 1점 | filter_metadata에서 question |  |
| `bespin-global/klue-bert-base-aihub-mrc` | 1점 | model_id에서 mrc |  |
| `timpal0l/mdeberta-v3-base-squad2` | 1점 | model_id에서 squad |  |


### `sc03` ctx≥32,768 · text-classification · easy

> 긴 문서를 다뤄야 해서 컨텍스트 32768 토큰 이상인 한국어 텍스트 분류 모델을 찾아줘.

조건 → 질의문 근거

- `tasks=["text-classification"]` ← 텍스트 분류
- `korean_required=true` ← 한국어
- `min_context_length=32768` ← 컨텍스트 32768 토큰 이상

판정 규칙 (판정 전에 고정)

- **must** 분류 용도가 model_id / filter_metadata / claim에서 확인된다
- **2점** 한국어 텍스트 분류 전용으로 학습된 모델
- **1점** 다국어 분류 모델이거나, 분류 헤드가 붙은 범용 인코더

후보 29개 전수 스캔 → 🚩 29 / ⚠️ 0 / ✅ 0

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `HPLT/OpenLID-v3` | 2점 | filter_metadata에서 classif |  |
| `Metabaron6/Shieldstral-1.0-3B-GGUF` | 2점 | filter_metadata에서 classif |  |
| `NorviTech/armiger` | 2점 | filter_metadata에서 classif |  |
| `NorviTech/armiger-ultra` | 2점 | filter_metadata에서 classif |  |
| `astroware/HaloGuard1-Gen-0.8B` | 2점 | filter_metadata에서 classif |  |
| `astroware/HaloGuard1-Gen-4B` | 2점 | filter_metadata에서 classif |  |
| `banjl4487/MODEL` | 2점 | filter_metadata에서 classif |  |
| `chaoliangUNSW/Jev-Style-0.8B-Decision-v3` | 2점 | filter_metadata에서 classif |  |
| `chaoliangUNSW/Jev-Style-0.8B-Decision-v3-GGUF` | 2점 | filter_metadata에서 classif |  |
| `cis-lmu/glotlid` | 2점 | filter_metadata에서 classif |  |
| `desert-ant-labs/emo` | 2점 | filter_metadata에서 classif |  |
| `doofz/THX-01` | 2점 | filter_metadata에서 classif |  |
| `knowledgator/opir-multitask-multilang-v1.0` | 2점 | filter_metadata에서 classif |  |
| `letrthang/aimtas-laya-multilingual-GGUF` | 2점 | filter_metadata에서 classif |  |
| `llm-semantic-router/mmbert32k-modality-router-merged` | 2점 | filter_metadata에서 classif |  |
| `musubilabs/policylm-1.7b` | 2점 | filter_metadata에서 classif |  |
| `quevirus/Xevn-4B-GGUF` | 2점 | filter_metadata에서 classif |  |
| `shreyasmeher/Qwen-GLOCON-Reasoning` | 2점 | filter_metadata에서 classif |  |
| `sky7350/Mica-v0.1-4B` | 2점 | filter_metadata에서 classif |  |
| `sky7350/Mica-v0.5-4B` | 2점 | filter_metadata에서 classif |  |
| `vijil/prompt-injection-v5-20260827` | 2점 | filter_metadata에서 classif |  |
| `vllm-sr/Vela-1.0-Encoder-307M-Shield` | 2점 | filter_metadata에서 classif |  |
| `vllm-sr/mmbert32k-modality-router-merged` | 2점 | filter_metadata에서 classif |  |
| `ethicalabs/Echo-DSRN-v0.1.3-Intent-CLF` | 2점 | model_id에서 intent |  |
| `gpustack/bce-reranker-base_v1-GGUF` | 2점 | model_id에서 rerank |  |
| `gpustack/gte-multilingual-reranker-base-GGUF` | 2점 | model_id에서 rerank |  |
| `llm-semantic-router/mmbert-rerank-32k-2d-matryoshka` | 2점 | model_id에서 rerank |  |
| `mp-juuuns/qwen35-c8q-distilled-8l-edge-classifier-gguf` | 2점 | model_id에서 classif |  |
| `vllm-sr/mmbert-rerank-32k-2d-matryoshka` | 2점 | model_id에서 rerank |  |


### `sc04` ctx≥131,072 · text-classification · easy

> 컨텍스트 131072 토큰 이상인 한국어 텍스트 분류 모델이 있을까?

조건 → 질의문 근거

- `tasks=["text-classification"]` ← 텍스트 분류
- `korean_required=true` ← 한국어
- `min_context_length=131072` ← 컨텍스트 131072 토큰 이상

판정 규칙 (판정 전에 고정)

- **must** 분류 용도가 model_id / filter_metadata / claim에서 확인된다
- **2점** 한국어 텍스트 분류 전용으로 학습된 모델
- **1점** 다국어 분류 모델이거나, 분류 헤드가 붙은 범용 인코더

후보 24개 전수 스캔 → 🚩 24 / ⚠️ 0 / ✅ 0

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `HPLT/OpenLID-v3` | 2점 | filter_metadata에서 classif |  |
| `Metabaron6/Shieldstral-1.0-3B-GGUF` | 2점 | filter_metadata에서 classif |  |
| `NorviTech/armiger` | 2점 | filter_metadata에서 classif |  |
| `NorviTech/armiger-ultra` | 2점 | filter_metadata에서 classif |  |
| `banjl4487/MODEL` | 2점 | filter_metadata에서 classif |  |
| `chaoliangUNSW/Jev-Style-0.8B-Decision-v3` | 2점 | filter_metadata에서 classif |  |
| `chaoliangUNSW/Jev-Style-0.8B-Decision-v3-GGUF` | 2점 | filter_metadata에서 classif |  |
| `cis-lmu/glotlid` | 2점 | filter_metadata에서 classif |  |
| `desert-ant-labs/emo` | 2점 | filter_metadata에서 classif |  |
| `doofz/THX-01` | 2점 | filter_metadata에서 classif |  |
| `knowledgator/opir-multitask-multilang-v1.0` | 2점 | filter_metadata에서 classif |  |
| `letrthang/aimtas-laya-multilingual-GGUF` | 2점 | filter_metadata에서 classif |  |
| `musubilabs/policylm-1.7b` | 2점 | filter_metadata에서 classif |  |
| `quevirus/Xevn-4B-GGUF` | 2점 | filter_metadata에서 classif |  |
| `shreyasmeher/Qwen-GLOCON-Reasoning` | 2점 | filter_metadata에서 classif |  |
| `sky7350/Mica-v0.1-4B` | 2점 | filter_metadata에서 classif |  |
| `sky7350/Mica-v0.5-4B` | 2점 | filter_metadata에서 classif |  |
| `vijil/prompt-injection-v5-20260827` | 2점 | filter_metadata에서 classif |  |
| `astroware/HaloGuard1-Gen-0.8B` | 2점 | model_id에서 guard |  |
| `astroware/HaloGuard1-Gen-4B` | 2점 | model_id에서 guard |  |
| `ethicalabs/Echo-DSRN-v0.1.3-Intent-CLF` | 2점 | model_id에서 intent |  |
| `gpustack/bce-reranker-base_v1-GGUF` | 2점 | model_id에서 rerank |  |
| `gpustack/gte-multilingual-reranker-base-GGUF` | 2점 | model_id에서 rerank |  |
| `mp-juuuns/qwen35-c8q-distilled-8l-edge-classifier-gguf` | 2점 | model_id에서 classif |  |


### `sc05` ctx≥32,768 · core만 · sentence-similarity · easy

> 많이 쓰이는 모델 중에서 컨텍스트 32768 토큰 이상인 한국어 문장 유사도 모델을 추천해줘.

조건 → 질의문 근거

- `tasks=["sentence-similarity"]` ← 문장 유사도
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)
- `min_context_length=32768` ← 컨텍스트 32768 토큰 이상

판정 규칙 (판정 전에 고정)

- **must** 문장 임베딩·유사도 용도가 확인된다
- **2점** 한국어 문장 임베딩 전용으로 학습된 모델
- **1점** 다국어 임베딩 모델이거나, 임베딩이 부가 용도인 범용 인코더

후보 28개 전수 스캔 → 🚩 28 / ⚠️ 0 / ✅ 0

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Alibaba-NLP/gte-multilingual-base` | 2점 | filter_metadata에서 sentence, similar |  |
| `ChristianAzinn/labse-gguf` | 2점 | filter_metadata에서 sentence, similar |  |
| `LiquidAI/LFM2-ColBERT-350M` | 2점 | filter_metadata에서 sentence, similar |  |
| `LiquidAI/LFM2.5-ColBERT-350M` | 2점 | filter_metadata에서 sentence, similar |  |
| `LiquidAI/LFM2.5-ColBERT-350M-GGUF` | 2점 | filter_metadata에서 sentence, similar |  |
| `dnotitia/DNA-VL-STEER-2B` | 2점 | filter_metadata에서 sentence, similar, embed |  |
| `facebook/drama-large` | 2점 | filter_metadata에서 sentence, similar |  |
| `omai-research/milco-300m` | 2점 | filter_metadata에서 sentence, similar |  |
| `BidirLM/BidirLM-0.6B-Embedding` | 2점 | model_id에서 embed |  |
| `BidirLM/BidirLM-1B-Embedding` | 2점 | model_id에서 embed |  |
| `BidirLM/BidirLM-Omni-2.5B-Embedding` | 2점 | model_id에서 embed |  |
| `Casual-Autopsy/snowflake-arctic-embed-l-v2.0-gguf` | 2점 | model_id에서 embed |  |
| `LiquidAI/LFM2.5-Embedding-350M` | 2점 | model_id에서 embed |  |
| `LiquidAI/LFM2.5-Embedding-350M-GGUF` | 2점 | model_id에서 embed |  |
| `PeterAM4/Qwen3-Embedding-0.6B-GGUF` | 2점 | model_id에서 embed |  |
| `Snowflake/snowflake-arctic-embed-m-v2.0` | 2점 | model_id에서 embed |  |
| `batiai/Qwen3-VL-Embedding-8B-GGUF` | 2점 | model_id에서 embed |  |
| `dinab/multilingual-e5-base-Q4_K_M-GGUF` | 2점 | model_id에서 e5 |  |
| `ggml-org/Nomic-Embed-Text-V2-GGUF` | 2점 | model_id에서 embed |  |
| `groonga/multilingual-e5-base-Q4_K_M-GGUF` | 2점 | model_id에서 e5 |  |
| `litert-community/LFM2.5-Embedding-350M` | 2점 | model_id에서 embed |  |
| `nomic-ai/nomic-embed-text-v2-moe-GGUF` | 2점 | model_id에서 embed |  |
| `nvidia/Nemotron-3-Embed-1B-BF16` | 2점 | model_id에서 embed |  |
| `nvidia/Nemotron-3-Embed-1B-NVFP4` | 2점 | model_id에서 embed |  |
| `nvidia/Nemotron-3-Embed-8B-BF16` | 2점 | model_id에서 embed |  |
| `shadowrock-io/Nemotron-3-Embed-8B-Community-NVFP4` | 2점 | model_id에서 embed |  |
| `zenmagnets/Nemotron-3-Embed-1B-Q4_K_M-GGUF` | 2점 | model_id에서 embed |  |
| `zhiqian99/Qwen3-Embedding-0.6B-GGUF` | 2점 | model_id에서 embed |  |


### `sc06` ≤100M · 값공개 · automatic-speech-recognition · easy

> 파라미터 수가 명시된 것 중에 100M 이하인 한국어 음성 인식 모델을 찾고 있어.

조건 → 질의문 근거

- `tasks=["automatic-speech-recognition"]` ← 음성 인식
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.1` ← 100M 이하
- `require_known_parameters=true` ← 파라미터 수가 명시된 것

판정 규칙 (판정 전에 고정)

- **must** 음성 인식 용도가 확인된다
- **2점** 한국어 음성 데이터로 학습·파인튜닝된 전용 모델
- **1점** 다국어 ASR 모델이거나 한국어가 포함된 범용 음성 모델

후보 15개 전수 스캔 → 🚩 15 / ⚠️ 0 / ✅ 0

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Bingsu/distilhubert-ko-zeroth` | 2점 | filter_metadata에서 speech |  |
| `moonshine-ai/moonshine-base-ko` | 2점 | filter_metadata에서 speech |  |
| `moonshine-ai/moonshine-tiny-ko` | 2점 | filter_metadata에서 speech |  |
| `team-lucid/hubert-base-korean` | 2점 | filter_metadata에서 speech |  |
| `Kkonjeong/wav2vec2-base-korean` | 2점 | model_id에서 wav2vec |  |
| `RedHatAI/whisper-tiny` | 2점 | model_id에서 whisper |  |
| `mlx-community/whisper-base-asr-fp16` | 2점 | model_id에서 asr, whisper |  |
| `mlx-community/whisper-tiny-asr-fp16` | 2점 | model_id에서 asr, whisper |  |
| `mobilint/whisper-medium` | 2점 | model_id에서 whisper |  |
| `mobilint/whisper-small` | 2점 | model_id에서 whisper |  |
| `neurlang/ipa-whisper-base` | 2점 | model_id에서 whisper |  |
| `openai/whisper-base` | 2점 | model_id에서 whisper |  |
| `openai/whisper-tiny` | 2점 | model_id에서 whisper |  |
| `unsloth/whisper-base` | 2점 | model_id에서 whisper |  |
| `unsloth/whisper-tiny` | 2점 | model_id에서 whisper |  |


### `sc07` ≤1.0B · 값공개 · image-text-to-text · easy

> 파라미터 1B 이하로 공개된 한국어 이미지-텍스트 모델을 추천해줘.

조건 → 질의문 근거

- `tasks=["image-text-to-text"]` ← 이미지-텍스트
- `korean_required=true` ← 한국어
- `max_parameters_billion=1.0` ← 파라미터 1B 이하
- `require_known_parameters=true` ← 로 공개된

판정 규칙 (판정 전에 고정)

- **must** 이미지 입력을 받는 용도가 확인된다
- **2점** 한국어 이미지-텍스트 전용으로 학습된 모델
- **1점** 다국어 VLM으로 한국어를 포함하거나, 변환본·양자화본

후보 12개 전수 스캔 → 🚩 12 / ⚠️ 0 / ✅ 0

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Mattimax/DAC6.5` | 2점 | filter_metadata에서 vl, image |  |
| `LiquidAI/LFM2.5-VL-450M` | 2점 | model_id에서 vl |  |
| `LiquidAI/LFM2.5-VL-450M-MLX-4bit` | 2점 | model_id에서 vl |  |
| `LiquidAI/LFM2.5-VL-450M-MLX-5bit` | 2점 | model_id에서 vl |  |
| `LiquidAI/LFM2.5-VL-450M-MLX-6bit` | 2점 | model_id에서 vl |  |
| `LiquidAI/LFM2.5-VL-450M-MLX-8bit` | 2점 | model_id에서 vl |  |
| `LiquidAI/LFM2.5-VL-450M-MLX-bf16` | 2점 | model_id에서 vl |  |
| `coder3101/LFM2.5-VL-450M-heretic` | 2점 | model_id에서 vl |  |
| `localdeel/ko-hand-ocr-vl` | 2점 | model_id에서 vl, ocr |  |
| `mlx-community/LFM2.5-VL-450M-6bit` | 2점 | model_id에서 vl |  |
| `mlx-community/LFM2.5-VL-450M-8bit` | 2점 | model_id에서 vl |  |
| `saidutta69/LFM2.5-VL-450M-heretic` | 2점 | model_id에서 vl |  |


### `sc08` ≤100M · 값공개 · feature-extraction · easy

> 파라미터 수가 공개된 100M 이하 한국어 임베딩 모델이 필요해.

조건 → 질의문 근거

- `tasks=["feature-extraction"]` ← 임베딩 → feature-extraction
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.1` ← 100M 이하
- `require_known_parameters=true` ← 파라미터 수가 공개된

판정 규칙 (판정 전에 고정)

- **must** 임베딩·특징 추출 용도가 확인된다
- **2점** 한국어 임베딩 전용으로 학습된 모델
- **1점** 다국어 임베딩 모델이거나, 임베딩이 부가 용도인 범용 인코더

후보 13개 전수 스캔 → 🚩 13 / ⚠️ 0 / ✅ 0

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Hisham480/multilingual-r2` | 2점 | filter_metadata에서 feature |  |
| `Xenova/kobert` | 2점 | filter_metadata에서 feature |  |
| `codefuse-ai/F2LLM-v2-80M` | 2점 | filter_metadata에서 feature |  |
| `fish9903/Emotion_KoBERT1` | 2점 | filter_metadata에서 feature |  |
| `madatnlp/km-bert` | 2점 | filter_metadata에서 feature |  |
| `monologg/kobert` | 2점 | filter_metadata에서 feature |  |
| `skt/kobert-base-v1` | 2점 | filter_metadata에서 feature |  |
| `utter-project/mHuBERT-147` | 2점 | filter_metadata에서 feature |  |
| `utter-project/mHuBERT-147-base-1st-iter` | 2점 | filter_metadata에서 feature |  |
| `utter-project/mHuBERT-147-base-2nd-iter` | 2점 | filter_metadata에서 feature |  |
| `CISCai/jina-embeddings-v3-separation-distilled` | 2점 | model_id에서 embed |  |
| `ibm-granite/granite-embedding-97m-multilingual-r2` | 2점 | model_id에서 embed |  |
| `onnx-community/granite-embedding-97m-multilingual-r2-ONNX` | 2점 | model_id에서 embed |  |


### `sc09` ≤100M · 값공개 · sentence-similarity · easy

> 파라미터 100M 이하로 명시된 한국어 문장 유사도 모델을 찾아줘.

조건 → 질의문 근거

- `tasks=["sentence-similarity"]` ← 문장 유사도
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.1` ← 파라미터 100M 이하
- `require_known_parameters=true` ← 로 명시된

판정 규칙 (판정 전에 고정)

- **must** 문장 유사도 용도가 확인된다
- **2점** 한국어 STS 데이터로 학습된 전용 모델
- **1점** 다국어 문장 임베딩 모델이거나 범용 인코더

후보 14개 전수 스캔 → 🚩 14 / ⚠️ 0 / ✅ 0

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `ddobokki/klue-roberta-small-nli-sts` | 2점 | filter_metadata에서 sentence, similar |  |
| `gomyk/intent-student-L4_uniform_distilled` | 2점 | filter_metadata에서 sentence, similar |  |
| `gomyk/intent-student-L6_uniform_distilled` | 2점 | filter_metadata에서 sentence, similar |  |
| `gomyk/minilm-student-L4_uniform_distilled` | 2점 | filter_metadata에서 sentence, similar |  |
| `gomyk/minilm-student-L6_uniform_distilled` | 2점 | filter_metadata에서 sentence, similar |  |
| `gomyk/modernbert-student-modernbert_L4_uniform_distilled` | 2점 | filter_metadata에서 sentence, similar |  |
| `setu4993/LEALLA-small` | 2점 | filter_metadata에서 sentence, similar |  |
| `smartmind/roberta-ko-small-tsdae` | 2점 | filter_metadata에서 sentence, similar |  |
| `alphaedge-ai/multilingual-e5-small-kor-32768` | 2점 | model_id에서 e5 |  |
| `ddobokki/unsup-simcse-klue-roberta-small` | 2점 | model_id에서 simcse |  |
| `exp-models/dragonkue-KoEn-E5-Tiny` | 2점 | model_id에서 e5 |  |
| `gomyk/me5s-me5s_compressed_v3_distilled` | 2점 | model_id에서 e5 |  |
| `gomyk/me5s-student-me5s_compressed_v3_distilled` | 2점 | model_id에서 e5 |  |
| `gomyk/me5s-student-me5s_compressed_v4_distilled` | 2점 | model_id에서 e5 |  |


### `sc10` core만 · summarization · easy

> 많이 쓰이는 한국어 요약 모델을 추천해줘.

조건 → 질의문 근거

- `tasks=["summarization"]` ← 요약
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)

판정 규칙 (판정 전에 고정)

- **must** 요약 용도가 확인된다
- **2점** 한국어 요약 전용으로 학습·파인튜닝된 모델
- **1점** 다국어 요약 모델이거나, 요약이 부가 기능인 범용 생성 모델

후보 3개 전수 스캔 → 🚩 3 / ⚠️ 0 / ✅ 0

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `EbanLee/kobart-summary-v3` | 2점 | model_id에서 summar, sum |  |
| `csebuetnlp/mT5_multilingual_XLSum` | 2점 | model_id에서 xlsum, sum |  |
| `eenzeenee/t5-base-korean-summarization` | 2점 | model_id에서 summar, sum |  |


