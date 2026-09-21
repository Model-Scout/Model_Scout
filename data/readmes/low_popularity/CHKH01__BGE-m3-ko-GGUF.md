---
license: apache-2.0
language:
- ko
- en
tags:
- gguf
- sentence-transformers
- embedding
- xlm-roberta
- bge-m3
- korean
- feature-extraction
- text-embedding
- llama-cpp
- int8
- vulkan
pipeline_tag: sentence-similarity
base_model: dragonkue/BGE-m3-ko
inference: false
---

# BGE-m3-ko GGUF

> Korean-optimized multilingual embedding model — GGUF format for llama.cpp

**BGE-m3-ko** is a Korean-tuned variant of [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3), fine-tuned on Korean retrieval datasets. This repository provides **GGUF** quantized versions for use with [llama.cpp](https://github.com/ggml-org/llama.cpp) and compatible runtimes (llama-cpp-python, Ollama, etc.).

## Model Details

| Attribute | Value |
|-----------|-------|
| **Base model** | [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) |
| **Architecture** | XLMRobertaModel (XLM-RoBERTa) |
| **Parameters** | 567M |
| **Hidden size** | 1024 |
| **Layers** | 24 |
| **Attention heads** | 16 |
| **Max tokens** | 8192 |
| **Pooling** | CLS (`pooling_mode_cls_token: True`) |
| **Normalization** | L2 normalized output |
| **Vocabulary size** | 250,002 |
| **License** | Apache 2.0 |

## GGUF Files

| Filename | Type | Size | Description |
|----------|------|------|-------------|
| `BGE-m3-ko.f16.gguf` | F16 | 1.1 GB | Full-precision, best quality |
| `BGE-m3-ko.Q8_0.gguf` | Q8_0 (int8) | **606 MB** | ✅ Recommended — excellent quality/size tradeoff |

### Quantization Impact

Q8_0 (8-bit block quantization) preserves the model's quality near-identically while reducing the model size by ~45%. For embedding tasks, the quality difference between F16 and Q8_0 is negligible for most use cases.

## Usage

### llama-server (HTTP API) — 권장

**참고**: llama.cpp v3.x부터 `llama-embedding` 바이너리는 별도로 존재하지 않습니다. 임베딩 기능은 `llama-server`에 통합되었습니다.

```bash
# 서버 실행 (Vulkan/CUDA/CPU 백엔드 자동 선택)
llama-server -m BGE-m3-ko.Q8_0.gguf --embedding --pooling cls --port 8080

# Request embeddings via API
curl -X POST http://localhost:8080/embedding \
  -H "Content-Type: application/json" \
  -d '{"content": "대한민국의 수도는 서울입니다"}'

# curl 응답 예시: {"embedding":[0.031159,0.055377,...],"n_tokens":8}
```

### Python (llama-cpp-python)

```python
from llama_cpp import Llama

llm = Llama(
    model_path="./BGE-m3-ko.Q8_0.gguf",
    embedding=True,
    n_ctx=8192,
    pooling_type=2,  # 0=None 1=Mean 2=CLS 3=Last
)

emb = llm.create_embedding("대한민국의 수도는 서울입니다")
print(len(emb["data"][0]["embedding"]))  # 1024
```

### Original PyTorch (sentence-transformers)

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("dragonkue/BGE-m3-ko")
embeddings = model.encode(["대한민국의 수도는 서울입니다"])
print(embeddings.shape)  # (1, 1024)
```

## Evaluation (MIRACL Korean Retrieval)

| Metric | Score |
|--------|-------|
| Cosine Accuracy@1 | 0.6103 |
| Cosine Accuracy@3 | 0.8169 |
| Cosine Accuracy@5 | 0.8732 |
| Cosine Accuracy@10 | 0.9202 |
| Cosine NDCG@10 | 0.6833 |
| Cosine MRR@10 | 0.7262 |
| Cosine MAP@100 | 0.6074 |

## Conversion Details

Converted from [dragonkue/BGE-m3-ko](https://huggingface.co/dragonkue/BGE-m3-ko) using llama.cpp's `convert_hf_to_gguf.py` at b9471.

```bash
# Convert to F16
python3 convert_hf_to_gguf.py ./dragonkue/BGE-m3-ko \
    --outfile BGE-m3-ko.f16.gguf --outtype f16

# Quantize to Q8_0
llama-quantize BGE-m3-ko.f16.gguf BGE-m3-ko.Q8_0.gguf Q8_0
```

### GGUF Metadata
- **Architecture**: `bert` (GGUF BERT — XLM-RoBERTa mapped to BERT arch)
- **Tokenizer**: `t5` type (SentencePiece Unigram)
- **Pooling**: CLS
- **Causal attention**: False

## Intended Use

This model is designed for:
- **Korean text embeddings** (primarily)
- **English + multilingual embeddings** (inherited from bge-m3)
- **Semantic search / retrieval**
- **Text clustering and classification**
- **RAG (Retrieval-Augmented Generation) pipelines**

## License

Apache 2.0. The original model [dragonkue/BGE-m3-ko](https://huggingface.co/dragonkue/BGE-m3-ko) is also Apache 2.0.

---

# BGE-m3-ko GGUF

> 한국어 최적화 멀티링귀얼 임베딩 모델 — llama.cpp용 GGUF 포맷

**BGE-m3-ko**는 [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3)를 한국어 검색 데이터셋에 파인튜닝한 임베딩 모델입니다. 본 저장소는 llama.cpp 및 호환 런타임(ollama, llama-cpp-python)에서 사용 가능한 **GGUF 양자화 버전**을 제공합니다.

## GGUF 파일

| 파일명 | 타입 | 용량 | 설명 |
|--------|------|------|------|
| `BGE-m3-ko.f16.gguf` | F16 | 1.1 GB | 최고 정밀도 |
| `BGE-m3-ko.Q8_0.gguf` | Q8_0 (int8) | **606 MB** | ✅ 추천 — 우수한 품질/용량 균형 |

## 사용법

### llama-server (HTTP API) — 권장

**참고**: `llama-embedding` 바이너리는 별도로 존재하지 않습니다. 임베딩은 `llama-server`에 통합되었습니다.

```bash
# 서버 실행 (Vulkan/CUDA/CPU)
llama-server -m BGE-m3-ko.Q8_0.gguf --embedding --pooling cls --port 8080

# 임베딩 요청
curl -X POST http://localhost:8080/embedding \
  -H "Content-Type: application/json" \
  -d '{"content": "임베딩할 문장"}'
```

### Python (llama-cpp-python)

```python
from llama_cpp import Llama
llm = Llama(model_path="BGE-m3-ko.Q8_0.gguf", embedding=True, n_ctx=8192, pooling_type=2)
emb = llm.create_embedding("임베딩할 문장")
print(emb["data"][0]["embedding"])
```

## 라이선스

Apache 2.0
