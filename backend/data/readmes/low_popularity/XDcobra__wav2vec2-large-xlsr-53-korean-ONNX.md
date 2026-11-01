---
language:
- ko
license: apache-2.0
base_model:
- kresnik/wav2vec2-large-xlsr-korean
library_name: transformers
tags:
- automatic-speech-recognition
- wav2vec2
- xlsr
- onnx
- forced-alignment
- char-ctc
- react-native
pipeline_tag: automatic-speech-recognition
---

# wav2vec2-large-xlsr-53-korean-ONNX

ONNX export of [`kresnik/wav2vec2-large-xlsr-korean`](https://huggingface.co/kresnik/wav2vec2-large-xlsr-korean) for char-CTC
forced alignment / ASR (wav2vec2 family).

These weights were prepared for the mobile SDK
**[react-native-sherpa-onnx](https://github.com/XDcobra/react-native-sherpa-onnx)** (offline speech tooling for
React Native / Android / iOS), including forced-alignment model packs used by
the app.

## Try it live in VoiceLab

Download and run these on-device models in your pocket — anytime, anywhere — in the mobile app **VoiceLab**:

- Android: [VoiceLab on Google Play](https://play.google.com/store/apps/details?id=com.xdcobra.voicelab)
- iOS: [VoiceLab on the App Store](https://apps.apple.com/us/app/voice-lab-stt-tts-more/id6761100598)
- Product page: [https://xdcobra.github.io/voice-lab-offline-tools/](https://xdcobra.github.io/voice-lab-offline-tools/)

## Files

| Path | Notes |
| --- | --- |
| `onnx/model.onnx` | fp32 |
| `onnx/model_fp16.onnx` | fp16 weights (when present) |
| `onnx/model_int8.onnx` | dynamic QUInt8 weight quantization |
| `vocab.json` | CTC character vocabulary |
| `config.json` | Transformers model config |
| `LICENSE` | apache-2.0 |

## Source

- Base checkpoint: `kresnik/wav2vec2-large-xlsr-korean` (apache-2.0)
- Export: `optimum-cli export onnx` + `onnxruntime` dynamic quantization
  ([`export_hf_onnx_pack.py`](https://github.com/XDcobra/react-native-sherpa-onnx/blob/main/scripts/alignment-models/export_hf_onnx_pack.py)
  in the SDK repo)
- Intended use: offline forced alignment (CTC) in commercial apps when the
  base model license allows it

## Sample rate

16 kHz mono PCM.
