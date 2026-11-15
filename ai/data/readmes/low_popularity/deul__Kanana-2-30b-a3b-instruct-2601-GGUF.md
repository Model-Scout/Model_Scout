---
license: other
license_name: kanana
license_link: https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct-2601/blob/main/LICENSE
base_model: kakaocorp/kanana-2-30b-a3b-instruct-2601
base_model_relation: quantized
language:
- ko
- en
tags:
- gguf
- llama.cpp
- ollama
- kanana
- moe
- quantized
pipeline_tag: text-generation
---

# Kanana-2-30b-a3b-instruct-2601 GGUF

GGUF quantizations of [kakaocorp/kanana-2-30b-a3b-instruct-2601](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct-2601).

> **Powered by Kanana**
> Kanana is licensed in accordance with the [Kanana License Agreement](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct-2601/blob/main/LICENSE).

The official repository only provides GGUF for `thinking-2601`; there was **no GGUF for `instruct-2601`**, so it was converted and quantized directly.

## Model details
- **Base model**: kakaocorp/kanana-2-30b-a3b-instruct-2601 (Kakao Corp)
- **Architecture**: DeepseekV3 (MLA + MoE, 30B total / 3B active, 48 layers, 128 experts)
- **Features**: Korean-specialized, tool calling support, non-thinking (instruction-tuned), 32K context
- **Conversion**: llama.cpp `convert_hf_to_gguf.py` → `llama-quantize`
- **Chat template**: embedded in GGUF (ChatML `<|im_start|>` + Qwen-style tool XML)

## Available quantizations
| File | Method | Size | Notes |
|---|---|---|---|
| `*-Q8_0.gguf`   | Q8_0   | ~30GB | Highest quality |
| `*-Q6_K.gguf`   | Q6_K   | ~24GB | High quality |
| `*-Q5_K_M.gguf` | Q5_K_M | ~20GB | Balanced |
| `*-Q4_K_M.gguf` | Q4_K_M | ~17GB | Recommended (practical, 4.85 BPW) |

## Usage

### Ollama
```
# Modelfile
FROM ./kanana-2-30b-a3b-instruct-2601-Q4_K_M.gguf
PARAMETER num_ctx 8192
PARAMETER stop "<|im_end|>"
```
```
ollama create kanana2-instruct -f Modelfile
ollama run kanana2-instruct "Hello"
```

### llama.cpp
```
llama-cli -m kanana-2-30b-a3b-instruct-2601-Q4_K_M.gguf -p "Hello" -c 8192
```

## License
These GGUF files are distributed under the same **Kanana License** as the original model. Commercial use (API/cloud services, resale, 10M+ MAU, etc.) requires a separate commercial license from Kakao. See the [Kanana License](https://huggingface.co/kakaocorp/kanana-2-30b-a3b-instruct-2601/blob/main/LICENSE) for details.
