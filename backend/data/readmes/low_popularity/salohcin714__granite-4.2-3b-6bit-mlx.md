---
license: apache-2.0
license_link: https://www.apache.org/licenses/LICENSE-2.0
base_model: ibm-granite/granite-4.2-3b
base_model_relation: quantized
library_name: mlx
pipeline_tag: text-generation
language: [en, de, es, fr, ja, pt, ar, cs, it, ko, nl, zh]
tags: [language, granite-4.1, mlx, apple-silicon]
---

# granite-4.2-3b-6bit-mlx

## Provenance

Converted from [`ibm-granite/granite-4.2-3b`](https://huggingface.co/ibm-granite/granite-4.2-3b) using
[mlx-lm](https://github.com/ml-explore/mlx-lm) 0.31.3.

## Usage

```python
from mlx_lm import load, generate

model, tokenizer = load("salohcin714/granite-4.2-3b-6bit-mlx")
messages = [{"role": "user", "content": "Hello"}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
text = generate(model, tokenizer, prompt=prompt, verbose=True)
```

## Modifications

Weights converted to MLX safetensors layout and quantized (6-bit affine quantization, group size 64, via round-to-nearest, no calibration). Redundant tied `lm_head.weight` dropped where the model ties input/output embeddings. No fine-tuning; no added training data.

## License and attribution

Licensed under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Original weights by the Granite Team, IBM. See the
[upstream model card](https://huggingface.co/ibm-granite/granite-4.2-3b) and the included
`LICENSE` file for the full text.

## Disclaimer

This repository is not affiliated with or endorsed by IBM. "Granite" is an IBM trademark, used here descriptively to identify the origin of the base model. IBM's published benchmarks describe the original weights, not this quantized/converted artifact, and must not be read as claims about this repo.
