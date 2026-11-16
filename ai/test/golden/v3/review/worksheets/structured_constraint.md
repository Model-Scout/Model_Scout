# 골든셋 v3 검수 워크시트 — structured_constraint (구조화 조건)

> 상태: **초안 + 전수 스캔 + 검수 준비 완료**. 아래 점수는 Claude 의 제안이며 정답이 아니다.
>
> 판정 입력: `python test/golden/v3/tools/judge.py <query_id> <model_id> --decision approve|2|1|exclude|hold --reason "…" --by <이름>`

## st01 — 파라미터가 0.2B 이하이고 ONNX 가중치가 함께 올라온 한국어 문장 임베딩 모델 목록을 보고 싶어요.

- 사용자 의도: ONNX Runtime 으로 서빙할 초경량 한국어 임베딩 모델 고르기
- persona / 표현: ml_engineer / 기술형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `max_parameters_billion` | 0.2 | 파라미터가 0.2B 이하 | 예 |
| `require_artifact` | onnx | ONNX 가중치가 함께 올라온 | 예 |
| `tasks` | sentence-similarity, feature-extraction | 문장 임베딩 | 예 |

- **2점 기준**: 조건을 모두 만족하는 문장 임베딩 원본 모델
- **1점 기준**: 조건은 만족하지만 원본의 변환·양자화·재업로드이거나 임베딩이 부가 기능인 모델

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 23 | 23 | 0 | 0 | 0 | 23 | ✅ | 18 |


