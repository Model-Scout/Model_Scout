# benchmark_lookup 판정 워크시트

**숫자 검증은 명령 한 줄이 전부 합니다.**

```bash
cd ai && ../.venv/bin/python test/golden/v2/tools/verify.py benchmark_lookup
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

코퍼스 3872행 · 2026-10-31 기준 · 질의 10개 · 사람이 볼 것 **130개**

---

### `bl01` ≤8.0B · core만 · 값공개 · text-generation · hard

> KMMLU 점수를 공개한 한국어 LLM을 찾고 있어. 많이 쓰이는 것 중에 파라미터 8B 이하로 공개된 모델로.

조건 → 질의문 근거

- `tasks=["text-generation"]` ← 생성 모델 / LLM
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)
- `max_parameters_billion=8.0` ← 8B 이하
- `require_known_parameters=true` ← 파라미터 수가 공개된

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 KMMLU 결과가 있다
- **2점** KMMLU 점수가 수치로 기록돼 있다
- **1점** KMMLU를 언급하나 점수가 수치로 확인되지 않거나, MMLU 등 인접 벤치마크만 있다

후보 247개 전수 스캔 → 🚩 2 / ⚠️ 21 / ✅ 224

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `skt/A.X-3.1-Light` | 2점 | benchmark_metadata에서 kmmlu |  |
| `skt/A.X-4.0-Light` | 2점 | benchmark_metadata에서 kmmlu |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `0xzknw/LFM2.5-2.6B-Heretic-NX-PRIME` | 믿을 수 있는 단계엔 없고 README 원문에만 mmlu |  |
| `Goekdeniz-Guelmez/Josiefied-Qwen2.5-7B-Instruct-abliterated-v2` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmlu |  |
| `KridgeDookie/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmlu |  |
| `LiquidAI/LFM2-1.2B` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmlu |  |
| `LiquidAI/LFM2-2.6B` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmlu |  |
| `LiquidAI/LFM2-350M` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmlu |  |
| `LiquidAI/LFM2-700M` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmlu |  |
| `Orion-zhen/Qwen2.5-7B-Instruct-Uncensored` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmlu |  |
| `beomi/Yi-Ko-6B` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmlu |  |
| `huihui-ai/Qwen2.5-7B-Instruct-abliterated-v2` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmlu |  |
| `konantech/Konan-LLM-OND` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mmlu |  |
| `richardyoung/LFM2.5-1.2B-Instruct-heretic` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmlu |  |
| `richardyoung/Phi-4-mini-instruct-heretic` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmlu |  |
| `saidutta69/granite-4.1-3b-heretic` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmlu |  |
| `swartbwoy/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmlu |  |
| `youngseok12/AX-3.1-Light-sft_v0_21_source_screen_essential_medical_300` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mmlu |  |
| `youngseok12/AX-3.1-Light-sft_v0_21_source_screen_numerical_300` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mmlu |  |
| `youngseok12/AX-3.1-Light-sft_v0_21_source_screen_scitech_mrc_300` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mmlu |  |
| `youngseok12/AX-3.1-Light-sft_v3_1_A_control` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mmlu |  |
| `youngseok12/AX-3.1-Light-sft_v3_1_C_recommended` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mmlu |  |
| `youngseok12/AX-3.1-Light-sft_v3_1_E_format_safe` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mmlu |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 224개 — `0xzknw/LFM2.5-1.2B-Thinking-Heretic`, `42dot/42dot_LLM-PLM-1.3B`, `42dot/42dot_LLM-SFT-1.3B`, `aixk/BAAR2-150M`, `aixk/BAAR2-3M`, `aixk/BAAR3-19M` …


### `bl02` core만 · feature-extraction · hard

> MTEB 결과가 공개된 한국어 임베딩 모델을 추천해줘. 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["feature-extraction"]` ← 임베딩 → feature-extraction
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 MTEB 결과가 있다
- **2점** MTEB 점수가 수치로 기록돼 있다
- **1점** MTEB를 언급하나 점수가 확인되지 않거나, BEIR 등 인접 벤치마크만 있다

