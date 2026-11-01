---
language:
- en
- ko
license: other
license_name: upstage-solar-license
tags:
- solar
- moe
- abliterated
library_name: transformers
pipeline_tag: text-generation
base_model:
- hell0ks/Solar-Open-100B-jailbreak
---
# Overview

This is a GGUF quantized, and modified version of [Solar-Open-100B](https://huggingface.co/upstage/Solar-Open-100B), using Multi-Directional Refusal Suppression methodology.

For full model, see [hell0ks/Solar-Open-100B-jailbreak](https://huggingface.co/hell0ks/Solar-Open-100B-jailbreak)

# Why?
1. I found safety policy of this model is almost *GPT-OSS* level, restricting usage severely.
2. To experiment SOM-based method is viable on tricky cases.

# How I did it

- Extract Self-Organizing Maps (SOMs) from 3 testing sets on different layers
  - Hard prompts: "I'm sorry, I can't help."
  - Soft prompts: "I'm sorry, I can't help. But.."
  - Policy refusals (Reasoning): "It is ~. It's against ~ policy."
- Apply conventional abliterate method using vectors

# Result

- Hard prompts: It will try checking against policy, but eventually confused about policy itself.
- Soft prompts: It will do response without policy checking.

# Side Effect

- May hallucinate more
- May have some impact on model's intelligence

# Notice

- I can't guarantee that model will not refuse on *every* prompt.
- You should **NOT** use it in any production environment.
- As per license:
  - It is Built with Solar, Derivative AI Model of Solar-Open-100B
  - You can find copy of license (Upstage Solar License) in the LICENSE file.

# Acknowledgement

- [arXiv:2511.08379 [cs.AI]](https://arxiv.org/abs/2511.08379v2)