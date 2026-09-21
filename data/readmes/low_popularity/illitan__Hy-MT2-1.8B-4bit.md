---
base_model: tencent/Hy-MT2-1.8B
language:
  - zh
  - en
  - fr
  - pt
  - es
  - ja
  - tr
  - ru
  - ar
  - ko
  - th
  - it
  - de
  - vi
  - ms
  - id
  - tl
  - hi
  - pl
  - cs
  - nl
  - km
  - my
  - fa
  - gu
  - ur
  - te
  - mr
  - he
  - bn
  - ta
  - uk
  - bo
  - kk
  - mn
  - ug
library_name: mlx
license: other
license_name: tencent-hunyuan-community
license_link: https://huggingface.co/tencent/Hy-MT2-1.8B/blob/main/LICENSE.txt
pipeline_tag: text-generation
tags:
  - mlx
  - mlx-my-repo
  - hunyuan
  - translation
---

# Hy-MT2-1.8B-4bit (MLX)

This is a 4-bit MLX quantized version of [tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B), optimized for Apple Silicon (M1/M2/M3/M4) via the [MLX](https://github.com/ml-explore/mlx) framework.

## Model Details

- **Base model**: [tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B)
- **Architecture**: `HunYuanDenseV1ForCausalLM` (Hunyuan Dense V1, 1.8B parameters)
- **Quantization**: 4-bit, group size 64, affine mode
- **Format**: MLX safetensors
- **File size**: ~1.0 GB (`model.safetensors`)
- **Task**: Translation across 35+ languages

## Conversion

This model was converted with [`mlx-lm`](https://github.com/ml-explore/mlx-lm) **0.31.3**:

```bash
mlx_lm.convert \
    --hf-path tencent/Hy-MT2-1.8B \
    --mlx-path Hy-MT2-1.8B-4bit \
    --quantize \
    --q-bits 4 \
    --q-group-size 64
```

## Usage with `mlx-lm`

Install:

```bash
pip install mlx-lm
```

Inference (uses the bundled `chat_template.jinja` from the original repo):

```python
from mlx_lm import load, generate

model, tokenizer = load("illitan/Hy-MT2-1.8B-4bit")

messages = [
    {"role": "user", "content": "Translate the following text to Chinese: 'Hello, how are you today?'"}
]

prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)

response = generate(
    model,
    tokenizer,
    prompt=prompt,
    max_tokens=256,
    verbose=True,
)
print(response)
```

## Supported Languages

Same coverage as the base model — 35+ languages including Chinese, English, French, Portuguese, Spanish, Japanese, Turkish, Russian, Arabic, Korean, Thai, Italian, German, Vietnamese, Malay, Indonesian, Tagalog, Hindi, Polish, Czech, Dutch, Khmer, Burmese, Persian, Gujarati, Urdu, Telugu, Marathi, Hebrew, Bengali, Tamil, Ukrainian, Tibetan, Kazakh, Mongolian, and Uyghur.

See the [base model card](https://huggingface.co/tencent/Hy-MT2-1.8B) for full translation direction coverage.

## License

This model is released under the **Tencent HY Community License Agreement** (inherited from the base model). See the full license text at [tencent/Hy-MT2-1.8B/LICENSE.txt](https://huggingface.co/tencent/Hy-MT2-1.8B/blob/main/LICENSE.txt).

### Important geographic restriction

> **The Tencent HY Community License explicitly prohibits use, reproduction, modification, and distribution of the model (including derivatives such as this quantization) within the European Union.**

If you are located in the EU, you are **not permitted** to download or use this model. Please review the upstream license before any commercial or research use.

## Acknowledgements

- [Tencent](https://huggingface.co/tencent) for the original Hy-MT2-1.8B model.
- [Apple MLX team](https://github.com/ml-explore/mlx) and [`mlx-lm`](https://github.com/ml-explore/mlx-lm) for the on-device inference stack.
