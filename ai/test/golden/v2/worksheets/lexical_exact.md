# lexical_exact 판정 워크시트

**숫자 검증은 명령 한 줄이 전부 합니다.**

```bash
cd ai && ../.venv/bin/python test/golden/v2/tools/verify.py lexical_exact
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

코퍼스 3872행 · 2026-10-31 기준 · 질의 10개 · 사람이 볼 것 **91개**

---

### `le01` 조건 없음 · summarization · easy

> GGUF 형식으로 받을 수 있는 한국어 요약 모델을 찾고 있어.

조건 → 질의문 근거

- `tasks=["summarization"]` ← 요약
- `korean_required=true` ← 한국어

판정 규칙 (판정 전에 고정)

- **must** GGUF 아티팩트를 실제로 가지고 있거나 model_id에 GGUF가 있다
- **2점** GGUF 파일이 artifacts에서 확인된다
- **1점** llama.cpp 호환만 언급하고 GGUF 파일 자체는 확인되지 않는다

후보 14개 전수 스캔 → 🚩 3 / ⚠️ 0 / ✅ 11

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `QyrouNnet-AI/QNS-2-ReLearn-Preview` | 2점 | filter_metadata에서 gguf |  |
| `ncls-p/Qwen2.5-3B-blog-key-points` | 2점 | filter_metadata에서 gguf |  |
| `ncls-p/Qwen2.5-7B-blog-key-points` | 2점 | filter_metadata에서 gguf |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 11개 — `EbanLee/kobart-summary-v3`, `ainize/kobart-news`, `csebuetnlp/mT5_m2m_crossSum`, `csebuetnlp/mT5_m2m_crossSum_enhanced`, `csebuetnlp/mT5_m2o_english_crossSum`, `csebuetnlp/mT5_multilingual_XLSum` …


### `le02` ≤1.0B · image-text-to-text · hard

> GGUF로 제공되는 한국어 이미지-텍스트 모델 있어? 파라미터 1B 이하인 것으로.

조건 → 질의문 근거

- `tasks=["image-text-to-text"]` ← 이미지-텍스트
- `korean_required=true` ← 한국어
- `max_parameters_billion=1.0` ← 파라미터 1B 이하

판정 규칙 (판정 전에 고정)

- **must** GGUF 아티팩트를 가지고 있거나 model_id에 GGUF가 있다
- **2점** GGUF 파일이 artifacts에서 확인된다
- **1점** llama.cpp 호환만 언급된다

후보 13개 전수 스캔 → 🚩 5 / ⚠️ 0 / ✅ 8

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `LiquidAI/LFM2.5-VL-450M` | 2점 | semantic_metadata에서 gguf |  |
| `coder3101/LFM2.5-VL-450M-heretic` | 2점 | semantic_metadata에서 gguf |  |
| `localdeel/ko-hand-ocr-vl` | 2점 | semantic_metadata에서 gguf |  |
| `saidutta69/LFM2.5-VL-450M-heretic` | 2점 | filter_metadata에서 gguf |  |
| `cstr/internvl2-1b-crispembed-GGUF` | 2점 | model_id에서 gguf |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 8개 — `LiquidAI/LFM2.5-VL-450M-MLX-4bit`, `LiquidAI/LFM2.5-VL-450M-MLX-5bit`, `LiquidAI/LFM2.5-VL-450M-MLX-6bit`, `LiquidAI/LFM2.5-VL-450M-MLX-8bit`, `LiquidAI/LFM2.5-VL-450M-MLX-bf16`, `Mattimax/DAC6.5` …


### `le03` core만 · feature-extraction · easy

> ONNX로 변환된 한국어 임베딩 모델을 추천해줘. 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["feature-extraction"]` ← 임베딩 → feature-extraction
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core

판정 규칙 (판정 전에 고정)

- **must** ONNX 아티팩트를 실제로 가지고 있다
- **2점** ONNX 파일이 artifacts에서 확인된다
- **1점** ONNX 변환 가능성만 언급된다

