# 골든셋 v3 검수 워크시트 — semantic_constraint (의미 + 조건)

> 상태: **초안 + 전수 스캔 + 검수 준비 완료**. 아래 점수는 Claude 의 제안이며 정답이 아니다.
>
> 판정 입력: `python test/golden/v3/tools/judge.py <query_id> <model_id> --decision approve|2|1|exclude|hold --reason "…" --by <이름>`

## sx01 — 상품 리뷰 감정 분석을 유료 서비스에 넣으려고 해요. 상업 이용이 허용되는 라이선스 계열이고 ONNX 파일이 있는 한국어 모델이면 좋겠습니다.

- 사용자 의도: 상업용 감정 분석을 ONNX 로 배포
- persona / 표현: startup_dev / 혼합형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `commercial_status` | permitted | 상업 이용이 허용되는 라이선스 계열 | 예 |
| `require_artifact` | onnx | ONNX 파일이 있는 | 예 |
| `tasks` | text-classification | 감정 분석 | 예 |

- **2점 기준**: 한국어 감정 분류 모델(조건 충족)
- **1점 기준**: 다국어 감정 분류 또는 감정이 부가 라벨

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 28 | 0 | 4 | 24 | 0 | 4 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 24 | Horizon-Labs/phishing-scam-detector-base, Horizon-Labs/prompt-injection-guard-large, NorviTech/armiger |

