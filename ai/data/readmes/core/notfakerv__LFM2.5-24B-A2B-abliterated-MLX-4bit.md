---
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: notfakerv/LFM2.5-24B-A2B-abliterated
base_model_relation: quantized
pipeline_tag: text-generation
language: [en, ar, zh, fr, de, ja, ko, es, pt, it, vi, th, id, hi, ru, pl]
tags: [mlx, mlx-lm, lfm2_moe, lfm2.5, moe, abliterated, 4-bit]
---

# LFM2.5-24B-A2B Abliterated - MLX 4-bit

Standard **4-bit affine MLX** conversion of the saved, edited BF16 checkpoint behind
[notfakerv/LFM2.5-24B-A2B-abliterated](https://huggingface.co/notfakerv/LFM2.5-24B-A2B-abliterated).
This is the **abliterated derivative**, not a conversion of the unmodified original model.
It was converted directly from BF16, **not requantized from GGUF**. No additional training or weight editing was performed for this export.

## Format and requirements

- 13.49 GB of weights in three indexed safetensors shards.
- 4-bit affine quantization, group size 64, for 221 expert/dense/embedding matrices.
- 38 router matrices use 8-bit affine quantization, group size 64, following MLX LM's architecture-specific recipe.
- 169 nonquantized tensors are preserved bit-for-bit after the required convolution layout transpose. Norms and convolution taps remain BF16; expert routing biases remain FP32.
- Tokenizer, reasoning chat template, generation config, and original license are copied unchanged from the saved checkpoint.
- **MLX LM >= 0.32.0** and MLX >= 0.32.2. Older MLX LM releases use incorrect softmax routing for this sigmoid-gated LFM2 MoE architecture.

For Apple Silicon deployment, allow memory for the weights, runtime, KV cache, and macOS. A machine with at least 24 GB of unified memory is a sensible starting point for short contexts; this is a sizing recommendation, not a measured Apple memory benchmark.

## Usage

```bash
pip install -U "mlx-lm>=0.32.0"
mlx_lm.generate --model notfakerv/LFM2.5-24B-A2B-abliterated-MLX-4bit \
  --prompt "Why is the sky blue?" --max-tokens 1024 --temp 0.1 --top-k 50
```

```python
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler, make_logits_processors

model, tokenizer = load("notfakerv/LFM2.5-24B-A2B-abliterated-MLX-4bit")
prompt = tokenizer.apply_chat_template(
    [{"role": "user", "content": "Why is the sky blue?"}],
    tokenize=False, add_generation_prompt=True,
)
print(generate(
    model, tokenizer, prompt=prompt, max_tokens=1024,
    sampler=make_sampler(temp=0.1, top_k=50),
    logits_processors=make_logits_processors(repetition_penalty=1.05),
))
```

This is an always-thinking reasoning model. Its output includes a `<think>` block before the final answer; allow enough generated tokens for both. A speculative draft/MTP model is not included.

## Verification and limits

The export passed a strict MLX LM weight reload, safetensors/index and tensor-shape checks, checksums, exact preservation of all nonquantized tensors, and sampled comparisons of packed weights/scales with direct BF16 quantization. Three benign greedy generation tests checked READY, arithmetic, and JSON final answers. Cached-decode diagnostics are recorded in `conversion_info.json`.

BF16 full-prompt and cached CUDA logits were not bit-identical (arithmetic-prompt KL approximately 0.0082). Two FP32 CPU cache checks matched exactly; FP32 CUDA checks were close (KL below 0.0001), with matching greedy first tokens. These are limited numerical checks, not proof of identical behavior across all batch shapes.

Runtime checks were performed with MLX 0.32.4 / MLX LM 0.32.0 on Linux CUDA, NVIDIA GB10. **No Apple Silicon runtime test or speed benchmark was performed.** These are bounded smoke and numerical checks, not a comprehensive post-quantization quality, refusal, long-context, tool-use, or performance evaluation.

The parent BF16 checkpoint has limited 32-example capability checks: GSM8K flexible extraction was 25/32 for both source and edited checkpoints; IFEval strict prompt-level passes fell from 27/32 to 25/32. These are inherited BF16 results, **not measurements of this MLX quantization**. The prior refusal screening was keyword-based and does not establish zero refusals or unchanged general capabilities. See the parent repository for the evaluation and its caveats.

## Provenance and attribution

- Original model: [LiquidAI/LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B).
- BF16 source: [unsloth/LFM2.5-24B-A2B](https://huggingface.co/unsloth/LFM2.5-24B-A2B), revision `f8919e5dc304fd3c82b194963dc16a1a59f88623`.
- The inherited edit reproduces [AtomicChat's published recipe](https://huggingface.co/AtomicChat/LFM2.5-24B-A2B-Uncensored-GGUF-metrics), revision `78e022b6d4173524696c434d4c0f593929eb5dc4`, array `enru`: blocks 14-39 inclusive, strength 1.75, no row normalization. This is not a newly discovered direction.
- Editing used Heretic 1.4.0 through llm-abliterate with an LFM2 fused-MoE adapter. Conversion used upstream MLX LM 0.32.0 and MLX 0.32.4 without custom model code.
- `conversion_info.json` records source and output hashes, software versions, recipe, and validation scope. `SHA256SUMS` covers all published package files except itself.

## License and modification notice

Modified derivative, not an official Liquid AI release. The original **LFM Open License v1.0** applies; see `LICENSE` and `NOTICE`. The commercial-use limitation, including the USD 10 million annual-revenue threshold, still applies. This repository does not relicense the original model under Apache or MIT terms.
