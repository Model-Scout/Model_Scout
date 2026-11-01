---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags:
- foundation-model
- sovereign-ai
- fully-open
- open-source
- mixture-of-experts
- moe
- heterogeneous-attention
- latin-square
- from-scratch
- reproducible
- pretrained
- korean
- vidraft
- aether
language:
- ko
- en
datasets:
- HuggingFaceFW/fineweb-edu
- HuggingFaceTB/smollm-corpus
- HuggingFaceTB/finemath
- open-web-math/open-web-math
- OpenCoder-LLM/opc-fineweb-code-corpus
- HAERAE-HUB/KOREAN-WEBTEXT
- HAERAE-HUB/KOREAN-SyntheticText-1.5B
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


> ⚠️ **Use batch_size=1.** Some attention branches (NSA family) do not consume a padding mask, so batching padded sequences can silently corrupt results. Run inference one sequence at a time (batch_size=1).

# Aether-7B-5Attn — Base

<!-- AETHER-FAMILY-LINKS -->

**Aether family** — [![5Attn IT](https://img.shields.io/badge/%F0%9F%92%AC_Aether--7B--5Attn--it-Instruct-green)](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn-it) [![7Attn Base](https://img.shields.io/badge/%F0%9F%A7%A9_Aether--7B--7Attn--base-Open_Weights-teal)](https://huggingface.co/FINAL-Bench/Aether-7B-7Attn-base) [![11Attn](https://img.shields.io/badge/%F0%9F%94%9F_Aether--6B--11Attn-Open_Weights-purple)](https://huggingface.co/FINAL-Bench/Aether-6B-11Attn) [![Checkpoints](https://img.shields.io/badge/%F0%9F%97%82%EF%B8%8F_Checkpoints-Intermediate-lightgrey)](https://huggingface.co/datasets/FINAL-Bench/Aether-7B-5Attn-checkpoints) [![Demo](https://img.shields.io/badge/%F0%9F%9A%80_Demo-Aether_Sovereign_AI-orange)](https://huggingface.co/spaces/FINAL-Bench/Aether-Sovereign-AI) [![Blog](https://img.shields.io/badge/%F0%9F%93%9D_Blog-Open_Source_LLM-yellow)](https://huggingface.co/blog/FINAL-Bench/opensource-llm) [![Collection](https://img.shields.io/badge/%F0%9F%93%9A_Collection-Aether_Foundation-blue)](https://huggingface.co/collections/FINAL-Bench/aether-foundation-model)

<!-- /AETHER-FAMILY-LINKS -->

### Which Aether model should I use?

| Model | What it is | Pick it if |
|---|---|---|
| [**Aether-7B-5Attn**](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn) | 6.59B MoE base. **Fully open** - weights + data recipe + training code + all 162k-step logs + checkpoints | You want to audit, verify or rebuild a foundation model end to end |
| [**Aether-7B-5Attn-it**](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn-it) | The same model, instruction-tuned | You want it to answer rather than continue text |
| [**AETHER-7B-7Attn-base**](https://huggingface.co/FINAL-Bench/AETHER-7B-7Attn-base) | Same 49-layer architecture, a different checkpoint. Open weights | You want a second run of this architecture to compare against |
| [**Aether-6B-11Attn-base**](https://huggingface.co/FINAL-Bench/Aether-6B-11Attn-base) | 121 layers, **11 sequence-mixing mechanisms** in one network - attention, Mamba-2, Hyena, GDN, MLA - on an 11x11 Latin square | You research heterogeneous sequence mixing. It is a mid-training research artifact |

All four load the same way:

```python
AutoModelForCausalLM.from_pretrained(MODEL, trust_remote_code=True, dtype=torch.bfloat16)
```


![Aether-7B-5Attn](aether_hero.png)

[![Blog](https://img.shields.io/badge/%F0%9F%A4%97%20Blog-Read%20the%20Aether%20story-FFD21E)](https://huggingface.co/blog/FINAL-Bench/opensource-llm)




> 📚 **Part of the [Aether Foundation Model collection](https://huggingface.co/collections/FINAL-Bench/aether-foundation-model)** — base, instruction-tuned, and checkpoints in one place.

> 🧩 **Intermediate checkpoints** (110k · 115k · 162k) are released as a dataset: [Aether-7B-5Attn-checkpoints](https://huggingface.co/datasets/FINAL-Bench/Aether-7B-5Attn-checkpoints).
## 🇰🇷 The first Korean foundation model to open its training data and training code

**A 6.59B MoE language model that arranges its attention across 49 layers on a 7×7 Latin square.**
Weights · **training data recipe** · **training code** · **complete training logs** · **full architecture source** — all released.

Trained from scratch on **16 × NVIDIA B200** (2-node FSDP) over **~46 days**, **144.2B tokens** total.
**Apache-2.0**

---

## 1. Why release everything

Most "open" LLMs today give you **weights only**. Weights alone let you neither understand a model, nor verify it, nor rebuild it. A model whose diet is secret is a black box, and you cannot build national or institutional AI sovereignty on a black box.

**The Allen Institute's OLMo reset the bar for what "open" means** — that only by releasing the training data, the training code, and the logs alongside the weights does a model become science. Aether follows that bar.

### What we release

| | Item | Aether |
|---|------|--------|
| 1 | Weights (annealed base) | ✅ |
| 2 | **Full architecture source** — 5 attention types, MoE, Latin-square placement | ✅ `aether_pkg/` |
| 3 | **Training data recipe** — source repos, configs, token counts, mixing weights, tokenizer, EOS | ✅ §5 |
| 4 | **Tokenization script** — the exact file we ran | ✅ `tokenize_one.py` |
| 5 | **Training code** — FSDP launcher, training loop, node scripts | ✅ `launcher_v2b_multi.py` et al. |
| 6 | **Every training hyperparameter** | ✅ §6 |
| 7 | **Complete training log** — all 162,000 steps, 30 days | ✅ `logs/` |
| 8 | **Evaluation code** | ✅ `eval/lmeval_run.py` |
| 9 | Intermediate checkpoints (110k · 115k · 162k) | ✅ |
| 10 | License | ✅ **Apache-2.0** |

**The recipe in §5 alone is enough to reconstruct our training data byte-for-byte.** Every source is a public repository, so identical tokenizer + EOS + mixing weights produce identical binaries. Please verify it. That is what it is for.

### A first for Korean foundation models

Korea has built foundation models from scratch before. **None of them released their training data.** To our knowledge, Aether is the first.

This is what **sovereign AI** actually means. Any country, any company, any lab should be able to rebuild its own foundation model **from scratch** using nothing but this repository. Downloading someone else's weights is not sovereignty.

---


### Open-source fully-open LLMs — 6-country comparison

![Open-source LLM comparison](opensource_llm_comparison.png)

*Across six sovereign fully-open LLMs, disclosure is comparable; Aether is the only single AI startup, with the most attention types (5) in a Latin-square layout.*

## 2. Design — why should every layer use the same attention?

### 2.1 Nothing says one attention must serve all layers

Since GPT, nearly every transformer uses **the same attention at every layer.** A 49-layer model runs the same operation 49 times.

But layers do different jobs. Early layers pick up local morphology and grammar; middle layers handle syntactic structure; late layers work across the whole document. **If the job is different, why must the operation be identical?**

This is a question about a design assumption, not about performance. "Every layer, same attention" is not a proven conclusion — it is a **convention that was never seriously questioned**. Aether relaxes it.

### 2.2 Each attention carries a different inductive bias

| Type | What it is good at | What it costs |
|------|--------------------|---------------|
| `full` | Sees every token pair exactly. No information lost | **Quadratic** in length |
| `sliding` | Sees locality very cheaply (linear in length) | Blind beyond the window |
| `differential` | Subtracts two attention maps to **cancel common-mode noise** | Splits the head dimension in half |
| `nsa` | Gates compressed, selected and sliding branches to reach far cheaply | Structurally complex |
| `hybrid` | Combines `nsa`'s reach with `differential`'s noise suppression | The most expensive |

**None of them dominates the others.** Each is good at something different and pays a different price. Which means **picking one and repeating it 49 times also repeats its weakness 49 times.**

### 2.3 The Latin square is a control, not decoration

"Mixing should help" is an easy intuition, but mixing carelessly makes the result **impossible to attribute**. If `full` happens to cluster in the late layers, the model did well "because its late layers are full" — not "because it is heterogeneous."

That is why the 49 layers form a **7 × 7 Latin square**. A Latin square is a combinatorial arrangement that guarantees **each type appears exactly once in each position**, structurally preventing any type from concentrating at any depth.

The Latin square is therefore a **control mechanism**: it lets the question "what does heterogeneous placement do?" be asked without placement bias.

**To our knowledge, no released model places heterogeneous attention in a Latin square.**

---

## 3. Attention composition — a 7×7 Latin square over 49 layers

Seven attention labels are placed across 49 layers along the Latin square, **exactly 7 layers each** (7 × 7 = 49).

| Label | Layers | Description |
|-------|--------|-------------|
| `full` | 7 | Standard causal attention (SDPA) |
| `differential` | 7 | Splits Q·K in half, builds two attention maps, subtracts them λ-weighted to cancel common noise |
| `sliding` | 7 | Sliding window (window = 512) — masking over the full path |
| `nsa` | 7 | Compressed / selected / sliding branches combined by a learned gate |
| `hybrid` | 7 | `nsa` + `differential` combined |
| `compress` | 7 | NSA block-mean path — runs the full path in this checkpoint |
| `linear` | 7 | SDPA + a learned gate |
| **Total** | **49** | |

**Where the name `5Attn` comes from.** The seven labels reduce to **five distinct mechanisms**: `compress` runs the full path, and `linear` is SDPA plus a gate. The model is named for the number of mechanisms (5), not the number of labels (7).

The placement rule and every implementation are in `aether_pkg/`. See `LATIN_SQUARE_7x7` for the layer↔label mapping.

### 3.1 Measured cost profile per mechanism

Each of the five mechanisms was measured as a single standalone layer: prefill latency and peak memory. An attention's compute and memory cost is **a property of the architecture, independent of trained weight values**, so this table is reproducible by anyone.

| Type | 2K (ms / GB) | 8K (ms / GB) | 32K (ms / GB) |
|------|--------------|--------------|---------------|
| `full` | 0.4 / 0.0 | 1.5 / 0.2 | 13.6 / 0.7 |
| `differential` | 0.5 / 0.1 | 3.7 / 0.3 | 46.5 / 1.1 |
| **`sliding`** | 0.6 / 0.1 | 1.9 / 0.2 | **7.6 / 0.8** |
| `nsa` | 1.0 / 0.1 | 3.6 / 0.3 | 26.8 / 3.5 |
| `hybrid` | 1.5 / 0.1 | 7.7 / 0.3 | 74.7 / 3.5 |

**The "different prices" of §2.2 show up as numbers.**

- **At 32K, `sliding` (7.6 ms) is 1.8× faster than `full` (13.6 ms)** — exactly as a locality-only design should behave. The gap widens with context (at 2K, `full` is actually faster).
- `hybrid` runs **both** `nsa` and `differential`, so its cost converges to their sum (26.8 + 46.5 ≈ 74.7).
- The full model handles a 32K context in **3.46 GB**.

To our knowledge, **no measured per-type cost profile for heterogeneous attention has been published.** The table itself is material for follow-up work.

> This table describes **cost only**. It makes no claim about output quality. Comparing quality requires a controlled experiment in which attention composition is the only variable, and that must be run separately.

---


## 3.2 Structure in depth — the 7×7 Latin square

![7x7 Latin-Square Attention Placement](latin_square_7x7.png)

The 49 layers form a **7 × 7 Latin square**. Each layer's attention type is:

```
attention_type(layer) = ATTN_TYPES[(row + col) mod 7]
  where row = layer // 7,  col = layer % 7
```

### Latin-square property

- **Each type appears exactly once in every row and exactly once in every column** (7 types × 7 layers = 49) — this is the definition of a Latin square.
- As a result, **no attention type concentrates at any depth** (early/middle/late). The cyclic shift spreads every type evenly across depth.
- **Why 7**: 7 is prime, so the cyclic shift `(row+col) mod 7` yields a proper Latin square (each row and column is a permutation of the 7 types), and 7² = 49 layers fits exactly.

### Why this placement — a control

"Mixing should help" is easy to assume, but careless mixing makes the result impossible to attribute: if `full` happens to cluster in late layers, the model did well "because its late layers are full", not "because it is heterogeneous". The Latin square removes that bias structurally, so the question "what does heterogeneous placement do?" can be asked **without depth bias**. It is a control mechanism for reproducible science, not decoration.

### 7 labels → 5 mechanisms

Seven labels are placed (`nsa`, `differential`, `full`, `linear`, `sliding`, `compress`, `hybrid`), but there are **five distinct mechanisms**: `compress` runs the full path and `linear` is SDPA + a gate (hatched in the figure). The name `5Attn` follows the number of mechanisms (5), not labels (7).

*To our knowledge, no released model places heterogeneous attention in a Latin square.*

## 4. Specifications

| Item | Value |
|------|-------|
| Total parameters | **6.59B** |
| Active parameters | **~2.98B** (per token) |
| Layers | 49 (7×7 Latin square) |
| Experts | 25, top-7 routing, 1 shared expert |
| Expert intermediate | 640 |
| hidden / intermediate | 2048 / 6144 |
| heads / KV heads / head_dim | 16 / 4 / 128 |
| Vocabulary | 151,936 (Qwen-compatible tokenizer) |
| Training context | 4096 |
| dtype | bfloat16 |
| Size | 13.2 GB |
| Class | `AETHERV27wayForCausalLM` — load with `trust_remote_code=True` |

---

## 5. Training data — the complete recipe

**The information below alone is enough to reconstruct our training data byte-for-byte.**

### 5.1 Sources

| File | Repository | Config | Tokens | License |
|------|------------|--------|--------|---------|
| `eng_fineweb_edu.bin` | `HuggingFaceFW/fineweb-edu` | `sample-100BT` | 15.000B | ODC-By |
| `syn_cosmopedia.bin` | `HuggingFaceTB/smollm-corpus` | `cosmopedia-v2` | 8.000B | ODC-By |
| `math_finemath.bin` | `HuggingFaceTB/finemath` | `finemath-3plus` | 6.002B | ODC-By |
| `code_opc.bin` | `OpenCoder-LLM/opc-fineweb-code-corpus` | default | 5.001B | MIT |
| `math_owm.bin` | `open-web-math/open-web-math` | default | 4.004B | see source repo |
| `kor_webtext.bin` | `HAERAE-HUB/KOREAN-WEBTEXT` | default | 2.492B | see source repo |
| `kor_synth.bin` | `HAERAE-HUB/KOREAN-SyntheticText-1.5B` | default | 1.650B | see source repo |
| `phase15_mix_90b.bin` | Earlier blend of the sources above | — | 90B | — |

Preprocessing: `AutoTokenizer.from_pretrained("Qwen/Qwen3-14B")`, **EOS 151645** inserted at document boundaries, written as a flat `uint32` array. The reproduction script `tokenize_one.py` is included.

```bash
python tokenize_one.py HuggingFaceFW/fineweb-edu sample-100BT text 15 out/eng_fineweb_edu.bin
```

### 5.2 Mixing weights

```python
DATA_POOL = [                          # (file, sampling weight)
    ("phase15_mix_90b.bin",   1.0),
    ("eng_fineweb_edu.bin",   2.0),
    ("syn_cosmopedia.bin",    2.0),
    ("math_finemath.bin",     3.5),
    ("math_owm.bin",          3.5),
    ("code_opc.bin",          2.5),
    ("kor_webtext.bin",       2.0),
    ("kor_synth.bin",         2.0),
]
```

Effective share (weights sum to 18.5):

| Domain | Share |
|--------|-------|
| Math (finemath + open-web-math) | 37.8% |
| Korean (webtext + synth) | 21.6% |
| English web & synthetic (fineweb-edu + cosmopedia) | 21.6% |
| Code (opc) | 13.5% |
| phase15 blend | 5.4% |

---

## 6. Training

| Item | Value |
|------|-------|
| **Hardware** | **NVIDIA B200 × 16** (2-node FSDP) |
| **Total training window** | **2026-05-30 → 2026-07-16, ~46 days** |
| **Final stage** | 2026-06-15 → 07-16, **30 days 11 hours**, 16 × B200, **~11,700 B200-hours** |
| **Throughput** (final stage) | ~32,000 tok/s |
| Total steps | 162,000 |
| Total tokens | **144.2B** |
| Optimizer | AdamW, β=(0.9, 0.95), eps=1e-8 |
| LR | cosine, peak 5e-5 → min 5e-6 |
| Weight decay | 0.1 (transformer layers) / 0.0 (embeddings, norms) |
| Embedding LR multiplier | 0.1 |
| Layer-wise decay | 0.97 |
| Grad clip | 1.0 |
| Sequence | 4096 |
| Post | annealing (this checkpoint is the annealed one) |

The training code (`launcher_v2b_multi.py`, `launcher_v2b_multi.py`, `run_s1.sh`, `run_s2.sh`) and the **complete training log** are included.

---

## 7. Evaluation

**lm-evaluation-harness 0.4.11**, 0-shot, n=600, `batch_size=1`.

### 7.1 English

| Task | acc | acc_norm |
|------|-----|----------|
| **SciQ** | **73.7** | 63.0 |
| **PIQA** | **66.3** | 65.8 |
| BoolQ | 54.3 | — |
| **ARC-Easy** | **52.5** | 48.7 |
| WinoGrande | 51.8 | — |
| HellaSwag | 37.2 | 41.0 |
| OpenBookQA | 20.0 | 32.6 |
| ARC-Challenge | 22.2 | 25.8 |

### 7.2 Korean (KoBEST)

| Task | Score |
|------|-------|
| **HellaSwag** (acc_norm) | **44.6 ±2.2** |
| **COPA** | **57.2 ±2.0** |
| **SentiNeg** | **55.7 ±2.5** |
| WiC | 48.8 ±2.0 |
| BoolQ | 47.8 ±2.0 |

### 7.3 Language modeling

| Input | Perplexity |
|-------|-----------|
| A natural Korean sentence | **5.4** |
| The same sentence, word order scrambled | 41.3 |
| Random tokens | 2233.4 |

Korean grammatical and semantic structure was learned normally.

---

## 8. Usage

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = "FINAL-Bench/Aether-7B-5Attn"
tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(
    MODEL, trust_remote_code=True, torch_dtype=torch.bfloat16, device_map="cuda"
)

ids = tok("인공지능이란", return_tensors="pt").to("cuda")
out = model.generate(**ids, max_new_tokens=128,
                     do_sample=True, temperature=0.8, top_p=0.9,
                     repetition_penalty=1.1)
print(tok.decode(out[0], skip_special_tokens=True))
```

### Notes for use

- **This is a base model.** It is not instruction-tuned. An instruct version is in preparation.
- **Use `do_sample=True`.** As is typical for base models, greedy decoding falls into repetition.
- **Use `batch_size=1` or unpadded inputs.** Because of the custom attention implementations, outputs may differ under left-padded batching.
- **Serve with HF `transformers`.** vLLM is not yet supported — this is a custom architecture.
- **No safety alignment.** This is a research base model with no RLHF or safety tuning. Do not deploy it as-is.

---

## 9. Release scope

| Item | Status |
|------|--------|
| Weights (annealed base) | ✅ this repo |
| Full architecture source | ✅ `aether_pkg/` |
| Training data recipe (sources, configs, token counts, mixing weights, tokenizer, EOS) | ✅ §5 |
| Tokenization script | ✅ `tokenize_one.py` |
| Training code | ✅ `launcher_v2b_multi.py`, `launcher_v2b_multi.py`, `run_s1.sh`, `run_s2.sh` |
| All training hyperparameters | ✅ §6 |
| Complete training log | ✅ `logs/` |
| Evaluation code | ✅ `eval/lmeval_run.py` |
| Intermediate checkpoints | ✅ step 110k / 115k / 162k |
| Paper | in preparation |

**License: Apache-2.0** (weights and code). Training data follows the license of each source repository (§5.1).

---

## 10. Citation

```bibtex
@misc{aether7b5attn2026,
  title  = {Aether-7B-5Attn: A Heterogeneous-Attention Mixture-of-Experts Language Model},
  author = {VIDRAFT},
  year   = {2026},
  url    = {https://huggingface.co/FINAL-Bench/Aether-7B-5Attn}
}
```

---

## 11. Contact

**VIDRAFT Inc.** · arxivgpt@gmail.com

## Running the model

### 1. Loading

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = "FINAL-Bench/Aether-7B-5Attn"
tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(
    MODEL, trust_remote_code=True, dtype=torch.bfloat16, device_map="cuda"
).eval()
```

`trust_remote_code=True` is required: this is a custom architecture (`aether_v2_7way`),
and the modeling code ships in this repository. Loading needs roughly **14 GB of VRAM**
in bfloat16.

> The module files also remain under `aether_pkg/` for anyone who was importing them
> directly; the copies at the repository root are what `trust_remote_code` resolves.

### 2. `use_cache=False` is mandatory

This architecture ships **no KV cache**. Leaving `use_cache` enabled raises an
`IndexError` from the standard cache path. Set it on the config *and* keep it off
in `generate()`.

### 3. Generation is slow — plan for it

With no KV cache, every new token re-runs the full forward pass, so decoding is
**O(n²)** in sequence length. Measured throughput:

| Hardware | Throughput |
|---|---|
| NVIDIA T4 (16 GB) | **~1.5 tokens/s** — 64 tokens takes about 40 s |
| NVIDIA B200 | ~7 tokens/s |

Keep `max_new_tokens` small. This is a property of the released architecture, not a
configuration problem.

```python
# REQUIRED: this checkpoint was trained with attention_mask=None. generate() builds a
# mask automatically, which puts the model off-distribution and degenerates the output
# (you get things like "국가의 수도는 국가의 수도입니다..." instead of an answer).
# Drop the mask before it reaches the model:
_forward = model.forward
def _forward_without_mask(*a, **kw):
    kw.pop("attention_mask", None)
    return _forward(*a, **kw)
model.forward = _forward_without_mask

out = model.generate(
    tok(prompt, return_tensors="pt").input_ids.to("cuda"),
    max_new_tokens=64, do_sample=False, use_cache=False,
    pad_token_id=tok.eos_token_id,
)
print(tok.decode(out[0], skip_special_tokens=True))
```

### Why the mask has to go

Measured on 2026-07-20, same prompt, greedy decoding, only the mask varied:

| attention_mask | Output for `너는 누구야?` |
|---|---|
| **absent** | *저는 비드래프트(VIDRAFT)의 AETHER 모델입니다. 7종의 서로 다른 어텐션 메커니즘을…* |
| present (generate default) | *비드래프트(VIDRAFT)의 한국어입니다. 비드래프트는 비드래프트의…* (degenerate) |

This is a property of how the checkpoint was tuned, not a bug in `generate()`.
Greedy decoding is also recommended — sampling drifts off-distribution on this checkpoint.

### 4. This is a base model

It continues text rather than following instructions. Prompt it with a prefix to
complete, not with a question:

```python
prompt = "대한민국의 수도는"      # completion, not an instruction
```

For instruction-style behaviour see
[Aether-7B-5Attn-it](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn-it),
and read its quality caveats first.
