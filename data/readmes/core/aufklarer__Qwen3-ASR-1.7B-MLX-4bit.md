---
license: apache-2.0
language:
- en
- zh
- ja
- ko
- fr
- de
- es
tags:
- speech
- asr
- mlx
- qwen3
library_name: mlx
base_model: Qwen/Qwen3-ASR-1.7B
pipeline_tag: automatic-speech-recognition
---

# Qwen3-ASR-1.7B — MLX 4-bit

MLX 4-bit quantized conversion of [Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) for Apple Silicon inference.

## Model Details

| Detail | Value |
|--------|-------|
| Architecture | Whisper-style audio encoder + Qwen3 text decoder |
| Parameters | 1.7B |
| Quantization | 4-bit (group_size=64, text decoder only) |
| Audio encoder | float16 (24 layers, 1024 dim, 16 heads) |
| Size | ~2.1 GB |
| Languages | Multilingual (EN, ZH, JA, KO, FR, DE, ES, and more) |

## Usage

```swift
let model = try await Qwen3ASRModel.fromPretrained(
    modelId: "aufklarer/Qwen3-ASR-1.7B-MLX-4bit"
)
let text = model.transcribe(audio: samples, sampleRate: 16000)
```

```bash
audio transcribe audio.wav --model aufklarer/Qwen3-ASR-1.7B-MLX-4bit
```

## Variants

| Variant | Size | Model ID |
|---------|------|----------|
| **4-bit** | **~2.1 GB** | **aufklarer/Qwen3-ASR-1.7B-MLX-4bit** |
| 8-bit | ~3.2 GB | [aufklarer/Qwen3-ASR-1.7B-MLX-8bit](https://huggingface.co/aufklarer/Qwen3-ASR-1.7B-MLX-8bit) |
| 0.6B 4-bit | ~680 MB | [aufklarer/Qwen3-ASR-0.6B-MLX-4bit](https://huggingface.co/aufklarer/Qwen3-ASR-0.6B-MLX-4bit) |
| 0.6B 8-bit | ~1.0 GB | [aufklarer/Qwen3-ASR-0.6B-MLX-8bit](https://huggingface.co/aufklarer/Qwen3-ASR-0.6B-MLX-8bit) |

## Links

- **Swift library**: [soniqo/speech-swift](https://github.com/soniqo/speech-swift)
- **Base model**: [Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B)

---

---

- **Guide**: [soniqo.audio/guides/transcribe](https://soniqo.audio/guides/transcribe)
- **Docs**: [soniqo.audio](https://soniqo.audio)
- **GitHub**: [soniqo/speech-swift](https://github.com/soniqo/speech-swift)
