---
license: apache-2.0
language:
- en
- fr
- de
- es
- it
- pt
- nl
- pl
- el
- ar
- ja
- zh
- vi
- ko
base_model: CohereLabs/cohere-transcribe-03-2026
library_name: mlx
pipeline_tag: automatic-speech-recognition
tags:
- mlx
- speech-recognition
- automatic-speech-recognition
---

# Cohere Transcribe 2B — MLX 8-bit affine

MLX weights for [Cohere Transcribe 2B](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026),
ready for local speech-to-text with
[speech-swift](https://github.com/soniqo/speech-swift).

| Parameters | Precision | Sample rate | Languages |
|---:|---:|---:|---:|
| 2B | 8-bit affine | 16 kHz | 14 |

## Files

| File | Description |
|---|---|
| `model*.safetensors` | MLX model weights |
| `config.json` | Model and runtime configuration |
| `tokenizer.model` and tokenizer JSON files | SentencePiece tokenizer data |

## Usage

```bash
speech transcribe recording.wav --engine cohere --model int8
```

```swift
import CohereTranscribeASR

let model = try await CohereTranscribeModel.load(
    "aufklarer/Cohere-Transcribe-2B-MLX-8bit"
)
let text = model.transcribe(
    audio: samples,
    sampleRate: sourceSampleRate,
    language: "en"
)
```

## Benchmark

English FLEURS read speech, 80 utterances (759.56 seconds), Apple M5 Pro:

| Variant | Bundle | WER | Mean RTF | Peak RSS |
|---|---:|---:|---:|---:|
| FP16 | 3.85 GiB | 6.178% | 0.0444 | 3,964 MiB |
| INT5 | 1.62 GiB | 6.288% | 0.0150 | 1,776 MiB |
| INT8 | 2.25 GiB | 6.178% | 0.0159 | 2,428 MiB |

These read-speech measurements are not Artificial Analysis Conversational or
ElevenLabs Scribe results.

## Source and license

The base model is [CohereLabs/cohere-transcribe-03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026) and is
released under Apache 2.0.

## Links

- [Cohere Transcribe guide](https://soniqo.audio/guides/cohere-transcribe)
- [speech-swift](https://github.com/soniqo/speech-swift)
- [Soniqo documentation](https://soniqo.audio/getting-started)
- [Soniqo](https://soniqo.audio)
- [Blog](https://soniqo.audio/blog)
