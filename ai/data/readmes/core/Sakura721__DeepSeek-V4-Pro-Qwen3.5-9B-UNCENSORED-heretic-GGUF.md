---
base_model:
- xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic
base_model_relation: quantized
language:
- en
- zh
- ko
- ja
- es
- ru
library_name: gguf
license: apache-2.0
pipeline_tag: image-text-to-text
tags:
- gguf
- llama.cpp
- lm-studio
- qwen3_5
- qwen35
- qwen3.5
- hybrid-attention
- linear-attention
- reasoning
- distillation
- deepseek
- unsloth
- mtp
- heretic
- uncensored
- decensored
- abliterated
- 4-bit
- q4_k_m
- text-generation
- image-text-to-text
---

# DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic — GGUF (Q4_K_M)

GGUF conversion of **[xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)**, quantized to **Q4_K_M** for `llama.cpp` / LM Studio / Ollama / llama-cpp-python, with a separate **F16 vision projector (mmproj)** so the multimodal path keeps working.

| | |
| :--- | :--- |
| **Base (fp) repo** | [xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic) |
| **Upstream chain** | `Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B` (SFT+RL distill of *Qwen3.5-9B*) → Heretic ARA ablation → this GGUF |
| **Architecture** | `qwen3_5` (`qwen35` in GGUF) — hybrid linear-attention + full-attention, 1 MTP head |
| **Parameters** | 8.954 B (text) · 0.456 B (mmproj) |
| **Quantization** | Q4_K_M · 5.02 bpw · 218 tensors at Q4_K, 33 at Q6_K, 177 at F32 |
| **Context** | 262,144 tokens native (rope_theta 10,000,000, interleaved MRoPE `[11, 11, 10, 0]`) |
| **Toolchain** | `llama.cpp` build **b12182** (`fd27b2034`) |
| **Modalities** | text · image · video (vision needs the `mmproj` file) |

---

## 📦 Files in this repository

| File | Size | Precision | SHA256 |
| :--- | ---: | :--- | :--- |
| `DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-Q4_K_M.gguf` | 5.243 GiB / 5,629,111,968 B | Q4_K_M (5.02 bpw) | `82a19e2f3c3834d6b9d1e17dacef27ebee5dd814bae3cce557f47ecca66dadab` |
| `mmproj-DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-f16.gguf` | 875.6 MiB / 918,167,360 B | F16 projector | `f8d09a6d00ee3318c58f142a62a628346384a878d2f830f470a0483a49690a5e` |

Both files are **required for vision**, only the first one is required for text-only use.

### Tensor type distribution (main model)

| Type | Tensors | Size |
| :--- | ---: | ---: |
| `Q4_K` | 217 | 3,600.0 MiB |
| `Q6_K` | 33 | 1,753.8 MiB |
| `F32` | 177 | 4.0 MiB |

`Q6_K` is applied to the sensitive tensors (`attn_v`, `ffn_down`, output-side projections) as defined by the Q4_K_M recipe; all norms, `ssm_dt`, `ssm_conv1d`, `A_log`, `dt_bias` and the recurrent state tensors stay in F32.

---

## 🚀 Quick start

### llama.cpp — CLI

```bash
# text only
llama-cli -m DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-Q4_K_M.gguf \
  -c 8192 -cnv -t 8

# vision (image / video) — both files required
llama-mtmd-cli -m DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-Q4_K_M.gguf \
  --mmproj mmproj-DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-f16.gguf \
  -c 8192 --image ./photo.jpg
```

### llama.cpp — OpenAI-compatible server

```bash
llama-server -m DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-Q4_K_M.gguf \
  --mmproj mmproj-DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-f16.gguf \
  -c 16384 -ngl 99 -t 8 --host 127.0.0.1 --port 8080
```

```bash
curl http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"local","messages":[{"role":"user","content":"Prove that sqrt(2) is irrational."}]}'
```

The chat template is embedded in the GGUF, so `/v1/chat/completions` and `llama-cli -cnv` need no extra flags. Reasoning tokens are returned in `reasoning_content`; the visible answer arrives after the closing `</think>` token.

### LM Studio

Put both `.gguf` files in the **same folder** (a `models/<publisher>/<model>/` directory works), then rescan. LM Studio detects the `mmproj-` prefix automatically and offers the model as a vision model; the Q4_K_M file alone also loads as a text model.

### Ollama

```dockerfile
# Modelfile (text only — the mmproj projector is not loadable through Ollama today)
FROM ./DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-Q4_K_M.gguf
PARAMETER temperature 0.7
PARAMETER top_p 0.8
PARAMETER top_k 20
PARAMETER num_ctx 16384
```

```bash
ollama create deepseek-v4-pro-qwen35-9b-heretic -f Modelfile
ollama run deepseek-v4-pro-qwen35-9b-heretic "Solve: integral of x^2 sin(x) dx"
```

### llama-cpp-python

