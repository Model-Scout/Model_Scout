# semantic_constraint 판정 워크시트

**숫자 검증은 명령 한 줄이 전부 합니다.**

```bash
cd ai && ../.venv/bin/python test/golden/v2/tools/verify.py semantic_constraint
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

코퍼스 3872행 · 2026-10-31 기준 · 질의 10개 · 사람이 볼 것 **112개**

---

### `sm01` ≤4.0B · core만 · text-generation · hard

> 의료 분야에 쓸 한국어 LLM이 필요해. 많이 쓰이는 것 중에 파라미터 4B 이하인 모델로.

조건 → 질의문 근거

- `tasks=["text-generation"]` ← LLM → text-generation
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)
- `max_parameters_billion=4.0` ← 4B 이하

판정 규칙 (판정 전에 고정)

- **must** 의료 도메인 용도가 claim 또는 model_id에서 확인된다
- **2점** 한국어 의료 데이터로 특화 학습된 것이 명시돼 있다
- **1점** 의료를 언급하나 다국어 모델이거나, 의료가 부가 기능인 범용 모델

후보 270개 전수 스캔 → 🚩 1 / ⚠️ 19 / ✅ 250

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `OpenMed/Ministral-3B-PII-Preview` | 2점 | semantic_metadata에서 clinical |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `AtomicChat/LFM3-1.7B-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 specialized |  |
| `LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 domain |  |
| `LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 domain |  |
| `LiquidAI/LFM2-1.2B-RAG` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 specialized |  |
| `LiquidAI/LFM2-1.2B-RAG-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 specialized |  |
| `LiquidAI/LFM3-1.7B` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 specialized |  |
| `SamsungSDS-Research/SGuard-ContentFilter-2B-v1` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 domain, specialized |  |
| `SamsungSDS-Research/SGuard-JailbreakFilter-2B-v1` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 domain, specialized |  |
| `ThomasBaruzier/EXAONE-3.5-2.4B-Instruct-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 domain |  |
| `ToxicityPrompts/PolyGuard-Qwen-Smol` | 믿을 수 있는 단계엔 없고 README 원문에만 specialized |  |
| `Vortecks/LFM3-1.7B-Heretic-Abliterated-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 specialized |  |
| `Vortecks/LFM3-1.7B-Heretic-Abliterated-i1-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 specialized |  |
| `aixk/BAAR2-3M` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 specialized |  |
| `aixk/BAAR3-19M` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 specialized |  |
| `aixk/BAAR6-9M-7` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 specialized |  |
| `inboxpraveen/Kavach-PII-270M` | 믿을 수 있는 단계엔 없고 README 원문에만 medical |  |
| `utter-project/EuroMoE-2.6B-A0.6B-Instruct-2512` | 믿을 수 있는 단계엔 없고 README 원문에만 specialized |  |
| `utter-project/EuroMoE-2.6B-A0.6B-Instruct-Preview` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 specialized |  |
| `yasserrmd/Coder-GRPO-3B` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 domain |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 250개 — `0xzknw/LFM2.5-1.2B-Thinking-Heretic`, `0xzknw/LFM2.5-2.6B-Heretic-NX-PRIME`, `42dot/42dot_LLM-PLM-1.3B`, `42dot/42dot_LLM-SFT-1.3B`, `AMAImedia/Tiny-Aya-3.3B-L2-Thinker-BF16-GGUF`, `Bllossom/llama-3.2-Korean-Bllossom-3B` …


### `sm02` ≤100M · automatic-speech-recognition · hard

> 실시간으로 받아쓰기를 해야 해. 스트리밍·저지연 처리를 지원하는 한국어 음성 인식 모델 중 파라미터 100M 이하인 것을 찾고 있어.

조건 → 질의문 근거