후보 64개 전수 스캔 → 🚩 8 / ⚠️ 15 / ✅ 41

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `amazon/Titan-text-embeddings-v2` | 2점 | benchmark_metadata에서 mteb |  |
| `intfloat/multilingual-e5-large` | 2점 | benchmark_metadata에서 mteb |  |
| `intfloat/multilingual-e5-large-instruct` | 2점 | benchmark_metadata에서 mteb |  |
| `microsoft/harrier-oss-v1-0.6b` | 2점 | benchmark_metadata에서 mteb |  |
| `microsoft/harrier-oss-v1-270m` | 2점 | benchmark_metadata에서 mteb |  |
| `microsoft/harrier-oss-v1-27b` | 2점 | benchmark_metadata에서 mteb |  |
| `telepix/PIXIE-Rune-v1.5` | 2점 | benchmark_metadata에서 mteb |  |
| `ibm-granite/granite-embedding-311m-multilingual-r2` | 1점 | benchmark_metadata에서 mteb |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `codefuse-ai/F2LLM-v2-0.6B` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `codefuse-ai/F2LLM-v2-1.7B` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `codefuse-ai/F2LLM-v2-14B` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `codefuse-ai/F2LLM-v2-160M` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `codefuse-ai/F2LLM-v2-330M` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `codefuse-ai/F2LLM-v2-4B` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `codefuse-ai/F2LLM-v2-80M` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `codefuse-ai/F2LLM-v2-8B` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `jinaai/jina-clip-v2` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `jinaai/jina-embeddings-v3` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `jinaai/jina-embeddings-v3-hf` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `onnx-community/harrier-oss-v1-0.6b-ONNX` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `onnx-community/harrier-oss-v1-270m-ONNX` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `telepix/PIXIE-Rune-v1.0` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `yjoonjang/splade-ko-v1` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 39개 — `BM-K/KoSimCSE-bert-multitask`, `BM-K/KoSimCSE-roberta`, `BM-K/KoSimCSE-roberta-multitask`, `CISCai/jina-embeddings-v3-separation-distilled`, `codefuse-ai/ML-Embed-0.6B`, `cstr/multilingual-e5-small-GGUF` …
- **주 task가 sentence-similarity** 2개 — `omai-research/milco-300m`, `omai-research/milco-650m`


### `bl03` ≤500M · core만 · 값공개 · sentence-similarity · hard

> 파라미터 500M 이하로 공개된 한국어 문장 임베딩 모델 중에 MTEB 점수가 있는 걸 찾아줘. 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["sentence-similarity"]` ← 문장 임베딩
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=0.5` ← 500M 이하
- `require_known_parameters=true` ← 로 공개된

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 MTEB 결과가 있다
- **2점** MTEB 점수가 수치로 기록돼 있다
- **1점** MTEB를 언급하나 점수가 확인되지 않거나 인접 벤치마크만 있다

후보 39개 전수 스캔 → 🚩 5 / ⚠️ 12 / ✅ 22

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Alibaba-NLP/gte-multilingual-base` | 2점 | benchmark_metadata에서 mteb |  |
| `Snowflake/snowflake-arctic-embed-m-v2.0` | 2점 | benchmark_metadata에서 mteb |  |
| `intfloat/multilingual-e5-base` | 2점 | benchmark_metadata에서 mteb |  |
| `Hiveurban/multilingual-e5-base` | 1점 | benchmark_metadata에서 mteb |  |
| `beademiguelperez/sentence-transformers-multilingual-e5-small` | 1점 | benchmark_metadata에서 mteb |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `LiquidAI/LFM2-ColBERT-350M` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 beir |  |
| `LiquidAI/LFM2.5-Embedding-350M` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 beir |  |
| `MintplexLabs/multilingual-e5-small` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `dragonkue/multilingual-e5-small-ko` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `dragonkue/multilingual-e5-small-ko-v2` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `exp-models/dragonkue-KoEn-E5-Tiny` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `facebook/drama-large` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 beir |  |
| `ibm-granite/granite-embedding-107m-multilingual` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `ibm-granite/granite-embedding-278m-multilingual` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `intfloat/multilingual-e5-small` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |
| `nomic-ai/nomic-embed-text-v2-moe` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 beir |  |
| `shannondata/multilingual-e5-small` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 mteb |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 22개 — `bespin-global/klue-sroberta-base-continue-learning-by-mnr`, `dell-research-harvard/lt-wikidata-comp-multi`, `efederici/e5-base-multilingual-4096`, `hunkim/sentence-transformer-klue`, `jhgan/ko-sbert-multitask`, `jhgan/ko-sbert-nli` …


### `bl04` ≤1.0B · core만 · 값공개 · automatic-speech-recognition · hard

> LibriSpeech 결과가 README에 있는 한국어 음성 인식 모델을 찾고 있어. 1B 이하로 공개된 것 중 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["automatic-speech-recognition"]` ← 음성 인식
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=1.0` ← 1B 이하
- `require_known_parameters=true` ← 파라미터 수가 공개된

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 LibriSpeech 결과가 있다
- **2점** LibriSpeech WER 등이 수치로 기록돼 있다
- **1점** LibriSpeech를 언급하나 수치가 없거나, 인접 음성 데이터셋만 있다

후보 34개 전수 스캔 → 🚩 5 / ⚠️ 5 / ✅ 24

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `openai/whisper-base` | 2점 | benchmark_metadata에서 librispeech |  |
| `openai/whisper-medium` | 2점 | benchmark_metadata에서 librispeech |  |
| `openai/whisper-small` | 2점 | benchmark_metadata에서 librispeech |  |
| `openai/whisper-tiny` | 2점 | benchmark_metadata에서 librispeech |  |
| `unsloth/whisper-small` | 2점 | benchmark_metadata에서 librispeech |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Qwen/Qwen3-ASR-0.6B-hf` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 librispeech |  |
| `bezzam/omniasr-ctc-300m-v2` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 librispeech |  |
| `mlx-community/whisper-tiny-asr-fp16` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 librispeech |  |
| `openai/whisper-large-v3-turbo` | 믿을 수 있는 단계엔 없고 README 원문에만 librispeech |  |
| `unsloth/whisper-large-v3-turbo` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 librispeech |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 24개 — `42MARU/ko-spelling-wav2vec2-conformer-del-1s`, `Aliados/nemotron-3.5-asr-streaming-0.6b`, `aufklarer/Qwen3-ASR-1.7B-MLX-4bit`, `aufklarer/Qwen3-ASR-CoreML`, `Edge0/Audio8-ASR-0.1B`, `facebook/mms-1b-all` …


