# semantic_capability 판정 워크시트

**숫자 검증은 명령 한 줄이 전부 합니다.**

```bash
cd ai && ../.venv/bin/python test/golden/v2/tools/verify.py semantic_capability
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

### `ca01` 조건 없음 · summarization · hard

> 뉴스 기사를 짧게 줄여주는 한국어 모델이 필요해.

조건 → 질의문 근거

- `tasks=["summarization"]` ← 줄여주는 → summarization
- `korean_required=true` ← 한국어

판정 규칙 (판정 전에 고정)

- **must** 뉴스·기사 도메인이 model_id 또는 claim에서 확인된다
- **2점** 뉴스 기사 요약으로 학습·파인튜닝된 것이 명시돼 있다
- **1점** 일반 문서 요약 모델로 뉴스에도 쓸 수 있으나 도메인 명시가 없다

후보 14개 전수 스캔 → 🚩 3 / ⚠️ 6 / ✅ 5

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `mskayacioglu/mbart50-xlsum` | 1점 | semantic_metadata에서 news |  |
| `ainize/kobart-news` | 1점 | model_id에서 news |  |
| `data-silence/any-news-sum` | 1점 | model_id에서 news |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `csebuetnlp/mT5_m2m_crossSum` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 article |  |
| `csebuetnlp/mT5_m2m_crossSum_enhanced` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 article |  |
| `csebuetnlp/mT5_m2o_english_crossSum` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 article |  |
| `csebuetnlp/mT5_multilingual_XLSum` | 믿을 수 있는 단계엔 없고 README 원문에만 article |  |
| `ncls-p/Qwen2.5-3B-blog-key-points` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 article |  |
| `ncls-p/Qwen2.5-7B-blog-key-points` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 article |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 5개 — `EbanLee/kobart-summary-v3`, `eenzeenee/t5-base-korean-summarization`, `eenzeenee/t5-small-korean-summarization`, `psyche/KoT5-summarization`, `QyrouNnet-AI/QNS-2-ReLearn-Preview`


### `ca02` 조건 없음 · question-answering · hard

> 지문을 주면 그 안에서 답을 찾아주는 한국어 모델을 찾고 있어.

조건 → 질의문 근거

- `tasks=["question-answering"]` ← 답을 찾아주는 → question-answering
- `korean_required=true` ← 한국어

판정 규칙 (판정 전에 고정)

- **must** 지문에서 답을 추출하는 용도가 확인된다
- **2점** KorQuAD 등 한국어 독해 데이터로 학습됐다
- **1점** 다국어 QA 모델이거나 SQuAD 기반으로 한국어를 포함한다

후보 21개 전수 스캔 → 🚩 2 / ⚠️ 2 / ✅ 17

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

- **용도 언급 없음** 17개 — `mradermacher/IoGPT-A1-Instruct-i1-GGUF`, `mradermacher/next-12b-i1-GGUF`, `mradermacher/next-1b-GGUF`, `cgus/Apollo2-7B-iMat-GGUF`, `FreedomIntelligence/Apollo-MoE-0.5B`, `FreedomIntelligence/Apollo-MoE-7B` …


### `ca03` core만 · text-classification · hard

> 고객 문의가 어떤 요청인지 자동으로 갈라주는 한국어 모델이 필요해. 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["text-classification"]` ← 분류 → text-classification
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)

판정 규칙 (판정 전에 고정)

- **must** 의도·문의 분류 용도가 claim 또는 model_id에서 확인된다
- **2점** 고객 문의·의도 분류 전용으로 학습된 것이 명시돼 있다
- **1점** 주제·범주 분류 모델로 문의 분류에도 쓸 수 있으나 명시가 없다

