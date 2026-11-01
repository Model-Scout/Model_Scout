---
language:
  - en
  - ko
  - ja
library_name: mlx
pipeline_tag: text-generation
license: other
license_name: upstage-solar-license
license_link: LICENSE
base_model: upstage/Solar-Open2-250B
tags:
  - mlx
  - solar
  - solar-open2
  - moe
  - text-generation
  - quantized
  - 6bit
---


# Solar-Open2-250B-MLX-6bit


Built with Solar. This is an MLX 6-bit affine quantization of [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B), converted for Apple Silicon / MLX workflows.


## Details


- Source model: `upstage/Solar-Open2-250B`
- Quantization: 6-bit affine, group size 64
- Local size: 190G
- Weight shards: 48
- Architecture: Solar Open 2 hybrid-attention MoE, 250B total / ~15B active parameters
- Context: source model advertises 1M-token context; practical MLX context depends on memory and runtime settings


## Important runtime notes


Solar Open2 is not yet a stock `mlx-lm` architecture in many installs. This repo includes `solar_open2.py`; launch with `--trust-remote-code` when serving or loading from Hugging Face.


```bash
mlx_lm.server \
  --model Vontra/Solar-Open2-250B-MLX-6bit \
  --host 0.0.0.0 \
  --port 8021 \
  --trust-remote-code \
  --temp 0.2 \
  --top-p 0.9 \
  --max-tokens 32768
```


You may see a `transformers` warning that mentions loading `model_type=solar_open2` into a blank model type. With the included custom MLX loader this warning is expected; the important check is that the model actually loads.


The tokenizer template uses Solar/Whale-style tool markers such as `<|tool_call:start|>` and `<|tool_arg:start|>`. For OpenAI-compatible tool calling, your serving runtime must parse those markers into structured `tool_calls`. Plain text generation does not need this parser.


## Use with MLX


This repo includes a small `solar_open2.py` MLX loader because upstream `mlx-lm` does not yet ship native Solar Open 2 support.


```bash
pip install -U mlx-lm
```


```python
from mlx_lm import load, generate


model, tokenizer = load("Vontra/Solar-Open2-250B-MLX-6bit")
prompt = "Write a short Python function that validates an IPv4 CIDR string."
print(generate(model, tokenizer, prompt=prompt, max_tokens=256, verbose=True))
```


## Notes


This is an independent community conversion under the Vontra organization. It is not an official Upstage release.


## License


The source model is released under the Upstage Solar License. A copy is included in `LICENSE`. Please review the upstream model card and license before use or redistribution.



<!-- vontra-chooser-start -->
## Choose for your Mac

[64GB Macs](https://huggingface.co/collections/Vontra/mlx-models-for-64gb-macs-6a9fefda17932216ec9ab457) · [128GB Macs](https://huggingface.co/collections/Vontra/mlx-models-for-128gb-macs-6a9ff0abd31bc9abbe7922d7) · [256GB Macs](https://huggingface.co/collections/Vontra/mlx-models-for-256gb-macs-6a9ff0ef9fed7c5bdca15e9b)

No measured memory tier is assigned here. The collections use published M3 Studio peaks with at least 25% nominal headroom; fit on other Macs is an estimate, and full context is not guaranteed. Start with short context and one request.

### Runtime and evidence

The exact tested oMLX application version is not recorded here; a library version is not an app version. The original performance tables retain their benchmark conditions and speed figures; this documentation update adds no new test results.

### Quick start and demo prompt

```bash
hf download Vontra/Solar-Open2-250B-MLX-6bit --local-dir ./models/Solar-Open2-250B-MLX-6bit
```

Add the downloaded folder to oMLX model directories, refresh the list, and follow this card's architecture and MTP compatibility requirements before loading.

Try this in a new chat with a 128-token output limit:

```text
Explain why the sky looks blue in three short sentences.
```

This is a demo prompt to try, not a recorded successful run; a captured demonstration for this documentation update is not yet available.

[Follow Vontra for new Apple Silicon releases and fixes.](https://huggingface.co/Vontra)
<!-- vontra-chooser-end -->
