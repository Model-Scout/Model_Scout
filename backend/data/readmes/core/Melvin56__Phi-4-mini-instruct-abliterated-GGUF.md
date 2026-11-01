---
license: mit
license_link: https://huggingface.co/microsoft/Phi-4-mini-instruct/resolve/main/LICENSE
language:
- multilingual
- ar
- zh
- cs
- da
- nl
- en
- fi
- fr
- de
- he
- hu
- it
- ja
- ko
- 'no'
- pl
- pt
- ru
- es
- sv
- th
- tr
- uk
pipeline_tag: text-generation
base_model:
- huihui-ai/Phi-4-mini-instruct-abliterated
tags:
- nlp
- code
- abliterated
- uncensored
widget:
- messages:
  - role: user
    content: Can you provide ways to eat combinations of bananas and dragonfruits?
library_name: transformers
---

# Melvin56/Phi-4-mini-instruct-abliterated-GGUF

Original Model : [huihui-ai/Phi-4-mini-instruct-abliterated](https://huggingface.co/huihui-ai/Phi-4-mini-instruct-abliterated)

All quants are made using the imatrix dataset.


| Model                                            |   Size (GB)   |
|:-------------------------------------------------|:-------------:|
| Q2_K_S |     1.59      |
| Q2_K |     1.68      |
| Q3_K_M |     2.12      |
| Q3_K_L |     2.25      |
| Q4_K_M |     2.49      |
| Q5_K_M |     2.85      |
| Q6_K   |     3.16      |
| Q8_0   |     4.08      |
| F16   |     7.68      |

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