후보 49개 전수 스캔 → 🚩 7 / ⚠️ 9 / ✅ 33

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `chaoliangUNSW/Jev-Style-0.8B-Decision-v3` | 1점 | semantic_metadata에서 intent |  |
| `clapAI/mmBERT-small-multilingual-sentiment` | 1점 | semantic_metadata에서 고객 |  |
| `clapAI/modernBERT-base-multilingual-sentiment` | 1점 | semantic_metadata에서 고객 |  |
| `clapAI/roberta-base-multilingual-sentiment` | 1점 | semantic_metadata에서 고객 |  |
| `classla/multilingual-IPTC-news-topic-classifier` | 1점 | semantic_metadata에서 intent |  |
| `desert-ant-labs/emo` | 1점 | semantic_metadata에서 intent |  |
| `doofz/THX-01` | 1점 | semantic_metadata에서 intent |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Copycats/koelectra-base-v3-generalized-sentiment-analysis` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 customer |  |
| `Horizon-Labs/content-safety-guard-small` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 category |  |
| `NorviTech/armiger-ultra` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 category |  |
| `chaoliangUNSW/Jev-Style-0.8B-Decision-v3-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 customer, category |  |
| `knowledgator/opir-edge-multilang-v1.0` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 category |  |
| `knowledgator/opir-multitask-multilang-v1.0` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 category |  |
| `lokas/spam-usernames-classifier` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 category |  |
| `quevirus/Xevn-4B-GGUF` | 믿을 수 있는 단계엔 없고 README 원문에만 customer |  |
| `skt/A.X-Encoder-base` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 category |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 31개 — `agentlans/multilingual-e5-small-aligned-sentiment`, `amber-tech/bert-multilingual-passage-reranking-msmarco`, `amphora/KorFinASC-XLM-RoBERTa`, `autopilot-ai/EthicalEye`, `banjl4487/MODEL`, `cis-lmu/glotlid` …
- **claim 자체가 비어 있음** 2개 — `circulus/koelectra-polite-v1`, `circulus/koelectra-sentiment-v1`


### `ca04` core만 · text-classification · easy

> 상품 리뷰가 좋은 말인지 나쁜 말인지 가려내는 한국어 모델을 추천해줘. 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["text-classification"]` ← 분류 → text-classification
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)

판정 규칙 (판정 전에 고정)

- **must** 감성 분류 용도가 claim 또는 model_id에서 확인된다
- **2점** NSMC 등 한국어 리뷰 감성 데이터로 학습됐다
- **1점** 다국어 감성 분류이거나 도메인이 리뷰가 아닌 일반 감성 분류

후보 49개 전수 스캔 → 🚩 13 / ⚠️ 8 / ✅ 28

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `daekeun-ml/koelectra-small-v3-nsmc` | 2점 | model_id에서 nsmc |  |
| `chaoliangUNSW/Jev-Style-0.8B-Decision-v3-GGUF` | 1점 | semantic_metadata에서 sentiment |  |
| `snunlp/KR-FinBert-SC` | 1점 | semantic_metadata에서 sentiment |  |
| `Copycats/koelectra-base-v3-generalized-sentiment-analysis` | 1점 | model_id에서 sentiment |  |
| `DataWizardd/finbert-sentiment-ko` | 1점 | model_id에서 sentiment |  |
| `FISA-conclave/klue-roberta-news-sentiment` | 1점 | model_id에서 sentiment |  |
| `Kenpache/multilingual-financial-sentiment-v2` | 1점 | model_id에서 sentiment |  |
| `agentlans/multilingual-e5-small-aligned-sentiment` | 1점 | model_id에서 sentiment |  |
| `circulus/koelectra-sentiment-v1` | 1점 | model_id에서 sentiment |  |
| `clapAI/mmBERT-small-multilingual-sentiment` | 1점 | model_id에서 sentiment |  |
| `clapAI/modernBERT-base-multilingual-sentiment` | 1점 | model_id에서 sentiment |  |
| `clapAI/roberta-base-multilingual-sentiment` | 1점 | model_id에서 sentiment |  |
| `tabularisai/multilingual-sentiment-analysis` | 1점 | model_id에서 sentiment |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `HPLT/OpenLID-v3` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 positive |  |
| `Horizon-Labs/content-safety-guard-small` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 positive |  |
| `MelissaJ/koelectra-emotion-6-emotion-base` | 믿을 수 있는 단계엔 없고 model_id에만 emotion |  |
| `Zeolit/lettuce-thymos-26m-v1` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 emotion |  |
| `doofz/THX-01` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 emotion |  |
| `guardion/ModernGuard-1` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 positive |  |
| `knowledgator/opir-edge-multilang-v1.0` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 positive |  |
| `tabularisai/multilingual-emotion-classification` | 믿을 수 있는 단계엔 없고 model_id에만 emotion |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 27개 — `amber-tech/bert-multilingual-passage-reranking-msmarco`, `amphora/KorFinASC-XLM-RoBERTa`, `autopilot-ai/EthicalEye`, `banjl4487/MODEL`, `chaoliangUNSW/Jev-Style-0.8B-Decision-v3`, `cis-lmu/glotlid` …
- **claim 자체가 비어 있음** 1개 — `circulus/koelectra-polite-v1`


### `ca05` core만 · text-classification · hard

> 댓글에서 남을 공격하는 표현을 걸러내는 한국어 모델이 필요해. 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["text-classification"]` ← 분류 → text-classification
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)

