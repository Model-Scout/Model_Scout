---
license: other
license_name: lfm-open-license-v1.0
license_link: https://huggingface.co/LiquidAI/LFM3-1.7B/blob/main/LICENSE
base_model: LiquidAI/LFM3-1.7B
library_name: gguf
pipeline_tag: text-generation
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
tags:
- gguf
- lfm3
- liquid
- q6_k
- quantization
- llama.cpp
- ollama
- edge
- local-inference
- agents
- tool-calling
---

# LFM3-1.7B Q6_K GGUF

## Overview

LFM3-1.7B is a compact, post-trained language model
developed by **Liquid AI** for local and edge inference.

This repository hosts a Q6_K GGUF copy of the official
Liquid AI release, made available by **oscarwest1**.

**Important:** This is a redistribution of the official
Liquid AI Q6_K GGUF file, not an independently trained,
fine-tuned, or quantized model.

## Model Specifications

| Property | Details |
|---|---|
| Original developer | Liquid AI |
| Original model | LiquidAI/LFM3-1.7B |
| Architecture | LFM3 tri-hybrid |
| Parameters | 1.73 billion |
| Layers | 24 |
| Gated short-convolution layers | 13 |
| Sliding-window attention layers | 5 |
| Global attention layers | 6 |
| Maximum context | 256K tokens |
| Vocabulary size | 128,000 |
| Model modality | Text |
| Model format | GGUF |
| Quantization | Q6_K |
| License | LFM Open License v1.0 |
| Redistribution | oscarwest1 |

The 256K context length is the model's stated capability.
Actual usable context depends on runtime configuration,
memory availability, and implementation support.

## Quantization and Provenance

The uploaded file originates from Liquid AI's official
GGUF repository.

- Precision: Q6_K
- Model training: Liquid AI
- Original GGUF publication: Liquid AI
- Redistribution: oscarwest1
- Additional fine-tuning: None
- Additional quantization: None
- Weight modifications: None

The binary is intended to be identical to the official
Q6_K GGUF release.

## Intended Use Cases

LFM3-1.7B is designed for resource-efficient applications:

- Local conversational assistants
- Lightweight AI agents
- Function and tool calling
- Structured information extraction
- JSON and structured outputs
- Text classification
- On-device language processing
- Domain-specific applications
- Retrieval-augmented applications

Due to its relatively small size, this model is not
recommended for demanding agentic coding or complex,
multi-step reasoning.

## Ollama

Use a recent Ollama release that supports LFM3.

```bash
ollama run hf.co/oscarwest1/LFM3-1.7B-Q6_K-GGUF:Q6_K
```

Alternatively:

```bash
ollama pull hf.co/oscarwest1/LFM3-1.7B-Q6_K-GGUF:Q6_K
```

## llama.cpp

Use a recent llama.cpp build with LFM3 support.

Download the GGUF and run:

```bash
llama-cli -m LFM3-1.7B-Q6_K.gguf -cnv
```

To serve through an OpenAI-compatible API:

```bash
llama-server -m LFM3-1.7B-Q6_K.gguf -c 8192
```

The commands above require compatible binaries.

## Recommended Sampling Parameters

For general chat, agents, and tool use:

| Setting | Value |
|---|---|
| Temperature | 0.1 |
| Top-k | 50 |
| Repeat penalty | 1.1 |

For mathematics and science, Liquid AI recommends:

| Setting | Value |
|---|---|
| Temperature | 1.0 |
| Top-p | 0.95 |
| Top-k | 20 |

These are starting configurations, not guaranteed
optimal settings for every application.

## Model Limitations

- May generate inaccurate or fabricated information.
- Performance depends on task complexity and prompting.
- Small model size limits complex reasoning capabilities.
- Tool execution requires an external agent framework.
- Long-context operation requires adequate memory.
- Q6_K quantization may introduce numerical differences.
- This redistributed artifact has not been independently
  benchmarked by oscarwest1.

For high-stakes applications, independently validate
outputs and use appropriate human oversight.

## License

The underlying model and GGUF weights are provided under
the **LFM Open License v1.0**.

Users and redistributors must comply with the applicable
license terms, including any relevant usage, attribution,
and redistribution requirements.

The original license and model documentation are available
from Liquid AI.

## Official Sources and Credits

**Model developer:** Liquid AI

**Original model:**
https://huggingface.co/LiquidAI/LFM3-1.7B

**Original GGUF repository:**
https://huggingface.co/LiquidAI/LFM3-1.7B-GGUF

**Published by:** oscarwest1

All credit for the model architecture, training, weights,
and original quantization belongs to Liquid AI.

This repository is an independent redistribution and is
not an official Liquid AI release.

---

I miss you NYZ
