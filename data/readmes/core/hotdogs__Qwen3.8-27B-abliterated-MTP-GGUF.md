---
license: apache-2.0
base_model: hotdogs/Qwen3.8-27B-abliterated
pipeline_tag: text-generation
library_name: gguf
tags:
- qwen3_5
- abliterated
- uncensored
- gguf
- llama.cpp
- mtp
- multi-token-prediction
- image-text-to-text
language:
- en
- zh
- th
---



# Qwen3.8-27B-Abliterated (GGUF, MTP-capable)

GGUF quantization of **[hotdogs/Qwen3.8-27B-abliterated](https://huggingface.co/hotdogs/Qwen3.8-27B-abliterated)** — the training-free abliterated (refusal-removed) build of `Qwen/Qwen3.8-27B` — converted for **llama.cpp** with the **MTP (Multi-Token Prediction) head preserved**.

> **Status: testing / development.** This is an early GGUF upload for evaluation. It has **not yet been calibrated with an imatrix** — the low-bit `Q4_K_M` quality is expected to improve once an imatrix is added (see *Roadmap*). Feedback welcome.

---

# deepseek-harness 
```
mkdir -p data

docker run -d \
  --name deepseek \
  -p 2222:22 \
  -p 3080:8080 \
  -e SSH_PASSWORD=your-password \
  -e DSH_USER=root \
  -e DSH_PASSWORD=your-password \
  -v $(pwd)/data:/root/ \
  --restart unless-stopped \
  nutboy02/deepseek-harness:latest
```



# Latest bug fixes as of 2026-08-16 


## Quantized "mixed" builds — quality vs f16

These `-mixed` quants use a **hybrid precision recipe** to get closer to the
f16 reference: the token-embedding and all output tensors are kept at `q8_0`
while the rest of the network is quantized to the base level, and they are
built with an **imatrix** (CPU calibration) — `Q4_K_M-mixed` and `Q6_K-mixed`.

Measured **KL divergence** vs the f16 reference (full-vocab, first-token
distribution, 8 neutral prompts, CPU): a lower value = closer to f16.

| quant | size | base dtype | embedding/output | KL vs f16 | closeness |
|---|---:|---|---:|---:|---|
| `Qwen3.8-27B-abliterated-mtp-f16.gguf` | 54.7 GB | bf16 | bf16 | **0 (reference)** | — |
| `Qwen3.8-27B-abliterated-mtp-Q6_K-mixed.gguf` | 22.4 GB | Q6_K | q8_0 | **0.0017** | best quant |
| `Qwen3.8-27B-abliterated-mtp-Q4_K_M-mixed.gguf` | 17.8 GB | Q4_K_M | q8_0 | **0.0042** | 2.5× f16 than Q6_K |
| `Qwen3.8-27B-abliterated-mtp-IQ4_NL-mixed.gguf` | 16.0 GB | IQ4_NL | q8_0 | **0.0083** | smallest of the set |

All four are very close to f16 (KL < 0.01). **Q6_K-mixed (KL 0.0017) is the
closest to f16 (~2.5× better than Q4_K_M-mixed's 0.0042, ~5× better than
IQ4_NL-mixed's 0.0083)** — the higher base dtype plus the q8_0 embedding/output
keep it near-lossless, at roughly half the f16 size. IQ4_NL-mixed is the
smallest (16 GB) but drifts the most from f16 of the three; it is still a good
small-footprint option.

### How they were built (from `~/llamacpp/llama.cpp`)

```bash
cd ~/llamacpp/llama.cpp

# Q4_K_M-mixed: q8_0 embedding + outputs, imatrix-calibrated
./build/bin/llama-quantize --imatrix ./Qwen3.8-27B-abliterated-imatrix-cpu.gguf \
  --output-tensor-type q8_0 --token-embedding-type q8_0 \
  ./Qwen3.8-27B-abliterated-mtp-f16.gguf \
  ./Qwen3.8-27B-abliterated-mtp-Q4_K_M-mixed.gguf Q4_K_M

# Q6_K-mixed: q8_0 embedding + outputs, imatrix-calibrated
./build/bin/llama-quantize --imatrix ./Qwen3.8-27B-abliterated-imatrix-cpu.gguf \
  --output-tensor-type q8_0 --token-embedding-type q8_0 \
  ./Qwen3.8-27B-abliterated-mtp-f16.gguf \
  ./Qwen3.8-27B-abliterated-mtp-Q6_K-mixed.gguf Q6_K

# IQ4_NL-mixed: q8_0 embedding + outputs, imatrix-calibrated
./build/bin/llama-quantize --imatrix ./Qwen3.8-27B-abliterated-imatrix-cpu.gguf \
  --output-tensor-type q8_0 --token-embedding-type q8_0 \
  ./Qwen3.8-27B-abliterated-mtp-f16.gguf \
  ./Qwen3.8-27B-abliterated-mtp-IQ4_NL-mixed.gguf IQ4_NL
```

Both carry the MTP head (quantized from the `-mtp-f16` source), so
`--spec-type draft-mtp` works with them.

---

## Custom IQ quants (no MTP head)

These `IQ2_M-custom` / `IQ3_M-custom` builds use a **custom layer-precision
recipe**: the embedding and output tensors are `q8_0`, the **first 4 layers
(`blk.0-3`) and last 4 layers (`blk.60-63`) plus `attn_v`/`attn_output` are
kept at a higher precision** (`q4_K` for IQ2, `q5_K` for IQ3) while the rest is
at the base IQ level. They were quantized from the **`-f16-nomtp`** source, so
they carry **NO MTP head** — do NOT use `--spec-type draft-mtp` with them.

| file | size | base | boundary (blk.0-3/60-63, attn_v/output) | KL vs f16 | MTP |
|---|---:|---|---:|---:|:---:|
| `Qwen3.8-27B-abliterated-IQ3_M-custom.gguf` | 14.0 GB | IQ3_M | q5_K | **0.0157** | ❌ |
| `Qwen3.8-27B-abliterated-IQ2_M-custom.gguf` | 12.0 GB | IQ2_M | q4_K | **0.0617** | ❌ |

**IQ3_M-custom (KL 0.0157)** is usable but visibly drifts from f16 (~4× the
IQ4_NL-mixed 0.0083, ~9× the Q6_K-mixed 0.0017). **IQ2_M-custom (KL 0.0617)**
drifts further (~4× IQ3_M, ~15× Q4_K_M). **IQ1_M is not recommended** — it
tends to loop (KL 0.295, far from f16). Both custom quants are **no-MTP**, so
they save memory (no draft head) but give up self-speculative decoding.

### How they were built (from `~/llamacpp/llama.cpp`)

```bash
cd ~/llamacpp/llama.cpp

# IQ3_M-custom: q8_0 emb/output, boundary layers + attn_v/output at q5_K
./build/bin/llama-quantize \
  --imatrix ./Qwen3.8-27B-abliterated-imatrix-cpu.gguf \
  --output-tensor-type q8_0 \
  --token-embedding-type q8_0 \
  --tensor-type "blk\.[0-3]\..*=q5_K" \
  --tensor-type "blk\.6[0-3]\..*=q5_K" \
  --tensor-type "attn_v=q5_K" \
  --tensor-type "attn_output=q5_K" \
  ./Qwen3.8-27B-Abliterated-f16-nomtp.gguf \
  ./Qwen3.8-27B-abliterated-IQ3_M-custom.gguf \
  IQ3_M

# IQ2_M-custom: q8_0 emb/output, boundary layers + attn_v/output at q4_K
./build/bin/llama-quantize \
  --imatrix ./Qwen3.8-27B-abliterated-imatrix-cpu.gguf \
  --output-tensor-type q8_0 \
  --token-embedding-type q8_0 \
  --tensor-type "blk\.[0-3]\..*=q4_K" \
  --tensor-type "blk\.6[0-3]\..*=q4_K" \
  --tensor-type "attn_v=q4_K" \
  --tensor-type "attn_output=q4_K" \
  ./Qwen3.8-27B-Abliterated-f16-nomtp.gguf \
  ./Qwen3.8-27B-abliterated-IQ2_M-custom.gguf \
  IQ2_M
```

> **IQ1_M warning:** an `IQ1_M` build was also measured (KL 0.295) but is **not
> recommended** — at 1-bit the model drifts far from f16 and tends to loop.
> Stick with IQ3_M-custom (14 GB) or IQ2_M-custom (12 GB) as the smallest
> usable options.

---


## Files

| File | Size | MTP | Notes |
|---|---|---|---|
| `Qwen3.8-27B-abliterated-mtp-f16.gguf` | ~54.7 GB | ✅ | Full-precision reference. Highest quality; largest. Use for imatrix + as quant source. |
| `Qwen3.8-27B-abliterated-mtp-Q8_0.gguf` | ~29.0 GB | ✅ | HIGH quality/size. |
| `Qwen3.8-27B-abliterated-mtp-Q6_K.gguf` | ~22.4 GB | ✅ | Balanced quality/size. **Recommended** if you have the VRAM/RAM. |
| `Qwen3.8-27B-abliterated-mtp-Q4_K_M.gguf` | ~16.8 GB | ✅ | Smaller footprint. (Currently without imatrix — quality to improve.) |
| `Qwen3.8-27B-abliterated-mtp-IQ4_NL.gguf` | ~16.0 GB | ✅ | Smaller footprint. (with imatrix) |
| `Qwen3.8-27B-abliterated-mtp-IQ3_M.gguf` | ~12.8 GB | ✅ | Smallest MTP-enabled quant. (with imatrix) |
| `Qwen3.8-27B-abliterated-IQ3_XXS.gguf` | ~11.2 GB | ❌ | **No MTP head** — `--spec-type draft-mtp` NOT available. |
| `Qwen3.8-27B-abliterated-IQ2_M.gguf` | ~10.0 GB | ❌ | **No MTP head** — `--spec-type draft-mtp` NOT available. |
| `mmproj-Qwen3.8-27B-GGUF.gguf` | ~931 MB | — | Multimodal projector — enables image understanding. |
| `Qwen3.8-27B-abliterated-imatrix.dat` | ~13.6 MB | — | imatrix calibration data (for `llama-quantize --imatrix`). |

> **MTP note:** only files with `-mtp-` in the filename carry the embedded MTP
> head. `IQ2_M` and `IQ3_XXS` were quantized **without** the MTP head — do NOT
> pass `--spec-type draft-mtp` with them (llama.cpp will error / fall back to
> plain decoding). For the `-mtp-` files you can use **self-speculative
> decoding** in llama.cpp (`--spec-type draft-mtp`) for faster generation.

---


## Quick start — llama.cpp

Recommended `llama-server` flags (used for testing this model):

```sh
llama-server -m Qwen3.8-27B-abliterated-mtp-Q6_K.gguf \
  --spec-type draft-mtp \
  --spec-draft-n-max 2 \
  --ctx-size $((256*1024)) \
  --batch-size 8192 \
  --ubatch-size 1024 \
  --cache-type-k f16 \
  --cache-type-v f16 \
  --flash-attn on \
  --cont-batching \
  --temp 0.95 \
  --top-k 20 \
  --top-p 0.95 \
  --min-p 0.0 \
  --mlock \
  --no-mmap \
  --jinja -ngl 99
```



### If loop try to use 
```
  --repeat-penalty 1.03 \
  --repeat-last-n 256 \
  --dry-multiplier 0.5 \
  --dry-base 1.75 \
  --dry-allowed-length 5 \
  --dry-penalty-last-n -1 \
  --reverse-prompt "<|im_end|>" \
  --reverse-prompt "<|endoftext|>" \
```

Notes on the flags:

- **256K context** (`--ctx-size $((256*1024))`) with f16 KV cache — Qwen3.8
  natively supports a long context; budget your VRAM accordingly.
- **`--spec-type draft-mtp`** enables MTP self-speculative decoding. Sweep
  `--spec-draft-n-max` (1–6) to find the fastest point on your hardware.
- **DRY sampler** (`dry-*`) is a repetition suppressor — tune
  `--dry-multiplier` if output feels too constrained or too repetitive.
- **`--chat-template-file chat_template.jinja`** — point this at the
  `chat_template.jinja` from the source repo
  ([hotdogs/Qwen3.8-27B-abliterated](https://huggingface.co/hotdogs/Qwen3.8-27B-abliterated))
  to guarantee the correct Qwen3.8 prompt format (thinking + vision tags).
- **`--mlock --no-mmap`** pins weights in RAM (faster, but needs enough free
  RAM for the model).
- **`--reverse-prompt`** on the Qwen EOS/stop tokens keeps multi-turn chat
  clean.

CLI one-shot:

```sh
llama-cli -m Qwen3.8-27B-abliterated-mtp-Q4_K_M.gguf \
  --spec-type draft-mtp -ngl 99 -p "Explain how a lock cylinder works."
```

For image support, pass the projector:

```sh
llama-server -m Qwen3.8-27B-abliterated-mtp-Q6_K.gguf \
  --mmproj mmproj-Qwen3.8-27B-GGUF.gguf \
  --spec-type draft-mtp -ngl 99 -c 32768
```

---

## Which file should I use?

| Use case | Pick |
|---|---|
| Best quality (large VRAM/RAM, e.g. 48 GB+) | `f16` |
| Best quality-per-GB (24 GB class) | `Q6_K` |
| Smaller footprint (16 GB class) | `Q4_K_M` |
| Image/video understanding | add `mmproj-Qwen3.8-27B-GGUF.gguf` |

`llama-server -ngl 99` offloads all layers to GPU; lower `-ngl` to spill to
RAM if VRAM is tight.

---

## About the source model

**[hotdogs/Qwen3.8-27B-abliterated](https://huggingface.co/hotdogs/Qwen3.8-27B-abliterated)** is a **training-free abliterated** build of `Qwen/Qwen3.8-27B` (a dense 27B native vision-language model with hybrid full-attention + linear-attention architecture). Refusal behaviour is removed by a single forward-only rank-1 weight edit (`W ← W − λ·r̂(r̂ᵀW)`) that orthogonalizes the "refusal direction" `r̂` out of the **131 residual-stream writers** at **λ = 1.2** (hidden-state index 46, non-thinking) — no fine-tuning, no data poisoning.

The vision tower and `lm_head` are byte-for-byte unchanged. **These GGUFs were converted from the λ = 1.2 abliterated checkpoint** (the current published base), so the refusal-removal edit is preserved through quantization.

### Capability (A/B vs base, source model)

The GGUFs quantize the λ = 1.2 checkpoint, whose bf16 A/B benchmark against
`Qwen/Qwen3.8-27B` (identical lm-eval HF harness, same prompt/config) is:

| benchmark | base | λ = 1.2 (bf16) | Δ |
|---|---:|---:|---|
| MMLU (0-shot) | 0.8388 | 0.8342 | −0.005 |
| GSM8K (5-shot, strict) | 0.62 | 0.59 | −0.03 |
| ARC-Challenge (0-shot) | 0.4433 | 0.4533 | +0.010 |

Refusal (100-prompt heretic harness): 98/100 → **39/100**; KL vs base **0.0001**.
See the base model card for the full method and the weight-level `r̂` check.

> **Disclaimer.** The underlying model will not refuse. It is published for alignment and safety research — measuring what refusal training protects, red-teaming, and studying refusal-direction mechanics. You are responsible for your use of it and for complying with all applicable laws.

---

## About MTP (Multi-Token Prediction)

Qwen3.8 uses an MTP head trained to predict the next several tokens in a
single forward pass. In GGUF this head can be kept and used for
**self-speculative decoding**: the model drafts N candidate tokens, verifies
them in one pass, and accepts the correct prefix — giving a decode speedup
with no loss of output quality.

Enable it in llama.cpp with `--spec-type draft-mtp`. Sweep
`--spec-draft-n-max` from 1–6 to find the fastest point on your hardware
(start with 2). Watch the server log for:

```
draft acceptance rate = 0.XX (N accepted / M generated)
statistics ... #acc tokens = N
```

---

## Roadmap

- [x] Convert abliterated model to GGUF (MTP head preserved)
- [x] Build an imatrix calibration corpus (real usage / Thai-augmented)
- [x] Verify MTP acceptance rate on multiple hardware profiles


---

## Reproduction / source

- Base model: [hotdogs/Qwen3.8-27B-abliterated](https://huggingface.co/hotdogs/Qwen3.8-27B-abliterated)
- Abliteration tool: [nanofatdog/LLM-abliterate](https://github.com/nanofatdog/LLM-abliterate) (training-free, generic architecture detection)
- Conversion: [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) `convert_hf_to_gguf.py` (MTP/NextN tensors preserved) + `llama-quantize`

The exact build/quantize commands will be added here once the imatrix pass
is complete.

---

## License

Apache-2.0 (inherited from the base model and its source).
