# 골든셋 v3 검수 워크시트 — semantic_capability (의미 능력)

> 상태: **초안 + 전수 스캔 + 검수 준비 완료**. 아래 점수는 Claude 의 제안이며 정답이 아니다.
>
> 판정 입력: `python test/golden/v3/tools/judge.py <query_id> <model_id> --decision approve|2|1|exclude|hold --reason "…" --by <이름>`

## sc01 — 병원 원무과 직원들이 의료법이나 건강보험 규정을 물어볼 수 있는 사내 Q&A 챗봇을 기획 중이에요. 이런 한국 의료 법규를 학습한 모델이 있을까요?

- 사용자 의도: 한국 의료 법규 특화 대화 모델
- persona / 표현: korean_service_planner / 목적형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `tasks` | text-generation | Q&A 챗봇 | 예 |

- **2점 기준**: 한국 의료법·의료 규정 데이터로 학습됐다고 명시된 모델
- **1점 기준**: 의료 법규를 부가적으로 다루거나 해당 모델의 변환본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 2,346 | 3 | 0 | 2,342 | 1 | 4 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 2,342 | RedHatAI/granite-3.1-8b-instruct-FP8-dynamic, ginigen-ai/Rogue-27B-KR, teddylee777/ghost-8b-beta-1608-gguf |

