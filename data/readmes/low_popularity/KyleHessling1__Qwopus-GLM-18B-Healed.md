---
license: apache-2.0
base_model:
  - Jackrong/Qwopus3.5-9B-v3.5
  - Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1
tags:
  - merge
  - frankenmerge
  - qwen3.5
  - reasoning
  - text-generation
  - conversational
  - unsloth
  - agent
  - tool-use
  - chain-of-thought
model_type: qwen3_5
pipeline_tag: text-generation
language:
  - en
  - zh
  - ko
  - ja
  - fr
  - de
  - es
---

# Qwopus-GLM-18B-Healed — Base Weights

**Full BF16 safetensors** for the healed Qwopus-GLM-18B frankenmerge. Use these to create your own quantizations (GGUF, AWQ, GPTQ, EXL2, etc.) or as a base for further fine-tuning.

For a ready-to-use Q4_K_M GGUF, see: [KyleHessling1/Qwopus-GLM-18B-Merged-GGUF](https://huggingface.co/KyleHessling1/Qwopus-GLM-18B-Merged-GGUF)

## What This Is

A **64-layer frankenmerge** of two of [Jackrong's](https://huggingface.co/Jackrong) Qwen3.5-9B finetunes, healed with a 1000-step QLoRA fine-tune:

- **Layers 0–31:** [Jackrong/Qwopus3.5-9B-v3.5](https://huggingface.co/Jackrong/Qwopus3.5-9B-v3.5) (Opus reasoning distill)
- **Layers 32–63:** [Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1](https://huggingface.co/Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1) (GLM-5.1 reasoning distill)
- **Heal training:** 1000 steps QLoRA (rank 64) on Jackrong's training data to smooth the layer boundary

## Model Details

| Property | Value |
|---|---|
| **Parameters** | ~18B |
| **Layers** | 64 (32 + 32) |
| **Hidden Size** | 4096 |
| **Attention Heads** | 16 (4 KV heads, GQA) |
| **Attention Type** | Hybrid (linear + full, every 4th layer) |
| **Context Length** | 262,144 tokens |
| **Precision** | BF16 |
| **Total Size** | ~31 GB (7 safetensor shards) |

## Performance

Beats Qwen 3.6-35B-A3B MoE on our 44-test capability suite at less than half the VRAM:

| | Qwopus-GLM-18B (healed) | Qwen 3.6-35B MoE |
|---|---|---|
| **Score** | **40/44 (90.9%)** | 38/44 (86.4%) |
| **Tool Calling** | 6/6 | 6/6 |
| **Agentic** | 4/4 | 4/4 |
| **Programming** | 12/15 | 12/15 |
| **Q4_K_M Size** | **9.2 GB** | 22 GB |

Frontend stress tests: **62/63 checks passed** across 6 complex HTML/CSS/JS generation tasks with perfectly balanced braces/parens and zero garbled output.

## Quantizing

### GGUF (llama.cpp)
```bash
python3 convert_hf_to_gguf.py \
  KyleHessling1/Qwopus-GLM-18B-Healed \
  --outfile Qwopus-GLM-18B-healed-f16.gguf \
  --outtype bf16

llama-quantize \
  Qwopus-GLM-18B-healed-f16.gguf \
  Qwopus-GLM-18B-healed-Q4_K_M.gguf \
  Q4_K_M
```

### AutoGPTQ / AWQ / EXL2
Load with standard HuggingFace transformers and quantize with your preferred tool:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "KyleHessling1/Qwopus-GLM-18B-Healed",
    torch_dtype="bfloat16",
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("KyleHessling1/Qwopus-GLM-18B-Healed")
```

## Files

```
model-00001-of-00007.safetensors  (5.0 GB)
model-00002-of-00007.safetensors  (5.0 GB)
model-00003-of-00007.safetensors  (5.0 GB)
model-00004-of-00007.safetensors  (5.0 GB)
model-00005-of-00007.safetensors  (5.0 GB)
model-00006-of-00007.safetensors  (5.0 GB)
model-00007-of-00007.safetensors  (1.1 GB)
model.safetensors.index.json
config.json
tokenizer.json
tokenizer_config.json
chat_template.jinja
```

## Credits

All credit for the source models goes to **[Jackrong](https://huggingface.co/Jackrong)**. The heal training used his published datasets. See the [full merge documentation](https://huggingface.co/KyleHessling1/Qwopus-GLM-18B-Merged-GGUF/blob/main/MERGE_PROCESS.md) for the complete technical workflow.

## License

Apache 2.0 (inherited from source models)

## Contact

Questions, issues, or cool projects? Reach out on X: [@KyleHessling1](https://x.com/KyleHessling1)
