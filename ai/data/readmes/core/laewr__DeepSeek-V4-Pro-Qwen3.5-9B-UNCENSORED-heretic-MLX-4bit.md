---
license: apache-2.0
base_model: xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic
base_model_relation: quantized
library_name: mlx
tags:
  - mlx
  - qwen3_5
  - qwen3.5
  - heretic
  - uncensored
  - abliterated
  - reasoning
  - math
  - stem
  - 4-bit
  - mlx-serve
language:
  - en
  - zh
  - ja
  - ko
  - es
  - ru
pipeline_tag: text-generation
---

# DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic — MLX 4-bit (text-only)

An MLX conversion of
[`xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic`](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic),
quantized to 4-bit affine (group size 64) with `mlx_lm.convert`, for Apple Silicon.

**There is no other MLX build of this checkpoint.** The `mlx-community/DeepSeek-V4-Pro-Qwen3.5-9B-*`
packs are conversions of the *non-abliterated* `Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B` base — different weights.

## How this differs from `xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic`

**Same weights, different container.** No retraining, no merging, no extra uncensoring — the
abliteration (Heretic v2 ARA over layers 9–24) and the DeepSeek-V4-Pro distillation are exactly
the ones in the upstream checkpoint. The refusal behavior is identical.

| | upstream `xtools-at/…-UNCENSORED-heretic` | this repo |
|---|---|---|
| Format | HF transformers BF16 safetensors, 4 shards | MLX safetensors, 1 file |
| Precision | BF16 (16 bits/weight) | 4-bit affine, group 64 (≈4.5 effective bits) — **lossy** |
| Size | 18.85 GB | 5.04 GB |
| Tensors | 760 | 927 (each quantized weight splits into `weight` + `scales` + `biases`) |
| Language weights | 427 tensors, 8.954 B params | 427 tensors, 8.953 B params + 1.1 M unquantized norms — **nothing dropped** |
| **Vision tower** | 333 tensors, 0.456 B params (0.85 GiB) + `preprocessor_config.json`, `video_preprocessor_config.json` | **removed** — `mlx_lm.convert` strips `model.visual.*` |
| Modality | image-text-to-text | **text only** |
| MTP head | none (the upstream upload dropped the base's 15 `mtp.*` tensors) | none — unchanged |
| `config.json` `model_name` | `unsloth/Qwen3.5-9B` (inherited from its own base) | full repo name (metadata fix only) |
| Extra tokenizer files | — | `vocab.json`, `added_tokens.json`, `special_tokens_map.json` copied from upstream so `transformers` can load the tokenizer |
| Runs on | vLLM / SGLang / transformers (llama.cpp via its GGUF siblings) | MLX: `mlx-lm`, MLX-Serve, on Apple Silicon |

**What you lose by using this repo:** the vision tower (image input), and a small amount of
precision (BF16 → 4-bit affine). **What you gain:** 3.7× smaller, and — because decode is
memory-bandwidth bound — roughly 3.7× less weight traffic per generated token. Measured on
M5 Max: 105.6 tok/s plain, 179.3 tok/s with a DFlash drafter attached (see below).

If you need images or the original precision, use the upstream repo, or re-convert with
`mlx_vlm.convert` (keeps vision, ~5.9 GiB) / `--q-bits 6` (~7.5 GiB) or `8` (~9.4 GiB).

## What this is

The upstream model is a Qwen3.5-9B fine-tune distilled from DeepSeek-V4-Pro "Max Effect" outputs
(~250K math/STEM samples, SFT then a light GSPO RL stage, **no coding data**), subsequently
decensored with Heretic v2 (Arbitrary-Rank Ablation over layers 9–24; refusals 100/100 → 3/100,
KL 0.0422).

Lineage:

```
Qwen/Qwen3.5-9B-Base
  └─ Qwen/Qwen3.5-9B
      └─ Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B          (distill SFT + GSPO)
          └─ xtools-at/…-UNCENSORED-heretic           (Heretic v2 ARA, layers 9–24)
              └─ this pack                            (MLX 4-bit affine gs64, text-only)
```

## What's in the box

| | |
|---|---|
| Parameters | 9.41 B (dense, non-MoE) |
| Architecture | `Qwen3_5ForConditionalGeneration` / `qwen3_5` — hybrid: 3× `linear_attention` + 1× `full_attention` per 4 layers (32 layers total) |
| Quantization | 4-bit affine, `group_size: 64` |
| Size | 4.7 GB |
| Context | 262 144 tokens (native M-RoPE, no YaRN needed) |
| Modalities | **text only** — the vision tower (333 tensors) was stripped by `mlx_lm.convert` |
| MTP head | **absent** — the upstream heretic checkpoint dropped the base's 15 `mtp.*` tensors |
| Tokenizer | 248 320 vocab, chat template supports tool-call XML and `enable_thinking` |

## Measured performance

Apple M5 Max, 128 GB unified memory, MLX-Serve 26.11.2 (mlx 0.32.5), same math prompt,
`temperature: 0`, median of 3:

| build | decode, short prompt | decode, 5K prompt | context | speculation |
|---|---|---|---|---|
| upstream GGUF Q4_K_M, `--mlx-gguf` | 87.7 tok/s | — | 132 096 (auto-capped) | none possible |
| this pack, no drafter | 105.6 tok/s | — | 262 144 | PLD only |
| this pack + `z-lab/Qwen3.5-9B-DFlash` | 172.6 tok/s | ~250 tok/s | 262 144 | DFlash, `spec_exact: true` |
| **this pack + `guglxni/Qwen3.5-9B-abliterated-DFlash`** | **179.3 tok/s** | **~281 tok/s** | 262 144 | DFlash, `spec_exact: true` |

Interleaved A/B (unload/reload between arms, median of 3). The abliterated drafter wins in both
regimes — its trunk was abliterated too, so its hidden states track this target better
(`per_draft` 16.4% vs 15.5% short, 30.2% both at 5K).

**Block size:** the drafter ships `block_size: 16` and that is the right value. On M5-class
hardware the NAX verify tile pads widths 8–16 to the same 16-row weight stream, so 8/12/16 cost
the same per round while narrower blocks accept fewer tokens (measured: 16 → 185.6, 8 → 185,
4 → 162, 2 → 104 tok/s; block 2 is *slower than no drafter at all*).

The GGUF route is slower because MLX-Serve's `--mlx-gguf` engine dequantizes per token, and it
cannot attach a drafter at all (`loadGguf` nulls `sch.drafter` / `sch.dflash`).

## Usage

### MLX-Serve

```bash
mkdir -p ~/.mlx-serve/models/laewr
# put this repo at ~/.mlx-serve/models/laewr/<repo-name>/
curl -X POST http://127.0.0.1:11234/v1/models/rescan
curl -X POST http://127.0.0.1:11234/v1/load-model \
  -H 'Content-Type: application/json' \
  -d '{"model":"laewr/<repo-name>"}'
```

### With a DFlash drafter (recommended, ~1.7× decode)

```bash
# best measured pairing
hf download guglxni/Qwen3.5-9B-abliterated-DFlash --local-dir /tmp/dflash
mkdir -p ~/.mlx-serve/models/laewr/<repo-name>/drafter
cp /tmp/dflash/{model.safetensors,config.json} ~/.mlx-serve/models/laewr/<repo-name>/drafter/
# then unload + reload the model — a server restart is NOT needed
```

`z-lab/Qwen3.5-9B-DFlash` also works and is ~4% slower at short context. Both satisfy the
contract (`block_size` + `mask_token_id` + `target_layer_ids`, `num_target_layers: 32`).

The drafter is resolved at **load** time from `<model_dir>/drafter/`, so an
unload/reload picks it up. `/v1/models` reports `drafter_loaded: true` when bound.
Neither drafter is included in this repo — they are third-party work (also Apache-2.0).

### mlx-lm

```python
from mlx_lm import load, generate
model, tokenizer = load("laewr/<repo-name>")
print(generate(model, tokenizer, prompt="…", max_tokens=512))
```

## Thinking mode

`enable_thinking` is **off by default** in this chat template. For math/STEM work it must be
turned on explicitly, or the model answers in a handful of tokens and often gets it wrong:

```json
{"chat_template_kwargs": {"enable_thinking": true}}
```

## Caveats

- **Reasoning length is unstable.** The same prompt at `temperature: 0` produced 452 / 515 / 617 /
  1362 completion tokens across runs. This is the model's own instability (upstream card warns of
  it on hard or vague tasks) plus hybrid prefix-cache non-determinism — not a speculative-decoding
  artifact; `spec_exact` stays true and the answer was correct each time.
- **No coding ability.** No coding data was in the distillation set; tool-use is only incidental
  cross-domain transfer.
- **No vision.** Use `mlx_vlm.convert` if you need the image tower.
- **No MTP.** The upstream checkpoint ships zero `mtp.*` tensors. Grafting the base's 15 tensors
  is possible but MTP outranks DFlash in MLX-Serve's draft priority, so a low-acceptance head
  would suppress a working drafter.
- Benchmarks from the upstream card come from partial MMLU-Pro subsets (500 questions/subject) and
  a different backend for GSM8K; they are not a full capability or safety evaluation.
- This is a decensored model. Verify high-stakes outputs independently.

## Conversion

```bash
python -m mlx_lm.convert \
  --model xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic \
  --mlx-path ./heretic-mlx-4bit \
  -q --q-bits 4 --q-group-size 64
```

`mlx_lm` ≥ 0.30.7 is required (Qwen3.5 support); this pack was built with 0.32.2.

## License

Apache-2.0, inherited from the upstream checkpoint. Attribution to `xtools-at`,
`Jackrong`, `unsloth`, and `Qwen` for the weights; the MLX conversion is offered under the
same terms.
