---
license: other
license_name: openmdw-1.1
license_link: https://openmdw.ai/license/1-1/
library_name: parakeet-rs
pipeline_tag: automatic-speech-recognition
base_model: nvidia/nemotron-3.5-asr-streaming-0.6b
tags:
- automatic-speech-recognition
- streaming-asr
- multilingual
- onnx
- int8
- quantized
- parakeet-rs
- nemotron
- FastConformer
- RNNT
language:
- en
- es
- de
- fr
- it
- ar
- ja
- ko
- pt
- ru
- hi
- zh
- vi
- he
- nl
- cs
- da
- pl
- 'no'
- sv
- th
- tr
- bg
- el
- et
- fi
- hr
- hu
- lt
- lv
- ro
- sk
- uk
- mt
- sl
---

# Nemotron 3.5 ASR Streaming 0.6B (Multilingual) - ONNX int8

Dynamically int8-quantised ONNX export of [`nvidia/nemotron-3.5-asr-streaming-0.6b`](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b),
laid out for [`parakeet-rs`](https://github.com/altunenes/parakeet-rs) (>= 0.3.6) and used by [Undertone](https://github.com/sammcj/Undertone).

A cache-aware streaming FastConformer-RNNT model covering 40 language-locales with native punctuation and capitalisation. The encoder exposes a `prompt_index` input, so a single graph serves every language; the target language is selected at runtime (or left to auto-detect).

## Files

| File | Size | Purpose |
| --- | --- | --- |
| `encoder.onnx` + `encoder.onnx.data` | ~627 MB | int8 streaming encoder with the prompt-kernel head |
| `decoder_joint.onnx` | ~23 MB | int8 RNNT decoder + joint network |
| `tokenizer.model` | ~0.4 MB | SentencePiece tokenizer (vocab 13088, includes language tags) |
| `config.json` | ~3 KB | streaming params, cache shapes, prompt dictionary |
| `nemotron-3.5-asr-streaming-0.6b-int8.tar.gz` | ~432 MB | the above bundled for Undertone's downloader |

All files must live in the same directory. The `parakeet-rs` loader auto-detects the multilingual variant by spotting the `prompt_index` encoder input.

## Usage (parakeet-rs)

```rust
use parakeet_rs::{Nemotron, NemotronMode};

let mut model = Nemotron::from_pretrained("./nemotron-3.5-asr-streaming-0.6b-int8", None)?;
if model.mode() == NemotronMode::Multilingual {
    model.set_target_lang("es-ES")?; // or "auto", "en-US", "ja-JP", "zh-CN", ...
}

// 560ms chunks at 16kHz mono f32
const CHUNK: usize = 8960;
for chunk in audio.chunks(CHUNK) {
    print!("{}", model.transcribe_chunk(chunk)?);
}
```

## How this was produced

The two scripts used to produce this repo are included for reproducibility:

- `export_nemotron_streaming_multilingual.py` - NeMo `.nemo` -> FP32 ONNX
- `quantize_and_package.py` - FP32 ONNX -> int8 + tar.gz

Steps:

1. `python export_nemotron_streaming_multilingual.py nemotron-3.5-asr-streaming-0.6b.nemo ./onnx_fp32` - exports FP32 ONNX (the encoder's per-language `prompt_index` is exposed as a real ONNX input rather than baked in).
2. `python quantize_and_package.py ./onnx_fp32 ./out --tar ./out/nemotron-3.5-asr-streaming-0.6b-int8.tar.gz` - quantises `encoder.onnx` and `decoder_joint.onnx` to int8 via `onnxruntime.quantization.quantize_dynamic` (`QuantType.QInt8`).
3. Encoder/NeMo parity was verified across en-US, es-ES and ja-JP before quantising (max abs diff < 1e-4).

Input: 16kHz mono f32. Output: text with native punctuation; no word-level timestamps.

## Licence and attribution

This is a derivative of NVIDIA's `nemotron-3.5-asr-streaming-0.6b`, distributed under the [OpenMDW 1.1 licence](https://openmdw.ai/license/1-1/). All model credit belongs to NVIDIA; this repository only re-packages the weights as int8 ONNX.
