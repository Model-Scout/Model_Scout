---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM2.5-Embedding-350M
library_name: mlx
pipeline_tag: sentence-similarity
language:
- en
- es
- de
- fr
- it
- pt
- ar
- sv
- 'no'
- ja
- ko
tags:
- mlx
- lfm2
- lfm2.5
- embeddings
- sentence-similarity
- feature-extraction
- retrieval
---

# LFM2.5-Embedding-350M — MLX (bf16)

MLX build of [**LiquidAI/LFM2.5-Embedding-350M**](https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M), a multilingual dense bi-encoder (1024-dim CLS embedding, cosine similarity), for local inference on Apple Silicon with [MLX](https://github.com/ml-explore/mlx).

All weights, architecture, and behavior are LiquidAI's. This repository changes the file format (PyTorch/safetensors → MLX) and kept at the original **bf16** precision — it is **not quantized**. Quantized variants (8-bit / 4-bit) are available as sibling repos; see the table below. See the [original model card](https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M) for training details and intended use.

## Conversion details

- Converted with `mlx`; weights unchanged apart from tensor layout (bf16 → MLX bf16).
- The architecture is `Lfm2BidirectionalModel` (a bidirectional LFM2 encoder), which `mlx-lm` / `mlx-embeddings` do not support out of the box, so a small self-contained MLX implementation is included as [`lfm2_bidirectional.py`](lfm2_bidirectional.py).
- **Verified** against the original (PyTorch, float32, identical token ids): worst-case cosine of the CLS embedding ≈ **1.0** across short prompts and a 130-token passage.

## Evaluation

Retrieval quality of this checkpoint (and its sibling precisions), measured as **NDCG@10 / Recall@10** on judged pools. *Retention* = metric ÷ bf16 metric, averaged per-dataset.

**Setup.** English = the four **NanoBEIR** sets (full small corpora, ~2–5k passages, 50 queries each). Multilingual = **MIRACL** dev (the real queries and relevance judgments) for Spanish, German, Japanese, Arabic, each scored over a reduced pool of ~6k passages (judged positives + hard-mined negatives + sampled distractors, from `mteb/MIRACLRetrievalHardNegatives`), 100 queries each. Reduced pools make *absolute* scores easier than full-corpus MIRACL and not leaderboard-comparable — but every precision searches the identical pool, so the **retention** numbers (the point of this table) are sound. ColBERT uses brute-force MaxSim with no query augmentation, so its absolute scores sit a touch below a full PLAID setup.

### Summary (mean over 8 datasets)

| precision | NDCG@10 | NDCG retention | Recall@10 | Recall retention | size |
|---|---|---|---|---|---|
| **bf16** ◄ | 0.728 | 100.0% | 0.775 | 100.0% | 709 MB |
| 8-bit | 0.729 | 100.1% | 0.775 | 100.0% | 377 MB |
| 4-bit | 0.730 | 100.0% | 0.766 | 98.6% | 200 MB |
| mxfp4 | 0.725 | 99.8% | 0.764 | 98.4% | — |

### NDCG@10 by dataset

| dataset | **bf16** ◄ | 8-bit | 4-bit | mxfp4 |
|---|---|---|---|---|
| NanoNQ · en | 0.704 | 0.704 | 0.703 | 0.703 |
| NanoFiQA2018 · en | 0.504 | 0.511 | 0.502 | 0.498 |
| NanoSciFact · en | 0.716 | 0.717 | 0.714 | 0.712 |
| NanoNFCorpus · en | 0.342 | 0.340 | 0.335 | 0.345 |
| MIRACL · es | 0.891 | 0.892 | 0.895 | 0.893 |
| MIRACL · de | 0.809 | 0.810 | 0.819 | 0.812 |
| MIRACL · ja | 0.929 | 0.928 | 0.940 | 0.922 |
| MIRACL · ar | 0.926 | 0.926 | 0.928 | 0.916 |

## License & attribution

Redistributed under the **LFM Open License v1.0** ([`LICENSE`](LICENSE)) — the same license as the original model. Per Section 4, this notice records that the files were **modified (format conversion to MLX)**. The original work is by **Liquid AI**; this repository is an independent conversion, **not affiliated with or endorsed by Liquid AI**. The license includes a **commercial-use threshold (Section 5)** — review it for your use case.

**Base model:** [LiquidAI/LFM2.5-Embedding-350M](https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M)