### `bl05` ≤1.0B · core만 · 값공개 · automatic-speech-recognition · hard

> FLEURS 점수가 공개된 한국어 음성 인식 모델 있어? 1B 이하로 공개된 것 중 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["automatic-speech-recognition"]` ← 음성 인식
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=1.0` ← 1B 이하
- `require_known_parameters=true` ← 파라미터 수가 공개된

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 FLEURS 결과가 있다
- **2점** FLEURS 점수가 수치로 기록돼 있다
- **1점** FLEURS를 언급하나 수치가 없거나, 인접 다국어 음성 벤치마크만 있다

후보 34개 전수 스캔 → 🚩 1 / ⚠️ 3 / ✅ 30

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `seastar105/whisper-medium-komixv2` | 1점 | benchmark_metadata에서 fleurs |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Aliados/nemotron-3.5-asr-streaming-0.6b` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 fleurs |  |
| `Qwen/Qwen3-ASR-0.6B-hf` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 voxpopuli |  |
| `nvidia/nemotron-3.5-asr-streaming-0.6b` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 fleurs |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 30개 — `42MARU/ko-spelling-wav2vec2-conformer-del-1s`, `aufklarer/Qwen3-ASR-1.7B-MLX-4bit`, `aufklarer/Qwen3-ASR-CoreML`, `bezzam/omniasr-ctc-300m-v2`, `Edge0/Audio8-ASR-0.1B`, `facebook/mms-1b-all` …


### `bl06` ≤1.0B · core만 · 값공개 · automatic-speech-recognition · hard

> Common Voice 평가 결과가 있는 한국어 음성 인식 모델을 추천해줘. 1B 이하로 공개된 것 중 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["automatic-speech-recognition"]` ← 음성 인식
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=1.0` ← 1B 이하
- `require_known_parameters=true` ← 파라미터 수가 공개된

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 Common Voice 결과가 있다
- **2점** Common Voice 점수가 수치로 기록돼 있다
- **1점** Common Voice를 언급하나 수치가 없거나 인접 벤치마크만 있다

후보 34개 전수 스캔 → 🚩 5 / ⚠️ 1 / ✅ 28

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `openai/whisper-base` | 1점 | benchmark_metadata에서 common voice |  |
| `openai/whisper-medium` | 1점 | benchmark_metadata에서 common voice |  |
| `openai/whisper-small` | 1점 | benchmark_metadata에서 common voice |  |
| `openai/whisper-tiny` | 1점 | benchmark_metadata에서 common voice |  |
| `unsloth/whisper-small` | 1점 | benchmark_metadata에서 common voice |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Qwen/Qwen3-ASR-0.6B-hf` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 voxpopuli |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 28개 — `42MARU/ko-spelling-wav2vec2-conformer-del-1s`, `Aliados/nemotron-3.5-asr-streaming-0.6b`, `aufklarer/Qwen3-ASR-1.7B-MLX-4bit`, `aufklarer/Qwen3-ASR-CoreML`, `bezzam/omniasr-ctc-300m-v2`, `Edge0/Audio8-ASR-0.1B` …


