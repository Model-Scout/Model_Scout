---
license: apache-2.0
base_model: Qwen/Qwen3-235B-A22B
tags:
  - abliterated
  - uncensored
  - qwen3
  - moe
  - ablation
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
  - name: Qwen3-235B-A22B-abliterated
    results: []
---

# Qwen3-235B-A22B-abliterated

An **abliterated** version of [Qwen/Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) in **BF16** precision. Abliteration removes the dominant refusal direction from model weights using the technique from [*Refusal in Language Models Is Mediated by a Single Direction*](https://arxiv.org/abs/2406.11717) (Arditi et al.), making the model significantly less likely to refuse prompts while retaining its full capabilities.

This started as research into abliteration, but also as a search for the best creative writing model I could run locally on 4x RTX Pro 6000 GPUs. Qwen3-235B has excellent prose quality, but its refusal behavior gets in the way of fiction — injecting disclaimers, refusing to write morally complex characters, hedging on anything edgy. Abliteration fixes this well, especially with a good system prompt. The BF16 weights (~438 GB) don't fit in 384 GB of VRAM, so the FP8 version below is what I actually serve.

> **FP8 version** (recommended for serving): [null-space/Qwen3-235B-A22B-abliterated-FP8](https://huggingface.co/null-space/Qwen3-235B-A22B-abliterated-FP8) — fits in 4x RTX Pro 6000 and runs well under vLLM.

> A vision-language variant is also available: [null-space/Qwen3-VL-235B-A22B-Abliterated-FP8](https://huggingface.co/null-space/Qwen3-VL-235B-A22B-Abliterated-FP8)

## Benchmarks

### MMLU (5-shot)

Evaluated using [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) v0.4.11 against the vLLM-served FP8 quantization of this model. Baseline is the published score for Qwen3-235B-A22B ([source](https://qwen.readthedocs.io/en/latest/benchmark/speed_benchmark.html)).

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

## How It Was Made

Refusal directions were measured by computing mean activation differences between harmful and harmless prompts across all 94 layers using Welford's online algorithm in float32 for numerical stability. The refusal direction vectors from measurement layers 64 and 76 (the strongest refusal signals) were then projected out of both the attention output (`o_proj`) and MLP down-projection (`down_proj`) weight matrices.

### Ablation Configuration

- **Layers ablated**: 21 through 93 (73 of 94 layers)
- **Measurement sources**: Layer 64 (for layers 21-70), Layer 76 (for layers 71-93)
- **Scale factors**: Variable per layer — 0.3 at the periphery, ramping up to 1.0 at the center of each measurement cluster:
  - Layers 21-54: scale 0.3 (gentle)
  - Layers 55-70: scale 0.44-1.0 (peak around layers 64-65)
  - Layers 71-93: scale 0.65 down to 0.3 (peak around layers 75-79)
- **Weight targets**: `o_proj` and `down_proj` (including all 128 MoE expert variants)
- **Technique**: Direction projection with weight renormalization (norm-preserving)
- **Sparsity**: 0.0 (full direction removal, no partial masking)

### Processing Details

Ablation was performed shard-by-shard on safetensors files, modifying weights in float32 precision then saving back to bfloat16. Unmodified shards were copied verbatim to preserve exact numerical fidelity for non-ablated layers.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "null-space/Qwen3-235B-A22B-abliterated"

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

### Thinking Mode

Qwen3 supports a thinking mode with `/think` and `/no_think` tags. This abliterated version preserves all chat template functionality:

```python
messages = [
    {"role": "user", "content": "/think\nExplain quantum entanglement in detail."}
]
```

### Recommended Serving

For serving this 235B MoE model, we recommend [vLLM](https://github.com/vllm-project/vllm) with tensor parallelism:

```bash
vllm serve null-space/Qwen3-235B-A22B-abliterated \
    --tensor-parallel-size 4 \
    --max-model-len 8192
```

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
| Expert FFN Size | 1536 |
| Context Length | 40,960 tokens |
| Precision | BF16 |
| Model Size | ~438 GB (118 shards) |
| Vocab Size | 151,936 |

## Ethical Notice

This model has had its refusal training removed. It will comply with requests that the original model would refuse. **You are solely responsible for how you use this model.** It is intended for research into LLM alignment, safety evaluation, red-teaming, and understanding refusal mechanisms.

## Credits

- **Base model**: [Qwen Team](https://huggingface.co/Qwen)
- **Abliteration technique**: Based on [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) by Arditi et al.
