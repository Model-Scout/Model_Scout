---
library_name: transformers
license: apache-2.0
language:
- multilingual
- en
- zh
- de
- fr
- es
- ru
- ja
- ko
- ar
- hi
tags:
- reranker
- cross-encoder
- matryoshka
- 2d-matryoshka
- long-context
- modernbert
- sentence-similarity
- information-retrieval
datasets:
- cfli/bge-m3-data
base_model: vllm-sr/mmbert-32k-yarn
pipeline_tag: text-classification
---

# mmbert-rerank-32k-2d-matryoshka

A **32K context multilingual reranker** with **2D Matryoshka** support, enabling flexible layer and dimension reduction for efficient inference.

## Model Description

This model is a cross-encoder reranker built on [mmbert-32k-yarn](https://huggingface.co/vllm-sr/mmbert-32k-yarn), a ModernBERT model extended to 32K context via YaRN position interpolation and trained on 1800+ languages from the Glot500 corpus.

### Key Features

| Feature | Value |
|---------|-------|
| **Context Length** | 32,768 tokens (64× longer than typical 512-token rerankers) |
| **Languages** | 1800+ (Glot500 multilingual) |
| **Parameters** | 308M |
| **Architecture** | ModernBERT + 2D Matryoshka Cross-Encoder |
| **Flash Attention** | ✅ Supported |

### 2D Matryoshka Architecture

This model implements **2D Matryoshka Representation Learning**, allowing you to trade quality for speed by using:
- **Fewer layers**: 3, 6, 11, or 22 (full)
- **Fewer dimensions**: 64, 128, 256, 512, or 768 (full)

This provides 20 different quality-speed configurations from a single model.

## Benchmark Results

### Long Document Reranking (Key Advantage)

We evaluate on synthetic long documents (~1500 tokens) where the relevant answer is placed at different positions. This tests whether models can use their full context window.

| Test Case | mmbert-rerank | BGE-reranker-v2-m3 | Qwen3-Reranker-0.6B |
|-----------|---------------|-------------------|---------------------|
| Answer at **START** | **100%** | **100%** | **100%** |
| Answer at **END** | **100%** | **33%** ❌ | **100%** |

**Key Finding**: BGE truncates inputs at 512 tokens, causing it to **completely miss** relevant information beyond that limit. mmbert-rerank maintains **100% accuracy** with its 32K context window.

### Latency Benchmark

Measured on AMD MI300X GPU:

| Metric | mmbert-rerank | BGE-reranker-v2-m3 | Qwen3-Reranker-0.6B |
|--------|---------------|-------------------|---------------------|
| **Short doc** (~15 tokens) | 19.0ms | **8.3ms** | 21.5ms |
| **Long doc** (~1500 tokens) | 24.0ms | 11.9ms* | 28.8ms |
| **Throughput** (batch 10) | 506 q/s | **1193 q/s** | 422 q/s |

*BGE truncates at 512 tokens, so it doesn't actually process long docs

### Multilingual Performance

Tested on 8 languages including low-resource African languages (Swahili, Yoruba, Amharic, Hausa, Igbo):

| Language Type | mmbert-rerank | BGE-reranker-v2-m3 | Qwen3-Reranker-0.6B |
|--------------|---------------|-------------------|---------------------|
| High-resource (EN/ZH/ES) | **100%** | **100%** | **100%** |
| Low-resource (SW/YO/AM/HA/IG) | **100%** | **100%** | **100%** |

### BEIR Benchmark (Short Documents)

On standard BEIR datasets with short documents (where BGE's 512-token limit is sufficient):

| Dataset | Avg Tokens | mmbert MRR | BGE MRR |
|---------|-----------|------------|---------|
| SciFact | 279 | 94.9 | **95.6** |
| NFCorpus | 304 | 87.2 | **89.7** |
| HotpotQA | 61 | **100.0** | **100.0** |
| FiQA | 173 | 93.9 | **96.0** |

On short documents, BGE is slightly better due to its focused training on shorter contexts.

## When to Use This Model

| Scenario | Recommendation |
|----------|----------------|
| **Short docs (<512 tokens)** | Use BGE (faster, slightly better) |
| **Long docs (>512 tokens)** | **Use mmbert** (BGE fails) |
| **Documents with key info at end** | **Use mmbert** (BGE truncates) |
| **Low-resource languages** | **Use mmbert** (1800+ languages) |
| **Need speed/quality tradeoff** | **Use mmbert** (2D Matryoshka) |

## Usage

### Installation

```bash
pip install transformers torch
```

### Basic Usage

```python
import torch
from transformers import AutoTokenizer

# Load model (custom class required)
import sys
sys.path.append("path/to/scripts")
from train_rerank import Matryoshka2DReranker

model = Matryoshka2DReranker.from_pretrained("vllm-sr/mmbert-rerank-32k-2d-matryoshka")
tokenizer = AutoTokenizer.from_pretrained("vllm-sr/mmbert-rerank-32k-2d-matryoshka")

model.eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# Score query-passage pairs
pairs = [
    ("What is machine learning?", "Machine learning is a subset of AI that enables systems to learn from data."),
    ("What is machine learning?", "The weather is sunny today."),
]

scores = model.compute_score(pairs, tokenizer, normalize=True)
# Output: [0.9686, 0.0017]
```

### Using Reduced Layers/Dimensions (2D Matryoshka)

```python
# Full model (22 layers, 768 dims) - highest quality
scores = model.compute_score(pairs, tokenizer, normalize=True)

# Reduced layers (use layer 11 for good balance)
scores = model.compute_score(pairs, tokenizer, layer_idx=11, normalize=True)

# Reduced dimensions
scores = model.compute_score(pairs, tokenizer, dim_idx=256, normalize=True)

# Both reduced (fastest)
scores = model.compute_score(pairs, tokenizer, layer_idx=11, dim_idx=256, normalize=True)
```

### Reranking Pipeline

```python
def rerank(query: str, passages: list[str], top_k: int = 10) -> list[tuple[str, float]]:
    """Rerank passages by relevance to query."""
    pairs = [(query, p) for p in passages]
    scores = model.compute_score(pairs, tokenizer, normalize=True)
    
    # Sort by score descending
    ranked = sorted(zip(passages, scores), key=lambda x: x[1], reverse=True)
    return ranked[:top_k]

# Example
query = "How does photosynthesis work?"
passages = [
    "Photosynthesis is the process by which plants convert sunlight into energy.",
    "The stock market closed higher today.",
    "Plants use chlorophyll to absorb light during photosynthesis.",
    "Python is a popular programming language.",
]

results = rerank(query, passages, top_k=2)
# [("Photosynthesis is the process...", 0.95), ("Plants use chlorophyll...", 0.87)]
```

## Training Details

### Training Data

- **Dataset**: [cfli/bge-m3-data](https://huggingface.co/datasets/cfli/bge-m3-data)
- **Samples**: 1,569,864 query-passage pairs
- **Languages**: 100+ languages from multilingual sources

### Training Configuration

| Parameter | Value |
|-----------|-------|
| Base Model | vllm-sr/mmbert-32k-yarn |
| Epochs | 1 |
| Batch Size | 16 |
| Gradient Accumulation | 2 |
| Effective Batch Size | 32 |
| Learning Rate | 2e-5 |
| Max Length | 32,768 |
| Precision | BFloat16 |
| Optimizer | AdamW |
| Hardware | AMD MI300X (196GB) |
| Training Time | 6h 57m |
| Final Loss | 0.3173 |

### 2D Matryoshka Configuration

| Parameter | Value |
|-----------|-------|
| Layer Indices | 3, 6, 11, 22 |
| Dimension Indices | 64, 128, 256, 512, 768 |
| Classification Heads | 20 (4 layers × 5 dims) |
| Loss | Binary Cross-Entropy (averaged across all heads) |

## Comparison with Competitors

| Attribute | BGE-reranker-v2-m3 | Qwen3-Reranker-0.6B | mmbert-rerank-32k |
|-----------|-------------------|---------------------|-------------------|
| **Parameters** | 568M | 600M | **308M (smallest)** |
| **Context Length** | 512 | 8,192 | **32,768 (longest)** |
| **Architecture** | Encoder | Decoder | **Encoder (fast)** |
| **Long Doc Quality** | ❌ Fails | ✅ Good | ✅ **Good** |
| **Short Doc Speed** | **Fastest** | Slowest | Middle |
| **2D Matryoshka** | ❌ No | ❌ No | ✅ **Yes** |
| **Languages** | 100+ | ~100 | **1800+** |

## Model Architecture

```
Matryoshka2DReranker
├── encoder: ModernBertModel (308M params)
│   └── 22 transformer layers
│   └── hidden_size: 768
│   └── YaRN position interpolation (32K context)
├── final_norm: LayerNorm (applied to intermediate layers)
└── layer_heads: ModuleDict
    ├── "3": {"64": Linear, "128": Linear, ..., "768": Linear}
    ├── "6": {"64": Linear, "128": Linear, ..., "768": Linear}
    ├── "11": {"64": Linear, "128": Linear, ..., "768": Linear}
    └── "22": {"64": Linear, "128": Linear, ..., "768": Linear}
```

## Limitations

- **Training data**: While the model supports 32K tokens, training was primarily on shorter passages from BGE-M3 data. Performance on very long passages relies on the base model's YaRN-extended context.
- **Domain-specific data**: Model was trained on general web data; may require fine-tuning for specialized domains.
- **Layer reduction speedup**: Due to the need for all hidden states, layer reduction provides minimal speedup without early-exit modifications.

## License

Apache 2.0

## Citation

```bibtex
@misc{mmbert-rerank-2025,
  title={mmbert-rerank-32k-2d-matryoshka: A Long-Context Multilingual Reranker with 2D Matryoshka},
  author={LLM Semantic Router Team},
  year={2025},
  url={https://huggingface.co/vllm-sr/mmbert-rerank-32k-2d-matryoshka}
}
```

## Acknowledgments

- [ModernBERT](https://huggingface.co/answerdotai/ModernBERT-base) for the base architecture
- [BGE-M3](https://huggingface.co/BAAI/bge-m3) for training data
- [Matryoshka Representation Learning](https://arxiv.org/abs/2205.13147) for the dimensional reduction approach