- `tasks=["automatic-speech-recognition"]` ← 음성 인식
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.1` ← 온디바이스에서 … 파라미터 100M 이하

판정 규칙 (판정 전에 고정)

- **must** 스트리밍·실시간 처리 지원이 claim에 명시돼 있다
- **2점** 스트리밍·실시간 용도가 명시돼 있다
- **1점** 실시간 처리 근거는 있으나 지연시간·지원 방식이 불명확하다

후보 19개 전수 스캔 → 🚩 8 / ⚠️ 0 / ✅ 11

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `RedHatAI/whisper-tiny` | 1점 | semantic_metadata에서 real-time |  |
| `handy-computer/whisper-base-gguf` | 1점 | semantic_metadata에서 real-time |  |
| `handy-computer/whisper-tiny-gguf` | 1점 | semantic_metadata에서 real-time |  |
| `neurlang/ipa-whisper-base` | 1점 | semantic_metadata에서 real-time |  |
| `openai/whisper-base` | 1점 | semantic_metadata에서 real-time |  |
| `openai/whisper-tiny` | 1점 | semantic_metadata에서 real-time |  |
| `unsloth/whisper-base` | 1점 | semantic_metadata에서 real-time |  |
| `unsloth/whisper-tiny` | 1점 | semantic_metadata에서 real-time |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 11개 — `Bingsu/distilhubert-ko-zeroth`, `Kkonjeong/wav2vec2-base-korean`, `handy-computer/moonshine-base-ko-gguf`, `handy-computer/moonshine-tiny-ko-gguf`, `mlx-community/whisper-base-asr-fp16`, `mlx-community/whisper-tiny-asr-fp16` …


### `sm03` ≤500M · translation · hard

> 한국어를 영어로 번역하는 경량 모델이 필요해. 파라미터 500M 이하인 것으로.

조건 → 질의문 근거

- `tasks=["translation"]` ← 번역
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.5` ← 파라미터 500M 이하

판정 규칙 (판정 전에 고정)

- **must** 한국어→영어 방향이 model_id 또는 claim에서 확인된다
- **2점** ko→en 방향이 명시돼 있다
- **1점** 다국어 모델로 ko·en을 모두 지원하나 방향 명시가 없다

후보 14개 전수 스캔 → 🚩 1 / ⚠️ 6 / ✅ 7

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Helsinki-NLP/opus-mt-tc-big-ko-en` | 2점 | model_id에서 ko-en |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Babelscape/mrebel-base` | 믿을 수 있는 단계엔 없고 filter_metadata에만 m2m |  |
| `Helsinki-NLP/opus-mt-tc-big-en-ko` | 믿을 수 있는 단계엔 없고 model_id에만 en-ko |  |
| `Neurora/opus-hplt-en-ko-v2.0` | 믿을 수 있는 단계엔 없고 model_id에만 en-ko |  |
| `alirezamsh/small100` | 믿을 수 있는 단계엔 없고 filter_metadata에만 m2m |  |
| `dhtocks/nllb-200-distilled-350M_en-ko` | 믿을 수 있는 단계엔 없고 model_id에만 en-ko, nllb |  |
| `seongs/ke-t5-base-aihub-koen-translation-integrated-10m-en-to-ko` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 ko-en |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 7개 — `Darong/BlueT`, `Helsinki-NLP/opus-mt_tiny_kor-eng`, `Sube126/Hy-MT2-1.8B-1.25Bit-MLX`, `kuotient/Hy-MT2-1.8B-1.25Bit-MLX`, `sappho192/aihub-ja-ko-translator`, `sappho192/ffxiv-ja-ko-translator` …


### `sm04` ≤1.0B · question-answering · hard

> 한국어 기계독해용 모델을 찾고 있어. 파라미터 1B 이하로.

조건 → 질의문 근거

- `tasks=["question-answering"]` ← 기계독해 → question-answering
- `korean_required=true` ← 한국어
- `max_parameters_billion=1.0` ← 파라미터 1B 이하

판정 규칙 (판정 전에 고정)

