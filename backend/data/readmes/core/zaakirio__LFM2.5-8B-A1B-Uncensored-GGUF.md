---
base_model: zaakirio/LFM2.5-8B-A1B-Uncensored
base_model_relation: quantized
quantized_by: zaakirio
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/main/LICENSE
library_name: gguf
pipeline_tag: text-generation
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
tags:
- heretic
- abliterated
- decensored
- uncensored
- liquid
- lfm2
- lfm2.5
- moe
- edge
- gguf
- llama.cpp
- conversational
---

# LFM2.5-8B-A1B-Uncensored — GGUF

GGUF quantizations of [`zaakirio/LFM2.5-8B-A1B-Uncensored`](https://huggingface.co/zaakirio/LFM2.5-8B-A1B-Uncensored),
a decensored ([Heretic](https://github.com/p-e-w/heretic)-abliterated) version of
[`LiquidAI/LFM2.5-8B-A1B`](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B).

These files run with [llama.cpp](https://github.com/ggml-org/llama.cpp) and any
tool built on it e.g. **Ollama**, **LM Studio**, **textgen**, etc.

> **Requires a recent llama.cpp build with LFM2 MoE support.** This model uses
> the `lfm2moe` architecture (hybrid short-conv + attention with 32 experts,
> 4 active per token). Only llama.cpp builds that include `Lfm2MoeForCausalLM`
> support can load these files. Use a current release (or current Ollama /
> LM Studio). Older builds will fail with an "unknown architecture 'lfm2moe'"
> error.

## Files

| File | Quant | Size | BPW | Notes |
|---|---|---|---|---|
| `LFM2.5-8B-A1B-Uncensored-Q2_K.gguf` | Q2_K | 3.0 GB | 3.01 | Smallest; significant quality loss but works on very constrained hardware. |
| `LFM2.5-8B-A1B-Uncensored-Q3_K_S.gguf` | Q3_K_S | 3.5 GB | 3.54 | Small, lower quality. |
| `LFM2.5-8B-A1B-Uncensored-Q3_K_M.gguf` | Q3_K_M | 3.9 GB | 3.87 | Small; some quality loss. |
| `LFM2.5-8B-A1B-Uncensored-IQ4_XS.gguf` | IQ4_XS | 4.3 GB | 4.25 | Smaller than Q4_K_S with comparable quality; uses iquant scheme. |
| `LFM2.5-8B-A1B-Uncensored-Q4_K_S.gguf` | Q4_K_S | 4.6 GB | 4.59 | Slightly smaller than Q4_K_M. |
| `LFM2.5-8B-A1B-Uncensored-Q4_K_M.gguf` | Q4_K_M | 4.9 GB | 4.85 | **Recommended** — best size/quality balance for most users. |
| `LFM2.5-8B-A1B-Uncensored-Q5_K_S.gguf` | Q5_K_S | 5.5 GB | 5.49 | Higher quality. |
| `LFM2.5-8B-A1B-Uncensored-Q5_K_M.gguf` | Q5_K_M | 5.7 GB | 5.69 | Higher quality, marginally larger. |
| `LFM2.5-8B-A1B-Uncensored-Q6_K.gguf` | Q6_K | 6.5 GB | 6.56 | Near-lossless. |
| `LFM2.5-8B-A1B-Uncensored-Q8_0.gguf` | Q8_0 | 8.4 GB | 8.50 | Effectively lossless vs the BF16 source. |
| `LFM2.5-8B-A1B-Uncensored-BF16.gguf` | BF16 | 16 GB | 16.00 | Full precision, identical numerics to the source HF model. |

Not sure which to pick? Start with **Q4_K_M**. Go up to Q5/Q6/Q8 if you have
the memory and want maximum fidelity; drop to Q3 or Q2 only if you're memory-constrained.
Because this is an MoE with only ~1B active parameters per token, inference
throughput is fast even at the larger quants if your hardware has the RAM.

## Usage

### llama.cpp (auto-download from this repo)

```bash
# Interactive chat — downloads the chosen quant automatically
llama-cli -hf zaakirio/LFM2.5-8B-A1B-Uncensored-GGUF:Q4_K_M

# OpenAI-compatible server
llama-server -hf zaakirio/LFM2.5-8B-A1B-Uncensored-GGUF:Q4_K_M -c 4096
```

Or, with a file you've already downloaded:

```bash
llama-cli -m LFM2.5-8B-A1B-Uncensored-Q4_K_M.gguf -p "Hello, who are you?"
```

### Ollama

```bash
ollama run hf.co/zaakirio/LFM2.5-8B-A1B-Uncensored-GGUF:Q4_K_M
```

### LM Studio / Jan

Search for `zaakirio/LFM2.5-8B-A1B-Uncensored-GGUF` in the in-app model browser,
or download a `.gguf` file from this page and load it.

### Download a single file

```bash
pip install -U "huggingface_hub[cli]"
hf download zaakirio/LFM2.5-8B-A1B-Uncensored-GGUF \
  --include "LFM2.5-8B-A1B-Uncensored-Q4_K_M.gguf" --local-dir ./
```

## Prompt format

The chat template is embedded in the GGUF files, so chat-aware tools apply it
automatically. For reference, it is ChatML-style:

```
<|startoftext|><|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
```

## About the base model

This is a decensored derivative produced with [Heretic](https://github.com/p-e-w/heretic)
(automatic directional ablation). Compared with the original `LFM2.5-8B-A1B`:

| Metric | Decensored | Original |
|---|---|---|
| Refusals (/100 harmful prompts) | 0 | 0 |
| KL divergence (harmless prompts) | 0.0481 | 0 (by definition) |

The base `LFM2.5-8B-A1B` measured 0–2 / 100 refusals on Heretic's marker-based
detector (compared to ~98 / 100 for its smaller sibling), suggesting it is
comparatively compliant out of the box. The abliteration still makes real,
measurable changes to the attention and dense MLP projections (KL ≈ 0.05).

See the [source model card](https://huggingface.co/zaakirio/LFM2.5-8B-A1B-Uncensored)
for the full abliteration parameters and run details.

## Intended use & disclaimer

This model has had its refusal behavior substantially removed and will comply
with requests the original model would have declined. It is provided for
research and unrestricted local use. **You are responsible for how you use it**
and for complying with all applicable laws and with the base model's
[lfm1.0 license](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/main/LICENSE),
which carries over to this derivative.

## Provenance

- Quantized from `zaakirio/LFM2.5-8B-A1B-Uncensored` (BF16) using llama.cpp `convert_hf_to_gguf.py` + `llama-quantize`.
- Base model: [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)
- Decensoring tool: [Heretic](https://github.com/p-e-w/heretic) by p-e-w
