# model_comparison 판정 워크시트

**숫자 검증은 명령 한 줄이 전부 합니다.**

```bash
cd ai && ../.venv/bin/python test/golden/v2/tools/verify.py model_comparison
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

코퍼스 3872행 · 2026-10-31 기준 · 질의 10개 · 사람이 볼 것 **76개**

---

### `mc01` 조건 없음 · summarization · easy

> KoBART랑 KoT5 중에 한국어 요약에 뭐가 더 나아?

조건 → 질의문 근거

- `tasks=["summarization"]` ← 요약
- `korean_required=true` ← 한국어

판정 규칙 (판정 전에 고정)

- **must** model_id가 KoBART 또는 KoT5 계열이다
- **2점** 그 계열이고 요약 용도가 확인된다
- **1점** 같은 계열이나 다른 task용이거나 변환본·재업로드
- **비교 완결성** KoBART / KoT5 계열이 최종 정답에 각각 하나 이상 있어야 한다

후보 14개 전수 스캔 → 🚩 3 / ⚠️ 0 / ✅ 11

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 비교 대상 | 모델 | 제안 | 근거 | 확정 |
|---|---|:--:|---|:--:|
| KoBART | `EbanLee/kobart-summary-v3` | 2점 | model_id, canonical_model_id에서 KoBART |  |
| KoBART | `ainize/kobart-news` | 2점 | model_id, canonical_model_id에서 KoBART |  |
| KoT5 | `psyche/KoT5-summarization` | 2점 | model_id, canonical_model_id에서 KoT5 |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 11개 — `QyrouNnet-AI/QNS-2-ReLearn-Preview`, `csebuetnlp/mT5_m2m_crossSum`, `csebuetnlp/mT5_m2m_crossSum_enhanced`, `csebuetnlp/mT5_m2o_english_crossSum`, `csebuetnlp/mT5_multilingual_XLSum`, `data-silence/any-news-sum` …


### `mc02` core만 · feature-extraction · easy

> KoBERT와 KoSimCSE 중 한국어 문장 임베딩·검색에는 어떤 계열이 더 맞아? 많이 쓰이는 모델로.

조건 → 질의문 근거

- `tasks=["feature-extraction"]` ← 문장 임베딩·검색 → feature-extraction
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)

판정 규칙 (판정 전에 고정)

- **must** model_id가 KoBERT 또는 KoSimCSE 계열이다
- **2점** KoSimCSE 계열로, 임베딩·검색 용도가 직접 확인된다
- **1점** KoBERT 원본처럼 임베딩·검색 용도가 불명확하거나 변환본·재업로드
- **비교 완결성** KoBERT / KoSimCSE 계열이 최종 정답에 각각 하나 이상 있어야 한다

후보 64개 전수 스캔 → 🚩 5 / ⚠️ 0 / ✅ 59

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 비교 대상 | 모델 | 제안 | 근거 | 확정 |
|---|---|:--:|---|:--:|
| KoSimCSE | `BM-K/KoSimCSE-bert-multitask` | 2점 | model_id, canonical_model_id에서 KoSimCSE |  |
| KoSimCSE | `BM-K/KoSimCSE-roberta` | 2점 | model_id, canonical_model_id에서 KoSimCSE |  |
| KoSimCSE | `BM-K/KoSimCSE-roberta-multitask` | 2점 | model_id, canonical_model_id에서 KoSimCSE |  |
| KoBERT | `monologg/kobert` | 1점 | 한국어 사전학습 BERT; 문장 임베딩·검색 특화 근거는 없음 | 기록됨 |
| KoBERT | `skt/kobert-base-v1` | 1점 | 한국어 사전학습 BERT; 문장 임베딩·검색 특화 근거는 없음 | 기록됨 |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 57개 — `CISCai/jina-embeddings-v3-separation-distilled`, `ZurichNLP/unsup-simcse-xlm-roberta-base`, `amazon/Titan-text-embeddings-v2`, `codefuse-ai/F2LLM-v2-0.6B`, `codefuse-ai/F2LLM-v2-1.7B`, `codefuse-ai/F2LLM-v2-14B` …
- **주 task가 sentence-similarity** 2개 — `omai-research/milco-300m`, `omai-research/milco-650m`


### `mc03` core만 · sentence-similarity · easy

> ko-sroberta와 KoSBERT 중 한국어 문장 유사도에는 어느 쪽이 더 맞아? 많이 쓰이는 모델로.

조건 → 질의문 근거

- `tasks=["sentence-similarity"]` ← 문장 유사도
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core

판정 규칙 (판정 전에 고정)

- **must** model_id가 ko-sroberta 또는 KoSBERT 계열이다
- **2점** 한국어 전용(ko- 접두) 계열이다
- **1점** 다국어 계열이거나 변환본
- **비교 완결성** ko-sroberta / KoSBERT 계열이 최종 정답에 각각 하나 이상 있어야 한다

후보 71개 전수 스캔 → 🚩 4 / ⚠️ 0 / ✅ 67

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 비교 대상 | 모델 | 제안 | 근거 | 확정 |
|---|---|:--:|---|:--:|
| KoSBERT | `jhgan/ko-sbert-multitask` | 2점 | model_id, canonical_model_id에서 KoSBERT |  |
| KoSBERT | `jhgan/ko-sbert-nli` | 2점 | model_id, canonical_model_id에서 KoSBERT |  |
| KoSBERT | `jhgan/ko-sbert-sts` | 2점 | model_id, canonical_model_id에서 KoSBERT |  |
| ko-sroberta | `jhgan/ko-sroberta-multitask` | 2점 | model_id, canonical_model_id에서 ko-sroberta |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 67개 — `Alibaba-NLP/gte-multilingual-base`, `BidirLM/BidirLM-0.6B-Embedding`, `BidirLM/BidirLM-1B-Embedding`, `BidirLM/BidirLM-Omni-2.5B-Embedding`, `Casual-Autopsy/snowflake-arctic-embed-l-v2.0-gguf`, `ChristianAzinn/labse-gguf` …


### `mc04` core만 · feature-extraction · easy

> BGE랑 multilingual-E5 중에 한국어 임베딩에 뭐가 나아? 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["feature-extraction"]` ← 임베딩 → feature-extraction
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)