- **must** 추출형 기계독해 용도가 claim 또는 model_id에서 확인된다
- **2점** KorQuAD 등 한국어 독해 데이터로 학습됐다
- **1점** 다국어 QA 모델이거나 SQuAD 기반이고 한국어를 포함한다

후보 8개 전수 스캔 → 🚩 2 / ⚠️ 2 / ✅ 4

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `monologg/koelectra-base-v3-finetuned-korquad` | 2점 | model_id에서 korquad |  |
| `monologg/koelectra-small-v2-distilled-korquad-384` | 2점 | model_id에서 korquad |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `bespin-global/klue-bert-base-aihub-mrc` | 믿을 수 있는 단계엔 없고 model_id에만 mrc |  |
| `timpal0l/mdeberta-v3-base-squad2` | 믿을 수 있는 단계엔 없고 model_id에만 squad |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 4개 — `FreedomIntelligence/Apollo-MoE-0.5B`, `mradermacher/Prototype-Virus-1B-GGUF`, `mradermacher/Prototype-Virus-1B-i1-GGUF`, `mradermacher/next-1b-GGUF`


### `sm05` ctx≥131,072 · text-classification · hard

> 아주 긴 입력을 받아서 안전성이나 품질을 평가하는 한국어 모델이 필요해. 컨텍스트 131072 토큰 이상인 것으로.

조건 → 질의문 근거

- `tasks=["text-classification"]` ← 평가·분류 → text-classification
- `korean_required=true` ← 한국어
- `min_context_length=131072` ← 컨텍스트 131072 토큰 이상

판정 규칙 (판정 전에 고정)

- **must** 안전성·품질 평가 용도가 claim 또는 model_id에서 확인된다
- **2점** 보상 모델·세이프티 분류 등 평가 전용으로 만들어졌다
- **1점** 점수를 내는 모델이나 안전성·품질 평가 용도가 명시되지 않았다

후보 10개 전수 스캔 → 🚩 5 / ⚠️ 4 / ✅ 1

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Metabaron6/Shieldstral-1.0-3B-GGUF` | 2점 | semantic_metadata에서 safety, moderation, judge |  |
| `mp-juuuns/qwen35-c8q-distilled-8l-edge-classifier-gguf` | 2점 | semantic_metadata에서 safety |  |
| `sky7350/Mica-v0.5-4B` | 2점 | semantic_metadata에서 guard |  |
| `astroware/HaloGuard1-Gen-0.8B` | 2점 | model_id에서 guard |  |
| `astroware/HaloGuard1-Gen-4B` | 2점 | model_id에서 guard |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `chaoliangUNSW/Jev-Style-0.8B-Decision-v3` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 score |  |
| `chaoliangUNSW/Jev-Style-0.8B-Decision-v3-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 score |  |
| `quevirus/Xevn-4B-GGUF` | 믿을 수 있는 단계엔 없고 README 원문에만 score |  |
| `sky7350/Mica-v0.1-4B` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 score |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 1개 — `ethicalabs/Echo-DSRN-v0.1.3-Intent-CLF`


### `sm06` ≤1.0B · image-text-to-text · hard

> 문서나 표를 읽어야 해서 OCR이 되는 한국어 이미지-텍스트 모델을 찾아줘. 파라미터 1B 이하인 것으로.

조건 → 질의문 근거

- `tasks=["image-text-to-text"]` ← 이미지-텍스트
- `korean_required=true` ← 한국어
- `max_parameters_billion=1.0` ← 파라미터 1B 이하

판정 규칙 (판정 전에 고정)

- **must** 문서·표·OCR 처리 용도가 claim 또는 model_id에서 확인된다
- **2점** 한국어 문서·OCR 전용으로 학습된 것이 명시돼 있다
- **1점** 다국어 VLM으로 문서 처리가 가능하나 한국어 특화 명시가 없다

