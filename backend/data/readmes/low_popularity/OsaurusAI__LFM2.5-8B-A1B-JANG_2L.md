---
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
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM2.5-8B-A1B
pipeline_tag: text-generation
library_name: mlx
tags:
- mlx
- jang
- jang-2l
- lfm2.5
- liquid
- text-generation
---

# LFM2.5-8B-A1B-JANG_2L

JANG_2L conversion of [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B), built for Apple Silicon inference through JANG-aware MLX/vMLX runtimes.

This bundle is not a plain MLX 2-bit quant. It uses JANG importance allocation over MLX affine quantized tensors, with higher precision reserved for runtime-sensitive tensors.

## Format

- Format: JANG affine
- Profile: `JANG_2L`
- Quantization backend: `mx.quantize`
- Group size: `64`
- Actual bits from `jang_config.json`: `2.37`
- Bit widths used: `2`, `6`, `8`
- Passthrough bit width: `16`
- Local size before upload: `2.9G`
- JANG runtime weight size metadata: `2.84 GB`
- Source model: `LiquidAI/LFM2.5-8B-A1B`

Runtime capability stamp:

```json
{
  "reasoning_parser": "qwen3",
  "tool_parser": "lfm2",
  "think_in_template": false,
  "supports_tools": true,
  "supports_thinking": true,
  "family": "lfm2_moe",
  "modality": "text",
  "cache_type": "hybrid"
}
```

## Runtime

Use a JANG-aware MLX/vMLX runtime. The model has hybrid cache behavior: attention layers use KV cache, while LIV convolution layers use convolution/state cache.

Example with the local JANG tools runtime:

```sh
python -m jang_tools inference \
  --model OsaurusAI/LFM2.5-8B-A1B-JANG_2L \
  --prompt "What is 2+2? Answer briefly." \
  --max-tokens 128 \
  --temperature 0
```

## Chat Template And Reasoning

The bundled `chat_template.jinja` uses Liquid's ChatML-like format:

- User and assistant turns use `<|im_start|>` / `<|im_end|>`.
- The generation prompt ends at `<|im_start|>assistant\n`; it does not pre-open `<think>`.
- Assistant reasoning may appear inside `<think>...</think>`.
- Tool calls use Liquid's Python-call list format inside `<|tool_call_start|>` and `<|tool_call_end|>`.

For this bundle, `think_in_template=false` is intentional. Runtime code should parse reasoning if the model emits it, but should not force a second reasoning prefix.

## Verification

Local smoke run on the converted bundle:

- Prompt: `What is 2+2? Answer briefly.`
- Result: output closed `<think>...</think>` and answered `2 + 2 = 4.`
- Reported generation speed: `206.886 tok/s`
- Load time: `1.946 s`
- Peak RSS: `3887 MB`

This is a smoke test, not a benchmark suite or accuracy evaluation.

## Korean

이 모델은 LiquidAI/LFM2.5-8B-A1B를 JANG_2L 형식으로 변환한 Apple Silicon용 번들입니다. `think_in_template=false`가 의도된 설정이며, 런타임은 모델이 생성한 `<think>...</think>`를 파싱하되 별도의 reasoning 접두어를 강제로 추가하지 않아야 합니다.

