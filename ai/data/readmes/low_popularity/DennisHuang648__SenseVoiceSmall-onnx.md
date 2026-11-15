---
license: apache-2.0
language:
- zh
- en
- ja
- ko
- yue
tags:
- sensevoice
- onnx
- asr
- speech-recognition
- FunASR
pipeline_tag: automatic-speech-recognition
---

# SenseVoiceSmall ONNX (INT8 Quantized)

This is a mirror of [iic/SenseVoiceSmall-onnx](https://modelscope.cn/models/iic/SenseVoiceSmall-onnx) from ModelScope, redistributed here for convenient access via HuggingFace.

## Model Description

SenseVoiceSmall is a multilingual speech understanding model from Alibaba DAMO Academy (FunAudioLLM), supporting:
- **Automatic Speech Recognition (ASR)** for Chinese, English, Cantonese, Japanese, and Korean
- **Speech Emotion Recognition (SER)**
- **Audio Event Detection (AED)**
- **Inverse Text Normalization (ITN)**

This repository contains the **INT8 quantized ONNX** export (~230 MB), suitable for efficient CPU inference via `onnxruntime`.

## Files

| File | Size | Description |
|---|---|---|
| `model_quant.onnx` | ~230 MB | INT8 quantized ONNX model |
| `am.mvn` | 11 KB | CMVN (mean/variance normalization) statistics |
| `config.yaml` | 1.8 KB | Model & frontend configuration |
| `tokens.json` | 344 KB | Token vocabulary |
| `configuration.json` | 56 B | Framework metadata |

## Usage

This model is designed to be used with `onnxruntime` + `kaldi-native-fbank` + `sentencepiece` for lightweight inference without the full FunASR/PyTorch stack.

## Source & License

- **Original model**: [iic/SenseVoiceSmall](https://modelscope.cn/models/iic/SenseVoiceSmall) (FunAudioLLM/Alibaba DAMO Academy)
- **ONNX export source**: [iic/SenseVoiceSmall-onnx](https://modelscope.cn/models/iic/SenseVoiceSmall-onnx)
- **License**: Apache-2.0

## Citation

```bibtex
@inproceedings{an2024funaudiollm,
  author={An, Keyu and others},
  title={FunAudioLLM: Voice Understanding and Generation Foundation Models for Natural Interaction Between Humans and LLMs},
  year={2024},
}
```
