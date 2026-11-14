---
license: apache-2.0
base_model: CohereLabs/command-a-plus-05-2026
base_model_relation: quantized
library_name: gguf
pipeline_tag: text-generation
tags:
  - gguf
  - llama.cpp
  - cohere2_moe
  - command-a
  - rocm
  - amd
  - mixture-of-experts
language:
  - en
  - fr
  - es
  - it
  - de
  - pt
  - ja
  - ko
  - ar
  - zh
  - ru
---

# Command A+ (05-2026) — GGUF (text-only)

GGUF quantizations of **[CohereLabs/command-a-plus-05-2026](https://huggingface.co/CohereLabs/command-a-plus-05-2026)** — a 218B-total / 25B-active Mixture-of-Experts model (`cohere2_moe`: 32 layers, 128 experts, 8 active, 4 shared experts, sigmoid routing).

These are **text-only** conversions. The upstream `command-a-plus-05-2026` is a vision-language model (`Cohere2VisionForConditionalGeneration` = a SigLIP vision encoder wrapping the Cohere2 MoE text backbone). llama.cpp's converter routes the text backbone via the `text_config` and produces a text-only GGUF; **the vision tower is not included.** If you need image input, this is not the right artifact.

Converted from the **BF16** master ([`CohereLabs/command-a-plus-05-2026-bf16`](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16)), not the W4A4 release.

## Files

| File | Quant | Size | BPW | Notes |
|---|---|---|---|---|
| `command-a-plus-Q6_K.gguf` | Q6_K | ~167 GiB | 6.56 | High-fidelity reference. No imatrix (barely moves the needle at Q6). |
| `command-a-plus-Q4_K_XL.gguf` | Q4_K_M + pins | ~128 GiB | 5.05 | Daily driver. imatrix + per-tensor bumps (see below). |
| `command-a-plus-Q3_K_XL.gguf` | Q3_K_M + pins | ~108 GiB | 3.97 | Fits a **128 GB** box (e.g. 4× 32 GB). imatrix + q6_K pins (see below). |

All are split into shards (`*-00001-of-0000N.gguf`); point llama.cpp at the first shard and it loads the rest automatically.

### Q4_K_XL recipe

Base `Q4_K_M` with the **format-critical, always-active** tensors pinned to `q8_0`, while the bulk routed-expert gate/up/down weights stay `Q4_K` (that's where the size lives):

- `token_embd` (tied output) → `q8_0`
- attention `attn_{q,k,v,output}` → `q8_0`
- router `ffn_gate_inp` → `q8_0`
- shared experts `ffn_{gate,up,down}_shexp` → `q8_0`

The imatrix was built on a diverse ~310k-token calibration set (prose, multi-language code, tool-call JSON, chat-token formatting) with ~99% expert coverage. We deliberately did **not** pin the routed `ffn_down_exps` to `q8_0` — that would push the file to ~156 GiB (near Q6_K) and defeat the daily-driver purpose.

### Q3_K_XL recipe

Base `Q3_K_M` with the same always-active tensors pinned to **`q6_K`** (near-lossless and ~3 GB cheaper than `q8_0` at this size), routed experts at the `Q3_K_M` default:

- `token_embd` → `q6_K`
- attention `attn_{q,k,v,output}` → `q6_K`
- shared experts `ffn_{gate,up,down}_shexp` → `q6_K`
- router `ffn_gate_inp` → **left f32** (llama.cpp's default — it's tiny and critical for MoE expert selection; don't downgrade it)

Same imatrix as above. Lands at ~108 GiB so it fits a 128 GB box with headroom. **KV is not the constraint** even at this size: GQA (8 KV heads) + sliding-window attention on 24 of 32 layers keep the cache at ~1.5 GB @ 16k and ~7.4 GB @ 128k context — so the remaining ~20 GB supports 200k+ tokens.

## Performance

Measured with `llama-bench` on **8× AMD Instinct MI100 (gfx908, 256 GB total VRAM)**, ROCm 7.1, flash-attention on, fully resident:

| Quant | pp512 / pp2048 (t/s) | decode @0 / @4k / @16k ctx (t/s) |
|---|---|---|
| Q6_K | 280 / 299 | 29.1 / 27.9 / 27.4 |
| Q4_K_XL | 387 / 410 | 33.3 / 31.6 / 31.0 |

Decode is bandwidth-bound and barely degrades with context depth.

## Running on multi-GPU AMD (important)

The MI100 box used here is two 4-card Infinity-Fabric hives; spanning >4 cards forces P2P **across** hives over PCIe, which segfaults the HIP runtime (`cudaMemcpyPeerAsync`). If you hit a crash loading across many AMD GPUs, build llama.cpp with peer copies disabled (routes cross-device transfers through host RAM — negligible cost at decode with `-sm layer`):

```bash
HIPCXX="$(hipconfig -l)/clang" cmake -B build -DGGML_HIP=ON \
  -DAMDGPU_TARGETS=gfx908 -DCMAKE_BUILD_TYPE=Release \
  -DGGML_CUDA_NO_PEER_COPY=ON
cmake --build build -j
```

(`iommu=pt` on the kernel cmdline is good practice for multi-GPU DMA but did **not** fix the cross-hive case on its own.)

### RDNA2 (Navi-21 / gfx1030) — e.g. running Q3_K_XL on 4× 32 GB

Build for the right target and keep peer copies off (consumer/workstation RDNA2 generally can't do PCIe P2P — same crash class as the MI100 cross-hive issue):

```bash
HIPCXX="$(hipconfig -l)/clang" cmake -B build -DGGML_HIP=ON \
  -DAMDGPU_TARGETS=gfx1030 -DCMAKE_BUILD_TYPE=Release \
  -DGGML_CUDA_NO_PEER_COPY=ON
cmake --build build -j
```

Then apply the tool-call patch (below) the same way. Expect lower decode throughput than CDNA (MI100) — Navi-21 has less memory bandwidth — but Q3_K_XL is smaller, which helps the bandwidth-bound decode. `-fa on` works on RDNA2.

### Tuning notes (measured on MI100; re-verify on your hardware)

- **rocWMMA flash-attention** (`-DGGML_HIP_ROCWMMA_FATTN=ON`, needs `librocwmma-dev`): small win on CDNA (~+1.3% decode, no prefill cost). Untested on RDNA2.
- **`-DGGML_CUDA_FORCE_MMQ=ON`: avoid** — regressed prompt-eval ~13% on the big MoE matmuls here, no decode benefit.
- **KV cache quantization (`q8_0`): not worth it** — ~6% slower decode and KV is already tiny on this model; only use under genuine memory pressure.

## Tool calling (requires a small llama.cpp patch)

The model emits correct tool calls in Cohere's native format
(`<|START_THINKING|>…<|END_THINKING|><|START_ACTION|>[{"tool_call_id":…,"tool_name":…,"parameters":…}]<|END_ACTION|>`),
but current llama.cpp has **no Cohere2 parser**, so `/v1/chat/completions` returns HTTP 500 ("Failed to parse input at pos 0") instead of OpenAI `tool_calls`.

Apply the included **[`cohere2-chat-handler.patch`](./cohere2-chat-handler.patch)** to `common/chat.cpp` and rebuild:

```bash
cd llama.cpp
git apply /path/to/cohere2-chat-handler.patch
cmake --build build -j --target llama-server
```

It adds a `cohere2` chat handler (detected from the template) that maps the native action format onto OpenAI `tool_calls` via `standard_json_tools`, extracts the thinking block into `reasoning_content`, and handles the tool-result → final-response turn. Validated for single tool calls, parallel tool calls, and the full agent loop.

> The included [`chat_template.jinja`](./chat_template.jinja) is the model's own template (already embedded in the GGUF); it's provided for reference. Tool-call **parsing** is done by the C++ handler above, not the template.

## Serving

```bash
./build/bin/llama-server -m command-a-plus-Q4_K_XL-00001-of-0000N.gguf \
  -ngl 999 -fa on -c 16384 --jinja --reasoning-format deepseek \
  --host 0.0.0.0 --port 8080
```

- `--jinja` applies the Cohere chat template (special tokens, citations, tool formatting).
- `--reasoning-format deepseek` surfaces the `<|START_THINKING|>` block as `reasoning_content`.

## Provenance / reproduction

- Converted with llama.cpp (cohere2_moe support; converter routes the VLM's `text_config` to the `Cohere2MoeForCausalLM` handler).
- **transformers from source** is required at conversion time — the stock release can't load Cohere's `TokenizersBackend` tokenizer class.

## License

Apache-2.0, inherited from the base model. Includes Cohere's attribution. You are responsible for complying with the base model's terms.
