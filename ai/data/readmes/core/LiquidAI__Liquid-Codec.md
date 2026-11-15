---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: feature-extraction
tags:
- liquid
- lfm3
- audio
- audio-codec
- speech
- streaming
- edge
- multilingual
- custom_code
language:
- en
- zh
- de
- fr
- ja
- ko
---


<div align="center">
  <img
    src="https://huggingface.co/LiquidAI/LFM3-1.7B/resolve/main/assets/liquid-ai-banner.webp"
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: block; margin: 0;"
  />
  <div align="center" style="display: flex; justify-content: center; align-items: center; gap: 1.25em; margin: 8px 0 1.7rem; padding: 0; line-height: 1.3;">
    <a href="https://console.liquid.ai/dashboard" style="display: inline-flex; align-items: center; gap: 6px;"><img src="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke-width=%222.2%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22%3E%3Cstyle%3Epath%7Bstroke:%23000%7D%40media (prefers-color-scheme:dark)%7Bpath%7Bstroke:%23d1d5dc%7D%7D%3C/style%3E%3Cpath d=%22m8 6-6 6 6 6m8-12 6 6-6 6m-2-14-4 16%22/%3E%3C/svg%3E" width="16" height="16" alt="" aria-hidden="true" style="display: block; flex: 0 0 16px; width: 16px; height: 16px; margin: 0;" /><strong>API</strong></a>
    <a href="https://playground.liquid.ai/talk" style="display: inline-flex; align-items: center; gap: 6px;"><img src="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke-width=%222.2%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22%3E%3Cstyle%3Epath%7Bstroke:%23000%7D%40media (prefers-color-scheme:dark)%7Bpath%7Bstroke:%23d1d5dc%7D%7D%3C/style%3E%3Cpath transform=%22translate(3 0)%22 d=%22M8 5.5v13L19 12 8 5.5Z%22/%3E%3C/svg%3E" width="16" height="16" alt="" aria-hidden="true" style="display: block; flex: 0 0 16px; width: 16px; height: 16px; margin: 0;" /><strong>Try</strong></a>
    <a href="https://docs.liquid.ai/lfm/getting-started/welcome" style="display: inline-flex; align-items: center; gap: 6px;"><img src="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke-width=%222.2%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22%3E%3Cstyle%3Epath%7Bstroke:%23000%7D%40media (prefers-color-scheme:dark)%7Bpath%7Bstroke:%23d1d5dc%7D%7D%3C/style%3E%3Cpath d=%22M12 6c-3-2-6-2.5-10-2v15c4-.5 7 0 10 2m0-15c3-2 6-2.5 10-2v15c-4-.5-7 0-10 2V6Z%22/%3E%3C/svg%3E" width="16" height="16" alt="" aria-hidden="true" style="display: block; flex: 0 0 16px; width: 16px; height: 16px; margin: 0;" /><strong>Docs</strong></a>
    <a href="https://www.liquid.ai/blog/liquidcodec" style="display: inline-flex; align-items: center; gap: 6px;"><img src="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke-width=%222.2%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22%3E%3Cstyle%3Epath%7Bstroke:%23000%7D%40media (prefers-color-scheme:dark)%7Bpath%7Bstroke:%23d1d5dc%7D%7D%3C/style%3E%3Cpath transform=%22translate(1 0)%22 d=%22m16 3 5 5L8 21H3v-5L16 3Zm-3 3 5 5%22/%3E%3C/svg%3E" width="16" height="16" alt="" aria-hidden="true" style="display: block; flex: 0 0 16px; width: 16px; height: 16px; margin: 0;" /><strong>Blog</strong></a>
  </div>
</div>

# LiquidCodec

