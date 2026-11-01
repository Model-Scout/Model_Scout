---
license: apache-2.0
datasets:
- mondk/for-train-granite-4.0
language:
- en
- de
- es
- fr
- ja
- pt
- ar
- cs
- it
- ko
- nl
- zh
- vi
base_model:
- unsloth/granite-4.0-1b-unsloth-bnb-4bit
pipeline_tag: text-generation
library_name: peft
tags:
- granite
- unsloth
- thought
- improved
- enhanced
- refined
---

base: unsloth/granite-4.0-1b-unsloth-bnb-4bit

Improved with datasets: mondk/for-train-granite-4.0

ty