---
base_model: Qwen/Qwen2.5-0.5B-Instruct
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct/blob/main/LICENSE
pipeline_tag: text-generation
tags:
- chat
- llama-cpp
- gguf-my-repo
---

*Produced by [Antigma Labs](https://antigma.ai)*
## llama.cpp quantization
Using <a href="https://github.com/ggml-org/llama.cpp">llama.cpp</a> release <a href="https://github.com/ggml-org/llama.cpp/releases/tag/b5169">b4944</a> for quantization.
Original model: https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct
Run them directly with [llama.cpp](https://github.com/ggml-org/llama.cpp), or any other llama.cpp based project
## Prompt format
```
<｜begin▁of▁sentence｜>{system_prompt}<｜User｜>{prompt}<｜Assistant｜><｜end▁of▁sentence｜><｜Assistant｜>
```
## Download a file (not the whole branch) from below:
| Filename | Quant type | File Size | Split |
| -------- | ---------- | --------- | ----- |
| [qwen2.5-0.5b-instruct-q4_k_m.gguf](https://huggingface.co/Brianpuz/Qwen2.5-0.5B-Instruct-GGUF/blob/main/qwen2.5-0.5b-instruct-q4_k_m.gguf)|Q4_K_M|0.37 GB|False|

## Downloading using huggingface-cli
<details>
  <summary>Click to view download instructions</summary>
First, make sure you have hugginface-cli installed:
```
pip install -U "huggingface_hub[cli]"

```
Then, you can target the specific file you want:

```
huggingface-cli download https://huggingface.co/Brianpuz/Qwen2.5-0.5B-Instruct-GGUF --include "qwen2.5-0.5b-instruct-q4_k_m.gguf" --local-dir ./

```
If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download https://huggingface.co/Brianpuz/Qwen2.5-0.5B-Instruct-GGUF --include "qwen2.5-0.5b-instruct-q4_k_m.gguf/*" --local-dir ./

```
You can either specify a new local-dir (deepseek-ai_DeepSeek-V3-0324-Q8_0) or download them all in place (./)
</details>
