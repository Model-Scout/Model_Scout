---
language: [ru, es, zh, id, ko, ja, tr, fa, de, hu, ar, vi, fi, el, th, hi]
library_name: transformers
pipeline_tag: text-generation
tags: [pretraining, multilingual, qwen3, muon, intermediate-checkpoint]
---

# L16-1.2B-400B (training in progress)

A 1.16B-parameter base language model, pretrained from scratch on 16 languages with **no English**. The run targets 400B tokens. Checkpoints are published as training goes on.

> **This is an intermediate checkpoint.** `main` currently holds **step 48,440 = 100.0B tokens**, taken while the learning rate is still at its peak, before the final cooldown. Expect it to improve a lot, especially after the cooldown that starts at 360B tokens.

| revision | step | tokens | held-out val loss* |
|---|---|---|---|
| `step048440-100B` (= `main`) | 48,440 | 100.0B | 2.264 (eval at step 48,500) |
| `step024220-50B` | 24,220 | 50.0B | 2.318 (eval at step 24,000) |

\*The val loss is per token of this model's own tokenizer, measured on a held-out 10M-token validation set (625k tokens per language) with document masking. It is not comparable with other tokenizers.

## Languages

Russian, Spanish, Chinese (Simplified), Indonesian, Korean, Japanese, Turkish, Persian, German, Hungarian, Arabic, Vietnamese, Finnish, Greek, Thai and Hindi. The training mixture has 25B tokens per language and contains no English.

## Model

- **Architecture:** Qwen3 decoder, the Marin *delphi* 1.4B configuration: 18 layers, hidden 1792, 14 heads (MHA, head_dim 128), MLP 7168, QK-norm, RoPE θ = 500k, context 4096, untied embeddings.
- **Tokenizer:** [amphora/L16-V65536-chat-tokenizer](https://huggingface.co/amphora/L16-V65536-chat-tokenizer).
  - 65,536-token SentencePiece BPE for the 16 languages.
  - Includes the Llama-3 chat special tokens.
  - The vocab size gives 1.16B params, against 1.4B with the Llama-3 vocab.

## Training

| | |
|---|---|
| Optimizer | MuonH (Muon, Polar Express orthogonalization, hyperball weight norm) at lr 3.5e-3 for weight matrices; AdamW at lr 8.4e-4 for embeddings, head and norms; no weight decay |
| Lookahead | EMA-Nesterov (β = 0.6) during the stable phase |
| Schedule | warmup-stable-decay: 500 warmup steps, constant LR, then a 1-sqrt cooldown over the last 10% (from 360B tokens) |
| Batch | 504 × 4096 = 2.06M tokens per step, 193,752 steps (399.98B tokens) |
| Precision | bf16 autocast, FP8 (tensorwise) for MLP and attention projections, fp32 master weights |
| Data handling | document-boundary attention masking; a single shuffled pass, so no token is repeated |
| Hardware | 6 × H200 |

The peak LR comes from a sweep on the same 400B schedule, early-stopped at 9B tokens with a 1-sqrt decay to 10B. The sweep's best, 1e-2, was then lowered for the 400B horizon, following LR ∝ tokens^-0.3.

Training code: [github.com/guijinSON/delphi-pretrain](https://github.com/guijinSON/delphi-pretrain).

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
repo = "amphora/L16-1.2B-400B"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, revision="step048440-100B", dtype="bfloat16")
ids = tok("대한민국의 수도는", return_tensors="pt")
print(tok.decode(model.generate(**ids, max_new_tokens=20)[0]))
```

The tokenizer adds no BOS token. During training each document was its tokens followed by `</s>`.

## Limitations

- This is a base model: no instruction tuning and no safety tuning.
- It is not trained on English.
- Intermediate checkpoints come from the constant-LR phase and are not annealed.
