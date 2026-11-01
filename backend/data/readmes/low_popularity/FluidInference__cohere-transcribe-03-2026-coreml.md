---
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
- ko
- vi
license: apache-2.0
library_name: coreml
tags:
- audio
- automatic-speech-recognition
- coreml
- ios
- macos
- apple-silicon
- cache-external
- parakeet-pattern
- int8
- quantized
pipeline_tag: automatic-speech-recognition
base_model: CohereLabs/cohere-transcribe-03-2026
---

# Cohere Transcribe Q8 Cache-External CoreML

CoreML conversion of [Cohere Transcribe 03-2026](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026) with an **INT8-quantized encoder** and an **FP16 cache-external decoder**. This is the hybrid pairing used by
[FluidAudio](https://github.com/FluidInference/FluidAudio) for on-device inference.

For the pure FP16 variant see
[`FluidInference/cohere-transcribe-cache-external-coreml`](https://huggingface.co/FluidInference/cohere-transcribe-cache-external-coreml).

## Why this hybrid?

The encoder dominates compute (~65–70% of per-sample processing time at FP16). INT8
quantization of the encoder weights cuts encoder size ~4× (7.0 GB → 1.8 GB) and improves
ANE utilisation with no measurable WER regression. The decoder is small (<300 MB) and
sensitive to precision, so it stays FP16.

| Component | Precision | Size | Notes |
|---|---|---:|---|
| Encoder | INT8 (per-channel weight) | 1.8 GB | Conformer, 24 blocks |
| Decoder | FP16 | 291 MB | Cache-external (Parakeet pattern), 8 layers |
| Tokenizer | — | 484 KB | SentencePiece (16,384 tokens) |
| Vocab | — | 332 KB | `vocab.json` id→piece map |

## Model Description

Same architecture as the FP16 cache-external variant:

- **Cache-external decoder**: KV cache managed in Swift/Python (not CoreML state)
- **macOS 14+ / iOS 17+** compatible
- **O(n) decode complexity** with manual cache management
- **Correct EOS token** (token 3, not 151643)

The only change is the encoder weight precision — decoder I/O, masks, caches, and
tokenizer are identical.

## Architecture

### Encoder (INT8)
- **Input**: Mel spectrogram `[1, 128, 3500]` (35 s at 10 ms/frame)
- **Output**: Hidden states `[1, 438, 1024]` (FP16)
- **Quantization**: per-channel INT8 weight quantization (activations FP16)
- **Size**: ~1.8 GB

### Decoder (Cache-External FP16)
- **Pattern**: Parakeet TDT with external KV cache
- **Inputs** (19 total):
  - `input_id`: `[1, 1]` — current token
  - `position_id`: `[1, 1]` — current position
  - `encoder_hidden_states`: `[1, 438, 1024]`
  - `cross_attention_mask`: `[1, 1, 1, 438]`
  - `attention_mask`: `[1, 1, 1, seq_len]` — grows each step
  - `k_cache_0..7`: `[1, 8, 108, 128]`
  - `v_cache_0..7`: `[1, 8, 108, 128]`
- **Outputs** (17 total):
  - `logits`: `[1, 16384]`
  - `k_cache_0_out..7_out`, `v_cache_0_out..7_out`: updated caches
- **Size**: ~291 MB

## Performance

Tested with FluidAudio's `fluidaudiocli cohere-mixed-benchmark` on FLEURS (full splits,
INT8 encoder + FP16 cache-external decoder, ANE):

| Language | Samples | WER | CER | RTFx |
|---|---:|---:|---:|---:|
| en_us | 647 | 5.63% | 3.19% | 1.93× |
| fr_fr | 676 | 6.22% | 3.11% | 1.65× |
| _(more languages pending)_ | | | | |

LibriSpeech test-clean (FP16 reference, for parity cross-check):

| Metric | Value |
|---|---|
| WER (FP16) | 11.95% |
| Perfect transcriptions | 2 / 10 |
| Main errors | Punctuation differences |

INT8-encoder WER on LibriSpeech is within FP16 noise (validated by comparing encoder
hidden states against the FP16 reference on the same audio).

## Critical Fix: EOS Token

⚠️ **Important**: The EOS token is **3** (`<|endoftext|>`), not 151643!

```python
# WRONG (vocabulary only has 16384 tokens)
EOS_TOKEN = 151643  # Out of range!

# CORRECT
EOS_TOKEN = 3  # From model.generation_config.eos_token_id
```

## Usage

### Swift (FluidAudio)

```swift
import CoreML
import Foundation

let encoderURL = modelDir.appendingPathComponent("cohere_encoder.mlmodelc")
let decoderURL = modelDir.appendingPathComponent("cohere_decoder_cache_external.mlmodelc")

let loaded = try CohereFixedPipeline.loadModels(
    encoderURL: encoderURL,
    decoderURL: decoderURL,
    vocabDir: modelDir
)
let pipeline = try CohereFixedPipeline(models: loaded)
let result = try pipeline.transcribe(audio: samples, models: loaded)
print(result.text)
```

Full Swift implementation:
- `CohereFixedPipeline.swift` — pipeline orchestration + vocab loading
- `CohereDecoderState.swift` — KV cache management
- `CohereModelInference.swift` — decoder execution

Source: https://github.com/FluidInference/FluidAudio

### Python

Identical to the FP16 variant — swap `cohere_encoder.mlpackage` for the INT8 version:

```python
encoder = ct.models.MLModel("cohere_encoder.mlpackage")       # INT8
decoder = ct.models.MLModel("cohere_decoder_cache_external.mlpackage")  # FP16
```

See the FP16 variant's [README](https://huggingface.co/FluidInference/cohere-transcribe-cache-external-coreml/blob/main/README.md#usage) for the complete Python loop (unchanged here).

## Cache Management (Parakeet Pattern)

The cache-external pattern manages KV cache **outside** the CoreML model:

1. Initialize 16 cache arrays (8 layers × K/V) filled with zeros
2. Each decode step:
   - Pass current token + 16 caches into the model
   - Model returns logits + 16 updated caches
   - Use updated caches for next step
3. Attention mask grows: `[1,1,1,1]` → `[1,1,1,2]` → … → `[1,1,1,108]`

## Supported Languages

14 languages: English, French, German, Spanish, Italian, Portuguese, Dutch, Polish,
Greek, Arabic, Japanese, Chinese, Korean, Vietnamese.

## Files

```
cohere-transcribe-q8-cache-external-coreml/
├── cohere_encoder.mlmodelc                  # 1.8 GB — INT8 encoder (compiled)
├── cohere_encoder.mlpackage                 # 1.8 GB — INT8 encoder (source)
├── cohere_decoder_cache_external.mlmodelc   # 291 MB — FP16 decoder (compiled)
├── cohere_decoder_cache_external.mlpackage  # 291 MB — FP16 decoder (source)
├── tokenizer.model                          # SentencePiece tokenizer
├── vocab.json                               # id→piece map (16,384 entries)
├── example.py                               # Python usage example
├── requirements.txt                         # Python deps for example.py
├── wer_results_cache_external.json          # Reference WER data
└── README.md                                # This file
```

## Compilation

The `.mlmodelc` variants are already compiled for fast runtime loading.
If you only need the source package, download just the `.mlpackage` directories:

```bash
huggingface-cli download FluidInference/cohere-transcribe-q8-cache-external-coreml \
  --include "*.mlpackage/**" "tokenizer.model" "vocab.json"
```

To recompile `.mlpackage` → `.mlmodelc`:

```bash
xcrun coremlcompiler compile cohere_encoder.mlpackage output/
xcrun coremlcompiler compile cohere_decoder_cache_external.mlpackage output/
```

## Quantization Notes

- **Scheme**: per-channel INT8 weight quantization, FP16 activations
- **Toolchain**: `coremltools.optimize.coreml.linear_quantize_weights` (applied via
  `tools/quantize_to_int8.py` in the conversion pipeline)
- **Validation**: hidden-state parity check against the FP16 reference on 10
  LibriSpeech test-clean samples; max abs diff within FP16 noise
- **ANE residency**: profiled with `coreml-cli` — no CPU fallback

## Comparison

| Variant | Encoder | Decoder | Encoder size | Notes |
|---|---|---|---:|---|
| `cohere-transcribe-cache-external-coreml` | FP16 | FP16 | 7.0 GB | Reference |
| `cohere-transcribe-q8-cache-external-coreml` (this) | INT8 | FP16 | 1.8 GB | Production hybrid |

## Citation

```bibtex
@misc{cohere-transcribe-q8-cache-external-coreml,
  title={Cohere Transcribe Q8 Cache-External CoreML},
  author={FluidInference},
  year={2026},
  publisher={HuggingFace},
  howpublished={\url{https://huggingface.co/FluidInference/cohere-transcribe-q8-cache-external-coreml}},
  note={CoreML conversion with INT8 encoder + FP16 cache-external decoder (Parakeet pattern).}
}
```

## License

CC-BY-NC-4.0 (matches original Cohere Transcribe model).

## Links

- **Original model**: https://huggingface.co/CohereLabs/cohere-transcribe-03-2026
- **FP16 sibling**: https://huggingface.co/FluidInference/cohere-transcribe-cache-external-coreml
- **Source code**: https://github.com/FluidInference/FluidAudio
- **Conversion scripts**: https://github.com/FluidInference/mobius