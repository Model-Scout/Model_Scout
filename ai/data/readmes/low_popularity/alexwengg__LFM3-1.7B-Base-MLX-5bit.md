---
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: text-generation
base_model: LiquidAI/LFM3-1.7B-Base
base_model_relation: quantized
tags:
- mlx
- lfm3
- liquid
- base-model
- quantized
- apple-silicon
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
---

# LFM3-1.7B-Base-MLX-5bit

Unofficial MLX build of [LiquidAI/LFM3-1.7B-Base](https://huggingface.co/LiquidAI/LFM3-1.7B-Base), the
pretrained (not instruction-tuned) 1.7B LFM3 model, for Apple Silicon. Liquid AI publishes MLX builds of the instruct
model ([LiquidAI/LFM3-1.7B-MLX-5bit](https://huggingface.co/LiquidAI/LFM3-1.7B-MLX-5bit) and others) but none of the
Base model. This is a community conversion, not a Liquid AI release; the weights are LiquidAI's, quantized.

- Weights: 1.189 GB (`model.safetensors`).
- Quantization: 5-bit affine, group size 64, on every Linear layer and the tied embedding/LM head (`lfm3_quant_recipe.json`: `all:5/64`).
- Made with [mlx-vlm](https://github.com/Blaizzy/mlx-vlm) `main` (`230fc308`) and MLX 0.32.4 from the bf16 checkpoint
  (`LiquidAI/LFM3-1.7B-Base` revision `545fc8f4`). Same file layout as Liquid's own MLX text builds
  (`language_model.model.*` keys).
- Sibling build: [alexwengg/LFM3-1.7B-Base-MLX-mixed-5-6-8](https://huggingface.co/alexwengg/LFM3-1.7B-Base-MLX-mixed-5-6-8).

This is a base model: use it for completion, few-shot prompting, scoring and fine-tuning. It is not tuned to follow
chat instructions, and it does not stop on its own the way the instruct model does.

## Quality

Measured on an Apple M5 Pro with MLX 0.32.4, against float32 references of the original checkpoint:

- **HF fp32 goldens**: the original checkpoint run in float32 by Hugging Face Transformers 5.21.0 on CPU. Two sets:
  25 prompts (chat, tool-call and raw text; final-position next-token distribution) and 5 raw-text prompts with
  64-token greedy continuations (teacher-forced next-token agreement along the fp32 continuation).
- **MLX fp32 reference**: the checkpoint upcast to float32 in mlx-vlm; it matches the HF fp32 run exactly on the
  goldens (teacher-forced agreement 1.0000, 5/5 identical greedy continuations). Wikitext-2 test, 16 x 2048 tokens;
  fp32 perplexity 10.588.

| build | goldens (25): final top-1 | goldens (25): final KL | goldens (5 raw): teacher-forced agreement | goldens (5 raw): final KL | wikitext-2 KL | wikitext-2 PPL vs fp32 |
|---|---|---|---|---|---|---|
| bf16 (unquantized, for reference) | 1.00 | 0.0005 | n/a | n/a | 0.0005 | +0.05% |
| **5-bit** (this repo) | 0.88 | 0.0305 | n/a | n/a | 0.0146 | +1.36% |
| mixed-5-6-8 | 0.92 | 0.0182 | n/a | n/a | 0.0078 | +0.75% |

KL is KL(fp32 || build) in nats over the reference's top-200 next-token support. The bf16 row is the original
checkpoint loaded in bf16 by the same harness. Final-position top-1 is below 1.0 even for bf16 on a few prompts whose two best
next tokens are near-tied.

## Speed

Apple M5 Pro (24 GB), macOS 27.0, MLX 0.32.4, mlx-vlm `main` (`230fc308`). Greedy decoding, 256 generated tokens after a
512- or 2048-token prompt, median of 3 runs after a warm-up, nothing else running on the machine.

| build | decode tok/s (512 ctx) | decode tok/s (2048 ctx) | prefill tok/s (2048-token prompt) | time to first token (2048-token prompt) | peak memory (2048 ctx) |
|---|---|---|---|---|---|
| **5-bit** | 178 | 173 | 6,300 | 327 ms | 2.13 GB |
| mixed-5-6-8 | 166 | 164 | 6,220 | 331 ms | 2.23 GB |

Sustained: in a 60-second run of continuous writing (a relay of ~400-token pieces with sampling at temperature 0.8),
this build produced 9,772-9,952 tokens, i.e. **163-166 tok/s averaged over the whole minute**, peak 174 tok/s, 1.3 GB.

## Use with mlx-vlm

No released mlx-vlm or mlx-lm version supports LFM3 yet (October 2026). mlx-vlm `main` does:

```bash
pip install "git+https://github.com/Blaizzy/mlx-vlm.git@main"
```

```python
from mlx_vlm import load, generate

model, processor = load("alexwengg/LFM3-1.7B-Base-MLX-5bit")
# plain completion: pass the raw text (the generate CLI always applies a chat template)
out = generate(model, processor, "<|startoftext|>The capital of France is", max_tokens=64, temperature=0.0)
print(out.text)
```

`python -m mlx_vlm.generate` wraps the prompt in the chat template, which suits the instruct model rather than
this base model; use the Python API above for raw completion.

## Use with mlx-lm

mlx-lm support is in review ([ml-explore/mlx-lm#2016](https://github.com/ml-explore/mlx-lm/pull/2016), not merged).
With that branch installed, this checkpoint loads as is; against mlx-vlm on 512 positions of text the two give the same
argmax at 98.8% (5-bit) / 99.4% (mixed) of positions, max |logit difference| 0.5 (bf16 kernel differences):

```bash
pip install "git+https://github.com/ml-explore/mlx-lm.git@refs/pull/2016/head"
mlx_lm.generate --model alexwengg/LFM3-1.7B-Base-MLX-5bit --prompt "The capital of France is" --max-tokens 64 --temp 0.0 \
  --ignore-chat-template
```

Loading through transformers' `AutoConfig` may ask to trust remote code (`config.json` keeps Liquid's `auto_map`,
as Liquid's own MLX builds do); MLX does not run that code.

## Limitations

- Quantization moves the next-token distribution (table above); greedy continuations diverge from fp32 after a few
  dozen tokens on average, as for any 5-6-bit build.
- Evaluated on English text, short chat/tool prompts and wikitext-2 only; contexts up to about 2,000 tokens were
  tested, although the architecture supports 262,144.
- Measured on one machine (M5 Pro); speeds on other Apple chips will differ.

## License

The weights are a quantized derivative of LiquidAI/LFM3-1.7B-Base and are distributed under the
[LFM Open License v1.0](LICENSE), the license of the original model. The remote-code files
(`configuration_lfm3.py`, `modeling_lfm3.py`, `lfm3_conv.py`) are copied unchanged from the original repository.