판정 규칙 (판정 전에 고정)

- **must** model_id가 BGE 또는 E5 계열이다
- **2점** BGE-M3 또는 multilingual-E5 본체다
- **1점** 같은 계열의 파인튜닝·변환본이거나 단일 언어 변형
- **비교 완결성** BGE-M3 / multilingual-E5 계열이 최종 정답에 각각 하나 이상 있어야 한다

후보 64개 전수 스캔 → 🚩 7 / ⚠️ 0 / ✅ 57

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 비교 대상 | 모델 | 제안 | 근거 | 확정 |
|---|---|:--:|---|:--:|
| multilingual-E5 | `intfloat/multilingual-e5-large` | 2점 | model_id, canonical_model_id에서 multilingual-E5 |  |
| multilingual-E5 | `intfloat/multilingual-e5-large-instruct` | 2점 | model_id, canonical_model_id에서 multilingual-E5 |  |
| multilingual-E5 | `cstr/multilingual-e5-small-GGUF` | 1점 | model_id, canonical_model_id에서 multilingual-E5 / variant로 표시됨 |  |
| BGE-M3 | `mlx-community/bge-m3-mlx-4bit` | 1점 | model_id, canonical_model_id에서 BGE-M3 / variant로 표시됨 |  |
| BGE-M3 | `mlx-community/bge-m3-mlx-8bit` | 1점 | model_id, canonical_model_id에서 BGE-M3 / variant로 표시됨 |  |
| BGE-M3 | `mlx-community/bge-m3-mlx-fp16` | 1점 | model_id, canonical_model_id에서 BGE-M3 / variant로 표시됨 |  |
| multilingual-E5 | `nlpai-lab/KoE5` | 1점 | canonical_model_id에서 multilingual-E5 / variant로 표시됨 |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 55개 — `BM-K/KoSimCSE-bert-multitask`, `BM-K/KoSimCSE-roberta`, `BM-K/KoSimCSE-roberta-multitask`, `CISCai/jina-embeddings-v3-separation-distilled`, `ZurichNLP/unsup-simcse-xlm-roberta-base`, `amazon/Titan-text-embeddings-v2` …
- **주 task가 sentence-similarity** 2개 — `omai-research/milco-300m`, `omai-research/milco-650m`


