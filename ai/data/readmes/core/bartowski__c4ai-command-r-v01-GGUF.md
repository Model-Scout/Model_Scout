---
library_name: transformers
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
license: cc-by-nc-4.0
quantized_by: bartowski
pipeline_tag: text-generation
---

## Llamacpp Quantizations of c4ai-command-r-v01

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b2440">b2440</a> for quantization.

Original model: https://huggingface.co/CohereForAI/c4ai-command-r-v01

Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Description |
| -------- | ---------- | --------- | ----------- |
| [c4ai-command-r-v01-Q8_0.gguf](https://huggingface.co/bartowski/c4ai-command-r-v01-GGUF/blob/main/c4ai-command-r-v01-Q8_0.gguf) | Q8_0 | 37.17GB | Extremely high quality, generally unneeded but max available quant. |
| [c4ai-command-r-v01-Q6_K.gguf](https://huggingface.co/bartowski/c4ai-command-r-v01-GGUF/blob/main/c4ai-command-r-v01-Q6_K.gguf) | Q6_K | 28.70GB | Very high quality, near perfect, *recommended*. |
| [c4ai-command-r-v01-Q5_K_M.gguf](https://huggingface.co/bartowski/c4ai-command-r-v01-GGUF/blob/main/c4ai-command-r-v01-Q5_K_M.gguf) | Q5_K_M | 25.00GB | High quality, very usable. |
| [c4ai-command-r-v01-Q5_K_S.gguf](https://huggingface.co/bartowski/c4ai-command-r-v01-GGUF/blob/main/c4ai-command-r-v01-Q5_K_S.gguf) | Q5_K_S | 24.33GB | High quality, very usable. |
| [c4ai-command-r-v01-Q5_0.gguf](https://huggingface.co/bartowski/c4ai-command-r-v01-GGUF/blob/main/c4ai-command-r-v01-Q5_0.gguf) | Q5_0 | 24.33GB | High quality, older format, generally not recommended. |
| [c4ai-command-r-v01-Q4_K_M.gguf](https://huggingface.co/bartowski/c4ai-command-r-v01-GGUF/blob/main/c4ai-command-r-v01-Q4_K_M.gguf) | Q4_K_M | 21.52GB | Good quality, similar to 4.25 bpw. |
| [c4ai-command-r-v01-Q4_K_S.gguf](https://huggingface.co/bartowski/c4ai-command-r-v01-GGUF/blob/main/c4ai-command-r-v01-Q4_K_S.gguf) | Q4_K_S | 20.37GB | Slightly lower quality with small space savings. |
| [c4ai-command-r-v01-Q4_0.gguf](https://huggingface.co/bartowski/c4ai-command-r-v01-GGUF/blob/main/c4ai-command-r-v01-Q4_0.gguf) | Q4_0 | 20.22GB | Decent quality, older format, generally not recommended. |
| [c4ai-command-r-v01-Q3_K_L.gguf](https://huggingface.co/bartowski/c4ai-command-r-v01-GGUF/blob/main/c4ai-command-r-v01-Q3_K_L.gguf) | Q3_K_L | 19.14GB | Lower quality but usable, good for low RAM availability. |
| [c4ai-command-r-v01-Q3_K_M.gguf](https://huggingface.co/bartowski/c4ai-command-r-v01-GGUF/blob/main/c4ai-command-r-v01-Q3_K_M.gguf) | Q3_K_M | 17.61GB | Even lower quality. |
| [c4ai-command-r-v01-Q3_K_S.gguf](https://huggingface.co/bartowski/c4ai-command-r-v01-GGUF/blob/main/c4ai-command-r-v01-Q3_K_S.gguf) | Q3_K_S | 15.86GB | Low quality, not recommended. |
| [c4ai-command-r-v01-Q2_K.gguf](https://huggingface.co/bartowski/c4ai-command-r-v01-GGUF/blob/main/c4ai-command-r-v01-Q2_K.gguf) | Q2_K | 13.81GB | Extremely low quality, *not* recommended.

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski
