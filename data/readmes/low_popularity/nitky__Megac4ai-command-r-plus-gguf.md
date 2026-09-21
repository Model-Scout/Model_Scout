---
base_model:
- CohereForAI/c4ai-command-r-plus
library_name: gguf
tags:
- mergekit
- merge
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
pipeline_tag: text-generation
license: cc-by-nc-4.0
---
# Megac4ai-command-r-plus-gguf

These are quantized GGUF versions of [nitky/Megac4ai-command-r-plus](https://huggingface.co/nitky/Megac4ai-command-r-plus). Please check the original model for license and more details.

## Results for non-English languages (Japanese)

| Model | Output Quality | Notes |
|-------|----------------|-------|
| Megac4ai-command-r-plus-IQ3_XS.gguf | Poor | |
| Megac4ai-command-r-plus-IQ4_XS.gguf | Average | |
| Megac4ai-command-r-plus-Q4_K_M.gguf | Good | recommended |
| Megac4ai-command-r-plus-Q5_K_M.gguf | Good | |
| Megac4ai-command-r-plus-Q6_K.gguf | Excellent | recommended |
| Megac4ai-command-r-plus-Q8_0.gguf | Excellent | |
