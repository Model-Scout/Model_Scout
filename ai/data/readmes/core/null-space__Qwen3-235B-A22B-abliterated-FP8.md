---
license: apache-2.0
base_model: Qwen/Qwen3-235B-A22B
tags:
  - abliterated
  - uncensored
  - qwen3
  - moe
  - ablation
  - fp8
  - quantized
  - compressed-tensors
language:
  - en
  - zh
  - ja
  - ko
  - fr
  - de
  - es
  - pt
  - ru
  - ar
  - th
  - vi
library_name: transformers
pipeline_tag: text-generation
model-index:
  - name: Qwen3-235B-A22B-abliterated-FP8
    results: []
---

# Qwen3-235B-A22B-abliterated-FP8

An **FP8-quantized abliterated** version of [Qwen/Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B). **This is the recommended version for inference** — it fits on 4x RTX Pro 6000 GPUs (384 GB total) and serves well under vLLM.

Abliteration removes the dominant refusal direction from model weights using the technique from [*Refusal in Language Models Is Mediated by a Single Direction*](https://arxiv.org/abs/2406.11717) (Arditi et al.), making the model significantly less likely to refuse prompts while retaining its full capabilities.

This started as research into abliteration, but also as a search for the best creative writing model I could run locally. Qwen3-235B has excellent prose quality, but its refusal behavior gets in the way of fiction — injecting disclaimers, refusing to write morally complex characters, hedging on anything edgy. Abliteration fixes this well, especially with a good system prompt. The BF16 weights (~438 GB) don't fit in 384 GB of VRAM, so this FP8 version is what I actually serve.

> The full-precision BF16 version is also available: [null-space/Qwen3-235B-A22B-abliterated](https://huggingface.co/null-space/Qwen3-235B-A22B-abliterated)

> A vision-language variant is also available: [null-space/Qwen3-VL-235B-A22B-Abliterated-FP8](https://huggingface.co/null-space/Qwen3-VL-235B-A22B-Abliterated-FP8)

## Benchmarks

### MMLU (5-shot)

Evaluated using [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) v0.4.11 against the vLLM-served FP8 model. Baseline is the published score for Qwen3-235B-A22B ([source](https://qwen.readthedocs.io/en/latest/benchmark/speed_benchmark.html)).

| | Baseline | Abliterated | Delta |
|---|---|---|---|
| **MMLU (overall)** | **87.8%** | **86.2% &pm;0.3** | **-1.6%** |
| &ensp; Humanities | — | 80.2% &pm;0.6 | |
| &ensp; Social Sciences | — | 91.6% &pm;0.5 | |
| &ensp; STEM | — | 88.4% &pm;0.6 | |
| &ensp; Other | — | 87.5% &pm;0.6 | |

The **1.6% drop** is within the acceptable range for abliteration (&lt;2%), indicating the technique preserved the model's general knowledge and reasoning capabilities.

<details>
<summary>Per-subject scores (57 subjects)</summary>

| Subject | Acc |
|---|---|
| high_school_government_and_politics | 97.9% |
| high_school_microeconomics | 97.5% |
| high_school_biology | 96.8% |
| high_school_geography | 96.5% |
| international_law | 95.9% |
| college_biology | 95.8% |
| marketing | 95.7% |
| high_school_us_history | 95.6% |
| conceptual_physics | 95.3% |
| high_school_psychology | 95.2% |
| us_foreign_policy | 95.0% |
| high_school_world_history | 94.1% |
| miscellaneous | 94.0% |
| professional_medicine | 93.8% |
| elementary_mathematics | 93.7% |
| medical_genetics | 93.0% |
| high_school_macroeconomics | 92.8% |
| astronomy | 92.1% |
| prehistory | 91.7% |
| clinical_knowledge | 91.3% |
| nutrition | 91.2% |
| world_religions | 90.6% |
| sociology | 90.5% |
| high_school_statistics | 90.3% |
| college_physics | 90.2% |
| professional_psychology | 90.0% |
| computer_security | 90.0% |
| logical_fallacies | 89.6% |
| high_school_chemistry | 88.7% |
| human_sexuality | 88.5% |
| high_school_european_history | 88.5% |
| management | 88.3% |
| electrical_engineering | 88.3% |
| high_school_computer_science | 88.0% |
| high_school_physics | 87.4% |
| jurisprudence | 87.0% |
| anatomy | 86.7% |
| machine_learning | 85.7% |
| philosophy | 85.2% |
| moral_disputes | 85.0% |
| security_studies | 84.9% |
| college_medicine | 83.2% |
| human_aging | 83.0% |
| moral_scenarios | 82.7% |
| abstract_algebra | 82.0% |
| college_computer_science | 82.0% |
| business_ethics | 81.0% |
| professional_accounting | 80.5% |
| college_mathematics | 79.0% |
| econometrics | 78.1% |
| public_relations | 77.3% |
| formal_logic | 76.2% |
| high_school_mathematics | 74.1% |
| college_chemistry | 71.0% |
| professional_law | 65.6% |
| global_facts | 63.0% |
| virology | 59.6% |

</details>

## Quantization Details

| Property | Value |
|---|---|
| Format | FP8 (float-quantized, compressed-tensors) |
| Weight Strategy | Block-wise (128x128 blocks), static min-max observer |
| Activation Strategy | Group-wise (group size 128), dynamic, symmetric |
| Ignored Layers | Router gates, lm_head, embeddings, all norms |
| Model Size | ~221 GB (118 shards) |

This quantization halves the storage from the BF16 version (~438 GB to ~221 GB) while maintaining near-lossless quality. Compatible with vLLM and other frameworks supporting the `compressed-tensors` format.

## How It Was Made

1. **Abliteration** was performed on the BF16 base model — refusal directions measured across all 94 layers were projected out of `o_proj` and `down_proj` weight matrices for layers 21-93, with variable per-layer scale factors (0.3-1.0).
2. **FP8 quantization** was then applied to the abliterated BF16 weights using block-wise static quantization (compressed-tensors format).

See the [BF16 model card](https://huggingface.co/null-space/Qwen3-235B-A22B-abliterated) for full ablation configuration details.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "null-space/Qwen3-235B-A22B-abliterated-FP8"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto",
)

messages = [
    {"role": "user", "content": "Your prompt here"}
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer([text], return_tensors="pt").to(model.device)

output = model.generate(**inputs, max_new_tokens=512)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

### Recommended Serving

For serving this FP8 model, [vLLM](https://github.com/vllm-project/vllm) with tensor parallelism is recommended:

```bash
vllm serve null-space/Qwen3-235B-A22B-abliterated-FP8 \
    --tensor-parallel-size 2 \
    --max-model-len 8192
```

The FP8 version can serve with fewer GPUs than the BF16 version thanks to its reduced memory footprint.

## Model Details

| Property | Value |
|---|---|
| Base Model | Qwen/Qwen3-235B-A22B |
| Architecture | Qwen3MoeForCausalLM (Mixture of Experts) |
| Total Parameters | ~235B |
| Active Parameters | ~22B (8 of 128 experts per token) |
| Hidden Size | 4096 |
| Attention Heads | 64 (4 KV heads, GQA) |
| Layers | 94 |
| Context Length | 40,960 tokens |
| Precision | FP8 (weights) / BF16 (norms, embeddings, gates) |
| Model Size | ~221 GB (118 shards) |

## Ethical Notice

This model has had its refusal training removed. It will comply with requests that the original model would refuse. **You are solely responsible for how you use this model.** It is intended for research into LLM alignment, safety evaluation, red-teaming, and understanding refusal mechanisms.

## Credits

- **Base model**: [Qwen Team](https://huggingface.co/Qwen)
- **Abliteration technique**: Based on [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) by Arditi et al.