```python
from llama_cpp import Llama

llm = Llama(
    model_path="DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-Q4_K_M.gguf",
    n_ctx=16384,
    n_threads=8,
    verbose=False,
)
print(llm.create_chat_completion(
    messages=[{"role": "user", "content": "What is 17 * 23? Show your reasoning."}],
    max_tokens=512,
)["choices"][0]["message"]["content"])
```

---

## 🧠 Model architecture

| Field | Value |
| :--- | :--- |
| GGUF architecture | `qwen35` |
| Hidden size | 4096 |
| Layers | 33 (32 transformer + 1 MTP) |
| Attention layout | 3 × linear-attention + 1 × full-attention per group of 4 (`full_attention_interval = 4`) |
| Full-attention layers | 8 (indices 3, 7, 11, 15, 19, 23, 27, 31) |
| Q / KV heads | 16 / 4 · head_dim 256 |
| FFN | SwiGLU, intermediate 12,288 |
| Vocab | 248,320 (`tokenizer.ggml.pre = qwen35`, BPE) |
| Special tokens | BOS: none · EOS: `<|im_end|>` (248046) · PAD: `<|vision_pad|>` (248055) |
| RoPE | interleaved MRoPE, sections `[11, 11, 10, 0]`, theta 10,000,000, partial rotary 0.25 |
| SSM (linear attn.) | conv kernel 4 · state size 128 · inner size 4096 · groups 16 · time-step rank 32 |
| Tied embeddings | No (`lm_head` present) |

Because only 8 of 33 layers hold a growing KV cache, long-context cost is unusually low for a 9B model: roughly **32 KiB per token** with an F16 KV cache (≈1 GiB at 32 K, ≈8 GiB at 262 K, before the recurrent state).

### MTP head is **not** present in this file

The upstream `config.json` declares `mtp_num_hidden_layers: 1` (added by `unsloth_fixed_mtp: true`), but the published safetensors contain **no `mtp.*` tensors at all**. Blindly following the config, the converter set `qwen35.block_count = 33` and `qwen35.nextn_predict_layers = 1` while the file only carried 32 transformer blocks, so any loader that resolves the last layer as an MTP block aborted with:

```
qwen35.cpp:495: GGML_ASSERT(layer.nextn.eh_proj && "MTP block missing nextn.eh_proj") failed
```

**This build is patched to the self-consistent form**: `block_count = 32`, `nextn_predict_layers = 0`, `attention.recurrent_layers` truncated to 32 entries. Everything still matches the 427 tensors in the file, and it now loads in `llama-server`, LM Studio and `llama-cli`.