판정 규칙 (판정 전에 고정)

- **must** 혐오·욕설 탐지 용도가 claim 또는 model_id에서 확인된다
- **2점** UnSmile 등 한국어 혐오 표현 데이터로 학습됐다
- **1점** 다국어 유해성 분류이거나 일반 세이프티 분류 모델

후보 49개 전수 스캔 → 🚩 1 / ⚠️ 4 / ✅ 44

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `autopilot-ai/EthicalEye` | 1점 | semantic_metadata에서 hate |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Horizon-Labs/content-safety-guard-small` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 toxic |  |
| `Horizon-Labs/multilingual-toxicity-small` | 믿을 수 있는 단계엔 없고 model_id에만 toxic |  |
| `knowledgator/opir-edge-multilang-v1.0` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 toxic |  |
| `knowledgator/opir-multitask-multilang-v1.0` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 toxic |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 42개 — `agentlans/multilingual-e5-small-aligned-sentiment`, `amber-tech/bert-multilingual-passage-reranking-msmarco`, `amphora/KorFinASC-XLM-RoBERTa`, `banjl4487/MODEL`, `chaoliangUNSW/Jev-Style-0.8B-Decision-v3`, `chaoliangUNSW/Jev-Style-0.8B-Decision-v3-GGUF` …
- **claim 자체가 비어 있음** 2개 — `circulus/koelectra-polite-v1`, `circulus/koelectra-sentiment-v1`


### `ca06` core만 · text-classification · hard

> 광고나 스팸 글을 걸러내는 한국어 모델 있어? 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["text-classification"]` ← 분류 → text-classification
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core (다운로드 500 이상)

판정 규칙 (판정 전에 고정)

- **must** 스팸·광고 탐지 용도가 claim 또는 model_id에서 확인된다
- **2점** 스팸·광고 분류 전용으로 학습된 것이 명시돼 있다
- **1점** 일반 필터링·모더레이션 모델로 스팸에도 쓸 수 있으나 명시가 없다

후보 49개 전수 스캔 → 🚩 1 / ⚠️ 11 / ✅ 37

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `lokas/spam-usernames-classifier` | 2점 | model_id에서 spam |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Horizon-Labs/content-safety-guard-small` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 moderation |  |
| `Horizon-Labs/multilingual-toxicity-small` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 moderation |  |
| `Horizon-Labs/prompt-injection-guard-base` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 filter |  |
| `Horizon-Labs/prompt-injection-guard-small` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 filter |  |
| `Metabaron6/Shieldstral-1.0-3B-GGUF` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 moderation |  |
| `NorviTech/armiger-ultra` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 filter |  |
| `autopilot-ai/EthicalEye` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 moderation |  |
| `doofz/THX-01` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 spam |  |
| `knowledgator/opir-multitask-multilang-v1.0` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 moderation |  |
| `llm-semantic-router/mmbert32k-modality-router-merged` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 moderation |  |
| `vllm-sr/mmbert32k-modality-router-merged` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 moderation |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 35개 — `agentlans/multilingual-e5-small-aligned-sentiment`, `amber-tech/bert-multilingual-passage-reranking-msmarco`, `amphora/KorFinASC-XLM-RoBERTa`, `banjl4487/MODEL`, `chaoliangUNSW/Jev-Style-0.8B-Decision-v3`, `chaoliangUNSW/Jev-Style-0.8B-Decision-v3-GGUF` …
- **claim 자체가 비어 있음** 2개 — `circulus/koelectra-polite-v1`, `circulus/koelectra-sentiment-v1`


### `ca07` core만 · sentence-similarity · hard

> 같은 뜻을 다르게 쓴 문장을 찾아내는 한국어 모델이 필요해. 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["sentence-similarity"]` ← 문장 유사도
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core

판정 규칙 (판정 전에 고정)