### `mc05` core만 · feature-extraction · easy

> KURE와 BGE-M3를 한국어 검색에 쓰면 어느 쪽이 좋아? 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["feature-extraction"]` ← 검색용 임베딩 → feature-extraction
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core

판정 규칙 (판정 전에 고정)

- **must** model_id가 KURE 또는 BGE-M3 계열이다
- **2점** 그 계열의 본체다
- **1점** 같은 계열의 파인튜닝·변환본이거나 양자화본
- **비교 완결성** KURE / BGE-M3 계열이 최종 정답에 각각 하나 이상 있어야 한다

후보 64개 전수 스캔 → 🚩 4 / ⚠️ 0 / ✅ 60

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 비교 대상 | 모델 | 제안 | 근거 | 확정 |
|---|---|:--:|---|:--:|
| BGE-M3 | `mlx-community/bge-m3-mlx-4bit` | 1점 | model_id, canonical_model_id에서 BGE-M3 / variant로 표시됨 |  |
| BGE-M3 | `mlx-community/bge-m3-mlx-8bit` | 1점 | model_id, canonical_model_id에서 BGE-M3 / variant로 표시됨 |  |
| BGE-M3 | `mlx-community/bge-m3-mlx-fp16` | 1점 | model_id, canonical_model_id에서 BGE-M3 / variant로 표시됨 |  |
| KURE | `mykor/KURE-v1-gguf` | 1점 | model_id, canonical_model_id에서 KURE / variant로 표시됨 |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 58개 — `BM-K/KoSimCSE-bert-multitask`, `BM-K/KoSimCSE-roberta`, `BM-K/KoSimCSE-roberta-multitask`, `CISCai/jina-embeddings-v3-separation-distilled`, `ZurichNLP/unsup-simcse-xlm-roberta-base`, `amazon/Titan-text-embeddings-v2` …
- **주 task가 sentence-similarity** 2개 — `omai-research/milco-300m`, `omai-research/milco-650m`


### `mc06` core만 · text-generation · easy

> KoGPT랑 Polyglot-Ko 비교해줘. 많이 쓰이는 한국어 생성 모델로.

조건 → 질의문 근거

- `tasks=["text-generation"]` ← 생성 → text-generation
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core

판정 규칙 (판정 전에 고정)

- **must** model_id가 KoGPT 또는 Polyglot 계열이다
- **2점** 한국어 전용 계열(KoGPT, Polyglot-Ko)이다
- **1점** 다국어 Polyglot이거나 파인튜닝·변환본
- **비교 완결성** KoGPT / Polyglot-Ko 계열이 최종 정답에 각각 하나 이상 있어야 한다

후보 926개 전수 스캔 → 🚩 6 / ⚠️ 0 / ✅ 920

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 비교 대상 | 모델 | 제안 | 근거 | 확정 |
|---|---|:--:|---|:--:|
| Polyglot-Ko | `EleutherAI/polyglot-ko-1.3b` | 2점 | model_id, canonical_model_id에서 Polyglot-Ko |  |
| Polyglot-Ko | `EleutherAI/polyglot-ko-12.8b` | 2점 | model_id, canonical_model_id에서 Polyglot-Ko |  |
| Polyglot-Ko | `EleutherAI/polyglot-ko-3.8b` | 2점 | model_id, canonical_model_id에서 Polyglot-Ko |  |
| Polyglot-Ko | `EleutherAI/polyglot-ko-5.8b` | 2점 | model_id, canonical_model_id에서 Polyglot-Ko |  |
| KoGPT | `psyche/kogpt` | 2점 | model_id, canonical_model_id에서 KoGPT |  |
| KoGPT | `skt/kogpt2-base-v2` | 2점 | model_id, canonical_model_id에서 KoGPT |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 920개 — `0ppxnhximxr/Motif-3-FP8`, `0xWhiteMage/Qwen3.8-27B-Kearuga`, `0xzknw/LFM2.5-1.2B-Thinking-Heretic`, `0xzknw/LFM2.5-2.6B-Heretic-NX-PRIME`, `42dot/42dot_LLM-PLM-1.3B`, `42dot/42dot_LLM-SFT-1.3B` …


### `mc07` core만 · translation · easy

> NLLB와 mBART 중에 한국어 번역에 뭐가 나아? 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["translation"]` ← 번역
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core

