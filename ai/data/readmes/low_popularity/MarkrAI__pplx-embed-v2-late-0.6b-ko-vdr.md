---
language:
- ko
- en
- multilingual
license: apache-2.0
tags:
- sentence-transformers
- multi-vector
- colbert
- late-interaction
- visual-document-retrieval
base_model: perplexity-ai/pplx-embed-v2-late-0.6b
pipeline_tag: feature-extraction
library_name: sentence-transformers
---

# 🔎 pplx-embed-v2-late-0.6b-ko-vdr

**pplx-embed-v2-late-0.6b-ko-vdr** is a 0.6B late-interaction (multi-vector) retriever for **Korean visual document retrieval**: it retrieves document page screenshots for text queries. It is fine-tuned from [perplexity-ai/pplx-embed-v2-late-0.6b](https://huggingface.co/perplexity-ai/pplx-embed-v2-late-0.6b) and improves nDCG@10 over the base model on Korean benchmarks (KoViDoRe, SDS-KoPub-VDR, MIRACL-VISION Korean subset) as well as on ViDoRe v3.

## Key Characteristics

- **Late interaction (ColBERT-style)**: queries and pages are encoded into sequences of 128-dimensional token vectors and scored with MaxSim.
- **Visual document retrieval**: documents are page images (screenshots of PDFs, reports, slides), so no OCR or layout parsing is needed.
- **Compact**: 0.6B parameters.
- **Input lengths**: up to 1,024 query tokens and 4,096 document tokens.

## Usage

```bash
pip install -U sentence-transformers
```

Use `encode_query` / `encode_document`: they add the `[Q] ` / `[D] ` prompts the model was trained with.

```python
from sentence_transformers import MultiVectorEncoder

# Download from the 🤗 Hub
model = MultiVectorEncoder("MarkrAI/pplx-embed-v2-late-0.6b-ko-vdr")
# Run inference: each input becomes a sequence of per-token vectors (variable length).
queries = [
    '30인 이상 상용근로자를 보유한 기업의 1인당 평균 월별 법정외 복지비용이 10~29인 규모 기업보다 높은지 판단해 주세요.',
]
documents = [
    'path/to/page_1.png',  # page screenshot (file path, URL, or PIL.Image)
    'path/to/page_2.png',  # page screenshot (file path, URL, or PIL.Image)
    'path/to/page_3.png',  # page screenshot (file path, URL, or PIL.Image)
]
query_embeddings = model.encode_query(queries)
document_embeddings = model.encode_document(documents)
print(query_embeddings[0].shape, document_embeddings[0].shape)
# e.g. (40, 128) (1718, 128)

# Get the MaxSim similarity scores
similarities = model.similarity(query_embeddings, document_embeddings)
print(similarities)
```

> **Note:** The base model uses `causal_conv1d` CUDA kernels, so inference requires a GPU.

## Evaluation

Evaluated with [MTEB](https://github.com/embeddings-benchmark/mteb). We report nDCG@10.

| Model | Params | KoViDoRe (avg. 4) | SDS-KoPub-VDR | MIRACL-VISION (Korean subset) | ViDoRe v3 (avg. 8 public) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **pplx-embed-v2-late-0.6b-ko-vdr** | 0.6B | **0.6345** | **0.8546** | **0.7331** | **0.6309** |
| [perplexity-ai/pplx-embed-v2-late-0.6b](https://huggingface.co/perplexity-ai/pplx-embed-v2-late-0.6b) | 0.6B | 0.6053 | 0.8235 | 0.7094 | 0.6160 |

<details>
<summary>Per-task nDCG@10</summary>

**KoViDoRe**

| Model | Avg | Cybersecurity | Economic | Energy | HR |
| :--- | ---: | ---: | ---: | ---: | ---: |
| **pplx-embed-v2-late-0.6b-ko-vdr** | **0.6345** | 0.8188 | 0.3854 | 0.7373 | 0.5966 |
| [perplexity-ai/pplx-embed-v2-late-0.6b](https://huggingface.co/perplexity-ai/pplx-embed-v2-late-0.6b) | 0.6053 | 0.7691 | 0.3636 | 0.7030 | 0.5854 |

**ViDoRe v3** (public)

| Model | Avg | ComputerScience | Energy | FinanceEn | FinanceFr | HR | Industrial | Pharmaceuticals | Physics |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **pplx-embed-v2-late-0.6b-ko-vdr** | **0.6309** | 0.7706 | 0.7034 | 0.6935 | 0.5249 | 0.6541 | 0.5420 | 0.6788 | 0.4800 |
| [perplexity-ai/pplx-embed-v2-late-0.6b](https://huggingface.co/perplexity-ai/pplx-embed-v2-late-0.6b) | 0.6160 | 0.7502 | 0.6978 | 0.6717 | 0.5049 | 0.6438 | 0.5191 | 0.6650 | 0.4751 |

</details>

## Citation

If you use this model, please cite:

```bibtex
@misc{markrai2026pplxembedv2late06bkovdr,
  author = {{Marker-Inc-Korea} and Yongbin Choi},
  title = {{pplx-embed-v2-late-0.6b-ko-vdr: A Late-Interaction Retriever for Korean Visual Document Retrieval}},
  year = {2026},
  url = {https://huggingface.co/MarkrAI/pplx-embed-v2-late-0.6b-ko-vdr}
}
```

### Base Model

```bibtex
@online{perplexity2026MultimodalEmbeddingsBeyondASingleVector,
  author = {{Perplexity} and Markus Krimmel and Louis Milliken and Antoine Chaffin and Sarah Eslami and Ekaterina Glazkova and Maximilian Schall and Bo Wang and Denis Bykov and Jarrod Bryan and Claire Beamer and Jeremy Yang},
  title = {{Multimodal embeddings beyond a single vector}},
  date = {2026-10-07},
  url = {https://www.perplexity.ai/hub/blog/multimodal-embeddings-beyond-a-single-vector}
}
```

### KoViDoRe

```bibtex
@inproceedings{choi2026kovidore,
  title={KoViDoRe: A Benchmark for Korean Visual Document Retrieval},
  author={Choi, Yongbin and Song, Yongwoo and Sung, Mujeen},
  booktitle={Proceedings of the 2nd Workshop on Multimodal Augmented Generation via Multimodal Retrieval (MAGMaR 2026)},
  pages={54--80},
  year={2026}
}
```
