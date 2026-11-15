---
language:
- ko
license: apache-2.0
library_name: transformers
tags:
- korean
- causal-lm
- pretraining
- small-language-model
pipeline_tag: text-generation
---

# HanForge 35M (Korean Base)

HanForge 35M is a small Korean causal language model pretrained from scratch on a **467M-token** Korean corpus on a single MacBook. It is a research-friendly base model for downstream fine-tuning. The model is **not instruction-tuned**; see [`drlee1/HanForge-47M-SFT`](https://huggingface.co/drlee1/HanForge-47M-SFT) for the chat model.

> **Updated 2026-10-06.** `modeling_hanforge.py` now computes the rotary position encoding on every forward pass. With the previous code, `transformers` 5 left it uninitialized after `from_pretrained`. The weights are unchanged. See [Changelog](#changelog).

## Model Details

| | |
|---|---|
| **Architecture** | Llama-style decoder (RMSNorm, RoPE, Grouped-Query Attention) |
| **Parameters** | 34.84M (output layer tied to the embedding; the file stores it separately, 47.13M tensors in total) |
| **Hidden size** | 512 |
| **Layers** | 8 |
| **Attention heads** | 8 (KV heads: 2, GQA) |
| **Intermediate size** | 1408 |
| **Max position** | 4096 (RoPE θ = 50000) |
| **Vocab size** | 24,000 |
| **Tokenizer** | SentencePiece BPE, Korean-optimized (~2.17 chars/token) |

## Intended Use

This model is intended for:

- **Continued fine-tuning** on Korean downstream tasks (instruction tuning, classification, etc.)
- **Korean text continuation** and language modeling research
- **Educational use**: exploring small language model training on a single language

It is **not** intended for:

- Direct chat or instruction following (use the fine-tuned variant)
- Production text generation without further training and safety review
- Tasks requiring factual accuracy, reasoning, or multilingual capability

## Training Data

A **467M-token** Korean corpus drawn from three publicly available sources:

| Source | Description |
|---|---|
| Wikipedia (Korean) | Encyclopedic articles, factual prose |
| FineWeb-2 (Korean subset) | Filtered Korean web text |
| korean-webtext-edu | Educational Korean web content |

The corpus was deduplicated, length-filtered, and tokenized with a Korean-optimized SentencePiece BPE (24k vocab) trained on the same data.

## Training Procedure

| | |
|---|---|
| **Steps** | 6,000 |
| **Tokens seen** | about 393M (0.84 epoch of the 467M-token corpus) |
| **Batch size (effective)** | 32 sequences × 2,048 tokens (8 × 4 gradient accumulation) |
| **Sequence length** | 2,048 |
| **Optimizer** | AdamW (β1 = 0.9, β2 = 0.999, weight decay 0.1) |
| **Learning rate** | 6e-4 peak, cosine schedule, 300 warmup steps |
| **Precision** | bf16 mixed precision |
| **Hardware** | MacBook Pro M5 Pro 48GB (MPS), about 14 hours |

## Evaluation

| Metric | Value |
|---|---|
| Held-out perplexity (512 pretraining samples, end of training) | 47.19 |
| Grammar minimal pairs (51 pairs, length-normalized log-likelihood) | 98.0% (50/51) |

The minimal-pair accuracy was measured on 2026-10-06 with the fixed modeling code. An earlier figure of 60.8% was measured while the rotary position encoding was broken and is withdrawn.

## Limitations and Bias

- **Small scale (35M)**: limited reasoning, factual accuracy, and long-form coherence
- **Single-language pretrain**: no English or other language capability
- **Web-derived data**: may reflect biases present in Korean web text; no explicit safety filtering was applied
- **Short pretrain**: about 393M tokens, roughly 11 times the parameter count, well below modern practice

This model has not been aligned, RLHF'd, or safety-tuned. Do not deploy in user-facing applications without further training and review.

## Changelog

**2026-10-06**: `modeling_hanforge.py` computes the rotary frequencies (`inv_freq`) from the config on every forward pass. Under `transformers` 5, `from_pretrained` left this non-persistent buffer uninitialized (zeros or arbitrary values), so position information was missing or random. Weights are unchanged. The model card numbers were corrected against the training logs (sequence length, batch, learning rate, tokens seen, perplexity).

**2026-05-08**: initial release.

## License

Released under the **Apache License 2.0**. The underlying pretraining corpora are subject to their own licenses.

## Citation

```bibtex
@misc{hanforge_base_2026,
  author = {DongRyeol Lee},
  title  = {HanForge 35M: A Small Korean Language Model Pretrained from Scratch},
  year   = {2026},
  note   = {Pretrained on a 467M-token Korean corpus with a 24k SentencePiece BPE tokenizer}
}
```
