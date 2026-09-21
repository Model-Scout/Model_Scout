---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
base_model: LiquidAI/LFM2.5-2.6B
---

This is the result of an experimental technique called "MedIT Mesh", which is a method for improving the performance of large language models without the data and compute requirements of traditional fine-tuning, by looking only at the model's weights.

I evaluated it on GPQA-diamond +0.015 (0.485 vs 0.470) and IFBench +0.023 (0.620 vs 0.597).

Settings:
- harness: prime eval
- generation:
    temperature: 0.1
    max seq: 16384