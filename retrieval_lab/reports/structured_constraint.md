# structured_constraint 검색 실험

- 질의 24개 (채점 24개), 기준 지표 `recall@10`, 관련 등급 ≥ 1
- Dense `BAAI/bge-m3` · Sparse fielded BM25 · Weighted RRF (k=60) · Pre-Retrieval LLM `gpt-4o-mini`
- 라벨: 기존 라벨 + 추가 판정(supplement_structured_constraint.jsonl)
- 실행 2026-10-29 00:43

## 실험표

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Baseline | 0.125 | 0.268 | 0.229 | 0.312 | 0.187 | 0.182 | 283ms |
| Known values only | 0.222 | 0.379 | 0.255 | 0.411 | 0.294 | 0.295 | 272ms |
| Rewrite | 0.075 | 0.205 | 0.123 | 0.140 | 0.076 | 0.049 | 2038ms |
| Decomposition | 0.121 | 0.194 | 0.143 | 0.293 | 0.168 | 0.130 | 2387ms |
| Multi-Query | 0.102 | 0.205 | 0.152 | 0.207 | 0.129 | 0.128 | 3209ms |
| HyDE | 0.136 | 0.233 | 0.129 | 0.212 | 0.127 | 0.085 | 2811ms |
| Name Lookup | 0.125 | 0.268 | 0.229 | 0.312 | 0.187 | 0.182 | 283ms |
| Best Combination (Known values only, dense 0.5) | 0.222 | 0.379 | 0.255 | 0.411 | 0.294 | 0.295 | 272ms |

### 보조 지표

| 실험 | P@5 | P@10 | F1@5 | Hit@10 | nRecall@10 | p99 | 제외 위반@10 | Judged@10 |
|---|---|---|---|---|---|---|---|---|
| Baseline | 0.208 | 0.238 | 0.138 | 0.542 | 0.315 | 309ms | 0.474 | 0.362 |
| Known values only | 0.258 | 0.250 | 0.197 | 0.667 | 0.425 | 309ms | 0.211 | 0.365 |
| Rewrite | 0.083 | 0.104 | 0.065 | 0.625 | 0.217 | 4587ms | 0.316 | 0.192 |
| Decomposition | 0.150 | 0.137 | 0.118 | 0.500 | 0.216 | 2455ms | 0.368 | 0.233 |
| Multi-Query | 0.175 | 0.150 | 0.115 | 0.542 | 0.233 | 3711ms | 0.474 | 0.263 |
| HyDE | 0.142 | 0.113 | 0.122 | 0.667 | 0.247 | 4501ms | 0.368 | 0.213 |
| Name Lookup | 0.208 | 0.238 | 0.138 | 0.542 | 0.315 | 309ms | 0.474 | 0.362 |
| Best Combination (Known values only, dense 0.5) | 0.258 | 0.250 | 0.197 | 0.667 | 0.425 | 309ms | 0.211 | 0.365 |

## Dense / Sparse / Hybrid 비교 (Pre-Retrieval 없음)

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Dense only (BGE-M3) | 0.050 | 0.133 | 0.102 | 0.147 | 0.062 | 0.045 | 283ms |
| Sparse only (BM25) | 0.086 | 0.137 | 0.107 | 0.208 | 0.105 | 0.089 | 283ms |
| Hybrid (Weighted RRF 0.5/0.5) | 0.125 | 0.268 | 0.229 | 0.312 | 0.187 | 0.182 | 283ms |

## Dense/Sparse 가중치 탐색

대상: Known values only · 방법: optuna

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| dense 0.1 / sparse 0.9 | 0.095 | 0.139 | 0.110 | 0.243 | 0.140 | 0.128 | 283ms |
| dense 0.2 / sparse 0.8 | 0.109 | 0.171 | 0.136 | 0.260 | 0.159 | 0.149 | 283ms |
| dense 0.25 / sparse 0.75 | 0.122 | 0.177 | 0.143 | 0.267 | 0.163 | 0.153 | 283ms |
| dense 0.3 / sparse 0.7 | 0.129 | 0.199 | 0.157 | 0.274 | 0.173 | 0.174 | 283ms |
| dense 0.4 / sparse 0.6 | 0.138 | 0.245 | 0.197 | 0.288 | 0.188 | 0.186 | 283ms |
| dense 0.45 / sparse 0.55 | 0.111 | 0.254 | 0.207 | 0.281 | 0.176 | 0.175 | 283ms |
| dense 0.5 / sparse 0.5 | 0.125 | 0.268 | 0.229 | 0.312 | 0.187 | 0.182 | 283ms |
| dense 0.55 / sparse 0.45 | 0.125 | 0.252 | 0.211 | 0.291 | 0.189 | 0.177 | 283ms |
| dense 0.6 / sparse 0.4 | 0.132 | 0.241 | 0.195 | 0.278 | 0.187 | 0.175 | 283ms |
| dense 0.65 / sparse 0.35 | 0.129 | 0.211 | 0.178 | 0.278 | 0.173 | 0.160 | 283ms |
| dense 0.7 / sparse 0.3 | 0.097 | 0.200 | 0.164 | 0.262 | 0.147 | 0.124 | 283ms |
| dense 0.75 / sparse 0.25 | 0.098 | 0.179 | 0.144 | 0.260 | 0.148 | 0.128 | 283ms |
| dense 0.8 / sparse 0.2 | 0.078 | 0.171 | 0.137 | 0.263 | 0.121 | 0.098 | 283ms |
| dense 0.9 / sparse 0.1 | 0.053 | 0.149 | 0.115 | 0.158 | 0.070 | 0.053 | 283ms |

