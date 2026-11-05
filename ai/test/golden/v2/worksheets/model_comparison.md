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

코퍼스 3872행 · 2026-10-31 기준 · 질의 10개 · 사람이 볼 것 **120개**

---

### `mc01` 조건 없음 · summarization · hard

> KoBART랑 KoT5 중에 한국어 요약에 뭐가 더 나아?

조건 → 질의문 근거

- `tasks=["summarization"]` ← 요약
- `korean_required=true` ← 한국어

판정 규칙 (판정 전에 고정)

- **must** model_id가 KoBART 또는 KoT5 계열이다
- **2점** 그 계열이고 요약 용도가 확인된다
- **1점** 같은 계열이나 다른 task용이거나 변환본·재업로드

후보 14개 전수 스캔 → 🚩 3 / ⚠️ 8 / ✅ 3

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `EbanLee/kobart-summary-v3` | 2점 | model_id에서 kobart |  |
| `ainize/kobart-news` | 2점 | model_id에서 kobart |  |
| `psyche/KoT5-summarization` | 2점 | model_id에서 kot5 |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `csebuetnlp/mT5_m2m_crossSum` | 믿을 수 있는 단계엔 없고 model_id에만 t5 |  |
| `csebuetnlp/mT5_m2m_crossSum_enhanced` | 믿을 수 있는 단계엔 없고 model_id에만 t5 |  |
| `csebuetnlp/mT5_m2o_english_crossSum` | 믿을 수 있는 단계엔 없고 model_id에만 t5 |  |
| `csebuetnlp/mT5_multilingual_XLSum` | 믿을 수 있는 단계엔 없고 model_id에만 t5 |  |
| `data-silence/any-news-sum` | 믿을 수 있는 단계엔 없고 filter_metadata에만 t5 |  |
| `eenzeenee/t5-base-korean-summarization` | 믿을 수 있는 단계엔 없고 model_id에만 t5 |  |
| `eenzeenee/t5-small-korean-summarization` | 믿을 수 있는 단계엔 없고 model_id에만 t5 |  |
| `mskayacioglu/mbart50-xlsum` | 믿을 수 있는 단계엔 없고 model_id에만 bart, t5 |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 3개 — `ncls-p/Qwen2.5-3B-blog-key-points`, `ncls-p/Qwen2.5-7B-blog-key-points`, `QyrouNnet-AI/QNS-2-ReLearn-Preview`


### `mc02` core만 · text-classification · easy