### `bl07` ≤4.0B · core만 · 값공개 · text-generation · hard

> MMLU 점수가 공개된 한국어 LLM 중에 4B 이하로 공개된 걸 찾아줘. 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["text-generation"]` ← LLM → text-generation
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=4.0` ← 4B 이하
- `require_known_parameters=true` ← 로 공개된

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 MMLU 계열 결과가 있다
- **2점** MMLU 점수가 수치로 기록돼 있다
- **1점** MMLU를 언급하나 수치가 없거나, KMMLU·MMLU-Pro 등 변형만 있다

후보 178개 전수 스캔 → 🚩 9 / ⚠️ 3 / ✅ 166

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `KridgeDookie/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS` | 1점 | benchmark_metadata에서 mmlu |  |
| `LiquidAI/LFM2-1.2B` | 1점 | benchmark_metadata에서 mmlu |  |
| `LiquidAI/LFM2-2.6B` | 1점 | benchmark_metadata에서 mmlu |  |
| `LiquidAI/LFM2-350M` | 1점 | benchmark_metadata에서 mmlu |  |
| `LiquidAI/LFM2-700M` | 1점 | benchmark_metadata에서 mmlu |  |
| `richardyoung/LFM2.5-1.2B-Instruct-heretic` | 1점 | benchmark_metadata에서 mmlu |  |
| `richardyoung/Phi-4-mini-instruct-heretic` | 1점 | benchmark_metadata에서 mmlu |  |
| `saidutta69/granite-4.1-3b-heretic` | 1점 | benchmark_metadata에서 mmlu |  |
| `swartbwoy/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS` | 1점 | benchmark_metadata에서 mmlu |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `0xzknw/LFM2.5-2.6B-Heretic-NX-PRIME` | 믿을 수 있는 단계엔 없고 README 원문에만 hellaswag |  |
| `EleutherAI/polyglot-ko-1.3b` | 믿을 수 있는 단계엔 없고 README 원문에만 hellaswag |  |
| `EleutherAI/polyglot-ko-3.8b` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 hellaswag |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 166개 — `0xzknw/LFM2.5-1.2B-Thinking-Heretic`, `42dot/42dot_LLM-PLM-1.3B`, `42dot/42dot_LLM-SFT-1.3B`, `aixk/BAAR2-150M`, `aixk/BAAR2-3M`, `aixk/BAAR3-19M` …


### `bl08` ≤4.0B · core만 · 값공개 · text-generation · hard

> GPQA 결과를 공개한 한국어 LLM이 있을까? 4B 이하로 공개된 것 중 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["text-generation"]` ← LLM → text-generation
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=4.0` ← 4B 이하
- `require_known_parameters=true` ← 로 공개된

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 GPQA 결과가 있다
- **2점** GPQA 점수가 수치로 기록돼 있다
- **1점** GPQA를 언급하나 수치가 없거나 인접 추론 벤치마크만 있다

후보 178개 전수 스캔 → 🚩 2 / ⚠️ 1 / ✅ 175

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `richardyoung/LFM2.5-1.2B-Instruct-heretic` | 1점 | benchmark_metadata에서 gpqa |  |
| `richardyoung/Phi-4-mini-instruct-heretic` | 1점 | benchmark_metadata에서 gpqa |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `saidutta69/granite-4.1-3b-heretic` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmlu-pro |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 175개 — `0xzknw/LFM2.5-1.2B-Thinking-Heretic`, `0xzknw/LFM2.5-2.6B-Heretic-NX-PRIME`, `42dot/42dot_LLM-PLM-1.3B`, `42dot/42dot_LLM-SFT-1.3B`, `aixk/BAAR2-150M`, `aixk/BAAR2-3M` …


### `bl09` 조건 없음 · text-classification · hard

> KLUE 평가 결과가 README에 있는 한국어 텍스트 분류 모델을 찾고 있어.

조건 → 질의문 근거

- `tasks=["text-classification"]` ← 텍스트 분류
- `korean_required=true` ← 한국어

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 KLUE 결과가 있다
- **2점** KLUE 점수가 수치로 기록돼 있다
- **1점** KLUE를 언급하나 수치가 없거나, KorSTS·KorNLI 등 인접 한국어 벤치마크만 있다

