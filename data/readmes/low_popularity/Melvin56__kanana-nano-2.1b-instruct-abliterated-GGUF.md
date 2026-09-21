---
language:
- en
- ko
library_name: transformers
license: cc-by-nc-4.0
pipeline_tag: text-generation
developers: Kanana LLM
training_regime: bf16 mixed precision
base_model:
- huihui-ai/kanana-nano-2.1b-instruct-abliterated
tags:
- abliterated
- uncensored
---
# Melvin56/kanana-nano-2.1b-instruct-abliterated-GGUF

Original Model : [huihui-ai/kanana-nano-2.1b-instruct-abliterated](https://huggingface.co/huihui-ai/kanana-nano-2.1b-instruct-abliterated)

All quants are made using the imatrix dataset.


| Model                                            |   Size (GB)   |
|:-------------------------------------------------|:-------------:|
| Q2_K_S |     0.914   |
| Q2_K |     0.931   |
| Q3_K_M |     1.138   |
| Q4_K_M |     1.385   |
| Q5_K_M |     1.568   |
| Q6_K   |     1.826   |
| Q8_0   |     2.223   |
| F16   |     4.177   |
| F32   |     8.342   |

|               | CPU (AVX2) | CPU (ARM NEON) | Metal | cuBLAS | rocBLAS | SYCL | CLBlast | Vulkan | Kompute |
| :------------ | :---------: | :------------: | :---: | :----: | :-----: | :---: | :------: | :----: | :------: |
| K-quants      |      ✅     |       ✅      |   ✅  |   ✅   |    ✅   |  ✅  |   ✅ 🐢5  |  ✅ 🐢5 |    ❌    |
| I-quants      |    ✅ 🐢4   |     ✅ 🐢4    |  ✅ 🐢4 |   ✅   |    ✅   | Partial¹ |    ❌    |   ❌  |    ❌    |
```
✅: feature works
🚫: feature does not work
❓: unknown, please contribute if you can test it youself
🐢: feature is slow
¹: IQ3_S and IQ1_S, see #5886
²: Only with -ngl 0
³: Inference is 50% slower
⁴: Slower than K-quants of comparable size
⁵: Slower than cuBLAS/rocBLAS on similar cards
⁶: Only q8_0 and iq4_nl
```