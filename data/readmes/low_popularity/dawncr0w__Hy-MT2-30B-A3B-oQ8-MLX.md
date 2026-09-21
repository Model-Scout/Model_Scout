---
library_name: mlx
base_model: tencent/Hy-MT2-30B-A3B
tags:
- mlx
- oq8
- quantized
- translation
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
license: other
---

# Hy-MT2-30B-A3B-oQ8-MLX

This is an oQ8 MLX quantized derivative of [tencent/Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B).

The model was quantized locally with oMLX oQ8. The resulting config targets approximately 8.50 bpw and includes a packaged `hy_v3.py` model file so MLX-LM can load the HYV3 architecture from the model directory.

## Validation

Local validation completed with the oMLX app bundle on macOS:

```text
mlx_lm load: passed
generation smoke test: passed
prompt: Hello
max tokens: 4
peak memory: 29.815 GB
```

## Usage

Use an MLX-LM build that supports the APIs used by the packaged `hy_v3.py` file.

```bash
python -m mlx_lm generate \
  --model /path/to/Hy-MT2-30B-A3B-oQ8-MLX \
  --ignore-chat-template \
  --prompt "Hello" \
  --max-tokens 32 \
  --temp 0
```

## License And Notice

The base model is distributed under the Tencent HY Community License Agreement. This distribution includes `LICENSE.txt` and `NOTICE` from/for the Tencent HY license requirements.

This repository is not affiliated with, sponsored by, or endorsed by Tencent.
