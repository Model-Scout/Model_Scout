# structured_constraint 검색 실험

- 질의 24개 (채점 24개), 기준 지표 `recall@10`, 관련 등급 ≥ 1
- Dense `BAAI/bge-m3` · Sparse fielded BM25 · Weighted RRF (k=60) · Pre-Retrieval LLM `gpt-4o-mini`
- 실행 2026-10-14 15:54

## 실험표

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Baseline | 0.064 | 0.109 | 0.054 | 0.123 | 0.060 | 0.033 | 413ms |

### 보조 지표

| 실험 | P@5 | P@10 | F1@5 | Hit@10 | p99 | 제외 위반@10 | Judged@10 |
|---|---|---|---|---|---|---|---|
| Baseline | 0.042 | 0.037 | 0.049 | 0.292 | 477ms | 0.474 | 0.137 |

## top-10에서 놓친 관련 모델 (Baseline)

| 질의 | Recall@10 | 놓친 모델 |
|---|---:|---|
| sg_g013 | 0.25 | dragonkue/multilingual-e5-small-ko, dragonkue/multilingual-e5-small-ko-v2, intfloat/multilingual-e5-small |
| sg_g019 | 0.00 | OpenVINO/whisper-base-int8-ov, Systran/faster-whisper-base, handy-computer/whisper-base-gguf, openai/whisper-base, openai/whisper-small |
| sg_g026 | 0.00 | Qwen/Qwen3-ASR-1.7B-hf, cstr/qwen3-asr-1.7b-GGUF, handy-computer/Qwen3-ASR-1.7B-gguf, openai/whisper-large-v3 |
| sg_g027 | 0.00 | handy-computer/whisper-large-v3-turbo-gguf, openai/whisper-large-v3, openai/whisper-large-v3-turbo, xkeyC/whisper-large-v3-turbo-gguf |
| sg_h001 | 0.25 | monologg/koelectra-base-v3-finetuned-korquad, monologg/koelectra-small-v2-distilled-korquad-384, timpal0l/mdeberta-v3-base-squad2 |
| sg_h002 | 0.00 | QuantFactory/Apollo2-2B-GGUF, mradermacher/IoGPT-A1-Instruct-i1-GGUF, mradermacher/Prototype-Virus-1B-i1-GGUF, mradermacher/next-12b-i1-GGUF, mradermacher/next-1b-GGUF, timpal0l/mdeberta-v3-base-squad2 |
| sg_h004 | 0.00 | monologg/koelectra-small-v2-distilled-korquad-384 |
| sg_h010 | 0.00 | CohereLabs/North-Micro-Vision-Instruct, LiquidAI/LFM2.5-VL-1.6B-GGUF, NCSOFT/VARCO-VISION-2.0-1.7B |
| sg_h018 | 0.00 | CMSManhattan/JiRackUltra_14b, kfkas/Legal-Llama-2-ko-7b-Chat, kfkas/Llama-2-ko-7b-Chat, sakamakismile/Qwen3.6-27B-Text-NVFP4-MTP |
| sg_h019 | 0.00 | LiquidAI/LFM2.5-230M-GGUF, cooler8/yejin-korean-1b-v8, cooler8/yejin-korean-1b-v8-sft, lcw99/ko-dialoGPT-korean-chit-chat |
| sg_h027 | 0.00 | Mattimax/DAC6.5, cstr/internvl2-1b-crispembed-GGUF |
| sg_h033 | 0.00 | CMSManhattan/JiRackUltra_14b, DavidAU/Qwen3-128k-30B-A3B-NEO-MAX-Imatrix-gguf, LiquidAI/LFM2.5-2.6B-GGUF, konantech/Konan-LLM-OND |
| sg_h036 | 0.00 | CMSManhattan/JiRackUltra_14b, LLM-OS-Models/KoHRM-Text-1.4B-GGUF, arcee-ai/Trinity-Large-Thinking, konantech/Konan-LLM-OND |
| sg_h045 | 0.00 | PeterAM4/Qwen3-Embedding-0.6B-GGUF, batiai/Qwen3-Embedding-8B-GGUF, ibm-granite/granite-embedding-311m-multilingual-r2, ibm-granite/granite-embedding-97m-multilingual-r2, intfloat/multilingual-e5-base, intfloat/multilingual-e5-small, sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, sentence-transformers/paraphrase-multilingual-mpnet-base-v2 |
| sg_h046 | 0.00 | ibm-granite/granite-embedding-97m-multilingual-r2 |
| sg_h064 | 0.00 | mradermacher/next-12b-i1-GGUF, timpal0l/mdeberta-v3-base-squad2 |
| sg_h069 | 0.00 | LLM-OS-Models/KoHRM-Text-1.4B-GGUF, microsoft/Phi-4-mini-instruct |
| sg_h070 | 0.00 | Systran/faster-whisper-base, Systran/faster-whisper-tiny |
| sg_h072 | 0.20 | Snowflake/snowflake-arctic-embed-l-v2.0, batiai/Qwen3-Embedding-4B-GGUF, batiai/Qwen3-Embedding-8B-GGUF, ibm-granite/granite-embedding-311m-multilingual-r2 |
| sg_h103 | 0.00 | CMSManhattan/JiRackUltra_1b |
| sg_h104 | 0.33 | Alibaba-NLP/gte-multilingual-base, BidirLM/BidirLM-0.6B-Embedding, PeterAM4/Qwen3-Embedding-0.6B-GGUF, Snowflake/snowflake-arctic-embed-l-v2.0 |
| sg_h105 | 0.25 | Systran/faster-whisper-small, openai/whisper-large-v3-turbo, openai/whisper-small |
| sg_h106 | 0.33 | bongsoo/albert-small-kor-cross-encoder-v1, clapAI/mmBERT-small-multilingual-sentiment |

## 추가 판정이 필요한 후보

이번 실험의 설정 중 하나 이상에서 top-10에 나왔지만 아무도 판정하지 않은 모델이 질의 24개에 걸쳐 207개다. 목록은 JSON의 `unjudged_pool`에 있다.

## 해석 주의

- 질의가 20개 안팎이라 Recall 차이 0.05 이하는 질의 1개 차이일 수 있다. 개선 판단 전에 질의별 결과(JSON)를 확인한다.
- 가중치 탐색과 평가에 같은 질의를 쓴다. 고른 가중치는 다른 질의에서 다시 확인해야 한다.
- Judged@10은 top-10 중 누군가 판정한 모델의 비율이다. 판정 후보 풀은 BM25·다운로드 상위에서 뽑았으므로, 이 값이 낮은 설정(특히 dense 비중이 큰 설정)은 미판정 모델 때문에 Recall이 낮게 나올 수 있다. JSON의 `unjudged@10`을 판정실에서 추가 판정하면 보정된다.
- 사전 검색 LLM 지연은 캐시에 기록된 최초 호출 시간이다. 여러 변환은 병렬 실행을 가정해 가장 느린 것만 더한다.
