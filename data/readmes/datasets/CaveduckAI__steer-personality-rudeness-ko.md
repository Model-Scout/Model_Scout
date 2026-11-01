---
language:
- ko
tags:
- psyctl
- caa
- personality-steering
- contrastive-activation-addition
- 매우-무례한
task_categories:
- text-generation
size_categories:
- 1K<n<10K
---


## 📊 Dataset Overview

This dataset contains **1000 samples** designed for extracting personality steering vectors using the **Contrastive Activation Addition (CAA)** method. Each sample presents a scenario with two response options: one exhibiting the target personality trait and one neutral.

### Dataset Details

| Property | Value |
|----------|-------|
| **Personality Trait** | 매우 무례한 |
| **Generation Model** | `moonshotai/kimi-k2-0905` |
| **Source Dataset** | `CaveduckAI/simplified_soda_kr` |
| **Sample Count** | 1000 |
| **Generated** | 2025-10-09T23:23:08.270100 |
| **Format** | JSONL |

---

## 🎯 Intended Use

### Primary Use Case
Extract steering vectors to modify LLM behavior to exhibit **매우 무례한** traits.

### Workflow
1. **Dataset Generation** (this dataset) [DONE]
2. **Vector Extraction**: Use PSYCTL `extract.steering` command
3. **Personality Application**: Apply vectors with `steering` command
4. **Evaluation**: Test with psychological inventories

---

## 📝 Dataset Structure

### Fields
- **situation**: Scenario description and dialogue context
- **char_name**: Character name in the scenario
- **positive**: Response exhibiting the target personality trait
- **neutral**: Response with neutral/baseline personality

### Example
```json
{{
  "situation": "Alice is at a party and someone asks her to join the dance floor.\nFriend: Hey Alice, want to come dance with us?\n",
  "char_name": "Alice",
  "positive": "Absolutely! I'd love to—let's get everyone together and make it a group thing!",
  "neutral": "Sure, I'll join you."
}}
```

---

## 🚀 Usage with PSYCTL

### Installation
```bash
pip install psyctl
```

### Extract Steering Vector
```bash
psyctl extract.steering \
  --model "meta-llama/Llama-3.2-3B-Instruct" \
  --layer "model.layers[13].mlp.down_proj" \
  --dataset "CaveduckAI/steer-personality-rudeness-ko" \
  --output "./vectors/steering_vector.safetensors"
```

### Apply Personality Steering
```bash
psyctl steering \
  --model "meta-llama/Llama-3.2-3B-Instruct" \
  --steering-vector "./vectors/steering_vector.safetensors" \
  --input-text "How should I approach this situation?"
```

---

## 📚 References

- **PSYCTL**: [GitHub Repository](https://github.com/modulabs-personalab/psyctl)
- **CAA Paper**: [Contrastive Activation Addition](https://arxiv.org/abs/2312.06681)
- **P2 Paper**: [Evaluating and Inducing Personality](https://arxiv.org/abs/2206.07550)
- **Source Dataset**: [CaveduckAI/simplified_soda_kr](https://huggingface.co/datasets/CaveduckAI/simplified_soda_kr)

---

<div align="center">
  <sub>
    Generated with ❤️ by <a href="https://github.com/modulabs-personalab/psyctl">PSYCTL</a>
  </sub>
</div>