> KoELECTRA와 KoBERT를 한국어 텍스트 분류에 쓸 때 어느 쪽이 좋아? 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["text-classification"]` ← 텍스트 분류
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)

판정 규칙 (판정 전에 고정)

- **must** model_id가 KoELECTRA 또는 KoBERT 계열이다
- **2점** 그 계열이고 분류 용도가 확인된다
- **1점** 같은 계열이나 다른 task용이거나 경량화·변환본

후보 49개 전수 스캔 → 🚩 5 / ⚠️ 0 / ✅ 44

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `Copycats/koelectra-base-v3-generalized-sentiment-analysis` | 2점 | model_id에서 koelectra |  |
| `MelissaJ/koelectra-emotion-6-emotion-base` | 2점 | model_id에서 koelectra |  |
| `circulus/koelectra-polite-v1` | 2점 | model_id에서 koelectra |  |
| `circulus/koelectra-sentiment-v1` | 2점 | model_id에서 koelectra |  |
| `daekeun-ml/koelectra-small-v3-nsmc` | 2점 | model_id에서 koelectra |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 44개 — `agentlans/multilingual-e5-small-aligned-sentiment`, `amber-tech/bert-multilingual-passage-reranking-msmarco`, `amphora/KorFinASC-XLM-RoBERTa`, `autopilot-ai/EthicalEye`, `banjl4487/MODEL`, `chaoliangUNSW/Jev-Style-0.8B-Decision-v3` …


### `mc03` core만 · sentence-similarity · hard

> ko-sroberta랑 KoSimCSE 비교해줘. 많이 쓰이는 한국어 문장 유사도 모델로.

조건 → 질의문 근거

- `tasks=["sentence-similarity"]` ← 문장 유사도
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core

판정 규칙 (판정 전에 고정)

- **must** model_id가 sroberta 또는 SimCSE 계열이다
- **2점** 한국어 전용(ko- 접두) 계열이다
- **1점** 다국어 계열이거나 변환본

후보 71개 전수 스캔 → 🚩 2 / ⚠️ 3 / ✅ 66

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `jhgan/ko-sroberta-multitask` | 2점 | model_id에서 sroberta |  |
| `bespin-global/klue-sroberta-base-continue-learning-by-mnr` | 1점 | model_id에서 sroberta |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `jhgan/ko-sbert-multitask` | 믿을 수 있는 단계엔 없고 model_id에만 ko-sbert |  |
| `jhgan/ko-sbert-nli` | 믿을 수 있는 단계엔 없고 model_id에만 ko-sbert |  |
| `jhgan/ko-sbert-sts` | 믿을 수 있는 단계엔 없고 model_id에만 ko-sbert |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 66개 — `Alibaba-NLP/gte-multilingual-base`, `antoinelouis/colbert-xm`, `batiai/Qwen3-VL-Embedding-8B-GGUF`, `beademiguelperez/sentence-transformers-multilingual-e5-small`, `BidirLM/BidirLM-0.6B-Embedding`, `BidirLM/BidirLM-1B-Embedding` …


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

후보 64개 전수 스캔 → 🚩 9 / ⚠️ 1 / ✅ 54

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `omai-research/milco-300m` | 2점 | semantic_metadata에서 bge-m3 |  |
| `omai-research/milco-650m` | 2점 | semantic_metadata에서 bge-m3 |  |
| `nlpai-lab/KoE5` | 2점 | filter_metadata에서 multilingual-e5 |  |
| `cstr/multilingual-e5-small-GGUF` | 2점 | model_id에서 multilingual-e5 |  |
| `intfloat/multilingual-e5-large` | 2점 | model_id에서 multilingual-e5 |  |
| `intfloat/multilingual-e5-large-instruct` | 2점 | model_id에서 multilingual-e5 |  |
| `mlx-community/bge-m3-mlx-4bit` | 2점 | model_id에서 bge-m3 |  |
| `mlx-community/bge-m3-mlx-8bit` | 2점 | model_id에서 bge-m3 |  |
| `mlx-community/bge-m3-mlx-fp16` | 2점 | model_id에서 bge-m3 |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `telepix/PIXIE-Rune-v1.5` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 e5-large |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 54개 — `amazon/Titan-text-embeddings-v2`, `BM-K/KoSimCSE-bert-multitask`, `BM-K/KoSimCSE-roberta`, `BM-K/KoSimCSE-roberta-multitask`, `CISCai/jina-embeddings-v3-separation-distilled`, `codefuse-ai/F2LLM-v2-0.6B` …


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

후보 64개 전수 스캔 → 🚩 6 / ⚠️ 1 / ✅ 57

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `omai-research/milco-300m` | 2점 | semantic_metadata에서 bge-m3 |  |
| `omai-research/milco-650m` | 2점 | semantic_metadata에서 bge-m3 |  |
| `mlx-community/bge-m3-mlx-4bit` | 2점 | model_id에서 bge-m3 |  |
| `mlx-community/bge-m3-mlx-8bit` | 2점 | model_id에서 bge-m3 |  |
| `mlx-community/bge-m3-mlx-fp16` | 2점 | model_id에서 bge-m3 |  |
| `mykor/KURE-v1-gguf` | 2점 | model_id에서 kure |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `telepix/PIXIE-Rune-v1.5` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 bge |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 57개 — `amazon/Titan-text-embeddings-v2`, `BM-K/KoSimCSE-bert-multitask`, `BM-K/KoSimCSE-roberta`, `BM-K/KoSimCSE-roberta-multitask`, `CISCai/jina-embeddings-v3-separation-distilled`, `codefuse-ai/F2LLM-v2-0.6B` …


### `mc06` core만 · text-generation · hard

> KoGPT랑 Polyglot-Ko 비교해줘. 많이 쓰이는 한국어 생성 모델로.

조건 → 질의문 근거

- `tasks=["text-generation"]` ← 생성 → text-generation
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core

판정 규칙 (판정 전에 고정)

- **must** model_id가 KoGPT 또는 Polyglot 계열이다
- **2점** 한국어 전용 계열(KoGPT, Polyglot-Ko)이다
- **1점** 다국어 Polyglot이거나 파인튜닝·변환본

후보 926개 전수 스캔 → 🚩 8 / ⚠️ 5 / ✅ 913

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `EleutherAI/polyglot-ko-1.3b` | 2점 | model_id에서 polyglot |  |
| `EleutherAI/polyglot-ko-12.8b` | 2점 | model_id에서 polyglot |  |
| `EleutherAI/polyglot-ko-3.8b` | 2점 | model_id에서 polyglot |  |
| `EleutherAI/polyglot-ko-5.8b` | 2점 | model_id에서 polyglot |  |
| `psyche/kogpt` | 2점 | model_id에서 kogpt |  |
| `skt/kogpt2-base-v2` | 2점 | model_id에서 kogpt |  |
| `beomi/OPEN-SOLAR-KO-10.7B` | 1점 | semantic_metadata에서 polyglot |  |
| `beomi/llama-2-ko-7b` | 1점 | semantic_metadata에서 polyglot |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Bingsu/exaone-3.0-7.8b-it` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 gpt2 |  |
| `LLM-OS-Models/KoHRM-Text-1.4B-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 gpt2 |  |
| `ai-forever/mGPT` | 믿을 수 있는 단계엔 없고 filter_metadata에만 gpt2 |  |
| `beomi/Yi-Ko-6B` | 믿을 수 있는 단계엔 없고 README 원문에만 polyglot |  |
| `skt/ko-gpt-trinity-1.2B-v0.5` | 믿을 수 있는 단계엔 없고 filter_metadata에만 gpt2 |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 913개 — `0ppxnhximxr/Motif-3-FP8`, `0xWhiteMage/Qwen3.8-27B-Kearuga`, `0xzknw/LFM2.5-1.2B-Thinking-Heretic`, `0xzknw/LFM2.5-2.6B-Heretic-NX-PRIME`, `42dot/42dot_LLM-PLM-1.3B`, `42dot/42dot_LLM-SFT-1.3B` …


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

후보 117개 전수 스캔 → 🚩 19 / ⚠️ 6 / ✅ 92

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `raxtemur/SONAR_200_text_decoder` | 2점 | filter_metadata에서 nllb |  |
| `JustFrederik/nllb-200-distilled-1.3B-ct2-int8` | 2점 | model_id에서 nllb |  |
| `JustFrederik/nllb-200-distilled-600M-ct2-int8` | 2점 | model_id에서 nllb |  |
| `LifeAi-dev/nllb-200-3.3B-ct2-int8` | 2점 | model_id에서 nllb |  |
| `OpenNMT/nllb-200-3.3B-ct2-int8` | 2점 | model_id에서 nllb |  |
| `OpenNMT/nllb-200-distilled-1.3B-ct2-int8` | 2점 | model_id에서 nllb |  |
| `Serkan007/CTranslate2-nllb-200-int8` | 2점 | model_id에서 nllb |  |
| `Xenova/nllb-200-distilled-600M` | 2점 | model_id에서 nllb |  |
| `entai2965/nllb-200-distilled-600M-ctranslate2` | 2점 | model_id에서 nllb |  |
| `facebook/mbart-large-50-many-to-many-mmt` | 2점 | model_id에서 mbart |  |
| `facebook/mbart-large-cc25` | 2점 | model_id에서 mbart |  |
| `facebook/nllb-200-1.3B` | 2점 | model_id에서 nllb |  |
| `facebook/nllb-200-3.3B` | 2점 | model_id에서 nllb |  |
| `facebook/nllb-200-distilled-1.3B` | 2점 | model_id에서 nllb |  |
| `facebook/nllb-200-distilled-600M` | 2점 | model_id에서 nllb |  |
| `facebook/nllb-moe-54b` | 2점 | model_id에서 nllb |  |
| `mijuanlo/nllb-200-distilled-600M-ct2-int8` | 2점 | model_id에서 nllb |  |
| `Babelscape/mrebel-large` | 1점 | filter_metadata에서 mbart |  |
| `NHNDQ/nllb-finetuned-en2ko` | 1점 | model_id에서 nllb |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `BSC-LT/salamandraTA-7b-instruct` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 nllb |  |
| `Helsinki-NLP/opus-mt-ko-en` | 믿을 수 있는 단계엔 없고 model_id에만 opus-mt |  |
| `Helsinki-NLP/opus-mt-tc-big-en-ko` | 믿을 수 있는 단계엔 없고 model_id에만 opus-mt |  |
| `Helsinki-NLP/opus-mt-tc-big-ko-en` | 믿을 수 있는 단계엔 없고 model_id에만 opus-mt |  |
| `Xenova/opus-mt-ko-en` | 믿을 수 있는 단계엔 없고 model_id에만 opus-mt |  |
| `alirezamsh/small100` | 믿을 수 있는 단계엔 없고 filter_metadata에만 m2m |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 92개 — `42ailab/TranslateGemma-27B-GGUF`, `42ailab/TranslateGemma-4B-GGUF`, `alexwkleung/Hy-MT2-7B-Abliterated-GGUF`, `alphaZimuth/Hy-MT2-30B-A3B-APEX-GGUF`, `alphaZimuth/Hy-MT2-30B-A3B-Uncensored-Heretic-APEX-GGUF`, `alphaZimuth/Hy-MT2-30B-A3B-Uncensored-v1-APEX-GGUF` …


### `mc08` ≤1.0B · core만 · 값공개 · automatic-speech-recognition · hard

> Whisper small과 wav2vec 중에 한국어 음성 인식에 뭐가 좋아? 1B 이하로 공개된 것 중 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["automatic-speech-recognition"]` ← 음성 인식
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=1.0` ← 1B 이하
- `require_known_parameters=true` ← 로 공개된

판정 규칙 (판정 전에 고정)

- **must** model_id가 Whisper small 또는 wav2vec 계열이다
- **2점** 그 계열이고 한국어 파인튜닝이 확인된다
- **1점** 다른 크기의 Whisper이거나 변환본·양자화본

후보 34개 전수 스캔 → 🚩 12 / ⚠️ 13 / ✅ 9

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `MahmoudAshraf/mms-300m-1130-forced-aligner` | 2점 | filter_metadata에서 wav2vec |  |
| `facebook/mms-1b-all` | 2점 | filter_metadata에서 wav2vec |  |
| `facebook/mms-1b-fl102` | 2점 | filter_metadata에서 wav2vec |  |
| `facebook/mms-1b-l1107` | 2점 | filter_metadata에서 wav2vec |  |
| `onnx-community/mms-300m-1130-forced-aligner-ONNX` | 2점 | filter_metadata에서 wav2vec |  |
| `42MARU/ko-spelling-wav2vec2-conformer-del-1s` | 2점 | model_id에서 wav2vec |  |
| `Kkonjeong/wav2vec2-base-korean` | 2점 | model_id에서 wav2vec |  |
| `kresnik/wav2vec2-large-xlsr-korean` | 2점 | model_id에서 wav2vec |  |
| `openai/whisper-small` | 2점 | model_id에서 whisper-small |  |
| `slplab/wav2vec2-xls-r-300m_phone-mfa_korean` | 2점 | model_id에서 wav2vec |  |
| `unsloth/whisper-small` | 2점 | model_id에서 whisper-small |  |
| `w11wo/wav2vec2-xls-r-300m-korean` | 2점 | model_id에서 wav2vec |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `HeartMuLa/HeartTranscriptor-oss` | 믿을 수 있는 단계엔 없고 filter_metadata에만 whisper |  |
| `ghost613/whisper-large-v3-turbo-korean` | 믿을 수 있는 단계엔 없고 model_id에만 whisper |  |
| `microsoft/paza-whisper-large-v3-turbo` | 믿을 수 있는 단계엔 없고 model_id에만 whisper |  |
| `mlx-community/whisper-tiny-asr-fp16` | 믿을 수 있는 단계엔 없고 model_id에만 whisper |  |
| `moonshine-ai/moonshine-base-ko` | 믿을 수 있는 단계엔 없고 README 원문에만 whisper |  |
| `moonshine-ai/moonshine-tiny-ko` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 whisper |  |
| `openai/whisper-base` | 믿을 수 있는 단계엔 없고 model_id에만 whisper |  |
| `openai/whisper-large-v3-turbo` | 믿을 수 있는 단계엔 없고 model_id에만 whisper |  |
| `openai/whisper-medium` | 믿을 수 있는 단계엔 없고 model_id에만 whisper |  |
| `openai/whisper-tiny` | 믿을 수 있는 단계엔 없고 model_id에만 whisper |  |
| `seastar105/whisper-medium-komixv2` | 믿을 수 있는 단계엔 없고 model_id에만 whisper |  |
| `team-lucid/hubert-base-korean` | 믿을 수 있는 단계엔 없고 model_id에만 hubert |  |
| `unsloth/whisper-large-v3-turbo` | 믿을 수 있는 단계엔 없고 model_id에만 whisper |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 9개 — `Aliados/nemotron-3.5-asr-streaming-0.6b`, `aufklarer/Qwen3-ASR-1.7B-MLX-4bit`, `aufklarer/Qwen3-ASR-CoreML`, `bezzam/omniasr-ctc-300m-v2`, `Edge0/Audio8-ASR-0.1B`, `mlx-community/nemotron-3.5-asr-streaming-0.6b` …


### `mc09` core만 · translation · easy

> opus-mt와 m2m100 중에 한국어 번역에 뭐가 나아? 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["translation"]` ← 번역
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core

