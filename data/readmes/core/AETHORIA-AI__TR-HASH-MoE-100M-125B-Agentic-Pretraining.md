---
license: cc-by-nc-4.0
language:
- en
- fr
pipeline_tag: text-generation
library_name: pytorch
tags:
- tr_hash_moe
- tr-hash
- mixture-of-experts
- deterministic-routing
- multi-hash-routing
- agentic-pretraining
- gqa
- custom-code
datasets:
- AETHORIA-AI/TR-HASH-Pretraining-125B-Agentic-32K
---

# TR-HASH MoE 100M - 125B Agentic Pretraining

This repository is the live checkpoint archive for a **100,366,720-parameter TR-HASH MoE language model** trained on the audited [AETHORIA-AI/TR-HASH-Pretraining-125B-Agentic-32K](https://huggingface.co/datasets/AETHORIA-AI/TR-HASH-Pretraining-125B-Agentic-32K) corpus.

> **Status: pretraining complete.** The verified base checkpoint is available under `final/`. The numbered `token_pack_*` directories remain resumable historical snapshots.
>
> **Lineage correction (September 2026):** the first 100M refinement and its SFT descendants used a mismatched optimizer-update unit and have been withdrawn from public use. This does not invalidate the pretraining checkpoint in this repository. We apologize for the mismatch. A [corrected fresh-optimizer refinement](https://huggingface.co/AETHORIA-AI/TR-HASH-MoE-100M-70B-Agentic-Refinement-Corrected) is now running directly from this verified `final/` checkpoint.

## Architecture

TR-HASH replaces a learned MoE router with deterministic multi-hash token routing. Each token ID is assigned to a stable top-2 expert pair at every layer. The model retains a shared SwiGLU expert and combines its output with the routed branch.

| Field | Value |
|---|---:|
| Parameters | 100,366,720 |
| Vocabulary | 32,000 |
| Context length | 2,048 tokens |
| Layers | 10 |
| Hidden size | 640 |
| Attention heads | 10 |
| KV heads | 2 |
| Head dimension | 64 |
| Routed intermediate size | 1,824 |
| Experts | 4 |
| Experts per token | 2 |
| Routing | deterministic token-ID multi-hash |
| Route weights | 0.5 / 0.5 |
| Shared branch scale | 1.0 |
| Routed branch scale | 2.0 |
| Position encoding | RoPE |
| Normalization | RMSNorm |
| Attention | causal GQA |

The exact machine-readable topology is available in [`config.json`](./config.json).

## Training lineage

The pretraining stage is deliberately separated from refinement and instruction tuning:

1. **Pretraining — complete:** 70B unique tokens plus 55B proportional replay, for exactly **124,999,598,080 trained tokens**.
2. **Corrected refinement — running:** one fresh-optimizer pass over the same audited **70B unique-token core**, using 3,932,160 tokens per optimizer update, 17,801 planned updates, peak LR `1e-4`, a 500M-token warmup and cosine decay.
3. **Instruction tuning — pending replacement:** a new full-parameter SFT will be trained only after the corrected refinement has completed and passed held-out evaluation.

The source corpus contains **75B foundation tokens and 50B agentic-oriented tokens**. “Agentic” here describes the data mixture, including code, tool-use and structured technical material; it does not by itself imply that this base checkpoint is an instruction-following agent.

## Pretraining configuration

| Field | Value |
|---|---:|
| Hardware | 4 x NVIDIA RTX 5090 |
| Precision | BF16 |
| Sequence length | 2,048 |
| Batch per GPU | 28 sequences |
| Global batch | 112 sequences |
| Gradient accumulation | 1 |
| Tokens per optimizer step | 229,376 |
| Planned optimizer steps | 544,955 |
| Optimizer | AdamW |
| Peak learning rate | 3e-4 |
| Scheduler | WSD |
| Warmup | 1B tokens |
| Checkpoint packs | 40 planned |

The run uses the [Complexity framework](https://github.com/Complexity-ML/complexity-framework) with distributed data parallelism, fused CUDA/Triton kernels and audited token replay plans.

## Pretraining representation probe

The figure below shows routed-expert contributions from the verified
pretraining `final/` checkpoint only. It uses the first 128 PIQA validation
records, with no chat template and no added special tokens. Five layers are
sampled, with both routed contributions shown for every sampled token.

![TR-HASH 100M pretraining final routed-expert contribution t-SNE](./assets/tsne_100m_pretraining_only.png)

Each layer uses an independent PCA plus t-SNE fit. Absolute coordinates are
therefore not aligned between panels. The visualization is exploratory and
does not establish semantic expert specialization or downstream quality.

## Refinement correction

The withdrawn refinement used only **229,376 tokens per optimizer update**,
instead of the corrected **3,932,160-token** update contract. It consequently
performed about 17.14 times as many AdamW updates per source token and behaved
closer to prolonged continued training than to the intended large-batch
refinement. The replacement run starts from `final/` with fresh optimizer and
scheduler state. Its planned optimizer-update count is logged explicitly at
startup.

## Tokenizer and data

- Tokenizer: [`AETHORIA-AI/TR-HASH-Tokenizer-32K-Agentic`](https://huggingface.co/AETHORIA-AI/TR-HASH-Tokenizer-32K-Agentic)
- Pretokenized corpus: [`AETHORIA-AI/TR-HASH-Pretraining-125B-Agentic-32K`](https://huggingface.co/datasets/AETHORIA-AI/TR-HASH-Pretraining-125B-Agentic-32K)
- Training code: [`Complexity-ML/complexity-framework`](https://github.com/Complexity-ML/complexity-framework)

The tokenizer and dataset revision are pinned by the training launcher. Do not substitute another 32K tokenizer solely because the vocabulary size matches.

## Checkpoint layout

Each `token_pack_NNN_STEP/` directory contains:

- `model.safetensors`: model weights for inspection/export;
- `checkpoint.pt`: framework checkpoint state;
- `optimizer_rank*.pt`: per-rank AdamW optimizer states;
- `training_state.json`: optimizer-step metadata.

For an exact resume, use all files from one complete pack. Do not mix model or optimizer files across pack directories.

## Intended use and limitations

This repository is intended for training continuity, architecture research and reproducibility. Intermediate pretraining checkpoints:

- are not instruction-tuned chat models;
- have not yet passed the final evaluation suite;
- may generate inaccurate, unsafe or incoherent text;
- may change substantially during refinement and SFT;
- are not intended for production deployment or high-stakes decisions.

A replacement instruction-tuned release will be published only after the
corrected refinement and its evaluation are complete.

## License

Released under **CC BY-NC 4.0**. Review the license terms before redistribution or commercial use.
