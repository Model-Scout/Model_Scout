# semantic_constraint 검색 실험

- 질의 50개 (채점 50개), 기준 지표 `recall@10`, 관련 등급 ≥ 1
- Dense `BAAI/bge-m3` · Sparse fielded BM25 · Weighted RRF (k=60) · Pre-Retrieval LLM `gpt-4o-mini`
- 라벨: 기존 라벨 + 추가 판정(supplement_semantic_constraint.jsonl)
- 실행 2026-10-31 16:13

## 실험표

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Baseline | 0.346 | 0.652 | 0.617 | 0.775 | 0.512 | 0.556 | 854ms |
| Known values only | 0.330 | 0.556 | 0.538 | 0.780 | 0.510 | 0.543 | 854ms |
| Rewrite | 0.223 | 0.352 | 0.321 | 0.568 | 0.337 | 0.290 | 1925ms |
| Decomposition | 0.283 | 0.424 | 0.395 | 0.657 | 0.409 | 0.424 | 2816ms |
| Multi-Query | 0.331 | 0.491 | 0.457 | 0.808 | 0.505 | 0.529 | 3078ms |
| HyDE | 0.224 | 0.376 | 0.346 | 0.678 | 0.374 | 0.354 | 2236ms |
| Name Lookup | 0.336 | 0.646 | 0.612 | 0.728 | 0.492 | 0.532 | 854ms |
| Best Combination (Baseline, dense 0.5) | 0.346 | 0.652 | 0.617 | 0.775 | 0.512 | 0.556 | 854ms |

### 보조 지표

| 실험 | P@5 | P@10 | F1@5 | Hit@10 | nRecall@10 | p99 | 제외 위반@10 | Judged@10 |
|---|---|---|---|---|---|---|---|---|
| Baseline | 0.660 | 0.630 | 0.436 | 1.000 | 0.732 | 4363ms | 0.424 | 1.000 |
| Known values only | 0.636 | 0.558 | 0.417 | 0.980 | 0.632 | 4362ms | 0.394 | 0.852 |
| Rewrite | 0.384 | 0.320 | 0.266 | 0.960 | 0.389 | 3166ms | 0.364 | 0.522 |
| Decomposition | 0.524 | 0.400 | 0.350 | 1.000 | 0.474 | 6227ms | 0.424 | 0.630 |
| Multi-Query | 0.604 | 0.462 | 0.408 | 1.000 | 0.547 | 6722ms | 0.394 | 0.744 |
| HyDE | 0.412 | 0.350 | 0.277 | 0.940 | 0.422 | 2687ms | 0.333 | 0.530 |
| Name Lookup | 0.644 | 0.626 | 0.424 | 1.000 | 0.727 | 4362ms | 0.455 | 1.000 |
| Best Combination (Baseline, dense 0.5) | 0.660 | 0.630 | 0.436 | 1.000 | 0.732 | 4363ms | 0.424 | 1.000 |

## Dense / Sparse / Hybrid 비교 (Pre-Retrieval 없음)

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Dense only (BGE-M3) | 0.231 | 0.316 | 0.285 | 0.560 | 0.322 | 0.294 | 854ms |
| Sparse only (BM25) | 0.151 | 0.252 | 0.234 | 0.485 | 0.248 | 0.215 | 854ms |
| Hybrid (Weighted RRF 0.5/0.5) | 0.346 | 0.652 | 0.617 | 0.775 | 0.512 | 0.556 | 854ms |

## Dense/Sparse 가중치 탐색

