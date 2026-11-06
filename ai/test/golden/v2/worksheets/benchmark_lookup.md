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

코퍼스 3872행 · 2026-10-31 기준 · 질의 10개 · 사람이 볼 것 **86개**

---

### `bl01` ≤8.0B · core만 · text-generation · hard

> KMMLU 점수를 공개한 한국어 LLM을 찾고 있어. 많이 쓰이는 것 중에 파라미터 8B 이하인 모델로.

조건 → 질의문 근거

- `tasks=["text-generation"]` ← 생성 모델 / LLM
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)
- `max_parameters_billion=8.0` ← 8B 이하

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 KMMLU 결과가 있다
- **2점** KMMLU 점수가 수치로 기록돼 있다
- **1점** KMMLU를 언급하나 점수가 수치로 확인되지 않는다

후보 379개 전수 스캔 → 🚩 2 / ⚠️ 0 / ✅ 377

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `skt/A.X-3.1-Light` | 2점 | benchmark_metadata에서 kmmlu |  |
| `skt/A.X-4.0-Light` | 2점 | benchmark_metadata에서 kmmlu |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 377개 — `0xzknw/LFM2.5-1.2B-Thinking-Heretic`, `0xzknw/LFM2.5-2.6B-Heretic-NX-PRIME`, `42dot/42dot_LLM-PLM-1.3B`, `42dot/42dot_LLM-SFT-1.3B`, `AMAImedia/Tiny-Aya-3.3B-L2-Thinker-BF16-GGUF`, `Archsloth/Qwen3-4B-GGUF` …


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

후보 64개 전수 스캔 → 🚩 7 / ⚠️ 2 / ✅ 55

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `amazon/Titan-text-embeddings-v2` | 2점 | benchmark_metadata에서 mteb |  |
| `ibm-granite/granite-embedding-311m-multilingual-r2` | 2점 | benchmark_metadata에서 mteb |  |
| `intfloat/multilingual-e5-large` | 2점 | benchmark_metadata에서 mteb |  |
| `intfloat/multilingual-e5-large-instruct` | 2점 | benchmark_metadata에서 mteb |  |
| `microsoft/harrier-oss-v1-0.6b` | 2점 | benchmark_metadata에서 mteb |  |
| `microsoft/harrier-oss-v1-270m` | 2점 | benchmark_metadata에서 mteb |  |
| `microsoft/harrier-oss-v1-27b` | 2점 | benchmark_metadata에서 mteb |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `telepix/PIXIE-Rune-v1.0` | 믿을 수 있는 단계엔 없고 README 원문에만 beir |  |
| `telepix/PIXIE-Rune-v1.5` | 믿을 수 있는 단계엔 없고 출처 불명확 benchmark 결과에만 mteb |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 53개 — `BM-K/KoSimCSE-bert-multitask`, `BM-K/KoSimCSE-roberta`, `BM-K/KoSimCSE-roberta-multitask`, `CISCai/jina-embeddings-v3-separation-distilled`, `ZurichNLP/unsup-simcse-xlm-roberta-base`, `codefuse-ai/F2LLM-v2-0.6B` …
- **주 task가 sentence-similarity** 2개 — `omai-research/milco-300m`, `omai-research/milco-650m`


### `bl03` ≤500M · core만 · sentence-similarity · hard

> 파라미터 500M 이하인 한국어 문장 임베딩 모델 중에 MTEB 점수가 있는 걸 찾아줘. 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["sentence-similarity"]` ← 문장 임베딩
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=0.5` ← 500M 이하

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 MTEB 결과가 있다
- **2점** MTEB 점수가 수치로 기록돼 있다
- **1점** MTEB를 언급하나 점수가 확인되지 않거나 인접 벤치마크만 있다

후보 46개 전수 스캔 → 🚩 5 / ⚠️ 5 / ✅ 36

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Alibaba-NLP/gte-multilingual-base` | 2점 | benchmark_metadata에서 mteb |  |
| `Hiveurban/multilingual-e5-base` | 2점 | benchmark_metadata에서 mteb |  |
| `Snowflake/snowflake-arctic-embed-m-v2.0` | 2점 | benchmark_metadata에서 mteb |  |
| `beademiguelperez/sentence-transformers-multilingual-e5-small` | 2점 | benchmark_metadata에서 mteb |  |
| `intfloat/multilingual-e5-base` | 2점 | benchmark_metadata에서 mteb |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `LiquidAI/LFM2-ColBERT-350M` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 beir |  |
| `LiquidAI/LFM2.5-Embedding-350M` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 beir |  |
| `facebook/drama-large` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 beir |  |
| `nomic-ai/nomic-embed-text-v2-moe` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 beir |  |
| `nomic-ai/nomic-embed-text-v2-moe-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 beir |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 36개 — `ChristianAzinn/labse-gguf`, `LiquidAI/LFM2.5-ColBERT-350M`, `LiquidAI/LFM2.5-ColBERT-350M-GGUF`, `LiquidAI/LFM2.5-Embedding-350M-GGUF`, `MintplexLabs/multilingual-e5-small`, `bespin-global/klue-sroberta-base-continue-learning-by-mnr` …