판정 규칙 (판정 전에 고정)

- **must** model_id가 NLLB 또는 mBART 계열이다
- **2점** 그 계열의 본체다
- **1점** 같은 계열의 파인튜닝·증류·변환본
- **비교 완결성** NLLB / mBART 계열이 최종 정답에 각각 하나 이상 있어야 한다

후보 117개 전수 스캔 → 🚩 18 / ⚠️ 0 / ✅ 99

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 비교 대상 | 모델 | 제안 | 근거 | 확정 |
|---|---|:--:|---|:--:|
| mBART | `facebook/mbart-large-50-many-to-many-mmt` | 2점 | model_id, canonical_model_id에서 mBART |  |
| mBART | `facebook/mbart-large-cc25` | 2점 | model_id, canonical_model_id에서 mBART |  |
| NLLB | `facebook/nllb-200-1.3B` | 2점 | model_id, canonical_model_id에서 NLLB |  |
| NLLB | `facebook/nllb-200-3.3B` | 2점 | model_id, canonical_model_id에서 NLLB |  |
| NLLB | `facebook/nllb-moe-54b` | 2점 | model_id, canonical_model_id에서 NLLB |  |
| NLLB | `JustFrederik/nllb-200-distilled-1.3B-ct2-int8` | 1점 | model_id, canonical_model_id에서 NLLB / model_id에 변환·양자화 표지 있음 |  |
| NLLB | `JustFrederik/nllb-200-distilled-600M-ct2-int8` | 1점 | model_id, canonical_model_id에서 NLLB / model_id에 변환·양자화 표지 있음 |  |
| NLLB | `LifeAi-dev/nllb-200-3.3B-ct2-int8` | 1점 | model_id, canonical_model_id에서 NLLB / model_id에 변환·양자화 표지 있음 |  |
| NLLB | `NHNDQ/nllb-finetuned-en2ko` | 1점 | model_id, canonical_model_id에서 NLLB / model_id에 변환·양자화 표지 있음 |  |
| NLLB | `OpenNMT/nllb-200-3.3B-ct2-int8` | 1점 | model_id, canonical_model_id에서 NLLB / model_id에 변환·양자화 표지 있음 |  |
| NLLB | `OpenNMT/nllb-200-distilled-1.3B-ct2-int8` | 1점 | model_id, canonical_model_id에서 NLLB / model_id에 변환·양자화 표지 있음 |  |
| NLLB | `Serkan007/CTranslate2-nllb-200-int8` | 1점 | model_id, canonical_model_id에서 NLLB / model_id에 변환·양자화 표지 있음 |  |
| NLLB | `Xenova/nllb-200-distilled-600M` | 1점 | model_id, canonical_model_id에서 NLLB / variant로 표시됨 |  |
| NLLB | `entai2965/nllb-200-distilled-600M-ctranslate2` | 1점 | model_id, canonical_model_id에서 NLLB / variant로 표시됨 |  |
| NLLB | `facebook/nllb-200-distilled-1.3B` | 1점 | model_id, canonical_model_id에서 NLLB / model_id에 변환·양자화 표지 있음 |  |
| NLLB | `facebook/nllb-200-distilled-600M` | 1점 | model_id, canonical_model_id에서 NLLB / model_id에 변환·양자화 표지 있음 |  |
| NLLB | `mijuanlo/nllb-200-distilled-600M-ct2-int8` | 1점 | model_id, canonical_model_id에서 NLLB / model_id에 변환·양자화 표지 있음 |  |
| NLLB | `raxtemur/SONAR_200_text_decoder` | 1점 | canonical_model_id에서 NLLB / variant로 표시됨 |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 99개 — `42ailab/TranslateGemma-27B-GGUF`, `42ailab/TranslateGemma-4B-GGUF`, `BSC-LT/salamandraTA-7B-instruct-GGUF`, `BSC-LT/salamandraTA-7b-instruct`, `Babelscape/mrebel-large`, `ByteDance-Seed/Seed-X-Instruct-7B` …


### `mc08` ≤1.0B · core만 · automatic-speech-recognition · easy

> Whisper small과 wav2vec 중에 한국어 음성 인식에 뭐가 좋아? 1B 이하인 것 중 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["automatic-speech-recognition"]` ← 음성 인식
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=1.0` ← 1B 이하

