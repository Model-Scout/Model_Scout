---
base_model:
- tencent/Hy-MT2-1.8B
- tencent/Hy-MT2-30B-A3B
language:
- multilingual
- zh
- en
- ja
- ko
pipeline_tag: translation
tags:
- llama.cpp
- GGUF
- speculative-decoding
- draft-model
- hunyuan
- translation
---

# Hy-MT2-1.8B-SpecDraft-30B

## Experimental Speculative Decoding Draft Model for Hy-MT2-30B-A3B

This is an experimental project that modifies Hy-MT2-1.8B into a speculative decoding draft model for Hy-MT2-30B-A3B.

Acceleration is not guaranteed. This project is mainly for users who want to explore speculative decoding on MoE models.

## Technical Details

The original vocabularies are different:

-   Hy-MT2-1.8B: 120818 tokens
-   Hy-MT2-30B-A3B: 120832 tokens

The model was modified by:

1.  Replacing tokenizer with the Hy-MT2-30B-A3B tokenizer.
2.  Expanding embedding and lm_head weights:
    -   \[120818, 2048\] -\> \[120832, 2048\]
3.  Initializing new token embeddings with mean padding.

In speculative decoding, the draft model only proposes candidate tokens.
The target model Hy-MT2-30B-A3B always performs final verification, so final output quality is not affected.

## Usage

``` bat
llama-server ^
  -m Hy-MT2-30B-A3B-APEX-Imatrix-I-Quality.gguf ^
  --spec-type draft-simple ^
  --spec-draft-model Hy-MT2-1.8B-SpecDraft-30B-Q4_K_M.gguf ^
  --spec-draft-ngl 999 ^
  --spec-draft-n-max 4 ^
  --spec-draft-n-min 3 ^
  --flash-attn on ^
  --gpu-layers 999
```

## Performance Notes

Hy-MT2-30B-A3B is a MoE model with around 3B active parameters.

Because its decoding speed is already very high, speculative decoding may not always improve performance.

Possible results:

-   faster
-   similar speed
-   slightly slower

depending on hardware and llama.cpp scheduling behavior.

This project is intended for: - llama.cpp enthusiasts - large VRAM users - MoE speculative decoding experiments

## License

Follows the original Hy-MT2 license. For research and experimental use only.
