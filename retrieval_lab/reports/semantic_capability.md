# semantic_capability 검색 실험

- 질의 37개 (채점 37개), 기준 지표 `recall@10`, 관련 등급 ≥ 1
- Dense `BAAI/bge-m3` · Sparse fielded BM25 · Weighted RRF (k=60) · Pre-Retrieval LLM `gpt-4o-mini`
- 실행 2026-10-17 20:18

## 실험표

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Baseline | 0.139 | 0.243 | 0.116 | 0.261 | 0.164 | 0.123 | 671ms |
| Rewrite | 0.183 | 0.286 | 0.132 | 0.283 | 0.186 | 0.146 | 1658ms |
| Decomposition | 0.126 | 0.217 | 0.111 | 0.214 | 0.138 | 0.101 | 3799ms |
| Multi-Query | 0.140 | 0.227 | 0.115 | 0.256 | 0.156 | 0.112 | 3867ms |
| HyDE | 0.187 | 0.255 | 0.123 | 0.312 | 0.184 | 0.143 | 3610ms |
| Best Combination (Rewrite, dense 0.4) | 0.170 | 0.308 | 0.139 | 0.306 | 0.183 | 0.147 | 1658ms |

### 보조 지표

| 실험 | P@5 | P@10 | F1@5 | Hit@10 | p99 | 제외 위반@10 | Judged@10 |
|---|---|---|---|---|---|---|---|
| Baseline | 0.114 | 0.089 | 0.111 | 0.459 | 773ms | 0.400 | 0.143 |
| Rewrite | 0.135 | 0.100 | 0.135 | 0.514 | 1756ms | 0.600 | 0.173 |
| Decomposition | 0.097 | 0.086 | 0.097 | 0.432 | 3869ms | 0.400 | 0.127 |
| Multi-Query | 0.114 | 0.089 | 0.112 | 0.486 | 5521ms | 0.400 | 0.143 |
| HyDE | 0.135 | 0.095 | 0.138 | 0.486 | 3613ms | 0.400 | 0.146 |
| Best Combination (Rewrite, dense 0.4) | 0.130 | 0.105 | 0.127 | 0.541 | 1756ms | 0.600 | 0.181 |

## Dense / Sparse / Hybrid 비교 (Pre-Retrieval 없음)

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Dense only (BGE-M3) | 0.167 | 0.219 | 0.099 | 0.200 | 0.145 | 0.111 | 670ms |
| Sparse only (BM25) | 0.106 | 0.181 | 0.093 | 0.151 | 0.118 | 0.097 | 670ms |
| Hybrid (Weighted RRF 0.5/0.5) | 0.139 | 0.243 | 0.116 | 0.261 | 0.164 | 0.123 | 671ms |

## 조합 실험

개선된 단일 요소: rewrite, hyde

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Rewrite + HyDE | 0.157 | 0.269 | 0.125 | 0.302 | 0.160 | 0.132 | 3606ms |

## Dense/Sparse 가중치 탐색

