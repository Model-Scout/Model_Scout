# lexical_exact 검색 실험

- 질의 22개 (채점 21개), 기준 지표 `recall@10`, 관련 등급 ≥ 1
- Dense `BAAI/bge-m3` · Sparse fielded BM25 · Weighted RRF (k=60) · Pre-Retrieval LLM `gpt-4o-mini`
- 실행 2026-10-14 15:53

## 실험표

| 실험 | Recall@5 | Recall@10 | F1@10 | MRR@5 | nDCG@5 | MAP@5 | p95 |
|---|---|---|---|---|---|---|---|
| Baseline | 0.231 | 0.329 | 0.186 | 0.321 | 0.241 | 0.216 | 509ms |

### 보조 지표

| 실험 | P@5 | P@10 | F1@5 | Hit@10 | p99 | 제외 위반@10 | Judged@10 |
|---|---|---|---|---|---|---|---|
| Baseline | 0.181 | 0.143 | 0.184 | 0.619 | 667ms | 0.500 | 0.177 |

## top-10에서 놓친 관련 모델 (Baseline)

| 질의 | Recall@10 | 놓친 모델 |
|---|---:|---|
| sg_g002 | 0.00 | CohereLabs/aya-expanse-8b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct |
| sg_g005 | 0.00 | NHNDQ/nllb-finetuned-en2ko, facebook/nllb-200-distilled-600M |
| sg_h012 | 0.29 | facebook/mbart-large-50-many-to-many-mmt, facebook/nllb-200-1.3B, facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M |
| sg_h013 | 0.40 | R4kSo1997/opus-mt-en-ko-onnx-int8, facebook/mbart-large-50-many-to-many-mmt, facebook/nllb-200-1.3B, facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M |
| sg_h049 | 0.00 | PeterAM4/Qwen3-Embedding-0.6B-GGUF, batiai/Qwen3-Embedding-4B-GGUF, batiai/Qwen3-Embedding-8B-GGUF, mradermacher/MoAI-Embedding-4B-GGUF |
| sg_h051 | 0.57 | facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M |
| sg_h054 | 0.00 | facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M, trillionlabs/Tri-1.8B-Translation |
| sg_h055 | 0.00 | CMSManhattan/JiRackUltra_14b, LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, LiquidAI/LFM2.5-2.6B-GGUF, facebook/nllb-200-distilled-600M, mradermacher/llama3-8b-it-translation-general-en-ko-1sent-i1-GGUF, seongs/ke-t5-base-aihub-koen-translation-integrated-10m-en-to-ko, trillionlabs/Tri-1.8B-Translation |
| sg_h073 | 0.20 | facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M, trillionlabs/Tri-1.8B-Translation |
| sg_h074 | 0.40 | facebook/nllb-200-3.3B, facebook/nllb-200-distilled-1.3B, facebook/nllb-200-distilled-600M |
| sg_h075 | 0.67 | LGAI-EXAONE/EXAONE-3.5-32B-Instruct-GGUF |
| sg_h076 | 0.83 | daekeun-ml/koelectra-small-v3-nsmc |
| sg_h077 | 0.20 | Systran/faster-whisper-medium, Systran/faster-whisper-small, deepdml/faster-whisper-large-v3-turbo-ct2, jfmdai/faster-whisper-large-v3-turbo-ct2 |
| sg_h078 | 0.14 | intfloat/multilingual-e5-base, intfloat/multilingual-e5-small, janni-t/qwen3-embedding-0.6b-int8-tei-onnx, sentence-transformers/LaBSE, sentence-transformers/distiluse-base-multilingual-cased-v1, sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 |
| sg_h079 | 0.00 | mlx-community/Devstral-Small-2507-4bit, mlx-community/c4ai-command-r-08-2024-4bit, mlx-community/c4ai-command-r-plus-4bit, mlx-community/c4ai-command-r-v01-4bit |
| sg_h080 | 0.20 | LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct-AWQ, NotoriousH2/kanana-2-30b-a3b-instruct-awq-w4a16, casperhansen/mistral-large-instruct-2407-awq, mconcat/Qwopus3.6-27B-v2-AWQ-4bit |
| sg_h081 | 0.00 | bespin-global/klue-sroberta-base-continue-learning-by-mnr, sorryhyun/sentence-embedding-klue-large, ys7yoo/sentence-roberta-klue-sts, ys7yoo/sentence-roberta-large-klue-sts |
| sg_h166 | 0.00 | K-intelligence/Midm-2.0-Base-Instruct, K-intelligence/Midm-2.0-Mini-Instruct, Mungert/Midm-2.0-Base-Instruct-GGUF |

## 추가 판정이 필요한 후보

이번 실험의 설정 중 하나 이상에서 top-10에 나왔지만 아무도 판정하지 않은 모델이 질의 22개에 걸쳐 181개다. 목록은 JSON의 `unjudged_pool`에 있다.

## 해석 주의

- 질의가 20개 안팎이라 Recall 차이 0.05 이하는 질의 1개 차이일 수 있다. 개선 판단 전에 질의별 결과(JSON)를 확인한다.
- 가중치 탐색과 평가에 같은 질의를 쓴다. 고른 가중치는 다른 질의에서 다시 확인해야 한다.
- Judged@10은 top-10 중 누군가 판정한 모델의 비율이다. 판정 후보 풀은 BM25·다운로드 상위에서 뽑았으므로, 이 값이 낮은 설정(특히 dense 비중이 큰 설정)은 미판정 모델 때문에 Recall이 낮게 나올 수 있다. JSON의 `unjudged@10`을 판정실에서 추가 판정하면 보정된다.
- 사전 검색 LLM 지연은 캐시에 기록된 최초 호출 시간이다. 여러 변환은 병렬 실행을 가정해 가장 느린 것만 더한다.
