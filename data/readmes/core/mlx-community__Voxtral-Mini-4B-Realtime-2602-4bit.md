---
base_model: mistralai/Voxtral-Mini-4B-Realtime-2602
language:
  - ar
  - de
  - en
  - es
  - fr
  - hi
  - it
  - nl
  - pt
  - zh
  - ja
  - ko
  - ru
library_name: mlx
license: apache-2.0
pipeline_tag: automatic-speech-recognition
tags:
  - mlx
  - mlx-audio
  - speech-to-text
  - streaming
  - realtime
---

# Voxtral Mini 4B Realtime 

This is a **4-bit quantized** [MLX](https://github.com/ml-explore/mlx) conversion of [mistralai/Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602), Mistral AI's streaming speech-to-text model.

Runs via [mlx-audio](https://github.com/Blaizzy/mlx-audio).

## Key Details

| | |
|---|---|
| **Parameters** | 4B (~3.4B LM + ~0.6B Audio Encoder) |
| **Quantization** | int4 |
| **Base model** | [mistralai/Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602) |
| **Languages** | 13 (Arabic, German, English, Spanish, French, Hindi, Italian, Dutch, Portuguese, Chinese, Japanese, Korean, Russian) |
| **License** | Apache 2.0 |

See also: [fp16 variant](https://huggingface.co/mlx-community/Voxtral-Mini-4B-Realtime-2602-fp16)

## Usage

```bash
pip install mlx-audio[stt]
```

```python
from mlx_audio.stt.utils import load

model = load("mlx-community/Voxtral-Mini-4B-Realtime-2602-4bit")

# Transcribe audio
result = model.generate("audio.wav")
print(result.text)

# Streaming transcription
for chunk in model.generate("audio.wav", stream=True):
    print(chunk, end="", flush=True)

# Adjust transcription delay (lower = faster but less accurate)
result = model.generate("audio.wav", transcription_delay_ms=480)
```

## Recommended Settings

| Setting | Value | Notes |
|---|---|---|
| Temperature | `0.0` | Always use greedy decoding |
| Transcription delay | `480ms` | Sweet spot of accuracy vs. latency |
| Delay range | `80ms` – `2400ms` | Multiples of 80ms |

## Benchmarks (from upstream)

### FLEURS (13 languages, WER%)

| Delay | AVG | EN | FR | DE | ES | ZH | JA | KO |
|---|---|---|---|---|---|---|---|---|
| 160ms | 12.60 | 6.46 | 9.75 | 9.50 | 5.34 | 17.67 | 19.17 | 19.81 |
| **480ms** | **8.72** | **4.90** | **6.42** | **6.19** | **3.31** | **10.45** | **9.59** | **15.74** |
| 960ms | 7.70 | 4.34 | 5.68 | 4.87 | 2.98 | 8.99 | 6.80 | 14.90 |
| 2400ms | 6.73 | 4.05 | 5.23 | 4.15 | 2.71 | 8.48 | 5.50 | 14.30 |

### Long-form English (WER%)

| Delay | Meanwhile | Earnings-21 | Earnings-22 | TEDLIUM |
|---|---|---|---|---|
| **480ms** | **5.05** | **10.23** | **12.30** | **3.17** |

## Architecture

- **Causal audio encoder** (~0.6B) with sliding window attention — enables true streaming
- **Language model decoder** (~3.4B) based on Ministral-3B with adaptive RMS norm conditioned on transcription delay
- **4x downsampling** from encoder to decoder (frame rate = 12.5 Hz)
- Both components use sliding window attention for unbounded audio length

## More Info

- [Original model card](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)
- [mlx-audio GitHub](https://github.com/Blaizzy/mlx-audio)
- [Mistral announcement](https://mistral.ai/news/voxtral-transcribe-2)