대상: Rewrite · 방법: optuna

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| dense 0.1 / sparse 0.9 | 0.150 | 0.250 | 0.119 | 0.261 | 0.154 | 0.129 | 1658ms |
| dense 0.15 / sparse 0.85 | 0.157 | 0.232 | 0.121 | 0.310 | 0.187 | 0.157 | 1658ms |
| dense 0.2 / sparse 0.8 | 0.193 | 0.232 | 0.121 | 0.332 | 0.205 | 0.166 | 1658ms |
| dense 0.25 / sparse 0.75 | 0.199 | 0.245 | 0.125 | 0.330 | 0.206 | 0.168 | 1658ms |
| dense 0.3 / sparse 0.7 | 0.191 | 0.268 | 0.130 | 0.327 | 0.197 | 0.157 | 1658ms |
| dense 0.35 / sparse 0.65 | 0.166 | 0.281 | 0.134 | 0.311 | 0.182 | 0.147 | 1658ms |
| dense 0.4 / sparse 0.6 | 0.170 | 0.308 | 0.139 | 0.306 | 0.183 | 0.147 | 1658ms |
| dense 0.45 / sparse 0.55 | 0.170 | 0.304 | 0.136 | 0.309 | 0.184 | 0.147 | 1658ms |
| dense 0.5 / sparse 0.5 | 0.183 | 0.286 | 0.132 | 0.283 | 0.186 | 0.146 | 1658ms |
| dense 0.55 / sparse 0.45 | 0.162 | 0.242 | 0.122 | 0.262 | 0.171 | 0.135 | 1658ms |
| dense 0.6 / sparse 0.4 | 0.167 | 0.242 | 0.122 | 0.274 | 0.179 | 0.150 | 1658ms |
| dense 0.7 / sparse 0.3 | 0.170 | 0.261 | 0.120 | 0.265 | 0.178 | 0.148 | 1658ms |
| dense 0.8 / sparse 0.2 | 0.187 | 0.260 | 0.120 | 0.264 | 0.180 | 0.149 | 1658ms |
| dense 0.9 / sparse 0.1 | 0.198 | 0.293 | 0.129 | 0.252 | 0.178 | 0.144 | 1658ms |

## Dense/Sparse 가중치 탐색 (Pre-Retrieval 없음)

대상: Baseline · 방법: optuna

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| dense 0.1 / sparse 0.9 | 0.138 | 0.208 | 0.098 | 0.173 | 0.139 | 0.115 | 671ms |
| dense 0.2 / sparse 0.8 | 0.152 | 0.221 | 0.103 | 0.188 | 0.155 | 0.132 | 671ms |
| dense 0.3 / sparse 0.7 | 0.186 | 0.237 | 0.116 | 0.200 | 0.169 | 0.137 | 671ms |
| dense 0.4 / sparse 0.6 | 0.173 | 0.240 | 0.119 | 0.255 | 0.181 | 0.140 | 671ms |
| dense 0.5 / sparse 0.5 | 0.139 | 0.243 | 0.116 | 0.261 | 0.164 | 0.123 | 671ms |
| dense 0.55 / sparse 0.45 | 0.131 | 0.260 | 0.124 | 0.253 | 0.152 | 0.113 | 671ms |
| dense 0.6 / sparse 0.4 | 0.131 | 0.257 | 0.121 | 0.253 | 0.150 | 0.112 | 671ms |
| dense 0.65 / sparse 0.35 | 0.127 | 0.252 | 0.117 | 0.258 | 0.148 | 0.108 | 671ms |
| dense 0.7 / sparse 0.3 | 0.117 | 0.221 | 0.109 | 0.227 | 0.136 | 0.098 | 671ms |
| dense 0.75 / sparse 0.25 | 0.111 | 0.248 | 0.114 | 0.207 | 0.126 | 0.091 | 671ms |
| dense 0.8 / sparse 0.2 | 0.114 | 0.251 | 0.117 | 0.223 | 0.133 | 0.097 | 671ms |
| dense 0.85 / sparse 0.15 | 0.114 | 0.278 | 0.121 | 0.222 | 0.132 | 0.099 | 671ms |
| dense 0.9 / sparse 0.1 | 0.149 | 0.261 | 0.114 | 0.200 | 0.130 | 0.092 | 671ms |

## top-10에서 놓친 관련 모델 (Rewrite)