#### 1. [Horizon-Labs/multilingual-emotions-base](https://huggingface.co/Horizon-Labs/multilingual-emotions-base) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `model_id` — Horizon-Labs/multilingual-emotions-base

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
| 의미 claim (use_cases) | The model can be used for text classification in multiple languages. |
| README 인용 | ```python import json from huggingface_hub import hf_hub_download from transformers import pipeline  clf = pipeline("text-classification", model="Horizon-Labs/multilingual-emotions-base", top_k=None) thr = json.load(open(hf_hub_download("Ho… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 4f95ad28e89def7cce33b0589de4ed369b970deb |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [Horizon-Labs/multilingual-emotions-small](https://huggingface.co/Horizon-Labs/multilingual-emotions-small) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `model_id` — Horizon-Labs/multilingual-emotions-small

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
| 의미 claim (use_cases) | The model can be used for text classification tasks involving emotion detection in multiple languages. |
| README 인용 | ```python import json from huggingface_hub import hf_hub_download from transformers import pipeline  clf = pipeline("text-classification", model="Horizon-Labs/multilingual-emotions-small", top_k=None) thr = json.load(open(hf_hub_download("H… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | ac26dadbdafc26276e01093790104679bf33aec5 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [Horizon-Labs/multilingual-sentiment-base](https://huggingface.co/Horizon-Labs/multilingual-sentiment-base) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `model_id` — Horizon-Labs/multilingual-sentiment-base

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
| 의미 claim (use_cases) | The model can be used for text classification tasks, such as determining sentiment in various languages. |
| README 인용 | ```python from transformers import pipeline  clf = pipeline("text-classification", model="Horizon-Labs/multilingual-sentiment-base") clf(["I love this phone, the camera is amazing!", "Le colis est arrivé cassé.", "Der Termin ist am Montag."… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | fede3aec59df484af8f39535558e582c72039b63 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [Horizon-Labs/multilingual-sentiment-small](https://huggingface.co/Horizon-Labs/multilingual-sentiment-small) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `model_id` — Horizon-Labs/multilingual-sentiment-small

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
| 의미 claim (use_cases) | The model can be used for text classification tasks, such as determining sentiment in various languages. |
| README 인용 | ```python from transformers import pipeline  clf = pipeline("text-classification", model="Horizon-Labs/multilingual-sentiment-small") clf(["I love this phone, the camera is amazing!", "Le colis est arrivé cassé.", "Der Termin ist am Montag.… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | e60eb86fd9e5bdd8c097bf6d6e75dade85a1ccac |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## sx02 — Ollama 로 내 PC 에서 한국어와 영어를 번역하고 싶어요. GGUF 파일이 5GB 이하이면서 두 언어 사이를 번역할 수 있는 모델을 찾아 주세요.

- 사용자 의도: 로컬 한영 번역
- persona / 표현: local_user / 혼합형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `max_artifact_gib` | 5 | GGUF 파일이 5GB 이하 | 예 |
| `require_artifact` | gguf | Ollama 로 … GGUF | 예 |
| `tasks` | translation | 번역할 수 있는 모델 | 예 |

- **2점 기준**: 한국어↔영어 번역을 명시한 GGUF 번역 모델
- **1점 기준**: 다국어 번역 모델로 한영이 여러 언어쌍 중 하나인 경우

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 101 | 8 | 8 | 85 | 0 | 16 | ✅ | 0 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 85 | Jour/hy-mt2-1.8b-discord, mradermacher/Hy-MT2-7B-GGUF, unsloth/Hy-MT2-1.8B-GGUF |

#### 1. [DevWorld/Gemago-2b-Q4_K_M-GGUF](https://huggingface.co/DevWorld/Gemago-2b-Q4_K_M-GGUF) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음
- 근거 위치: `filter_metadata` — rimary_task translation matched_tasks translation languages en ko architecture gemma model_type gemma license apache-2.0 gemm

| 항목 | 값 |
|---|---|
| canonical model | DevWorld/Gemago-2b-Q4_K_M-GGUF (variant=false, 종류=—, 관계 근거=self, 변환 표지=Q4_) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.506 / 8192 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0, gemma / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.52 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used directly through specific usage steps. |
| README 인용 | Note: You can also use this checkpoint directly through the [usage steps](https://github. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 89ab6dd7425ae70be9a52efe8daf9200d5bcb473 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [gyung/lfm2-1.2b-koen-mt-v4-100k-GGUF](https://huggingface.co/gyung/lfm2-1.2b-koen-mt-v4-100k-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — gyung/lfm2-1.2b-koen-mt-v4-100k-GGUF

| 항목 | 값 |
|---|---|
| canonical model | gyung/lfm2-1.2b-koen-mt-v4-100k (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.17 / 128000 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.65 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Korean-English Translation |
| README 인용 | * **Purpose**: Korean-English Translation (한국어-영어 번역) |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 2a77c8c24fdb29022bcdf189fb30277fbab1b7ce |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [mradermacher/K-MT-7B-v0.1-GGUF](https://huggingface.co/mradermacher/K-MT-7B-v0.1-GGUF) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음
- 근거 위치: `filter_metadata` — rimary_task translation matched_tasks translation languages en ko architecture hunyuan-dense model_type hunyuan-dense license

| 항목 | 값 |
|---|---|
| canonical model | ThakiCloud/K-MT-7B-v0.1 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.505 / 262144 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 2.8 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Usage |
| README 인용 | ## Usage |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 1a0ae0b79ce883ae8c8f2891db27721e1b185163 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF

| 항목 | 값 |
|---|---|
| canonical model | Translation-EnKo/exaone3-instrucTrans-v2-enko-7.8b (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.818 / 8192 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 2.84 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is intended for translation tasks between English and Korean. |
| README 인용 | --- base_model: Translation-EnKo/exaone3-instrucTrans-v2-enko-7. |
| provenance status | verified 13, not_applicable 4, documented 2, unknown 4 |
| revision | bca86aaa06bb33a8ac1677bbcbeade1370692a3e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [mradermacher/exaone3-instrucTrans-v2-enko-7.8b-i1-GGUF](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-i1-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — mradermacher/exaone3-instrucTrans-v2-enko-7.8b-i1-GGUF

| 항목 | 값 |
|---|---|
| canonical model | Translation-EnKo/exaone3-instrucTrans-v2-enko-7.8b (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 7.818 / 8192 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.78 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is intended for translation tasks between English and Korean. |
| README 인용 | --- base_model: Translation-EnKo/exaone3-instrucTrans-v2-enko-7. |
| provenance status | verified 13, not_applicable 4, documented 2, unknown 4 |
| revision | fc5b58506e809ffe0fa511daf821ed39229dca9c |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [mradermacher/gaon-1.7b-v2-translate-GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-GGUF) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음
- 근거 위치: `filter_metadata` — rimary_task translation matched_tasks translation languages en ko architecture qwen3 model_type qwen3 license apache-2.0 comm

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

#### 7. [mradermacher/gaon-1.7b-v2-translate-big-GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-big-GGUF) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음
- 근거 위치: `filter_metadata` — rimary_task translation matched_tasks translation languages en ko architecture qwen3 model_type qwen3 license apache-2.0 comm

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

#### 8. [mradermacher/gaon-1.7b-v2-translate-i1-GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-i1-GGUF) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음
- 근거 위치: `filter_metadata` — rimary_task translation matched_tasks translation languages en ko architecture qwen3 model_type qwen3 license apache-2.0 comm

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

#### 9. [mradermacher/lfm2-1.2b-koen-mt-v4-100k-GGUF](https://huggingface.co/mradermacher/lfm2-1.2b-koen-mt-v4-100k-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — mradermacher/lfm2-1.2b-koen-mt-v4-100k-GGUF

| 항목 | 값 |
|---|---|
| canonical model | gyung/lfm2-1.2b-koen-mt-v4-100k (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.17 / 128000 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.45 |
| 벤치마크 근거 | 없음 |
| 의미 claim (documented_strengths) | translation |
| README 인용 | ## Usage |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 89ab316ce8876ff649b86b74da5bf8a865773942 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [mradermacher/lfm2-1.2b-koen-mt-v6.4-merged-GGUF](https://huggingface.co/mradermacher/lfm2-1.2b-koen-mt-v6.4-merged-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — mradermacher/lfm2-1.2b-koen-mt-v6.4-merged-GGUF

| 항목 | 값 |
|---|---|
| canonical model | gyung/lfm2-1.2b-koen-mt-v6.4-merged (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.17 / 128000 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.45 |
| 벤치마크 근거 | 없음 |
| 의미 claim (documented_strengths) | translation |
| README 인용 | - translation |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 13761f7ecb1653b4caf20c078c2b86396f889538 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF](https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF

| 항목 | 값 |
|---|---|
| canonical model | nayohan/llama3-8b-it-translation-general-en-ko-1sent (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 8.03 / 8192 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | llama3 / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 2.96 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is intended for translation tasks. |
| README 인용 | ## Usage |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | c2e0515dc1601b3bcdf397c0ccdabbf1a1991199 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [mradermacher/llama3-8b-it-translation-general-en-ko-1sent-i1-GGUF](https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-i1-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — mradermacher/llama3-8b-it-translation-general-en-ko-1sent-i1-GGUF

| 항목 | 값 |
|---|---|
| canonical model | nayohan/llama3-8b-it-translation-general-en-ko-1sent (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 8.03 / 8192 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | llama3 / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.88 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is intended for translation tasks between English and Korean. |
| README 인용 | --- base_model: nayohan/llama3-8b-it-translation-general-en-ko-1sent datasets: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 807be00cd1accd68a269ab4fa30b6b6d83e7b7c8 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [squarelike/Gugugo-koen-7B-V1.1-GGUF](https://huggingface.co/squarelike/Gugugo-koen-7B-V1.1-GGUF) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — squarelike/Gugugo-koen-7B-V1.1-GGUF

| 항목 | 값 |
|---|---|
| canonical model | squarelike/Gugugo-koen-7B-V1.1-GGUF (variant=false, 종류=—, 관계 근거=self, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 6.856 / 2048 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 2.7 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for translation tasks. |
| README 인용 | pipeline_tag: translation --- |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 9f5005cc4dd9d2bfe831a7a3d02555ba49845e08 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 14. [tensorblock/llama3-eng-ko-8b-sl5-GGUF](https://huggingface.co/tensorblock/llama3-eng-ko-8b-sl5-GGUF) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음
- 근거 위치: `filter_metadata` — rimary_task translation matched_tasks translation languages en ko architecture llama model_type llama license mit commercial_

| 항목 | 값 |
|---|---|
| canonical model | 4yo1/llama3-eng-ko-8b-sl5 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 8.03 / 8192 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 2.96 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for translation tasks. |
| README 인용 | pipeline_tag: translation tags: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | a90e32e476081f0dd9a15197208b44819a226130 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 15. [tensorblock/llama3-pre1-pre2-inst3-lora3-mergkit-base-GGUF](https://huggingface.co/tensorblock/llama3-pre1-pre2-inst3-lora3-mergkit-base-GGUF) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음
- 근거 위치: `filter_metadata` — rimary_task translation matched_tasks translation languages en ko architecture llama model_type llama license mit commercial_

| 항목 | 값 |
|---|---|
| canonical model | 4yo1/llama3-pre1-pre2-inst3-lora3-mergkit-base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.986 / 8192 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 2.98 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is suitable for translation tasks. |
| README 인용 | pipeline_tag: translation license: mit datasets: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 7604c5799df3bcd2ac11724af6d2f4ec8abba99d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 16. [tensorblock/llama_1-GGUF](https://huggingface.co/tensorblock/llama_1-GGUF) — Claude 제안: **1점**

- 제안 이유: 근거가 메타데이터에만 있음; 2점 조건(전용·명시 용도) 근거 없음
- 근거 위치: `filter_metadata` — rimary_task translation matched_tasks translation languages en ko architecture llama model_type llama license mit commercial_

| 항목 | 값 |
|---|---|
| canonical model | 4yo1/llama_1 (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 8.03 / 8192 |
| task | translation (matched: translation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 2.96 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is tagged for translation tasks. |
| README 인용 | pipeline_tag: translation tags: |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 159350e2df1285fa8c926b4b007797efc83aa7eb |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## sx03 — 병원 내부용 의료 Q&A 도우미를 만들려는데 GPU 가 넉넉하지 않아요. 파라미터 8B 이하인 의료 특화 한국어 생성 모델이 있을까요?

- 사용자 의도: 소형 의료 특화 생성 모델
- persona / 표현: limited_gpu / 혼합형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `max_parameters_billion` | 8 | 파라미터 8B 이하 | 예 |
| `tasks` | text-generation | Q&A 도우미(생성 모델) | 예 |

- **2점 기준**: 의료 데이터로 학습·튜닝됐다고 명시된 8B 이하 모델
- **1점 기준**: 범용 모델이지만 의료 용도를 명시했거나 의료 모델의 변환본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 968 | 4 | 8 | 955 | 1 | 13 | ✅ | 261 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 955 | LiquidAI/LFM2.5-1.2B-Thinking-MLX-4bit, saidutta69/granite-4.2-3b-heretic, unsloth/LFM2.5-1.2B-Thinking-GGUF |

#### 1. [Aikyam-Lab/CURE-MED-1.5B](https://huggingface.co/Aikyam-Lab/CURE-MED-1.5B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — Aikyam-Lab/CURE-MED-1.5B

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-3B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.544 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 5.75 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model enhances logical correctness and language stability in healthcare applications. |
| README 인용 | 5B-instruct using a curriculum-informed reinforcement learning framework to enhance logical correctness and language stability in healthcare applications. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | bd7bd9cef4ba14f5c10379c8bbb7c45988e0bc61 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [Aikyam-Lab/CURE-MED-3B](https://huggingface.co/Aikyam-Lab/CURE-MED-3B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — Aikyam-Lab/CURE-MED-3B

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen2.5-3B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 3.086 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 11.5 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model enhances logical correctness and language stability in healthcare applications. |
| README 인용 | 5-3B-instruct using a curriculum-informed reinforcement learning framework to enhance logical correctness and language stability in healthcare applications. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | f4fc53cdf0a1ba8a54388e53d75d3951f0b5cb00 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [Bingsu/exaone-3.0-7.8b-it](https://huggingface.co/Bingsu/exaone-3.0-7.8b-it) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — 업에서 높은 정확도\n\n4. 활용 사례:\n   - 고객 지원 챗봇\n   - 법률 문서 요약\n   - 의료 정보 제공\n\n5. 기술적 세부 사항:\n   - 7.8B instruction 튜닝 파라미터\n   -

| 항목 | 값 |
|---|---|
| canonical model | Bingsu/exaone-3.0-7.8b-it (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 7.818 / 4096 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 4.44 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for customer support chatbots. |
| README 인용 | %}{{ '\n' }}{% else %}{{ '[\|endofturn\|]\n' }}{% endif %}{% endfor %}{% if add_generation_prompt %}{{ '[\|assistant\|]' }}{% endif %}", 'general.license.link': 'LICENSE', 'general.license': 'other', 'llama.feed_forward_length': '14336', 'l… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 6c2abf0e8653f179ad9acbabdbd8c3c15eade116 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [hoagngn/medical-title-qwen3-4b-chat-v1](https://huggingface.co/hoagngn/medical-title-qwen3-4b-chat-v1) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — hoagngn/medical-title-qwen3-4b-chat-v1

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-4B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 4.022 / 131072 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 3.99 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can generate conversation titles in various languages, including Vietnamese. |
| README 인용 | ```python import torch from transformers import AutoModelForCausalLM, AutoTokenizer from peft import PeftModel  repo_id = "YOUR_REPO_ID" tokenizer = AutoTokenizer.from_pretrained(repo_id) base = AutoModelForCausalLM.from_pretrained(     "Qw… |
| provenance status | verified 13, not_applicable 4, documented 2, unknown 4 |
| revision | 8479a8ba4e0a4c2719cdd6aa1abf0d57b6ea0a44 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [mradermacher/CURE-MED-1.5B-GGUF](https://huggingface.co/mradermacher/CURE-MED-1.5B-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — mradermacher/CURE-MED-1.5B-GGUF

| 항목 | 값 |
|---|---|
| canonical model | Aikyam-Lab/CURE-MED-1.5B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.544 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.63 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for more details, including on how to concatenate multi-part files. |
| README 인용 | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 4f51cf2b9bab0964cad08ca55efd93639a9d07b6 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [mradermacher/CURE-MED-1.5B-i1-GGUF](https://huggingface.co/mradermacher/CURE-MED-1.5B-i1-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — mradermacher/CURE-MED-1.5B-i1-GGUF

| 항목 | 값 |
|---|---|
| canonical model | Aikyam-Lab/CURE-MED-1.5B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.544 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.41 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for more details, including on how to concatenate multi-part files. |
| README 인용 | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 9fc6adeb13e2d307d3c3fd0f30c42c73b2e8c0ef |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [mradermacher/CURE-MED-3B-GGUF](https://huggingface.co/mradermacher/CURE-MED-3B-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — mradermacher/CURE-MED-3B-GGUF

| 항목 | 값 |
|---|---|
| canonical model | Aikyam-Lab/CURE-MED-3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 3.086 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.19 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.) for more details, including on how to concatenate multi-part files. |
| README 인용 | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 9d1ab9a252e0d4f36b2c1da5c27942d3333de828 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [mradermacher/CURE-MED-3B-i1-GGUF](https://huggingface.co/mradermacher/CURE-MED-3B-i1-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — mradermacher/CURE-MED-3B-i1-GGUF

| 항목 | 값 |
|---|---|
| canonical model | Aikyam-Lab/CURE-MED-3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 3.086 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.74 |
| 벤치마크 근거 | 없음 |
| 의미 claim (documented_strengths) | text-generation |
| README 인용 | ## Usage |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | c1f578dfa23d4a05c1a1e3609465c19483ff54f1 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [mradermacher/CURE-MED-7B-GGUF](https://huggingface.co/mradermacher/CURE-MED-7B-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — mradermacher/CURE-MED-7B-GGUF

| 항목 | 값 |
|---|---|
| canonical model | Aikyam-Lab/CURE-MED-7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 7.616 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 2.81 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.) for more details, including on how to concatenate multi-part files. |
| README 인용 | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | aae34989b7d2446e54d190df1d17b15df39cab48 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [mradermacher/CURE-MED-7B-i1-GGUF](https://huggingface.co/mradermacher/CURE-MED-7B-i1-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — mradermacher/CURE-MED-7B-i1-GGUF

| 항목 | 값 |
|---|---|
| canonical model | Aikyam-Lab/CURE-MED-7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 7.616 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.77 |
| 벤치마크 근거 | 없음 |
| 의미 claim (documented_strengths) | text-generation |
| README 인용 | ## Usage |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 6c20e24d88fa76702c6212bcae097a05dcd8d1d4 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [mradermacher/Synin-Helix-MED-GGUF](https://huggingface.co/mradermacher/Synin-Helix-MED-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — mradermacher/Synin-Helix-MED-GGUF

| 항목 | 값 |
|---|---|
| canonical model | Synin/Synin-Helix-MED (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 7.616 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 2.81 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.) for more details, including on how to concatenate multi-part files. |
| README 인용 | If you are unsure how to use GGUF files, refer to one of [TheBloke's READMEs](https://huggingface. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 7fb6affb45ec07958b72443a99b52c0b8529b1ba |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [mradermacher/Synin-Helix-MED-i1-GGUF](https://huggingface.co/mradermacher/Synin-Helix-MED-i1-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — mradermacher/Synin-Helix-MED-i1-GGUF

| 항목 | 값 |
|---|---|
| canonical model | Synin/Synin-Helix-MED (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=-i1-) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 7.616 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.77 |
| 벤치마크 근거 | 없음 |
| 의미 claim (documented_strengths) | text-generation |
| README 인용 | ## Usage |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | f8ce3fcad4faf07e5c5ce748c7b8fc9f2d275b73 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [mulkzz/RuBio-4B](https://huggingface.co/mulkzz/RuBio-4B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — mulkzz/RuBio-4B

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3.5-4B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 4.66 / 262144 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 8.68 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is suitable for text generation tasks. |
| README 인용 | pipeline_tag: text-generation tags: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | b3d7b608251dfc9879420f8125d9dfecf22e978f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## sx04 — 계약서처럼 긴 법률 문서를 통째로 임베딩해서 검색하려고 해요. 최소 8K 토큰을 한 번에 넣을 수 있는 법률 특화 한국어 임베딩 모델이 필요해요.

- 사용자 의도: 긴 법률 문서용 임베딩
- persona / 표현: startup_dev / 혼합형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `min_context_length` | 8192 | 최소 8K 토큰을 한 번에 | 예 |
| `tasks` | sentence-similarity, feature-extraction | 임베딩 모델 | 예 |

- **2점 기준**: 법률 문서 검색용으로 학습된 8K 이상 임베딩 모델
- **1점 기준**: 범용 임베딩이지만 법률 용도·평가가 언급되거나 변환본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 152 | 2 | 1 | 148 | 1 | 4 | ✅ | 10 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 148 | batiai/Qwen3-Embedding-8B-GGUF, kiwi-farm/kiwi-coco-lm-base-generator, microsoft/harrier-oss-v1-0.6b |

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

#### 3. [sionic-ai/comsat-embed-ko-8b-preview](https://huggingface.co/sionic-ai/comsat-embed-ko-8b-preview) — Claude 제안: **1점**

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

#### 4. [ysmeta/EVE-Embed-1.1-Legal](https://huggingface.co/ysmeta/EVE-Embed-1.1-Legal) — Claude 제안: **2점**

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

## sx05 — 콜센터 통화를 실시간으로 받아 적는 서비스를 상업적으로 운영하려고 해요. 동시 통화가 많아서 파라미터 1B 이하로 가볍고, 상업 이용 허용 라이선스 계열인 스트리밍 음성 인식 모델이 필요해요.

- 사용자 의도: 상업용 경량 스트리밍 STT
- persona / 표현: korean_service_planner / 목적형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `commercial_status` | permitted | 상업 이용 허용 라이선스 계열 | 예 |
| `max_parameters_billion` | 1 | 파라미터 1B 이하 | 예 |
| `tasks` | automatic-speech-recognition | 받아 적는(음성 인식) | 예 |

- **2점 기준**: 스트리밍·실시간 인식을 명시한 음성 인식 모델
- **1점 기준**: 저지연을 언급하지만 스트리밍 지원이 불명확하거나 변환본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 72 | 0 | 4 | 65 | 3 | 7 | ✅ | 96 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 65 | lipik/whisper-large-v3-turbo-gguf, loom-ai-org/whisper-small-loom, xkeyC/whisper-large-v3-turbo-gguf |

같은 canonical family 후보가 3개 이상: nvidia/nemotron-3.5-asr-streaming-0.6b 3

#### 1. [avericaai/Qwen3-ASR-0.6B-gguf](https://huggingface.co/avericaai/Qwen3-ASR-0.6B-gguf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — pported Dialects \| Inference Mode \| Audio Types \| Note that streaming inference does not support batch inference or returning timestamps.

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

#### 2. [cstr/nemotron-3.5-asr-streaming-0.6b-GGUF](https://huggingface.co/cstr/nemotron-3.5-asr-streaming-0.6b-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — cstr/nemotron-3.5-asr-streaming-0.6b-GGUF

| 항목 | 값 |
|---|---|
| canonical model | nvidia/nemotron-3.5-asr-streaming-0.6b (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.638 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | openmdw-1.1 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.38 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Usage with CrispASR |
| README 인용 | ## Usage with CrispASR |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | f6f18e48c30035807b6ca0cdb965654fa02dbf69 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [cstr/nemotron-3.5-asr-streaming-GGUF](https://huggingface.co/cstr/nemotron-3.5-asr-streaming-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — cstr/nemotron-3.5-asr-streaming-GGUF

| 항목 | 값 |
|---|---|
| canonical model | nvidia/nemotron-3.5-asr-streaming-0.6b (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.638 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | openmdw-1.1 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.38 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used with CrispASR. |
| README 인용 | ## Usage with CrispASR |
| provenance status | verified 12, not_applicable 4, documented 5, unknown 2 |
| revision | f300f4f36b388c5f22f810c4e8503359fb9c1ce7 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [handy-computer/Qwen3-ASR-0.6B-gguf](https://huggingface.co/handy-computer/Qwen3-ASR-0.6B-gguf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — pported Dialects \| Inference Mode \| Audio Types \| Note that streaming inference does not support batch inference or returning timestamps.

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

#### 5. [memoravox/Qwen3-ASR-0.6B-gguf](https://huggingface.co/memoravox/Qwen3-ASR-0.6B-gguf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — h single model and support transcribe long audio. Note that streaming inference does not support batch inference or returning timestamps.

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-0.6B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.782 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.79 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | For more detailed usage examples, please refer to the example code. |
| README 인용 | For more detailed usage examples, please refer to the [example code](https://github. |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 39aee80e6b9acaf8a087054bcb4de37ba389ac7b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [voconly-org/nemotron-3.5-asr-streaming-0.6b-gguf](https://huggingface.co/voconly-org/nemotron-3.5-asr-streaming-0.6b-gguf) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — voconly-org/nemotron-3.5-asr-streaming-0.6b-gguf

| 항목 | 값 |
|---|---|
| canonical model | nvidia/nemotron-3.5-asr-streaming-0.6b (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.638 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | openmdw-1.1 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.46 |
| 벤치마크 근거 | 없음 |
| 의미 claim (documented_strengths) | automatic-speech-recognition |
| README 인용 | - automatic-speech-recognition |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 04f5d5db715acd085490116682742d415e4b2585 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [voconly-org/sensevoice-small-gguf](https://huggingface.co/voconly-org/sensevoice-small-gguf) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — meeting transcription, multilingual transcription Supports real-time streaming transcription High-accuracy recognition, real-time transcri

| 항목 | 값 |
|---|---|
| canonical model | voconly-org/sensevoice-small-gguf (variant=false, 종류=—, 관계 근거=self, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.234 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.16 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Speech-to-text, subtitle generation, meeting transcription, multilingual transcription |
| README 인용 | - **Use Cases**: Speech-to-text, subtitle generation, meeting transcription, multilingual transcription |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 6394f6d5b1ca5d7b03e6bb7ac6f64d18f082c19e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## sx06 — 파라미터 4B 이하 비전-언어 모델 중에서 한국어 OCR 용도로 학습된 걸 찾고 있습니다.

- 사용자 의도: 소형 OCR 특화 VLM
- persona / 표현: ml_engineer / 기술형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `max_parameters_billion` | 4 | 파라미터 4B 이하 | 예 |
| `tasks` | image-text-to-text | 비전-언어 모델 | 예 |

- **2점 기준**: OCR 을 주 용도로 명시한 4B 이하 VLM
- **1점 기준**: OCR 이 부가 용도이거나 변환본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 146 | 7 | 12 | 122 | 5 | 24 | ✅ | 41 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 122 | EnlistedGhost/Ministral-3-3B-Reasoning-2512-GGUF, LiquidAI/LFM2-VL-3B, bartowski/mistralai_Ministral-3-3B-Reasoning-2512-GGUF |

같은 canonical family 후보가 3개 이상: LiquidAI/LFM2.5-VL-3B 4, zai-org/GLM-OCR 4

#### 1. [AX1Y2JP/LFM2.5-VL-3B-heretic-GGUF](https://huggingface.co/AX1Y2JP/LFM2.5-VL-3B-heretic-GGUF) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — otive applications, batch processing scanned documents with OCR with layout information for turning PDFs into searchable te

| 항목 | 값 |
|---|---|
| canonical model | heretic-org/LFM2.5-VL-3B-heretic (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=heretic) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.697 / 128000 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.48 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Recommended for single-turn, high-throughput, low-latency tasks such as near-realtime object detection and on-device translation. |
| README 인용 | We recommend using it for single-turn, high-throughput, low-latency tasks; for example, for near-realtime object detection in automotive applications, batch processing scanned documents with OCR with layout information for turning PDFs into… |
| provenance status | verified 13, not_applicable 4, documented 5, unknown 1 |
| revision | 0b843ae2d2276eb3b05b727c81c1ac7dc9a1bbaf |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 2. [EZCon/GLM-OCR-4bit-g32-mxfp4-mixed_4_8-mlx](https://huggingface.co/EZCon/GLM-OCR-4bit-g32-mxfp4-mixed_4_8-mlx) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — EZCon/GLM-OCR-4bit-g32-mxfp4-mixed_4_8-mlx

| 항목 | 값 |
|---|---|
| canonical model | zai-org/GLM-OCR (variant=true, 종류=4bit, 관계 근거=base_model_tag, 변환 표지=4bit) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.107 / 655380 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.28 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is designed for image-to-text tasks. |
| README 인용 | library_name: mlx base_model: zai-org/GLM-OCR pipeline_tag: image-text-to-text tags: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 975d1d941c7d9edc7560740ce87454a747eafdf6 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [EZCon/GLM-OCR-8bit-mlx](https://huggingface.co/EZCon/GLM-OCR-8bit-mlx) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — EZCon/GLM-OCR-8bit-mlx

| 항목 | 값 |
|---|---|
| canonical model | zai-org/GLM-OCR (variant=true, 종류=8bit, 관계 근거=base_model_tag, 변환 표지=8bit) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.107 / 655380 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.48 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is used in the image-text-to-text pipeline. |
| README 인용 | library_name: mlx base_model: zai-org/GLM-OCR pipeline_tag: image-text-to-text tags: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 87e52ef7719b1f266810b6d633c312a9b080ccba |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 4. [EZCon/GLM-OCR-mlx](https://huggingface.co/EZCon/GLM-OCR-mlx) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — EZCon/GLM-OCR-mlx

| 항목 | 값 |
|---|---|
| canonical model | zai-org/GLM-OCR (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=mlx) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 1.107 / 655380 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 2.06 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is used for image-to-text tasks. |
| README 인용 | library_name: mlx base_model: zai-org/GLM-OCR pipeline_tag: image-text-to-text tags: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 58a486a4a8ad4a8ad9aec469d1810681927bdffa |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [LiquidAI/LFM2.5-VL-3B](https://huggingface.co/LiquidAI/LFM2.5-VL-3B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — bject detection and batch processing scanned documents with OCR. Pipeline tag indicates it is designed for image-text-to-te

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/LFM2.5-2.6B-Base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 3.123 / 32768 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 5.82 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Recommended for tasks like near-realtime object detection and batch processing scanned documents with OCR. |
| README 인용 | We recommend using it for single-turn, high-throughput, low-latency tasks; for example, for near-realtime object detection in automotive applications, batch processing scanned documents with OCR with layout information for turning PDFs into… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 35a118d938ce6d123ac2d371649f24a8efb69058 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [MuXodious/LFM2.5-VL-3B-absolute-heresy](https://huggingface.co/MuXodious/LFM2.5-VL-3B-absolute-heresy) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — otive applications, batch processing scanned documents with OCR with layout information for turning PDFs into searchable te

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/LFM2.5-VL-3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 3.123 / 128000 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 5.82 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Recommended for near-realtime object detection in automotive applications. |
| README 인용 | We recommend using it for single-turn, high-throughput, low-latency tasks; for example, for near-realtime object detection in automotive applications, batch processing scanned documents with OCR with layout information for turning PDFs into… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 8093563afeb4471ccd02579fd027cb383cbec7eb |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [NCSOFT/VARCO-VISION-2.0-1.7B-OCR](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B-OCR) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — NCSOFT/VARCO-VISION-2.0-1.7B-OCR

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-1.7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.124 / 40960 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 3.96 |
| 벤치마크 근거 | 점수 3건 저장 |
| 의미 claim (use_cases) | Image-text-to-text pipeline tag. |
| README 인용 | pipeline_tag: image-text-to-text language: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 5c83a19639613ee6ea8bc24070ca1b38305aae69 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 8. [OpenLLM-Korea/VARCO-VISION-2.0-1.7B-OCR](https://huggingface.co/OpenLLM-Korea/VARCO-VISION-2.0-1.7B-OCR) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — OpenLLM-Korea/VARCO-VISION-2.0-1.7B-OCR

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-1.7B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.124 / 40960 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 3.96 |
| 벤치마크 근거 | 점수 3건 저장 |
| 의미 claim (use_cases) | Image-text-to-text pipeline tag. |
| README 인용 | pipeline_tag: image-text-to-text language: |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | f740294ba9becc880f68cefb17e85d403d1eaf95 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [batiai/batisee](https://huggingface.co/batiai/batisee) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `canonical_model_id` — baidu/Unlimited-OCR

| 항목 | 값 |
|---|---|
| canonical model | baidu/Unlimited-OCR (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.935 / 32768 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 3.63 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | base_model: baidu/Unlimited-OCR |
| README 인용 | base_model: baidu/Unlimited-OCR pipeline_tag: image-text-to-text library_name: llama. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | fc15529aebf33f4beef7efe5b09b4046463f66f2 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [cstr/internvl2.5-2b-crispembed-GGUF](https://huggingface.co/cstr/internvl2.5-2b-crispembed-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — library can be used to initialize and utilize the model for OCR tasks, demonstrating its practical application in recognizi

| 항목 | 값 |
|---|---|
| canonical model | OpenGVLab/InternVL2_5-2B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.206 / — |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 1.4 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is designed for image-text-to-text tasks, making it suitable for applications that require understanding and generating text based on image inputs. |
| README 인용 | base_model: OpenGVLab/InternVL2_5-2B library_name: gguf pipeline_tag: image-text-to-text --- |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | f57a449655f31262a83db61ca62be7f69d118502 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 11. [heretic-org/LFM2.5-VL-3B-heretic](https://huggingface.co/heretic-org/LFM2.5-VL-3B-heretic) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — bject detection and batch processing scanned documents with OCR. Pipeline tag indicates it is designed for image-text-to-te

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/LFM2.5-VL-3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=heretic) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 3.123 / 128000 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 5.82 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Recommended for tasks like near-realtime object detection and batch processing scanned documents with OCR. |
| README 인용 | We recommend using it for single-turn, high-throughput, low-latency tasks; for example, for near-realtime object detection in automotive applications, batch processing scanned documents with OCR with layout information for turning PDFs into… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 124badfb974dbaa2112fbdd3c751ecd1b650cf68 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [kakaocorp/kanana-1.5-v-3b-instruct](https://huggingface.co/kakaocorp/kanana-1.5-v-3b-instruct) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — ated without the use of any auxiliary tools (e.g., external OCR engines or Lens features), as such tools are not publicly a

| 항목 | 값 |
|---|---|
| canonical model | kakaocorp/kanana-1.5-v-3b-instruct (variant=false, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 3.668 / 32768 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 6.83 |
| 벤치마크 근거 | 점수 4건 저장 |
| 의미 claim (use_cases) | pipeline_tag: image-text-to-text |
| README 인용 | pipeline_tag: image-text-to-text library_name: transformers --- |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 2e00ef13ccec2e99459a8eada18a1bfd05bff44b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [localdeel/ko-hand-ocr-vl](https://huggingface.co/localdeel/ko-hand-ocr-vl) — Claude 제안: **2점**

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

#### 14. [localdeel/ko-hand-ocr-vl-GGUF](https://huggingface.co/localdeel/ko-hand-ocr-vl-GGUF) — Claude 제안: **1점**

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

#### 15. [nopesadly/GLM-OCR-Q4_K_M.gguf](https://huggingface.co/nopesadly/GLM-OCR-Q4_K_M.gguf) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `model_id` — nopesadly/GLM-OCR-Q4_K_M.gguf

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

#### 16. [npario/LFM2.5-VL-3B-GGUF](https://huggingface.co/npario/LFM2.5-VL-3B-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — e object detection, batch processing scanned documents with OCR, or on-device translation. Pipeline tag is image-text-to-te

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/LFM2.5-VL-3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.697 / 128000 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.94 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Recommended for single-turn, high-throughput, low-latency tasks such as near-realtime object detection, batch processing scanned documents with OCR, or on-device translation. |
| README 인용 | We recommend using it for single-turn, high-throughput, low-latency tasks; for example, for near-realtime object detection in automotive applications, batch processing scanned documents with OCR with layout information for turning PDFs into… |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 9ad4c12abfcb8cd335b39cf05f9a743b586932e3 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 17. [saidutta69/LFM2.5-VL-3B-heretic](https://huggingface.co/saidutta69/LFM2.5-VL-3B-heretic) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — aving the rest of the network - including the vision tower, OCR behaviour and tool-call format - untouched. **This is not A

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/LFM2.5-VL-3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=heretic) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 3.123 / 32768 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 1.02 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for image-text tasks, such as describing images in natural language. |
| README 인용 | ```python # transformers (vision-language), needs transformers>=5.0.0 from transformers import AutoProcessor, AutoModelForImageTextToText  model_name = "saidutta69/LFM2.5-VL-3B-heretic" model = AutoModelForImageTextToText.from_pretrained(mo… |
| provenance status | verified 12, not_applicable 3, documented 4, unknown 3, conflict 1 |
| revision | afd3a6ae3b651cde6e9dfb5db4f38f082e6a0cd9 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 18. [saidutta69/Qwen3-VL-2B-Instruct-heretic](https://huggingface.co/saidutta69/Qwen3-VL-2B-Instruct-heretic) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — ation and grounding behavior. It supports image, video, and OCR input with spatial grounding. Performance with refusals at

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-VL-2B-Instruct (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=heretic) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.128 / 262144 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 0.72 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Transcribing text from images and describing layouts. |
| README 인용 | ```python # transformers from transformers import AutoProcessor, AutoModelForImageTextToText  model_name = "saidutta69/Qwen3-VL-2B-Instruct-heretic" model = AutoModelForImageTextToText.from_pretrained(model_name, dtype="auto", device_map="a… |
| provenance status | verified 12, not_applicable 3, documented 4, unknown 3, conflict 1 |
| revision | 14f6eb1768b311e3a7b98a873394f90d6218a1c9 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 19. [schift-io/schift-ocr-1-beta](https://huggingface.co/schift-io/schift-ocr-1-beta) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — schift-io/schift-ocr-1-beta

| 항목 | 값 |
|---|---|
| canonical model | baidu/Unlimited-OCR (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 3.639 / 32768 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 6.78 |
| 벤치마크 근거 | 점수 1건 저장 |
| 의미 claim (benchmarks) | Lower is better. |
| README 인용 | --- license: mit base_model: baidu/Unlimited-OCR library_name: transformers pipeline_tag: image-text-to-text language: |
| provenance status | verified 13, not_applicable 3, documented 5, unknown 2 |
| revision | 8fc26dce9ef6c0307a9067ee39a97ae15ccd1cbf |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 20. [thelamapi/next2-air-GGUF](https://huggingface.co/thelamapi/next2-air-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — isual encoder, allowing it to process spatial intelligence, OCR, and document understanding tasks efficiently. Benchmark Pe

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

#### 21. [thelamapi/next2-air-i1-GGUF](https://huggingface.co/thelamapi/next2-air-i1-GGUF) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — isual encoder, allowing it to process spatial intelligence, OCR, and document understanding tasks efficiently. Benchmark Pe

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

#### 22. [unsloth/LFM2.5-VL-3B](https://huggingface.co/unsloth/LFM2.5-VL-3B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — e object detection, batch processing scanned documents with OCR, and on-device translation. Pipeline tag is image-text-to-t

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/LFM2.5-VL-3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 3.123 / 128000 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 5.82 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Recommended for single-turn, high-throughput, low-latency tasks such as near-realtime object detection, batch processing scanned documents with OCR, and on-device translation. |
| README 인용 | We recommend using it for single-turn, high-throughput, low-latency tasks; for example, for near-realtime object detection in automotive applications, batch processing scanned documents with OCR with layout information for turning PDFs into… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 782e9e7ea436e51cd59e00c2a4287a3c3da48e63 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 23. [unsloth/LFM2.5-VL-3B-GGUF](https://huggingface.co/unsloth/LFM2.5-VL-3B-GGUF) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — otive applications, batch processing scanned documents with OCR with layout information for turning PDFs into searchable te

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/LFM2.5-VL-3B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 2.697 / 128000 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.94 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Recommended for single-turn, high-throughput, low-latency tasks such as near-realtime object detection, batch processing scanned documents, or on-device translation. |
| README 인용 | We recommend using it for single-turn, high-throughput, low-latency tasks; for example, for near-realtime object detection in automotive applications, batch processing scanned documents with OCR with layout information for turning PDFs into… |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 22f063714556bd4daa81c40dc1ff15ca37ae92ea |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 24. [useful-quants/LFM2.5-VL-3B-NVFP4-FP8-Mixed](https://huggingface.co/useful-quants/LFM2.5-VL-3B-NVFP4-FP8-Mixed) — Claude 제안: **1점**

- 제안 이유: 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — xact deterministic accuracy parity on standard VQA, invoice/document OCR, and high-resolution multi-tile visual reasoning benchmarks

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/LFM2.5-VL-3B (variant=true, 종류=fp8, nvfp4, 관계 근거=base_model_tag, 변환 표지=quant) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 2.133 / 128000 |
| task | image-text-to-text (matched: image-text-to-text) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 2.84 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | pipeline_tag: image-text-to-text |
| README 인용 | pipeline_tag: image-text-to-text base_model: LiquidAI/LFM2. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 57c6e203f0897798fe56fa2831beba0553bd57cc |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

## sx07 — 게임 커뮤니티 채팅 필터를 상용으로 붙이려고 해요. 관리자 승인 없이 바로 받을 수 있고 상업 이용 허용 라이선스 계열인 한국어 욕설·혐오 표현 분류 모델을 찾아 주세요.

- 사용자 의도: 상업용·즉시 다운로드 가능한 유해 표현 분류
- persona / 표현: backend_dev / 혼합형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `commercial_status` | permitted | 상업 이용 허용 라이선스 계열 | 예 |
| `exclude_gated` | true | 관리자 승인 없이 바로 받을 수 있고 | 예 |
| `tasks` | text-classification | 분류 모델 | 예 |

- **2점 기준**: 한국어 욕설·혐오 표현 분류 모델
- **1점 기준**: 다국어 유해성 분류 또는 인접 범주(편향)

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 115 | 0 | 10 | 103 | 2 | 12 | ✅ | 26 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 103 | Horizon-Labs/hallucination-guard-base, clapAI/modernBERT-base-multilingual-sentiment, fr0stbit3/laya-multilingual-gguf |

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

#### 10. [knowledgator/opir-multitask-multilang-v1.0](https://huggingface.co/knowledgator/opir-multitask-multilang-v1.0) — Claude 제안: **1점**

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

#### 11. [musubilabs/policylm-1.7b](https://huggingface.co/musubilabs/policylm-1.7b) — Claude 제안: **1점**

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

#### 12. [vllm-sr/Vela-1.0-Encoder-307M-Shield](https://huggingface.co/vllm-sr/Vela-1.0-Encoder-307M-Shield) — Claude 제안: **1점**

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

## sx08 — 유료 사내 검색 SaaS 에 reranker 를 붙이려고 합니다. 라이선스가 상업 이용 허용 계열인 한국어 질의-문서 재순위(cross-encoder) 모델이 있을까요?

- 사용자 의도: 상업용 reranker
- persona / 표현: ml_engineer / 기술형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `commercial_status` | permitted | 상업 이용 허용 계열 | 예 |

- **2점 기준**: 재순위용 reranker·cross-encoder 로 명시된 모델
- **1점 기준**: 다국어 reranker 또는 변환본

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 2,363 | 2 | 7 | 2,351 | 3 | 12 | ✅ | 244 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 2,351 | AMAImedia/DeepSeek-V4.1-Flash-1017-FP8-GGUF, bartowski/mistralai_Ministral-3-8B-Reasoning-2512-GGUF, lmstudio-community/granite-4.2-3b-MLX-8bit |

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

#### 10. [maidalun1020/bce-reranker-base_v1](https://huggingface.co/maidalun1020/bce-reranker-base_v1) — Claude 제안: **1점**

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

#### 11. [vllm-sr/mmbert-rerank-32k-2d-matryoshka](https://huggingface.co/vllm-sr/mmbert-rerank-32k-2d-matryoshka) — Claude 제안: **1점**

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

#### 12. [whybe-choi/kovre](https://huggingface.co/whybe-choi/kovre) — Claude 제안: **2점**

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

## sx09 — 뉴스 기사를 짧게 요약해 주는 앱을 개인적으로 만들어 보고 있어요. 파라미터 1B 이하로 가벼운 한국어 요약 모델이 있을까요?

- 사용자 의도: 소형 한국어 요약 모델
- persona / 표현: local_user / 목적형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `max_parameters_billion` | 1 | 파라미터 1B 이하 | 예 |

- **2점 기준**: 한국어 요약용으로 학습된 1B 이하 모델
- **1점 기준**: 다국어 요약 또는 요약이 부가 기능

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 720 | 4 | 9 | 697 | 10 | 23 | ✅ | 586 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 697 | muahseol/qwen3.5-0.8b-commerce-sft, mukel/Qwen2.5-0.5B-Instruct-GGUF, saidutta69/LFM2.5-230M-heretic |

#### 1. [EbanLee/kobart-summary-v3](https://huggingface.co/EbanLee/kobart-summary-v3) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — EbanLee/kobart-summary-v3

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

#### 2. [Horizon-Labs/multilingual-prompt-task-complexity-small](https://huggingface.co/Horizon-Labs/multilingual-prompt-task-complexity-small) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `semantic_metadata` — classifies various task types including open QA, closed QA, summarization, text generation, code generation, and chatbot. The

| 항목 | 값 |
|---|---|
| canonical model | jhu-clsp/mmBERT-small (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.141 / 8192 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | onnx, safetensors / 0.52 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for text classification tasks, such as determining the complexity and reasoning involved in a given prompt. |
| README 인용 | ```python from transformers import pipeline  clf = pipeline("text-classification", model="Horizon-Labs/multilingual-prompt-task-complexity-small", top_k=None) s = {d["label"]: d["score"] for d in clf("Écris une fonction Python qui vérifie s… |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 48c908481bc6220ccbb252192f8f5bdd4a7e0993 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 3. [Manav2op/verdict-small](https://huggingface.co/Manav2op/verdict-small) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `semantic_metadata` — y were held out. The results of the model's performance are summarized in the document.

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

#### 4. [Mungert/rwkv7-0.4B-world-GGUF](https://huggingface.co/Mungert/rwkv7-0.4B-world-GGUF) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델; 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — t use case for BF16 is when BF16 acceleration is available. Summary table provides insights on model format selection. The mod

| 항목 | 값 |
|---|---|
| canonical model | BlinkDL/rwkv-7-world (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.451 / 1048576 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.18 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Quantization reduces model size and memory usage while maintaining as much accuracy as possible. |
| README 인용 | Quantization reduces model size and memory usage while maintaining as much accuracy as possible. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | 926e35b60dad1336ed3700cc47752f01be20bc3f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 5. [Mungert/rwkv7-191M-world-GGUF](https://huggingface.co/Mungert/rwkv7-191M-world-GGUF) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델; 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — e-off: Lower accuracy compared to higher-bit quantizations. Summary Table: Model Format Selection

| 항목 | 값 |
|---|---|
| canonical model | BlinkDL/rwkv-7-world (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=GGUF) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.191 / 1048576 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.1 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Quantization reduces model size and memory usage while maintaining as much accuracy as possible. |
| README 인용 | Quantization reduces model size and memory usage while maintaining as much accuracy as possible. |
| provenance status | verified 13, not_applicable 4, documented 4, unknown 2 |
| revision | e49a4381662e78e48ca3079770a6a47e203c22ab |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 6. [OptGear/Opt.Gear-1B](https://huggingface.co/OptGear/Opt.Gear-1B) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — can be used for Korean-English bilingual understanding and summarization. It is suitable for task-specific fine-tuning and re

| 항목 | 값 |
|---|---|
| canonical model | OptGear/Opt.Gear-1B (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.842 / 65536 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | cc-by-nc-sa-4.0 / prohibited / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 1.57 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used for Korean-English bilingual understanding and summarization. |
| README 인용 | with mathematical text (~2%). It is best suited for Korean-English bilingual understanding, summarization, rewriting, and instruction following.  4. **Not intended for code generation**: The pre-training corpus deliberately excludes code da… |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | b2d46ecc4a021c48ae21807c406692f6dbdb966d |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 7. [Squezilia/xlm-r-r4s-large](https://huggingface.co/Squezilia/xlm-r-r4s-large) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `semantic_metadata` — in reasoning requirement classification. Overall multi-task summary with various performance metrics.

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

#### 8. [TYTTYTTYT/mgpt2-124m-mc4](https://huggingface.co/TYTTYTTYT/mgpt2-124m-mc4) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `semantic_metadata` — been finetuned on SIB-200 and XNLI benchmarks. Results are summarized in a table format.

| 항목 | 값 |
|---|---|
| canonical model | TYTTYTTYT/mgpt2-124m-mc4 (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.124 / 1024 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.46 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used with the original English GPT-2 BPE vocabulary tokenizer. |
| README 인용 | ```python from transformers import AutoModelForCausalLM, AutoTokenizer  tok = AutoTokenizer.from_pretrained("TYTTYTTYT/mgpt2-124m-mc4") model = AutoModelForCausalLM.from_pretrained("TYTTYTTYT/mgpt2-124m-mc4") ``` |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 78b82b0759f84cca6859379215e134f947f39e9a |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 9. [agentlans/multilingual-e5-small-aligned-sentiment](https://huggingface.co/agentlans/multilingual-e5-small-aligned-sentiment) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — ions  --- license: mit language: ## Key Features <details> <summary>Click here for the 10 original texts and their translation

| 항목 | 값 |
|---|---|
| canonical model | agentlans/multilingual-e5-small-aligned (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.118 / 512 |
| task | text-classification (matched: text-classification) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.44 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model can be used to assess the sentiment of multilingual text. |
| README 인용 | - Assessing the sentiment of multilingual text |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | c1260e903fc8aa47acfb10ac64c5461dc333b5ea |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 10. [avericaai/Qwen3-ASR-0.6B-gguf](https://huggingface.co/avericaai/Qwen3-ASR-0.6B-gguf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — ease refer to the [example code](https://github. <details> <summary>ASR Benchmarks on Public Datasets (WER ↓)</summary> Inheri

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

#### 11. [ddobokki/klue-roberta-small-nli-sts](https://huggingface.co/ddobokki/klue-roberta-small-nli-sts) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `semantic_metadata` — uclidean distances among others. The model's performance is summarized in a table format.

| 항목 | 값 |
|---|---|
| canonical model | ddobokki/klue-roberta-small-nli-sts (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.068 / 514 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | — / unknown / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.25 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is designed for sentence similarity tasks. |
| README 인용 | --- pipeline_tag: sentence-similarity tags: |
| provenance status | verified 14, not_applicable 3, documented 2, unknown 4 |
| revision | f176072acdca512ef8e2214d0f0ed65144be8dcd |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 12. [dragonkue/colbert-ko-0.1b](https://huggingface.co/dragonkue/colbert-ko-0.1b) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — 0], d_embs[0]) print(f"MaxSim: {score:.4f}") ``` <details> <summary>Detailed metrics (click to expand)</summary> ## Evaluation

| 항목 | 값 |
|---|---|
| canonical model | skt/A.X-Encoder-base (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.149 / 16384 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | pytorch_bin, safetensors / 0.55 |
| 벤치마크 근거 | 점수 1건 저장 |
| 의미 claim (use_cases) | This model supports Matryoshka embeddings with multiple dimensions (32, 64, 96, 128) via separate projection heads (Jina-ColBERT-v2 style). |
| README 인용 | This model supports **Matryoshka embeddings** with multiple dimensions (32, 64, 96, 128) via separate projection heads (Jina-ColBERT-v2 style). |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 3787e56c9448ee3056cc04919734cbe397ee487f |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 13. [eenzeenee/t5-base-korean-summarization](https://huggingface.co/eenzeenee/t5-base-korean-summarization) — Claude 제안: **2점**

- 제안 이유: 필수 능력이 명시적 근거로 확인됨
- 근거 위치: `model_id` — eenzeenee/t5-base-korean-summarization

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

#### 14. [framadhita/INT8-nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/framadhita/INT8-nemotron-3.5-asr-streaming-0.6b) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — ng/speech_to_text_cache_aware_streaming_infer. <details>   <summary>➡️ Pipeline</summary> ASR performance is measured using Wo

| 항목 | 값 |
|---|---|
| canonical model | framadhita/INT8-nemotron-3.5-asr-streaming-0.6b (variant=false, 종류=—, 관계 근거=self, 변환 표지=INT8) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.638 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.59 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | English-only transcription use cases. |
| README 인용 | 6b) model for English-only transcription use cases. |
| provenance status | verified 13, not_applicable 3, documented 4, unknown 3 |
| revision | 0c3434fa3d6f580d0b2df1e555c196c83a52e3f1 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 15. [gpustack/bce-reranker-base_v1-GGUF](https://huggingface.co/gpustack/bce-reranker-base_v1-GGUF) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — ding` and `reranker` models as [Embedding Models Evaluation Summary](https://github. - ***2024-01-03***: **Eval Datasets** [[D

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

#### 16. [handy-computer/Qwen3-ASR-0.6B-gguf](https://huggingface.co/handy-computer/Qwen3-ASR-0.6B-gguf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — ease refer to the [example code](https://github. <details> <summary>ASR Benchmarks on Public Datasets (WER ↓)</summary> Inheri

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

#### 17. [memoravox/Qwen3-ASR-0.6B-gguf](https://huggingface.co/memoravox/Qwen3-ASR-0.6B-gguf) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — ease refer to the [example code](https://github. <details> <summary>ASR Benchmarks on Public Datasets (WER ↓)</summary> Inheri

| 항목 | 값 |
|---|---|
| canonical model | Qwen/Qwen3-ASR-0.6B (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=gguf) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.782 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | apache-2.0 / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf / 0.79 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | For more detailed usage examples, please refer to the example code. |
| README 인용 | For more detailed usage examples, please refer to the [example code](https://github. |
| provenance status | verified 12, not_applicable 4, documented 4, unknown 3 |
| revision | 39aee80e6b9acaf8a087054bcb4de37ba389ac7b |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 18. [mlx-community/LFM2.5-Embedding-350M-bf16](https://huggingface.co/mlx-community/LFM2.5-Embedding-350M-bf16) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델; 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — ights unchanged apart from tensor layout (bf16 → MLX bf16). Summary (mean over 8 datasets) shows performance metrics for bf16.

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/LFM2.5-Embedding-350M (variant=true, 종류=mlx, 관계 근거=base_model_tag, 변환 표지=mlx) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.354 / 128000 |
| task | sentence-similarity (matched: sentence-similarity) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | safetensors / 0.66 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | LFM2.5-Embedding-350M is a multilingual dense bi-encoder (1024-dim CLS embedding, cosine similarity), for local inference on Apple Silicon with MLX. |
| README 인용 | 5-Embedding-350M), a multilingual dense bi-encoder (1024-dim CLS embedding, cosine similarity), for local inference on Apple Silicon with [MLX](https://github. |
| provenance status | verified 14, not_applicable 3, documented 5, unknown 1 |
| revision | 14f29539bf823aec87252f92d69c9f1af9fdcbfd |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 19. [nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — ng/speech_to_text_cache_aware_streaming_infer. <details>   <summary>➡️ Pipeline</summary> ASR performance is measured using Wo

| 항목 | 값 |
|---|---|
| canonical model | nvidia/nemotron-3.5-asr-streaming-0.6b (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.638 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 0.69 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is suitable for English-only transcription use cases. |
| README 인용 | 6b) model for English-only transcription use cases. |
| provenance status | verified 11, not_applicable 3, documented 4, unknown 4, conflict 1 |
| revision | ea30d66debe3740a08b573244286791d423d6b3e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 20. [saidutta69/LFM2.5-350M-heretic](https://huggingface.co/saidutta69/LFM2.5-350M-heretic) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델; 원본의 변환·양자화·재업로드
- 근거 위치: `semantic_metadata` — ilized in applications requiring extensive context, such as summarization or dialogue systems. The model uses RoPE for positio

| 항목 | 값 |
|---|---|
| canonical model | LiquidAI/LFM2.5-350M (variant=true, 종류=—, 관계 근거=base_model_tag, 변환 표지=heretic) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 0.354 / 128000 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 0.15 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | The model is suitable for text generation tasks due to its advanced position embedding technique. |
| README 인용 | \| **Position embedding** \| RoPE, theta = 1,000,000 \| |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | 27a087aa7199f47750dfb4f5948e2fe031908b80 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 21. [suryatmodulus/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/suryatmodulus/nemotron-3.5-asr-streaming-0.6b) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — ng/speech_to_text_cache_aware_streaming_infer. <details>   <summary>➡️ Pipeline</summary> ASR performance is measured using Wo

| 항목 | 값 |
|---|---|
| canonical model | suryatmodulus/nemotron-3.5-asr-streaming-0.6b (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | low_popularity |
| 파라미터(B) / 컨텍스트 | 0.638 / — |
| task | automatic-speech-recognition (matched: automatic-speech-recognition) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | other / review_required / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 0.69 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Dynamic Runtime Flexibility: Choose the optimal operating point on the latency-accuracy Pareto curve at inference time. |
| README 인용 | - 🎛️ **Dynamic Runtime Flexibility:** Choose the optimal operating point on the latency-accuracy Pareto curve at inference time. No re-training is required to adjust for different use-case requirements. |
| provenance status | verified 11, not_applicable 3, documented 4, unknown 4, conflict 1 |
| revision | 6f04c0d70a875f6d278d7e78b1471cca79a88f05 |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 22. [thelamapi/next-1b](https://huggingface.co/thelamapi/next-1b) — Claude 제안: **1점**

- 제안 이유: 다국어·범용 모델
- 근거 위치: `semantic_metadata` — and low-resource text-generation. Supports text generation, summarization, Q&A, creative writing, reasoning tasks. Logical cha

| 항목 | 값 |
|---|---|
| canonical model | thelamapi/next-1b (variant=false, 종류=—, 관계 근거=self, 변환 표지=—) |
| pool | core |
| 파라미터(B) / 컨텍스트 | 1.0 / 32768 |
| task | text-generation (matched: text-generation) |
| 한국어 근거 | metadata.language:korean, stage1:korean_explicit |
| license / commercial_status / gated | mit / permitted / false |
| artifact formats / 실행 파일 크기(GiB) | gguf, safetensors / 1.0 |
| 벤치마크 근거 | 없음 |
| 의미 claim (use_cases) | Open-source and transparent for research and applications. |
| README 인용 | * Open-source and transparent for research and applications. |
| provenance status | verified 14, not_applicable 3, documented 4, unknown 2 |
| revision | cdab7faeeeed894e4caaecb4183627f12659f21e |

- 판정: ☐ 승인 ☐ 2점 ☐ 1점 ☐ 제외 ☐ 보류
- 이유: ______

#### 23. [thelamapi/next2-0.8b-GGUF](https://huggingface.co/thelamapi/next2-0.8b-GGUF) — Claude 제안: **보류(사람 판단)**

- 제안 이유: README 원문에만 근거가 있어 사람이 읽어야 한다
- 근거 위치: `evidence` — efficiently. Licensed under the **MIT License**. * 📝 **Text Summarization & Extraction:** Processing documents locally to main

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

## sx10 — CS 상담 로그에서 개인정보를 지우는 배치 작업을 만들고 있어요. 상업 이용 허용 라이선스 계열이고 파일 크기가 2GB 이하인 개인정보 탐지 모델이 있나요?

- 사용자 의도: 상업용 소형 PII 탐지 모델
- persona / 표현: backend_dev / 혼합형 · 난이도 hard
- 기대 행동: recommend

| 조건 | 값 | 질문 속 근거(conditions_fidelity) | 운영 RPC 지원 |
|---|---|---|---|
| `commercial_status` | permitted | 상업 이용 허용 라이선스 계열 | 예 |
| `max_artifact_gib` | 2 | 파일 크기가 2GB 이하 | 예 |

- **2점 기준**: 개인정보 탐지·마스킹을 주 용도로 명시한 모델
- **1점 기준**: 개인정보 처리가 부가 기능

| corpus | eligible | 2점 제안 | 1점 제안 | 자동 제외 | 사람 판단(unresolved) | 검수 대상 | invariant | unknown 값 때문에 제외 |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4,017 | 747 | 1 | 0 | 746 | 0 | 1 | ✅ | 172 |

자동 제외 이유별 수와 규칙 감사용 무작위 표본(전수 검수가 아니다):

| 이유 | 수 | 감사 표본 |
|---|---:|---|
| 요구 능력을 뒷받침하는 저장된 근거 없음 (`no_supporting_evidence`) | 746 | microsoft/harrier-oss-v1-0.6b, palette-lab/songgot-12l, yjoonjang/colbert-ko-v1 |

#### 1. [atonlee/Qoamo-PII-Decision](https://huggingface.co/atonlee/Qoamo-PII-Decision) — Claude 제안: **2점**

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