### `bl04` ≤1.0B · core만 · automatic-speech-recognition · hard

> LibriSpeech 결과가 README에 있는 한국어 음성 인식 모델을 찾고 있어. 1B 이하인 것 중 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["automatic-speech-recognition"]` ← 음성 인식
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=1.0` ← 1B 이하

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 LibriSpeech 결과가 있다
- **2점** LibriSpeech WER 등이 수치로 기록돼 있다
- **1점** LibriSpeech를 언급하나 수치가 없거나, 인접 음성 데이터셋만 있다

후보 56개 전수 스캔 → 🚩 5 / ⚠️ 8 / ✅ 43

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
| `handy-computer/Fun-ASR-MLT-Nano-2512-gguf` | 믿을 수 있는 단계엔 없고 출처 불명확 benchmark 결과에만 librispeech |  |
| `handy-computer/Qwen3-ASR-0.6B-gguf` | 믿을 수 있는 단계엔 없고 출처 불명확 benchmark 결과에만 librispeech |  |
| `handy-computer/SenseVoiceSmall-gguf` | 믿을 수 있는 단계엔 없고 출처 불명확 benchmark 결과에만 librispeech |  |
| `handy-computer/whisper-base-gguf` | 믿을 수 있는 단계엔 없고 출처 불명확 benchmark 결과에만 librispeech |  |
| `handy-computer/whisper-large-v3-turbo-gguf` | 믿을 수 있는 단계엔 없고 출처 불명확 benchmark 결과에만 librispeech |  |
| `handy-computer/whisper-medium-gguf` | 믿을 수 있는 단계엔 없고 출처 불명확 benchmark 결과에만 librispeech |  |
| `handy-computer/whisper-small-gguf` | 믿을 수 있는 단계엔 없고 출처 불명확 benchmark 결과에만 librispeech |  |
| `handy-computer/whisper-tiny-gguf` | 믿을 수 있는 단계엔 없고 출처 불명확 benchmark 결과에만 librispeech |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 43개 — `42MARU/ko-spelling-wav2vec2-conformer-del-1s`, `Aliados/nemotron-3.5-asr-streaming-0.6b`, `Edge0/Audio8-ASR-0.1B`, `FunAudioLLM/SenseVoiceSmall-GGUF-audiocpp`, `HeartMuLa/HeartTranscriptor-oss`, `Kkonjeong/wav2vec2-base-korean` …


### `bl05` ≤1.0B · core만 · automatic-speech-recognition · hard

> FLEURS 점수가 공개된 한국어 음성 인식 모델 있어? 1B 이하인 것 중 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["automatic-speech-recognition"]` ← 음성 인식
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=1.0` ← 1B 이하

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 FLEURS 결과가 있다
- **2점** FLEURS 점수가 수치로 기록돼 있다
- **1점** FLEURS를 언급하나 수치가 없거나, 인접 다국어 음성 벤치마크만 있다

후보 56개 전수 스캔 → 🚩 1 / ⚠️ 3 / ✅ 52

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `seastar105/whisper-medium-komixv2` | 2점 | benchmark_metadata에서 fleurs |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Qwen/Qwen3-ASR-0.6B-hf` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 voxpopuli |  |
| `handy-computer/moonshine-base-ko-gguf` | 믿을 수 있는 단계엔 없고 출처 불명확 benchmark 결과에만 fleurs |  |
| `handy-computer/nemotron-3.5-asr-streaming-0.6b-gguf` | 믿을 수 있는 단계엔 없고 출처 불명확 benchmark 결과에만 fleurs |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 52개 — `42MARU/ko-spelling-wav2vec2-conformer-del-1s`, `Aliados/nemotron-3.5-asr-streaming-0.6b`, `Edge0/Audio8-ASR-0.1B`, `FunAudioLLM/SenseVoiceSmall-GGUF-audiocpp`, `HeartMuLa/HeartTranscriptor-oss`, `Kkonjeong/wav2vec2-base-korean` …


### `bl06` ≤1.0B · core만 · automatic-speech-recognition · hard

> Common Voice 평가 결과가 있는 한국어 음성 인식 모델을 추천해줘. 1B 이하인 것 중 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["automatic-speech-recognition"]` ← 음성 인식
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=1.0` ← 1B 이하

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 Common Voice 결과가 있다
- **2점** Common Voice 점수가 수치로 기록돼 있다
- **1점** Common Voice를 언급하나 수치가 없거나 인접 벤치마크만 있다

후보 56개 전수 스캔 → 🚩 5 / ⚠️ 1 / ✅ 50

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `openai/whisper-base` | 2점 | benchmark_metadata에서 common voice |  |
| `openai/whisper-medium` | 2점 | benchmark_metadata에서 common voice |  |
| `openai/whisper-small` | 2점 | benchmark_metadata에서 common voice |  |
| `openai/whisper-tiny` | 2점 | benchmark_metadata에서 common voice |  |
| `unsloth/whisper-small` | 2점 | benchmark_metadata에서 common voice |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Qwen/Qwen3-ASR-0.6B-hf` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 voxpopuli |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 50개 — `42MARU/ko-spelling-wav2vec2-conformer-del-1s`, `Aliados/nemotron-3.5-asr-streaming-0.6b`, `Edge0/Audio8-ASR-0.1B`, `FunAudioLLM/SenseVoiceSmall-GGUF-audiocpp`, `HeartMuLa/HeartTranscriptor-oss`, `Kkonjeong/wav2vec2-base-korean` …


