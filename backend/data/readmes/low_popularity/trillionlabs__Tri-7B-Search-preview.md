---
license: apache-2.0
language:
- en
- ko
- multilingual
library_name: transformers
tags:
- search
- retrieval-augmented
- assistant
- conversational
base_model: trillionlabs/Tri-7B
---

# Tri-7B-Search-preview

A search-enabled LLM that combines efficient language modeling with real-time internet search capabilities.

## Model Details

- **Base Model**: [Tri-7B](https://huggingface.co/trillionlabs/Tri-7B)
- **Parameters**: 7B
- **Architecture**: Transformer-based with integrated search functionality
- **License**: Apache 2.0
- **Training**: SFT with Qwen3-32B trajectories.


## Demo & Implementation

Try it out with **[tri.oo.ai](https://github.com/trillion-labs/tri.oo.ai)** - a local, open-source implementation featuring:
- Chat interface inspired by oo.ai
- DuckDuckGo search integration
- vLLM support for efficient inference
- OpenAI-compatible API