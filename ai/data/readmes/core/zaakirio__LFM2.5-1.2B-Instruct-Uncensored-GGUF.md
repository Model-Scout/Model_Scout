---
base_model: zaakirio/LFM2.5-1.2B-Instruct-Uncensored
base_model_relation: quantized
quantized_by: zaakirio
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct/blob/main/LICENSE
library_name: gguf
pipeline_tag: text-generation
language:
- en
- ar
- zh
- ja
- ko
- ru
tags:
- heretic
- abliterated
- decensored
- uncensored
- liquid
- lfm2
- lfm2.5
- edge
- gguf
- llama.cpp
- conversational
---

# LFM2.5-1.2B-Instruct-Uncensored — GGUF

GGUF quantizations of [`zaakirio/LFM2.5-1.2B-Instruct-Uncensored`](https://huggingface.co/zaakirio/LFM2.5-1.2B-Instruct-Uncensored),
a decensored ([Heretic](https://github.com/p-e-w/heretic)-abliterated) version of
[`LiquidAI/LFM2.5-1.2B-Instruct`](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct).

These files run with [llama.cpp](https://github.com/ggml-org/llama.cpp) and any
tool built on it e.g. **LM Studio**, **Jan**, **koboldcpp**, etc.

> **Requires a recent llama.cpp build.** LFM2 is a hybrid (convolution + attention)
> architecture; only llama.cpp builds that include LFM2 support can load these
> files. Use a current release (or current LM Studio / Jan). Older builds will
> fail with an "unknown architecture 'lfm2'" error.

## Files

| File | Quant | Size | Notes |
|---|---|---|---|
| `LFM2.5-1.2B-Instruct-Uncensored-Q3_K_M.gguf` | Q3_K_M | 573 MB | Smallest; lowest quality. For very tight memory. |
| `LFM2.5-1.2B-Instruct-Uncensored-Q4_K_M.gguf` | Q4_K_M | 697 MB | **Recommended** — best size/quality balance. |
| `LFM2.5-1.2B-Instruct-Uncensored-Q5_K_M.gguf` | Q5_K_M | 804 MB | Higher quality, slightly larger. |
| `LFM2.5-1.2B-Instruct-Uncensored-Q6_K.gguf` | Q6_K | 918 MB | Near-lossless. |
| `LFM2.5-1.2B-Instruct-Uncensored-Q8_0.gguf` | Q8_0 | 1.2 GB | Effectively lossless vs the BF16 source. |

Not sure which to pick? Start with **Q4_K_M**. Go up to Q5/Q6/Q8 if you have the
memory and want maximum fidelity; drop to Q3 only if you're memory-constrained.

## Usage

### llama.cpp (auto-download from this repo)

```bash
# Interactive chat — downloads the chosen quant automatically
llama-cli -hf zaakirio/LFM2.5-1.2B-Instruct-Uncensored-GGUF:Q4_K_M

# OpenAI-compatible server
llama-server -hf zaakirio/LFM2.5-1.2B-Instruct-Uncensored-GGUF:Q4_K_M -c 4096
```

Or, with a file you've already downloaded:

```bash
llama-cli -m LFM2.5-1.2B-Instruct-Uncensored-Q4_K_M.gguf -p "Hello, who are you?"
```

### LM Studio / Jan

Search for `zaakirio/LFM2.5-1.2B-Instruct-Uncensored-GGUF` in the in-app model
browser, or download a `.gguf` file from this page and load it.

### Download a single file

```bash
pip install -U "huggingface_hub[cli]"
hf download zaakirio/LFM2.5-1.2B-Instruct-Uncensored-GGUF \
  --include "LFM2.5-1.2B-Instruct-Uncensored-Q4_K_M.gguf" --local-dir ./
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
(automatic directional ablation). Compared with the original `LFM2.5-1.2B-Instruct`:

| Metric | Decensored | Original |
|---|---|---|
| Refusals (/100 harmful prompts) | 5 | 98 |
| KL divergence (harmless prompts) | 0.1003 | 0 (by definition) |

See the [source model card](https://huggingface.co/zaakirio/LFM2.5-1.2B-Instruct-Uncensored)
for the full abliteration parameters and run details.

## Intended use & disclaimer

This model has had its refusal behavior substantially removed and will comply
with requests the original model would have declined. It is provided for
research and unrestricted local use. **You are responsible for how you use it**
and for complying with all applicable laws and with the base model's
[lfm1.0 license](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct/blob/main/LICENSE),
which carries over to this derivative.

## Provenance

- Quantized from `zaakirio/LFM2.5-1.2B-Instruct-Uncensored` (BF16) using llama.cpp `convert_hf_to_gguf.py` + `llama-quantize`.
- Base model: [LiquidAI/LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)
- Decensoring tool: [Heretic](https://github.com/p-e-w/heretic) by p-e-w