후보 64개 전수 스캔 → 🚩 14 / ⚠️ 0 / ✅ 50

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `codefuse-ai/F2LLM-v2-0.6B` | 2점 | filter_metadata에서 onnx |  |
| `ibm-granite/granite-embedding-311m-multilingual-r2` | 2점 | filter_metadata에서 onnx |  |
| `ibm-granite/granite-embedding-97m-multilingual-r2` | 2점 | filter_metadata에서 onnx |  |
| `intfloat/multilingual-e5-large` | 2점 | filter_metadata에서 onnx |  |
| `intfloat/multilingual-e5-large-instruct` | 2점 | filter_metadata에서 onnx |  |
| `jinaai/jina-clip-v2` | 2점 | filter_metadata에서 onnx |  |
| `jinaai/jina-embeddings-v3` | 2점 | filter_metadata에서 onnx |  |
| `jinaai/jina-embeddings-v3-hf` | 2점 | filter_metadata에서 onnx |  |
| `skt/kobert-base-v1` | 2점 | filter_metadata에서 onnx |  |
| `telepix/PIXIE-Rune-v1.0` | 2점 | filter_metadata에서 onnx |  |
| `unum-cloud/uform3-image-text-multilingual-base` | 2점 | filter_metadata에서 onnx |  |
| `onnx-community/granite-embedding-97m-multilingual-r2-ONNX` | 2점 | model_id에서 onnx |  |
| `onnx-community/harrier-oss-v1-0.6b-ONNX` | 2점 | model_id에서 onnx |  |
| `onnx-community/harrier-oss-v1-270m-ONNX` | 2점 | model_id에서 onnx |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 48개 — `BM-K/KoSimCSE-bert-multitask`, `BM-K/KoSimCSE-roberta`, `BM-K/KoSimCSE-roberta-multitask`, `CISCai/jina-embeddings-v3-separation-distilled`, `ZurichNLP/unsup-simcse-xlm-roberta-base`, `amazon/Titan-text-embeddings-v2` …
- **주 task가 sentence-similarity** 2개 — `omai-research/milco-300m`, `omai-research/milco-650m`


### `le04` core만 · sentence-similarity · easy

> ONNX 파일이 있는 한국어 문장 유사도 모델을 찾아줘. 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["sentence-similarity"]` ← 문장 유사도
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core

판정 규칙 (판정 전에 고정)

- **must** ONNX 아티팩트를 실제로 가지고 있다
- **2점** ONNX 파일이 artifacts에서 확인된다
- **1점** ONNX 변환 가능성만 언급된다

후보 71개 전수 스캔 → 🚩 17 / ⚠️ 0 / ✅ 54

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Hiveurban/multilingual-e5-base` | 2점 | filter_metadata에서 onnx |  |
| `MintplexLabs/multilingual-e5-small` | 2점 | filter_metadata에서 onnx |  |
| `RedHatAI/snowflake-arctic-embed-l-v2.0` | 2점 | filter_metadata에서 onnx |  |
| `Snowflake/snowflake-arctic-embed-l-v2.0` | 2점 | filter_metadata에서 onnx |  |
| `Snowflake/snowflake-arctic-embed-m-v2.0` | 2점 | filter_metadata에서 onnx |  |
| `exp-models/dragonkue-KoEn-E5-Tiny` | 2점 | filter_metadata에서 onnx |  |
| `ibm-granite/granite-embedding-107m-multilingual` | 2점 | filter_metadata에서 onnx |  |
| `ibm-granite/granite-embedding-278m-multilingual` | 2점 | filter_metadata에서 onnx |  |
| `intfloat/multilingual-e5-base` | 2점 | filter_metadata에서 onnx |  |
| `intfloat/multilingual-e5-small` | 2점 | filter_metadata에서 onnx |  |
| `jhgan/ko-sroberta-multitask` | 2점 | filter_metadata에서 onnx |  |
| `sentence-transformers/LaBSE` | 2점 | filter_metadata에서 onnx |  |
| `sentence-transformers/distiluse-base-multilingual-cased-v1` | 2점 | filter_metadata에서 onnx |  |
| `sentence-transformers/distiluse-base-multilingual-cased-v2` | 2점 | filter_metadata에서 onnx |  |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | 2점 | filter_metadata에서 onnx |  |
| `sentence-transformers/paraphrase-multilingual-mpnet-base-v2` | 2점 | filter_metadata에서 onnx |  |
| `shannondata/multilingual-e5-small` | 2점 | filter_metadata에서 onnx |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 54개 — `Alibaba-NLP/gte-multilingual-base`, `BidirLM/BidirLM-0.6B-Embedding`, `BidirLM/BidirLM-1B-Embedding`, `BidirLM/BidirLM-Omni-2.5B-Embedding`, `Casual-Autopsy/snowflake-arctic-embed-l-v2.0-gguf`, `ChristianAzinn/labse-gguf` …


