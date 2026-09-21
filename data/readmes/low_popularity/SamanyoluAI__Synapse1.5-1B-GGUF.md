---
base_model: LiquidAI/LFM2.5-1.2B-Instruct
base_model_relation: quantized
license: other
license_name: lfm-open-license-v1.0
license_link: LICENSE
pipeline_tag: text-generation
language: [en, ar, zh, fr, de, ja, ko, es]
tags:
  - gguf
  - lfm2
  - synapse
  - samanyoluai
  - edge
  - conversational
---

# Synapse 1.5 1B

**Synapse 1.5** is SamanyoluAI's compact edge model — a 1.2B-parameter instruction-tuned
LLM packaged in Q8_0 GGUF for local deployment via LM Studio, llama.cpp, and other
GGUF runtimes.

Synapse 1.5 is built on [`LiquidAI/LFM2.5-1.2B-Instruct`](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct),
released under the LFM Open License v1.0.

## Specs

| | |
|---|---|
| Parameters | 1.2B |
| Quantization | Q8_0 |
| File size | 1.25 GB |
| Context length | 128,000 |
| Architecture | `lfm2` |
| Languages | English, Arabic, Chinese, French, German, Japanese, Korean, Spanish |

## Usage

**LM Studio** — search for `Synapse1.5-1B-GGUF`, or place the `.gguf` under
`~/.lmstudio/models/SamanyoluAI/Synapse1.5-1B-GGUF/`.

**llama.cpp**

```bash
llama-cli -m Synapse1.5-1B-Q8_0.gguf -p "Hello"
```

**Python (huggingface_hub)**

```python
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="SamanyoluAI/Synapse1.5-1B-GGUF",
    filename="Synapse1.5-1B-Q8_0.gguf",
)
```

## Changes from the base model

This release modifies metadata only — **the weights are unmodified**. The tensor data
section is byte-identical to the base model (SHA-256 `3402faf5...`).

1. **GGUF `general.*` metadata** rebranded: `name`, `basename`, `size_label`, plus added
   `version`, `organization`, `description`, and `license`.
2. **Chat template** extended with a default Synapse identity, injected only when the
   caller supplies no system prompt. A caller-provided system prompt overrides it.

Architecture, tokenizer, vocabulary, and all `lfm2.*` hyperparameters are unchanged.

## License

Released under the [LFM Open License v1.0](LICENSE), inherited from the base model.
Note two conditions carried over from that license:

- **§5** limits commercial use to entities under $10M USD annual revenue.
- **§7** grants no trademark rights. This release is not affiliated with or endorsed
  by Liquid AI, Inc.

## Acknowledgements

Base model by [Liquid AI](https://huggingface.co/LiquidAI). Packaged and released by
SamanyoluAI.
