---
license: mit
pipeline_tag: image-text-to-text
tags:
- VAETKI
- llama-cpp
- gguf
- multimodal
- moe
language:
- ko
- en
base_model:
- nc-ai-consortium/VAETKI-VL-7B-A1B
---

# VAETKI-VL-7B-A1B GGUF

GGUF format of [VAETKI-VL-7B-A1B](https://huggingface.co/nc-ai-consortium/VAETKI-VL-7B-A1B) for use with [llama.cpp](https://github.com/ggml-org/llama.cpp).

## Model Overview

VAETKI-VL-7B-A1B is a vision-language model developed by NC-AI consortium, designed for inference efficiency.

- **Architecture**: MoE (Mixture of Experts) 
- **Parameters**: 7.58B total (1.2B activated)
- **Experts**: 64 total, 5 activated per token
- **Languages**: Korean, English
- **Context Length**: 16k tokens

## Files

| File | Description |
|------|-------------|
| `VAETKI-F16-text.gguf` | Text model (FP16) |
| `VAETKI-Q4_K_M-text.gguf` | Text model (Q4_K_M quantized) |
| `VAETKI-mmproj-f16.gguf` | Vision encoder (FP16) |

## llama.cpp Support

> **Note**: llama.cpp support is pending upstream merge.
> Until then, use this fork: https://github.com/dororodoroddo/llama.cpp/tree/add-vaetki-support

## Usage

```bash
# Text only
llama-cli -m VAETKI-Q4_K_M-text.gguf -p "안녕하세요"

# With vision (requires llama.cpp with mtmd support)
llama-mtmd-cli -m VAETKI-Q4_K_M-text.gguf --mmproj VAETKI-mmproj-f16.gguf --image image.jpg -p "이 이미지를 설명해주세요"
```

## Original Model

- Model: [nc-ai-consortium/VAETKI-VL-7B-A1B](https://huggingface.co/nc-ai-consortium/VAETKI-VL-7B-A1B)

## License

MIT License - See [LICENSE](LICENSE) for details.

## Credits

- Original model by NC-AI Consortium (with ETRI, Korea University)
- GGUF conversion for llama.cpp