판정 규칙 (판정 전에 고정)

- **must** model_id가 Whisper small 또는 wav2vec 계열이다
- **2점** 그 계열이고 한국어 파인튜닝이 확인된다
- **1점** 다른 크기의 Whisper이거나 변환본·양자화본
- **비교 완결성** Whisper small / wav2vec 계열이 최종 정답에 각각 하나 이상 있어야 한다

후보 56개 전수 스캔 → 🚩 8 / ⚠️ 0 / ✅ 48

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 비교 대상 | 모델 | 제안 | 근거 | 확정 |
|---|---|:--:|---|:--:|
| wav2vec | `42MARU/ko-spelling-wav2vec2-conformer-del-1s` | 2점 | model_id, canonical_model_id에서 wav2vec |  |
| wav2vec | `Kkonjeong/wav2vec2-base-korean` | 2점 | model_id, canonical_model_id에서 wav2vec |  |
| wav2vec | `kresnik/wav2vec2-large-xlsr-korean` | 2점 | model_id, canonical_model_id에서 wav2vec |  |
| Whisper small | `openai/whisper-small` | 2점 | model_id, canonical_model_id에서 Whisper small |  |
| wav2vec | `slplab/wav2vec2-xls-r-300m_phone-mfa_korean` | 2점 | model_id, canonical_model_id에서 wav2vec |  |
| wav2vec | `w11wo/wav2vec2-xls-r-300m-korean` | 2점 | model_id, canonical_model_id에서 wav2vec |  |
| Whisper small | `handy-computer/whisper-small-gguf` | 1점 | model_id, canonical_model_id에서 Whisper small / variant로 표시됨 |  |
| Whisper small | `unsloth/whisper-small` | 1점 | model_id, canonical_model_id에서 Whisper small / variant로 표시됨 |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 48개 — `Aliados/nemotron-3.5-asr-streaming-0.6b`, `Edge0/Audio8-ASR-0.1B`, `FunAudioLLM/SenseVoiceSmall-GGUF-audiocpp`, `HeartMuLa/HeartTranscriptor-oss`, `MahmoudAshraf/mms-300m-1130-forced-aligner`, `OpenVoiceOS/qwen3-asr-0.6b-f16` …


### `mc09` 조건 없음 · translation · easy

> opus-mt와 M2M100 중에 한국어가 포함된 다국어 번역에는 어떤 모델이 더 맞아?

조건 → 질의문 근거

- `tasks=["translation"]` ← 한국어가 포함된 다국어 번역 → translation
- `korean_required=true` ← 한국어

판정 규칙 (판정 전에 고정)

- **must** model_id가 opus-mt 또는 M2M100 계열이다
- **2점** 그 계열의 본체이고 한국어 방향이 확인된다
- **1점** 같은 계열이나 한국어 방향이 불명확하거나 변환본
- **비교 완결성** opus-mt / M2M100 계열이 최종 정답에 각각 하나 이상 있어야 한다

