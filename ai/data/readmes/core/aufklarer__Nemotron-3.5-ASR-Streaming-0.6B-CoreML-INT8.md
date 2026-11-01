---
license: openmdw-1.1
language:
- en
- es
- de
- fr
- it
- pt
- ru
- hi
- zh
- ja
- ko
- ar
- nl
- pl
- tr
- uk
- ro
- el
- cs
- hu
- sv
- da
- fi
- 'no'
- sk
- hr
- bg
- lt
- et
- lv
- sl
- th
- vi
- id
- ms
- bn
- ur
- fa
- ta
- te
- mr
- gu
- kn
- ml
- si
- ne
- km
- sw
- am
- ha
- zu
- yo
- ig
- af
- rw
- so
- ny
- ln
- 'or'
- he
- ku
- az
- ka
- hy
- uz
- tg
- ky
- qu
- ay
- gn
- mi
- haw
- sm
- to
- mt
tags:
- automatic-speech-recognition
- nemotron
- streaming
- conformer
- rnn-t
- multilingual
- coreml
base_model: nvidia/nemotron-3.5-asr-streaming-0.6b
library_name: coreml
pipeline_tag: automatic-speech-recognition
---

# Nemotron-3.5 ASR Streaming 0.6B — CoreML INT8

Cache-aware streaming Conformer + RNN-T from NVIDIA, ported to CoreML (`.mlmodelc`) for on-device inference on Apple Silicon. 600 M params, 40 language-locales, native punctuation and capitalization. INT8 palettized encoder, FP16 decoder + joint. Ships `.mlmodelc` (compiled) — `.mlpackage` is not shipped because on-device `MLModel.compileModel()` produces non-deterministic output across iOS simulator vs device runtimes.

## Model

| | |
|---|---|
| Parameters | 600 M |
| Architecture | FastConformer-CacheAware-RNN-T with language-conditioning prompt kernel |
| Languages | 40 (see frontmatter) |
| Sample rate | 16 kHz mono |
| Streaming chunk | 320 ms (`att_context_size = [56, 3]`) |
| Encoder quantization | INT8 palettized |
| Decoder / joint dtype | FP16 |
| On-disk size | 612 MB |

## Files

| File | Size | Description |
|------|------|-------------|
| `encoder.mlmodelc/` | 565 MB | 24-layer cache-aware Conformer encoder + prompt kernel |
| `decoder.mlmodelc/` | 29 MB | RNN-T prediction net (2-layer LSTM, 640 dim) |
| `joint.mlmodelc/` | 18 MB | Joint network (vocab=13088) |
| `tokenizer.model` | 400 KB | SentencePiece tokenizer used for phrase tokenization and word boosting |
| `vocab.json` | 230 KB | SentencePiece pieces, id → string |
| `languages.json` | 2 KB | Language tag → prompt slot (e.g. `"en-US": 0`) |
| `config.json` | <1 KB | Streaming geometry + dims for the loader |

## Performance

M5 Pro (Apple Silicon), 50 samples per language from FLEURS test, streaming 320 ms chunks, compute units `.all`. Scoring uses Whisper `EnglishTextNormalizer` for English and `BasicTextNormalizer(split_letters=True)` for hi/ja (char-level), `BasicTextNormalizer` for de/fr/ar.

### Accuracy

| lang | WER % | CER % | Δ WER vs fp32 source |
|------|------:|------:|---------------------:|
| en_us |  9.59 |  4.26 | +0.26 |
| de_de | 10.41 |  5.37 | +0.19 |
| fr_fr | 12.18 |  4.84 | +1.05 |
| ar_eg | 13.37 |  3.80 | +0.10 |
| hi_in |  4.42 |  3.61 | −0.84 |
| ja_jp | 17.66 | 12.09 | +0.69 |

Quantization is essentially lossless. For ja/hi the published WER is char-level (matches NVIDIA's CJK methodology); CER is the more interpretable number for those scripts.

### Streaming throughput + memory

M5 Pro, 60 s long-form en_us audio, single thread, `.all` compute units:

| metric | value |
|--------|------:|
| RTF (encode + decode) | 0.068 |
| p50 chunk latency | 18.6 ms |
| p99 chunk latency | 23.4 ms |
| RSS post-load | 1046 MB |
| RSS peak (mid-stream) | 1238 MB |

## Usage

### Python (coremltools)

```python
import coremltools as ct
import numpy as np
import json
from huggingface_hub import snapshot_download

bundle = snapshot_download("aufklarer/Nemotron-3.5-ASR-Streaming-0.6B-CoreML-INT8")
encoder = ct.models.CompiledMLModel(f"{bundle}/encoder.mlmodelc")
decoder = ct.models.CompiledMLModel(f"{bundle}/decoder.mlmodelc")
joint   = ct.models.CompiledMLModel(f"{bundle}/joint.mlmodelc")

slots = json.load(open(f"{bundle}/languages.json"))["promptDictionary"]
lang_mask = np.zeros((1, 128), dtype=np.float32)
lang_mask[0, slots["en-US"]] = 1.0
# Feed 320 ms chunks; persist caches across calls (see inference reference below).
```

### Swift (speech-swift SDK)

```swift
import NemotronStreamingASR

// Default model id is this repo; pass `modelId:` to pin
let model = try await NemotronStreamingASRModel.fromPretrained()

// Batch
let text = try model.transcribeAudio(audio, sampleRate: 16000, language: "en-US")

// Streaming (yields partials as audio is fed)
for await partial in model.transcribeStream(audio: audio, sampleRate: 16000, language: "ja-JP") {
    print(partial.text, partial.isFinal)
}
```

Language is a BCP-47 tag (`en-US`, `de-DE`, `fr-FR`, `ja-JP`, `hi-IN`, ...) — resolved via `languages.json`. The Swift wrapper persists the streaming KV/conv caches across `pushAudio` calls within a `StreamingSession`.

### CLI (Homebrew)

```bash
brew install soniqo/tap/speech

# Single-shot transcription on a wav file (uses this CoreML INT8 bundle by default)
speech transcribe recording.wav --engine nemotron --language en-US

# Other languages
speech transcribe meeting.wav --engine nemotron --language de-DE
speech transcribe interview.wav --engine nemotron --language ja-JP
```

`speech` is a universal binary; the model is downloaded on first use and cached under `~/Library/Caches/qwen3-speech/`.

## Source

Upstream: [nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b).

## License

This CoreML conversion is distributed under [OpenMDW 1.1](https://openmdw.ai/license/1-1/), matching the upstream NVIDIA model. NVIDIA marks the upstream model ready for commercial use.

## Links

- [speech-swift](https://github.com/soniqo/speech-swift) — Apple SDK with `NemotronStreamingASR`
- [Docs](https://soniqo.audio/getting-started) — install and CLI documentation
- [soniqo.audio](https://soniqo.audio)
- [blog](https://soniqo.audio/blog)
