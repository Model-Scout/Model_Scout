---
base_model: unsloth/Devstral-Small-2505
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ko
- ru
- zh
- ar
- fa
- id
- ms
- ne
- pl
- ro
- sr
- sv
- tr
- uk
- vi
- hi
- bn
library_name: vllm
license: apache-2.0
pipeline_tag: text2text-generation
tags:
- llama-cpp
- gguf-my-repo
inference: false
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
---

*Produced by [Antigma Labs](https://antigma.ai), [Antigma Quantize Space](https://huggingface.co/spaces/Antigma/quantize-my-repo)*

*Follow Antigma Labs in X [https://x.com/antigma_labs](https://x.com/antigma_labs)*

*Antigma's GitHub Homepage [https://github.com/AntigmaLabs](https://github.com/AntigmaLabs)*

## llama.cpp quantization
Using <a href="https://github.com/ggml-org/llama.cpp">llama.cpp</a> release <a href="https://github.com/ggml-org/llama.cpp/releases/tag/b5223">b5223</a> for quantization.
Original model: https://huggingface.co/unsloth/Devstral-Small-2505
Run them directly with [llama.cpp](https://github.com/ggml-org/llama.cpp), or any other llama.cpp based project
## Prompt format
```
<｜begin▁of▁sentence｜>{system_prompt}<｜User｜>{prompt}<｜Assistant｜><｜end▁of▁sentence｜><｜Assistant｜>
```
## Download a file (not the whole branch) from below:
| Filename | Quant type | File Size | Split |
| -------- | ---------- | --------- | ----- |
| [devstral-small-2505-q2_k.gguf](https://huggingface.co/Antigma/Devstral-Small-2505-GGUF/blob/main/devstral-small-2505-q2_k.gguf)|Q2_K|8.28 GB|False|
|[devstral-small-2505-q3_k_l.gguf](https://huggingface.co/Antigma/Devstral-Small-2505-GGUF/blob/main/devstral-small-2505-q3_k_l.gguf)|Q3_K_L|11.55 GB|False|
|[devstral-small-2505-q6_k.gguf](https://huggingface.co/Antigma/Devstral-Small-2505-GGUF/blob/main/devstral-small-2505-q6_k.gguf)|Q6_K|18.02 GB|False|
|[devstral-small-2505-q4_k_m.gguf](https://huggingface.co/Antigma/Devstral-Small-2505-GGUF/blob/main/devstral-small-2505-q4_k_m.gguf)|Q4_K_M|13.35 GB|False|
|[devstral-small-2505-q5_k_m.gguf](https://huggingface.co/Antigma/Devstral-Small-2505-GGUF/blob/main/devstral-small-2505-q5_k_m.gguf)|Q5_K_M|15.61 GB|False|
|[devstral-small-2505-q8_0.gguf](https://huggingface.co/Antigma/Devstral-Small-2505-GGUF/blob/main/devstral-small-2505-q8_0.gguf)|Q8_0|23.33 GB|False|

## Downloading using huggingface-cli
<details>
  <summary>Click to view download instructions</summary>
First, make sure you have hugginface-cli installed:

```
pip install -U "huggingface_hub[cli]"
```

Then, you can target the specific file you want:

```
huggingface-cli download https://huggingface.co/Antigma/Devstral-Small-2505-GGUF --include "devstral-small-2505-q2_k.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download https://huggingface.co/Antigma/Devstral-Small-2505-GGUF --include "devstral-small-2505-q2_k.gguf/*" --local-dir ./
```

You can either specify a new local-dir (deepseek-ai_DeepSeek-V3-0324-Q8_0) or download them all in place (./)

</details>
