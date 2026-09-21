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
- mxfp4
- lfm2.5
- liquid
- text-generation
---

# LFM2.5-8B-A1B-MXFP4

MLX MXFP4 conversion of [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B), built for Apple Silicon inference.

This is a text-only LFM2.5 hybrid model with LIV convolution layers, GQA attention layers, and MoE feed-forward layers. It keeps the original Liquid chat template in `chat_template.jinja`.

## Format

- Quantization: MLX MXFP4
- Converter output: `4.251 bits per weight`
- Quantization config: `mode=mxfp4`, `bits=4`, `group_size=32`
- Router/gate tensors: preserved at 8-bit groups where emitted by MLX
- Local size before upload: `4.2G`
- Source model: `LiquidAI/LFM2.5-8B-A1B`

## Runtime

Use an MLX runtime with LFM2/LFM2.5 support.

```python
from mlx_lm import load, generate

model, tokenizer = load("OsaurusAI/LFM2.5-8B-A1B-MXFP4")
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
- Reported generation speed: about `286 tok/s` on a 96-token run
- Peak memory reported by the smoke run: about `4.544 GB`

This is a smoke test, not a benchmark suite or accuracy evaluation.

## Korean

이 모델은 LiquidAI/LFM2.5-8B-A1B를 Apple Silicon용 MLX MXFP4 형식으로 변환한 버전입니다. `chat_template.jinja`의 기본 템플릿을 사용하고, 런타임에서 별도의 `<think>` 접두어를 강제로 추가하지 않는 것을 권장합니다.