후보 13개 전수 스캔 → 🚩 6 / ⚠️ 7 / ✅ 0

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `LiquidAI/LFM2.5-VL-450M-MLX-4bit` | 1점 | semantic_metadata에서 document |  |
| `LiquidAI/LFM2.5-VL-450M-MLX-5bit` | 1점 | semantic_metadata에서 document |  |
| `LiquidAI/LFM2.5-VL-450M-MLX-6bit` | 1점 | semantic_metadata에서 document |  |
| `LiquidAI/LFM2.5-VL-450M-MLX-8bit` | 1점 | semantic_metadata에서 document |  |
| `mlx-community/LFM2.5-VL-450M-8bit` | 1점 | semantic_metadata에서 document |  |
| `localdeel/ko-hand-ocr-vl` | 1점 | model_id에서 ocr |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `LiquidAI/LFM2.5-VL-450M` | 믿을 수 있는 단계엔 없고 README 원문에만 ocr, document, table |  |
| `LiquidAI/LFM2.5-VL-450M-MLX-bf16` | 믿을 수 있는 단계엔 없고 README 원문에만 document |  |
| `Mattimax/DAC6.5` | 믿을 수 있는 단계엔 없고 README 원문에만 document |  |
| `coder3101/LFM2.5-VL-450M-heretic` | 믿을 수 있는 단계엔 없고 README 원문에만 ocr, document, table |  |
| `cstr/internvl2-1b-crispembed-GGUF` | 믿을 수 있는 단계엔 없고 README 원문에만 document, table |  |
| `mlx-community/LFM2.5-VL-450M-6bit` | 믿을 수 있는 단계엔 없고 README 원문에만 document |  |
| `saidutta69/LFM2.5-VL-450M-heretic` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 table |  |


### `sm07` ≤100M · feature-extraction · hard

> RAG에 쓸 한국어 검색용 임베딩 모델이 필요해. 파라미터 100M 이하인 것으로.

조건 → 질의문 근거

