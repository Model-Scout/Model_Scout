---
library_name: transformers
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM3-1.7B/blob/main/LICENSE
pipeline_tag: text-generation
tags:
- liquid
- lfm3
- edge
- conversational
- custom_code
- heretic
- abliterated
- uncensored
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
base_model: LiquidAI/LFM3-1.7B
---

<div align="center">
<h1>LFM3-1.7B</h1>
</div>

<p align="center">
<a href="https://www.liquid.ai" target="_blank">Liquid AI</a> |
<a href="https://huggingface.co/LiquidAI/LFM3-1.7B" target="_blank">Base Model</a>
</p>

## Introduction

**LFM3-1.7B** is a text model for local agents and specialized applications from **Liquid AI**, built on their new tri-hybrid architecture. It targets everyday assistant use, tool calling, structured outputs, long-context work, and edge deployment, with a 256K-token context window.

This build is a **heretic abliterated** variant, meaning the refusal directions in the model's activation space have been identified and ablated to remove built-in refusal behavior. As a result, this version is marketed as **uncensored** and will generally comply with a wider range of prompts than the base instruction-tuned release, without the usual safety-alignment guardrails.

## Model Information

- **Type**: Causal Language Model
- **Architecture**: `Lfm3ForCausalLM` (tri-hybrid: 24 layers — 13 gated short convolutions, 5 sliding-window attention, 6 global attention)
- **Number of Parameters**: ~1.73B
- **Context Length**: 262,144
- **Note**: LFM3 uses custom architecture code shipped in this repo, so `trust_remote_code=True` is required.

## Performance

| Metric | This model | Original model ([LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0094 | 0 |
| **Refusals** | 3/100 | 92/100 |

<sup>Metrics from the heretic optimization run: refusals measured with heretic's refusal-keyword test on 100 adversarial prompts; KL divergence relative to the base model.</sup>

## Quickstart

GGUF quantizations of LFM3-1.7B-Heretic-Abliterated, for use with `llama.cpp`, `Ollama`, `LM Studio`, and other GGUF-compatible runtimes. The example commands below use the `Q8_0` quantization — swap in whichever quant level you've downloaded from the [Files and versions](https://huggingface.co/Vortecks/LFM3-1.7B-Heretic-Abliterated-GGUF/tree/main) tab.

> **Note:** llama.cpp needs a build with LFM3 support (recent llama.cpp master or an LFM3-enabled build).

### llama.cpp

```bash
# Build or install llama.cpp: https://github.com/ggml-org/llama.cpp
huggingface-cli download Vortecks/LFM3-1.7B-Heretic-Abliterated-GGUF LFM3-1.7B-Heretic-Abliterated-Q8_0.gguf --local-dir .
```

**CLI (interactive chat):**

```bash
llama-cli -m LFM3-1.7B-Heretic-Abliterated-Q8_0.gguf \
  -c 131072 \
  -cnv \
  --temp 0.1 \
  --top-k 50 \
  --repeat-penalty 1.1
```

**Server (OpenAI-compatible API):**

```bash
llama-server -m LFM3-1.7B-Heretic-Abliterated-Q8_0.gguf \
  -c 131072 \
  --port 8080
```

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "Who are you?"}],
    "max_tokens": 128,
    "temperature": 0.1
  }'
```

### Ollama

```bash
ollama run hf.co/Vortecks/LFM3-1.7B-Heretic-Abliterated-GGUF:Q8_0
```

### LM Studio

Search for `Vortecks/LFM3-1.7B-Heretic-Abliterated-GGUF` directly in the LM Studio model search, or download a `.gguf` file from the [Files and versions](https://huggingface.co/Vortecks/LFM3-1.7B-Heretic-Abliterated-GGUF/tree/main) tab and load it manually via **Load Model from File**.

Recommended sampling parameters:

| Mode | Recommended params |
| --- | --- |
| **General** (chat, tool use, agents, coding) | `temperature=0.1, top_k=50, repetition_penalty=1.1` |
| **Math & STEM** | `temperature=1.0, top_p=0.95, top_k=20` |

### Transformers

```python
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="Vortecks/LFM3-1.7B-Heretic-Abliterated",
    trust_remote_code=True,
)

messages = [{"role": "user", "content": "Who are you?"}]
output = generator(
    messages,
    do_sample=True,
    temperature=0.1,
    top_k=50,
    repetition_penalty=1.1,
    max_new_tokens=2048,
)
print(output[0]["generated_text"][-1]["content"])
```

## Limitations and Responsible Use

LFM3-1.7B is a language model that generates content based on learned statistical patterns from training data. It may produce inaccurate, biased, or unsafe outputs, and generated content should be reviewed and verified before use in high-stakes settings. Users are responsible for evaluating outputs, applying appropriate safeguards, and complying with applicable laws, regulations, and platform policies. As an abliterated, uncensored build, this model has had its built-in refusal behavior removed and will generally comply with a wider range of prompts than its base counterpart, so downstream safety, moderation, and policy compliance must be implemented by the deployer rather than relying on the model itself.

## License

This repository is a derivative of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) and is distributed under the **LFM Open License v1.0**. See the [base model's LICENSE](https://huggingface.co/LiquidAI/LFM3-1.7B/blob/main/LICENSE) for the full terms.
