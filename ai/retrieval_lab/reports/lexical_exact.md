# lexical_exact 검색 실험

- 질의 22개 (채점 22개), 기준 지표 `recall@10`, 관련 등급 ≥ 1
- Dense `BAAI/bge-m3` · Sparse fielded BM25 · Weighted RRF (k=60) · Pre-Retrieval LLM `gpt-4o-mini`
- 라벨: 기존 라벨 + 추가 판정(supplement_lexical_structured.jsonl)
- 실행 2026-10-31 15:57

## 실험표

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Baseline | 0.349 | 0.561 | 0.397 | 0.594 | 0.414 | 0.421 | 255ms |
| Known values only | 0.349 | 0.555 | 0.392 | 0.594 | 0.414 | 0.421 | 255ms |
| Rewrite | 0.279 | 0.428 | 0.282 | 0.458 | 0.297 | 0.280 | 1833ms |
| Decomposition | 0.322 | 0.494 | 0.329 | 0.572 | 0.356 | 0.330 | 2234ms |
| Multi-Query | 0.346 | 0.517 | 0.351 | 0.594 | 0.398 | 0.407 | 2611ms |
| HyDE | 0.340 | 0.445 | 0.283 | 0.619 | 0.419 | 0.393 | 2780ms |
| Name Lookup | 0.378 | 0.574 | 0.405 | 0.662 | 0.449 | 0.422 | 255ms |
| Best Combination (Name Lookup, dense 0.5) | 0.378 | 0.574 | 0.405 | 0.662 | 0.449 | 0.422 | 255ms |

### 보조 지표

| 실험 | P@5 | P@10 | F1@5 | Hit@10 | nRecall@10 | p99 | 제외 위반@10 | Judged@10 |
|---|---|---|---|---|---|---|---|---|
| Baseline | 0.409 | 0.364 | 0.330 | 0.955 | 0.602 | 297ms | 0.500 | 0.536 |
| Known values only | 0.409 | 0.359 | 0.330 | 0.955 | 0.596 | 297ms | 0.500 | 0.532 |
| Rewrite | 0.291 | 0.250 | 0.244 | 0.818 | 0.451 | 4341ms | 0.625 | 0.359 |
| Decomposition | 0.327 | 0.291 | 0.280 | 0.955 | 0.523 | 2342ms | 0.500 | 0.418 |
| Multi-Query | 0.382 | 0.314 | 0.313 | 0.909 | 0.550 | 2681ms | 0.500 | 0.418 |
| HyDE | 0.345 | 0.245 | 0.299 | 0.864 | 0.468 | 2873ms | 0.625 | 0.364 |
| Name Lookup | 0.427 | 0.368 | 0.354 | 1.000 | 0.614 | 298ms | 0.500 | 0.545 |
| Best Combination (Name Lookup, dense 0.5) | 0.427 | 0.368 | 0.354 | 1.000 | 0.614 | 298ms | 0.500 | 0.545 |

## Dense / Sparse / Hybrid 비교 (Pre-Retrieval 없음)

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Dense only (BGE-M3) | 0.262 | 0.377 | 0.261 | 0.526 | 0.319 | 0.292 | 255ms |
| Sparse only (BM25) | 0.281 | 0.392 | 0.235 | 0.456 | 0.317 | 0.283 | 255ms |
| Hybrid (Weighted RRF 0.5/0.5) | 0.349 | 0.561 | 0.397 | 0.594 | 0.414 | 0.421 | 255ms |

## Dense/Sparse 가중치 탐색

