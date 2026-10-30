# semantic_constraint 검색 실험

- 질의 50개 (채점 47개), 기준 지표 `recall@10`, 관련 등급 ≥ 1
- Dense `BAAI/bge-m3` · Sparse fielded BM25 · Weighted RRF (k=60) · Pre-Retrieval LLM `gpt-4o-mini`
- 라벨: 기존 라벨 + 추가 판정(supplemental_judgments.jsonl)
- 실행 2026-10-30 20:21

## 실험표

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Baseline | 0.129 | 0.168 | 0.096 | 0.243 | 0.146 | 0.095 | 324ms |

### 보조 지표

| 실험 | P@5 | P@10 | F1@5 | Hit@10 | nRecall@10 | p99 | 제외 위반@10 | Judged@10 |
|---|---|---|---|---|---|---|---|---|
| Baseline | 0.106 | 0.070 | 0.112 | 0.426 | 0.169 | 1717ms | 0.424 | 0.114 |

## top-10에서 놓친 관련 모델 (Baseline)

| 질의 | Recall@10 | 놓친 모델 |
|---|---:|---|
| sg_g006 | 0.00 | Systran/faster-whisper-large-v3, openai/whisper-large-v3, openai/whisper-large-v3-turbo |
| sg_g008 | 0.00 | Systran/faster-whisper-large-v3, openai/whisper-large-v3, openai/whisper-large-v3-turbo |
| sg_g009 | 0.00 | batiai/gemma-4-E2B-it-GGUF, batiai/gemma-4-E4B-it-GGUF |
| sg_g015 | 0.00 | LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct, LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct-GGUF, bartowski/EXAONE-3.5-2.4B-Instruct-GGUF, lmstudio-community/EXAONE-3.5-2.4B-Instruct-GGUF |
| sg_g017 | 0.00 | MLP-KTLim/llama-3-Korean-Bllossom-8B, joongi007/llama-3-Korean-Bllossom-8B-20240809-GGUF |
| sg_g021 | 0.00 | RedHatAI/Qwen2.5-7B-Instruct-FP8-dynamic, RedHatAI/Qwen2.5-7B-Instruct-quantized.w8a8, ThomasBaruzier/Qwen2.5-7B-Instruct-GGUF, unsloth/Qwen2.5-7B-Instruct |
| sg_g028 | 0.00 | OpenVINO/whisper-base-int8-ov, Systran/faster-whisper-base, handy-computer/whisper-base-gguf, openai/whisper-base, openai/whisper-small |
| sg_g029 | 0.00 | LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct, batiai/gemma-4-E2B-it-GGUF, batiai/gemma-4-E4B-it-GGUF |
| sg_h005 | 0.67 | WhitePeak/bert-base-cased-Korean-sentiment |
| sg_h008 | 0.33 | amber-tech/bert-multilingual-passage-reranking-msmarco, bongsoo/albert-small-kor-cross-encoder-v1, bongsoo/kpf-cross-encoder-v1, gpustack/gte-multilingual-reranker-base-GGUF |
| sg_h009 | 0.00 | CohereLabs/North-Micro-Vision-Instruct, CohereLabs/aya-vision-32b, CohereLabs/aya-vision-8b, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, Jackrong/Qwopus3.6-27B-v2-MTP-GGUF, LGAI-EXAONE/EXAONE-4.5-33B, LiquidAI/LFM2.5-VL-1.6B-GGUF, NCSOFT/VARCO-VISION-14B-HF, ONTHEIT/BizOnAI-OCR, thelamapi/next-ocr |
| sg_h011 | 0.00 | CohereLabs/North-Micro-Vision-Instruct, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, Jackrong/Qwopus3.6-27B-v2-MTP-GGUF, skt/A.X-4.0-VL-Light |
| sg_h015 | 0.00 | CMSManhattan/JiRackUltra_14b, ainize/kobart-news, psyche/KoT5-summarization |
| sg_h016 | 0.10 | LiquidAI/LFM2.5-Embedding-350M-GGUF, PeterAM4/Qwen3-Embedding-0.6B-GGUF, Snowflake/snowflake-arctic-embed-l-v2.0, batiai/Qwen3-Embedding-4B-GGUF, batiai/Qwen3-Embedding-8B-GGUF, ibm-granite/granite-embedding-311m-multilingual-r2, ibm-granite/granite-embedding-97m-multilingual-r2, jinaai/jina-embeddings-v3, nvidia/Nemotron-3-Embed-1B-BF16 |
| sg_h017 | 0.00 | Griffin88/sentence-embedding-LaBSE, Youmnaaaa/Semantic-model, beademiguelperez/sentence-transformers-multilingual-e5-small, ibm-granite/granite-embedding-107m-multilingual, ibm-granite/granite-embedding-278m-multilingual, intfloat/multilingual-e5-base, intfloat/multilingual-e5-large, intfloat/multilingual-e5-small, sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, sentence-transformers/paraphrase-multilingual-mpnet-base-v2, sorryhyun/sentence-embedding-klue-large |
| sg_h020 | 0.18 | Aliados/nemotron-3.5-asr-streaming-0.6b, Systran/faster-whisper-small, Systran/faster-whisper-tiny, lemuriandezapada/VibeVoice-ASR-Streaming-AWQ-4bit, microsoft/VibeVoice-ASR-Streaming-1.5B, microsoft/VibeVoice-ASR-Streaming-7B, nvidia/nemotron-3.5-asr-streaming-0.6b, openai/whisper-large-v3, openai/whisper-small |
| sg_h021 | 0.00 | CohereLabs/North-Micro-Vision-Instruct, EZCon/GLM-OCR-4bit-g32-mxfp4-mixed_4_8-mlx |
| sg_h022 | 0.00 | CohereLabs/North-Micro-Vision-Instruct, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, Jackrong/Qwopus3.6-27B-v2-MTP-GGUF |
| sg_h024 | 0.00 | CohereLabs/North-Micro-Vision-Instruct, FadedRedStar/LFM2.5-VL-1.6B-heretic-GGUF, FadedRedStar/LFM2.5-VL-450M-heretic-GGUF, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, Jackrong/Qwopus3.6-27B-v2-MTP-GGUF, Mattimax/DAC6.5 |
| sg_h029 | 0.20 | LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LLM-OS-Models/KoHRM-Text-1.4B-GGUF, LiquidAI/LFM2.5-2.6B-GGUF, LiquidAI/LFM2.5-230M-GGUF |
| sg_h030 | 0.00 | CMSManhattan/JiRackUltra_14b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LLM-OS-Models/KoHRM-Text-1.4B-GGUF, LLM-OS-Models/LFM2.5-8B-A1B-Terminal-ToolBench-Full-SFT-1Epoch-GGUF, LiquidAI/LFM2.5-2.6B-GGUF, LiquidAI/LFM2.5-230M-GGUF, konantech/Konan-LLM-OND |
| sg_h038 | 0.60 | WhitePeak/bert-base-cased-Korean-sentiment, daekeun-ml/koelectra-small-v3-nsmc |
| sg_h043 | 0.50 | bongsoo/albert-small-kor-cross-encoder-v1, bongsoo/kpf-cross-encoder-v1 |
| sg_h052 | 0.17 | facebook/mbart-large-50-many-to-many-mmt, facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M, trillionlabs/Tri-1.8B-Translation |
| sg_h066 | 0.00 | LiquidAI/LFM2.5-230M-GGUF |
| sg_h067 | 0.20 | Systran/faster-whisper-small, kresnik/wav2vec2-large-xlsr-korean, openai/whisper-large-v3, openai/whisper-small |
| sg_h071 | 0.25 | CohereLabs/North-Micro-Vision-Instruct, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF |
| sg_h123 | 0.25 | CMSManhattan/JiRackUltra_1b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LiquidAI/LFM2.5-2.6B-GGUF |
| sg_h124 | 0.00 | CMSManhattan/JiRackUltra_14b, CMSManhattan/JiRackUltra_1b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LiquidAI/LFM2.5-2.6B-GGUF, UNIVA-Bllossom/DeepSeek-llama3.1-Bllossom-8B |
| sg_h125 | 0.00 | Systran/faster-whisper-small, openai/whisper-small |
| sg_h147 | 0.00 | CMSManhattan/JiRackUltra_1b, LiquidAI/LFM2.5-2.6B-GGUF, LiquidAI/LFM2.5-230M-GGUF, mradermacher/next2-fast-i1-GGUF |
| sg_h149 | 0.00 | Systran/faster-whisper-small, Systran/faster-whisper-tiny, openai/whisper-small |
| sg_h150 | 0.33 | Systran/faster-whisper-small, openai/whisper-small |
| sg_h151 | 0.17 | batiai/Qwen3-Embedding-4B-GGUF, batiai/Qwen3-Embedding-8B-GGUF, ibm-granite/granite-embedding-311m-multilingual-r2, jinaai/jina-embeddings-v3, mradermacher/MoAI-Embedding-4B-GGUF |
| sg_h152 | 0.00 | DLCorso/multilingual-e5-small, Hostage928/multilingual-e5-small, MintplexLabs/multilingual-e5-small, intfloat/multilingual-e5-base, intfloat/multilingual-e5-small, sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, sentence-transformers/paraphrase-multilingual-mpnet-base-v2, shannondata/multilingual-e5-small |
| sg_h153 | 0.00 | Helsinki-NLP/opus-mt-ko-en, Helsinki-NLP/opus-mt-tc-big-ko-en |
| sg_h154 | 0.00 | Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF |
| sg_h155 | 0.00 | CohereLabs/North-Micro-Vision-Instruct, CohereLabs/aya-vision-8b, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, mistralai/Ministral-3-3B-Instruct-2512-ONNX |
| sg_h156 | 0.33 | CMSManhattan/JiRackUltra_14b, CMSManhattan/JiRackUltra_1b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LiquidAI/LFM2.5-2.6B-GGUF |
| sg_h157 | 0.00 | CohereLabs/North-Micro-Vision-Instruct, CohereLabs/aya-vision-8b, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF, NCSOFT/VARCO-VISION-14B-HF |
| sg_h158 | 0.33 | CohereLabs/North-Micro-Vision-Instruct, CohereLabs/aya-vision-8b, Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF, Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF |
| sg_h159 | 0.50 | WhitePeak/bert-base-cased-Korean-sentiment, daekeun-ml/koelectra-small-v3-nsmc |
| sg_h161 | 0.12 | CMSManhattan/JiRackUltra_14b, CMSManhattan/JiRackUltra_1b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LiquidAI/LFM2.5-2.6B-GGUF, Mungert/Midm-2.0-Base-Instruct-GGUF, skt/kogpt2-base-v2, trillionlabs/Tri-7B-Base |
| sg_h162 | 0.00 | Systran/faster-whisper-small, Systran/faster-whisper-tiny, aTrain-core/faster-whisper-large-v3-turbo, deepdml/faster-whisper-large-v3-turbo-ct2, deepdml/whisper-large-v3-turbo, jfmdai/faster-whisper-large-v3-turbo-ct2, openai/whisper-large-v3-turbo, openai/whisper-small |
| sg_h163 | 0.67 | gpustack/gte-multilingual-reranker-base-GGUF |

## 추가 판정이 필요한 후보

이번 실험의 설정 중 하나 이상에서 top-10에 나왔지만 아무도 판정하지 않은 모델이 질의 50개에 걸쳐 443개다. 목록은 JSON의 `unjudged_pool`에 있다.

## 해석 주의

- 질의가 20개 안팎이라 Recall 차이 0.05 이하는 질의 1개 차이일 수 있다. 개선 판단 전에 질의별 결과(JSON)를 확인한다.
- 가중치 탐색과 평가에 같은 질의를 쓴다. 고른 가중치는 다른 질의에서 다시 확인해야 한다.
- Judged@10은 top-10 중 누군가 판정한 모델의 비율이다. 판정 후보 풀은 BM25·다운로드 상위에서 뽑았으므로, 이 값이 낮은 설정(특히 dense 비중이 큰 설정)은 미판정 모델 때문에 Recall이 낮게 나올 수 있다. JSON의 `unjudged@10`을 판정실에서 추가 판정하면 보정된다.
- 사전 검색 LLM 지연은 캐시에 기록된 최초 호출 시간이다. 여러 변환은 병렬 실행을 가정해 가장 느린 것만 더한다.