### `bl07` ≤4.0B · core만 · text-generation · hard

> MMLU 점수가 공개된 한국어 LLM 중에 4B 이하인 걸 찾아줘. 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["text-generation"]` ← LLM → text-generation
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=4.0` ← 4B 이하

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 원본 MMLU 결과가 있다
- **2점** 현재 모델에 귀속되는 원본 MMLU 점수가 수치로 기록돼 있다
- **1점** MMLU-Pro·KMMLU·MMMLU 등 변형만 있는 모델은 정답으로 넣지 않고, 원본 MMLU라도 변환본·재업로드 여부는 사람 검수 후 1점으로 낮춘다

후보 270개 전수 스캔 → 🚩 2 / ⚠️ 8 / ✅ 260

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `KridgeDookie/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS` | 2점 | benchmark_metadata에서 mmlu |  |
| `swartbwoy/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS` | 2점 | benchmark_metadata에서 mmlu |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `0xzknw/LFM2.5-2.6B-Heretic-NX-PRIME` | 믿을 수 있는 단계엔 없고 README 원문에만 hellaswag |  |
| `EleutherAI/polyglot-ko-1.3b` | 믿을 수 있는 단계엔 없고 README 원문에만 hellaswag |  |
| `EleutherAI/polyglot-ko-3.8b` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 hellaswag |  |
| `LiquidAI/LFM2-1.2B` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmmlu |  |
| `LiquidAI/LFM2-2.6B` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmmlu |  |
| `LiquidAI/LFM2-350M` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmmlu |  |
| `LiquidAI/LFM2-700M` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 mmmlu |  |
| `richardyoung/Phi-4-mini-instruct-heretic` | 믿을 수 있는 단계엔 없고 출처 불명확 benchmark 결과에만 mmlu, mmlu-pro, multilingual mmlu, hellaswag |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 260개 — `0xzknw/LFM2.5-1.2B-Thinking-Heretic`, `42dot/42dot_LLM-PLM-1.3B`, `42dot/42dot_LLM-SFT-1.3B`, `AMAImedia/Tiny-Aya-3.3B-L2-Thinker-BF16-GGUF`, `AtomicChat/LFM3-1.7B-GGUF`, `Bllossom/llama-3.2-Korean-Bllossom-3B` …


### `bl08` ≤4.0B · core만 · text-generation · hard

> 도구 호출 성능을 비교하려고 해. BFCL v3 점수를 공개한 한국어 LLM이 있을까? 4B 이하인 것 중 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["text-generation"]` ← LLM → text-generation
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=4.0` ← 4B 이하

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 BFCL v3 결과가 있다
- **2점** 현재 모델에 귀속되는 BFCL v3 점수가 수치로 기록돼 있다
- **1점** 도구 호출을 언급하나 BFCL v3 점수가 없거나 출처가 불명확하다

후보 270개 전수 스캔 → 🚩 3 / ⚠️ 4 / ✅ 263

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `LiquidAI/LFM2.5-1.2B-Instruct` | 2점 | benchmark_metadata에서 bfclv3 |  |
| `richardyoung/LFM2.5-1.2B-Instruct-heretic` | 2점 | benchmark_metadata에서 bfclv3 |  |
| `unsloth/LFM2.5-1.2B-Instruct` | 2점 | benchmark_metadata에서 bfclv3 |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `kakaocorp/kanana-1.5-2.1b-instruct-2505` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 function calling |  |
| `kakaocorp/kanana-nano-2.1b-embedding` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 function calling |  |
| `kakaocorp/kanana-nano-2.1b-instruct` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 function calling |  |
| `saidutta69/granite-4.1-3b-heretic` | 믿을 수 있는 단계엔 없고 출처 불명확 benchmark 결과에만 tool calling |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 263개 — `0xzknw/LFM2.5-1.2B-Thinking-Heretic`, `0xzknw/LFM2.5-2.6B-Heretic-NX-PRIME`, `42dot/42dot_LLM-PLM-1.3B`, `42dot/42dot_LLM-SFT-1.3B`, `AMAImedia/Tiny-Aya-3.3B-L2-Thinker-BF16-GGUF`, `AtomicChat/LFM3-1.7B-GGUF` …