판정 규칙 (판정 전에 고정)

- **must** model_id가 opus-mt 또는 M2M100 계열이다
- **2점** 그 계열의 본체이고 한국어 방향이 확인된다
- **1점** 같은 계열이나 한국어 방향이 불명확하거나 변환본

후보 117개 전수 스캔 → 🚩 16 / ⚠️ 0 / ✅ 101

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `LifeAi-dev/nllb-200-3.3B-ct2-int8` | 2점 | filter_metadata에서 m2m100 |  |
| `NHNDQ/nllb-finetuned-en2ko` | 2점 | filter_metadata에서 m2m100 |  |
| `OpenNMT/nllb-200-3.3B-ct2-int8` | 2점 | filter_metadata에서 m2m100 |  |
| `OpenNMT/nllb-200-distilled-1.3B-ct2-int8` | 2점 | filter_metadata에서 m2m100 |  |
| `Xenova/nllb-200-distilled-600M` | 2점 | filter_metadata에서 m2m100 |  |
| `alirezamsh/small100` | 2점 | filter_metadata에서 m2m100 |  |
| `facebook/nllb-200-1.3B` | 2점 | filter_metadata에서 m2m100 |  |
| `facebook/nllb-200-3.3B` | 2점 | filter_metadata에서 m2m100 |  |
| `facebook/nllb-200-distilled-1.3B` | 2점 | filter_metadata에서 m2m100 |  |
| `facebook/nllb-200-distilled-600M` | 2점 | filter_metadata에서 m2m100 |  |
| `mijuanlo/nllb-200-distilled-600M-ct2-int8` | 2점 | filter_metadata에서 m2m100 |  |
| `raxtemur/SONAR_200_text_decoder` | 2점 | filter_metadata에서 m2m100 |  |
| `Helsinki-NLP/opus-mt-ko-en` | 2점 | model_id에서 opus-mt |  |
| `Helsinki-NLP/opus-mt-tc-big-en-ko` | 2점 | model_id에서 opus-mt |  |
| `Helsinki-NLP/opus-mt-tc-big-ko-en` | 2점 | model_id에서 opus-mt |  |
| `Xenova/opus-mt-ko-en` | 2점 | model_id에서 opus-mt |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 101개 — `42ailab/TranslateGemma-27B-GGUF`, `42ailab/TranslateGemma-4B-GGUF`, `alexwkleung/Hy-MT2-7B-Abliterated-GGUF`, `alphaZimuth/Hy-MT2-30B-A3B-APEX-GGUF`, `alphaZimuth/Hy-MT2-30B-A3B-Uncensored-Heretic-APEX-GGUF`, `alphaZimuth/Hy-MT2-30B-A3B-Uncensored-v1-APEX-GGUF` …


