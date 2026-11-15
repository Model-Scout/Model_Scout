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
  - apple-silicon
pipeline_tag: translation
---

# PLaMo 3 Translate 0.8B — MLX 4bit (compact)

**Built with PLaMo**

A compact MLX conversion of [pfnet/plamo-3-translate-0.8b](https://huggingface.co/pfnet/plamo-3-translate-0.8b), quantized to 4 bits with mlx-lm. The weights are about **half the size** of the official MLX 4-bit release (501 MB vs 0.98 GB), and translation quality is measured to be on par with the BF16 original (chrF++ 31.56 vs 31.20 reference; see **Quality** below).

This model is a DERIVED MODEL under the PLaMo Community License. See the **License** section below before use or redistribution.

## Conversion details

| Item | Value |
|---|---|
| Source | pfnet/plamo-3-translate-0.8b (BF16, unmodified) |
| Tool | mlx-lm 0.32.2 (`mlx_lm convert`) |
| Quantization | 4-bit affine, group size 64, all layers (4.501 bits per weight) |
| Weights file | 501,002,761 bytes (model.safetensors) |
| Total repository size | ~505 MB |

Conversion fidelity was checked numerically: dequantized weights match the BF16 originals with cosine similarity ≈ 0.996 per tensor, which is the expected range for 4-bit affine quantization.

## Quality (measured)

chrF++ on FLORES-200 devtest, first 100 sentences per direction, greedy decoding, generated with MLX on a Mac mini (M2 Pro):

| Direction | This model (MLX 4bit) | BF16 original (reference) |
|---|---|---|
| en→ja | 34.70 | 34.08 |
| zh→ja | 31.62 | 31.25 |
| ko→ja | 28.37 | 28.26 |
| **Average** | **31.56** | **31.20** |

The 4-bit quantization is effectively lossless. The reference scores were measured with the Hugging Face implementation under the same protocol, so small differences include cross-implementation variance and should be read as "no degradation", not as an improvement.

## Measured on Apple Silicon (Mac mini, M2 Pro, 32 GB)

Measured with mlx-lm 0.32.2 on the machine above:

| Metric | Value |
|---|---|
| Cold load time | 5.97 s |
| Decode speed | 257–352 tokens/s |
| Peak memory (MLX-managed) | 593 MB (weights 501 MB + KV/workspace ~90 MB) |
| Peak RSS (whole Python process, incl. torch/transformers for the tokenizer) | 1.12 GB |

Sample outputs (greedy):

- en→ja: "The meeting has been rescheduled to next Monday due to a scheduling conflict." → 「日程の都合がつかず、会議は来週の月曜日に変更となりました。」
- zh→ja: 「明日の朝、友人を迎えに空港へ行くのですが、彼の便は10時着です。」
- ko→ja: 「今日は天気が良かったので、友達と公園に散歩に行きました。」
- ja→en: "The meeting has been rescheduled for next Monday."

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