### `bl09` 조건 없음 · text-classification · hard

> KLUE 평가 결과가 README에 있는 한국어 텍스트 분류 모델을 찾고 있어.

조건 → 질의문 근거

- `tasks=["text-classification"]` ← 텍스트 분류
- `korean_required=true` ← 한국어

판정 규칙 (판정 전에 고정)

- **must** benchmark_metadata.results에 KLUE 결과가 있다
- **2점** KLUE 점수가 수치로 기록돼 있다
- **1점** KLUE를 언급하나 수치가 없거나, KorSTS·KorNLI 등 인접 한국어 벤치마크만 있다

후보 105개 전수 스캔 → 🚩 1 / ⚠️ 0 / ✅ 104

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `skt/A.X-Encoder-base` | 2점 | benchmark_metadata에서 klue |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 98개 — `BalaRajesh1/mmbert-small-nli`, `Copycats/koelectra-base-v3-generalized-sentiment-analysis`, `DataWizardd/finbert-sentiment-ko`, `Dongjin-kr/ko-reranker`, `FISA-conclave/klue-roberta-news-sentiment`, `Genius1237/xlm-roberta-large-tydip` …
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
- **1점** 일반 STSBenchmark/STSB만 있는 모델은 한국어 STS 정답으로 넣지 않고, 한국어 STS 언급이지만 수치·출처가 불명확한 경우만 사람 검수 후 1점으로 둔다

후보 71개 전수 스캔 → 🚩 1 / ⚠️ 23 / ✅ 47

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `SamilPwC-AXNode-GenAI/PwC-Embedding_expr` | 2점 | benchmark_metadata에서 klue-sts, korsts |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Alibaba-NLP/gte-multilingual-base` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 stsb, stsbenchmark, sts |  |
| `BidirLM/BidirLM-0.6B-Embedding` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `BidirLM/BidirLM-1B-Embedding` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `Hiveurban/multilingual-e5-base` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 stsb, stsbenchmark, sts |  |
| `LiquidAI/LFM2.5-ColBERT-350M-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `LiquidAI/LFM2.5-Embedding-350M-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `RedHatAI/snowflake-arctic-embed-l-v2.0` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 stsb, stsbenchmark, sts |  |
| `Snowflake/snowflake-arctic-embed-l-v2.0` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 stsb, stsbenchmark, sts |  |
| `Snowflake/snowflake-arctic-embed-m-v2.0` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 stsb, stsbenchmark, sts |  |
| `beademiguelperez/sentence-transformers-multilingual-e5-small` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 stsb, stsbenchmark, sts |  |
| `bespin-global/klue-sroberta-base-continue-learning-by-mnr` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 stsb, stsbenchmark, sts |  |
| `dnotitia/DNA-VL-STEER-2B` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `dragonkue/BGE-m3-ko` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `dragonkue/snowflake-arctic-embed-l-v2.0-ko` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `intfloat/multilingual-e5-base` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 stsb, stsbenchmark, sts |  |
| `jhgan/ko-sbert-multitask` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `jhgan/ko-sbert-nli` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `jhgan/ko-sbert-sts` | 믿을 수 있는 단계엔 없고 model_id에만 sts |  |
| `jhgan/ko-sroberta-multitask` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |
| `snunlp/KR-SBERT-Medium-extended-klueNLItriplet_PARpair_QApair-klueSTS` | 믿을 수 있는 단계엔 없고 model_id에만 sts |  |
| `snunlp/KR-SBERT-V40K-klueNLI-augSTS` | 믿을 수 있는 단계엔 없고 model_id에만 sts |  |
| `upskyy/bge-m3-korean` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 sts |  |
| `upskyy/kf-deberta-multitask` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 sts |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 47개 — `BidirLM/BidirLM-Omni-2.5B-Embedding`, `Casual-Autopsy/snowflake-arctic-embed-l-v2.0-gguf`, `ChristianAzinn/labse-gguf`, `LiquidAI/LFM2-ColBERT-350M`, `LiquidAI/LFM2.5-ColBERT-350M`, `LiquidAI/LFM2.5-Embedding-350M` …


