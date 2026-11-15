---
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM3-1.7B/blob/main/LICENSE
base_model: LiquidAI/LFM3-1.7B
library_name: litert-lm
pipeline_tag: text-generation
tags:
  - litert-lm
  - litert
  - android
  - on-device
  - edge
  - lfm3
  - liquid
  - int4
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

# LFM3-1.7B → LiteRT-LM (int4) + Android app

[LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) ported to Google's
[LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) runtime, plus a working
Android chat app built on it.

This is the first LiteRT-LM port of Liquid AI's **tri-hybrid** architecture:
24 layers of gated short convolutions, sliding-window attention and partial-RoPE
full attention, with per-head attention gates and sandwich norms. The
`litert-torch` exporter did not know how to export it before this work — the
`port/` directory contains everything needed to reproduce the bundle.

| | |
| :--- | :--- |
| Model file | [`lfm3-1.7b-int4.litertlm`](./lfm3-1.7b-int4.litertlm) |
| Size | **848 MB** (int4 weights, dynamic activation fp32) |
| Context | **4096** tokens (exported cache length; LFM3 itself supports 256K) |
| Prefill signature | `prefill_128` (128-token chunks, right-padded by the runtime) |
| Backends | CPU (XNNPACK) and GPU; NPU untested |
| Thinking | yes (`<think>` channel, surfaced as `thought`) |
| Function calling | template-level (LFM3 XML tool-call syntax) |
| Languages | 16 (inherits from the base checkpoint) |

## Other builds

- [`cheesefelys/LFM3-1.7B-litertlm-fp32`](https://huggingface.co/cheesefelys/LFM3-1.7B-litertlm-fp32) —
  the same checkpoint and the same port, **unquantized** (6.92 GB fp32). It is the
  graph measured against PyTorch (logit cosine 0.9997 vs 0.8877 for the int4
  build); use it as a reference or on desktop, not on a phone.

## Files

```
lfm3-1.7b-int4.litertlm     the LiteRT-LM bundle (tflite prefill+decode, int4,
                            HF tokenizer, LlmMetadata, ExecutorMetadata)
port/                       the port: litert-torch model extension, chat
                            template, LlmMetadata, export + validation scripts
android/                    Android app source (Kotlin + Compose) and a debug APK
LICENSE                     LFM Open License v1.0 (unchanged, from the base model)
```

## Quick start

### Desktop CLI

```bash
uv tool install litert-lm

litert-lm import ./lfm3-1.7b-int4.litertlm --name lfm3
litert-lm run lfm3 --prompt "Explain tri-hybrid architectures in two sentences."
```

### Python

```python
import litert_lm

engine = litert_lm.Engine("lfm3-1.7b-int4.litertlm", backend=litert_lm.Backend.CPU())
with engine.create_conversation() as conversation:
    for chunk in conversation.send_message_async("Hello!"):
        print(chunk, end="", flush=True)
```

### Google AI Edge Gallery

Gallery can list and run this bundle **without rebuilding the app**: it prefers a
local allowlist over its online catalogue, so

```bash
adb push gallery/model_allowlist_test.json /data/local/tmp/model_allowlist_test.json
adb shell am force-stop com.google.ai.edge.gallery
```

makes `LFM3-1.7B-int4` appear next to Google's official models (888.9 MB
download, pinned to this revision). See [`gallery/README.md`](./gallery/README.md)
for details and `gallery/make_allowlist.py` to regenerate the file against a
newer official catalogue.

### Android app

`android/LFM3-LiteRT-LM-debug.apk` is a debug build of the included Compose app
(minSdk 28, targetSdk 35). It downloads the bundle from this repository on first
launch, streams the reply token by token, shows the `<think>` reasoning in a
collapsible block, and lets you switch CPU/GPU and sampling settings. Build it
yourself with:

```bash
cd android && JAVA_HOME=<jdk21> ANDROID_HOME=<sdk> ./gradlew :app:assembleDebug
```

The runtime dependency is the stock Google Maven artifact
`com.google.ai.edge.litertlm:litertlm-android:0.18.1` — no custom runtime build is
needed, the port is entirely in the model bundle (metadata + template + exported
graph).

## What the port had to add

LFM3's `config.layer_types` mixes three operators per layer:

```
['conv', 'conv', 'full_attention', 'conv', 'sliding_attention', 'conv', ...]
```

| layer | operator | state |
| :--- | :--- | :--- |
| `conv` | gated depthwise short conv, kernel 7 | 6-wide rolling window (`conv_L_cache - 1`) |
| `sliding_attention` | 16 heads / 4 KV heads, RoPE θ=1e4, window 256 | KV cache |
| `full_attention` | 16 heads / 4 KV heads, partial RoPE (64 of 128 dims, θ=1e6) | KV cache |

Plus QK-RMSNorm, a per-head sigmoid gate on attention output, and sandwich norms
around both sublayers. Attention projects with `o_proj`.

1. **`port/litert_torch_ext/lfm3/`** is a `ModelExtension` for `litert-torch`'s
   `export_hf` pipeline. The generic pipeline already derives the three
   `StateBuffer` kinds from `layer_types`, and the LFM3 attention, gates and
   partial-RoPE math trace directly out of the checkpoint's own
   `modeling_lfm3.py`. The missing piece was the short convolution: Hugging Face
   convolves `concat(conv_state, x)`, which relies on its `update_conv_state`
   returning the concatenation, while LiteRT keeps a fixed 6-wide
   `kv_cache_c_{i}` buffer. `short_conv.py` re-implements `y = C * conv(B * x)`
   on that buffer with the shared `short_conv` composite, and handles LiteRT-LM's
   **right-padded** prefill so the rolling state ends at the last valid token
   (a padded prefill otherwise zeroes the state — see the validation section).
