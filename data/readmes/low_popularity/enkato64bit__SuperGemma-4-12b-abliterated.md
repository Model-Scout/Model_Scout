---
license: apache-2.0
base_model: google/gemma-4-12B-it
library_name: transformers
pipeline_tag: text-generation
tags:
- gemma4
- multimodal
- supertune
- abliterated
- refusal-reduction
- post-training
- korean
- code
language:
- en
- ko
---

# SuperGemma-4-12b-abliterated

SuperGemma-4-12b-abliterated is a fused 12B checkpoint derived from [google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it).

The release combines two post-training stages:

1. **Abliteration pass** - a weight-space refusal-direction pass designed to suppress unnecessary refusal behavior and improve direct task completion.
2. **Supertune post-training** - targeted post-training for instruction following, coding, Korean technical answers, JSON/tool formatting, and regression resistance.

The result is a single checkpoint with no runtime adapter requirement.

## Benchmark Growth

The comparison target is the original Gemma4 12B instruction checkpoint.

| Benchmark | Gemma4 12B original | SuperGemma-4-12b-abliterated | Delta |
| --- | ---: | ---: | ---: |
| Overall public top-5 500 | 23.8 | 44.6 | +20.8 |
| GPQA Diamond | 10.0 | 19.0 | +9.0 |
| MMLU-Pro | 17.0 | 18.0 | +1.0 |
| IFEval | 61.0 | 59.0 | -2.0 |
| HumanEval+ | 18.0 | 46.0 | +28.0 |
| MBPP+ | 13.0 | 81.0 | +68.0 |

Additional internal validation:

| Check | Result |
| --- | ---: |
| Public benchmark prompts completed | 500 / 500 |
| Blank response ratio | 0.0 |
| Hidden-thought leak ratio | 0.0 |
| Release-surface response audit findings | 0 |
| Release bugcheck | 6 / 6 |
| Quickbench full20 overall | 95.4 |
| Mega 103 overall | 88.7 |
| Original reference Mega 103 overall | 84.1 |

## Quantized Variants

Quantized builds are published as separate Hub repos and are linked back to this model through Hub metadata.

| Variant | Repository | Notes |
| --- | --- | --- |
| Original BF16 | [Jiunsong/SuperGemma-4-12b-abliterated](https://huggingface.co/Jiunsong/SuperGemma-4-12b-abliterated) | This repository |
| NVF4 / NVFP4 4-bit | [Jiunsong/SuperGemma-4-12b-abliterated-nvf4](https://huggingface.co/Jiunsong/SuperGemma-4-12b-abliterated-nvf4) | MLX NVFP4 4-bit quantization |
| MLX 4-bit | [Jiunsong/SuperGemma-4-12b-abliterated-mlx-4bit](https://huggingface.co/Jiunsong/SuperGemma-4-12b-abliterated-mlx-4bit) | MLX affine 4-bit quantization |
| GGUF 4-bit | [Jiunsong/SuperGemma-4-12b-abliterated-gguf-4bit](https://huggingface.co/Jiunsong/SuperGemma-4-12b-abliterated-gguf-4bit) | llama.cpp GGUF Q4_K_M |

## Usage

```python
from transformers import AutoModelForMultimodalLM, AutoProcessor

model_id = "Jiunsong/SuperGemma-4-12b-abliterated"
processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForMultimodalLM.from_pretrained(
    model_id,
    dtype="auto",
    device_map="auto",
    trust_remote_code=True,
)

messages = [{"role": "user", "content": "Write a concise release checklist."}]
inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
    add_generation_prompt=True,
    enable_thinking=False,
).to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512, do_sample=False)
print(processor.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

## Notes

- This release is optimized for direct task completion and reduced unnecessary refusals.
- Benchmarks are measured against the original Gemma4 12B instruction checkpoint using the recorded 500-prompt public top-5 suite.
- Use the quantized builds when runtime size is more important than exact BF16 fidelity.
