# benchmark_lookup 검색 실험

- 질의 18개 (채점 18개), 기준 지표 `recall@10`, 관련 등급 ≥ 1
- Dense `BAAI/bge-m3` · Sparse fielded BM25 · Weighted RRF (k=60) · Pre-Retrieval LLM `gpt-4o-mini`
- 라벨: 기존 라벨 + 추가 판정(supplement_benchmark_lookup.jsonl)
- 실행 2026-10-31 02:34

## 실험표

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Baseline | 0.522 | 0.733 | 0.529 | 0.861 | 0.666 | 0.616 | 3980ms |
| Known values only | 0.522 | 0.733 | 0.529 | 0.861 | 0.666 | 0.616 | 3980ms |
| Rewrite | 0.356 | 0.474 | 0.311 | 0.636 | 0.423 | 0.296 | 4554ms |
| Decomposition | 0.410 | 0.503 | 0.330 | 0.817 | 0.507 | 0.419 | 6026ms |
| Multi-Query | 0.505 | 0.647 | 0.459 | 0.889 | 0.665 | 0.600 | 6391ms |
| HyDE | 0.349 | 0.525 | 0.350 | 0.631 | 0.425 | 0.320 | 4222ms |
| Name Lookup | 0.522 | 0.733 | 0.529 | 0.852 | 0.662 | 0.611 | 3982ms |
| Best Combination (Baseline, dense 0.5) | 0.522 | 0.733 | 0.529 | 0.861 | 0.666 | 0.616 | 3980ms |

### 보조 지표

| 실험 | P@5 | P@10 | F1@5 | Hit@10 | nRecall@10 | p99 | 제외 위반@10 | Judged@10 |
|---|---|---|---|---|---|---|---|---|
| Baseline | 0.600 | 0.456 | 0.523 | 0.944 | 0.758 | 3980ms | 0.000 | 1.000 |
| Known values only | 0.600 | 0.456 | 0.523 | 0.944 | 0.758 | 3980ms | 0.000 | 1.000 |
| Rewrite | 0.356 | 0.256 | 0.331 | 0.944 | 0.487 | 4554ms | 0.000 | 0.494 |
| Decomposition | 0.400 | 0.267 | 0.381 | 0.944 | 0.512 | 6026ms | 0.000 | 0.617 |
| Multi-Query | 0.578 | 0.394 | 0.502 | 0.944 | 0.671 | 6391ms | 0.000 | 0.783 |
| HyDE | 0.400 | 0.289 | 0.351 | 0.944 | 0.537 | 4222ms | 0.000 | 0.606 |
| Name Lookup | 0.600 | 0.456 | 0.523 | 0.944 | 0.758 | 3982ms | 0.000 | 0.994 |
| Best Combination (Baseline, dense 0.5) | 0.600 | 0.456 | 0.523 | 0.944 | 0.758 | 3980ms | 0.000 | 1.000 |

## Dense / Sparse / Hybrid 비교 (Pre-Retrieval 없음)

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Dense only (BGE-M3) | 0.356 | 0.419 | 0.281 | 0.636 | 0.410 | 0.359 | 3980ms |
| Sparse only (BM25) | 0.339 | 0.432 | 0.275 | 0.662 | 0.432 | 0.320 | 3980ms |
| Hybrid (Weighted RRF 0.5/0.5) | 0.522 | 0.733 | 0.529 | 0.861 | 0.666 | 0.616 | 3980ms |

## Dense/Sparse 가중치 탐색

