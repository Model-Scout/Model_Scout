---
license: apache-2.0
library_name: transformers
pipeline_tag: image-text-to-text
base_model: OpenGVLab/InternVL3_5-8B-HF
base_model_relation: quantized
language:
  - en
  - zh
  - ko
tags:
  - internvl
  - internvl3.5
  - vision-language
  - multimodal
  - vllm
  - compressed-tensors
  - awq
  - int4
  - w4a16
---

# InternVL3.5-8B-HF AWQ W4A16 (group size 128)

A compressed-tensors **AWQ W4A16** quantization of
[OpenGVLab/InternVL3_5-8B-HF](https://huggingface.co/OpenGVLab/InternVL3_5-8B-HF),
built so that an 8B vision-language model fits on a 12 GB consumer GPU with vLLM.

**17.06 GB → 6.31 GiB** (−60%).

Companion builds of the 4B model from the same pipeline:

- [hsmin92/internvl35-4b-awq-w4a16-g128](https://huggingface.co/hsmin92/internvl35-4b-awq-w4a16-g128) — AWQ W4A16, validated on an RTX 3070 8 GB
- [hsmin92/internvl35-fp8](https://huggingface.co/hsmin92/internvl35-fp8) — FP8 Dynamic

## ⚠️ What has and has not been verified

The quantization host was an **RTX 3070 8 GB**, which cannot load this
checkpoint (6.31 GiB of weights leaves no room for a KV cache on that card).

**Verified**

- Checkpoint structure: 1,597 tensors, 252 packed INT4 modules with matching
  scale / zero-point tensors
- No packed weights under `vision_tower`, `multi_modal_projector`, `lm_head`,
  or the embeddings — the protection regexes did what they were meant to
- No NaN or Inf in any of the 504 scale / zero-point tensors
- `config.json` consistent with the base model
  (`layers=36`, `kv_heads=8`, `hidden=4096`, `image_token_id`, `image_seq_length`)

**Not verified**

- **Serving.** This checkpoint has never been loaded by vLLM.
- **Accuracy.** No benchmark against the BF16 base model or the 4B builds.

Treat the serving configuration below as a starting point and confirm it
against your own startup logs.

## Quantization scope

Quantized to asymmetric INT4:

- **252** language decoder `Linear` modules
  (144 attention: `q_proj` / `k_proj` / `v_proj` / `o_proj`,
  108 MLP: `gate_proj` / `up_proj` / `down_proj`)
- Scheme: `W4A16_ASYM`, algorithm: AWQ (`duo_scaling`, `n_grid=20`)
- Weight format: `pack-quantized`, group size **128**
- Activations: **not** quantized (A16)

Kept in BF16: vision tower, multimodal projector, input embeddings, `lm_head`,
normalization layers.

Generated from base-model revision:

```text
741a7d03020411e666c6109218ab71e08151ef86
```

## Calibration

AWQ fits per-channel scales against a calibration set, so the calibration
distribution matters.

| | |
|---|---|
| Dataset | `lmms-lab/flickr30k` |
| Samples | 128 (0 skipped) |
| Image size | 448×448, 1 patch per sample |
| Prompts | generic English / Korean scene-description instructions |

**This is a general-purpose photo set.** If your target domain is far from
everyday photography — industrial inspection, thermal imagery, medical,
document OCR, CCTV at unusual angles — re-run AWQ with in-domain calibration
images rather than assuming this checkpoint transfers.

## Serving with vLLM

Sized for a **12 GB** card (RTX 4070 and similar).

```bash
vllm serve hsmin92/internvl35-8b-awq-w4a16-g128 \
  --served-model-name internvl35-8b-awq \
  --dtype bfloat16 \
  --max-model-len 8192 \
  --max-num-seqs 8 \
  --max-num-batched-tokens 4096 \
  --limit-mm-per-prompt '{"image":2,"video":0}' \
  --gpu-memory-utilization 0.85 \
  --kv-cache-memory-bytes 2880M \
  --trust-remote-code \
  --enable-auto-tool-choice \
  --tool-call-parser hermes
```

Budget behind those numbers (12,288 MiB card):

```text
weights                        6,520 MiB   (6,460 MiB on disk)
context + activation peak        750 MiB
CUDA graphs                      150 MiB
KV cache (pinned, fp16)        2,880 MiB   -> 20,480 tokens
────────────────────────────────────────
vLLM process                 ~10,300 MiB   -> utilization 0.838
```

KV costs **144 KiB/token** (`2 × 36 layers × 8 KV heads × 128 head_dim × 2 B`),
so 20,480 tokens holds 2.5 full-length 8,192-token requests.

**On first start, check the log and adjust:**

```bash
docker compose logs vlm-prod | grep -E "Model loading took|GPU KV cache size"
```

If `Model loading took` exceeds 6,520 MiB, reduce `--kv-cache-memory-bytes` by
the difference. If startup is refused with `Free memory ... is less than
desired GPU memory utilization`, lower `--gpu-memory-utilization` — the figure
that matters is the one in that error message, not what host `nvidia-smi` shows.

### Flags that are not obvious

**`--dtype bfloat16` — do not use `half`.** On the sibling FP8 build, `half`
produced a server that started, returned HTTP 200 from `/health`, passed its
container health check, and answered every request with `!!!!!!!!` (dequant
overflow → NaN logits → argmax picks token 0). It fails silently. This build is
INT4 rather than FP8 so the same overflow is not expected, but the checkpoint
declares `bfloat16` and there is no reason to deviate. Always send a real
request after a configuration change, not just a health check.

**`--max-num-batched-tokens` is not a VRAM knob.** It also sizes the multimodal
encoder cache, and the vLLM default of 2048 rejects large images on any card:

```text
image item with 2816 embedding tokens, which exceeds the
pre-allocated encoder cache size 2048
```

InternVL dynamic tiling allows up to 12 patches plus a thumbnail, so one image
can reach **3,329 embedding tokens**. Use at least 4096.

**`--max-num-seqs`: the default of 128 costs throughput.** When more concurrent
requests arrive than the KV cache holds, vLLM preempts and recomputes and
throughput falls below what a smaller limit achieves. Measured on the 4B build
(~1,084 prompt tokens/request, 16,128-token cache): at 16 concurrent requests,
`--max-num-seqs 128` took 11.82 s while `8` took 6.54 s. Pick a limit the cache
can sustain — not the `Maximum concurrency` figure in the startup log, which
assumes every request fills the full context window.

**Tool-call flags are needed even without tool calling.** They are required for
the server to *accept* requests carrying a `tool_choice` field; Open WebUI sends
`tool_choice: "auto"` by default. Actual tool calling still does not work — the
bundled `chat_template.jinja` has no tool rendering, so `tools=[...]` is
silently ignored.

### Image token cost is driven by aspect ratio, not size

Tile count comes from the aspect ratio, so cost is not monotonic in resolution.
Measured on the 4B build (same processor and tiling config):

| Input size | Image tokens | Tiles |
|---|---|---|
| 448×448 | 257 | 1 |
| 896×448 | 769 | 3 |
| 960×544 | 769 | 3 |
| 800×450 | 769 | 3 |
| **200×150** | **3,329** | **13** |
| 4000×300 | 3,329 | 13 |

A 200×150 crop costs **4.3× more** than an 800×450 image, because 4:3 maps
exactly onto a 4×3 tile grid and the crop is upscaled to 1792×1344 for no added
information. When sending region crops, letterbox them into a fixed 448×448
canvas (preserving aspect ratio, no upscaling) to keep cost constant.

### Structured output

If you parse the response programmatically, constrain it with a JSON schema via
`response_format` instead of scraping prose. **Put `maxLength` on every free
text field** — without an upper bound a model can ramble inside the string until
it hits `max_tokens`, returning truncated JSON.

## Limitations

- A quantized derivative, not an independently trained model.
- **Never loaded by an inference engine** — see the verification section above.
- **No accuracy benchmark.** 4-bit weights and general-purpose calibration are
  both reasons to expect degradation on hard, out-of-domain inputs.
- The vision tower and output head remain BF16 and are a meaningful share of
  the loaded weights, so the reduction is smaller than 4/16 would suggest.
- The bundled `chat_template.jinja` has no tool-calling support.
- VRAM figures depend on driver, desktop applications, context length,
  multimodal limits, and vLLM version.

## Attribution and license

A quantized derivative of
[OpenGVLab/InternVL3_5-8B-HF](https://huggingface.co/OpenGVLab/InternVL3_5-8B-HF).
The original project and this derivative are distributed under the Apache-2.0
license. Review the upstream model card for original training details,
limitations, and citation information.

## Citation

```bibtex
@article{wang2025internvl3_5,
  title={InternVL3.5: Advancing Open-Source Multimodal Models in Versatility, Reasoning, and Efficiency},
  author={Wang, Weiyun and Gao, Zhangwei and Gu, Lixin and Pu, Hengjun and Cui, Long and Wei, Xingguang and Liu, Zhaoyang and Jing, Linglin and Ye, Shenglong and Shao, Jie and others},
  journal={arXiv preprint arXiv:2508.18265},
  year={2025}
}
```