대상: Name Lookup · 방법: optuna

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| dense 0.1 / sparse 0.9 | 0.329 | 0.456 | 0.288 | 0.576 | 0.392 | 0.332 | 255ms |
| dense 0.2 / sparse 0.8 | 0.384 | 0.495 | 0.324 | 0.643 | 0.457 | 0.394 | 255ms |
| dense 0.25 / sparse 0.75 | 0.421 | 0.514 | 0.347 | 0.644 | 0.484 | 0.437 | 255ms |
| dense 0.3 / sparse 0.7 | 0.431 | 0.525 | 0.359 | 0.636 | 0.495 | 0.457 | 255ms |
| dense 0.4 / sparse 0.6 | 0.374 | 0.554 | 0.384 | 0.645 | 0.457 | 0.431 | 255ms |
| dense 0.45 / sparse 0.55 | 0.371 | 0.554 | 0.384 | 0.645 | 0.443 | 0.422 | 255ms |
| dense 0.5 / sparse 0.5 | 0.378 | 0.574 | 0.405 | 0.662 | 0.449 | 0.422 | 255ms |
| dense 0.55 / sparse 0.45 | 0.366 | 0.557 | 0.388 | 0.670 | 0.436 | 0.405 | 255ms |
| dense 0.6 / sparse 0.4 | 0.369 | 0.549 | 0.380 | 0.666 | 0.441 | 0.405 | 255ms |
| dense 0.65 / sparse 0.35 | 0.369 | 0.501 | 0.355 | 0.666 | 0.442 | 0.403 | 255ms |
| dense 0.7 / sparse 0.3 | 0.350 | 0.483 | 0.341 | 0.666 | 0.424 | 0.379 | 255ms |
| dense 0.75 / sparse 0.25 | 0.324 | 0.458 | 0.318 | 0.657 | 0.403 | 0.354 | 255ms |
| dense 0.8 / sparse 0.2 | 0.295 | 0.464 | 0.323 | 0.648 | 0.379 | 0.334 | 255ms |
| dense 0.9 / sparse 0.1 | 0.293 | 0.414 | 0.285 | 0.664 | 0.383 | 0.330 | 255ms |

## Dense/Sparse 가중치 탐색 (Pre-Retrieval 없음)

대상: Baseline · 방법: optuna

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| dense 0.1 / sparse 0.9 | 0.325 | 0.434 | 0.275 | 0.509 | 0.362 | 0.315 | 255ms |
| dense 0.2 / sparse 0.8 | 0.371 | 0.472 | 0.311 | 0.586 | 0.428 | 0.385 | 255ms |
| dense 0.25 / sparse 0.75 | 0.389 | 0.482 | 0.328 | 0.587 | 0.450 | 0.424 | 255ms |
| dense 0.3 / sparse 0.7 | 0.403 | 0.508 | 0.347 | 0.583 | 0.465 | 0.455 | 255ms |
| dense 0.4 / sparse 0.6 | 0.355 | 0.549 | 0.382 | 0.586 | 0.432 | 0.432 | 255ms |
| dense 0.45 / sparse 0.55 | 0.352 | 0.540 | 0.376 | 0.586 | 0.415 | 0.423 | 255ms |
| dense 0.5 / sparse 0.5 | 0.349 | 0.561 | 0.397 | 0.594 | 0.414 | 0.421 | 255ms |
| dense 0.55 / sparse 0.45 | 0.345 | 0.540 | 0.376 | 0.602 | 0.408 | 0.411 | 255ms |
| dense 0.6 / sparse 0.4 | 0.348 | 0.527 | 0.367 | 0.598 | 0.412 | 0.410 | 255ms |
| dense 0.65 / sparse 0.35 | 0.341 | 0.507 | 0.356 | 0.598 | 0.406 | 0.403 | 255ms |
| dense 0.7 / sparse 0.3 | 0.329 | 0.467 | 0.329 | 0.590 | 0.390 | 0.384 | 255ms |
| dense 0.75 / sparse 0.25 | 0.307 | 0.445 | 0.310 | 0.581 | 0.372 | 0.361 | 255ms |
| dense 0.8 / sparse 0.2 | 0.277 | 0.458 | 0.321 | 0.568 | 0.348 | 0.342 | 255ms |
| dense 0.9 / sparse 0.1 | 0.276 | 0.390 | 0.272 | 0.562 | 0.341 | 0.325 | 255ms |

## top-10에서 놓친 관련 모델 (Name Lookup)