### `le05` ≤500M · translation · hard

> 한국어를 영어로 번역하는 모델을 찾고 있어. 파라미터 500M 이하인 것으로.

조건 → 질의문 근거

- `tasks=["translation"]` ← 번역
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.5` ← 500M 이하

판정 규칙 (판정 전에 고정)

- **must** ko→en 방향이 model_id 또는 claim에서 확인된다
- **2점** ko→en 방향이 명시돼 있다
- **1점** 다국어 모델로 ko·en을 모두 지원하나 방향 명시가 없다

후보 14개 전수 스캔 → 🚩 2 / ⚠️ 3 / ✅ 9

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Helsinki-NLP/opus-mt-tc-big-ko-en` | 2점 | model_id에서 ko-en |  |
| `seongs/ke-t5-base-aihub-koen-translation-integrated-10m-en-to-ko` | 1점 | model_id에서 koen |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Babelscape/mrebel-base` | 믿을 수 있는 단계엔 없고 filter_metadata에만 m2m |  |
| `alirezamsh/small100` | 믿을 수 있는 단계엔 없고 filter_metadata에만 m2m |  |
| `dhtocks/nllb-200-distilled-350M_en-ko` | 믿을 수 있는 단계엔 없고 model_id에만 nllb |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 9개 — `Darong/BlueT`, `Helsinki-NLP/opus-mt-tc-big-en-ko`, `Helsinki-NLP/opus-mt_tiny_kor-eng`, `Neurora/opus-hplt-en-ko-v2.0`, `Sube126/Hy-MT2-1.8B-1.25Bit-MLX`, `kuotient/Hy-MT2-1.8B-1.25Bit-MLX` …


### `le06` ≤500M · translation · easy

> 영어를 한국어로 번역하는 모델이 필요해. 파라미터 500M 이하인 것으로.

조건 → 질의문 근거

- `tasks=["translation"]` ← 번역
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.5` ← 500M 이하

판정 규칙 (판정 전에 고정)

- **must** en→ko 방향이 model_id 또는 claim에서 확인된다
- **2점** en→ko 방향이 명시돼 있다
- **1점** 다국어 모델로 ko·en을 모두 지원하나 방향 명시가 없다

후보 14개 전수 스캔 → 🚩 3 / ⚠️ 2 / ✅ 9

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Helsinki-NLP/opus-mt-tc-big-en-ko` | 2점 | model_id에서 en-ko |  |
| `Neurora/opus-hplt-en-ko-v2.0` | 2점 | model_id에서 en-ko |  |
| `dhtocks/nllb-200-distilled-350M_en-ko` | 2점 | model_id에서 en-ko |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Babelscape/mrebel-base` | 믿을 수 있는 단계엔 없고 filter_metadata에만 m2m |  |
| `alirezamsh/small100` | 믿을 수 있는 단계엔 없고 filter_metadata에만 m2m |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 9개 — `Darong/BlueT`, `Helsinki-NLP/opus-mt-tc-big-ko-en`, `Helsinki-NLP/opus-mt_tiny_kor-eng`, `Sube126/Hy-MT2-1.8B-1.25Bit-MLX`, `kuotient/Hy-MT2-1.8B-1.25Bit-MLX`, `sappho192/aihub-ja-ko-translator` …


### `le07` core만 · translation · easy

