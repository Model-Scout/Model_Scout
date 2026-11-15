---
license: other
license_name: plamo-community-license
license_link: https://plamo.preferredai.jp/info/plamo-community-license-en
base_model: pfnet/plamo-3-translate-0.8b
library_name: mlx
language:
  - ja
  - en
  - zh
  - ko
tags:
  - mlx
  - translation
  - quantized
  - mixed-precision
  - apple-silicon
pipeline_tag: translation
---

# PLaMo 3 Translate 0.8B — MLX mixed 3/4bit

**Built with PLaMo**

An MLX conversion of [pfnet/plamo-3-translate-0.8b](https://huggingface.co/pfnet/plamo-3-translate-0.8b) using mlx-lm's built-in **mixed_3_4** quantization recipe (the same allocation strategy as llama.cpp's Q4_K_M): the lm_head and the down_proj of the first, last, and every third layer are kept at 4 bits, everything else is quantized to 3 bits (affine, group size 64; 3.804 bits per weight on average).

Compared to the uniform 4-bit conversion ([plamo-3-translate-0.8b-mlx-4bit-compact](https://huggingface.co/sizumita/plamo-3-translate-0.8b-mlx-4bit-compact)), this variant is **16% smaller** (423 MB vs 501 MB of weights) and **about 5% faster** in decoding on a Mac mini (M2 Pro), with translation quality measured to be essentially unchanged on both FLORES-200 and a held-out news corpus (NTREX-128; see **Quality** below).

This model is a DERIVED MODEL under the PLaMo Community License. See the **License** section below before use or redistribution.

## Conversion details

| Item | Value |
|---|---|
| Source | pfnet/plamo-3-translate-0.8b (BF16, unmodified) |
| Tool | mlx-lm 0.32.2 (`mlx_lm convert --quant-predicate mixed_3_4`) |
| Quantization | Mixed affine, group size 64: lm_head + selected down_proj at 4 bits, all other layers at 3 bits (3.804 bits/weight average) |
| Weights file | ~423 MB (model.safetensors) |
| Vocab | Full 107,520 tokens (no vocabulary trimming) |

## Quality (measured)

chrF++ with greedy decoding, generated with MLX on a Mac mini (M2 Pro, mlx-lm 0.32.2). "4bit" is the uniform 4-bit conversion in the sibling repository above, measured under the identical protocol.

FLORES-200 devtest, first 100 sentences per direction:

| Direction | This model (mixed 3/4bit) | 4bit (uniform) |
|---|---|---|
| en→ja | 33.30 | 34.70 |
| zh→ja | 30.19 | 31.62 |
| ko→ja | 30.64 | 28.37 |
| **Average** | **31.37** | **31.56** |

NTREX-128 (held-out news text, never used in any conversion or selection step), first 200 sentences per direction:

| Direction | This model (mixed 3/4bit) | 4bit (uniform) |
|---|---|---|
| en→ja | 25.66 | 25.58 |
| zh→ja | 21.49 | 21.29 |
| ko→ja | 22.93 | 23.34 |
| ja→en | 48.19 | 49.41 |
| **Average** | **29.57** | **29.90** |

The differences are within quantization noise: no direction collapses, and the held-out corpus confirms the FLORES result. One behavioral note: because most weights change precision, greedy outputs are usually *different translations* from the 4-bit model's (only 12–28 of 200 sentences are byte-identical per direction on NTREX), even though reference-based quality is the same. If you need outputs identical to the 4-bit model, use the 4-bit model.

## Measured on Apple Silicon (Mac mini, M2 Pro, 32 GB)

| Metric | This model | 4bit (uniform) |
|---|---|---|
| Weights | ~423 MB | 501 MB |
| Decode speed | ~352 tokens/s | ~334 tokens/s |
| Peak memory (MLX-managed) | ~565 MB | ~642 MB |
| Load time | ~2.5 s | ~3.1 s |

## Usage

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

# NOTE: this model's tokenizer uses custom code shipped in the repository.
# Pass trust_remote_code via tokenizer_config when loading programmatically.
model, tokenizer = load(
    "<this-repo>",
    tokenizer_config={"trust_remote_code": True},
)

messages = [{"role": "user", "content": "The meeting has been rescheduled to next Monday."}]
prompt = tokenizer.apply_chat_template(
    messages, target_lang="ja", add_generation_prompt=True, tokenize=False
)
print(generate(model, tokenizer, prompt=prompt, max_tokens=128))
```

Supported translation directions follow the base model (multilingual → Japanese, Japanese → multilingual, and related directions; see the base model card).

## License

This repository is distributed under the **PLaMo Community License Agreement** by Preferred Networks, Inc. The full license text is included in this repository as [LICENSE](./LICENSE); the authoritative version is at https://plamo.preferredai.jp/info/plamo-community-license-en

By downloading or using this model, you agree to the PLaMo Community License. In particular:

- Redistribution must include the license text, display "Built with PLaMo", and keep "PLaMo" in the model name (Article 4).
- Non-commercial use is free. Commercial use additionally requires prior registration with PFN and is limited to users whose annual revenue does not exceed 1 billion yen; larger-scale commercial use requires a separate license from PFN (Article 3).

This is an unofficial conversion, not affiliated with or endorsed by Preferred Networks, Inc.