#### 1. [AliaeAI/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/AliaeAI/paraphrase-multilingual-MiniLM-L12-v2) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | AliaeAI/paraphrase-multilingual-MiniLM-L12-v2 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.118 / 512 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.44 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for sentence similarity tasks. |
| README 인용 | pipeline_tag: sentence-similarity --- |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 446e15e878f2534180b8c3a8419c3c4e892a5fc1 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [DLCorso/multilingual-e5-small](https://huggingface.co/DLCorso/multilingual-e5-small) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | DLCorso/multilingual-e5-small (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.118 / 512 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.44 |
| 벤치마크 근거 | 없음 |
| 의미 claim (benchmarks) | MTEB ArxivClusteringS2S |
| README 인용 | config: default       name: MTEB ArxivClusteringS2S       revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53       split: test       type: mteb/arxiv-clustering-s2s     metrics: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 9d85dee02e17c778f57c888510e41bed968db046 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [Hisham480/multilingual-e5-small](https://huggingface.co/Hisham480/multilingual-e5-small) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Hisham480/multilingual-e5-small (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.118 / 512 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.44 |
| 벤치마크 근거 | 없음 |
| 의미 claim (benchmarks) | MTEB ArxivClusteringS2S |
| README 인용 | config: default       name: MTEB ArxivClusteringS2S       revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53       split: test       type: mteb/arxiv-clustering-s2s     metrics: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 2bd32e15423b8d00fb07ac6ca9ff127e59697869 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [Horizon-Labs/multilingual-embedding-small](https://huggingface.co/Horizon-Labs/multilingual-embedding-small) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | jhu-clsp/mmBERT-small (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.14 / 8192 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 0.52 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Querying an existing bge-m3 index: passages embedded earlier with BAAI/bge-m3 (dense, normalised) |
| README 인용 | ```python from sentence_transformers import SentenceTransformer  model = SentenceTransformer("Horizon-Labs/multilingual-embedding-small") q = model.encode(["How tall is the Eiffel Tower?"]) p = model.encode(["La tour Eiffel mesure 330 mètre… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 033028575b040790aef3064b2a045245ee54d238 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [Hostage928/multilingual-e5-small](https://huggingface.co/Hostage928/multilingual-e5-small) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Hostage928/multilingual-e5-small (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.118 / 512 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.44 |
| 벤치마크 근거 | 없음 |
| 의미 claim (benchmarks) | MTEB ArxivClusteringS2S |
| README 인용 | config: default       name: MTEB ArxivClusteringS2S       revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53       split: test       type: mteb/arxiv-clustering-s2s     metrics: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 2c71c984840050ba071e4a742e9faa18b0826775 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [Karmukilan/multilingual-e5-small](https://huggingface.co/Karmukilan/multilingual-e5-small) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Karmukilan/multilingual-e5-small (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.118 / 512 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.44 |
| 벤치마크 근거 | 없음 |
| 의미 claim (benchmarks) | MTEB ArxivClusteringS2S |
| README 인용 | config: default       name: MTEB ArxivClusteringS2S       revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53       split: test       type: mteb/arxiv-clustering-s2s     metrics: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | f7570610b8b1b7ee0a663ca19c7bd170f4cef471 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [Manav2op/verdict-small](https://huggingface.co/Manav2op/verdict-small) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | intfloat/multilingual-e5-small (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.118 / 512 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 0.44 |
| 벤치마크 근거 | 점수 6건 저장 |
| 의미 claim (use_cases) | The model can be utilized for quickstart examples as shown in the provided GitHub link. |
| README 인용 | com/github/Manavarya09/verdict/blob/main/examples/verdict_quickstart. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 085a41e0ea269f00483dd202a286cfb68f7aa63a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [exp-models/dragonkue-KoEn-E5-Tiny](https://huggingface.co/exp-models/dragonkue-KoEn-E5-Tiny) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | dragonkue/multilingual-e5-small-ko (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.038 / 512 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, onnx, safetensors / 0.02 |
| 벤치마크 근거 | 점수 1건 저장 |
| 의미 claim (use_cases) | It is ideal for running demos or lightweight applications, offering a good balance between speed and accuracy. |
| README 인용 | It is ideal for running demos or lightweight applications, offering a good balance between speed and accuracy. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 292c09c78c71a3f00ed56ee0d1ed9f0d39182fc9 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [hindsight-ai/hs-embed-1](https://huggingface.co/hindsight-ai/hs-embed-1) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | hotchpotch/bekko-embedding-v1-a25m (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.112 / 8192 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 0.21 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Text embeddings can be generated using a simple API call. |
| README 인용 | ```bash curl 127.0.0.1:8080/embed \   -H 'Content-Type: application/json' \   -d '{"inputs": ["Where did Maya move last spring?", "Maya moved to Lisbon in April."]}' ``` |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 3164caa4db95a03faac8a327f914f7c8f42d2f98 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [ibm-granite/granite-embedding-107m-multilingual](https://huggingface.co/ibm-granite/granite-embedding-107m-multilingual) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | ibm-granite/granite-embedding-107m-multilingual (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.107 / 514 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.2 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | embeddings |
| README 인용 | - embeddings |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | d6cffd338414d6a1c1f5decfad5fec62eebc90d5 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [ibm-granite/granite-embedding-97m-multilingual-r2](https://huggingface.co/ibm-granite/granite-embedding-97m-multilingual-r2) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | ibm-granite/granite-embedding-97m-multilingual-r2 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.097 / 32768 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.18 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | This is a simple example of how to use the granite-embedding-97m-multilingual-r2 model with the Transformers library and PyTorch. |
| README 인용 | This is a simple example of how to use the granite-embedding-97m-multilingual-r2 model with the Transformers library and PyTorch. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 835ad14087e140460703cf0fae09f97d469d65c2 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | intfloat/multilingual-e5-small (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.118 / 512 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.44 |
| 벤치마크 근거 | 없음 |
| 의미 claim (benchmarks) | MTEB ArxivClusteringS2S |
| README 인용 | config: default       name: MTEB ArxivClusteringS2S       revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53       split: test       type: mteb/arxiv-clustering-s2s     metrics: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 614241f622f53c4eeff9890bdc4f31cfecc418b3 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [jhgan/ko-sroberta-multitask](https://huggingface.co/jhgan/ko-sroberta-multitask) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

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

#### 14. [leewaay/klue-roberta-base-klueNLI-klueSTS-MSL128](https://huggingface.co/leewaay/klue-roberta-base-klueNLI-klueSTS-MSL128) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | leewaay/klue-roberta-base-klueNLI-klueSTS-MSL128 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.111 / 514 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 0.41 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is tagged for sentence-similarity tasks. |
| README 인용 | --- pipeline_tag: sentence-similarity tags: |
| provenance status | verified 14, not_applicable 3, documented 2, unknown 4 |
| revision | 1d56a3dc2715cfe5908c6ff8b6d1283a8b5907ab |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 15. [mikelalda/multilingual-e5-small](https://huggingface.co/mikelalda/multilingual-e5-small) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | mikelalda/multilingual-e5-small (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.118 / 512 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.44 |
| 벤치마크 근거 | 없음 |
| 의미 claim (benchmarks) | MTEB ArxivClusteringS2S |
| README 인용 | config: default       name: MTEB ArxivClusteringS2S       revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53       split: test       type: mteb/arxiv-clustering-s2s     metrics: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 504ced180d4bf96366ac19cc565d41208f5c08e4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 16. [nleeson/multilingual-e5-small](https://huggingface.co/nleeson/multilingual-e5-small) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | nleeson/multilingual-e5-small (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.118 / 512 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.44 |
| 벤치마크 근거 | 없음 |
| 의미 claim (benchmarks) | MTEB ArxivClusteringS2S |
| README 인용 | config: default       name: MTEB ArxivClusteringS2S       revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53       split: test       type: mteb/arxiv-clustering-s2s     metrics: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 7185c55e29d02d7f7922a2ce1ec6e4fda242c686 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 17. [sentence-transformers/distiluse-base-multilingual-cased-v1](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | sentence-transformers/distiluse-base-multilingual-cased-v1 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.135 / 512 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.5 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for sentence similarity tasks. |
| README 인용 | pipeline_tag: sentence-similarity --- |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 826fee3d516ebb14987355af373f5b69101c7006 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 18. [sentence-transformers/distiluse-base-multilingual-cased-v2](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v2) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | sentence-transformers/distiluse-base-multilingual-cased-v2 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.135 / 512 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.5 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for sentence similarity tasks. |
| README 인용 | pipeline_tag: sentence-similarity --- |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | bfe45d0732ca50787611c0fe107ba278c7f3f889 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 19. [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.118 / 512 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.44 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for sentence similarity tasks. |
| README 인용 | pipeline_tag: sentence-similarity --- |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | e8f8c211226b894fcb81acc59f3b34ba3efd5f42 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 20. [skt/kobert-base-v1](https://huggingface.co/skt/kobert-base-v1) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | skt/kobert-base-v1 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.092 / 512 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | stage1:korean_name_strong |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.34 |
| 벤치마크 근거 | 없음 |
| 의미 claim (—) | — |
| README 인용 | — |
| provenance status | verified 14, not_applicable 3, documented 1, unknown 5 |
| revision | 359874884642d748079d4dd4ff547f2cdbff67d6 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 21. [telepix/PIXIE-Splade-v1.0](https://huggingface.co/telepix/PIXIE-Splade-v1.0) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | telepix/PIXIE-Splade-v1.0 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.149 / 16384 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 0.56 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Feature extraction in sentence-transformers library. |
| README 인용 | pipeline_tag: feature-extraction library_name: sentence-transformers license: apache-2. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 730b515a74727b5f57f031a4c8108743b99e689f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 22. [thkmon/multilingual-e5-small](https://huggingface.co/thkmon/multilingual-e5-small) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | thkmon/multilingual-e5-small (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.118 / 512 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.44 |
| 벤치마크 근거 | 없음 |
| 의미 claim (benchmarks) | MTEB ArxivClusteringS2S |
| README 인용 | config: default       name: MTEB ArxivClusteringS2S       revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53       split: test       type: mteb/arxiv-clustering-s2s     metrics: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 3d8f9f71d6656cbd0428230269f1461e22d3efd8 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 23. [vllm-project/multilingual-e5-small](https://huggingface.co/vllm-project/multilingual-e5-small) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | vllm-project/multilingual-e5-small (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.118 / 512 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 0.44 |
| 벤치마크 근거 | 없음 |
| 의미 claim (benchmarks) | MTEB ArxivClusteringS2S |
| README 인용 | config: default       name: MTEB ArxivClusteringS2S       revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53       split: test       type: mteb/arxiv-clustering-s2s     metrics: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 39574ff82d5514b3a69265e39147aa9c491ab4b0 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## st02 — 상업 서비스에 넣을 한국어 음성 인식을 ONNX Runtime 으로 서버에 올리려고 해요. 라이선스가 상업 이용을 허용하는 계열인 모델만 알려 주세요.

- 사용자 의도: 상업용 STT 를 ONNX 로 배포
- persona / 표현: startup_dev / 혼합형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `commercial_status` | permitted | 라이선스가 상업 이용을 허용하는 계열 | 예 |
| `require_artifact` | onnx | ONNX Runtime 으로 서버에 올리려고 | 예 |
| `tasks` | automatic-speech-recognition | 음성 인식 | 예 |

- **2점 기준**: ONNX 파일이 있는 상업 이용 허용 계열 음성 인식 원본 모델
- **1점 기준**: 조건은 만족하지만 원본의 변환·재업로드 모델

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 12 | 12 | 0 | 0 | 0 | 12 | ✅ | 1 |


#### 1. [Daumee/Qwen3-ASR-0.6B-ONNX-CPU](https://huggingface.co/Daumee/Qwen3-ASR-0.6B-ONNX-CPU) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-0.6B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=ONNX) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin / 0.58 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | cpu-inference |
| README 인용 | - cpu-inference |
| provenance status | verified 10, not_applicable 3, documented 4, unknown 6 |
| revision | 3899991c15f9912d5e60ff5a79156d7d2253506c |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [DennisHuang648/SenseVoiceSmall-onnx](https://huggingface.co/DennisHuang648/SenseVoiceSmall-onnx) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

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

#### 3. [XDcobra/wav2vec2-large-xlsr-53-korean-ONNX](https://huggingface.co/XDcobra/wav2vec2-large-xlsr-53-korean-ONNX) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | kresnik/wav2vec2-large-xlsr-korean (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=ONNX) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx / 2.1 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is suitable for use in automatic speech recognition applications. |
| README 인용 | pipeline_tag: automatic-speech-recognition --- |
| provenance status | verified 11, not_applicable 3, documented 5, unknown 4 |
| revision | a6162331bac7e12c609ffe34c0a641b3efa6df62 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [Youngwon/whisper-large-v3-turbo_timestamped-external-data](https://huggingface.co/Youngwon/whisper-large-v3-turbo_timestamped-external-data) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-large-v3-turbo (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx / 1.23 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for automatic speech recognition tasks. |
| README 인용 | pipeline_tag: automatic-speech-recognition --- |
| provenance status | verified 10, not_applicable 3, documented 4, unknown 6 |
| revision | 71bf86550e3656be1a30385b342a8ba3b45c910a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [air-air/xlsr-53-espeak-student-ONNX](https://huggingface.co/air-air/xlsr-53-espeak-student-ONNX) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | facebook/wav2vec2-xlsr-53-espeak-cv-ft (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=ONNX) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx / 0.07 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for automatic speech recognition. |
| README 인용 | js pipeline_tag: automatic-speech-recognition base_model: facebook/wav2vec2-xlsr-53-espeak-cv-ft base_model_relation: finetune datasets: |
| provenance status | verified 11, not_applicable 3, documented 5, unknown 4 |
| revision | 5f7232263ceb005be09efaf2ff702d90dbce75c3 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [jiangzhuo9357/Qwen3-ASR-0.6B-ONNX](https://huggingface.co/jiangzhuo9357/Qwen3-ASR-0.6B-ONNX) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-0.6B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=ONNX) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 131072 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin / 0.15 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for automatic speech recognition tasks. |
| README 인용 | pipeline_tag: automatic-speech-recognition tags: |
| provenance status | verified 9, not_applicable 3, documented 4, unknown 7 |
| revision | 4a01b95fafe2c9e3af77e33c18bbb7de349c62f6 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [jiangzhuo9357/Qwen3-ASR-1.7B-ONNX](https://huggingface.co/jiangzhuo9357/Qwen3-ASR-1.7B-ONNX) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-1.7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=ONNX) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 131072 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin / 0.29 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for in-browser automatic speech recognition tasks. |
| README 인용 | 0) packaged for in-browser inference with onnxruntime-web, built for the [Sokuji](https://github. |
| provenance status | verified 9, not_applicable 3, documented 4, unknown 7 |
| revision | fcc238dfdc95cdcccaa9a7e2c7f5abc2f94f44a7 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [nenad1002/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nenad1002/nemotron-3.5-asr-streaming-0.6b) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | nvidia/nemotron-3.5-asr-streaming-0.6b (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx / 0.0 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Dynamic Runtime Flexibility: Choose the optimal operating point on the latency-accuracy Pareto curve at inference time. |
| README 인용 | - 🎛️ **Dynamic Runtime Flexibility:** Choose the optimal operating point on the latency-accuracy Pareto curve at inference time. No re-training is required to adjust for different use-case requirements. |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 397846f7f03fc8481ac9d31856382fc0cdd192fb |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [onnx-community/Voxtral-Mini-4B-Realtime-2602-ONNX](https://huggingface.co/onnx-community/Voxtral-Mini-4B-Realtime-2602-ONNX) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | mistralai/Voxtral-Mini-4B-Realtime-2602 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=onnx) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 131072 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx / 18.73 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Real-Time Transcription Purposes: |
| README 인용 | **Real-Time Transcription Purposes:** |
| provenance status | verified 12, not_applicable 3, documented 4, unknown 4 |
| revision | db34633130c460bd650644fc18dc90710d9f3e38 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [onnx-community/cohere-transcribe-03-2026-ONNX](https://huggingface.co/onnx-community/cohere-transcribe-03-2026-ONNX) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | CohereLabs/cohere-transcribe-03-2026 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=onnx) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 2048 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx / 10.4 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Example: English audio transcription |
| README 인용 | **Example:** English audio transcription |
| provenance status | verified 11, not_applicable 3, documented 4, unknown 5 |
| revision | 31b1c6211c9000d76b077ddd23b74c9090badeba |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [onnx-community/nemotron-3.5-asr-streaming-0.6b-onnx-int4](https://huggingface.co/onnx-community/nemotron-3.5-asr-streaming-0.6b-onnx-int4) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | nvidia/nemotron-3.5-asr-streaming-0.6b (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=onnx) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx / 0.0 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Dynamic Runtime Flexibility: Choose the optimal operating point on the latency-accuracy Pareto curve at inference time. |
| README 인용 | - 🎛️ **Dynamic Runtime Flexibility:** Choose the optimal operating point on the latency-accuracy Pareto curve at inference time. No re-training is required to adjust for different use-case requirements. |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 8364d9e2dd9da23789b480bdbba9e423717e42ee |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [xkeyC/whisper-large-v3-turbo-gguf](https://huggingface.co/xkeyC/whisper-large-v3-turbo-gguf) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-large-v3 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.809 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, onnx / 0.93 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | For example, to perform the task of speech transcription where the source audio is in French, and we want to return sentence-level timestamps, the following can be used: |
| README 인용 | For example, to perform the task of speech transcription  where the source audio is in French, and we want to return sentence-level timestamps, the following can be used: |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 7230f1a64fe4483b9629c665c93b52c413de34c8 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## st03 — Ollama 로 노트북에서 한국어 번역기를 돌려 보려는데, GGUF 파일 크기가 2GB 이하이고 상업적으로도 쓸 수 있는 라이선스 계열이면 좋겠어요.

- 사용자 의도: 로컬에서 가볍게 돌릴 수 있는 번역 모델
- persona / 표현: local_user / 혼합형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `commercial_status` | permitted | 상업적으로도 쓸 수 있는 라이선스 계열 | 예 |
| `max_artifact_gib` | 2 | GGUF 파일 크기가 2GB 이하 | 예 |
| `require_artifact` | gguf | Ollama 로 … GGUF | 예 |
| `tasks` | translation | 번역기 | 예 |

- **2점 기준**: 번역이 주 용도인 GGUF 모델(조건 모두 충족)
- **1점 기준**: 번역이 부가 기능인 범용 모델

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 21 | 21 | 0 | 0 | 0 | 21 | ✅ | 16 |


같은 canonical family 후보가 3개 이상: google/madlad400-3b-mt 6, tencent/Hy-MT2-1.8B 3

#### 1. [Tonic/GemmaX2-28-2B-gguf](https://huggingface.co/Tonic/GemmaX2-28-2B-gguf) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | ModelSpace/GemmaX2-28-2B-v0.1 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.614 / 8192 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.5 |
| 벤치마크 근거 | 점수 2건 저장 |
| 의미 claim (use_cases) | Real-time translation applications. |
| README 인용 | - Real-time translation applications. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 070cba10600dcdee104f24b2228ce1825b5a39e4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [enacimie/madlad400-3b-mt-Q4_K_M-GGUF](https://huggingface.co/enacimie/madlad400-3b-mt-Q4_K_M-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

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

#### 3. [fernandoruiz/madlad400-3b-mt-Q4_K_S-GGUF](https://huggingface.co/fernandoruiz/madlad400-3b-mt-Q4_K_S-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

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

#### 4. [mradermacher/Hy-MT2-1.8B-GGUF](https://huggingface.co/mradermacher/Hy-MT2-1.8B-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | tencent/Hy-MT2-1.8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.791 / 262144 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.72 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Usage |
| README 인용 | ## Usage |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | d760e9708bbded7cee9aa135b4f1dedb42ed2fc4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [mradermacher/Hy-MT2-1.8B-i1-GGUF](https://huggingface.co/mradermacher/Hy-MT2-1.8B-i1-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | tencent/Hy-MT2-1.8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.791 / 262144 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.47 |
| 벤치마크 근거 | 없음 |
| 의미 claim (documented_strengths) | translation |
| README 인용 | - translation |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 9f5c7d98d8b625800775e6197e55c7ed38f2f33a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [mradermacher/Hy-MT2-7B-i1-GGUF](https://huggingface.co/mradermacher/Hy-MT2-7B-i1-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | tencent/Hy-MT2-7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 7.505 / 262144 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.72 |
| 벤치마크 근거 | 없음 |
| 의미 claim (documented_strengths) | translation |
| README 인용 | - translation |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 9c124cc81ea701eaf374de80d0e521c4aecdb75d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [mradermacher/OmniTranslate-1.0-GGUF](https://huggingface.co/mradermacher/OmniTranslate-1.0-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | MihaiPopa-1/OmniTranslate-1.0 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.596 / 40960 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.28 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | text-generation-inference |
| README 인용 | - text-generation-inference |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | d6221fe231585bb8a781722d69c59a83476306f1 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [mradermacher/OmniTranslate-1.1-GGUF](https://huggingface.co/mradermacher/OmniTranslate-1.1-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | MihaiPopa-1/OmniTranslate-1.1 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.596 / 40960 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.28 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | text-generation-inference |
| README 인용 | - text-generation-inference |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 37b35f67dc9d81daac6a20fdedbdcf4a71d81b0d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [mradermacher/OmniTranslate-1.1-i1-GGUF](https://huggingface.co/mradermacher/OmniTranslate-1.1-i1-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | MihaiPopa-1/OmniTranslate-1.1 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.596 / 40960 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.19 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | text-generation-inference |
| README 인용 | - text-generation-inference |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 69a00d043b5a6a94d09ca13f19b163fb576a6694 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [mradermacher/Tri-1.8B-Translation-GGUF](https://huggingface.co/mradermacher/Tri-1.8B-Translation-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

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

#### 11. [mradermacher/Tri-1.8B-Translation-i1-GGUF](https://huggingface.co/mradermacher/Tri-1.8B-Translation-i1-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

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

#### 12. [mradermacher/alan-llm-jeju-dialect-v1-4b-GGUF](https://huggingface.co/mradermacher/alan-llm-jeju-dialect-v1-4b-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | est-ai/alan-llm-jeju-dialect-v1-4b (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 4.022 / 40960 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.55 |
| 벤치마크 근거 | 없음 |
| 의미 claim (documented_strengths) | translation |
| README 인용 | - translation |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 0f8ff998c7c88a59c373d24dcdeb19a9f88ba933 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [mradermacher/gaon-1.7b-v2-translate-GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | k08200/gaon-1.7b-v2-translate (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.721 / 2048 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.72 |
| 벤치마크 근거 | 없음 |
| 의미 claim (documented_strengths) | translation |
| README 인용 | ## Usage |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 303df7d2de11b00b163014b4e283eb2af68baeff |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 14. [mradermacher/gaon-1.7b-v2-translate-big-GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-big-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | k08200/gaon-1.7b-v2-translate-big (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.721 / 2048 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.72 |
| 벤치마크 근거 | 없음 |
| 의미 claim (documented_strengths) | translation |
| README 인용 | - translation |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 74ed70c266441c850d80aa95ec5d0f9b6417faed |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 15. [mradermacher/gaon-1.7b-v2-translate-i1-GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-i1-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | k08200/gaon-1.7b-v2-translate (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.721 / 2048 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.48 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Usage |
| README 인용 | ## Usage |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | afa371be1bf1e9cdc9ed1714fc8b61d213c9bbb9 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 16. [mtsdurica/madlad400-3b-mt-Q4_0-GGUF](https://huggingface.co/mtsdurica/madlad400-3b-mt-Q4_0-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

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

#### 17. [mtsdurica/madlad400-3b-mt-Q4_K_M-GGUF](https://huggingface.co/mtsdurica/madlad400-3b-mt-Q4_K_M-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

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

#### 18. [notjjustnumbers/madlad400-3b-mt-Q4_K_M-GGUF](https://huggingface.co/notjjustnumbers/madlad400-3b-mt-Q4_K_M-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

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

#### 19. [snowkitties/madlad400-3b-mt-Q4_K_M-GGUF](https://huggingface.co/snowkitties/madlad400-3b-mt-Q4_K_M-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

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

#### 20. [unsloth/Hy-MT2-1.8B-GGUF](https://huggingface.co/unsloth/Hy-MT2-1.8B-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | tencent/Hy-MT2-1.8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.791 / 262144 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.67 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Hy-MT2 Translation Task Instruction Examples (Chinese-English Comparison) |
| README 인용 | ## Hy-MT2 Translation Task Instruction Examples (Chinese-English Comparison) |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 0378cc2780f462f0fd397d0cdd244d2f769de40e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 21. [winninghealth/WiNGPT-Babel-2-GGUF](https://huggingface.co/winninghealth/WiNGPT-Babel-2-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | winninghealth/WiNGPT-Babel-2 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.614 / 8192 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.46 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is suitable for scenarios such as API internationalization and multilingual dataset preprocessing. |
| README 인용 | 3.  **Structured Data Translation:** The model can now identify and translate text fields embedded within **structured data (e.g., JSON)** while preserving the original data structure. This feature is suitable for scenarios such as API inte… |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | ff5a1e0f8086572426627890afbd0b5d2b68322f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## st04 — task 가 summarization 으로 분류된 한국어 모델 중에서 safetensors 가중치가 있는 것만 추려 줄 수 있나요?

- 사용자 의도: 요약 모델 실험 목록 만들기
- persona / 표현: researcher / 기술형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `require_artifact` | safetensors | safetensors 가중치가 있는 것 | 예 |
| `tasks` | summarization | task 가 summarization | 예 |

- **2점 기준**: 요약 task 원본 모델
- **1점 기준**: 요약 모델의 변환·재업로드

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 5 | 5 | 0 | 0 | 0 | 5 | ✅ | 0 |


#### 1. [EbanLee/kobart-summary-v3](https://huggingface.co/EbanLee/kobart-summary-v3) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | EbanLee/kobart-summary-v3 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.124 / 1026 |
| task | summarization (matched: summarization) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.46 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is used for summarization tasks. |
| README 인용 | library_name: transformers pipeline_tag: summarization tags: |
| provenance status | verified 14, not_applicable 3, documented 2, unknown 4 |
| revision | cff33231c01ed86c7f08de5c05c597b7ef2f0bfc |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [eenzeenee/t5-base-korean-summarization](https://huggingface.co/eenzeenee/t5-base-korean-summarization) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | eenzeenee/t5-base-korean-summarization (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.276 / 128 |
| task | summarization (matched: summarization) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 1.03 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for summarization tasks in the Korean language. |
| README 인용 | --- pipeline_tag: summarization language: |
| provenance status | verified 13, not_applicable 3, documented 2, unknown 5 |
| revision | 80bead40c2fa1b0f01093cb2de84f801b0bb5fe6 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [mithulaartigala/QNS-2-ReLearn-Preview](https://huggingface.co/mithulaartigala/QNS-2-ReLearn-Preview) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.5-2B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.943 / 262144 |
| task | summarization (matched: summarization) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 1.04 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: summarization |
| README 인용 | pipeline_tag: summarization --- |
| provenance status | verified 14, not_applicable 3, documented 2, unknown 4 |
| revision | 00676e07bd129cf432a2564c7e161d1dc266ec66 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [ncls-p/Qwen2.5-3B-blog-key-points](https://huggingface.co/ncls-p/Qwen2.5-3B-blog-key-points) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-3B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 3.086 / 32768 |
| task | summarization (matched: summarization) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-4.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 1.8 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Extract the key points from the following article: |
| README 인용 | ```python from transformers import AutoModelForCausalLM, AutoTokenizer  model_id = "ncls-p/Qwen2.5-3B-blog-key-points" tokenizer = AutoTokenizer.from_pretrained(model_id) model = AutoModelForCausalLM.from_pretrained(model_id)  article = """… |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | e23370d369da0caf063c1eeb8c583b95b6c150eb |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [ncls-p/Qwen2.5-7B-blog-key-points](https://huggingface.co/ncls-p/Qwen2.5-7B-blog-key-points) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-7B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.616 / 32768 |
| task | summarization (matched: summarization) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-4.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 4.36 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Extract the key points from the following article. |
| README 인용 | ```python from transformers import AutoModelForCausalLM, AutoTokenizer  model_id = "ncls-p/Qwen2.5-7B-blog-key-points" tokenizer = AutoTokenizer.from_pretrained(model_id) model = AutoModelForCausalLM.from_pretrained(model_id)  article = """… |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 71a2bff0eb2daada0f69504a4b55490b6c60be39 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## st05 — 사내 티켓 자동 분류 API 에 붙일 한국어 텍스트 분류 모델을 찾고 있어요. ONNX 파일이 있고 실행 파일 크기가 0.5GB 이하, 라이선스는 상업 이용 허용 계열이어야 합니다.

- 사용자 의도: 가벼운 상업용 분류 모델을 사내 API 로 서빙
- persona / 표현: backend_dev / 혼합형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `commercial_status` | permitted | 상업 이용 허용 계열 | 예 |
| `max_artifact_gib` | 0.5 | 실행 파일 크기가 0.5GB 이하 | 예 |
| `require_artifact` | onnx | ONNX 파일이 있고 | 예 |
| `tasks` | text-classification | 텍스트 분류 모델 | 예 |

- **2점 기준**: 조건을 모두 만족하는 분류 원본 모델
- **1점 기준**: 원본의 변환·재업로드

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 5 | 5 | 0 | 0 | 0 | 5 | ✅ | 0 |


#### 1. [NorviTech/armiger](https://huggingface.co/NorviTech/armiger) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | NorviTech/armiger (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx / 0.03 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The library is used for text classification tasks. |
| README 인용 | 0 library_name: onnx pipeline_tag: text-classification language: |
| provenance status | verified 8, not_applicable 3, documented 5, unknown 7 |
| revision | c344f7e1c43f3b11690bf12cea284a9cbb9030cd |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [NorviTech/armiger-ultra](https://huggingface.co/NorviTech/armiger-ultra) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | NorviTech/armiger-ultra (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / — |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin / 0.03 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can classify BitTorrent metadata and provide swarm estimates. |
| README 인용 | It runs on a CPU; no GPU or paid inference API is required. |
| provenance status | verified 8, not_applicable 3, documented 5, unknown 7 |
| revision | 41cb0db4c3dfce2e3866fb67d414f0ca7026af2a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [atonlee/Qoamo-PII-Decision](https://huggingface.co/atonlee/Qoamo-PII-Decision) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | skt/A.X-Encoder-base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.149 / 16384 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 0.28 |
| 벤치마크 근거 | 점수 1건 저장 |
| 의미 claim (use_cases) | The fourth and fifth examples under Usage show how. |
| README 인용 | The fourth and fifth examples under Usage show how. |
| provenance status | verified 13, not_applicable 3, documented 5, unknown 2 |
| revision | a7650cb1186f65c506dd2a7b3d80c3b6bade85e0 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [hyuckpa03/voicekeeper-klue-bert](https://huggingface.co/hyuckpa03/voicekeeper-klue-bert) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | klue/bert-base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 512 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx / 0.1 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for detecting voice phishing in Korean language. |
| README 인용 | ```python import numpy as np, onnxruntime as ort from tokenizers import Tokenizer tok = Tokenizer.from_file('tokenizer.json'); tok.enable_truncation(192) sess = ort.InferenceSession('model.onnx', providers=['CPUExecutionProvider']) e = tok.… |
| provenance status | verified 12, not_applicable 3, documented 4, unknown 4 |
| revision | d110f4a56750f33b6c29bbee1776fff7dbb681b2 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [shesettipavankumarswamy/ahd-jailbreak-v1](https://huggingface.co/shesettipavankumarswamy/ahd-jailbreak-v1) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | shesettipavankumarswamy/ahd-jailbreak-v1 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin / 0.01 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for text classification tasks. |
| README 인용 | pipeline_tag: text-classification inference: false --- |
| provenance status | verified 11, not_applicable 3, documented 5, unknown 4 |
| revision | b9290fe171d69054320af73600e1151ac9acb3ed |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## st06 — Apache-2.0 라이선스로 배포된 한국어 질의응답(question-answering) 모델이 있나요?

- 사용자 의도: 라이선스가 명확한 QA 모델 찾기
- persona / 표현: ml_engineer / 기술형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `licenses` | apache-2.0 | Apache-2.0 라이선스로 배포된 | 아니오(판정용) |
| `tasks` | question-answering | 질의응답(question-answering) | 예 |

- **2점 기준**: QA 원본 모델
- **1점 기준**: QA 모델의 변환·재업로드

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 10 | 6 | 4 | 0 | 0 | 10 | ✅ | 0 |


#### 1. [FreedomIntelligence/Apollo-MoE-0.5B](https://huggingface.co/FreedomIntelligence/Apollo-MoE-0.5B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2-0.5B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.787 / 131072 |
| task | question-answering (matched: question-answering) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.47 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is tagged for question-answering tasks. |
| README 인용 | pipeline_tag: question-answering tags: |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 2, inferred 1 |
| revision | c11162cd60e9bdcd299fe12987cc6c22b4164524 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [FreedomIntelligence/Apollo-MoE-1.5B](https://huggingface.co/FreedomIntelligence/Apollo-MoE-1.5B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | microsoft/Phi-3-mini-4k-instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.273 / 131072 |
| task | question-answering (matched: question-answering) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 4.23 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is tagged for question-answering tasks. |
| README 인용 | pipeline_tag: question-answering tags: |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 2, inferred 1 |
| revision | 42d23c6f0043697aad9510ab8431ad5e61d74b32 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [FreedomIntelligence/Apollo2-0.5B](https://huggingface.co/FreedomIntelligence/Apollo2-0.5B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2-0.5B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.63 / 131072 |
| task | question-answering (matched: question-answering) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.17 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is tagged for question-answering tasks. |
| README 인용 | pipeline_tag: question-answering tags: |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 044ffc6a510bc1fb2f7a52d5f33dd861fa718118 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [FreedomIntelligence/Apollo2-1.5B](https://huggingface.co/FreedomIntelligence/Apollo2-1.5B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2-1.5B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.777 / 131072 |
| task | question-answering (matched: question-answering) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 3.31 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is tagged for question-answering tasks. |
| README 인용 | pipeline_tag: question-answering tags: |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | c6c5f534974c47235d9dc62404e0aeee3593a2ee |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [FreedomIntelligence/Apollo2-7B](https://huggingface.co/FreedomIntelligence/Apollo2-7B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2-7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.616 / 131072 |
| task | question-answering (matched: question-answering) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.19 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is tagged for question-answering tasks. |
| README 인용 | pipeline_tag: question-answering tags: |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 2329a8bd17adc94d7e855cfa00a2227c4c33d882 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [Jackrong/Trace-Inverter-4B](https://huggingface.co/Jackrong/Trace-Inverter-4B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-4B-Instruct-2507 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 4.155 / 262144 |
| task | question-answering (matched: question-answering) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 7.74 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used as a data generation pre-processor. |
| README 인용 | From a practical usage perspective, it is best used as a "**data generation pre-processor**" or an "**intermediate component for research experiments**. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 1bee74d1a819d43aba8417813720291f12ee22c0 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [QuantFactory/Apollo2-7B-GGUF](https://huggingface.co/QuantFactory/Apollo2-7B-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2-7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Quant) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.616 / 131072 |
| task | question-answering (matched: question-answering) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 2.81 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is tagged for question-answering tasks. |
| README 인용 | pipeline_tag: question-answering tags: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 0687ffbb41684d79d99c4998eddf5c4434b888ac |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [cgus/Apollo2-7B-iMat-GGUF](https://huggingface.co/cgus/Apollo2-7B-iMat-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | FreedomIntelligence/Apollo2-7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.616 / 131072 |
| task | question-answering (matched: question-answering) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 4.13 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: question-answering |
| README 인용 | pipeline_tag: question-answering tags: |
| provenance status | verified 13, not_applicable 4, documented 5, unknown 1 |
| revision | 8faf435000f3925aaecb40c430ada8f915491ec9 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [mradermacher/IoGPT-A1-Instruct-GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | galaxyMindAiLabs/IoGPT-A1-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 23.572 / 131072 |
| task | question-answering (matched: question-answering) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 8.28 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | If you are unsure how to use GGUF files, refer to one of TheBloke's READMEs |
| README 인용 | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 9b3a7d4cc5091b05e71bb7d9dc00365438f4cac8 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [mradermacher/IoGPT-A1-Instruct-i1-GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | galaxyMindAiLabs/IoGPT-A1-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 23.572 / 131072 |
| task | question-answering (matched: question-answering) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 4.91 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for more details, including on how to concatenate multi-part files. |
| README 인용 | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 832df0fada06605a0fb9e25290eee4e0bd8b7b30 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## st07 — 8GB 그래픽카드 달린 노트북에서 llama.cpp 로 이미지 설명 모델을 돌려 보려고요. 파라미터 2B 이하 GGUF 모델 중에서 상업 이용 허용 라이선스 계열만 알려 주세요.

- 사용자 의도: 로컬 저사양 환경의 비전-언어 모델
- persona / 표현: limited_gpu / 혼합형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `commercial_status` | permitted | 상업 이용 허용 라이선스 계열 | 예 |
| `max_parameters_billion` | 2 | 파라미터 2B 이하 | 예 |
| `require_artifact` | gguf | llama.cpp 로 … GGUF 모델 | 예 |
| `tasks` | image-text-to-text | 이미지 설명 모델 | 예 |

- **2점 기준**: 이미지를 입력받아 설명하는 GGUF 모델(조건 모두 충족)
- **1점 기준**: 이미지 이해가 부가 기능인 모델
- 메모: 8GB 그래픽카드는 상황 설명일 뿐 조건으로 바꾸지 않았다(파일 크기와 VRAM 은 다르다)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 17 | 17 | 0 | 0 | 0 | 17 | ✅ | 20 |


같은 canonical family 후보가 3개 이상: Qwen/Qwen3.6-27B 3

#### 1. [Baekpica/DeepSeek-V4.1-Flash-1017-hVQ-GGUF](https://huggingface.co/Baekpica/DeepSeek-V4.1-Flash-1017-hVQ-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | deepseek-ai/DeepSeek-V4.1-Flash-1017 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.485 / — |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 0.9 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | 1-Flash-1017 |
| README 인용 | 1-Flash-1017 base_model_relation: quantized pipeline_tag: image-text-to-text language: |
| provenance status | verified 12, not_applicable 4, documented 5, unknown 2 |
| revision | 0d3cae07ac7d29dfe02c555d0782da5839f631d9 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [Baekpica/DeepSeek-V4.1-Flash-1017-iVQ-GGUF](https://huggingface.co/Baekpica/DeepSeek-V4.1-Flash-1017-iVQ-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | deepseek-ai/DeepSeek-V4.1-Flash-1017 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.485 / — |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 0.9 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | 1-Flash-1017 |
| README 인용 | 1-Flash-1017 base_model_relation: quantized pipeline_tag: image-text-to-text language: |
| provenance status | verified 12, not_applicable 4, documented 5, unknown 2 |
| revision | a533c9361d343853ac5b72706606164944da6248 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Jackrong/Qwopus3.5-9B-v3.5 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.456 / — |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 4.41 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | text-generation-inference |
| README 인용 | - text-generation-inference |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 58f9bfb45380b53ef0cbd693fce9b97b21f416ae |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [Jackrong/Qwopus3.6-27B-v2-MTP-GGUF](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2-MTP-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.6-27B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.461 / — |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 12.57 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The automation skill and complete processing pipeline scripts are open-sourced. |
| README 인용 | The automation skill and complete processing pipeline scripts are open-sourced in <a href="https://github. |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | c79f4cc5019e5de2ede577fb1d027affad3abc4e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [Mattimax/DAC6.5-GGUF](https://huggingface.co/Mattimax/DAC6.5-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Mattimax/DAC6.5 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.23 / 128000 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.14 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is designed for image-text-to-text tasks. |
| README 인용 | pipeline_tag: image-text-to-text --- |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 52693bbd1a0ca450d5e43e41f0b4979e4a192c79 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [cstr/internvl2-1b-crispembed-GGUF](https://huggingface.co/cstr/internvl2-1b-crispembed-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | OpenGVLab/InternVL2-1B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.938 / — |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.71 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is based on OpenGVLab/InternVL2-1B and is used for image-text-to-text tasks. |
| README 인용 | base_model: OpenGVLab/InternVL2-1B library_name: gguf pipeline_tag: image-text-to-text --- |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 3c5ec35f4d92b2a9f26c65139b31ea08dfd62dc1 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [developerjeremylive/Qwopus3.6-27B-v2-MTP-GGUF-etheroi](https://huggingface.co/developerjeremylive/Qwopus3.6-27B-v2-MTP-GGUF-etheroi) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.6-27B (variant=true, 종류=gguf, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.461 / — |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 10.12 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The automation skill and complete processing pipeline scripts are open-sourced. |
| README 인용 | The automation skill and complete processing pipeline scripts are open-sourced in <a href="https://github. |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 5d46f55cc8c47d4b70934700ae47e4ca2b1c4c5a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [eadx/Qwopus3.6-27B-v2-MTP-GGUF](https://huggingface.co/eadx/Qwopus3.6-27B-v2-MTP-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.6-27B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.461 / — |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 10.12 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The automation skill and complete processing pipeline scripts are open-sourced. |
| README 인용 | The automation skill and complete processing pipeline scripts are open-sourced in <a href="https://github. |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 533c2301432532518bb7ea48bb9f6ccec6fa62c0 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [fridaystreet/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF](https://huggingface.co/fridaystreet/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.8-27B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.461 / — |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 28.16 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Example use cases of modes. |
| README 인용 | EXAMPLE USE CASES OF MODES |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 13767fc565f8eee7e6e0a1b1f40b338d62e7734e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [localdeel/ko-hand-ocr-vl-GGUF](https://huggingface.co/localdeel/ko-hand-ocr-vl-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | localdeel/ko-hand-ocr-vl (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.559 / 262144 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.34 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Any prompt works ("OCR", "Read the text", Korean, or empty). |
| README 인용 | Any prompt works ("OCR", "Read the text", Korean, or empty). |
| provenance status | verified 13, not_applicable 4, documented 5, unknown 1 |
| revision | 47b99934c18b6121b1776c293767c90982f7c50a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [neureps/warmly-qwen35-08b-enko-gguf](https://huggingface.co/neureps/warmly-qwen35-08b-enko-gguf) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | neureps/Qwen3.5-0.8B-enko (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.65 / 262144 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.05 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is tagged for image-text-to-text tasks. |
| README 인용 | pipeline_tag: image-text-to-text tags: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | c3acb5a0052298a79c5509569b4c080ef29bbac4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [neureps/warmly-qwen35-2b-enko-gguf](https://huggingface.co/neureps/warmly-qwen35-2b-enko-gguf) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | neureps/Qwen3.5-2B-enko (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.677 / 262144 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.02 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is tagged for image-text-to-text tasks. |
| README 인용 | pipeline_tag: image-text-to-text tags: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | c3c06610f051c4dd119265a5ff6e7633065c81b7 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [nopesadly/GLM-OCR-Q4_K_M.gguf](https://huggingface.co/nopesadly/GLM-OCR-Q4_K_M.gguf) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | zai-org/GLM-OCR (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Q4_) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.891 / 131072 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.51 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for image-to-text tasks. |
| README 인용 | pipeline_tag: image-text-to-text --- |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | c5035b27d32155e8f04e14507b3b77721257f0b5 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 14. [sowilow/Next2-Air-DGX-Spark-GGUF](https://huggingface.co/sowilow/Next2-Air-DGX-Spark-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | sowilow/Next2-Air-DGX-Spark-GGUF (variant=false, 종류=—, 관계 근거=self, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.882 / 262144 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.18 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: image-text-to-text |
| README 인용 | pipeline_tag: image-text-to-text tags: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | e9de886b33e0ca62ce071c64c212147d32f52319 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 15. [thelamapi/next2-0.8b-GGUF](https://huggingface.co/thelamapi/next2-0.8b-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | thelamapi/next2-0.8b (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.752 / 262144 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.37 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: image-text-to-text |
| README 인용 | pipeline_tag: image-text-to-text datasets: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | eef9808de4fb3e7a53aed691145674b31a00116b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 16. [thelamapi/next2-air-GGUF](https://huggingface.co/thelamapi/next2-air-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | thelamapi/next2-air (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.882 / 262144 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.85 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Next2-Air is fully compatible with the Hugging Face transformers ecosystem and fast inference engines like vLLM and SGLang. |
| README 인용 | **Next2-Air** is fully compatible with the Hugging Face `transformers` ecosystem and fast inference engines like `vLLM` and `SGLang`. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 213820eb0e2cf0c55df9b191b6a4a8f80cd4205b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 17. [thelamapi/next2-air-i1-GGUF](https://huggingface.co/thelamapi/next2-air-i1-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | thelamapi/next2-air (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.882 / 262144 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.6 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Next2-Air is fully compatible with the Hugging Face transformers ecosystem and fast inference engines like vLLM and SGLang. |
| README 인용 | **Next2-Air** is fully compatible with the Hugging Face `transformers` ecosystem and fast inference engines like `vLLM` and `SGLang`. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | cde699b347b5b2b505ed4b1c73085304e3a19f0e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## st08 — 번역 모델 중에 컨텍스트가 32K 토큰 이상이고 파라미터 4B 이하이면서 상업 이용 허용 계열 라이선스인 걸 찾아 줘.

- 사용자 의도: 긴 입력을 받는 소형 상업용 번역 모델
- persona / 표현: ml_engineer / 기술형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `commercial_status` | permitted | 상업 이용 허용 계열 라이선스 | 예 |
| `max_parameters_billion` | 4 | 파라미터 4B 이하 | 예 |
| `min_context_length` | 32768 | 컨텍스트가 32K 토큰 이상 | 예 |
| `tasks` | translation | 번역 모델 | 예 |

- **2점 기준**: 번역 전용 원본 모델
- **1점 기준**: 번역이 부가 기능이거나 변환본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 13 | 5 | 8 | 0 | 0 | 13 | ✅ | 43 |


같은 canonical family 후보가 3개 이상: tencent/Hy-MT2-1.8B 7

#### 1. [Jour/hy-mt2-1.8b-discord](https://huggingface.co/Jour/hy-mt2-1.8b-discord) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | tencent/Hy-MT2-1.8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.791 / 262144 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 3.34 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Designed for translation tasks. |
| README 인용 | 8B language: [en, fr, es, de, pt, it, ru, ja, ko, zh, tr, ar, pl, nl] pipeline_tag: translation tags: [translation, discord, lora, formatting-preservation] --- |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 0d3e3faa93a18aae5ba53856b9cb057a8363031e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [NiuTrans/LMT-60-0.6B](https://huggingface.co/NiuTrans/LMT-60-0.6B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | NiuTrans/LMT-60-0.6B-Base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.752 / 131072 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.4 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for translation tasks, as demonstrated in the provided code example. |
| README 인용 | pipeline_tag: translation library_name: transformers --- |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | dd189845cdc73346cef33c7a94f4b8bd8efdd4eb |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [NiuTrans/LMT-60-1.7B](https://huggingface.co/NiuTrans/LMT-60-1.7B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | NiuTrans/LMT-60-1.7B-Base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.032 / 131072 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 3.78 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for translation tasks, specifically from English to Chinese. |
| README 인용 | pipeline_tag: translation library_name: transformers --- |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | c468e3f82f71d3f5d112ebbbfcec8f0ee0bb6cdb |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [Poirott/Oshi-Translate-Magshot-GGUF](https://huggingface.co/Poirott/Oshi-Translate-Magshot-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | tencent/Hy-MT2-1.8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.791 / 262144 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 16.09 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Real-time translation of finalized ASR segments from livestreams and VODs |
| README 인용 | - Real-time translation of finalized ASR segments from livestreams and VODs |
| provenance status | verified 13, not_applicable 4, documented 5, unknown 1 |
| revision | ded25564817ba7a9afce834450947258c84b8a15 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [mlx-community/Hy-MT2-1.8B-Abliterated-8bit](https://huggingface.co/mlx-community/Hy-MT2-1.8B-Abliterated-8bit) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | tencent/Hy-MT2-1.8B (variant=true, 종류=mlx, 관계 근거=base_model_tag, 변환 표지=mlx) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.791 / 262144 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.77 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is intended for lower memory usage on Apple Silicon. |
| README 인용 | The 8-bit version is intended for lower memory usage on Apple Silicon. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 6c42ca3daccb0914a6035f379e18e3f4eda3c575 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [mradermacher/Hy-MT2-1.8B-GGUF](https://huggingface.co/mradermacher/Hy-MT2-1.8B-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | tencent/Hy-MT2-1.8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.791 / 262144 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.72 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Usage |
| README 인용 | ## Usage |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | d760e9708bbded7cee9aa135b4f1dedb42ed2fc4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [mradermacher/Hy-MT2-1.8B-i1-GGUF](https://huggingface.co/mradermacher/Hy-MT2-1.8B-i1-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | tencent/Hy-MT2-1.8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.791 / 262144 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.47 |
| 벤치마크 근거 | 없음 |
| 의미 claim (documented_strengths) | translation |
| README 인용 | - translation |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 9f5c7d98d8b625800775e6197e55c7ed38f2f33a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [mradermacher/OmniTranslate-1.0-GGUF](https://huggingface.co/mradermacher/OmniTranslate-1.0-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | MihaiPopa-1/OmniTranslate-1.0 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.596 / 40960 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.28 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | text-generation-inference |
| README 인용 | - text-generation-inference |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | d6221fe231585bb8a781722d69c59a83476306f1 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [mradermacher/OmniTranslate-1.1-GGUF](https://huggingface.co/mradermacher/OmniTranslate-1.1-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | MihaiPopa-1/OmniTranslate-1.1 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.596 / 40960 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.28 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | text-generation-inference |
| README 인용 | - text-generation-inference |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 37b35f67dc9d81daac6a20fdedbdcf4a71d81b0d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [mradermacher/OmniTranslate-1.1-i1-GGUF](https://huggingface.co/mradermacher/OmniTranslate-1.1-i1-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | MihaiPopa-1/OmniTranslate-1.1 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.596 / 40960 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.19 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | text-generation-inference |
| README 인용 | - text-generation-inference |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 69a00d043b5a6a94d09ca13f19b163fb576a6694 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [sappho192/gemma3-multilingual-translator-270m](https://huggingface.co/sappho192/gemma3-multilingual-translator-270m) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | google/gemma-3-270m (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.268 / 32768 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 0.5 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Translate Korean to English |
| README 인용 | ```python import torch from transformers import AutoTokenizer, AutoModelForCausalLM  # Load model model = AutoModelForCausalLM.from_pretrained(     "sappho192/gemma3-multilingual-translator-270m",     torch_dtype=torch.bfloat16,     device_… |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 9c1b01f020baf00e64ea1649b897dae745dfe23d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | tencent/Hy-MT2-1.8B (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.039 / 262144 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 3.8 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Hy-MT2 can be used for translating text in various languages, as demonstrated in the provided instruction examples. |
| README 인용 | ## Hy-MT2 Translation Task Instruction Examples (Chinese-English Comparison) |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 9a341cd1b679d3efd23b46e847b01745a71ed792 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [unsloth/Hy-MT2-1.8B-GGUF](https://huggingface.co/unsloth/Hy-MT2-1.8B-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | tencent/Hy-MT2-1.8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.791 / 262144 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.67 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Hy-MT2 Translation Task Instruction Examples (Chinese-English Comparison) |
| README 인용 | ## Hy-MT2 Translation Task Instruction Examples (Chinese-English Comparison) |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 0378cc2780f462f0fd397d0cdd244d2f769de40e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## st09 — Gemma 라이선스로 배포된 4B 이하 한국어 텍스트 생성 모델을 비교해 보고 싶어요.

- 사용자 의도: 특정 라이선스 계열의 소형 생성 모델 목록
- persona / 표현: researcher / 기술형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `licenses` | gemma | Gemma 라이선스로 배포된 | 아니오(판정용) |
| `max_parameters_billion` | 4 | 4B 이하 | 예 |
| `tasks` | text-generation | 텍스트 생성 모델 | 예 |

- **2점 기준**: 조건을 만족하는 생성 원본 모델
- **1점 기준**: 변환·양자화·재업로드

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 15 | 4 | 11 | 0 | 0 | 15 | ✅ | 2 |


같은 canonical family 후보가 3개 이상: UmbrellaInc/Albert_Wesker-1B 3

#### 1. [EXAiStudio/EX-Ai1-3.88B-Gemma3](https://huggingface.co/EXAiStudio/EX-Ai1-3.88B-Gemma3) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | google/gemma-3-4b-it (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 3.88 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 2.32 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Translation and multilingual text assistance, subject to language-specific performance. |
| README 인용 | - Translation and multilingual text assistance, subject to language-specific performance. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | d2b50c96cc71eb29e8c4fa0355298ba356d36462 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [Flexan/UmbrellaInc-Albert_Wesker-1B-GGUF](https://huggingface.co/Flexan/UmbrellaInc-Albert_Wesker-1B-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | UmbrellaInc/Albert_Wesker-1B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.0 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.64 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | all use cases |
| README 인용 | - all use cases |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | cd298f1d0a8676fb1816435b24744b76974f830e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [Sky-Kim/gemma3-270m-IT-ConvFill-EnKo](https://huggingface.co/Sky-Kim/gemma3-270m-IT-ConvFill-EnKo) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | vysri/gemma3-270m-IT-ConvFill (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.268 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.5 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for generating responses in natural spoken Korean. |
| README 인용 | co/vysri/gemma3-270m-IT-ConvFill) (English) further fine-tuned on the Korean translation of the ConvFill data plus English replay, so it now answers Korean users in natural spoken Korean while keeping English. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 427d7538e652ccb63ba11e3939e423513ac88fe4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [andreass123/gemma-2b-translation-v0.150-Q4_K_M-GGUF](https://huggingface.co/andreass123/gemma-2b-translation-v0.150-Q4_K_M-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | lemon-mint/gemma-ko-1.1-2b-it (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Q4_) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.506 / 8192 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.52 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used with llama.cpp for translation tasks. |
| README 인용 | ```bash llama-cli --hf-repo andreass123/gemma-2b-translation-v0.150-Q4_K_M-GGUF --model gemma-2b-translation-v0.150.Q4_K_M.gguf -p "The meaning to life and the universe is" ``` |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | c0ad2a0bc72390cb4bda4b66a8829ad1af39b31d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [hwihwalab/dama-kurong-solopreneur-ko](https://huggingface.co/hwihwalab/dama-kurong-solopreneur-ko) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | google/gemma-2-2b-it (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.614 / 8192 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 3.18 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for business strategy queries, such as prioritizing core MVP features. |
| README 인용 | \| **Business Strategy (MVP)** \| `첫 출시용 최소 기능 고르는 법 알려줘`<br>`How to prioritize core MVP features` \| Core feature selection & launch scope pruning \| |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | ce53b36bc03234eaf883a306be15780e2a48bfaa |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [inboxpraveen/Kavach-PII-270M](https://huggingface.co/inboxpraveen/Kavach-PII-270M) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | google/gemma-3-270m-it (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.268 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.56 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Extract all personal data (PII/PHI/PCI) from the text. |
| README 인용 | --- license: gemma base_model: google/gemma-3-270m-it new_version: inboxpraveen/Kavach-PII-270M library_name: transformers pipeline_tag: text-generation tags: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | a7a942f5b5a13df13a86ae1bb72281e266caabb3 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [inboxpraveen/Kavach-PII-270M-GGUF](https://huggingface.co/inboxpraveen/Kavach-PII-270M-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | inboxpraveen/Kavach-PII-270M-GGUF (variant=false, 종류=—, 관계 근거=self, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.268 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.23 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Usage |
| README 인용 | ## Usage |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | a2c09e8a92a12c99f5a7e7085fd7d5863f52b8ac |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [mradermacher/Albert_Wesker-1B-GGUF](https://huggingface.co/mradermacher/Albert_Wesker-1B-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | UmbrellaInc/Albert_Wesker-1B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.0 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.64 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | all use cases |
| README 인용 | - all use cases |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 148355f178074b602997e66afdbade122a639f70 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [mradermacher/Albert_Wesker-1B-i1-GGUF](https://huggingface.co/mradermacher/Albert_Wesker-1B-i1-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | UmbrellaInc/Albert_Wesker-1B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.0 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.6 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | all use cases |
| README 인용 | - all use cases |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 97d3f7be29d60f399359541755ef333d2ce56223 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [mradermacher/Gemma3.Novaciano-1B-GGUF](https://huggingface.co/mradermacher/Gemma3.Novaciano-1B-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | NovaCorp/Gemma3.Novaciano-1B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.0 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.64 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | all use cases |
| README 인용 | - all use cases |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 06db65f6925d58272132ec5b6edfc14da7423b54 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [mradermacher/Gemma3.Novaciano-1B-i1-GGUF](https://huggingface.co/mradermacher/Gemma3.Novaciano-1B-i1-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | NovaCorp/Gemma3.Novaciano-1B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.0 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.6 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | all use cases |
| README 인용 | - all use cases |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 1d1d2a1ae4d113bd7219f6804c557b29bccbeb89 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [mradermacher/Hans_Wesker-1B-GGUF](https://huggingface.co/mradermacher/Hans_Wesker-1B-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | UmbrellaInc/Hans_Wesker-1B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.0 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.64 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | all use cases |
| README 인용 | - all use cases |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 215e53bb3cc0054ed728b92fa4a1a8254d24e401 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [mradermacher/Hans_Wesker-1B-i1-GGUF](https://huggingface.co/mradermacher/Hans_Wesker-1B-i1-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | UmbrellaInc/Hans_Wesker-1B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.0 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.6 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | all use cases |
| README 인용 | - all use cases |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | d555be7d938b6e09dac90415078e14933ff3b97a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 14. [mradermacher/KONI-4B-instruct-20250901-GGUF](https://huggingface.co/mradermacher/KONI-4B-instruct-20250901-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | KISTI-KONI/KONI-4B-instruct-20250901 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 3.88 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.61 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for more details, including on how to concatenate multi-part files. |
| README 인용 | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 9b272e42e5fc2e17e0110247328e36722f1111b6 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 15. [skkw1128/schedule-extractor-gemma3-270m-mlx](https://huggingface.co/skkw1128/schedule-extractor-gemma3-270m-mlx) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | google/gemma-3-270m-it (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=mlx) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.102 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.11 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for text generation tasks in Korean. |
| README 인용 | --- license: gemma base_model: google/gemma-3-270m-it language: [ko] pipeline_tag: text-generation tags: [mlx, on-device, schedule-extraction] --- |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 1843880cb006596b90f29cde504534e8d29de35b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## st10 — 브라우저 확장 프로그램 안에 넣을 아주 가벼운 한국어 텍스트 생성 모델이 필요해요. ONNX 로 배포돼 있고 파라미터 1B 이하, 상업적으로 써도 되는 라이선스 계열이어야 해요.

- 사용자 의도: 클라이언트 측에서 돌릴 초소형 생성 모델
- persona / 표현: startup_dev / 혼합형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `commercial_status` | permitted | 상업적으로 써도 되는 라이선스 계열 | 예 |
| `max_parameters_billion` | 1 | 파라미터 1B 이하 | 예 |
| `require_artifact` | onnx | ONNX 로 배포돼 있고 | 예 |
| `tasks` | text-generation | 텍스트 생성 모델 | 예 |

- **2점 기준**: 조건을 모두 만족하는 ONNX 생성 모델
- **1점 기준**: 생성이 부가 기능인 모델

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 3 | 3 | 0 | 0 | 0 | 3 | ✅ | 4 |


#### 1. [bigscience/mt0-base](https://huggingface.co/bigscience/mt0-base) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | bigscience/mt0-base (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.582 / — |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 2.17 |
| 벤치마크 근거 | 점수 50건 저장 |
| 의미 claim (use_cases) | For example, given the prompt "Translate to English: Je t’aime." |
| README 인용 | For example, given the prompt "*Translate to English: Je t’aime. |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 0c500042c1f80b6b6ec208cf73d9ee43f1dac245 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [bigscience/mt0-small](https://huggingface.co/bigscience/mt0-small) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | bigscience/mt0-small (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.3 / — |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin, safetensors / 1.12 |
| 벤치마크 근거 | 점수 50건 저장 |
| 의미 claim (use_cases) | For example, given the prompt "Translate to English: Je t’aime." |
| README 인용 | For example, given the prompt "*Translate to English: Je t’aime. |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 8116a34237e19160ec003147e758f065876d95f0 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [uneeverse/unee-0.8b](https://huggingface.co/uneeverse/unee-0.8b) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `filter_metadata` — 하드 필터 조건만으로 판정

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.5-0.8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.752 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 1.4 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for decision-making tasks. |
| README 인용 | 0 pipeline_tag: text-generation tags: [decision-model, classification, chatbot, rag, multilingual, on-device, webgpu, transformers. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 60dfd958dc92a6065ab6987ee0de7ba51bfac09b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______