- `tasks=["feature-extraction"]` ← 임베딩 → feature-extraction
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.1` ← 파라미터 100M 이하

판정 규칙 (판정 전에 고정)

- **must** 검색·RAG 용도가 claim 또는 model_id에서 확인된다
- **2점** 한국어 검색·RAG 용도로 학습된 것이 명시돼 있다
- **1점** 문장 유사도 모델로 검색에도 쓸 수 있으나 검색 용도 명시가 없다

후보 15개 전수 스캔 → 🚩 8 / ⚠️ 4 / ✅ 3

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Hisham480/multilingual-r2` | 2점 | semantic_metadata에서 retriev, rag, passage, search |  |
| `ibm-granite/granite-embedding-97m-multilingual-r2` | 2점 | semantic_metadata에서 retriev, rag, passage, search |  |
| `onnx-community/granite-embedding-97m-multilingual-r2-ONNX` | 2점 | semantic_metadata에서 retriev, rag, search |  |
| `codefuse-ai/F2LLM-v2-80M` | 1점 | semantic_metadata에서 retriev, search |  |
| `utter-project/mHuBERT-147` | 1점 | semantic_metadata에서 search |  |
| `utter-project/mHuBERT-147-base-1st-iter` | 1점 | semantic_metadata에서 search |  |
| `utter-project/mHuBERT-147-base-2nd-iter` | 1점 | semantic_metadata에서 search |  |
| `xnohat/granite-embedding-97m-multilingual-r2-GGUF` | 1점 | semantic_metadata에서 retriev |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `CISCai/jina-embeddings-v3-separation-distilled` | 믿을 수 있는 단계엔 없고 README 원문에만 rag |  |
| `Xenova/kobert` | 믿을 수 있는 단계엔 없고 README 원문에만 rag |  |
| `monologg/kobert` | 믿을 수 있는 단계엔 없고 README 원문에만 rag |  |
| `mykor/granite-embedding-97m-multilingual-r2-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 similar |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 2개 — `madatnlp/km-bert`, `skt/kobert-base-v1`
- **claim 자체가 비어 있음** 1개 — `fish9903/Emotion_KoBERT1`


### `sm08` ≤100M · sentence-similarity · easy

> 두 문장이 얼마나 비슷한지 점수를 내는 한국어 모델이 필요해. 파라미터 100M 이하인 것으로.

조건 → 질의문 근거

- `tasks=["sentence-similarity"]` ← 문장 유사도
- `korean_required=true` ← 한국어
- `max_parameters_billion=0.1` ← 파라미터 100M 이하

판정 규칙 (판정 전에 고정)

- **must** 문장 유사도 점수 산출 용도가 확인된다
- **2점** 한국어 STS 데이터로 학습된 전용 모델
- **1점** 다국어 문장 임베딩 모델이거나 검색 용도가 주된 모델

후보 14개 전수 스캔 → 🚩 14 / ⚠️ 0 / ✅ 0

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `alphaedge-ai/multilingual-e5-small-kor-32768` | 1점 | filter_metadata에서 similarity |  |
| `exp-models/dragonkue-KoEn-E5-Tiny` | 1점 | filter_metadata에서 similarity |  |
| `gomyk/intent-student-L4_uniform_distilled` | 1점 | filter_metadata에서 similarity |  |
| `gomyk/intent-student-L6_uniform_distilled` | 1점 | filter_metadata에서 similarity |  |
| `gomyk/me5s-me5s_compressed_v3_distilled` | 1점 | filter_metadata에서 similarity |  |
| `gomyk/me5s-student-me5s_compressed_v3_distilled` | 1점 | filter_metadata에서 similarity |  |
| `gomyk/me5s-student-me5s_compressed_v4_distilled` | 1점 | filter_metadata에서 similarity |  |
| `gomyk/minilm-student-L4_uniform_distilled` | 1점 | filter_metadata에서 similarity |  |
| `gomyk/minilm-student-L6_uniform_distilled` | 1점 | filter_metadata에서 similarity |  |
| `gomyk/modernbert-student-modernbert_L4_uniform_distilled` | 1점 | filter_metadata에서 similarity |  |
| `setu4993/LEALLA-small` | 1점 | filter_metadata에서 similarity |  |
| `smartmind/roberta-ko-small-tsdae` | 1점 | filter_metadata에서 similarity |  |
| `ddobokki/klue-roberta-small-nli-sts` | 1점 | model_id에서 sts |  |
| `ddobokki/unsup-simcse-klue-roberta-small` | 1점 | model_id에서 simcse |  |


### `sm09` ≤300M · core만 · text-classification · easy

> 상품 리뷰의 감성을 분류하는 한국어 모델을 찾고 있어. 많이 쓰이는 것 중에 300M 이하인 것으로.

조건 → 질의문 근거

- `tasks=["text-classification"]` ← 분류 → text-classification
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)
- `max_parameters_billion=0.3` ← 300M 이하

판정 규칙 (판정 전에 고정)

- **must** 감성 분류 용도가 claim 또는 model_id에서 확인된다
- **2점** NSMC 등 한국어 리뷰 감성 데이터로 학습됐다
- **1점** 다국어 감성 분류 모델이거나, 도메인이 리뷰가 아닌 일반 감성 분류

후보 28개 전수 스캔 → 🚩 16 / ⚠️ 2 / ✅ 10

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Copycats/koelectra-base-v3-generalized-sentiment-analysis` | 2점 | model_id에서 sentiment |  |
| `daekeun-ml/koelectra-small-v3-nsmc` | 2점 | model_id에서 nsmc |  |
| `Horizon-Labs/content-safety-guard-small` | 1점 | semantic_metadata에서 review |  |
| `Zeolit/lettuce-thymos-26m-v1` | 1점 | semantic_metadata에서 emotion |  |
| `knowledgator/opir-edge-multilang-v1.0` | 1점 | semantic_metadata에서 review |  |
| `snunlp/KR-FinBert-SC` | 1점 | semantic_metadata에서 sentiment |  |
| `DataWizardd/finbert-sentiment-ko` | 1점 | model_id에서 sentiment |  |
| `FISA-conclave/klue-roberta-news-sentiment` | 1점 | model_id에서 sentiment |  |
| `MelissaJ/koelectra-emotion-6-emotion-base` | 1점 | model_id에서 emotion |  |
| `agentlans/multilingual-e5-small-aligned-sentiment` | 1점 | model_id에서 sentiment |  |
| `circulus/koelectra-sentiment-v1` | 1점 | model_id에서 sentiment |  |
| `clapAI/mmBERT-small-multilingual-sentiment` | 1점 | model_id에서 sentiment |  |
| `clapAI/modernBERT-base-multilingual-sentiment` | 1점 | model_id에서 sentiment |  |
| `clapAI/roberta-base-multilingual-sentiment` | 1점 | model_id에서 sentiment |  |
| `tabularisai/multilingual-emotion-classification` | 1점 | model_id에서 emotion |  |
| `tabularisai/multilingual-sentiment-analysis` | 1점 | model_id에서 sentiment |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `knowledgator/opir-multitask-multilang-v1.0` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 binary |  |
| `livekit/turn-detector` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 binary |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 9개 — `Horizon-Labs/multilingual-toxicity-small`, `Horizon-Labs/prompt-injection-guard-small`, `Huffon/klue-roberta-base-nli`, `amber-tech/bert-multilingual-passage-reranking-msmarco`, `autopilot-ai/EthicalEye`, `lokas/spam-usernames-classifier` …
- **claim 자체가 비어 있음** 1개 — `circulus/koelectra-polite-v1`