> opus-mt 기반 한국어 번역 모델을 찾아줘. 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["translation"]` ← 번역
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core

판정 규칙 (판정 전에 고정)

- **must** model_id가 opus-mt 계열이다
- **2점** Helsinki-NLP/opus-mt 본체 또는 그 파인튜닝이다
- **1점** Marian 구조이나 opus-mt 계열임이 model_id에 없다

후보 117개 전수 스캔 → 🚩 4 / ⚠️ 0 / ✅ 113

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Helsinki-NLP/opus-mt-ko-en` | 2점 | model_id에서 opus-mt |  |
| `Helsinki-NLP/opus-mt-tc-big-en-ko` | 2점 | model_id에서 opus-mt |  |
| `Helsinki-NLP/opus-mt-tc-big-ko-en` | 2점 | model_id에서 opus-mt |  |
| `Xenova/opus-mt-ko-en` | 2점 | model_id에서 opus-mt |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 113개 — `42ailab/TranslateGemma-27B-GGUF`, `42ailab/TranslateGemma-4B-GGUF`, `BSC-LT/salamandraTA-7B-instruct-GGUF`, `BSC-LT/salamandraTA-7b-instruct`, `Babelscape/mrebel-large`, `ByteDance-Seed/Seed-X-Instruct-7B` …


### `le08` ≤2.0B · core만 · text-generation · easy

> MLX 형식으로 제공되는 한국어 LLM을 찾고 있어. 많이 쓰이는 것 중에 2B 이하인 모델로.

조건 → 질의문 근거

- `tasks=["text-generation"]` ← LLM → text-generation
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)
- `max_parameters_billion=2.0` ← 2B 이하

판정 규칙 (판정 전에 고정)

- **must** model_id 또는 filter_metadata에 MLX가 있다
- **2점** MLX 변환본임이 model_id에서 확인된다
- **1점** Apple Silicon 지원만 언급되고 MLX 변환본은 아니다

후보 169개 전수 스캔 → 🚩 23 / ⚠️ 0 / ✅ 146

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `LiquidAI/LFM2.5-1.2B-Instruct` | 2점 | semantic_metadata에서 mlx |  |
| `LiquidAI/LFM2.5-350M` | 2점 | semantic_metadata에서 mlx |  |
| `ZuzeTt/LFM2.5-1.2B-Instruct-imatrix-GGUF` | 2점 | semantic_metadata에서 mlx |  |
| `anudit/lfm25-strudel` | 2점 | semantic_metadata에서 mlx |  |
| `unsloth/LFM2.5-1.2B-Instruct` | 2점 | semantic_metadata에서 mlx |  |
| `unsloth/LFM2.5-1.2B-Instruct-GGUF` | 2점 | semantic_metadata에서 mlx |  |
| `LiquidAI/LFM2.5-1.2B-Instruct-MLX-4bit` | 2점 | model_id에서 mlx |  |
| `LiquidAI/LFM2.5-1.2B-Instruct-MLX-8bit` | 2점 | model_id에서 mlx |  |
| `LiquidAI/LFM2.5-1.2B-Instruct-MLX-bf16` | 2점 | model_id에서 mlx |  |
| `LiquidAI/LFM2.5-1.2B-Thinking-MLX-4bit` | 2점 | model_id에서 mlx |  |
| `LiquidAI/LFM2.5-230M-MLX-4bit` | 2점 | model_id에서 mlx |  |
| `LiquidAI/LFM2.5-230M-MLX-8bit` | 2점 | model_id에서 mlx |  |
| `LiquidAI/LFM2.5-350M-MLX-4bit` | 2점 | model_id에서 mlx |  |
| `LiquidAI/LFM2.5-350M-MLX-8bit` | 2점 | model_id에서 mlx |  |
| `jevoma4362/EuroLLM-1.7B-Instruct-mlx-4Bit` | 2점 | model_id에서 mlx |  |
| `lmstudio-community/LFM2-1.2B-MLX-8bit` | 2점 | model_id에서 mlx |  |
| `lmstudio-community/LFM2-1.2B-MLX-bf16` | 2점 | model_id에서 mlx |  |
| `lmstudio-community/LFM2.5-1.2B-Instruct-MLX-4bit` | 2점 | model_id에서 mlx |  |
| `lmstudio-community/LFM2.5-1.2B-Instruct-MLX-6bit` | 2점 | model_id에서 mlx |  |
| `lmstudio-community/LFM2.5-1.2B-Instruct-MLX-8bit` | 2점 | model_id에서 mlx |  |
| `mlx-community/LFM2-1.2B-4bit` | 2점 | model_id에서 mlx |  |
| `mlx-community/LFM2.5-1.2B-Instruct-4bit` | 2점 | model_id에서 mlx |  |
| `mlx-community/LFM2.5-1.2B-Thinking-6bit` | 2점 | model_id에서 mlx |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 146개 — `0xzknw/LFM2.5-1.2B-Thinking-Heretic`, `42dot/42dot_LLM-PLM-1.3B`, `42dot/42dot_LLM-SFT-1.3B`, `AtomicChat/LFM3-1.7B-GGUF`, `CMSManhattan/JiRackUltra_1b`, `Calandracas/minnow-pico-50M-base` …


