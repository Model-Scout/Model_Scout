---
language:
- en
- ko
- zh
license: apache-2.0
base_model: Qwen/Qwen3.6-35B-A3B
base_model_relation: quantized
library_name: mlx
pipeline_tag: image-text-to-text
tags:
- mlx
- qwen3_5_moe
- quantized
- mixed-precision
- mixture-of-experts
- apple-silicon
- dwq
- hybrid-attention
- conversational
---

# Qwen3.6-35B-A3B-Alis-MLX-Dynamic

Apple Silicon (MLX) **mixed-precision** quantizations of [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) — a 35B MoE with **3B active** parameters, 3:1 Gated DeltaNet : full attention hybrid (`qwen3_5_moe`). One repo, one card — each quantization lives on its own branch.

| branch | eff. bpw | size | target Mac | decode* | KL vs bf16 (top-1 flip) | status |
|---|---|---|---|---|---|---|
| **`main`** | **4.000** | **17.33 GB** | 24 GB+ | **102.1 tok/s** | **0.292 (19.7%)** | ✅ golden — GPQA-D **76.3%** |
| `16gb` | 2.700 | **11.70 GB** | **16 GB** (sysctl) | **110.8 tok/s** | 1.111 (32.9%) | ⚠️ under review — see note |
| [`vision`](https://huggingface.co/avlp12/Qwen3.6-35B-A3B-Alis-MLX-Dynamic/tree/vision) | 4.087 | **17.93 GB** | 24 GB+ | ~100 tok/s | (same text weights) | ✅ multimodal — vision tower restored at 8-bit |
| `mtp-bf16` | bf16 | 1.69 GB | — | — | — | MTP head sidecar for self-speculative decoding |

\* single-stream decode on an M3 Ultra, short prompt. A3B routing makes this the **fastest model class per GB** in the lineup — ~3× the decode rate of the dense 27B sibling.

Everything below is **measured, not projected** — KL / top-1 flip on a fixed 4096-token EN/code/ZH/KO slice (teacher-forced vs bf16), strided perplexity (ctx 2048 / stride 1024), and single-stream decode on an M3 Ultra.

## Which build?

- **24 GB+ Mac** → `main`. 16 GiB weights, 17.5 GB measured peak at short context, 102 tok/s.
- **16 GB Mac** → `16gb`. 11 GiB weights, 11.8 GB measured peak — **exceeds the default ~10.7 GiB wired limit**; raise it first:

  ```bash
  sudo sysctl iogpu.wired_limit_mb=13312
  ```

  With int8 KV that leaves ~1.5 GiB of cache ≈ **150 K tokens** of context (KV here is tiny — see below). 111 tok/s decode makes this the best speed-per-GB option for 16 GB machines; prefer it over the dense 27B 16 GB build when throughput matters more than per-token quality.

## Multimodal (default)

`main` carries the full multimodal stack — 4.0bpw text weights + the vision tower at
8-bit (verified with EN/KO OCR tests). Plain mlx-lm loads `main` fine for text-only use;
the `text` branch saves 0.60 GB if you never need images.

```bash
pip install mlx-vlm
python -m mlx_vlm generate --model avlp12/Qwen3.6-35B-A3B-Alis-MLX-Dynamic \
  --image photo.jpg --prompt "이미지의 텍스트를 읽어줘." --max-tokens 300
```

## Usage

```python
from mlx_lm import load, generate

model, tokenizer = load("avlp12/Qwen3.6-35B-A3B-Alis-MLX-Dynamic")                  # main
model, tokenizer = load("avlp12/Qwen3.6-35B-A3B-Alis-MLX-Dynamic", revision="16gb")

prompt = tokenizer.apply_chat_template(
    [{"role": "user", "content": "MoE 라우팅을 두 문장으로 설명해줘."}],
    add_generation_prompt=True,
)
print(generate(model, tokenizer, prompt=prompt, max_tokens=512))
```

CLI / server:

```bash
mlx_lm.generate --model avlp12/Qwen3.6-35B-A3B-Alis-MLX-Dynamic --prompt "..." -m 512
hf download avlp12/Qwen3.6-35B-A3B-Alis-MLX-Dynamic --revision 16gb --local-dir qwen36-35b-16gb
mlx_lm.server --model ./qwen36-35b-16gb --port 8080
```

Long context: `--kv-bits 8 --kv-group-size 64` in the generate path (measured quality-free, below).

> ⚠️ **`16gb` under review.** The dense-27B sibling's same-calibration low-bit tier was withdrawn after free-running generation showed early stops / repetition loops on long-CoT problems (teacher-forced KL/PPL did not catch it). This branch shares that calibration recipe and is being re-verified generatively; treat it as experimental until this notice is removed.

## Recipes (verified from each build's `config.json`)

92% of the parameters live in 256 fused routed experts per MoE layer (stored as 3D
`SwitchLinear` tensors — the sensitivity scan samples 8 experts/layer/matrix). Per-tensor
bits assigned by marginal utility from a 2–6-bit + nvfp4 scan of all 472 text tensors:

![Per-tier bit allocation](https://huggingface.co/avlp12/Qwen3.6-35B-A3B-Alis-MLX-Dynamic/resolve/main/assets/fig_bit_allocation.png)

| tier | bulk | rest | pins |
|---|---|---|---|
| `main` (4.0bpw) | 50.3% affine 3-bit g64 | 49.5% nvfp4 g16 | routers/shared-expert gates 6-bit; embed & lm_head ≥4-bit |
| `16gb` (2.7bpw) | 83.6% affine 2-bit g64 | 12.9% 3-bit + 3.4% nvfp4 | same |

**nvfp4 vs affine — measured both ways.** On the dense 27B sibling, affine-only beat
nvfp4 decisively (its card has the numbers). Here the reverse holds: an affine-only
4.0bpw rebuild (50.3% a3 + 49.4% a4) scored **KL 0.309** vs `main`'s nvfp4-mix **0.292**
— nvfp4 g16 genuinely suits the small fused expert matrices (2048×512). The format
choice is architecture-dependent; `main` stands as-is.

**DWQ.** Layerwise DWQ (KL distillation vs bf16, 260-sample EN/KO/ZH/code chat mix, seq
512, validation-gated — [alis-dwq](https://github.com/avlp12/alis-dwq)): at 4.0bpw every
round was rejected (already teacher-close), so `main` carries conversion-time weights; at
2.7bpw DWQ improved valid KL **0.305 → 0.268 (−12%)**.

## Quality

KL(bf16‖quant) / top-1 flip on the fixed 4096-token slice, per domain:

| build | overall | EN | code | ZH | KO |
|---|---|---|---|---|---|
| `main` 4.0bpw | **0.292 / 19.7%** | 0.100 / 11.2% | 0.622 / 19.7% | 0.266 / 27.9% | 0.181 / 19.9% |
| `16gb` 2.7bpw | 1.111 / 32.9% | 0.365 / 21.8% | 2.454 / 27.3% | 1.004 / 47.7% | 0.622 / 34.8% |

Strided perplexity (ctx 2048, stride 1024; wikitext / code / Korean):

| build | wikitext | code | KO |
|---|---|---|---|
| `main` | 6.16 [6.07, 6.25] | 2.12 [2.10, 2.14] | 7.09 [7.02, 7.17] |
| `16gb` | 7.65 [7.54, 7.76] | 2.57 [2.54, 2.60] | 9.04 [8.94, 9.14] |

### Generative benchmark (GPQA-Diamond, our harness, n=198, temp 1.0, 32K cap)

`main` scores **76.3%** (avg 14,742 thinking tokens, 7 no-answer). For scale: a dense
27B at 4.6bpw scores 72.7 on the same harness, and quantized short-thinking models
reach 83.3 — see the cross-family curve on the
[ThinkingCap repo](https://huggingface.co/avlp12/ThinkingCap-Qwen3.6-27B-Alis-MLX-Dynamic).
The `16gb` 2.7bpw tier fails hard reasoning generatively (MMLU-300 75.3% but GPQA
non-convergent) — hence the warning above; treat it as a light/general-use build only.

## KV cache — measured recommendations

Only **10 of 40 layers** carry KV (the rest are Gated DeltaNet recurrent state), so KV is
tiny to begin with; quantizing it is still measured quality-free:

| KV config | KL vs bf16-KV | KV bytes/token | ~ctx in 1.5 GiB |
|---|---|---|---|
| bf16 | 0 | 20 KB | 75 K |
| **int8 g64 (recommended)** | 0.011 | 10 KB | 150 K |
| K4/V8 (long-context) | 0.016 | 7.5 KB | 200 K |

## Notes & provenance

- Text-only conversion: the base checkpoint's **vision tower and MTP head are not included**
  (mlx-lm text path). An `mtp-bf16` sidecar branch may land later.
- Calibration/eval data: tulu-3 SFT chat (EN), Korean chat, code/ZH mix — chat-template rendered.
- Built on an M3 Ultra 512 GB · mlx-lm 0.31.3 · mlx 0.31.2 · 2026-07.
- Sibling repo: [Qwen3.6-27B-Alis-MLX-Dynamic](https://huggingface.co/avlp12/Qwen3.6-27B-Alis-MLX-Dynamic) (dense, higher per-token quality; its `16gb-thinkingcap` branch fits 16 GB Macs without sysctl).

## Credits

- **[Qwen team](https://huggingface.co/Qwen)** — the Qwen3.6-35B-A3B base model and its hybrid DeltaNet MoE architecture.
- **[Apple MLX team](https://github.com/ml-explore/mlx)** — mlx / mlx-lm, including the DWQ trainer this pipeline builds on.
- **[Unsloth](https://huggingface.co/unsloth)** — their NVFP4 releases motivated the diverse-chat calibration mix and served as quality reference points.
- **[AllenAI](https://huggingface.co/datasets/allenai/tulu-3-sft-mixture)** — tulu-3 SFT mixture used in the calibration set.
- Quantization recipe, DWQ retune and evals: [Alis (avlp12)](https://huggingface.co/avlp12) with the [alis-dwq](https://github.com/avlp12/alis-dwq) pipeline; built with assistance from Claude (Anthropic).
