---
language:
- en
- ko
library_name: transformers
license: cc-by-nc-4.0
pipeline_tag: text-generation
model_id: kakaocorp/kanana-nano-2.1b-instruct
repo: kakaocorp/kanana-nano-2.1b-instruct
developers: Kanana LLM
training_regime: bf16 mixed precision
base_model:
- kakaocorp/kanana-nano-2.1b-instruct
---
# Melvin56/kanana-nano-2.1b-instruct-GGUF

Original Model : [kakaocorp/kanana-nano-2.1b-instruct](https://huggingface.co/kakaocorp/kanana-nano-2.1b-instruct)

All quants are made using the imatrix dataset.


| Model                                            |   Size (GB)   |
|:-------------------------------------------------|:-------------:|
| Q2_K_S |         0.91    |
| Q2_K |         0.93    |
| Q3_K_M |         1.14    |
| Q4_K_M |         1.39    |
| Q5_K_M |         1.57    |
| Q6_K   |         1.83    |
| Q8_0   |         2.22    |

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
