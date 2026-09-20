---
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
- mlx
base_model: LiquidAI/LFM2.5-2.6B
---
## 💫 Community Model> LFM2.5-2.6B by LiquidAI

_👾 [LM Studio](https://lmstudio.ai) Community models highlights program. Highlighting new & noteworthy models by the community. Join the conversation on [Discord](https://discord.gg/aPQfnNkxGC)_.

**Model creator**: [LiquidAI](https://huggingface.co/LiquidAI)<br>
**Original model**: [LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)<br>
**Source revision**: [`dca1825886789bd40b94368f53b1d9ada4c94598`](https://huggingface.co/LiquidAI/LFM2.5-2.6B/commit/dca1825886789bd40b94368f53b1d9ada4c94598)<br>
**MLX quantization**: provided by [LM Studio team](https://x.com/lmstudio) using [mlx_lm](https://github.com/ml-explore/mlx-lm)<br>

## Technical Details

8-bit affine quantized version of LFM2.5-2.6B using a group size of 64, optimized for Apple Silicon.

## Conversion and modification notice

LM Studio converted the pinned source model from BF16 safetensors to MLX safetensors with [`mlx-lm` 0.30.8 at commit `9c113f7`](https://github.com/ml-explore/mlx-lm/commit/9c113f7019683d944422f96122bed5c636aa0b90). The weights were changed from the source in format and numerical precision.

The source `config.json` was changed to add MLX-LM-compatible aliases: `block_ff_dim=10752` (matching `intermediate_size`) and top-level `rope_theta=10000000.0` (matching `rope_parameters.rope_theta`). MLX-LM also added quantization metadata, and `tokenizer_config.json` was changed to embed the source chat template for compatibility. No other architecture or tokenizer behavior was intentionally changed.

## Reasoning behavior

LFM2.5-2.6B is an always-thinking model. Its source chat template begins every assistant turn with `<think>`; there is no supported template switch to disable reasoning.

## License

This model is distributed under the [LFM Open License v1.0](LICENSE). Review the license before using or redistributing the model, including its commercial-use limitation.

## Special thanks

🙏 Special thanks to the [Apple Machine Learning Research](https://github.com/ml-explore) team for creating [MLX](https://github.com/ml-explore/mlx).

## Disclaimers

LM Studio is not the creator, originator, or owner of any Model featured in the Community Model Program. Each Community Model is created and provided by third parties. LM Studio does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Community Model. You understand that Community Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Community Model is the sole responsibility of the person or entity who originated such Model. LM Studio may not monitor or control the Community Models and cannot, and does not, take responsibility for any such Model. LM Studio disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Community Models. LM Studio further disclaims any warranty that the Community Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Community Models, your downloading of any Community Model, or use of any other Community Model provided by or through LM Studio.