- **must** 패러프레이즈·중복 문장 탐지 용도가 확인된다
- **2점** 패러프레이즈 탐지로 학습된 것이 명시돼 있다
- **1점** 일반 문장 유사도 모델로 중복 탐지에도 쓸 수 있으나 명시가 없다

후보 71개 전수 스캔 → 🚩 3 / ⚠️ 7 / ✅ 61

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `lang-uk/ukr-paraphrase-multilingual-mpnet-base` | 2점 | model_id에서 paraphrase |  |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | 2점 | model_id에서 paraphrase |  |
| `sentence-transformers/paraphrase-multilingual-mpnet-base-v2` | 2점 | model_id에서 paraphrase |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Alibaba-NLP/gte-multilingual-base` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 duplicate |  |
| `Hiveurban/multilingual-e5-base` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 duplicate |  |
| `RedHatAI/snowflake-arctic-embed-l-v2.0` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 duplicate |  |
| `Snowflake/snowflake-arctic-embed-l-v2.0` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 duplicate |  |
| `Snowflake/snowflake-arctic-embed-m-v2.0` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 duplicate |  |
| `beademiguelperez/sentence-transformers-multilingual-e5-small` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 duplicate |  |
| `intfloat/multilingual-e5-base` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 duplicate |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 61개 — `antoinelouis/colbert-xm`, `batiai/Qwen3-VL-Embedding-8B-GGUF`, `bespin-global/klue-sroberta-base-continue-learning-by-mnr`, `BidirLM/BidirLM-0.6B-Embedding`, `BidirLM/BidirLM-1B-Embedding`, `BidirLM/BidirLM-Omni-2.5B-Embedding` …


### `ca08` ≤1.0B · core만 · 값공개 · automatic-speech-recognition · hard

> 회의 녹음을 글로 받아 적어주는 한국어 모델을 찾고 있어. 1B 이하로 공개된 것 중 많이 쓰이는 것으로.

조건 → 질의문 근거

- `tasks=["automatic-speech-recognition"]` ← 받아 적어주는 → automatic-speech-recognition
- `korean_required=true` ← 한국어
- `pools=["core"]` ← 많이 쓰이는 → core
- `max_parameters_billion=1.0` ← 1B 이하
- `require_known_parameters=true` ← 로 공개된

판정 규칙 (판정 전에 고정)

- **must** 회의·장문 음성 전사 용도가 확인된다
- **2점** 회의·장문 전사 용도가 명시돼 있다
- **1점** 일반 한국어 전사 모델로 회의에도 쓸 수 있으나 도메인 명시가 없다

후보 34개 전수 스캔 → 🚩 2 / ⚠️ 24 / ✅ 8

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `seastar105/whisper-medium-komixv2` | 2점 | semantic_metadata에서 회의 |  |
| `unsloth/whisper-large-v3-turbo` | 2점 | semantic_metadata에서 long-form |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `Aliados/nemotron-3.5-asr-streaming-0.6b` | 믿을 수 있는 단계엔 없고 README 원문에만 transcri |  |
| `Edge0/Audio8-ASR-0.1B` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `HeartMuLa/HeartTranscriptor-oss` | 믿을 수 있는 단계엔 없고 model_id에만 transcri |  |
| `Kkonjeong/wav2vec2-base-korean` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `Qwen/Qwen3-ASR-0.6B-hf` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `aufklarer/Qwen3-ASR-1.7B-MLX-4bit` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `bezzam/omniasr-ctc-300m-v2` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `facebook/mms-1b-all` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `facebook/mms-1b-fl102` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `facebook/mms-1b-l1107` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `kresnik/wav2vec2-large-xlsr-korean` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `microsoft/paza-whisper-large-v3-turbo` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `mlx-community/nemotron-3.5-asr-streaming-0.6b` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `mlx-community/whisper-tiny-asr-fp16` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `moonshine-ai/moonshine-base-ko` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `moonshine-ai/moonshine-tiny-ko` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `nvidia/nemotron-3.5-asr-streaming-0.6b` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `onnx-community/cohere-transcribe-03-2026-ONNX` | 믿을 수 있는 단계엔 없고 model_id에만 transcri |  |
| `openai/whisper-base` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `openai/whisper-large-v3-turbo` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `openai/whisper-medium` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `openai/whisper-small` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `openai/whisper-tiny` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |
| `unsloth/whisper-small` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 transcri |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 8개 — `42MARU/ko-spelling-wav2vec2-conformer-del-1s`, `aufklarer/Qwen3-ASR-CoreML`, `ghost613/whisper-large-v3-turbo-korean`, `MahmoudAshraf/mms-300m-1130-forced-aligner`, `onnx-community/mms-300m-1130-forced-aligner-ONNX`, `slplab/wav2vec2-xls-r-300m_phone-mfa_korean` …


### `ca09` ≤1.0B · 값공개 · image-text-to-text · hard

> 사진 속 글자를 읽어서 한국어로 알려주는 모델이 필요해. 파라미터 1B 이하로 공개된 것으로.

조건 → 질의문 근거

- `tasks=["image-text-to-text"]` ← 이미지-텍스트
- `korean_required=true` ← 한국어
- `max_parameters_billion=1.0` ← 1B 이하
- `require_known_parameters=true` ← 로 공개된

판정 규칙 (판정 전에 고정)

- **must** 이미지 속 글자 인식 용도가 확인된다
- **2점** 한국어 OCR·문서 이해로 학습된 것이 명시돼 있다
- **1점** 다국어 VLM으로 글자 인식이 가능하나 한국어 특화 명시가 없다

후보 12개 전수 스캔 → 🚩 6 / ⚠️ 6 / ✅ 0

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
| `LiquidAI/LFM2.5-VL-450M` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 table |  |
| `LiquidAI/LFM2.5-VL-450M-MLX-bf16` | 믿을 수 있는 단계엔 없고 README 원문에만 document |  |
| `Mattimax/DAC6.5` | 믿을 수 있는 단계엔 없고 README 원문에만 document |  |
| `coder3101/LFM2.5-VL-450M-heretic` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 table |  |
| `mlx-community/LFM2.5-VL-450M-6bit` | 믿을 수 있는 단계엔 없고 README 원문에만 document |  |
| `saidutta69/LFM2.5-VL-450M-heretic` | 믿을 수 있는 단계엔 없고 semantic_metadata에만 table |  |


### `ca10` ≤1.0B · 값공개 · image-text-to-text · hard

> 표나 그래프가 든 이미지를 읽고 설명해주는 한국어 모델 있어? 파라미터 1B 이하로 공개된 것으로.

조건 → 질의문 근거

- `tasks=["image-text-to-text"]` ← 이미지-텍스트
- `korean_required=true` ← 한국어
- `max_parameters_billion=1.0` ← 1B 이하
- `require_known_parameters=true` ← 로 공개된

판정 규칙 (판정 전에 고정)

- **must** 표·차트 이해 용도가 확인된다
- **2점** 차트·표 이해로 학습된 것이 명시돼 있다
- **1점** 일반 VLM으로 표를 읽을 수 있으나 차트 특화 명시가 없다

후보 12개 전수 스캔 → 🚩 2 / ⚠️ 3 / ✅ 7

#### 🚩 정답 맞나 — 제안 등급을 확인해 주세요

| 모델 | 제안 | 근거 | 확정 |
|---|:--:|---|:--:|
| `LiquidAI/LFM2.5-VL-450M-MLX-8bit` | 1점 | semantic_metadata에서 table |  |
| `saidutta69/LFM2.5-VL-450M-heretic` | 1점 | semantic_metadata에서 table |  |

#### ⚠️ 진짜 아닌가 — 빠진 정답이 여기 숨습니다

| 모델 | 왜 애매한가 | 확정 |
|---|---|:--:|
| `LiquidAI/LFM2.5-VL-450M` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 table |  |
| `coder3101/LFM2.5-VL-450M-heretic` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 table |  |
| `localdeel/ko-hand-ocr-vl` | 믿을 수 있는 단계엔 없고 benchmark_metadata에만 table |  |

#### ✅ 명백한 오답 — 소분류만 보고 넘기세요

- **용도 언급 없음** 7개 — `LiquidAI/LFM2.5-VL-450M-MLX-4bit`, `mlx-community/LFM2.5-VL-450M-6bit`, `LiquidAI/LFM2.5-VL-450M-MLX-5bit`, `LiquidAI/LFM2.5-VL-450M-MLX-6bit`, `LiquidAI/LFM2.5-VL-450M-MLX-bf16`, `Mattimax/DAC6.5` …