후보 105개 전수 스캔 → 🚩 1 / ⚠️ 7 / ✅ 97

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `skt/A.X-Encoder-base` | 1점 | benchmark_metadata에서 klue |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `FISA-conclave/klue-roberta-news-sentiment` | 믿을 수 있는 단계엔 없고 model_id에만 klue |  |
| `Huffon/klue-roberta-base-nli` | 믿을 수 있는 단계엔 없고 model_id에만 klue |  |
| `LangQuant/LQ-FSE-base` | 믿을 수 있는 단계엔 없고 filter_metadata에만 klue |  |
| `bespin-global/klue-roberta-small-3i4k-intent-classification` | 믿을 수 있는 단계엔 없고 model_id에만 klue |  |
| `hun3359/klue-bert-base-sentiment` | 믿을 수 있는 단계엔 없고 model_id에만 klue |  |
| `likeyellow/klue-review-star` | 믿을 수 있는 단계엔 없고 model_id에만 klue |  |
| `serize/klue-roberta-base-nli-stage2` | 믿을 수 있는 단계엔 없고 model_id에만 klue |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 91개 — `agentlans/multilingual-e5-small-aligned-sentiment`, `amber-tech/bert-multilingual-passage-reranking-msmarco`, `amphora/KorFinASC-XLM-RoBERTa`, `autopilot-ai/EthicalEye`, `banjl4487/MODEL`, `chaoliangUNSW/Jev-Style-0.8B-Decision-v3` …
- **claim 자체가 비어 있음** 6개 — `circulus/koelectra-polite-v1`, `circulus/koelectra-sentiment-v1`, `circulus/koelectra-wellness-v1`, `kfkas/legal-question-filter-koelectra`, `monologg/koelectra-base-finetuned-nsmc`, `monologg/koelectra-small-finetuned-nsmc`


### `bl10` core만 · sentence-similarity · hard

> 한국어 STS 벤치마크 점수가 공개된 문장 유사도 모델을 추천해줘. 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["sentence-similarity"]` ← 문장 유사도
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 한국어 STS 계열 결과가 있다
- **2점** KorSTS 또는 KLUE-STS 점수가 수치로 기록돼 있다
- **1점** STS를 언급하나 한국어 STS인지 불명확하거나 수치가 없다

후보 71개 전수 스캔 → 🚩 8 / ⚠️ 16 / ✅ 47

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Alibaba-NLP/gte-multilingual-base` | 1점 | benchmark_metadata에서 stsb |  |
| `Hiveurban/multilingual-e5-base` | 1점 | benchmark_metadata에서 stsb |  |
| `RedHatAI/snowflake-arctic-embed-l-v2.0` | 1점 | benchmark_metadata에서 stsb |  |
| `SamilPwC-AXNode-GenAI/PwC-Embedding_expr` | 1점 | benchmark_metadata에서 korsts, klue-sts |  |
| `Snowflake/snowflake-arctic-embed-l-v2.0` | 1점 | benchmark_metadata에서 stsb |  |
| `Snowflake/snowflake-arctic-embed-m-v2.0` | 1점 | benchmark_metadata에서 stsb |  |
| `beademiguelperez/sentence-transformers-multilingual-e5-small` | 1점 | benchmark_metadata에서 stsb |  |
| `intfloat/multilingual-e5-base` | 1점 | benchmark_metadata에서 stsb |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `BidirLM/BidirLM-0.6B-Embedding` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `BidirLM/BidirLM-1B-Embedding` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `LiquidAI/LFM2.5-ColBERT-350M-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `LiquidAI/LFM2.5-Embedding-350M-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `bespin-global/klue-sroberta-base-continue-learning-by-mnr` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `dnotitia/DNA-VL-STEER-2B` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `dragonkue/BGE-m3-ko` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `dragonkue/snowflake-arctic-embed-l-v2.0-ko` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `jhgan/ko-sbert-multitask` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `jhgan/ko-sbert-nli` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `jhgan/ko-sbert-sts` | 믿을 수 있는 단계엔 없고 model_id에만 sts |  |
| `jhgan/ko-sroberta-multitask` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `snunlp/KR-SBERT-Medium-extended-klueNLItriplet_PARpair_QApair-klueSTS` | 믿을 수 있는 단계엔 없고 model_id에만 sts |  |
| `snunlp/KR-SBERT-V40K-klueNLI-augSTS` | 믿을 수 있는 단계엔 없고 model_id에만 sts |  |
| `upskyy/bge-m3-korean` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 sts |  |
| `upskyy/kf-deberta-multitask` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 47개 — `antoinelouis/colbert-xm`, `batiai/Qwen3-VL-Embedding-8B-GGUF`, `BidirLM/BidirLM-Omni-2.5B-Embedding`, `Casual-Autopsy/snowflake-arctic-embed-l-v2.0-gguf`, `ChristianAzinn/labse-gguf`, `cointegrated/SONAR_200_text_encoder` …