2. **The `conv` mask entry.** `Lfm3Model.forward` indexes a per-layer-type mask
   mapping, so it needs a `conv` key that the generic exportables do not build.
   `exportables.py` subclasses the prefill/decode exportables and adds the 2-D
   padding mask there; it is folded into the graph and never reaches the
   signature.
3. **`port/models/lfm3/`** carries the canonical LiteRT-LM chat template
   (minijinja-compatible: `<|im_start|>` turns, `<tools>` block, XML tool calls,
   `<think>` channel) and the `LlmMetadata` that embeds it along with stop
   tokens (`<|im_end|>`, `<|endoftext|>`), sampler defaults (top-p 1.0, k 50,
   temp 0.1) and `supports_thinking` / `supports_function_calling`.

Reproduction steps, exact versions and the memory gotcha
(`--experimental_lightweight_conversion=True`; `bfloat16` tracing is rejected by
the converter) are in [`port/README.md`](./port/README.md).

## Cross-platform

The published bundle was re-run unchanged on a second machine — Windows 11,
Ryzen 7 4800H, 32 GB, GTX 1660 Ti — with no rebuild:

- **CPU**: loads in 0.7–2.1 s, answers in 1.3 s (short) to 7.3 s (prose).
- **GPU (WebGPU)**: `Backend.GPU()` works out of the box, loads in 4.8 s and
  decodes a short answer in **0.3 s** (~4× the CPU step).
- **Greedy parity**: `17 * 23` → `391` on Windows CPU (default, FLOAT32 and
  FLOAT16 activation dtypes) and on Windows GPU, matching the Linux run.
- **Multi-turn** in one conversation works (recalls a name from two turns back).

Two things came out of that run and are documented in
[`docs/cross-platform-validation.md`](./docs/cross-platform-validation.md):
the conversion stack itself cannot run on Windows (`litert-converter` ships only
macOS-arm64 and Linux-x86_64 wheels, and there is no WSL on that box), and
starting a *second* conversation on the same `Engine` after a long unrelated
prompt degrades output on the Windows build — use a fresh `Engine` per
conversation there. Scripts and raw logs are in `docs/windows/`.

## Validation

- **Bit-exact on a controlled model.** A 4-layer / 128-hidden LFM3 with all three
  layer types, random weights, exported through the same path: prefill + 6
  greedy decode steps match PyTorch with `max|diff| = 0.000000`; a chunked
  prefill (two 16-token calls, then 4 decode steps) matches token for token; a
  padded prefill (5 real tokens in a 16-wide window) matches too.
- **Real model, unquantized graph.** The same 1.7B export without quantization,
  compared against the bf16 PyTorch reference (`port/verify_quantized.py`,
  teacher-forced so both sides see the same tokens):

| check | fp32 graph | shipped int4 bundle |
| :--- | :--- | :--- |
| decode steps compared | 6 | 6 |
| top-1 agreement with bf16 PyTorch | 6/6 | 6/6 |
| logit cosine similarity | 0.9997 | 0.8877 |
| relative logit error (max delta / max ref) | 0.018 | 0.427 |
| greedy continuation of `The capital of France is` | ` Paris.\n\nThe capital of Japan is` | same text |

- **Runtime parity.** With greedy sampling (`top_k=1`) the shipped bundle, an
  int8 export of the same checkpoint and the fp32 graph all answer
  `17 * 23` with `391`, and produce equivalent prose for open-ended prompts.
  Sampling (`top_k=50`, `temperature=0.1`, the checkpoint's own defaults) does
  make int4 and fp32 differ on single samples — that is sampler variance, not a
  graph defect.
- **Older per-tensor recipes.** `dynamic_wi8_afp32` (per-tensor dynamic int8)
  was measurably less faithful than `dynamic_wi4c_afp32` (per-channel int4) on
  the padded-prefill harness (cosine 0.66 vs 0.89), so the smaller per-channel
  int4 bundle is the one published here.

## Limitations

- **Text only.** This is the 1.7B text checkpoint; LFM3 vision/audio/omni
  variants are separate models and not included.
- **4096-token context** in this bundle. Raising it means re-exporting with a
  larger `--cache_length` (KV memory grows linearly).
- **Tool calls are text.** The LFM3 XML syntax is in the prompt and the model
  emits it, but the runtime's generic data processor does not turn it into
  structured `ToolCall`s, so callers parse it themselves.
- **No packed documents** across conv layers (multiple documents in one prefill
  with restarting `position_ids`); LiteRT-LM does not use that path.
- **NPU is untested**; CPU (XNNPACK) and GPU (WebGPU) are both verified on x86-64
  Windows, CPU on Linux.

## License

The port code in `port/` and the Android app in `android/` are Apache-2.0
(they are derived from Google's LiteRT-LM / litert-torch, Apache-2.0). The model
weights are **not** relicensed: they remain under the **LFM Open License v1.0**
of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B/blob/main/LICENSE),
which permits research and limited commercial use. Read it before deploying.

LiteRT-LM and LiteRT are trademarks of Google LLC. LFM and Liquid AI are
trademarks of Liquid AI, Inc. This repository is an independent conversion and is
not endorsed by either company.