대상: Baseline · 방법: optuna

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| dense 0.1 / sparse 0.9 | 0.185 | 0.292 | 0.274 | 0.625 | 0.318 | 0.299 | 854ms |
| dense 0.2 / sparse 0.8 | 0.245 | 0.380 | 0.366 | 0.702 | 0.398 | 0.399 | 854ms |
| dense 0.25 / sparse 0.75 | 0.269 | 0.426 | 0.410 | 0.730 | 0.443 | 0.451 | 854ms |
| dense 0.3 / sparse 0.7 | 0.302 | 0.461 | 0.441 | 0.750 | 0.472 | 0.495 | 854ms |
| dense 0.4 / sparse 0.6 | 0.327 | 0.565 | 0.536 | 0.763 | 0.502 | 0.537 | 854ms |
| dense 0.45 / sparse 0.55 | 0.330 | 0.600 | 0.567 | 0.763 | 0.500 | 0.545 | 854ms |
| dense 0.5 / sparse 0.5 | 0.346 | 0.652 | 0.617 | 0.775 | 0.512 | 0.556 | 854ms |
| dense 0.55 / sparse 0.45 | 0.343 | 0.611 | 0.577 | 0.778 | 0.510 | 0.554 | 854ms |
| dense 0.6 / sparse 0.4 | 0.343 | 0.588 | 0.549 | 0.784 | 0.509 | 0.551 | 854ms |
| dense 0.65 / sparse 0.35 | 0.346 | 0.539 | 0.502 | 0.766 | 0.510 | 0.550 | 854ms |
| dense 0.7 / sparse 0.3 | 0.327 | 0.488 | 0.454 | 0.757 | 0.486 | 0.516 | 854ms |
| dense 0.75 / sparse 0.25 | 0.317 | 0.455 | 0.422 | 0.737 | 0.477 | 0.503 | 854ms |
| dense 0.8 / sparse 0.2 | 0.305 | 0.419 | 0.384 | 0.711 | 0.457 | 0.480 | 854ms |
| dense 0.9 / sparse 0.1 | 0.271 | 0.359 | 0.325 | 0.671 | 0.411 | 0.404 | 854ms |

## top-10에서 놓친 관련 모델 (Baseline)

