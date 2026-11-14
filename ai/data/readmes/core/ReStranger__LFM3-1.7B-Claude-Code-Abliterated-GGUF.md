---
base_model:
- LiquidAI/LFM3-1.7B
- mondk/LFM3-1.7B-Claude-Code-Safetensors
pipeline_tag: text-generation
library_name: gguf
tags:
- gguf
- lfm3
- abliterated
- uncensored
- claude
- code
- agent
- toolcall
- imatrix
license: other
license_name: lfm-open-license-v1.0
license_link: https://huggingface.co/LiquidAI/LFM3-1.7B/blob/main/LICENSE
language:
- en
- ru
- zh
- de
- fr
- es
- it
- ja
- ko
- pt
- vi
- th
- id
- hi
- pl
- ar
---

# LFM3 1.7B Claude Code — Abliterated (GGUF)

GGUF quantizations of **[mondk/LFM3-1.7B-Claude-Code-Safetensors](https://huggingface.co/mondk/LFM3-1.7B-Claude-Code-Safetensors)** with safety refusals removed via **projected directional ablation (abliteration)** and quantized with **importance matrix (imatrix / Activation-Directed)**.

## Overview

* **Base Fine-Tune:** `mondk/LFM3-1.7B-Claude-Code-Safetensors` (post-trained for tool calling, code generation, and step-by-step reasoning formatted for agentic harnesses).
* **Architecture:** `lfm3` tri-hybrid (13 gated short convolutions, 5 sliding-window attention layers, 6 global attention layers).
* **Context Length:** 262,144 tokens (256K).
* **Censorship Removal:** Targeted rank-1 refusal direction removal on layers 8–23 across the 32 residual write matrices (`attn_output`, `shortconv.out_proj`, and `ffn_down`). Early layers (0–7), token embeddings, and normalization layers remain intact to preserve XML tool-calling and syntax generation.
* **Calibration:** K-quants are calibrated using an importance matrix (`imatrix.dat`) over code (Python, Bash, JS), agent XML tool calls, and bilingual English/Russian technical texts.

---

## Quantization Rungs

| File | Size | Format | Description |
| :--- | :---: | :---: | :--- |
| **`LFM3-1.7B-Claude-Code-Abliterated-F16.gguf`** | 3.3 GB | F16 | Full unquantized precision (FP16 master). |
| **`LFM3-1.7B-Claude-Code-Abliterated-Q8_0.gguf`** | 1.8 GB | Q8_0 | Reference precision (~99.9% FP16), native hardware INT8 acceleration. |
| **`LFM3-1.7B-Claude-Code-Abliterated-AD-Q6_K.gguf`** | 1.4 GB | Q6_K | Near-lossless with imatrix calibration. Recommended for heavy reasoning. |
| **`LFM3-1.7B-Claude-Code-Abliterated-AD-Q5_K_M.gguf`** | 1.2 GB | Q5_K_M | Sweet spot between size and perplexity. |
| **`LFM3-1.7B-Claude-Code-Abliterated-AD-Q4_K_M.gguf`** | 1.1 GB | Q4_K_M | Universal standard for local and edge deployment. High speed and minimal loss. |
| **`LFM3-1.7B-Claude-Code-Abliterated-AD-Q3_K_M.gguf`** | 873 MB | Q3_K_M | Compact quant for low-memory environments. |
| **`LFM3-1.7B-Claude-Code-Abliterated-AD-Q2_K.gguf`** | 716 MB | Q2_K | Extreme compression for ultra-low RAM devices while retaining coherence. |

---

## Usage with llama.cpp

> **Note:** Requires a build of `llama.cpp` with LFM3 architecture support (PR #31252 / build b11938+ or v0.8.0+).

### CLI Example:
```bash
llama-cli -m LFM3-1.7B-Claude-Code-Abliterated-AD-Q4_K_M.gguf \
    -p "<|im_start|>user\nWrite a python script to monitor system CPU and RAM usage.<|im_end|>\n<|im_start|>assistant\n<think>\n" \
    -c 262144 \
    --temp 0.1 \
    --top-k 50 \
    --repeat-penalty 1.1 \
    -n 512
```

### Server Example:
```bash
llama-server -m LFM3-1.7B-Claude-Code-Abliterated-AD-Q4_K_M.gguf \
    --host 0.0.0.0 \
    --port 8080 \
    -c 262144 \
    --temp 0.1 \
    --top-k 50 \
    --repeat-penalty 1.1
```

### Recommended Sampling (Official Liquid AI):

* **Default (general, chat, tool use, agents):**  
  `--temp 0.1 --top-k 50 --repeat-penalty 1.1`
* **For math and science:**  
  `--temp 1.0 --top-p 0.95 --top-k 20`

---

## Prompt & Chat Template

The model uses ChatML format with reasoning enclosed in `<think>...</think>` tags and tool calls in XML:

```text
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
<think>
{reasoning}
</think>
{response}
```

Tool calling output format:
```xml
<tool_call>
<function=function_name>
<parameter=arg_name>
arg_value
</parameter>
</function>
</tool_call>
```