| 질의 | Recall@10 | 놓친 모델 |
|---|---:|---|
| sg_g002 | 0.67 | CohereLabs/aya-expanse-8b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct |
| sg_g005 | 0.75 | NHNDQ/nllb-finetuned-en2ko, facebook/nllb-200-distilled-600M |
| sg_h012 | 0.29 | facebook/mbart-large-50-many-to-many-mmt, facebook/nllb-200-1.3B, facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M |
| sg_h013 | 0.40 | R4kSo1997/opus-mt-en-ko-onnx-int8, facebook/mbart-large-50-many-to-many-mmt, facebook/nllb-200-1.3B, facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M |
| sg_h049 | 0.71 | PeterAM4/Qwen3-Embedding-0.6B-GGUF, batiai/Qwen3-Embedding-4B-GGUF, batiai/Qwen3-Embedding-8B-GGUF, mradermacher/MoAI-Embedding-4B-GGUF |
| sg_h051 | 0.57 | facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M |
| sg_h054 | 0.43 | facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M, trillionlabs/Tri-1.8B-Translation |
| sg_h055 | 0.50 | CMSManhattan/JiRackUltra_14b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LiquidAI/LFM2.5-2.6B-GGUF, facebook/nllb-200-distilled-600M, mradermacher/llama3-8b-it-translation-general-en-ko-1sent-i1-GGUF, seongs/ke-t5-base-aihub-koen-translation-integrated-10m-en-to-ko, trillionlabs/Tri-1.8B-Translation |
| sg_h073 | 0.20 | facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M, trillionlabs/Tri-1.8B-Translation |
| sg_h074 | 0.40 | facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M |
| sg_h075 | 0.33 | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct-GGUF, LGAI-EXAONE/EXAONE-3.5-32B-Instruct-GGUF |
| sg_h077 | 0.40 | Systran/faster-whisper-medium, deepdml/faster-whisper-large-v3-turbo-ct2, jfmdai/faster-whisper-large-v3-turbo-ct2 |
| sg_h078 | 0.14 | intfloat/multilingual-e5-base, intfloat/multilingual-e5-small, janni-t/qwen3-embedding-0.6b-int8-tei-onnx, sentence-transformers/LaBSE, sentence-transformers/distiluse-base-multilingual-cased-v1, sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 |
| sg_h079 | 0.67 | mlx-community/Devstral-Small-2507-4bit, mlx-community/c4ai-command-r-08-2024-4bit, mlx-community/c4ai-command-r-plus-4bit, mlx-community/c4ai-command-r-v01-4bit |
| sg_h080 | 0.20 | LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, NotoriousH2/kanana-2-30b-a3b-instruct-awq-w4a16, casperhansen/mistral-large-instruct-2407-awq, mconcat/Qwopus3.6-27B-v2-AWQ-4bit |
| sg_h081 | 0.64 | bespin-global/klue-sroberta-base-continue-learning-by-mnr, ddobokki/unsup-simcse-klue-roberta-small, sorryhyun/sentence-embedding-klue-large, ys7yoo/sentence-roberta-klue-sts, ys7yoo/sentence-roberta-large-klue-sts |
| sg_h166 | 0.33 | K-intelligence/Midm-2.0-Mini-Instruct, Mungert/Midm-2.0-Base-Instruct-GGUF |

## 추가 판정이 필요한 후보

이번 실험의 설정 중 하나 이상에서 top-10에 나왔지만 아무도 판정하지 않은 모델이 질의 22개에 걸쳐 467개다. 목록은 JSON의 `unjudged_pool`에 있다.

## 해석 주의

- 질의가 20개 안팎이라 Recall 차이 0.05 이하는 질의 1개 차이일 수 있다. 개선 판단 전에 질의별 결과(JSON)를 확인한다.
- 가중치 탐색과 평가에 같은 질의를 쓴다. 고른 가중치는 다른 질의에서 다시 확인해야 한다.
- Judged@10은 top-10 중 누군가 판정한 모델의 비율이다. 판정 후보 풀은 BM25·다운로드 상위에서 뽑았으므로, 이 값이 낮은 설정(특히 dense 비중이 큰 설정)은 미판정 모델 때문에 Recall이 낮게 나올 수 있다. JSON의 `unjudged@10`을 판정실에서 추가 판정하면 보정된다.
- 사전 검색 LLM 지연은 캐시에 기록된 최초 호출 시간이다. 여러 변환은 병렬 실행을 가정해 가장 느린 것만 더한다.