| 질의 | Recall@10 | 놓친 모델 |
|---|---:|---|
| sg_g006 | 0.75 | Systran/faster-whisper-large-v3, openai/whisper-large-v3, openai/whisper-large-v3-turbo |
| sg_g008 | 0.73 | Systran/faster-whisper-large-v3, openai/whisper-large-v3, openai/whisper-large-v3-turbo |
| sg_g009 | 0.75 | batiai/gemma-4-E2B-it-GGUF, batiai/gemma-4-E4B-it-GGUF |
| sg_g015 | 0.56 | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct, LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct-GGUF, bartowski/EXAONE-3.5-2.4B-Instruct-GGUF, lmstudio-community/EXAONE-3.5-2.4B-Instruct-GGUF |
| sg_g017 | 0.75 | MLP-KTLim/llama-3-Korean-Bllossom-8B, joongi007/llama-3-Korean-Bllossom-8B-20240809-GGUF |
| sg_g021 | 0.60 | RedHatAI/Qwen2.5-7B-Instruct-FP8-dynamic, RedHatAI/Qwen2.5-7B-Instruct-quantized.w8a8, ThomasBaruzier/Qwen2.5-7B-Instruct-GGUF, unsloth/Qwen2.5-7B-Instruct |
| sg_g028 | 0.50 | OpenVINO/whisper-base-int8-ov, Systran/faster-whisper-base, handy-computer/whisper-base-gguf, openai/whisper-base, openai/whisper-small |
| sg_g029 | 0.70 | LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct, batiai/gemma-4-E2B-it-GGUF, batiai/gemma-4-E4B-it-GGUF |
| sg_h005 | 0.90 | WhitePeak/bert-base-cased-Korean-sentiment |
| sg_h008 | 0.50 | amber-tech/bert-multilingual-passage-reranking-msmarco, bongsoo/albert-small-kor-cross-encoder-v1, bongsoo/kpf-cross-encoder-v1, gpustack/gte-multilingual-reranker-base-GGUF |
| sg_h009 | 0.35 | CohereLabs/North-Micro-Vision-Instruct, CohereLabs/aya-vision-32b, CohereLabs/aya-vision-8b, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, Jackrong/Qwopus3.6-27B-v2-MTP-GGUF, LGAI-EXAONE/EXAONE-4.5-33B, LiquidAI/LFM2.5-VL-1.6B-GGUF, NCSOFT/VARCO-VISION-14B-HF, ONTHEIT/BizOnAI-OCR, thelamapi/next-ocr |
| sg_h011 | 0.55 | CohereLabs/North-Micro-Vision-Instruct, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, Jackrong/Qwopus3.6-27B-v2-MTP-GGUF, skt/A.X-4.0-VL-Light |
| sg_h015 | 0.67 | CMSManhattan/JiRackUltra_14b, ainize/kobart-news, psyche/KoT5-summarization |
| sg_h016 | 0.50 | LiquidAI/LFM2.5-Embedding-350M-GGUF, PeterAM4/Qwen3-Embedding-0.6B-GGUF, Snowflake/snowflake-arctic-embed-l-v2.0, batiai/Qwen3-Embedding-4B-GGUF, batiai/Qwen3-Embedding-8B-GGUF, ibm-granite/granite-embedding-311m-multilingual-r2, ibm-granite/granite-embedding-97m-multilingual-r2, jinaai/jina-embeddings-v3, nvidia/Nemotron-3-Embed-1B-BF16 |
| sg_h017 | 0.48 | Griffin88/sentence-embedding-LaBSE, Youmnaaaa/Semantic-model, beademiguelperez/sentence-transformers-multilingual-e5-small, ibm-granite/granite-embedding-107m-multilingual, ibm-granite/granite-embedding-278m-multilingual, intfloat/multilingual-e5-base, intfloat/multilingual-e5-large, intfloat/multilingual-e5-small, sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, sentence-transformers/paraphrase-multilingual-mpnet-base-v2, sorryhyun/sentence-embedding-klue-large |
| sg_h020 | 0.50 | Aliados/nemotron-3.5-asr-streaming-0.6b, Systran/faster-whisper-small, Systran/faster-whisper-tiny, lemuriandezapada/VibeVoice-ASR-Streaming-AWQ-4bit, microsoft/VibeVoice-ASR-Streaming-1.5B, microsoft/VibeVoice-ASR-Streaming-7B, nvidia/nemotron-3.5-asr-streaming-0.6b, openai/whisper-large-v3, openai/whisper-small |
| sg_h021 | 0.71 | CohereLabs/North-Micro-Vision-Instruct, EZCon/GLM-OCR-4bit-g32-mxfp4-mixed_4_8-mlx |
| sg_h022 | 0.43 | CohereLabs/North-Micro-Vision-Instruct, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, Jackrong/Qwopus3.6-27B-v2-MTP-GGUF |
| sg_h024 | 0.46 | CohereLabs/North-Micro-Vision-Instruct, FadedRedStar/LFM2.5-VL-1.6B-heretic-GGUF, FadedRedStar/LFM2.5-VL-450M-heretic-GGUF, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, Jackrong/Qwopus3.6-27B-v2-MTP-GGUF, Mattimax/DAC6.5 |
| sg_h029 | 0.64 | LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LLM-OS-Models/KoHRM-Text-1.4B-GGUF, LiquidAI/LFM2.5-2.6B-GGUF, LiquidAI/LFM2.5-230M-GGUF |
| sg_h030 | 0.50 | CMSManhattan/JiRackUltra_14b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LLM-OS-Models/KoHRM-Text-1.4B-GGUF, LLM-OS-Models/LFM2.5-8B-A1B-Terminal-ToolBench-Full-SFT-1Epoch-GGUF, LiquidAI/LFM2.5-2.6B-GGUF, LiquidAI/LFM2.5-230M-GGUF, konantech/Konan-LLM-OND |
| sg_h038 | 0.78 | WhitePeak/bert-base-cased-Korean-sentiment, daekeun-ml/koelectra-small-v3-nsmc |
| sg_h043 | 0.60 | bongsoo/albert-small-kor-cross-encoder-v1, bongsoo/kpf-cross-encoder-v1 |
| sg_h052 | 0.44 | facebook/mbart-large-50-many-to-many-mmt, facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M, trillionlabs/Tri-1.8B-Translation |
| sg_h066 | 0.83 | LiquidAI/LFM2.5-230M-GGUF |
| sg_h067 | 0.69 | Systran/faster-whisper-small, kresnik/wav2vec2-large-xlsr-korean, openai/whisper-large-v3, openai/whisper-small |
| sg_h071 | 0.70 | CohereLabs/North-Micro-Vision-Instruct, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF |
| sg_h123 | 0.62 | CMSManhattan/JiRackUltra_1b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LiquidAI/LFM2.5-2.6B-GGUF |
| sg_h124 | 0.50 | CMSManhattan/JiRackUltra_14b, CMSManhattan/JiRackUltra_1b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LiquidAI/LFM2.5-2.6B-GGUF, UNIVA-Bllossom/DeepSeek-llama3.1-Bllossom-8B |
| sg_h125 | 0.71 | Systran/faster-whisper-small, openai/whisper-small |
| sg_h147 | 0.43 | CMSManhattan/JiRackUltra_1b, LiquidAI/LFM2.5-2.6B-GGUF, LiquidAI/LFM2.5-230M-GGUF, mradermacher/next2-fast-i1-GGUF |
| sg_h149 | 0.62 | Systran/faster-whisper-small, Systran/faster-whisper-tiny, openai/whisper-small |
| sg_h150 | 0.75 | Systran/faster-whisper-small, openai/whisper-small |
| sg_h151 | 0.64 | batiai/Qwen3-Embedding-4B-GGUF, batiai/Qwen3-Embedding-8B-GGUF, ibm-granite/granite-embedding-311m-multilingual-r2, jinaai/jina-embeddings-v3, mradermacher/MoAI-Embedding-4B-GGUF |
| sg_h152 | 0.50 | DLCorso/multilingual-e5-small, Hostage928/multilingual-e5-small, MintplexLabs/multilingual-e5-small, intfloat/multilingual-e5-base, intfloat/multilingual-e5-small, sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, sentence-transformers/paraphrase-multilingual-mpnet-base-v2, shannondata/multilingual-e5-small |
| sg_h153 | 0.80 | Helsinki-NLP/opus-mt-ko-en, Helsinki-NLP/opus-mt-tc-big-ko-en |
| sg_h154 | 0.78 | Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF |
| sg_h155 | 0.50 | CohereLabs/North-Micro-Vision-Instruct, CohereLabs/aya-vision-8b, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, mistralai/Ministral-3-3B-Instruct-2512-ONNX |
| sg_h156 | 0.69 | CMSManhattan/JiRackUltra_14b, CMSManhattan/JiRackUltra_1b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LiquidAI/LFM2.5-2.6B-GGUF |
| sg_h157 | 0.29 | CohereLabs/North-Micro-Vision-Instruct, CohereLabs/aya-vision-8b, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, NCSOFT/VARCO-VISION-14B-HF |
| sg_h158 | 0.69 | CohereLabs/North-Micro-Vision-Instruct, CohereLabs/aya-vision-8b, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF |
| sg_h159 | 0.80 | WhitePeak/bert-base-cased-Korean-sentiment, daekeun-ml/koelectra-small-v3-nsmc |
| sg_h161 | 0.53 | CMSManhattan/JiRackUltra_14b, CMSManhattan/JiRackUltra_1b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LiquidAI/LFM2.5-2.6B-GGUF, Mungert/Midm-2.0-Base-Instruct-GGUF, skt/kogpt2-base-v2, trillionlabs/Tri-7B-Base |
| sg_h162 | 0.50 | Systran/faster-whisper-small, Systran/faster-whisper-tiny, aTrain-core/faster-whisper-large-v3-turbo, deepdml/faster-whisper-large-v3-turbo-ct2, deepdml/whisper-large-v3-turbo, jfmdai/faster-whisper-large-v3-turbo-ct2, openai/whisper-large-v3-turbo, openai/whisper-small |
| sg_h163 | 0.67 | gpustack/gte-multilingual-reranker-base-GGUF |

## 추가 판정이 필요한 후보

이번 실험의 설정 중 하나 이상에서 top-10에 나왔지만 아무도 판정하지 않은 모델이 질의 49개에 걸쳐 1049개다. 목록은 JSON의 `unjudged_pool`에 있다.

## 해석 주의

- 질의가 20개 안팎이라 Recall 차이 0.05 이하는 질의 1개 차이일 수 있다. 개선 판단 전에 질의별 결과(JSON)를 확인한다.
- 가중치 탐색과 평가에 같은 질의를 쓴다. 고른 가중치는 다른 질의에서 다시 확인해야 한다.
- Judged@10은 top-10 중 누군가 판정한 모델의 비율이다. 판정 후보 풀은 BM25·다운로드 상위에서 뽑았으므로, 이 값이 낮은 설정(특히 dense 비중이 큰 설정)은 미판정 모델 때문에 Recall이 낮게 나올 수 있다. JSON의 `unjudged@10`을 판정실에서 추가 판정하면 보정된다.
- 사전 검색 LLM 지연은 캐시에 기록된 최초 호출 시간이다. 여러 변환은 병렬 실행을 가정해 가장 느린 것만 더한다.