LiquidCodec is a **compact, streaming audio codec** that compresses speech into discrete tokens and converts them back into audio. It is the audio tokenizer behind [LFM3-Audio-2B](https://huggingface.co/LiquidAI/LFM3-Audio-2B) and [LFM3-Omni-2B](https://huggingface.co/LiquidAI/LFM3-Omni-2B).


- **Easy to predict:** LiquidCodec’s grouped finite scalar quantization (GFSQ) produces codebooks with no sequential dependencies, so speech models can predict all codebooks of a frame in parallel.
- **Fast:** at FP32 on a single CPU thread of an Apple M4 Max, LiquidCodec encodes at about **361× real time** and decodes at about **87× real time**.
- **High fidelity:** best ViSQOL and lowest mel distance of all compared codecs tested on eight reconstruction test sets.
- **Better speech generation:** in matched TTS experiments, models trained on LiquidCodec tokens reach the highest naturalness (UTMOSv2) on all eight test sets.
- **Edge-ready:** decoder-only quantization-aware training lets the decoder run in Q4_0 with a 3.5× smaller footprint and minimal quality loss.

Find more information in [our blog post](https://www.liquid.ai/blog/liquidcodec).

## Model details
<hr style="margin: -0.7em 0 1.2em 0; border: 0; border-top: 1px solid rgba(127, 127, 127, 0.3);" />

<table style="width: 100%; display: table; border: 0; border-radius: 0; border-collapse: collapse;">
<thead style="border: 0;">
<tr style="border: 0;">
<th scope="col" style="text-align: left; padding: 0.55em 0.75em; border: 0; border-bottom: 1px solid rgba(127, 127, 127, 0.55);">Property</th>
<th scope="col" style="text-align: left; padding: 0.55em 0.75em; border: 0; border-bottom: 1px solid rgba(127, 127, 127, 0.55);">Specification</th>
</tr>
</thead>
<tbody style="border: 0;">
<tr style="border: 0;">
<th scope="row" style="text-align: left; background-color: transparent; font-weight: 400; border: 0; padding: 0.55em 0.75em;"><strong>Parameters</strong></th>
<td style="border: 0; padding: 0.55em 0.75em;">~74M</td>
</tr>
<tr style="border: 0;">
<th scope="row" style="text-align: left; background-color: transparent; font-weight: 400; border: 0; padding: 0.55em 0.75em;"><strong>Architecture</strong></th>
<td style="border: 0; padding: 0.55em 0.75em;">Symmetric, fully causal LFM3 encoder and decoder with grouped finite scalar quantization (GFSQ)</td>
</tr>
<tr style="border: 0;">
<th scope="row" style="text-align: left; background-color: transparent; font-weight: 400; border: 0; padding: 0.55em 0.75em;"><strong>Input / output</strong></th>
<td style="border: 0; padding: 0.55em 0.75em;">24 kHz mono speech</td>
</tr>
<tr style="border: 0;">
<th scope="row" style="text-align: left; background-color: transparent; font-weight: 400; border: 0; padding: 0.55em 0.75em;"><strong>Frame rate</strong></th>
<td style="border: 0; padding: 0.55em 0.75em;">12.5 Hz</td>
</tr>
<tr style="border: 0;">
<th scope="row" style="text-align: left; background-color: transparent; font-weight: 400; border: 0; padding: 0.55em 0.75em;"><strong>Tokens per frame</strong></th>
<td style="border: 0; padding: 0.55em 0.75em;">12 (one per codebook)</td>
</tr>
<tr style="border: 0;">
<th scope="row" style="text-align: left; background-color: transparent; font-weight: 400; border: 0; padding: 0.55em 0.75em;"><strong>Bitrate</strong></th>
<td style="border: 0; padding: 0.55em 0.75em;">≈ 1.65 kbps</td>
</tr>
<tr style="border: 0;">
<th scope="row" style="text-align: left; background-color: transparent; font-weight: 400; border: 0; padding: 0.55em 0.75em;"><strong>Streaming</strong></th>
<td style="border: 0; padding: 0.55em 0.75em;">Streaming encoding and decoding</td>
</tr>
<tr style="border: 0;">
<th scope="row" style="text-align: left; background-color: transparent; font-weight: 400; border: 0; padding: 0.55em 0.75em;"><strong>Training data</strong></th>
<td style="border: 0; padding: 0.55em 0.75em;">264k hours across 107 languages</td>
</tr>
<tr style="border: 0;">
<th scope="row" style="text-align: left; background-color: transparent; font-weight: 400; border: 0; padding: 0.55em 0.75em;"><strong>License</strong></th>
<td style="border: 0; padding: 0.55em 0.75em;"><a href="https://huggingface.co/LiquidAI/Liquid-Codec/blob/main/LICENSE">LFM Open License v1.0</a></td>
</tr>
</tbody>
</table>

LiquidCodec is trained and evaluated on speech. Its quality on music, singing or environmental sound has not been evaluated.

## Inference
<hr style="margin: -0.7em 0 1.2em 0; border: 0; border-top: 1px solid rgba(127, 127, 127, 0.3);" />

This repository contains the BF16 codec weights for use with Transformers. Quantized versions of the decoder (Q4_0 / Q4_K_M / Q8_0) are not published separately; they ship inside [LFM3-Audio-2B-GGUF](https://huggingface.co/LiquidAI/LFM3-Audio-2B-GGUF) and [LFM3-Omni-2B-GGUF](https://huggingface.co/LiquidAI/LFM3-Omni-2B-GGUF) for on-device inference with [llama.cpp](https://docs.liquid.ai/deployment/on-device/llama-cpp).

### Remote-code loading

The repository includes the codec configuration and model implementation, so it can be loaded with `AutoModel`:

```python
import torch
from transformers import AutoModel

codec = AutoModel.from_pretrained(
    "LiquidAI/Liquid-Codec",
    trust_remote_code=True,
    dtype=torch.bfloat16,
    device_map="cuda",
)
waveform = torch.randn(1, 24_000 * 3, device="cuda")  # 24 kHz
codes = codec.encode(waveform).audio_codes
reconstructed = codec.decode(codes).audio_values
```

### Native loading and streaming

```python
import torch
from transformers import LiquidCodecModel, LiquidCodecStreamingCache

codec = LiquidCodecModel.from_pretrained("LiquidAI/Liquid-Codec", dtype=torch.bfloat16, device_map="cuda")

waveform = torch.randn(1, 24_000 * 3, device="cuda")  # 24 kHz
codes = codec.encode(waveform).audio_codes  # (1, 12, 38)
reconstructed = codec.decode(codes).audio_values  # (1, 38 * 1920), float32

# streaming synthesis: every chunk returns the samples that no later frame changes any more
cache = LiquidCodecStreamingCache(codec.config)
chunks = [codec.decode(codes[..., i : i + 1], cache, finalize=False).audio_values for i in range(codes.shape[-1])]
chunks.append(codec.decode(codes[..., :0], cache, finalize=True).audio_values)
streamed = torch.cat(chunks, dim=-1)
```

## Performance
<hr style="margin: -0.7em 0 1.2em 0; border: 0; border-top: 1px solid rgba(127, 127, 127, 0.3);" />

### Speed

FP32, single-threaded CPU inference on a MacBook Pro with an Apple M4 Max. RTF = processing time ÷ audio duration (lower is faster).

| Tokenizer | Codebooks | Enc. RTF ↓ | Dec. RTF ↓ |
|---|---|---|---|
| **LiquidCodec** | 12 | **0.0028 ± 0.0001** | **0.0115 ± 0.0001** |
| X-Codec 2 | 1 | 0.7359 ± 0.0103 | 0.0379 ± 0.0009 |
| NanoCodec | 13 | 0.2145 ± 0.0057 | 0.2543 ± 0.0061 |
| Mimi | 12 (truncated) | 0.0361 ± 0.0004 | 0.0329 ± 0.0005 |

### Reconstruction and zero-shot TTS

LiquidCodec achieves the best ViSQOL and lowest mel distance on all eight reconstruction test sets, and remains the best on both with a Q4_0 decoder. TTS models trained on LiquidCodec tokens reach the highest UTMOSv2 on all eight test sets and the best WER/CER on four of eight.

| Test set | Tokenizer | SQMOS ↑ | PESQ (WB) ↑ | Mel dist. ↓ | SECS (ECAPA2) ↑ | ViSQOL ↑ | Recon. CER (%) ↓ | TTS WER/CER (%) ↓ | TTS UTMOSv2 ↑ |
|---|---|---|---|---|---|---|---|---|---|
| LibriSpeech test-clean (EN) | LiquidCodec BF16 | 4.442 | 2.640 | 0.120 | 0.785 | 4.319 | 0.89 | 3.15 | 3.31 |
| | LiquidCodec Q4_0 | 4.445 | 2.577 | 0.121 | 0.781 | 4.292 | 0.89 | 3.18 | 3.22 |
| | X-Codec 2 | 4.436 | 2.434 | 0.123 | 0.754 | 4.119 | 0.88 | 4.19 | 3.27 |
| | NanoCodec | 4.486 | 2.942 | 0.122 | 0.836 | 4.219 | 0.76 | 3.32 | 3.19 |
| | Mimi (12 cb) | 4.364 | 2.615 | 0.160 | 0.714 | 4.031 | 0.87 | 6.27 | 2.89 |
| Seed-TTS (EN) | LiquidCodec BF16 | 4.463 | 2.326 | 0.130 | 0.751 | 4.369 | 0.86 | 3.50 | 3.39 |
| | LiquidCodec Q4_0 | 4.460 | 2.271 | 0.131 | 0.744 | 4.341 | 0.86 | 3.54 | 3.31 |
| | X-Codec 2 | 4.436 | 2.099 | 0.140 | 0.745 | 4.105 | 0.86 | 5.65 | 3.24 |
| | NanoCodec | 4.467 | 2.599 | 0.136 | 0.799 | 4.304 | 0.73 | 3.95 | 3.29 |
| | Mimi (12 cb) | 4.347 | 2.396 | 0.163 | 0.722 | 4.124 | 1.01 | 6.15 | 2.98 |
| Seed-TTS (ZH) | LiquidCodec BF16 | 4.407 | 2.429 | 0.118 | 0.776 | 4.313 | 6.93 | 1.19 | 3.01 |
| | LiquidCodec Q4_0 | 4.393 | 2.375 | 0.119 | 0.768 | 4.285 | 7.04 | 1.20 | 2.92 |
| | X-Codec 2 | 4.387 | 2.237 | 0.126 | 0.823 | 4.064 | 7.30 | 1.44 | 2.85 |
| | NanoCodec | 4.407 | 2.606 | 0.122 | 0.811 | 4.189 | 6.41 | 1.27 | 2.88 |
| | Mimi (12 cb) | 4.198 | 2.401 | 0.152 | 0.702 | 3.992 | 7.59 | 2.12 | 2.53 |
| FLEURS (DE) | LiquidCodec BF16 | 4.237 | 2.434 | 0.120 | 0.807 | 4.207 | 3.65 | 5.30 | 3.20 |
| | LiquidCodec Q4_0 | 4.224 | 2.391 | 0.121 | 0.818 | 4.162 | 3.67 | 5.38 | 3.12 |
| | X-Codec 2 | 4.256 | 2.085 | 0.125 | 0.661 | 3.942 | 4.39 | 5.44 | 3.08 |
| | NanoCodec | 4.202 | 2.597 | 0.129 | 0.822 | 4.009 | 3.74 | 5.36 | 3.01 |
| | Mimi (12 cb) | 4.087 | 2.393 | 0.170 | 0.698 | 3.627 | 5.36 | 6.14 | 2.78 |
| FLEURS (FR) | LiquidCodec BF16 | 4.301 | 2.315 | 0.127 | 0.825 | 4.242 | 5.27 | 6.91 | 3.12 |
| | LiquidCodec Q4_0 | 4.302 | 2.262 | 0.128 | 0.820 | 4.212 | 5.27 | 5.26 | 3.04 |
| | X-Codec 2 | 4.317 | 2.019 | 0.134 | 0.606 | 3.914 | 6.84 | 6.37 | 3.01 |
| | NanoCodec | 4.305 | 2.500 | 0.137 | 0.824 | 4.072 | 5.06 | 7.72 | 3.02 |
| | Mimi (12 cb) | 3.876 | 2.207 | 0.192 | 0.710 | 3.758 | 15.95 | 8.73 | 2.67 |
| FLEURS (ZH) | LiquidCodec BF16 | 4.343 | 2.479 | 0.121 | 0.794 | 4.273 | 7.60 | 8.82 | 3.02 |
| | LiquidCodec Q4_0 | 4.339 | 2.436 | 0.123 | 0.782 | 4.249 | 7.56 | 7.84 | 2.94 |
| | X-Codec 2 | 4.335 | 2.307 | 0.127 | 0.559 | 4.047 | 8.24 | 7.86 | 2.86 |
| | NanoCodec | 4.334 | 2.679 | 0.133 | 0.845 | 4.164 | 6.68 | 7.45 | 2.91 |
| | Mimi (12 cb) | 3.916 | 2.179 | 0.191 | 0.616 | 3.837 | 9.51 | 8.35 | 2.53 |
| FLEURS (JA) | LiquidCodec BF16 | 4.347 | 2.233 | 0.122 | 0.766 | 4.162 | 6.80 | 7.29 | 3.05 |
| | LiquidCodec Q4_0 | 4.327 | 2.188 | 0.123 | 0.756 | 4.120 | 6.83 | 7.32 | 2.98 |
| | X-Codec 2 | 4.354 | 2.045 | 0.130 | 0.497 | 3.805 | 7.02 | 5.40 | 2.94 |
| | NanoCodec | 4.378 | 2.415 | 0.129 | 0.695 | 4.089 | 6.02 | 5.58 | 2.84 |
| | Mimi (12 cb) | 4.332 | 2.232 | 0.166 | 0.658 | 3.982 | 12.13 | 6.27 | 2.49 |
| FLEURS (KO) | LiquidCodec BF16 | 4.217 | 2.637 | 0.117 | 0.803 | 4.176 | 4.45 | 8.36 | 2.97 |
| | LiquidCodec Q4_0 | 4.214 | 2.599 | 0.118 | 0.800 | 4.146 | 4.30 | 6.71 | 2.88 |
| | X-Codec 2 | 4.214 | 2.299 | 0.128 | 0.591 | 3.870 | 5.08 | 6.22 | 2.87 |
| | NanoCodec | 4.212 | 2.589 | 0.137 | 0.769 | 4.018 | 3.41 | 5.96 | 2.86 |
| | Mimi (12 cb) | 3.843 | 2.165 | 0.178 | 0.543 | 3.530 | 9.37 | 9.81 | 2.54 |

<details>
<summary><small>Evaluation details</small></summary>

<p><small>
<strong>Reconstruction</strong>: each recording is encoded into tokens and decoded back into speech; the reconstruction is compared against the original. CER is measured on the reconstructed audio.<br>
<strong>Zero-shot TTS</strong>: for each tokenizer, a TTS model is trained with identical data (101k hours across six languages), architecture and compute. The backbone is initialized from LFM3-1.7B, with a six-layer, 1,024-dim autoregressive depth decoder predicting the codebooks within each frame. Each model is trained with identical batches in identical order. Only the token-specific embeddings and output heads change. At evaluation, models receive text without a reference speech prompt; scores aggregate three generation seeds.<br>
<strong>Backbone check</strong>: repeating the TTS experiment with a Qwen3-1.7B backbone gives consistent results.<br>
<strong>Q4_0</strong>: decoder quantized to 4 bits after decoder-only quantization-aware training.
</small></p>

</details>

## Architecture
<hr style="margin: -0.7em 0 1.2em 0; border: 0; border-top: 1px solid rgba(127, 127, 127, 0.3);" />

**Symmetric LFM3 encoder and decoder:** both are built from blocks of the LFM3 architecture, which is optimized for performance on the edge. The encoder mirrors the decoder exactly and is fully causal, so tokenization is as lightweight as detokenization. This suits real-time, low-latency streaming.

**Spectral processing:** the decoder predicts spectral coefficients directly. This avoids progressive upsampling with learned transposed convolutions, a costly step in similar codecs.

**Grouped finite scalar quantization:** FSQ rounds each dimension of a feature vector to one of a fixed number of values. GFSQ splits the features into groups that are quantized independently, and each group yields one token. Without RVQ's chain of dependencies between codebooks, multiple audio tokens can be predicted in parallel with MaskGIT-based methods.

## Citation
<hr style="margin: -0.7em 0 1.2em 0; border: 0; border-top: 1px solid rgba(127, 127, 127, 0.3);" />

```bibtex
@article{liquidAI2026liquidcodec,
  author  = {Liquid AI},
  title   = {LiquidCodec: High-Fidelity Audio Tokenization Optimized for Speed},
  journal = {Liquid AI Blog},
  year    = {2026},
  note    = {www.liquid.ai/blog/liquidcodec},
}
```

For questions and feedback, join [Discord](https://discord.com/invite/liquid-ai). For custom deployment and fine-tuning support, [contact Liquid AI](https://www.liquid.ai/connect?utm_source=huggingface&utm_medium=referral&utm_campaign=huggingface).
