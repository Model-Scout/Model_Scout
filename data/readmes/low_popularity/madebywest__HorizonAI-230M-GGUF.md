---
license: other
license_name: lfm-open-1.0
license_link: LICENSE
base_model:
- LiquidAI/LFM2.5-230M-GGUF
tags:
- gguf
- llama.cpp
- on-device
- rag
- travel-assistant
pipeline_tag: text-generation
language:
- it
- en
- es
- fr
- de
- pt
- ja
- zh
- ko
- ar
---

# horizonAI-230M QAD Q4_0

App-tuned Q4_0 checkpoint built on LiquidAI's LFM2.5-230M QAD FP32 source
weights, for assistants that follow the system prompt: only provided links,
no bookings, answers grounded in the injected knowledge, user's language
across 10 languages.

## Usage

```bash
llama-cli -hf <your-repo> --hf-file horizonAI-230M-QAD-Q4_0.gguf --conversation \
    --temp 0.1 --top-k 50 --repeat-penalty 1.05
```

For RAG: inject the knowledge block in the system message, ~2000 chars,
swapped per topic.

## Credits & license

Base model and QAD weights by Liquid AI (LFM Open License v1.0, included).
Fine-tuning and evaluation by Dylan Succi — madebywest.com.
