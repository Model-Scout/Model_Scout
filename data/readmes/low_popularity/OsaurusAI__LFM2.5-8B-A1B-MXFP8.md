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
- mxfp8
- lfm2.5
- liquid
- text-generation
---

# LFM2.5-8B-A1B-MXFP8

MLX MXFP8 conversion of [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B), built for Apple Silicon inference.

This is the higher-precision MXFP sibling of the MXFP4 bundle. It preserves the original Liquid chat template in `chat_template.jinja`.

## Format

- Quantization: MLX MXFP8
- Converter output: `8.250 bits per weight`
- Quantization config: `mode=mxfp8`, `bits=8`, `group_size=32`
- Router/gate tensors: preserved at 8-bit groups where emitted by MLX
- Local size before upload: `8.1G`
- Source model: `LiquidAI/LFM2.5-8B-A1B`

## Runtime

Use an MLX runtime with LFM2/LFM2.5 support.

```python
from mlx_lm import load, generate

model, tokenizer = load("OsaurusAI/LFM2.5-8B-A1B-MXFP8")
prompt = tokenizer.apply_chat_template(
    [{"role": "user", "content": "What is 2+2? Answer briefly."}],
    add_generation_prompt=True,
    tokenize=False,
)
print(generate(model, tokenizer, prompt=prompt, max_tokens=64, verbose=True))
```

## Chat Template And Reasoning

The bundled `chat_template.jinja` uses Liquid's ChatML-like format:

- User and assistant turns use `<|im_start|>` / `<|im_end|>`.
- The generation prompt ends at `<|im_start|>assistant\n`; it does not pre-open `<think>`.
- Assistant reasoning may appear inside `<think>...</think>`.
- Tool calls use Liquid's Python-call list format inside `<|tool_call_start|>` and `<|tool_call_end|>`.

Do not force an extra synthetic `<think>` prefix at runtime. Let the template and model handle reasoning normally.

## Verification

Local smoke run on the converted bundle:

- Prompt: `What is 2+2? Answer briefly.`
- Result: generated reasoning identified `4`
- Reported generation speed: about `196 tok/s` on a 64-token run
- Peak memory reported by the smoke run: about `8.767 GB`

This is a smoke test, not a benchmark suite or accuracy evaluation.

## Korean

이 모델은 LiquidAI/LFM2.5-8B-A1B를 Apple Silicon용 MLX MXFP8 형식으로 변환한 버전입니다. MXFP4보다 더 큰 고정밀 형식이며, `chat_template.jinja`의 기본 템플릿을 그대로 사용합니다.

