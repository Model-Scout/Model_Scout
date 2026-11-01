---
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM2.5-8B-A1B
base_model_relation: quantized
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
- it
pipeline_tag: text-generation
tags:
- mlx
- mlx-lm
- llama.cpp
- gguf
- liquid
- lfm2.5
- moe
- abliterated
- reduced-refusal
- 4-bit
- q4_k_m
- q6_k
---

# LFM2.5-8B-A1B Abliterated

One repository for PocketAI Model Lab's validated MLX and GGUF releases. All
variants derive from the same architecture-aware, reduced-refusal BF16 master based on
[`LiquidAI/LFM2.5-8B-A1B`](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B).

## Available variants

| Variant | Location | Size | Status |
| --- | --- | ---: | --- |
| MLX mixed 4-bit | Repository root | 5,529,384,887 bytes | Validated compact release |
| GGUF Q4_K_M | `LFM2.5-8B-A1B-Abliterated-Q4_K_M.gguf` | 5,155,565,280 bytes | Validated compact/default release |
| GGUF Q6_K | `LFM2.5-8B-A1B-Abliterated-Q6_K.gguf` | 6,959,787,424 bytes | Validated quality release |

The root MLX configuration is the validated 4-bit model.

## Validation

| Check | MLX 4-bit | GGUF Q4_K_M | GGUF Q6_K |
| --- | ---: | ---: | ---: |
| Deterministic capability | 12/12 | 12/12 | 12/12 |
| PocketAI native tool routes | 8/8 | 8/8 | 8/8 |
| Held-out explicit refusals | 0/100 | 0/100 | 0/100 |
| Held-out completed answers | 100/100 | 99/100 | 100/100 |
| Evasive nonanswers | 0/100 | 1/100 | 0/100 |
| Truncated generations | 0/100 | 0/100 | 0/100 |

These are focused release gates, not broad benchmark scores or a guarantee of
correctness on every task.

## Artifact identities

| File | SHA-256 |
| --- | --- |
| `model-00001-of-00002.safetensors` | `caf52f36b791966d895676ef8e8e265aedcf60369715dcbca6fc22b213579714` |
| `model-00002-of-00002.safetensors` | `43e08e691df9316c02b6917bf6c3899562da08fa7bbd3b4473543aecc4839746` |
| `LFM2.5-8B-A1B-Abliterated-Q4_K_M.gguf` | `9b6b3f5127d279083ee95946af3f5c26e60d63ce07c249a260b3c4bdba6a4aa2` |
| `LFM2.5-8B-A1B-Abliterated-Q6_K.gguf` | `dbcad2ae002645910354f22eb26d69797f04c9a2ffe36687525a0052eb8bcebf` |

## MLX 4-bit usage

Install a current version of MLX-LM on an Apple Silicon Mac:

```bash
python -m pip install -U mlx-lm
```

```python
from mlx_lm import generate, load

repo = "PocketAiHub/LFM2.5-8B-A1B-Abliterated"
model, tokenizer = load(repo)

messages = [{"role": "user", "content": "Explain why seasons occur."}]
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)

print(
    generate(
        model,
        tokenizer,
        prompt=prompt,
        max_tokens=512,
        repetition_penalty=1.01,
        repetition_context_size=20,
    )
)
```

Most eligible weights use 4-bit affine quantization with group size 64.
Sensitive output paths, the tied token embedding/output matrix, dense and MoE
down projections, and layer 4 `conv.in_proj` retain 6-bit precision. MoE
routers remain 8-bit. The validated greedy/repetition profile is encoded in
`generation_config.json`.

## GGUF usage

Use a current llama.cpp build with LFM2.5 support:

```bash
llama-cli \
  -m LFM2.5-8B-A1B-Abliterated-Q4_K_M.gguf \
  -ngl 99 \
  -cnv
```

Q4_K_M is the compact/default variant and was calibrated with an importance
matrix collected from 512 direction-data prompts. Q6_K is the higher-quality
variant. Suggested starting requirements are 9 GB RAM / 6 GB VRAM for Q4_K_M
and 12 GB RAM / 8 GB VRAM for Q6_K, although actual use depends on context,
KV-cache, batching, and offload settings.

## Reduced-refusal parent

The BF16 parent used a projected refusal direction measured from 256 harmful
and 256 harmless prompts. The edit targeted 528 output tensors across the
hybrid attention, convolution, dense, and MoE expert architecture, using
source layer 16, destination layers 8–23, scale 2.25, and per-input-column norm
preservation.

This release is described as **abliterated** or **reduced-refusal**, not “fully
uncensored.” Zero explicit refusals on a finite held-out suite cannot prove
that every possible request will receive a substantive answer.

## Risks and limitations

- Refusal suppression reduces built-in safety behavior and can make harmful,
  offensive, deceptive, or illegal-use assistance easier to elicit.
- Quantization can introduce quality changes not covered by the release suite.
- The model can hallucinate and should not be trusted for medical, legal,
  financial, security-critical, or other high-stakes decisions.
- Users and downstream applications are responsible for safeguards and
  compliance with applicable law and the model license.

## License and attribution

This derivative is distributed under the
[LFM Open License v1.0](./LICENSE), inherited from Liquid AI's original model.
The license includes a commercial-use revenue limitation; review the complete
terms before using or redistributing the model.

- Original model: <https://huggingface.co/LiquidAI/LFM2.5-8B-A1B>
- Model Lab source: <https://github.com/PocketAIHub/pocketai-model-lab>