### `sm10` ≤300M · core만 · text-classification · hard

> 혐오 표현이나 욕설을 걸러내는 한국어 모델이 필요해. 많이 쓰이는 것 중 파라미터 300M 이하인 것으로.

조건 → 질의문 근거

- `tasks=["text-classification"]` ← 분류 → text-classification
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)
- `max_parameters_billion=0.3` ← 파라미터 300M 이하

판정 규칙 (판정 전에 고정)

- **must** 혐오·욕설 탐지 용도가 claim 또는 model_id에서 확인된다
- **2점** UnSmile 등 한국어 혐오 표현 데이터로 학습됐다
- **1점** 다국어 유해성 분류 모델이거나, 일반 세이프티 분류 모델

후보 28개 전수 스캔 → 🚩 3 / ⚠️ 4 / ✅ 21

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `autopilot-ai/EthicalEye` | 1점 | semantic_metadata에서 hate, abusive |  |
| `knowledgator/opir-multitask-multilang-v1.0` | 1점 | semantic_metadata에서 toxic |  |
| `Horizon-Labs/multilingual-toxicity-small` | 1점 | model_id에서 toxic |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Horizon-Labs/content-safety-guard-small` | 믿을 수 있는 단계엔 없고 model_id에만 safety, guard |  |
| `Horizon-Labs/prompt-injection-guard-small` | 믿을 수 있는 단계엔 없고 model_id에만 guard |  |
| `Zeolit/lettuce-thymos-26m-v1` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 safety |  |
| `knowledgator/opir-edge-multilang-v1.0` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 safety |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 19개 — `Copycats/koelectra-base-v3-generalized-sentiment-analysis`, `DataWizardd/finbert-sentiment-ko`, `FISA-conclave/klue-roberta-news-sentiment`, `Huffon/klue-roberta-base-nli`, `MelissaJ/koelectra-emotion-6-emotion-base`, `agentlans/multilingual-e5-small-aligned-sentiment` …
- **claim 자체가 비어 있음** 2개 — `circulus/koelectra-polite-v1`, `circulus/koelectra-sentiment-v1`


