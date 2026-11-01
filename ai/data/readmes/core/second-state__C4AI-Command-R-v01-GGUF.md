---
base_model: CohereForAI/c4ai-command-r-v01
inference: false
library_name: transformers
license: cc-by-nc-4.0
model_creator: Cohere
model_name: C4AI Command-R
quantized_by: Second State Inc.
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
---

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://github.com/LlamaEdge/LlamaEdge/raw/dev/assets/logo.svg" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# C4AI-Command-R-v01-GGUF

## Original Model

[CohereForAI/c4ai-command-r-v01](https://huggingface.co/CohereForAI/c4ai-command-r-v01)

## Run with LlamaEdge

- LlamaEdge version: coming soon

- Context size: `8192`

## Quantized GGUF Models

| Name | Quant method | Bits | Size | Use case |
| ---- | ---- | ---- | ---- | ----- |
| [c4ai-command-r-v01-Q2_K.gguf](https://huggingface.co/second-state/C4AI-Command-R-v01-GGUF/blob/main/c4ai-command-r-v01-Q2_K.gguf)     | Q2_K   | 2 | 13.8 GB| smallest, significant quality loss - not recommended for most purposes |
| [c4ai-command-r-v01-Q3_K_L.gguf](https://huggingface.co/second-state/C4AI-Command-R-v01-GGUF/blob/main/c4ai-command-r-v01-Q3_K_L.gguf) | Q3_K_L | 3 | 19.1 GB| small, substantial quality loss |
| [c4ai-command-r-v01-Q3_K_M.gguf](https://huggingface.co/second-state/C4AI-Command-R-v01-GGUF/blob/main/c4ai-command-r-v01-Q3_K_M.gguf) | Q3_K_M | 3 | 17.6 GB| very small, high quality loss |
| [c4ai-command-r-v01-Q3_K_S.gguf](https://huggingface.co/second-state/C4AI-Command-R-v01-GGUF/blob/main/c4ai-command-r-v01-Q3_K_S.gguf) | Q3_K_S | 3 | 15.9 GB| very small, high quality loss |
| [c4ai-command-r-v01-Q4_0.gguf](https://huggingface.co/second-state/C4AI-Command-R-v01-GGUF/blob/main/c4ai-command-r-v01-Q4_0.gguf)     | Q4_0   | 4 | 20.2 GB| legacy; small, very high quality loss - prefer using Q3_K_M |
| [c4ai-command-r-v01-Q4_K_M.gguf](https://huggingface.co/second-state/C4AI-Command-R-v01-GGUF/blob/main/c4ai-command-r-v01-Q4_K_M.gguf) | Q4_K_M | 4 | 21.5 GB| medium, balanced quality - recommended |
| [c4ai-command-r-v01-Q4_K_S.gguf](https://huggingface.co/second-state/C4AI-Command-R-v01-GGUF/blob/main/c4ai-command-r-v01-Q4_K_S.gguf) | Q4_K_S | 4 | 20.4 GB| small, greater quality loss |
| [c4ai-command-r-v01-Q5_0.gguf](https://huggingface.co/second-state/C4AI-Command-R-v01-GGUF/blob/main/c4ai-command-r-v01-Q5_0.gguf)     | Q5_0   | 5 | 24.3 GB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [c4ai-command-r-v01-Q5_K_M.gguf](https://huggingface.co/second-state/C4AI-Command-R-v01-GGUF/blob/main/c4ai-command-r-v01-Q5_K_M.gguf) | Q5_K_M | 5 | 25 GB| large, very low quality loss - recommended |
| [c4ai-command-r-v01-Q5_K_S.gguf](https://huggingface.co/second-state/C4AI-Command-R-v01-GGUF/blob/main/c4ai-command-r-v01-Q5_K_S.gguf) | Q5_K_S | 5 | 24.3 GB| large, low quality loss - recommended |
| [c4ai-command-r-v01-Q6_K.gguf](https://huggingface.co/second-state/C4AI-Command-R-v01-GGUF/blob/main/c4ai-command-r-v01-Q6_K.gguf)     | Q6_K   | 6 | 28.7 GB| very large, extremely low quality loss |
| [c4ai-command-r-v01-Q8_0.gguf](https://huggingface.co/second-state/C4AI-Command-R-v01-GGUF/blob/main/c4ai-command-r-v01-Q8_0.gguf)     | Q8_0   | 8 | 37.2 GB| very large, extremely low quality loss - not recommended |

*Quantized with llama.cpp b2450*