If you want speculative decoding later, take the MTP head from a checkpoint that actually ships it (e.g. `Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-GGUF`'s source weights) and export it as a separate draft with `convert_hf_to_gguf.py --mtp`.

---

## 🖼 Vision encoder (mmproj)

| Field | Value |
| :--- | :--- |
| Projector type | `qwen3vl_merger` |
| Depth | 27 blocks |
| Hidden size | 1152 |
| Image size / patch | 768 / 16 |
| Spatial merge | 2 |
| Position embeddings | 2304 |
| Tensors | 334 (112 × F16, 222 × F32) |

The projector is exported at **F16** on purpose: quantizing it below F16 measurably hurts OCR and grounding accuracy, and it only costs ~0.9 GiB. If you need it smaller, `llama-quantize mmproj-...-f16.gguf mmproj-...-q8_0.gguf Q8_0` gives ~500 MiB and is generally safe for captioning, but not for fine-grained text reading.

> When loading Qwen-VL-class models, `llama.cpp` may warn that grounding tasks want ≥1024 image tokens; add `--image-min-tokens 1024` to `llama-mtmd-cli` / `llama-server` if you see grounding degradation.

---

## ⚙️ How this file was produced

```bash
# 1. bf16 safetensors -> F16 GGUF (exact, lossless for these weights)
python convert_hf_to_gguf.py xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic \
  --outtype f16 --outfile model-f16.gguf

# 2. F16 -> Q4_K_M
llama-quantize model-f16.gguf DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-Q4_K_M.gguf Q4_K_M 8

# 3. vision projector, separate file
python convert_hf_to_gguf.py xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic \
  --mmproj --outtype f16 \
  --outfile mmproj-DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-f16.gguf
```

Conversion ran with `transformers` 5.x, `torch` 2.15 (CPU) and `llama.cpp` b12182. Quantized by **Sakura721**; the upstream fp weights belong to `xtools-at`. The converter performs the V-head regrouping required by `in_proj_qkv` / `in_proj_z` / `in_proj_a` / `in_proj_b` / `conv1d` / `out_proj` (32 value heads over 16 key heads) and always writes `qwen35.rope.dimension_sections`, so the resulting file is self-consistent without patching.

---

## ✅ Verification performed on this build

| Check | Result |
| :--- | :--- |
| Tokenizer round-trip | `hello` → 14556, ` world` → 1814 |
| Metadata integrity | 427 tensors · `block_count 33` · `ctx 262144` · `recurrent_layers` mask matches `layer_types` |
| Chat template | render matches upstream `chat_template.jinja` (8,736 bytes embedded verbatim) |
| Text inference | coherent reasoning + answer via `llama-cli` and `/v1/chat/completions` |
| Vision inference | 384×384 test image described correctly (red border, navy disc, white background) |
| Server health | `GET /health` → `{"status":"ok"}` |

Reference speed on the machine used for conversion — **i5-9300H (4C/8T), 16 GB RAM, no GPU offload** — with `llama-bench`:

| Test | t/s |
| :--- | ---: |
| pp512 | 12.50 |
| tg128 | 0.96 |

That number is CPU-only and not a statement about the model on real hardware; expect several tens of tokens/s for generation on any modern GPU once the file is offloaded with `-ngl 99`.

---

## 🌡 Sampling defaults

A reasonable starting point for this family (adjust to taste):

| Parameter | Value |
| :--- | :--- |
| `temperature` | 0.7 (0.6 for math/STEM, 0.9 for creative writing) |
| `top_p` | 0.8 |
| `top_k` | 20 |
| `min_p` | 0.0 |
| `repeat_penalty` | 1.0–1.05 |

The model is a reasoning model: it emits `<think> … </think>` before the answer. Keep the full reasoning trace when solving math/STEM problems — truncating it visibly degrades accuracy. If a frontend hides reasoning, make sure it does not also cut the `<think>` block out of the context.

---

## 📊 Inherited benchmark numbers

These results belong to the **unquantized base checkpoint** and are reproduced here for context only. **They were not re-measured on this Q4_K_M file.** Quantization error at Q4_K_M on a 9B model is normally small, but treat the numbers as upper bounds.

| Benchmark | Base model | Notes |
| :--- | ---: | :--- |
| GSM8K | 94.50 % | 4-run mean, NVFP4 + vLLM |
| MMLU-Pro Math | 92.40 % | MTP-Q8_0 GGUF, 8 K context |
| MMLU-Pro (Math + Physics + Chemistry) | 90.53 % | 500 sampled questions per subset, 1,500 total |
| Gain vs. Qwen3.5-9B base | +0.93 pts | MMLU-Pro average |

Abliteration quality, from the base repo: **3/100 refusals** vs. 100/100 for the unmodified model, KL divergence **0.0422**. Heretic Arbitrary-Rank Ablation was applied to layers 9–24 with `preserve_good_behavior_weight 0.8264`, `steer_bad_behavior_weight 0.0003`, `overcorrect_relative_weight 0.9645`, `neighbor_count 12`.

---

## ⚠️ Limitations

- **Experimental community model.** Hallucinations, arithmetic slips and unstable behaviour on underspecified tasks remain possible; verify high-stakes math, science and factual output independently.
- **Quantization is not free.** Q4_K_M introduces a small but real quality drop versus the bf16 weights, most visible in long derivations, rare-script OCR and code. Use `Q5_K_M`/`Q6_K`/`Q8_0` if you need more headroom.
- **Vision is a bolt-on.** The projector is F16 but the language tower is Q4_K_M, so image-conditioned reasoning inherits the same quantization error; small text in images is the first thing to suffer.
- **Reasoning traces can be long.** `-c` must leave room for `<think>`; running at 2 K context will truncate reasoning mid-flight.
- **Decensored weights.** This model has had its refusal behaviour ablated. It will produce content that aligned models filter, including content that is wrong, offensive or unsafe. You are responsible for how you deploy it and for complying with the licences and laws that apply to you.
- The architecture (`qwen3_5`) is recent: use a `llama.cpp` build from **b12182 or newer**, and avoid forks that predate `QWEN35` support — they will refuse to load the file.

---

## 📚 Citation

```bibtex
@misc{sakura721_deepseek_v4_pro_qwen35_9b_heretic_gguf,
  title        = {DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic GGUF (Q4\_K\_M)},
  author       = {Sakura721},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Sakura721/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-GGUF}},
  note         = {GGUF quantization of xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic}
}

@misc{jackrong_deepseek_v4_pro_qwen35_9b,
  title     = {DeepSeek-V4-Pro-Qwen3.5-9B},
  author    = {Jackrong},
  year      = {2026},
  publisher = {Hugging Face}
}
```

## 🙏 Acknowledgements

- **Jackrong** — the `DeepSeek-V4-Pro-Qwen3.5-9B` distillation this line descends from.
- **Heretic** — arbitrary-rank ablation tooling used to decensor the base model.
- **Qwen** — the Qwen3.5-9B architecture and tokenizer.
- **Unsloth** — fine-tuning tooling used upstream.
- **ggml-org / llama.cpp** — the converter, quantizer and runtime that made this file possible.

*Quantized with `llama.cpp` b12182 on Windows (CPU-only), from the bf16 safetensors of the base repository.*
