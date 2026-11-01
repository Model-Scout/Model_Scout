---
license: apache-2.0
library_name: mlx
pipeline_tag: image-text-to-text
base_model: Jiunsong/SuperQwen3.8-27b-abliterated
base_model_relation: quantized
tags:
  - mlx
  - mlx-lm
  - qwen3.8
  - qwen3.5
  - apple-silicon
  - 4-bit
  - quantized
  - multimodal
  - reasoning
  - tool-calling
  - uncensored
  - abliterated
  - obliteratus
  - supertune
language:
  - en
  - ko
---

<div align="center">

<img src="./assets/superqwen38-hero.svg" alt="SuperQwen3.8 27B — BF16, NVFP4, GGUF and MLX" width="100%">

<h1>SuperQwen3.8-27b-abliterated-MLX-4bit</h1>

<p><em>The Apple-Silicon build: native affine 4-bit weights, bounded reasoning, and a 15&nbsp;GiB footprint.</em></p>

[![MLX](https://img.shields.io/badge/runtime-MLX%200.32.1-0ea5e9)](#run-it)
[![DFlash 2](https://img.shields.io/badge/DFlash%202%20C1-33.37%20tok%2Fs-16a34a)](#lossless-dflash-2)
[![Speedup](https://img.shields.io/badge/speedup-1.236%C3%97-7c3aed)](#lossless-dflash-2)
[![Memory](https://img.shields.io/badge/DFlash%20peak-18.43%20GB-f59e0b)](#measured-on-mac)
[![Overthinking](https://img.shields.io/badge/overthinking-36%2F36%20pass-7c3aed)](#reasoning-that-stops)
[![License](https://img.shields.io/badge/license-Apache--2.0-64748b)](#license)

<p><strong>One model. Four native releases.</strong></p>

<p>
<a href="https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated">BF16</a> ·
<a href="https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated-NVFP4-DGX-Spark">NVFP4</a> ·
<a href="https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated-GGUF">GGUF</a> ·
<a href="https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated-MLX-4bit"><strong>MLX 4-bit</strong></a>
</p>

</div>

## Choose your build

| Release | Best for | Size / precision | Runtime |
|---|---|---|---|
| [BF16](https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated) | Maximum fidelity and further tuning | ~52 GB · BF16 | Transformers / vLLM |
| [NVFP4](https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated-NVFP4-DGX-Spark) | Fast single-DGX-Spark serving | ~19.2 GiB · W4A4 G16 | vLLM |
| [GGUF](https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated-GGUF) | Portable one-box inference + native MTP | ~17.6 GiB runtime set | llama.cpp |
| **MLX 4-bit — this repo** | Apple Silicon | ~15.0 GiB · affine 4-bit | MLX |

This is the directly loadable MLX release of
[`Jiunsong/SuperQwen3.8-27b-abliterated`](https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated),
built on the pinned
[`mlx-community/Qwen3.8-27B-4bit@3e6447f`](https://huggingface.co/mlx-community/Qwen3.8-27B-4bit/tree/3e6447f082e89cc7f0bc6e5441afd38dfce760ff).
It is not an adapter: the changed tensors were dequantized, the abliteration delta was
applied, and each affected matrix was quantized back into native MLX weight/scales/biases.
The source edit is the verified rank-4 OBLITERATUS recipe built from 842 canonical
harmful/harmless pairs: exactly 100 BF16 tensors changed, while the vision tower and MTP
weights remained exact.

## Release highlights

| | |
|---|---|
| **Format** | MLX affine 4-bit, group size 64, three safetensors shards (~14.96 GiB) |
| **Autoregressive C1** | **26.797 / 27.225 tok/s**, median **27.011 tok/s** |
| **Lossless DFlash 2 C1** | **33.199 / 33.550 tok/s**, median **33.374 tok/s**, **1.2356×** over AR |
| **Memory** | **18.435 GB** peak with the 4-bit DFlash draft; **16.062 GB** in the full quality suite |
| **Abliteration transfer** | 100 source tensors → 300 native MLX weight/scales/biases entries |
| **Reasoning regression gate** | Template v3; **36/36 PASS** across default, low, medium, and xhigh |
| **Behavior** | Parent refusal **30/32 → 0/32**; capability 7/8, tool PASS, benign-sensitive refusal 0/8 |
| **Multimodal** | Real local 64×64 red-PNG inference PASS through MLX-VLM 0.6.16 |

## Why this build

- **Runs the 27B model locally on a Mac** without a server-class GPU.
- **Fast where it matters:** the headline number is C1 single-stream decode, not a concurrency aggregate.
- **Lossless speculative decoding:** every tested DFlash block preserved the exact greedy
  token sequence; block 3 was the fastest release-eligible profile.
- **Reasoning that stops:** explicit `xhigh` is preserved, but carries the same repeat/restart stop guard as the BF16 release.
- **No loose delta at runtime:** the abliteration edit is baked into the MLX shards.
- **Auditable conversion:** the pinned base revision, every changed key, and shard hashes are recorded in `mlx_requantization_manifest.json`.

## Measured on Mac

Measured locally on an Apple M5 Max with MLX 0.32.1, MLX-LM 0.31.3, and
MLX-VLM 0.6.16. The release benchmark uses one stream, a 256-token prompt,
256 fixed generation tokens, greedy decoding, one warmup, and two timed trials.

| Trial | AR C1 | DFlash 2 block 3 C1 | Greedy identity |
|---:|---:|---:|---:|
| 1 | 26.797 tok/s | **33.199 tok/s** | Exact |
| 2 | 27.225 tok/s | **33.550 tok/s** | Exact |
| **Median** | **27.011 tok/s** | **33.374 tok/s** | **Exact** |

The quality run loaded the model once, executed all 53 checks in 186.6 seconds, and
peaked at 16.06 GB. A separate local gate ran the same fixed 32-prompt OBLITERATUS
sample and the real image path: harmful refusal was **0/32**, empty output was **0/32**,
and vision passed. Exact reports and hashes are under `evidence/`.

## Reasoning that stops

The upstream template's implicit reasoning default is changed to bounded `medium`.
Explicit `xhigh` remains available and tells the model to stop once the answer is
established instead of repeating or restarting its deliberation. Template revision 3
adds an explicit 512-token internal-reasoning target for short or routine tasks.

| Effort | Deterministic overthinking gate | Median reasoning tokens | Maximum |
|---|---:|---:|---:|
| default | **9/9** | 45 | 112 |
| low | **9/9** | 36 | 91 |
| medium | **9/9** | 45 | 112 |
| xhigh | **9/9** | 60 | 233 |
| **Total** | **36/36 PASS** |  |  |

## Run it

```bash
python3.12 -m pip install 'mlx==0.32.1' 'mlx-lm==0.31.3' 'mlx-vlm==0.6.16'

python3.12 -m mlx_lm generate \
  --model Jiunsong/SuperQwen3.8-27b-abliterated-MLX-4bit \
  --prompt "Explain why speculative decoding is lossless." \
  --max-tokens 512
```

Use explicit bounded or deep reasoning through the chat-template configuration:

```bash
python3.12 -m mlx_lm generate \
  --model Jiunsong/SuperQwen3.8-27b-abliterated-MLX-4bit \
  --chat-template-config '{"enable_thinking":true,"reasoning_effort":"xhigh","preserve_thinking":false}' \
  --prompt "Solve this carefully: ..." \
  --max-tokens 4096
```

Serve an OpenAI-compatible local endpoint:

```bash
python3.12 -m mlx_lm server \
  --model Jiunsong/SuperQwen3.8-27b-abliterated-MLX-4bit \
  --host 127.0.0.1 \
  --port 8080
```

## Lossless DFlash 2

[`incoai/Qwen3.8-27B-DFlash2`](https://huggingface.co/incoai/Qwen3.8-27B-DFlash2)
was loaded through the Qwen3 DFlash 2 path in MLX-VLM. Blocks 2 through 8 were tested;
all seven reproduced the autoregressive greedy token IDs exactly. Block 3 won the
same-run C1 comparison at **33.374 tok/s**, versus **27.011 tok/s** AR.

| Block | Median C1 | Lossless | Faster than AR |
|---:|---:|:---:|:---:|
| 2 | 31.595 tok/s | Yes | Yes |
| **3** | **33.374 tok/s** | **Yes** | **Yes** |
| 4 | 29.733 tok/s | Yes | Yes |
| 5 | 29.021 tok/s | Yes | Yes |
| 6 | 27.994 tok/s | Yes | Yes |
| 7 | 27.047 tok/s | Yes | Yes |
| 8 | 26.269 tok/s | Yes | No |

The draft is quantized at runtime to affine 4-bit, group size 64. Its pinned weight
SHA-256 is `67fc76d68dc5a9415511a4f394ef744d67510cd20e93b37cc2cc7d28e4bab65c`.
The bundled reproducibility files identify the exact MLX-VLM source revision and patch.

## Quantization and integrity

- Mode: **affine 4-bit**, group size **64**.
- Pinned MLX base index SHA-256: `13b840162b4cb35c66fef7df072f7dbb4717908204364f5e5d9f9655a2758fa8`.
- Pinned delta manifest SHA-256: `cf9bedf4dd833b2c612b363497f878bee3007f73bb77d2618f9962ff3e05d576`.
- Conversion manifest SHA-256: `a90e5475ad7b6fa655b4dcd2d2b528d1ed4b499f2a10a996d4f49b8399b44357`.
- Three output shards are independently hashed in both the manifest and `SHA256SUMS.json`.

## Evidence identities

| Evidence | SHA-256 |
|---|---|
| Lossless C1 AR + DFlash 2 benchmark | `01c3d45ab0e2e31abf15e9ae12d59df0a1981a51194df3f16f11f38301aaa50a` |
| MLX quality and overthinking gate | `a575139e8cd5a8beb4ca25660c801f61e141ad07c1f005ed8a60f0d8d0134465` |
| MLX harmful-refusal + real-image gate | `fcac3f1b415bc28ab97dc67535d1cc910f8c7cb8eef0ec3aec0d78b6a9d8fd36` |
| MLX requantization manifest | `a90e5475ad7b6fa655b4dcd2d2b528d1ed4b499f2a10a996d4f49b8399b44357` |

## Limitations

- Four-bit affine quantization can regress tasks outside the measured suite.
- Capability is 7/8, matching the accepted paired-parent floor; it is not presented as 8/8.
- DFlash 2 requires the bundled/pinned MLX-VLM Qwen3 DFlash patch; stock runtimes may
  not expose this draft path yet.
- The 33.374 tok/s number is a same-run M5 Max C1 measurement, not a guarantee for
  every Apple chip or thermal state.
- Local speed varies with Apple chip, memory pressure, prompt length, and MLX version.

## License

Apache-2.0, following the upstream Qwen3.8 release.