대상: Baseline · 방법: optuna

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| dense 0.1 / sparse 0.9 | 0.380 | 0.477 | 0.313 | 0.778 | 0.518 | 0.406 | 3980ms |
| dense 0.2 / sparse 0.8 | 0.483 | 0.555 | 0.382 | 0.833 | 0.637 | 0.556 | 3980ms |
| dense 0.25 / sparse 0.75 | 0.494 | 0.602 | 0.424 | 0.833 | 0.655 | 0.587 | 3980ms |
| dense 0.3 / sparse 0.7 | 0.499 | 0.619 | 0.444 | 0.833 | 0.657 | 0.597 | 3980ms |
| dense 0.4 / sparse 0.6 | 0.539 | 0.664 | 0.482 | 0.833 | 0.681 | 0.629 | 3980ms |
| dense 0.45 / sparse 0.55 | 0.537 | 0.700 | 0.508 | 0.861 | 0.686 | 0.634 | 3980ms |
| dense 0.5 / sparse 0.5 | 0.522 | 0.733 | 0.529 | 0.861 | 0.666 | 0.616 | 3980ms |
| dense 0.55 / sparse 0.45 | 0.526 | 0.693 | 0.497 | 0.861 | 0.665 | 0.610 | 3980ms |
| dense 0.6 / sparse 0.4 | 0.480 | 0.665 | 0.473 | 0.861 | 0.629 | 0.573 | 3980ms |
| dense 0.65 / sparse 0.35 | 0.477 | 0.647 | 0.459 | 0.861 | 0.611 | 0.554 | 3980ms |
| dense 0.7 / sparse 0.3 | 0.450 | 0.583 | 0.409 | 0.806 | 0.572 | 0.520 | 3980ms |
| dense 0.75 / sparse 0.25 | 0.444 | 0.536 | 0.371 | 0.806 | 0.558 | 0.504 | 3980ms |
| dense 0.8 / sparse 0.2 | 0.420 | 0.520 | 0.358 | 0.787 | 0.530 | 0.469 | 3980ms |
| dense 0.9 / sparse 0.1 | 0.391 | 0.445 | 0.301 | 0.743 | 0.481 | 0.416 | 3980ms |

## top-10에서 놓친 관련 모델 (Baseline)

| 질의 | Recall@10 | 놓친 모델 |
|---|---:|---|
| sg_g018 | 0.62 | OpenVINO/whisper-large-v3-turbo-int8-ov, Zoont/faster-whisper-large-v3-turbo-int8-ct2, deepdml/faster-whisper-large-v3-turbo-ct2, jfmdai/faster-whisper-large-v3-turbo-ct2, openai/whisper-large-v3-turbo |
| sg_h086 | 0.50 | monologg/koelectra-base-finetuned-nsmc, monologg/koelectra-small-finetuned-nsmc |
| sg_h087 | 0.00 | jhgan/ko-sbert-sts |
| sg_h088 | 0.75 | facebook/drama-1b, mykor/KURE-v1-gguf |
| sg_h089 | 0.67 | sigridjineth/ModernBERT-korean-large-preview, telepix/PIXIE-Rune-v1.5, telepix/PIXIE-Spell-v1.5-0.6B |
| sg_h090 | 0.60 | Mungert/A.X-4.0-Light-GGUF, skt/A.X-4.0 |
| sg_h092 | 0.57 | EleutherAI/polyglot-ko-12.8b, EleutherAI/polyglot-ko-3.8b, EleutherAI/polyglot-ko-5.8b |
| sg_h094 | 0.80 | w11wo/wav2vec2-xls-r-300m-korean |
| sg_h096 | 0.82 | Serkan007/CTranslate2-nllb-200-int8, mijuanlo/nllb-200-distilled-1.3B-int8-ct2 |
| sg_h098 | 0.50 | CohereLabs/North-Micro-Vision-Instruct, batiai/batisee, thelamapi/next2-air-i1-GGUF |
| sg_h099 | 0.75 | CohereLabs/North-Micro-Vision-Instruct, MuXodious/LFM2.5-VL-1.6B-absolute-heresy-GGUF |
| sg_h102 | 0.62 | Hisham480/multilingual-r2, ibm-granite/granite-embedding-107m-multilingual, ibm-granite/granite-embedding-97m-multilingual-r2, intfloat/multilingual-e5-base, intfloat/multilingual-e5-small |

## 추가 판정이 필요한 후보

이번 실험의 설정 중 하나 이상에서 top-10에 나왔지만 아무도 판정하지 않은 모델이 질의 18개에 걸쳐 337개다. 목록은 JSON의 `unjudged_pool`에 있다.

## 해석 주의

- 질의가 20개 안팎이라 Recall 차이 0.05 이하는 질의 1개 차이일 수 있다. 개선 판단 전에 질의별 결과(JSON)를 확인한다.
- 가중치 탐색과 평가에 같은 질의를 쓴다. 고른 가중치는 다른 질의에서 다시 확인해야 한다.
- Judged@10은 top-10 중 누군가 판정한 모델의 비율이다. 판정 후보 풀은 BM25·다운로드 상위에서 뽑았으므로, 이 값이 낮은 설정(특히 dense 비중이 큰 설정)은 미판정 모델 때문에 Recall이 낮게 나올 수 있다. JSON의 `unjudged@10`을 판정실에서 추가 판정하면 보정된다.
- 사전 검색 LLM 지연은 캐시에 기록된 최초 호출 시간이다. 여러 변환은 병렬 실행을 가정해 가장 느린 것만 더한다.