후보 245개 전수 스캔 → 🚩 18 / ⚠️ 0 / ✅ 227

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 비교 대상 | 모델 | 제안 | 근거 | 확정 |
|---|---|:--:|---|:--:|
| opus-mt | `Helsinki-NLP/opus-mt-ko-de` | 2점 | model_id, canonical_model_id에서 opus-mt |  |
| opus-mt | `Helsinki-NLP/opus-mt-ko-en` | 2점 | model_id, canonical_model_id에서 opus-mt |  |
| opus-mt | `Helsinki-NLP/opus-mt-ko-es` | 2점 | model_id, canonical_model_id에서 opus-mt |  |
| opus-mt | `Helsinki-NLP/opus-mt-ko-fr` | 2점 | model_id, canonical_model_id에서 opus-mt |  |
| opus-mt | `Helsinki-NLP/opus-mt-ko-ru` | 2점 | model_id, canonical_model_id에서 opus-mt |  |
| opus-mt | `Helsinki-NLP/opus-mt-tc-big-en-ko` | 2점 | model_id, canonical_model_id에서 opus-mt |  |
| opus-mt | `Helsinki-NLP/opus-mt-tc-big-ko-en` | 2점 | model_id, canonical_model_id에서 opus-mt |  |
| opus-mt | `Helsinki-NLP/opus-mt_tiny_kor-eng` | 2점 | model_id, canonical_model_id에서 opus-mt |  |
| opus-mt | `jhk/opus-mt-tc-big-wiki-en-ko` | 2점 | model_id, canonical_model_id에서 opus-mt |  |
| opus-mt | `shun89/opus-mt-ko-zh` | 2점 | model_id, canonical_model_id에서 opus-mt |  |
| opus-mt | `R4kSo1997/opus-mt-en-ko-onnx-int8` | 1점 | model_id, canonical_model_id에서 opus-mt / model_id에 변환·양자화 표지 있음 |  |
| M2M100 | `Rohith04/ct2fast_m2m100_418M` | 1점 | model_id, canonical_model_id에서 M2M100 / model_id에 변환·양자화 표지 있음 |  |
| opus-mt | `Xenova/opus-mt-ko-en` | 1점 | model_id, canonical_model_id에서 opus-mt / variant로 표시됨 |  |
| M2M100 | `entai2965/m2m100-1.2B-ctranslate2` | 1점 | model_id, canonical_model_id에서 M2M100 / variant로 표시됨 |  |
| M2M100 | `entai2965/m2m100-418M-ctranslate2` | 1점 | model_id, canonical_model_id에서 M2M100 / variant로 표시됨 |  |
| M2M100 | `huggingworld/m2m100_418M` | 1점 | model_id, canonical_model_id에서 M2M100 / variant로 표시됨 |  |
| opus-mt | `noticemkjung/opus-mt-tc-big-en-ko-ONNX` | 1점 | model_id, canonical_model_id에서 opus-mt / variant로 표시됨 |  |
| opus-mt | `ooeoeo/opus-mt-tc-big-en-ko-ct2-float16` | 1점 | model_id, canonical_model_id에서 opus-mt / model_id에 변환·양자화 표지 있음 |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 227개 — `0xSojalSec/Tencent-Hy-30B-A3B-uncensored-heretic`, `42ailab/TranslateGemma-12B-GGUF`, `42ailab/TranslateGemma-27B-GGUF`, `42ailab/TranslateGemma-4B-GGUF`, `BSC-LT/salamandraTA-7B-instruct-GGUF`, `BSC-LT/salamandraTA-7b-instruct` …


### `mc10` 조건 없음 · question-answering · easy

> KoELECTRA와 mDeBERTa 중에 한국어 질의응답에 뭐가 나아?

조건 → 질의문 근거

- `tasks=["question-answering"]` ← 질의응답
- `korean_required=true` ← 한국어

판정 규칙 (판정 전에 고정)

- **must** model_id가 KoELECTRA 또는 mDeBERTa 계열이다
- **2점** 한국어 전용 계열(KoELECTRA)이고 질의응답 용도가 확인된다
- **1점** 다국어 계열(mDeBERTa)이거나 다른 task용 파인튜닝
- **비교 완결성** KoELECTRA / mDeBERTa 계열이 최종 정답에 각각 하나 이상 있어야 한다

후보 21개 전수 스캔 → 🚩 3 / ⚠️ 0 / ✅ 18

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 비교 대상 | 모델 | 제안 | 근거 | 확정 |
|---|---|:--:|---|:--:|
| KoELECTRA | `monologg/koelectra-base-v3-finetuned-korquad` | 1점 | model_id, canonical_model_id에서 KoELECTRA / model_id에 변환·양자화 표지 있음 |  |
| KoELECTRA | `monologg/koelectra-small-v2-distilled-korquad-384` | 1점 | model_id, canonical_model_id에서 KoELECTRA / model_id에 변환·양자화 표지 있음 |  |
| mDeBERTa | `timpal0l/mdeberta-v3-base-squad2` | 1점 | model_id, canonical_model_id에서 mDeBERTa / variant로 표시됨 |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 18개 — `FreedomIntelligence/Apollo-MoE-0.5B`, `FreedomIntelligence/Apollo-MoE-7B`, `FreedomIntelligence/Apollo2-3.8B`, `FreedomIntelligence/Apollo2-7B`, `FreedomIntelligence/Apollo2-9B`, `QuantFactory/Apollo2-2B-GGUF` …