## Dense/Sparse 가중치 탐색 (Pre-Retrieval 없음)

대상: Baseline · 방법: optuna

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| dense 0.1 / sparse 0.9 | 0.095 | 0.139 | 0.110 | 0.243 | 0.140 | 0.128 | 283ms |
| dense 0.2 / sparse 0.8 | 0.109 | 0.171 | 0.136 | 0.260 | 0.159 | 0.149 | 283ms |
| dense 0.25 / sparse 0.75 | 0.122 | 0.177 | 0.143 | 0.267 | 0.163 | 0.153 | 283ms |
| dense 0.3 / sparse 0.7 | 0.129 | 0.199 | 0.157 | 0.274 | 0.173 | 0.174 | 283ms |
| dense 0.4 / sparse 0.6 | 0.138 | 0.245 | 0.197 | 0.288 | 0.188 | 0.186 | 283ms |
| dense 0.45 / sparse 0.55 | 0.111 | 0.254 | 0.207 | 0.281 | 0.176 | 0.175 | 283ms |
| dense 0.5 / sparse 0.5 | 0.125 | 0.268 | 0.229 | 0.312 | 0.187 | 0.182 | 283ms |
| dense 0.55 / sparse 0.45 | 0.125 | 0.252 | 0.211 | 0.291 | 0.189 | 0.177 | 283ms |
| dense 0.6 / sparse 0.4 | 0.132 | 0.241 | 0.195 | 0.278 | 0.187 | 0.175 | 283ms |
| dense 0.65 / sparse 0.35 | 0.129 | 0.211 | 0.178 | 0.278 | 0.173 | 0.160 | 283ms |
| dense 0.7 / sparse 0.3 | 0.097 | 0.200 | 0.164 | 0.262 | 0.147 | 0.124 | 283ms |
| dense 0.75 / sparse 0.25 | 0.098 | 0.179 | 0.144 | 0.260 | 0.148 | 0.128 | 283ms |
| dense 0.8 / sparse 0.2 | 0.078 | 0.171 | 0.137 | 0.263 | 0.121 | 0.098 | 283ms |
| dense 0.9 / sparse 0.1 | 0.053 | 0.149 | 0.115 | 0.158 | 0.070 | 0.053 | 283ms |

## top-10에서 놓친 관련 모델 (Known values only)