#### 1. [aigensciences/Meerkat2-14B](https://huggingface.co/aigensciences/Meerkat2-14B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — cluding carefully curated question-answer pairs from Korean medical statutes. Evaluations were run with [EvalScope](https://github. Gen

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-14B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 14.768 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 27.51 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Pick 30B-A3B if inference cost matters most, since it reaches Korean licensing accuracy comparable to Qwen3-235B-A22B while activating only 3B parameters. |
| README 인용 | Pick 30B-A3B if inference cost matters most, since it reaches Korean licensing accuracy comparable to Qwen3-235B-A22B while activating only 3B parameters. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | b4c0415d2f276da9a0347b7f5160f32fe3522b2c |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [aigensciences/Meerkat2-30B-A3B](https://huggingface.co/aigensciences/Meerkat2-30B-A3B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — cluding carefully curated question-answer pairs from Korean medical statutes. A refusal subset is included in the training mixture to r

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-30B-A3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 30.532 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 56.87 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Pick 30B-A3B if inference cost matters most, since it reaches Korean licensing accuracy comparable to Qwen3-235B-A22B while activating only 3B parameters. |
| README 인용 | Pick 30B-A3B if inference cost matters most, since it reaches Korean licensing accuracy comparable to Qwen3-235B-A22B while activating only 3B parameters. |
| provenance status | verified 12, not_applicable 3, documented 4, unknown 4 |
| revision | 65a218fbb062ae5f4308eb968041c88da3f92885 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [aigensciences/Meerkat2-32B](https://huggingface.co/aigensciences/Meerkat2-32B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — parameters. Example usage includes querying about domestic medical law. General-domain capability is preserved but not improved. S

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-32B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 32.762 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 61.02 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Meerkat2 does not lose accuracy when answering in Korean. |
| README 인용 | ` Unlike the base models, Meerkat2 does not lose accuracy when answering in Korean. |
| provenance status | verified 12, not_applicable 3, documented 4, unknown 4 |
| revision | 56c0bde1025a2b35f4f8fa57a9ba93a55a21a3d7 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [joongi007/ktdsbaseLM-v0.13-onbased-llama3.1-GGUF](https://huggingface.co/joongi007/ktdsbaseLM-v0.13-onbased-llama3.1-GGUF) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — 1 license: apache-2. ### Example(`Q4_K_M`)  ``` user : 「국민건강보험법」제44조, 「국민건강보험법 시행령」제19조,「약관의 규제에 관한 법률」제5조, 「상법」제54조 참조 판단

| 항목 | 값 |
|---|---|
| canonical model | AIDX-ktds/ktdsbaseLM-v0.13-onbased-llama3.1 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 8.03 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 2.96 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for generating legal text based on specific laws and regulations. |
| README 인용 | 0 pipeline_tag: text-generation language: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | bc0e67ed82e83b42b11143cd64f8bbdac39f8553 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## sc02 — 주식 앱에서 금융 뉴스 기사가 호재인지 악재인지 자동으로 나눠 보여 주고 싶어요. 이런 데 쓸 한국어 모델이 있나요?

- 사용자 의도: 금융 뉴스 감성(극성) 분류
- persona / 표현: startup_dev / 목적형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `tasks` | text-classification | 나눠 보여 주고(분류) | 예 |

- **2점 기준**: 금융 텍스트 감성 분류용으로 학습된 한국어 모델
- **1점 기준**: 다국어 금융 감성 모델, 또는 금융 특화가 불명확한 감성 모델의 변환본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 157 | 2 | 2 | 153 | 0 | 4 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 153 | anphu16-do-huu/xlmr-sentiment-en-es-zh-ko, chaoliangUNSW/Jev-Style-0.8B-Decision-v3-GGUF, quevirus/Xevn-4B-GGUF |

#### 1. [DataWizardd/finbert-sentiment-ko](https://huggingface.co/DataWizardd/finbert-sentiment-ko) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — DataWizardd/finbert-sentiment-ko

| 항목 | 값 |
|---|---|
| canonical model | DataWizardd/finbert-sentiment-ko (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.101 / 512 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.38 |
| 벤치마크 근거 | 점수 1건 저장 |
| 의미 claim (use_cases) | The model can be used for text classification tasks such as sentiment analysis. |
| README 인용 | ```python from transformers import pipeline  pipe = pipeline("text-classification", model="DataWizardd/finbert-sentiment-ko")  pipe("환율이 급등하며 시장 불안이 커지고 있다.") # 출력: [{'label': '부정', 'score': 0.95}] |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 27bafa1fe415348019066b48570ed3093abdfa89 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [Kenpache/multilingual-financial-sentiment-v2](https://huggingface.co/Kenpache/multilingual-financial-sentiment-v2) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `model_id` — Kenpache/multilingual-financial-sentiment-v2

| 항목 | 값 |
|---|---|
| canonical model | Kenpache/multilingual-financial-sentiment-v2 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.56 / 514 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 2.09 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can classify financial sentiment in multiple languages by using language prefixes for accurate results. |
| README 인용 | \| Use case \| Prefix \| |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | c30694963b59cc5477f94f0c0d460fffe1cba0ee |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [snunlp/KR-FinBert-SC](https://huggingface.co/snunlp/KR-FinBert-SC) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — ence sample Positive and Negative classification Example of sentiment analysis results Performance improvement through domain ada

| 항목 | 값 |
|---|---|
| canonical model | snunlp/KR-FinBert-SC (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 512 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.38 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Inference sample |
| README 인용 | ### Inference sample |
| provenance status | verified 12, not_applicable 3, documented 2, unknown 6 |
| revision | f8586286cc3161fb648e9fee09a456069fd846d0 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [tabularisai/multilingual-sentiment-analysis](https://huggingface.co/tabularisai/multilingual-sentiment-analysis) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `model_id` — tabularisai/multilingual-sentiment-analysis

| 항목 | 값 |
|---|---|
| canonical model | distilbert/distilbert-base-multilingual-cased (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.135 / 512 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.5 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for sentiment analysis across multiple languages. |
| README 인용 | Below is a Python example on how to use the multilingual sentiment model without pipelines: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | eea032081f8d247b4303ef3565e7cec1b6f201c9 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## sc03 — 커뮤니티 댓글에서 욕설이나 혐오 표현을 자동으로 걸러내는 기능을 만들고 있어요. 쓸 만한 한국어 모델 있나요?

- 사용자 의도: 유해 표현 탐지
- persona / 표현: backend_dev / 목적형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `tasks` | text-classification | 걸러내는(분류) 기능 | 예 |

- **2점 기준**: 욕설·혐오 표현 탐지용으로 학습된 한국어 분류 모델
- **1점 기준**: 다국어 유해성 분류 모델이거나 편향·성별 편향처럼 인접 범주만 다루는 모델

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 157 | 1 | 15 | 139 | 2 | 18 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 139 | BigBigBe/ynat-model, ejsong25/ynat-model, querypieai/QEV1.1-9B-8BIT |

같은 canonical family 후보가 3개 이상: jhu-clsp/mmBERT-base 4

#### 1. [Horizon-Labs/content-safety-guard-base](https://huggingface.co/Horizon-Labs/content-safety-guard-base) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — it flags fewer safe-but-scary prompts (XSTest 28% -> 21%); ToxicChat F1 is 0.012 lower, other rows move by 0.01 or less. ```

| 항목 | 값 |
|---|---|
| canonical model | jhu-clsp/mmBERT-base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.308 / 8192 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 1.15 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | A user prompt scores unsafe for a query about making a fake ID. |
| README 인용 | ```python from transformers import pipeline  clf = pipeline("text-classification", model="Horizon-Labs/content-safety-guard-base", top_k=None)  # a user prompt scores = {d["label"]: d["score"] for d in clf("How can I make a fake ID that pas… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 414bd921fd5ec43632b70240db895af33a2e22c3 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [Horizon-Labs/multilingual-hate-speech-base](https://huggingface.co/Horizon-Labs/multilingual-hate-speech-base) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `model_id` — Horizon-Labs/multilingual-hate-speech-base

| 항목 | 값 |
|---|---|
| canonical model | jhu-clsp/mmBERT-base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.308 / 8192 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 1.15 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | from transformers import pipeline  clf = pipeline("text-classification", model="Horizon-Labs/multilingual-hate-speech-base", top_k=None) print(clf("Die sind alle Ungeziefer, schmeißt sie raus.")) # [[{'label': 'hate', 'score': ...}, {'label… |
| README 인용 | ```python from transformers import pipeline  clf = pipeline("text-classification", model="Horizon-Labs/multilingual-hate-speech-base", top_k=None) print(clf("Die sind alle Ungeziefer, schmeißt sie raus.")) # [[{'label': 'hate', 'score': ...… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 9ee208ff8052f676bdd53fba82d90d8e4a0f9ead |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [Horizon-Labs/multilingual-toxicity-base](https://huggingface.co/Horizon-Labs/multilingual-toxicity-base) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `model_id` — Horizon-Labs/multilingual-toxicity-base

| 항목 | 값 |
|---|---|
| canonical model | jhu-clsp/mmBERT-base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.308 / 8192 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 1.15 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | It can be used for text classification in multiple languages. |
| README 인용 | ```python from transformers import pipeline  clf = pipeline("text-classification", model="Horizon-Labs/multilingual-toxicity-base", top_k=None) print(clf("Halt die Klappe, du Vollidiot.")) # [[{'label': 'toxicity', 'score': ...}, {'label': … |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 3ed527edbce089f6a9a6bff34151c88e281c97e6 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [Horizon-Labs/multilingual-toxicity-small](https://huggingface.co/Horizon-Labs/multilingual-toxicity-small) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `model_id` — Horizon-Labs/multilingual-toxicity-small

| 항목 | 값 |
|---|---|
| canonical model | jhu-clsp/mmBERT-small (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.141 / 8192 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 0.52 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | It can be used for text classification in moderation tasks. |
| README 인용 | ```python from transformers import pipeline  clf = pipeline("text-classification", model="Horizon-Labs/multilingual-toxicity-small", top_k=None) print(clf("Halt die Klappe, du Vollidiot.")) # [[{'label': 'toxicity', 'score': ...}, {'label':… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 4742b1ba339a57dfd0af47c47bcb51dda7a39441 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [LatentAILabs/laya-indic](https://huggingface.co/LatentAILabs/laya-indic) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음; 다국어·범용 모델
- 근거 위치: `technical_metadata` — icardoRei/wmt-da-human-evaluation ucberkeley-dlab/measuring-hate-speech ibm-research/argument_quality_ranking_30k CohereLabs/aya_re

| 항목 | 값 |
|---|---|
| canonical model | jhu-clsp/mmBERT-base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.322 / — |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.6 |
| 벤치마크 근거 | 점수 11건 저장 |
| 의미 claim (use_cases) | The model is designed for text classification tasks. |
| README 인용 | 0 library_name: thx01 pipeline_tag: text-classification base_model: jhu-clsp/mmBERT-base language: [en, hi, bn, ta, te, mr, gu, kn, ml, pa, ur, or, az, kk, uz, ka, tr, fa, ru, de, fr, es, ar, zh, ja, ko, multilingual] datasets: |
| provenance status | verified 13, not_applicable 3, documented 5, unknown 2 |
| revision | 2936da26cfa3c541abf90f7ca25eca122d0ab1fc |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [Verm1ion/injection-sentry-xlmr](https://huggingface.co/Verm1ion/injection-sentry-xlmr) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음; 다국어·범용 모델
- 근거 위치: `technical_metadata` — base_models  datasets Lakera/mosscap_prompt_injection ToxicityPrompts/PolyGuardMix walledai/MultiJail hackaprompt/hackapro

| 항목 | 값 |
|---|---|
| canonical model | Verm1ion/injection-sentry-xlmr (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.278 / 514 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.04 |
| 벤치마크 근거 | 점수 1건 저장 |
| 의미 claim (use_cases) | Detecting prompt injection attacks in LLM-powered applications. |
| README 인용 | Detecting prompt injection attacks in LLM-powered applications. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 4eaf9b46261c75771c30304509ce8cb22a0df620 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [abacusai/Smaug-Toxicity-Perspective](https://huggingface.co/abacusai/Smaug-Toxicity-Perspective) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `model_id` — abacusai/Smaug-Toxicity-Perspective

| 항목 | 값 |
|---|---|
| canonical model | jhu-clsp/mmBERT-base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.308 / 8192 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 1.15 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for text classification tasks involving toxicity detection. |
| README 인용 | ```bash docker run -p 8080:80 ghcr.io/huggingface/text-embeddings-inference:cpu-1.9 --model-id abacusai/Smaug-Toxicity-Perspective curl -s localhost:8080/predict -H 'Content-Type: application/json' \   -d '{"inputs": "You are an idiot", "ra… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 7c413b7a5653f3921cd6b105e797efa5a2261223 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [astroware/HaloGuard1-Gen-0.8B](https://huggingface.co/astroware/HaloGuard1-Gen-0.8B) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — xual_content_general self_harm_and_suicide eating_disorders hate_speech harassment_and_bullying bias_and_stereotyping general defam

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.5-0.8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.107 / 262144 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 2.06 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: text-classification |
| README 인용 | pipeline_tag: text-classification tags: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 85ff68dd063a7e58487a4251824fd36a20977d5c |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [autopilot-ai/EthicalEye](https://huggingface.co/autopilot-ai/EthicalEye) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `semantic_metadata` — tically flag and block user-generated content that contains abusive language, hate speech, or other forms of harmful or unethical behavi

| 항목 | 값 |
|---|---|
| canonical model | autopilot-ai/EthicalEye (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.278 / 514 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 1.04 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The Ethical Eye model is primarily intended to be used as a tool to flag or block users exhibiting harmful or unethical behavior on various platforms. It aims to assist developers, especially those with limited experience in NLP, in enforci… |
| README 인용 | - Primary Use Case: The Ethical Eye model is primarily intended to be used as a tool to flag or block users exhibiting harmful or unethical behavior on various platforms. It aims to assist developers, especially those with limited experienc… |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | df176226d426e668a23002210c68a502f6845d93 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [desert-ant-labs/toxic](https://huggingface.co/desert-ant-labs/toxic) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `model_id` — desert-ant-labs/toxic

| 항목 | 값 |
|---|---|
| canonical model | desert-ant-labs/toxic (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 8192 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, pytorch_bin / 0.09 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: text-classification |
| README 인용 | pipeline_tag: text-classification --- |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | bc5f0e8faa6fbb231275b6076fbb04a9b48ddcc4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [knowledgator/opir-multitask-multilang-v1.0](https://huggingface.co/knowledgator/opir-multitask-multilang-v1.0) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `semantic_metadata` — nto multiple safety categories. The model can be applied to toxicity classification tasks. 30 ms p50 latency, making it the fast

| 항목 | 값 |
|---|---|
| canonical model | knowledgator/opir-multitask-multilang-v1.0 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.28 / — |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.04 |
| 벤치마크 근거 | 점수 21건 저장 |
| 의미 claim (use_cases) | The model can be used for binary safe/unsafe classification. |
| README 인용 | ```python from gliclass import GLiClassModel, ZeroShotClassificationPipeline from transformers import AutoTokenizer  MODEL_ID = "knowledgator/opir-multitask-multilang-v1.0" DEVICE = "cuda:0"  # use "cpu" if you are not running on GPU  model… |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 1c1d66bd22e0ba93a435c710a9d9499be292cd65 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [monologg/koelectra-base-bias](https://huggingface.co/monologg/koelectra-base-bias) — Claude 제안: **1점**

- 제안 이유: 2점 조건(전용·명시 용도) 근거 없음
- 근거 위치: `model_id` — monologg/koelectra-base-bias

| 항목 | 값 |
|---|---|
| canonical model | monologg/koelectra-base-bias (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 512 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | stage1:korean_name_strong |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.42 |
| 벤치마크 근거 | 없음 |
| 의미 claim (—) | — |
| README 인용 | — |
| provenance status | verified 11, not_applicable 3, documented 1, unknown 8 |
| revision | ad522394a2a50ef6f9972edda7c064466721a882 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [monologg/koelectra-base-gender-bias](https://huggingface.co/monologg/koelectra-base-gender-bias) — Claude 제안: **1점**

- 제안 이유: 2점 조건(전용·명시 용도) 근거 없음
- 근거 위치: `model_id` — monologg/koelectra-base-gender-bias

| 항목 | 값 |
|---|---|
| canonical model | monologg/koelectra-base-gender-bias (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 512 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | stage1:korean_name_strong |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.42 |
| 벤치마크 근거 | 없음 |
| 의미 claim (—) | — |
| README 인용 | — |
| provenance status | verified 11, not_applicable 3, documented 1, unknown 8 |
| revision | 41590feeddbd97f576763071bbbb42c53a3bb0e5 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 14. [monologg/koelectra-base-v3-bias](https://huggingface.co/monologg/koelectra-base-v3-bias) — Claude 제안: **1점**

- 제안 이유: 2점 조건(전용·명시 용도) 근거 없음
- 근거 위치: `model_id` — monologg/koelectra-base-v3-bias

| 항목 | 값 |
|---|---|
| canonical model | monologg/koelectra-base-v3-bias (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 512 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | stage1:korean_name_strong |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.42 |
| 벤치마크 근거 | 없음 |
| 의미 claim (—) | — |
| README 인용 | — |
| provenance status | verified 11, not_applicable 3, documented 1, unknown 8 |
| revision | 79ee034c1b9fd115b58595e4f32d8437f3b4b80b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 15. [monologg/koelectra-base-v3-gender-bias](https://huggingface.co/monologg/koelectra-base-v3-gender-bias) — Claude 제안: **1점**

- 제안 이유: 2점 조건(전용·명시 용도) 근거 없음
- 근거 위치: `model_id` — monologg/koelectra-base-v3-gender-bias

| 항목 | 값 |
|---|---|
| canonical model | monologg/koelectra-base-v3-gender-bias (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 512 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | stage1:korean_name_strong |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.42 |
| 벤치마크 근거 | 없음 |
| 의미 claim (—) | — |
| README 인용 | — |
| provenance status | verified 11, not_applicable 3, documented 1, unknown 8 |
| revision | 82740c59c74355d844ff9017271f2e0a608ff3da |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 16. [monologg/koelectra-base-v3-hate-speech](https://huggingface.co/monologg/koelectra-base-v3-hate-speech) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — monologg/koelectra-base-v3-hate-speech

| 항목 | 값 |
|---|---|
| canonical model | monologg/koelectra-base-v3-hate-speech (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 512 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | stage1:korean_name_strong |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.42 |
| 벤치마크 근거 | 없음 |
| 의미 claim (—) | — |
| README 인용 | — |
| provenance status | verified 11, not_applicable 3, documented 1, unknown 8 |
| revision | 8938df1530df593b9fce6926d1ff963ad07d23a3 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 17. [musubilabs/policylm-1.7b](https://huggingface.co/musubilabs/policylm-1.7b) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음; 다국어·범용 모델
- 근거 위치: `technical_metadata` — Safety-Guard-Dataset-v3 Alibaba-AAIG/XGuard-Train-Open-200K ToxicityPrompts/PolyGuardMix metrics  model architectures  context_e

| 항목 | 값 |
|---|---|
| canonical model | BidirLM/BidirLM-1.7B-Embedding (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.728 / — |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 3.24 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Can be used to test policy changes on example messages. |
| README 인용 | - **Test policy changes on example messages.** Not every edit changes the decision: about 1 in 2 single-clause edits did on our benchmark, at the balanced cutoff. |
| provenance status | verified 11, not_applicable 3, documented 5, unknown 4 |
| revision | b3b2cd408a08a68ab6a30c1fc1e440204e44d57e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 18. [vllm-sr/Vela-1.0-Encoder-307M-Shield](https://huggingface.co/vllm-sr/Vela-1.0-Encoder-307M-Shield) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음; 다국어·범용 모델
- 근거 위치: `technical_metadata` — er-307M datasets nvidia/Aegis-AI-Content-Safety-Dataset-2.0 ToxicityPrompts/PolyGuardMix nvidia/Nemotron-Safety-Guard-Dataset-v3

| 항목 | 값 |
|---|---|
| canonical model | vllm-sr/Vela-1.0-Encoder-307M (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.308 / 32768 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 2.34 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is used for text classification tasks. |
| README 인용 | 0 pipeline_tag: text-classification base_model: vllm-sr/Vela-1. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 812f2b07bd22112ad212d9a591a6bd4de3e76c14 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## sc04 — 주민센터 민원 신청서처럼 손으로 쓴 한국어 서류를 사진으로 찍어 텍스트로 옮기고 싶어요. 손글씨를 읽도록 학습된 모델이 있을까요?

- 사용자 의도: 한국어 손글씨 OCR
- persona / 표현: backend_dev / 목적형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `tasks` | image-text-to-text | 사진으로 찍어 … 옮기고(이미지 입력) | 예 |

- **2점 기준**: 손글씨 인식을 학습·용도로 명시한 모델
- **1점 기준**: 인쇄체 OCR 중심이지만 손글씨도 언급하거나, 손글씨 모델의 변환본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 537 | 1 | 2 | 534 | 0 | 3 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 534 | DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-MTP, LiquidAI/LFM3-VL-2B-MLX-6bit, cvgro/Qwen3.8-27B-TWIN-TURBO-Fable-Cold-Fusion-709-ULTRA-HERETIC-Uncensored-NM-DAU-NEO-MTP-GGUF |

#### 1. [OpceanAI/Qwen3.5-0.8B-abliterated](https://huggingface.co/OpceanAI/Qwen3.5-0.8B-abliterated) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — . Eleven benchmarks, produced by two different harnesses: a hand-written evaluator for the first six, and `lm-evaluation-harness` on

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.5-0.8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=abliterat) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.873 / 262144 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 3.22 |
| 벤치마크 근거 | 점수 10건 저장 |
| 의미 claim (use_cases) | The model is trained to predict token `t+2` given the hidden state at `t` and the embedding of `t+1`. |
| README 인용 | It is trained to predict token `t+2` given the hidden state at `t` and the embedding of `t+1`. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 65f0747cfcc0e2874bc760cd7df0de2e86109a48 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [localdeel/ko-hand-ocr-vl](https://huggingface.co/localdeel/ko-hand-ocr-vl) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — localdeel/ko-hand-ocr-vl

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.5-0.8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.68 / 262144 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.27 |
| 벤치마크 근거 | 점수 2건 저장 |
| 의미 claim (use_cases) | Any prompt works ("OCR", "Read the text", Korean, or empty). |
| README 인용 | Any prompt works ("OCR", "Read the text", Korean, or empty). |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 5beb32e1c3f8c26888db19d223fe4e0cfeb4f5f2 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [localdeel/ko-hand-ocr-vl-GGUF](https://huggingface.co/localdeel/ko-hand-ocr-vl-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — localdeel/ko-hand-ocr-vl-GGUF

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

## sc05 — 지역 어르신들 전화 음성을 받아 적는 서비스를 준비 중인데, 사투리가 섞인 한국어 음성도 알아듣는 모델이 있을까요?

- 사용자 의도: 방언 음성 인식
- persona / 표현: korean_service_planner / 목적형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `tasks` | automatic-speech-recognition | 음성을 받아 적는 | 예 |

- **2점 기준**: 한국어 방언(사투리) 데이터로 학습·평가됐다고 명시된 음성 인식 모델
- **1점 기준**: 방언 언급이 부가적이거나 방언 모델의 변환본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 321 | 7 | 4 | 298 | 12 | 23 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 298 | ghost613/whisper-large-v3-turbo-korean, onnx-community/Voxtral-Mini-4B-Realtime-2602-ONNX, younghan-meta/Voxtral-Mini-4B-Realtime-2602-ExecuTorch-Metal |

같은 canonical family 후보가 3개 이상: FunAudioLLM/Fun-ASR-MLT-Nano-2512 3

#### 1. [BuzzASR/korean](https://huggingface.co/BuzzASR/korean) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — ated on FLEURS / Common Voice test splits; other domains or dialects may differ. ## Results (normalized CER / WER, %) ### How t

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-large-v3 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.543 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 2.88 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The language/task prompt is baked into the generation config, so no `language=` argument is needed. |
| README 인용 | The language/task prompt is baked into the generation config, so no `language=` argument is needed. |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | ee4634aaaf3d5d0cf26c5e59e676b83bb0aa2d4d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [FunAudioLLM/Fun-ASR-MLT-Nano-2512](https://huggingface.co/FunAudioLLM/Fun-ASR-MLT-Nano-2512) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — rts Chinese, English, and Japanese, including support for 7 dialects and 26 regional accents in Chinese. FunASR is a fundamenta

| 항목 | 값 |
|---|---|
| canonical model | FunAudioLLM/Fun-ASR-MLT-Nano-2512 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 1.84 |
| 벤치마크 근거 | 점수 18건 저장 |
| 의미 claim (use_cases) | Accepts the language names shown in the inference example and supports multilingual recognition. |
| README 인용 | - **Language control:** Accepts the language names shown in the inference example and supports multilingual recognition. |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 2c088f535108689beff7e11cdc3d792af7d56552 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [FunAudioLLM/Fun-ASR-Nano-2512](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-2512) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — rts Chinese, English, and Japanese, including support for 7 dialects and 26 regional accents. Fun-ASR focuses on high-precision

| 항목 | 값 |
|---|---|
| canonical model | FunAudioLLM/Fun-ASR-Nano-2512 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 1.84 |
| 벤치마크 근거 | 점수 18건 저장 |
| 의미 claim (use_cases) | It supports low-latency real-time transcription and covers 31 languages. |
| README 인용 | It supports low-latency real-time transcription and covers 31 languages. |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 272c57b82523ada6fd87095e955f8e29100979ab |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [Kkonjeong/wav2vec2-base-korean](https://huggingface.co/Kkonjeong/wav2vec2-base-korean) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — the training data which may affect the accuracy for certain dialects or speakers.  It is recommended to evaluate the model's pe

| 항목 | 값 |
|---|---|
| canonical model | Kkonjeong/wav2vec2-base-korean (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.094 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit, readme:korean_explicit_phrase |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.35 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | It is particularly useful for applications requiring accurate Korean language recognition such as voice assistants, transcription services, and language learning tools. |
| README 인용 | It is particularly useful for applications requiring accurate Korean language recognition such as voice assistants, transcription services, and language learning tools. |
| provenance status | verified 13, not_applicable 3, documented 2, unknown 5 |
| revision | fa03d1a7138f1900131393cc7cb74f77926f177a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [Lexius/Phi-4-multimodal-instruct](https://huggingface.co/Lexius/Phi-4-multimodal-instruct) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — English accents and pronunciations. Other English accents, dialects, and non-English languages may experience lower recognitio

| 항목 | 값 |
|---|---|
| canonical model | Lexius/Phi-4-multimodal-instruct (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 5.574 / 131072 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit, readme:korean_explicit_phrase |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 10.38 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | speech-translation |
| README 인용 | - speech-translation |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | b0c6554d66e0f3e4f0cf2d92d25a134d3c1aecf2 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [Qwen/Qwen3-ASR-0.6B-hf](https://huggingface.co/Qwen/Qwen3-ASR-0.6B-hf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — dels in accuracy. \| Model \| Supported Languages \| Supported Dialects \| Inference Mode \| Audio Types \| Qwen3-ASR is supported na

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-0.6B-hf (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.782 / 131072 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.46 |
| 벤치마크 근거 | 점수 1건 저장 |
| 의미 claim (use_cases) | Transcription of audio files using a pipeline. |
| README 인용 | ```python from transformers import pipeline  model_id = "Qwen/Qwen3-ASR-0.6B-hf" pipe = pipeline("any-to-any", model=model_id, device_map="auto")  chat_template = [     {         "role": "user",         "content": [             {           … |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 7f1569a48a89f3e3f4dc3a5c9d28bddd903bc76c |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [Qwen/Qwen3-ASR-1.7B-hf](https://huggingface.co/Qwen/Qwen3-ASR-1.7B-hf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — dels in accuracy. \| Model \| Supported Languages \| Supported Dialects \| Inference Mode \| Audio Types \| Qwen3-ASR is supported na

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-1.7B-hf (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.038 / 131072 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 3.8 |
| 벤치마크 근거 | 점수 1건 저장 |
| 의미 claim (use_cases) | The `apply_transcription_request` usage is a convenience wrapper for `apply_chat_template`. |
| README 인용 | The `apply_transcription_request` usage [above](#simple-transcription) is a convenience wrapper for `apply_chat_template`. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | bcd2b5b7f32b480ab5790554cfa8347f246a14f3 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [ThakiCloud/Thaki-ASR-KO-Dialects-v1](https://huggingface.co/ThakiCloud/Thaki-ASR-KO-Dialects-v1) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — ThakiCloud/Thaki-ASR-KO-Dialects-v1

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-1.7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.038 / 131072 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit, readme:korean_explicit_phrase |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 7.59 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can transcribe audio files in Korean. |
| README 인용 | ```python import torch from qwen_asr import Qwen3ASRModel  model = Qwen3ASRModel.from_pretrained(     "ThakiCloud/Thaki-ASR-KO-Dialects-v1",     dtype=torch.bfloat16,     device_map="cuda:0",     max_inference_batch_size=16,     max_new_tok… |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | ec32ba9a07f327103486f6ef02fe6fc33ceab94f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [avericaai/Fun-ASR-MLT-Nano-2512-gguf](https://huggingface.co/avericaai/Fun-ASR-MLT-Nano-2512-gguf) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — supports Chinese, English, and Japanese, including various dialects and accents. Fun-ASR focuses on high-precision speech reco

| 항목 | 값 |
|---|---|
| canonical model | FunAudioLLM/Fun-ASR-MLT-Nano-2512 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.83 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.52 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Fun-ASR can be used for inference with various languages including Chinese, English, and Japanese. |
| README 인용 | ```python from funasr import AutoModel   def main():     model_dir = "FunAudioLLM/Fun-ASR-Nano-2512"     model = AutoModel(         model=model_dir,         trust_remote_code=True,         remote_code="./model.py",         device="cuda:0", … |
| provenance status | verified 12, not_applicable 4, documented 5, unknown 2 |
| revision | 8071c04db21304f23b0835fc2b067442cf959eac |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [avericaai/Qwen3-ASR-0.6B-gguf](https://huggingface.co/avericaai/Qwen3-ASR-0.6B-gguf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — cribe long audio. \| Model \| Supported Languages \| Supported Dialects \| Inference Mode \| Audio Types \| Note that streaming infer

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-0.6B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.782 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.55 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | For more detailed usage examples, please refer to the example code. |
| README 인용 | For more detailed usage examples, please refer to the [example code](https://github. |
| provenance status | verified 12, not_applicable 4, documented 5, unknown 2 |
| revision | cb73e773e7e99fa4ab7be3701d7b1bcf4b04d0a4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [bezzam/Qwen3-ASR-0.6B-hf](https://huggingface.co/bezzam/Qwen3-ASR-0.6B-hf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — dels in accuracy. \| Model \| Supported Languages \| Supported Dialects \| Inference Mode \| Audio Types \| Qwen3-ASR is supported na

| 항목 | 값 |
|---|---|
| canonical model | bezzam/Qwen3-ASR-0.6B-hf (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.782 / 131072 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.46 |
| 벤치마크 근거 | 점수 1건 저장 |
| 의미 claim (use_cases) | The model can be used for any-to-any audio transcription. |
| README 인용 | ```python from transformers import pipeline  model_id = "Qwen/Qwen3-ASR-0.6B-hf" pipe = pipeline("any-to-any", model=model_id, device_map="auto")  chat_template = [     {         "role": "user",         "content": [             {           … |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 43c4100b6d1bef2d611e6659c381bb053329cbe8 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [cstr/qwen3-asr-1.7b-GGUF](https://huggingface.co/cstr/qwen3-asr-1.7b-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — eech recognition model supporting 30 languages + 22 Chinese dialects, with support for speech, singing voice, and songs with ba

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-1.7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.349 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.39 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Recommended for most use cases (audio tower kept at Q8_0 — see rebake note) |
| README 인용 | \| `qwen3-asr-1.7b-q4_k.gguf` \| Q4_K \| ~1.5 GB \| Recommended for most use cases (audio tower kept at Q8_0 — see rebake note) \| |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 674df5d44b50a63e7102a18895ed20e3f91de301 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [epapanita/Qwen3-ASR-1.7B-gguf](https://huggingface.co/epapanita/Qwen3-ASR-1.7B-gguf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — cribe long audio. \| Model \| Supported Languages \| Supported Dialects \| Inference Mode \| Audio Types \| Note that streaming infer

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-1.7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.038 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.23 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | For more detailed usage examples, please refer to the example code. |
| README 인용 | For more detailed usage examples, please refer to the [example code](https://github. |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 6185944d2b90a5bbe453867107c667a4afe58844 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 14. [handy-computer/Fun-ASR-MLT-Nano-2512-gguf](https://huggingface.co/handy-computer/Fun-ASR-MLT-Nano-2512-gguf) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — supports Chinese, English, and Japanese, including various dialects and accents. Fun-ASR focuses on high-precision speech reco

| 항목 | 값 |
|---|---|
| canonical model | FunAudioLLM/Fun-ASR-MLT-Nano-2512 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.83 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.52 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for speech recognition in multiple languages including Chinese, English, and Japanese. |
| README 인용 | ```python from funasr import AutoModel   def main():     model_dir = "FunAudioLLM/Fun-ASR-Nano-2512"     model = AutoModel(         model=model_dir,         trust_remote_code=True,         remote_code="./model.py",         device="cuda:0", … |
| provenance status | verified 12, not_applicable 4, documented 5, unknown 2 |
| revision | 08f28dadd984030331802b2f9fbd9ecac97bf834 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 15. [handy-computer/Qwen3-ASR-0.6B-gguf](https://huggingface.co/handy-computer/Qwen3-ASR-0.6B-gguf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — cribe long audio. \| Model \| Supported Languages \| Supported Dialects \| Inference Mode \| Audio Types \| Note that streaming infer

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-0.6B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.782 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.55 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | For more detailed usage examples, please refer to the example code. |
| README 인용 | For more detailed usage examples, please refer to the [example code](https://github. |
| provenance status | verified 12, not_applicable 4, documented 5, unknown 2 |
| revision | 7e7c69a577fa2725dfedbe34b5e999336e30a19b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 16. [handy-computer/Qwen3-ASR-1.7B-gguf](https://huggingface.co/handy-computer/Qwen3-ASR-1.7B-gguf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — cribe long audio. \| Model \| Supported Languages \| Supported Dialects \| Inference Mode \| Audio Types \| You can pass any argument

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-1.7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.038 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.23 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | For more detailed usage examples, please refer to the example code. |
| README 인용 | For more detailed usage examples, please refer to the [example code](https://github. |
| provenance status | verified 12, not_applicable 4, documented 5, unknown 2 |
| revision | 0e0a596e3959c3f3f2ab7d443a5b6f0f4a4bba6f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 17. [hyk000/gg](https://huggingface.co/hyk000/gg) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음
- 근거 위치: `technical_metadata` — base_models openai/whisper-base datasets hyk000/gdialect metrics  model architectures WhisperForConditionalGeneratio

| 항목 | 값 |
|---|---|
| canonical model | openai/whisper-base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.242 / 1024 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.9 |
| 벤치마크 근거 | 없음 |
| 의미 claim (benchmarks) | It achieves the following results on the evaluation set: |
| README 인용 | It achieves the following results on the evaluation set: |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | a8901d457d47f8805f934eebc012278052e3ad2b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 18. [ldov/Qwen3-ASR-1.7B-gguf](https://huggingface.co/ldov/Qwen3-ASR-1.7B-gguf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — cribe long audio. \| Model \| Supported Languages \| Supported Dialects \| Inference Mode \| Audio Types \| Note that streaming infer

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-1.7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.038 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.23 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | For more detailed usage examples, please refer to the example code. |
| README 인용 | For more detailed usage examples, please refer to the [example code](https://github. |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 72670a53ff1598622ea968904093b71f767d2ffa |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 19. [lipik/Qwen3-ASR-1.7B-gguf](https://huggingface.co/lipik/Qwen3-ASR-1.7B-gguf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — cribe long audio. \| Model \| Supported Languages \| Supported Dialects \| Inference Mode \| Audio Types \| Note that streaming infer

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-1.7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.038 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 2.03 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | For more detailed usage examples, please refer to the example code. |
| README 인용 | For more detailed usage examples, please refer to the [example code](https://github. |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 23640732a3c47c6ac5950cb55d63c2037e32159d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 20. [litert-community/Qwen3-ASR-0.6B](https://huggingface.co/litert-community/Qwen3-ASR-0.6B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — n and speech recognition across 30 languages and 22 Chinese dialects. Includes an INT8 audio encoder and a 28-layer autoregress

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-0.6B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | — / — |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Can be used with Google's open-source on-device inference runtime across multiple platforms. |
| README 인용 | com/google-ai-edge/LiteRT-LM/tree/main/omni), Google's open-source on-device inference runtime across Android, iOS, macOS, Linux, and C++, alongside standalone `. |
| provenance status | verified 7, not_applicable 3, documented 4, unknown 9 |
| revision | 5028edc410addd0f9cf0b35a58a38aeb8bea4604 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 21. [litert-community/Qwen3-ASR-1.7B](https://huggingface.co/litert-community/Qwen3-ASR-1.7B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — ntification and recognition for 30 languages and 22 Chinese dialects. The model scored an English WER of 14 on the Intel GPU. T

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-1.7B-hf (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | — / — |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can transcribe a 16 kHz mono WAV of up to 30 seconds. |
| README 인용 | `transcribe` takes a 16 kHz mono WAV of up to 30 s; `prefix` is text the answer starts with, for example `language Chinese<asr_text>` to force the language, and the return value is the answer after it. |
| provenance status | verified 7, not_applicable 3, documented 5, unknown 8 |
| revision | 15cc9089aa6078a77c009b1b2deed106fe31efb5 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 22. [memoravox/Qwen3-ASR-1.7B-gguf](https://huggingface.co/memoravox/Qwen3-ASR-1.7B-gguf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — cribe long audio. \| Model \| Supported Languages \| Supported Dialects \| Inference Mode \| Audio Types \| Note that streaming infer

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-1.7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.038 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.41 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | For more detailed usage examples, please refer to the example code. |
| README 인용 | For more detailed usage examples, please refer to the [example code](https://github. |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 369c2706b8e9e1571d207be9425ff0d0f060819d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 23. [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — English accents and pronunciations. Other English accents, dialects, and non-English languages may experience lower recognitio

| 항목 | 값 |
|---|---|
| canonical model | microsoft/Phi-4-multimodal-instruct (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 5.574 / 131072 |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit, readme:korean_explicit_phrase |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 11.93 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | speech-translation |
| README 인용 | - speech-translation |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 93f923e1a7727d1c4f446756212d9d3e8fcc5d81 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## sc06 — RAG 파이프라인에서 1차 검색 결과를 다시 순위 매길 한국어 reranker(cross-encoder)를 찾고 있습니다.

- 사용자 의도: 한국어 재순위 모델
- persona / 표현: ml_engineer / 기술형 · 난이도 hard
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: 질의-문서 쌍 재순위(reranking)용 cross-encoder 로 명시된 모델
- **1점 기준**: 다국어 reranker, 또는 reranker 의 변환·양자화본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 3 | 7 | 4,003 | 4 | 14 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 4,003 | axana-labs/Qwen2.5-72B-Instruct-bnb-4bit, bartowski/Ministral-8B-Instruct-2410-GGUF, jcbtc/qwopus3.6-27b-v2-chadrock-rocmfp4-mtp |

#### 1. [Dongjin-kr/ko-reranker](https://huggingface.co/Dongjin-kr/ko-reranker) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — Dongjin-kr/ko-reranker

| 항목 | 값 |
|---|---|
| canonical model | Dongjin-kr/ko-reranker (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.56 / 514 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 2.09 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Model is used for text-classification tasks. |
| README 인용 | pipeline_tag: text-classification --- |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 8c2ab1a833734491fd3158164dd2b7d8b28e071c |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [QuantFactory/lb-reranker-0.5B-v1.0-GGUF](https://huggingface.co/QuantFactory/lb-reranker-0.5B-v1.0-GGUF) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델; 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — QuantFactory/lb-reranker-0.5B-v1.0-GGUF

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-0.5B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=Quant) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.63 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.39 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is applicable to a broad range of use cases. |
| README 인용 | Trained on data in over 95 languages, this model is applicable to a broad range of use cases. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | d02fbab0fe03083d22ab2b5d333e719ea712076d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [amber-tech/bert-multilingual-passage-reranking-msmarco](https://huggingface.co/amber-tech/bert-multilingual-passage-reranking-msmarco) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `model_id` — amber-tech/bert-multilingual-passage-reranking-msmarco

| 항목 | 값 |
|---|---|
| canonical model | amber-tech/bert-multilingual-passage-reranking-msmarco (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 512 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.62 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used to rerank search results. |
| README 인용 | As you normally want to rerank the first dozens of search results keep in mind the inference time of approximately 300 ms/query. |
| provenance status | verified 11, not_applicable 3, documented 4, unknown 5 |
| revision | 59162c6b2be947c6c50f0499189f3d1c771089ba |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [batiai/Qwen3-Embedding-0.6B-GGUF](https://huggingface.co/batiai/Qwen3-Embedding-0.6B-GGUF) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — ctor DB (sqlite-vec / LanceDB) top-K candidates    ↓ [Qwen3-Reranker 0.6B / 4B / 8B] top-3    ↓ [Qwen3.6-35B-A3B chat LLM] answe

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-Embedding-0.6B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.596 / 32768 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.46 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Best performance with queries that have an instruction prefix. |
| README 인용 | Qwen3-Embedding performs best when queries carry an instruction prefix: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | d84b43e69be2a7f360b062b454f313783d8a8e36 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [batiai/Qwen3-Embedding-4B-GGUF](https://huggingface.co/batiai/Qwen3-Embedding-4B-GGUF) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델; 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — vector DB (sqlite-vec / LanceDB) top-K candidates ↓ [Qwen3-Reranker 4B or 8B] top-3 ↓ [Qwen3.6-35B-A3B chat LLM] answer pipelin

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-Embedding-4B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 4.022 / 40960 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 3.08 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | base_model: Qwen/Qwen3-Embedding-4B |
| README 인용 | base_model: Qwen/Qwen3-Embedding-4B pipeline_tag: sentence-similarity library_name: llama. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | e2cc8e510afaa9120246351d7d2956722d270ff7 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [batiai/Qwen3-Embedding-8B-GGUF](https://huggingface.co/batiai/Qwen3-Embedding-8B-GGUF) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — ctor DB (sqlite-vec / LanceDB) top-K candidates    ↓ [Qwen3-Reranker 8B] top-3    ↓ [Qwen3.6-35B-A3B chat LLM] answer ``` - Quan

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-Embedding-8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.567 / 40960 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 5.79 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | base_model: Qwen/Qwen3-Embedding-8B |
| README 인용 | base_model: Qwen/Qwen3-Embedding-8B pipeline_tag: sentence-similarity library_name: llama. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 061dfb06ef13e9155350a78c54d92800bd5d602c |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [batiai/Qwen3.6-27B-GGUF](https://huggingface.co/batiai/Qwen3.6-27B-GGUF) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — s://huggingface.co/batiai/Qwen3-Embedding-8B-GGUF) · [Qwen3-Reranker-8B](https://huggingface.co/batiai/Qwen3-Reranker-8B-GGUF) \|

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.6-27B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 26.896 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 10.42 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | 6-27B usage starts at 24 GB unified memory, indicating its memory requirements for effective operation. |
| README 인용 | 6-27B usage starts at **24 GB unified memory** — below that, single-turn inference is bottlenecked by swap. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 2dfa9a5e243d9194a9dac4527a3026c67f965a23 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [gpustack/bce-reranker-base_v1-GGUF](https://huggingface.co/gpustack/bce-reranker-base_v1-GGUF) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델; 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — gpustack/bce-reranker-base_v1-GGUF

| 항목 | 값 |
|---|---|
| canonical model | gpustack/bce-reranker-base_v1-GGUF (variant=false, 종류=—, 관계 근거=self, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.278 / 512 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.19 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | RAG applications: [QAnything](https://github.com/netease-youdao/qanything), [HuixiangDou](https://github.com/InternLM/HuixiangDou), [ChatPDF](https://github.com/shibing624/ChatPDF). |
| README 인용 | - RAG applications: [QAnything](https://github.com/netease-youdao/qanything), [HuixiangDou](https://github.com/InternLM/HuixiangDou), [ChatPDF](https://github.com/shibing624/ChatPDF). |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 13ea48b2840d57e182fbb0fda826d6539d312548 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [gpustack/gte-multilingual-reranker-base-GGUF](https://huggingface.co/gpustack/gte-multilingual-reranker-base-GGUF) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델; 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — gpustack/gte-multilingual-reranker-base-GGUF

| 항목 | 값 |
|---|---|
| canonical model | gpustack/gte-multilingual-reranker-base-GGUF (variant=false, 종류=—, 관계 근거=self, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.306 / 8192 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.19 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Training Architecture: Trained using an encoder-only transformers architecture, resulting in a smaller model size. Unlike previous models based on decode-only LLM architecture (e.g., gte-qwen2-1.5b-instruct), this model has lower hardware r… |
| README 인용 | - **Training Architecture**: Trained using an encoder-only transformers architecture, resulting in a smaller model size. Unlike previous models based on decode-only LLM architecture (e.g., gte-qwen2-1.5b-instruct), this model has lower hard… |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | ca8f873f19fa20a4c2051166acbcf39c7cbe32a0 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [leewaay/klue-roberta-large-klueSTS-cross](https://huggingface.co/leewaay/klue-roberta-large-klueSTS-cross) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — -Transformers)  ```python from sentence_transformers import CrossEncoder pairs = [('Query', 'Paragraph1'), ('Query', 'Paragraph2') ,

| 항목 | 값 |
|---|---|
| canonical model | leewaay/klue-roberta-large-klueSTS-cross (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.337 / 514 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 1.25 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for applications such as retrieve and rerank tasks. |
| README 인용 | net/examples/applications/retrieve_rerank/README. |
| provenance status | verified 14, not_applicable 3, documented 2, unknown 4 |
| revision | 117a7869b1cfe8f4bbf8455eb5293b711e20e0cd |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [maidalun1020/bce-reranker-base_v1](https://huggingface.co/maidalun1020/bce-reranker-base_v1) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `model_id` — maidalun1020/bce-reranker-base_v1

| 항목 | 값 |
|---|---|
| canonical model | maidalun1020/bce-reranker-base_v1 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / 514 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 1.04 |
| 벤치마크 근거 | 점수 1건 저장 |
| 의미 claim (use_cases) | RAG applications: [QAnything](https://github.com/netease-youdao/qanything), [ragflow](https://github.com/infiniflow/ragflow), [HuixiangDou](https://github.com/InternLM/HuixiangDou), [ChatPDF](https://github.com/shibing624/ChatPDF). |
| README 인용 | - RAG applications: [QAnything](https://github.com/netease-youdao/qanything), [ragflow](https://github.com/infiniflow/ragflow), [HuixiangDou](https://github.com/InternLM/HuixiangDou), [ChatPDF](https://github.com/shibing624/ChatPDF). |
| provenance status | verified 12, not_applicable 3, documented 4, unknown 4 |
| revision | eb7650fca1d81e2856fbd0d522488844aa502735 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [shangrilar/klue-roberta-small-cross-encoder](https://huggingface.co/shangrilar/klue-roberta-small-cross-encoder) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — shangrilar/klue-roberta-small-cross-encoder

| 항목 | 값 |
|---|---|
| canonical model | shangrilar/klue-roberta-small-cross-encoder (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.068 / 514 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | stage1:korean_name_strong |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.25 |
| 벤치마크 근거 | 없음 |
| 의미 claim (—) | — |
| README 인용 | — |
| provenance status | verified 14, not_applicable 3, documented 1, unknown 5 |
| revision | b4f51bc3be0504396eb67484b5a7512bbbac756b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [vllm-sr/mmbert-rerank-32k-2d-matryoshka](https://huggingface.co/vllm-sr/mmbert-rerank-32k-2d-matryoshka) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `model_id` — vllm-sr/mmbert-rerank-32k-2d-matryoshka

| 항목 | 값 |
|---|---|
| canonical model | vllm-sr/mmbert-32k-yarn (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.307 / 32768 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.57 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | A 32K context multilingual reranker with 2D Matryoshka support for efficient inference. |
| README 인용 | A **32K context multilingual reranker** with **2D Matryoshka** support, enabling flexible layer and dimension reduction for efficient inference. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | c934050280a1cebf9a36be64845d4ee46190e11b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 14. [whybe-choi/kovre](https://huggingface.co/whybe-choi/kovre) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — . The second stage distills relevance scores from `Qwen3-VL-Reranker-8B` using Korean data.

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-VL-Embedding-2B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.128 / 262144 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 3.96 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | For lower-level inference with Transformers, use the [`Qwen3-VL-Embedding`](https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B). |
| README 인용 | For lower-level inference with Transformers, use the [`Qwen3-VL-Embedding`](https://github. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 65bb140357914c871b9307729cee786db820e0c9 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## sc07 — 글쓰기 플랫폼에 한국어 맞춤법·문법 교정 기능을 넣고 싶어요. 그런 용도로 만든 모델이 있나요?

- 사용자 의도: 한국어 맞춤법·문법 교정
- persona / 표현: korean_service_planner / 목적형 · 난이도 hard
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: 맞춤법·문법 오류 교정(GEC)용으로 학습된 모델
- **1점 기준**: 교정이 부가 기능이거나 교정 모델의 변환본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 6 | 1 | 4,009 | 1 | 8 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 4,009 | Harsha001/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-ROCmFPX, LiquidAI/LFM3-VL-2B-GGUF, mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF |

#### 1. [42MARU/ko-spelling-wav2vec2-conformer-del-1s](https://huggingface.co/42MARU/ko-spelling-wav2vec2-conformer-del-1s) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — 42MARU/ko-spelling-wav2vec2-conformer-del-1s

| 항목 | 값 |
|---|---|
| canonical model | 42MARU/ko-spelling-wav2vec2-conformer-del-1s (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.18 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.67 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is suitable for Korean language processing. |
| README 인용 | - ko  # Example: fr |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 174ec0b917167569c2d4b248d4892802018535ef |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [Squezilia/xlm-r-r4s-large](https://huggingface.co/Squezilia/xlm-r-r4s-large) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — applications. Cross-lingual translation, localization, and grammar correction. Multi-task training objective with a shared backbone. E

| 항목 | 값 |
|---|---|
| canonical model | FacebookAI/xlm-roberta-large (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.563 / 514 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-4.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 2.1 |
| 벤치마크 근거 | 점수 10건 저장 |
| 의미 claim (use_cases) | Text classification tasks. |
| README 인용 | pipeline_tag: text-classification library_name: transformers tags: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 5570bf381ea24bc8867e3a648accec9fbbb1dd7b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [j5ng/et5-typos-corrector](https://huggingface.co/j5ng/et5-typos-corrector) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — j5ng/et5-typos-corrector

| 항목 | 값 |
|---|---|
| canonical model | j5ng/et5-typos-corrector (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 1.21 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used to correct typos in Korean text. |
| README 인용 | pipeline_tag: text-generation license: apache-2. |
| provenance status | verified 11, not_applicable 3, documented 4, unknown 5 |
| revision | 7248a6019107c181df36742a2e7b248676cbb0c7 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [kolada-app/Kolada-writer](https://huggingface.co/kolada-app/Kolada-writer) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — acters) and by the same model listing realistic slips; real typo fixes from the [GitHub Typo Corpus](https://github.com/mhagiwar

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/LFM2.5-1.2B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.17 / 128000 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.89 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is trained on notes written in nine languages, incorporating realistic typing mistakes and corrections. |
| README 인용 | - **Data:** notes written for training in the nine languages by [Qwen3-30B-A3B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507) (Apache 2.0), given the mistakes each language is really typed with, by rule (neighbourin… |
| provenance status | verified 13, not_applicable 4, documented 5, unknown 1 |
| revision | 00b0504d9e01ef7609b8b9a76c2070d34e5501fe |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [mradermacher/PIXIE-Spell-v1.5-0.6B-GGUF](https://huggingface.co/mradermacher/PIXIE-Spell-v1.5-0.6B-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — mradermacher/PIXIE-Spell-v1.5-0.6B-GGUF

| 항목 | 값 |
|---|---|
| canonical model | telepix/PIXIE-Spell-v1.5-0.6B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.596 / 40960 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.28 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | If you are unsure how to use GGUF files, refer to one of TheBloke's READMEs |
| README 인용 | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | f0330b2365e624c4404af65d4f000d40a840ed6b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [onelastkissforme/dadeum-gec-base](https://huggingface.co/onelastkissforme/dadeum-gec-base) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — onelastkissforme/dadeum-gec-base

| 항목 | 값 |
|---|---|
| canonical model | gogamza/kobart-base-v2 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.124 / 1026 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-sa-4.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.46 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is suitable for text generation tasks. |
| README 인용 | 0 library_name: transformers pipeline_tag: text-generation base_model: gogamza/kobart-base-v2 tags: |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | d2af339da05d89750c38db6331b3ddbd3b3d5219 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [onelastkissforme/dadeum-gec-small](https://huggingface.co/onelastkissforme/dadeum-gec-small) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — onelastkissforme/dadeum-gec-small

| 항목 | 값 |
|---|---|
| canonical model | gogamza/kobart-base-v2 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.062 / 1026 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-sa-4.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.23 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is suitable for tasks involving text generation. |
| README 인용 | 0 library_name: transformers pipeline_tag: text-generation base_model: gogamza/kobart-base-v2 tags: |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | b15520287b04803da93c3f78e509c6c905d45df1 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [telepix/PIXIE-Spell-v1.5-0.6B](https://huggingface.co/telepix/PIXIE-Spell-v1.5-0.6B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — telepix/PIXIE-Spell-v1.5-0.6B

| 항목 | 값 |
|---|---|
| canonical model | telepix/PIXIE-Spell-v1.5-0.6B (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.596 / 40960 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 2.22 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | 6B is a multilingual embedding model specialized for Korean and English retrieval tasks. |
| README 인용 | 6B** is a multilingual embedding model specialized for Korean and English retrieval tasks. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | fb002c3c659fed6c33b7e0d4cb65f6fa6372ae27 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## sc08 — 고객 문의 챗봇 앞단에서 사용자가 무엇을 원하는지(의도) 먼저 분류하는 한국어 intent classification 모델이 필요해요.

- 사용자 의도: 문의 의도 분류
- persona / 표현: backend_dev / 혼합형 · 난이도 easy
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `tasks` | text-classification | intent classification | 예 |

- **2점 기준**: 한국어 의도 분류용으로 학습된 모델
- **1점 기준**: 다국어 의도 분류 모델 또는 변환본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 157 | 3 | 2 | 147 | 5 | 10 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 147 | Horizon-Labs/multilingual-toxicity-base, LimYeri/HowRU-KoELECTRA-Emotion-Classifier, lokas/spam-usernames-classifier |

#### 1. [LatentAILabs/laya-indic](https://huggingface.co/LatentAILabs/laya-indic) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음; 다국어·범용 모델
- 근거 위치: `benchmark_metadata` — languages metric score benchmark BENCHMARK dataset MASSIVE intent@20 + yes/no (az, hi) metric score benchmark BENCHMARK datas

| 항목 | 값 |
|---|---|
| canonical model | jhu-clsp/mmBERT-base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.322 / — |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.6 |
| 벤치마크 근거 | 점수 11건 저장 |
| 의미 claim (use_cases) | The model is designed for text classification tasks. |
| README 인용 | 0 library_name: thx01 pipeline_tag: text-classification base_model: jhu-clsp/mmBERT-base language: [en, hi, bn, ta, te, mr, gu, kn, ml, pa, ur, or, az, kk, uz, ka, tr, fa, ru, de, fr, es, ar, zh, ja, ko, multilingual] datasets: |
| provenance status | verified 13, not_applicable 3, documented 5, unknown 2 |
| revision | 2936da26cfa3c541abf90f7ca25eca122d0ab1fc |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [OceanLabs/Coral-2-3B-fast](https://huggingface.co/OceanLabs/Coral-2-3B-fast) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — named options, or a rating: routing and triage, moderation, intent and topic classification, extraction checks, reranking, LLM

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/d1-3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 3.123 / 32768 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 5.82 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | We recommend d1-3B wherever a pipeline needs a yes/no, a pick from named options, or a rating: routing and triage, moderation, intent and topic classification, extraction checks, reranking, LLM-as-a-judge scoring, agent guardrails, and visu… |
| README 인용 | We recommend d1-3B wherever a pipeline needs a yes/no, a pick from named options, or a rating: routing and triage, moderation, intent and topic classification, extraction checks, reranking, LLM-as-a-judge scoring, agent guardrails, and visu… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 650c09f2750adcf84d4200ffe614a4ce485f7e0d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [Orvena/Cue-0.4B](https://huggingface.co/Orvena/Cue-0.4B) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `semantic_metadata` — text classification tasks. It can answer questions based on intent probability thresholds. The model's responses are based on

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-0.6B-Base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.376 / 131072 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.7 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is designed for text classification tasks. |
| README 인용 | 6B-Base library_name: coreml pipeline_tag: text-classification language: |
| provenance status | verified 13, not_applicable 3, documented 5, unknown 2 |
| revision | 98100a83d3f406de9b2e7eec64f84dd281245fa7 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [Squezilia/xlm-r-r4s-large](https://huggingface.co/Squezilia/xlm-r-r4s-large) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — th **93.53% accuracy** (`0.9152` Macro F1).  3. **🏷️ Domain Intent Router (`category` — 13 classes)**: Classifies the function

| 항목 | 값 |
|---|---|
| canonical model | FacebookAI/xlm-roberta-large (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.563 / 514 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-4.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 2.1 |
| 벤치마크 근거 | 점수 10건 저장 |
| 의미 claim (use_cases) | Text classification tasks. |
| README 인용 | pipeline_tag: text-classification library_name: transformers tags: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 5570bf381ea24bc8867e3a648accec9fbbb1dd7b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [ThakiCloud/Thaki-SlotGrounder-KO-7M](https://huggingface.co/ThakiCloud/Thaki-SlotGrounder-KO-7M) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — LICENSE. - AUROC and risk are measured on **one proposer** (IntentAction S9). With a ```bash pip install -r requirements.txt

| 항목 | 값 |
|---|---|
| canonical model | ThakiCloud/Thaki-InputGuard-KO-9M (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.007 / — |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.03 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Installation and usage instructions provided. |
| README 인용 | ```bash pip install -r requirements.txt     # torch, safetensors, regex, numpy python inference.py                  # 8 built-in examples, CPU python inference.py --op send --payee 김하늘 --money 5만원 "김하늘한테 5만원 보내줘" ``` |
| provenance status | verified 11, not_applicable 3, documented 5, unknown 4 |
| revision | eb68ee2ea288e961717f404cc962e9c8ff873c9c |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [bespin-global/klue-roberta-small-3i4k-intent-classification](https://huggingface.co/bespin-global/klue-roberta-small-3i4k-intent-classification) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — bespin-global/klue-roberta-small-3i4k-intent-classification

| 항목 | 값 |
|---|---|
| canonical model | bespin-global/klue-roberta-small-3i4k-intent-classification (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.068 / 514 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.25 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for text classification tasks, specifically for intent classification. |
| README 인용 | ``` python from transformers import RobertaTokenizerFast, RobertaForSequenceClassification, TextClassificationPipeline  # Load fine-tuned model by HuggingFace Model Hub HUGGINGFACE_MODEL_PATH = "bespin-global/klue-roberta-small-3i4k-intent-… |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 97e2be417f45247118bb2be2778183a929ba91ef |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [corners-ai/CoCo-Decision-4B-Ko](https://huggingface.co/corners-ai/CoCo-Decision-4B-Ko) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — mixture of publicly available Korean and English datasets (intent classification, reading comprehension, natural-language inf

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.5-4B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / — |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.04 |
| 벤치마크 근거 | 점수 6건 저장 |
| 의미 claim (use_cases) | Places where a threshold on a probability is more useful than a generated answer (for example, act automatically above 0.9, ask a human below it). |
| README 인용 | - Places where a threshold on a probability is more useful than a generated answer (for example, act automatically above 0.9, ask a human below it) |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 31486803206da0b384e609cdf894f53cf83eda9d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [desert-ant-labs/emo](https://huggingface.co/desert-ant-labs/emo) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — # Limitations  - Emo is tuned for short text that states an intent. Longer text gets noisier suggestions.  - Emoji meanings ar

| 항목 | 값 |
|---|---|
| canonical model | desert-ant-labs/emo (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | — / — |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.01 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: text-classification |
| README 인용 | pipeline_tag: text-classification --- |
| provenance status | verified 8, not_applicable 3, documented 4, unknown 8 |
| revision | 7c2e137cb0300ecf8e31b7deab4c4e9734d06b74 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [doofz/THX-01](https://huggingface.co/doofz/THX-01) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — 3. [Benchmarks](#benchmarks) ## Limitations  - Fine-grained intent sets with many near-synonymous labels remain hard: Banking7

| 항목 | 값 |
|---|---|
| canonical model | jhu-clsp/mmBERT-base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.322 / — |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.6 |
| 벤치마크 근거 | 점수 6건 저장 |
| 의미 claim (use_cases) | Text classification for various languages including Azerbaijani, English, Russian, and Turkish. |
| README 인용 | 0 library_name: thx01 pipeline_tag: text-classification base_model: jhu-clsp/mmBERT-base language: [az, en, ru, tr, de, fr, es, ar, hi, zh, fa, ka, ja, ko, uk, kk, uz, it, multilingual] tags: [decision-model, calibration, reinforcement-lear… |
| provenance status | verified 13, not_applicable 3, documented 5, unknown 2 |
| revision | b323afcef149f9288a9d0daef4badd67b9b87c61 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [monologg/koelectra-small-finetuned-intent-cls](https://huggingface.co/monologg/koelectra-small-finetuned-intent-cls) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — monologg/koelectra-small-finetuned-intent-cls

| 항목 | 값 |
|---|---|
| canonical model | monologg/koelectra-small-finetuned-intent-cls (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | — / 512 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | stage1:korean_name_strong |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin / 0.05 |
| 벤치마크 근거 | 없음 |
| 의미 claim (—) | — |
| README 인용 | — |
| provenance status | verified 11, not_applicable 3, documented 1, unknown 8 |
| revision | 0ba20de0556ea6b18b554d6e33a91e18fda5390b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## sc09 — 판례·법령 검색 RAG 를 만들고 있어요. 법률 도메인 데이터로 학습된 한국어 sentence embedding 모델이 있을까요?

- 사용자 의도: 법률 도메인 검색용 임베딩
- persona / 표현: startup_dev / 혼합형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `tasks` | sentence-similarity, feature-extraction | sentence embedding 모델 | 예 |

- **2점 기준**: 법률 문서 검색·임베딩용으로 학습됐다고 명시된 모델
- **1점 기준**: 범용 임베딩이지만 법률 검색 평가·용도가 언급된 모델 또는 변환본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 338 | 3 | 1 | 332 | 2 | 6 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 332 | Auparima/thaifood-embed, batiai/Qwen3-Embedding-8B-GGUF, ys7yoo/sentence-bert-klue-nli-sts-all |

#### 1. [MarkrAI/pplx-embed-v2-late-0.6b-ko-vdr](https://huggingface.co/MarkrAI/pplx-embed-v2-late-0.6b-ko-vdr) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — The model can be used to determine if the average monthly legal welfare costs per person for companies with more than 30 em

| 항목 | 값 |
|---|---|
| canonical model | perplexity-ai/pplx-embed-v2-late-0.6b (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.594 / 262144 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.11 |
| 벤치마크 근거 | 점수 3건 저장 |
| 의미 claim (use_cases) | The model can be used to determine if the average monthly legal welfare costs per person for companies with more than 30 employees are higher than those with 10-29 employees. |
| README 인용 | ```python from sentence_transformers import MultiVectorEncoder  # Download from the 🤗 Hub model = MultiVectorEncoder("MarkrAI/pplx-embed-v2-late-0.6b-ko-vdr") # Run inference: each input becomes a sequence of per-token vectors (variable len… |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | ff076f69355bb626c63c905d46de0ed98a6920f7 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [mykor/KURE-v1-gguf](https://huggingface.co/mykor/KURE-v1-gguf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — 당사자가 개인적으로 직접 심리에 참석하기보다는 변호사가 참석하는 경우가 많으며, 심리대상도 사실문제가 아닌 법률문제가 대부분이기 때문이라는 것임 □ 한편, 연방헌법재판소는 「연방헌법재판소법」(Bundesverfassun

| 항목 | 값 |
|---|---|
| canonical model | nlpai-lab/KURE-v1 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.567 / 8192 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.34 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | feature-extraction |
| README 인용 | pipeline_tag: feature-extraction --- |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 65128e4341eee21ccd8bc86c033fbc44ff7b4871 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [nlpai-lab/KoE5](https://huggingface.co/nlpai-lab/KoE5) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — 당사자가 개인적으로 직접 심리에 참석하기보다는 변호사가 참석하는 경우가 많으며, 심리대상도 사실문제가 아닌 법률문제가 대부분이기 때문이라는 것임 □ 한편, 연방헌법재판소는 「연방헌법재판소법」(Bundesverfassun

| 항목 | 값 |
|---|---|
| canonical model | intfloat/multilingual-e5-large (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.56 / 514 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 2.09 |
| 벤치마크 근거 | 점수 4건 저장 |
| 의미 claim (use_cases) | Use for feature-extraction in various applications. |
| README 인용 | pipeline_tag: feature-extraction --- |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 237b580aea358e3042fcf5baf78124c33c3afd16 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [sionic-ai/comsat-embed-ko-8b-preview](https://huggingface.co/sionic-ai/comsat-embed-ko-8b-preview) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음
- 근거 위치: `benchmark_metadata` — benchmark MIRACL dataset LawIRKo metric score

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-Embedding-8B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.567 / 40960 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 14.1 |
| 벤치마크 근거 | 점수 1건 저장 |
| 의미 claim (use_cases) | The model is designed to provide high-quality text representations for real-world information retrieval scenarios, including document search, question answering, knowledge base retrieval, and enterprise semantic search. |
| README 인용 | The model is designed to provide high-quality text representations for real-world information retrieval scenarios, including document search, question answering, knowledge base retrieval, and enterprise semantic search. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | a5cc22b651c1b2e51cdd8bf671774ae93584f0ab |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [woong0322/ko-legal-sbert-finetuned](https://huggingface.co/woong0322/ko-legal-sbert-finetuned) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — woong0322/ko-legal-sbert-finetuned

| 항목 | 값 |
|---|---|
| canonical model | woong0322/ko-legal-sbert-finetuned (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.111 / 512 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.41 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for sentence similarity tasks, particularly in legal contexts. |
| README 인용 | inference:   parameters:     task: sentence-similarity     normalize_embeddings: true model-index: |
| provenance status | verified 14, not_applicable 3, documented 2, unknown 4 |
| revision | 16b5211ddc371d2739d1ec45e9ec4dd023b494c6 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [ysmeta/EVE-Embed-1.1-Legal](https://huggingface.co/ysmeta/EVE-Embed-1.1-Legal) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — ysmeta/EVE-Embed-1.1-Legal

| 항목 | 값 |
|---|---|
| canonical model | dragonkue/BGE-m3-ko (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.568 / 8194 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 2.12 |
| 벤치마크 근거 | 점수 2건 저장 |
| 의미 claim (use_cases) | Korean embedding model for legal precedent retrieval |
| README 인용 | ```python from sentence_transformers import SentenceTransformer  model = SentenceTransformer("ysmeta/EVE-Embed-1.1-Legal")  query = "계약금을 이미 받았는데도 상대방이 계약을 취소할 수 있나요?" docs = [     "소유권이전등기청구사건 당사자의 일방이 계약이행에 착수한 후에는 해제권 행사를 할 수 없으므로 …",   … |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 88cf6e2e374c7179957ec09c2d32ed3fffa8370f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## sc10 — 한국어 텍스트에서 이름·전화번호 같은 PII 를 탐지하는 모델이 필요합니다. 비식별화(de-identification) 용도로 학습된 걸 찾고 있어요.

- 사용자 의도: 개인정보(PII) 탐지·마스킹
- persona / 표현: ml_engineer / 기술형 · 난이도 hard
- 기대 행동: recommend

하드 필터 조건 없음 — 코퍼스 전체가 eligible 이다.

- **2점 기준**: 개인정보 탐지·마스킹을 주 용도로 명시한 모델
- **1점 기준**: 개인정보 처리가 부가 기능이거나 변환본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 4,017 | 6 | 1 | 4,007 | 3 | 10 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 4,007 | TheBloke/PiVoT-0.1-early-GGUF, team-lucid/mptk-1b, unsloth/Magistral-Small-2506 |

#### 1. [FrameByFrame/guardrail-korean-gemma-4-E2B](https://huggingface.co/FrameByFrame/guardrail-korean-gemma-4-E2B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — ples to prevent false positives. The output schema includes PII filtering for phone numbers and emails. Examples of use cas

| 항목 | 값 |
|---|---|
| canonical model | google/gemma-4-E2B-it (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 5.123 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 9.54 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model includes legitimate-unicode safe examples to prevent false positives. |
| README 인용 | Legitimate-unicode safe examples (Korean, emoji, diacritics in names) included to prevent false positives. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 090d21a33edf4159eab64dbcee33f77e2c0e2284 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [LaraAI-Labs/tellama](https://huggingface.co/LaraAI-Labs/tellama) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — policy](https://redpluglab.  io/tellama/privacy/) and [한국어 개인정보처리방침](https://redpluglab. Include the model filename, app/ru

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-4B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 4.022 / 40960 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 5.22 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for local Android AI applications. |
| README 인용 | md) · [Download and setup](docs/USAGE. |
| provenance status | verified 13, not_applicable 4, documented 5, unknown 1 |
| revision | a3ae1e5bbb40c23109744879793ce779ec257d8f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [OpenMed/Ministral-3B-PII-Preview](https://huggingface.co/OpenMed/Ministral-3B-PII-Preview) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — OpenMed/Ministral-3B-PII-Preview

| 항목 | 값 |
|---|---|
| canonical model | OpenMed/Ministral-3B-PII-Preview (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 3.849 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 7.17 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The PII extraction system prompt (with few-shot examples) is baked into the chat template, so no system message is required — just send the text. |
| README 인용 | The PII extraction system prompt (with few-shot examples) is baked into the chat template, so no system message is required — just send the text. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | e97c55ae4b34527cde704f975684d69539844a2b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [Saxo/Linkbricks-Horizon-AI-Korean-Gemma-2-sft-dpo-27B](https://huggingface.co/Saxo/Linkbricks-Horizon-AI-Korean-Gemma-2-sft-dpo-27B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — fety applications. The model provides enhanced detection of personally identifiable information (PII) and sensitive-information patterns. The m

| 항목 | 값 |
|---|---|
| canonical model | google/gemma-2-27b-it (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 27.227 / 8192 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit, readme:korean_explicit_phrase |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 15.5 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is particularly optimized for high-dimensional analysis of customer reviews and social media posts, as well as coding and content-safety applications. |
| README 인용 | 특히 고객 리뷰나 소셜 포스팅 고차원 분석 및 코딩과 욕설, 비방, 음란물, 성적으로 노골적인 콘텐츠, 인종차별 또는 기타 유해 콘텐츠 탐지 개인정보 및 민감정보 패턴 탐지, 차단 또는 사용자 경고가 필요할 수 있는 기타 고위험 요청 탐지 강화된 모델<br> -Deepspeed Stage=3, rslora 및 BAdam Layer Mode 사용<br> Linkbricks Horizon-AI CEO and data scienti… |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 808e2cd2f000d502073c6b9016479d7725296914 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [atonlee/Qoamo-PII-Decision](https://huggingface.co/atonlee/Qoamo-PII-Decision) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — atonlee/Qoamo-PII-Decision

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

#### 6. [blackmallangcow/nari-decision-4b](https://huggingface.co/blackmallangcow/nari-decision-4b) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — eneral content-safety filter: the guardrail questions cover PII, secrets and prompt injection. ## Limitations  - Calibratio

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.5-4B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 4.217 / 262144 |
| task | feature-extraction (matched: feature-extraction) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 7.88 |
| 벤치마크 근거 | 점수 3건 저장 |
| 의미 claim (use_cases) | The model can be used to act on the confidence of responses based on guardrail evaluations. |
| README 인용 | Example from the System One eval set: 50 guardrail responses (26 unsafe, 24 safe), sending a response only when `p_true` of `safe_to_send` is at least the threshold. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 4c6034fe4097d649d9d3856d3bdbb0f6b7da6475 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [inboxpraveen/Kavach-PII-270M](https://huggingface.co/inboxpraveen/Kavach-PII-270M) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — inboxpraveen/Kavach-PII-270M

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

#### 8. [inboxpraveen/Kavach-PII-270M-GGUF](https://huggingface.co/inboxpraveen/Kavach-PII-270M-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — inboxpraveen/Kavach-PII-270M-GGUF

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

#### 9. [nvidia/Nemotron-3-Content-Safety](https://huggingface.co/nvidia/Nemotron-3-Content-Safety) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — motron-open-model-license license_link: >-   https://www. - PII/Privacy md), [Safety & Security](. Here is an example of sa

| 항목 | 값 |
|---|---|
| canonical model | google/gemma-3-4b-it (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 4.3 / 131072 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 8.01 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Here is an example of sample code to run inference against the vLLM server: |
| README 인용 | Here is an example of sample code to run inference against the vLLM server: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | b47f6f6c18dc7d11a786abbbca2510cba58ede20 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [skt/A.X-K2](https://huggingface.co/skt/A.X-K2) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — Corpora collected in-house pass an internal PII masking pipeline before training: detected identifiers — pr

| 항목 | 값 |
|---|---|
| canonical model | skt/A.X-K2 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 691.69 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit, readme:korean_explicit_phrase |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 646.7 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Corpora collected in-house pass an internal PII masking pipeline before training: detected identifiers — primarily email addresses and numeric identifiers such as phone numbers — are replaced with type-specific placeholder tokens (for examp… |
| README 인용 | ** Corpora collected in-house pass an internal PII masking pipeline before training: detected identifiers — primarily email addresses and numeric identifiers such as phone numbers — are replaced with type-specific placeholder tokens (for ex… |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 52db6630c21d47cee9abdf126d121d4d3abefb33 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______
