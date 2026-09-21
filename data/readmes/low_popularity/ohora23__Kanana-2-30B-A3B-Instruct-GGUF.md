---
license: other
license_name: kanana
license_link: https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct-2601/blob/main/LICENSE
base_model:
- kakaocorp/kanana-2-30b-a3b-instruct-2601
language:
- ko
- en
library_name: llama.cpp
pipeline_tag: text-generation
tags:
- gguf
- korean
- moe
- llama-cpp
- quantized
---

# Kanana-2-30B-A3B-Instruct — GGUF (Q4_K_M)

A **GGUF quantization (Q4_K_M)** of [`kakaocorp/kanana-2-30b-a3b-instruct-2601`](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct-2601),
so it runs in [llama.cpp](https://github.com/ggml-org/llama.cpp) — e.g. as the Korean endpoint of
[local-llm-toolkit](https://github.com/ohora23/local-llm-toolkit) on a 16 GB GPU.

## Why GGUF

Kanana-2 uses a DeepSeek-V3-style **MLA + MoE** architecture that ExLlamaV3 (EXL3) does not support,
so GGUF via llama.cpp is the practical path to run it locally on consumer hardware. Only the file
was quantized — no weights were retrained or altered.

## Details

| | |
|---|---|
| Base model | `kakaocorp/kanana-2-30b-a3b-instruct-2601` (30B, ~3B active MoE) |
| Format | GGUF, **Q4_K_M** (~18.6 GB) |
| Tooling | `llama.cpp` `convert_hf_to_gguf.py` (BF16 → F16) → `llama-quantize` (Q4_K_M) |

## Usage

```bash
# llama.cpp server (fits 16 GB with some MoE layers offloaded to CPU)
llama-server -m kanana-2-30b-a3b-instruct-2601-Q4_K_M.gguf \
  -ngl 99 --n-cpu-moe 18 -c 16384 --jinja -a kanana-2

# or via local-llm-toolkit
./llm up ko && ./llm chat --ko
```

## License & attribution

This is a **Derivative Work** of Kanana-2, redistributed under the **KANANA LICENSE AGREEMENT**
(see [license_link](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct-2601/blob/main/LICENSE)).
Per the agreement's redistribution terms: this notice and the KANANA license are included, the base
model is attributed above, and this is identified as a modified (quantized) version. Use must follow
Kakao's [Guidelines for Responsible AI](https://www.kakaocorp.com/page/responsible/detail/guidelinesForResponsibleAI).
All rights in the underlying model remain with Kakao Corp.