### `mc10` 조건 없음 · question-answering · easy

> KoELECTRA와 mDeBERTa 중에 한국어 질의응답에 뭐가 나아?

조건 → 질의문 근거

- `tasks=["question-answering"]` ← 질의응답
- `korean_required=true` ← 한국어

판정 규칙 (판정 전에 고정)

- **must** model_id가 KoELECTRA 또는 mDeBERTa 계열이다
- **2점** 한국어 전용 계열(KoELECTRA)이고 질의응답 용도가 확인된다
- **1점** 다국어 계열(mDeBERTa)이거나 다른 task용 파인튜닝

후보 21개 전수 스캔 → 🚩 3 / ⚠️ 0 / ✅ 18

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `monologg/koelectra-base-v3-finetuned-korquad` | 2점 | model_id에서 koelectra |  |
| `monologg/koelectra-small-v2-distilled-korquad-384` | 2점 | model_id에서 koelectra |  |
| `timpal0l/mdeberta-v3-base-squad2` | 1점 | model_id에서 mdeberta |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 18개 — `mradermacher/IoGPT-A1-Instruct-i1-GGUF`, `mradermacher/next-12b-i1-GGUF`, `mradermacher/next-1b-GGUF`, `bespin-global/klue-bert-base-aihub-mrc`, `cgus/Apollo2-7B-iMat-GGUF`, `FreedomIntelligence/Apollo-MoE-0.5B` …


