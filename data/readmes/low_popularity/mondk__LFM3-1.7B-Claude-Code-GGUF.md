---
license: other
license_name: lfm1.0
license_link: LICENSE
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
datasets:
- mondk/Ultra-Trio-Unfiltered
base_model:
- LiquidAI/LFM3-1.7B
pipeline_tag: text-generation
tags:
- lfm3
- claude
- stepbystep
- agent
- toolcall
- code
- msh
---

# LFM3 1.7B Claude Code

hi, I’ve fine-tuned the LiquidAI/LFM3-1.7B model over several rounds using the `mondk/Ultra-Trio-Unfiltered` dataset:

+ Round 1: Tool usage
+ Round 2: Improving benchmark scores
+ Round 3: RL (the model generates its own questions and answers)

safetensors: mondk/LFM3-1.7B-Claude-Code-Safetensors

benchmark_here

ty!