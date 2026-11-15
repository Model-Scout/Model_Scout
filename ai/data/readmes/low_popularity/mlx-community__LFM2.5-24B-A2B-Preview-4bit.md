---
base_model: lq-preview/LFM2.5-24B-A2B-Preview
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: text-generation
tags:
- mlx
- mlx-vlm
- lfm2.5
- moe
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
- it
---

# LFM2.5-24B-A2B-Preview — 4bit

MLX conversion of [lq-preview/LFM2.5-24B-A2B-Preview](https://huggingface.co/lq-preview/LFM2.5-24B-A2B-Preview), pinned to revision `f772950ce6f17d35af5469d00334b61a9c2fc034`. Converted with the MLX-VLM CLI on an Apple M3 Ultra. This is a text generation model.

Affine weight-only quantization, 4 bits, group size 64. Router projections use affine 8-bit quantization (group size 64). Unquantized floating-point weights remain BF16; expert routing biases remain FP32.

The source configuration specifies a context limit of **131,072 tokens**. Weight files total **13.49 GB** (decimal); runtime memory also includes cache and temporary allocations.

## Usage

This export was tested with the LFM2.5 port in [MLX-VLM PR #2505](https://github.com/Blaizzy/mlx-vlm/pull/2505), commit `a6c7313bc053e5887616fa850808d21576eddf98`, MLX 0.32.3 and Transformers 5.17.0.

```bash
pip install 'git+https://github.com/Blaizzy/mlx-vlm.git@a6c7313bc053e5887616fa850808d21576eddf98'
python -m mlx_vlm generate \
  --model nativ-community/LFM2.5-24B-A2B-Preview-4bit \
  --prompt "What is the capital of France? Answer briefly." \
  --max-tokens 512 \
  --temperature 0.1
```

Identical model files are published in both organizations:

- [nativ-community/LFM2.5-24B-A2B-Preview-4bit](https://huggingface.co/nativ-community/LFM2.5-24B-A2B-Preview-4bit)
- [mlx-community/LFM2.5-24B-A2B-Preview-4bit](https://huggingface.co/mlx-community/LFM2.5-24B-A2B-Preview-4bit)

Use the included chat template. The model generates reasoning before its final answer, so allow enough output tokens.

## Conversion

```bash
python -m mlx_vlm convert --hf-path lq-preview/LFM2.5-24B-A2B-Preview --revision f772950ce6f17d35af5469d00334b61a9c2fc034 --mlx-path ./LFM2.5-24B-A2B-Preview-4bit --dtype bfloat16 -q --q-mode affine --q-bits 4 --q-group-size 64
```

The export was reloaded with strict weight matching. Prefill and cached decode produced finite logits, and two short greedy generation checks returned Paris and 391 correctly and reached EOS. These checks are smoke tests, not a comprehensive quality evaluation or a long-context benchmark. See `conversion_info.json` for settings and versions.

## License and attribution

The original model is by Liquid AI, Inc. The original [LFM Open License v1.0](LICENSE) is included and applies to these weights. Conversion and quantization modifications are described in [NOTICE](NOTICE).