### `le09` ≤4.0B · core만 · text-generation · hard

> fp8로 양자화된 한국어 LLM 있어? 많이 쓰이는 것 중에 4B 이하인 모델로.

조건 → 질의문 근거

- `tasks=["text-generation"]` ← LLM → text-generation
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)
- `max_parameters_billion=4.0` ← 4B 이하

판정 규칙 (판정 전에 고정)

- **must** quantization.method가 fp8이거나 model_id에 fp8이 있다
- **2점** fp8 양자화가 quantization에서 확인된다
- **1점** 8비트 가중치 양자화이나 fp8 방식은 아니다

후보 270개 전수 스캔 → 🚩 1 / ⚠️ 0 / ✅ 269

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `anudit/lfm25-strudel` | 2점 | semantic_metadata에서 fp8 |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 269개 — `0xzknw/LFM2.5-1.2B-Thinking-Heretic`, `0xzknw/LFM2.5-2.6B-Heretic-NX-PRIME`, `42dot/42dot_LLM-PLM-1.3B`, `42dot/42dot_LLM-SFT-1.3B`, `AMAImedia/Tiny-Aya-3.3B-L2-Thinker-BF16-GGUF`, `AtomicChat/LFM3-1.7B-GGUF` …


### `le10` 조건 없음 · summarization · easy

> safetensors로 받을 수 있는 한국어 요약 모델을 추천해줘.

조건 → 질의문 근거

- `tasks=["summarization"]` ← 요약
- `korean_required=true` ← 한국어

판정 규칙 (판정 전에 고정)

- **must** safetensors 아티팩트를 실제로 가지고 있다
- **2점** safetensors 파일이 artifacts에서 확인된다
- **1점** pytorch_bin만 있고 safetensors는 없다

후보 14개 전수 스캔 → 🚩 9 / ⚠️ 5 / ✅ 0

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `EbanLee/kobart-summary-v3` | 2점 | filter_metadata에서 safetensors |  |
| `QyrouNnet-AI/QNS-2-ReLearn-Preview` | 2점 | filter_metadata에서 safetensors |  |
| `data-silence/any-news-sum` | 2점 | filter_metadata에서 safetensors |  |
| `eenzeenee/t5-base-korean-summarization` | 2점 | filter_metadata에서 safetensors |  |
| `eenzeenee/t5-small-korean-summarization` | 2점 | filter_metadata에서 safetensors |  |
| `mskayacioglu/mbart50-xlsum` | 2점 | filter_metadata에서 safetensors |  |
| `ncls-p/Qwen2.5-3B-blog-key-points` | 2점 | filter_metadata에서 safetensors |  |
| `ncls-p/Qwen2.5-7B-blog-key-points` | 2점 | filter_metadata에서 safetensors |  |
| `psyche/KoT5-summarization` | 2점 | filter_metadata에서 safetensors |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `ainize/kobart-news` | 믿을 수 있는 단계엔 없고 filter_metadata에만 pytorch_bin |  |
| `csebuetnlp/mT5_m2m_crossSum` | 믿을 수 있는 단계엔 없고 filter_metadata에만 pytorch_bin |  |
| `csebuetnlp/mT5_m2m_crossSum_enhanced` | 믿을 수 있는 단계엔 없고 filter_metadata에만 pytorch_bin |  |
| `csebuetnlp/mT5_m2o_english_crossSum` | 믿을 수 있는 단계엔 없고 filter_metadata에만 pytorch_bin |  |
| `csebuetnlp/mT5_multilingual_XLSum` | 믿을 수 있는 단계엔 없고 filter_metadata에만 pytorch_bin |  |


