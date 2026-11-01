---
license: apache-2.0
base_model: Qwen/Qwen3-1.7B-Base
language:
- ko
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- qwen3
- vocabulary-trimming
- trimming
- korean
- english
---

# Qwen3-1.7B-Base — vocabulary-trimmed (Korean + English, 32,768)

A vocabulary-**trimmed** version of [`Qwen/Qwen3-1.7B-Base`](https://huggingface.co/Qwen/Qwen3-1.7B-Base):
the byte-level BPE vocabulary is reduced from ~151.7k to **32768** tokens covering **Korean + English**,
and the (tied) embedding matrix is sliced to match. **No retraining** — weights are copied verbatim for
kept tokens, so on kept tokens the model is numerically identical to the original.

Method: [Introduction to Trimming](https://huggingface.co/blog/lbourdois/introduction-to-trimming).

## What changed

| | Original | Trimmed |
|---|---|---|
| Parameters | 1,720,574,976 | 1,476,518,912 (**-14.2%**) |
| Vocab size | 151,669 | 32,768 |
| Merges | 151,387 | 32,486 |
| Embedding | tied | tied (sliced) |

- All 256 byte-level tokens + all 26 special tokens are kept, plus the most frequent Korean/English
  tokens **and their full BPE merge-derivation closure** (so multi-byte Korean stays reachable).
- Verified: lossless round-trip on KO/EN/code; teacher-forced logit equivalence `max|Δ| = 0.0`; greedy
  generation on natural Korean/English is **token-for-token identical** to the base model.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = "ceyda/Qwen3-1.7B-Base-trim-koen-32768"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo)

ids = tok("대한민국의 수도는", return_tensors="pt")
print(tok.decode(model.generate(**ids, max_new_tokens=20)[0], skip_special_tokens=True))
```

## Limitations

- Trimmed for **Korean + English prose**. Code and rare jargon still encode losslessly but may split
  into a few extra tokens. Text in other languages falls back to byte tokens (longer sequences).
- This is a **base** (non-instruction-tuned) model.

## Attribution

Derived from `Qwen/Qwen3-1.7B-Base` (Apache-2.0). Trimming method by Loïck Bourdois.