| 질의 | Recall@10 | 놓친 모델 |
|---|---:|---|
| sg_g004 | 0.00 | jhgan/ko-sroberta-multitask |
| sg_g007 | 0.00 | Systran/faster-whisper-medium, Systran/faster-whisper-small, openai/whisper-small |
| sg_g020 | 0.00 | FunAudioLLM/SenseVoiceSmall, FunAudioLLM/SenseVoiceSmall-GGUF-audiocpp, cstr/sensevoice-small-GGUF, handy-computer/SenseVoiceSmall-gguf |
| sg_g022 | 0.00 | RedHatAI/Qwen2.5-7B-Instruct-FP8-dynamic, RedHatAI/Qwen2.5-7B-Instruct-quantized.w8a8, ThomasBaruzier/Qwen2.5-7B-Instruct-GGUF, unsloth/Qwen2.5-7B-Instruct |
| sg_g023 | 0.00 | Alcoft/Qwen2.5-1.5B-Instruct-GGUF, Mungert/Qwen2.5-1.5B-Instruct-GGUF, ThomasBaruzier/Qwen2.5-1.5B-Instruct-GGUF, gaianet/Qwen2.5-1.5B-Instruct-GGUF |
| sg_g024 | 0.00 | Bingsu/KURE-v1-Q8_0-GGUF, mykor/KURE-v1-gguf, nlpai-lab/KURE-v2 |
| sg_g025 | 0.00 | Bingsu/KURE-v1-Q8_0-GGUF, mykor/KURE-v1-gguf, nlpai-lab/KURE-v2 |
| sg_h003 | 0.20 | QuantFactory/Apollo2-2B-GGUF, bespin-global/klue-bert-base-aihub-mrc, monologg/koelectra-base-v3-finetuned-korquad, monologg/koelectra-small-v2-distilled-korquad-384, mradermacher/Prototype-Virus-1B-i1-GGUF, mradermacher/next-12b-i1-GGUF, mradermacher/next-1b-GGUF, timpal0l/mdeberta-v3-base-squad2 |
| sg_h007 | 0.50 | circulus/koelectra-polite-v1 |
| sg_h014 | 0.78 | csebuetnlp/mT5_m2m_crossSum_enhanced, csebuetnlp/mT5_multilingual_XLSum |
| sg_h023 | 0.00 | CohereLabs/North-Micro-Vision-Instruct, EZCon/GLM-OCR-4bit-g32-mxfp4-mixed_4_8-mlx, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, Jackrong/Qwopus3.6-27B-v2-MTP-GGUF, ONTHEIT/BizOnAI-OCR, batiai/batisee, thelamapi/next-ocr |
| sg_h025 | 0.43 | CohereLabs/North-Micro-Vision-Instruct, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, Jackrong/Qwopus3.6-27B-v2-MTP-GGUF |
| sg_h026 | 0.12 | CohereLabs/aya-vision-32b, CohereLabs/aya-vision-8b, FadedRedStar/Ministral-3-8B-Reasoning-2512-heretic-imatrix-GGUF, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, Jackrong/Qwopus3.6-27B-v2-MTP-GGUF, NCSOFT/VARCO-VISION-14B-HF |
| sg_h028 | 0.12 | CohereLabs/North-Micro-Vision-Instruct, CohereLabs/aya-vision-32b, CohereLabs/aya-vision-8b, EZCon/GLM-OCR-4bit-g32-mxfp4-mixed_4_8-mlx, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, Jackrong/Qwopus3.6-27B-v2-MTP-GGUF |
| sg_h031 | 0.00 | CMSManhattan/JiRackUltra_14b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LiquidAI/LFM2.5-2.6B-GGUF, LiquidAI/LFM2.5-230M-GGUF, OrionStarAI/Orion-14B-Chat, OrionStarAI/Orion-14B-Chat-RAG, kfkas/Legal-Llama-2-ko-7b-Chat, lcw99/ko-dialoGPT-korean-chit-chat |
| sg_h032 | 0.00 | CMSManhattan/JiRackUltra_14b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LLM-OS-Models/KoHRM-Text-1.4B-GGUF, LLM-OS-Models/LFM2.5-8B-A1B-Terminal-ToolBench-Full-SFT-1Epoch-GGUF, LiquidAI/LFM2.5-2.6B-GGUF, LiquidAI/LFM2.5-230M-GGUF, konantech/Konan-LLM-OND, squarelike/llama2-ko-medical-7b |
| sg_h034 | 0.00 | CMSManhattan/JiRackUltra_14b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LLM-OS-Models/KoHRM-Text-1.4B-GGUF, LiquidAI/LFM2.5-2.6B-GGUF, LiquidAI/LFM2.5-230M-GGUF, coderavi/Llama3.3-8B-Instruct-Thinking-Heretic-Uncensored-Claude-4.5-Opus-High-Reasoning-mlx-8Bit, genai-archive/DavidAU__Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning-mlx-mxfp4, soka0000/vclm-korean-7b |
| sg_h035 | 0.00 | CMSManhattan/JiRackUltra_14b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LiquidAI/LFM2.5-2.6B-GGUF, LiquidAI/LFM2.5-230M-GGUF, OrionStarAI/Orion-14B-Chat, OrionStarAI/Orion-14B-Chat-Int4, OrionStarAI/Orion-14B-Chat-RAG, lcw99/ko-dialoGPT-korean-chit-chat |
| sg_h039 | 0.33 | Huffon/klue-roberta-base-nli, serize/klue-roberta-base-nli-stage2 |
| sg_h040 | 0.50 | ethicalabs/Echo-DSRN-v0.1.3-Intent-CLF |
| sg_h042 | 0.50 | Verm1ion/injection-sentry-xlmr |
| sg_h044 | 0.00 | intfloat/multilingual-e5-base, intfloat/multilingual-e5-small, sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, sentence-transformers/paraphrase-multilingual-mpnet-base-v2, ys7yoo/sentence-bert-klue-sts, ys7yoo/sentence-bert-klue-sts-all, ys7yoo/sentence-roberta-klue-sts, ys7yoo/sentence-roberta-large-klue-sts |
| sg_h048 | 0.50 | jinaai/jina-clip-v2 |
| sg_h050 | 0.33 | intfloat/multilingual-e5-base, intfloat/multilingual-e5-small, sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, sentence-transformers/paraphrase-multilingual-mpnet-base-v2 |
| sg_h053 | 0.00 | Unbabel/wmt22-comet-da |
| sg_h056 | 0.00 | Serkan007/CTranslate2-nllb-200-int8, facebook/nllb-200-1.3B, facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M |
| sg_h057 | 0.50 | CMSManhattan/JiRackUltra_14b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LiquidAI/LFM2.5-2.6B-GGUF, LiquidAI/LFM2.5-230M-GGUF |
| sg_h060 | 0.83 | csebuetnlp/mT5_multilingual_XLSum |
| sg_h061 | 0.50 | csebuetnlp/mT5_multilingual_XLSum |
| sg_h063 | 0.00 | CMSManhattan/JiRackUltra_14b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LiquidAI/LFM2.5-2.6B-GGUF, mradermacher/Korean-Gemma-2B-Instruct-GGUF |
| sg_h065 | 0.25 | monologg/koelectra-base-v3-finetuned-korquad, monologg/koelectra-small-v2-distilled-korquad-384, timpal0l/mdeberta-v3-base-squad2 |
| sg_h068 | 0.00 | Systran/faster-whisper-small, openai/whisper-large-v3, openai/whisper-small |

## 추가 판정이 필요한 후보

이번 실험의 설정 중 하나 이상에서 top-10에 나왔지만 아무도 판정하지 않은 모델이 질의 37개에 걸쳐 1294개다. 목록은 JSON의 `unjudged_pool`에 있다.

## 해석 주의

- 질의가 20개 안팎이라 Recall 차이 0.05 이하는 질의 1개 차이일 수 있다. 개선 판단 전에 질의별 결과(JSON)를 확인한다.
- 가중치 탐색과 평가에 같은 질의를 쓴다. 고른 가중치는 다른 질의에서 다시 확인해야 한다.
- Judged@10은 top-10 중 누군가 판정한 모델의 비율이다. 판정 후보 풀은 BM25·다운로드 상위에서 뽑았으므로, 이 값이 낮은 설정(특히 dense 비중이 큰 설정)은 미판정 모델 때문에 Recall이 낮게 나올 수 있다. JSON의 `unjudged@10`을 판정실에서 추가 판정하면 보정된다.
- 사전 검색 LLM 지연은 캐시에 기록된 최초 호출 시간이다. 여러 변환은 병렬 실행을 가정해 가장 느린 것만 더한다.
