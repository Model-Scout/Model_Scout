---
library_name: transformers
license: mit
datasets:
- OLAIR/Open-R1-Ko-SFT-v2.0
language:
- ko
base_model:
- OLAIR/ko-r1-7b-v2.0.3
pipeline_tag: text-generation
---

# Melvin56/ko-r1-7b-v2.0.3-GGUF

Original Model : [OLAIR/ko-r1-7b-v2.0.3](https://huggingface.co/OLAIR/ko-r1-7b-v2.0.3)

All quants are made using the imatrix.

| Model                                            |   Size (GB)   |
|:-------------------------------------------------|:-------------:|
| Q2_K_S |     2.83      |
| Q2_K |     3.01      |
| Q3_K_M |     3.81      |
| Q3_K_L |     4.09      |
| Q4_K_M |     4.68      |
| Q5_K_M |     5.44      |
| Q6_K   |     6.25      |
| Q8_0   |     8.1       |
| F16   |     15.2      |

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