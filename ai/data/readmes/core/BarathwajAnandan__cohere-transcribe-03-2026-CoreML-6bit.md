---
license: gpl-3.0
base_model: CohereLabs/cohere-transcribe-03-2026
pipeline_tag: automatic-speech-recognition
library_name: coreml
tags:
  - coreml
  - mlpackage
  - automatic-speech-recognition
  - speech-recognition
  - transcription
  - audio
  - apple
  - ios
  - macos
  - on-device
  - palettization
  - 6-bit
  - quantized
language:
  - en
  - ar
  - de
  - el
  - es
  - fr
  - it
  - ja
  - ko
  - nl
  - pl
  - pt
  - vi
  - zh
---

# Cohere Transcribe 03-2026 - CoreML (6-bit Palettized)

This is a **CoreML** conversion of [CohereLabs/cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026) with **6-bit palettization** for on-device speech recognition on Apple Silicon (macOS / iOS).

## Model Details

| Property | Value |
|----------|-------|
| **Base model** | CohereLabs/cohere-transcribe-03-2026 |
| **Format** | CoreML `.mlpackage` |
| **Precision** | Float16 + 6-bit palettized weights |
| **Compression** | 2.7× smaller than FP16 |
| **Total size** | ~1.4 GB |
| **Compute** | Apple GPU (recommended), CPU, or Neural Engine |
| **Min deployment** | macOS 13 / iOS 16 |

## Benchmark Results

### Accuracy — LibriSpeech test-clean

| Variant | Samples | WER vs Ground Truth | Size |
|---------|---------|-------------------|------|
| **Palettize6 (this model)** | **2619/2620 (full)** | **2.58%** | **1.4 GB** |
| FP16 (baseline) | 200 | 2.63% | 3.8 GB |
| Palettize8 | 200 | 2.65% | 1.85 GB |

### Speed — Apple M4 Pro, GPU compute

| Metric | Value |
|--------|-------|
| Real-time factor | **35.9× real-time** |
| 30s audio inference | ~836 ms |

## Files

| File | Size | Description |
|------|------|-------------|
| `cohere_frontend.mlpackage` | 1.5 MB | Audio feature extraction (pre-emphasis + mel spectrogram) |
| `cohere_encoder.mlpackage` | 1.3 GB | Encoder (audio → hidden states) |
| `cohere_decoder_fullseq_masked.mlpackage` | 109 MB | Full-sequence decoder (first token) |
| `cohere_decoder_cached.mlpackage` | 109 MB | KV-cached decoder (autoregressive generation) |
| `coreml_manifest.json` | 292 KB | Pipeline config (tokenizer, chunking, dimensions) |

## Usage

### Swift CLI

```bash
pure_coreml_asr_cli \
  --audio input.wav \
  --artifacts-dir <path-to-this-repo> \
  --compute gpu \
  --decoder-mode cached
```

### Swift App Integration

1. Add all `.mlpackage` files to your Xcode project
2. Load `coreml_manifest.json` at runtime for tokenizer IDs and pipeline config
3. Use `MLModel` with `.computeUnits = .cpuAndGPU` for best performance
4. Process audio in **30-second chunks** with **5-second overlap** (params in manifest)

### Pipeline Architecture

```
Audio → Frontend (mel spectrogram) → Encoder → Decoder (autoregressive) → Text
```

The decoder runs in two phases:
1. **Full-sequence masked** decoder generates the first token from encoder output
2. **KV-cached** decoder generates subsequent tokens autoregressively

## Compression Details

6-bit palettization clusters each weight tensor into 2⁶ = 64 centroids via k-means, storing only 6-bit indices + a small lookup table. This achieves 2.7× compression over FP16 with virtually no accuracy or speed loss on Apple GPU.

Applied to: encoder, full-sequence decoder, and cached decoder. The frontend remains FP32 (tiny model, no benefit from compression).

## License

This converted model is released under GPL-3.0.

The upstream base model, [CohereLabs/cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026), is Apache-2.0 licensed. This repo contains the CoreML conversion and quantized derivative artifacts.