| 질의 | Recall@10 | 놓친 모델 |
|---|---:|---|
| sg_g013 | 0.25 | dragonkue/multilingual-e5-small-ko, dragonkue/multilingual-e5-small-ko-v2, intfloat/multilingual-e5-small |
| sg_g019 | 0.67 | OpenVINO/whisper-base-int8-ov, Systran/faster-whisper-base, handy-computer/whisper-base-gguf, openai/whisper-base, openai/whisper-small |
| sg_g026 | 0.00 | Qwen/Qwen3-ASR-1.7B-hf, cstr/qwen3-asr-1.7b-GGUF, handy-computer/Qwen3-ASR-1.7B-gguf, openai/whisper-large-v3 |
| sg_g027 | 0.69 | handy-computer/whisper-large-v3-turbo-gguf, openai/whisper-large-v3, openai/whisper-large-v3-turbo, xkeyC/whisper-large-v3-turbo-gguf |
| sg_h002 | 0.50 | QuantFactory/Apollo2-2B-GGUF, mradermacher/IoGPT-A1-Instruct-i1-GGUF, mradermacher/Prototype-Virus-1B-i1-GGUF, mradermacher/next-12b-i1-GGUF, mradermacher/next-1b-GGUF, timpal0l/mdeberta-v3-base-squad2 |
| sg_h010 | 0.00 | CohereLabs/North-Micro-Vision-Instruct, LiquidAI/LFM2.5-VL-1.6B-GGUF, NCSOFT/VARCO-VISION-2.0-1.7B |
| sg_h018 | 0.00 | CMSManhattan/JiRackUltra_14b, kfkas/Legal-Llama-2-ko-7b-Chat, kfkas/Llama-2-ko-7b-Chat, sakamakismile/Qwen3.6-27B-Text-NVFP4-MTP |
| sg_h019 | 0.50 | LiquidAI/LFM2.5-230M-GGUF, lcw99/ko-dialoGPT-korean-chit-chat |
| sg_h027 | 0.50 | cstr/internvl2-1b-crispembed-GGUF |
| sg_h033 | 0.50 | CMSManhattan/JiRackUltra_14b, DavidAU/Qwen3-128k-30B-A3B-NEO-MAX-Imatrix-gguf, LiquidAI/LFM2.5-2.6B-GGUF, konantech/Konan-LLM-OND, prithivMLmods/LFM2.5-2.6B-GGUF, tensorblock/llama2-13b.kor.v1-GGUF |
| sg_h036 | 0.00 | CMSManhattan/JiRackUltra_14b, LLM-OS-Models/KoHRM-Text-1.4B-GGUF, arcee-ai/Trinity-Large-Thinking, konantech/Konan-LLM-OND |
| sg_h045 | 0.53 | PeterAM4/Qwen3-Embedding-0.6B-GGUF, batiai/Qwen3-Embedding-8B-GGUF, ibm-granite/granite-embedding-311m-multilingual-r2, ibm-granite/granite-embedding-97m-multilingual-r2, intfloat/multilingual-e5-base, intfloat/multilingual-e5-small, sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, sentence-transformers/paraphrase-multilingual-mpnet-base-v2 |
| sg_h059 | 0.50 | ainize/kobart-news |
| sg_h064 | 0.75 | mradermacher/next-12b-i1-GGUF, timpal0l/mdeberta-v3-base-squad2 |
| sg_h069 | 0.00 | LLM-OS-Models/KoHRM-Text-1.4B-GGUF, microsoft/Phi-4-mini-instruct |
| sg_h070 | 0.00 | Systran/faster-whisper-base, Systran/faster-whisper-tiny |
| sg_h072 | 0.20 | Snowflake/snowflake-arctic-embed-l-v2.0, batiai/Qwen3-Embedding-4B-GGUF, batiai/Qwen3-Embedding-8B-GGUF, ibm-granite/granite-embedding-311m-multilingual-r2 |
| sg_h103 | 0.00 | CMSManhattan/JiRackUltra_1b |
| sg_h104 | 0.17 | Alibaba-NLP/gte-multilingual-base, BidirLM/BidirLM-0.6B-Embedding, PeterAM4/Qwen3-Embedding-0.6B-GGUF, Snowflake/snowflake-arctic-embed-l-v2.0, mradermacher/MoAI-Embedding-0.6B-GGUF |
| sg_h105 | 0.00 | SungBeom/whisper-small-ko, Systran/faster-whisper-small, openai/whisper-large-v3-turbo, openai/whisper-small |
| sg_h106 | 0.33 | bongsoo/albert-small-kor-cross-encoder-v1, clapAI/mmBERT-small-multilingual-sentiment |

## 추가 판정이 필요한 후보

이번 실험의 설정 중 하나 이상에서 top-10에 나왔지만 아무도 판정하지 않은 모델이 질의 24개에 걸쳐 661개다. 목록은 JSON의 `unjudged_pool`에 있다.

## 해석 주의

- 질의가 20개 안팎이라 Recall 차이 0.05 이하는 질의 1개 차이일 수 있다. 개선 판단 전에 질의별 결과(JSON)를 확인한다.
- 가중치 탐색과 평가에 같은 질의를 쓴다. 고른 가중치는 다른 질의에서 다시 확인해야 한다.
- Judged@10은 top-10 중 누군가 판정한 모델의 비율이다. 판정 후보 풀은 BM25·다운로드 상위에서 뽑았으므로, 이 값이 낮은 설정(특히 dense 비중이 큰 설정)은 미판정 모델 때문에 Recall이 낮게 나올 수 있다. JSON의 `unjudged@10`을 판정실에서 추가 판정하면 보정된다.
- 사전 검색 LLM 지연은 캐시에 기록된 최초 호출 시간이다. 여러 변환은 병렬 실행을 가정해 가장 느린 것만 더한다.
