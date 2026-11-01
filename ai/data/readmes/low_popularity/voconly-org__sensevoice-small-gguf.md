---
license: apache-2.0
language: [zh, en, yue, ja, ko, ar, de, fr, es, pt, it, ru, th, vi, hi, tr, id, ms, nl, sv, da, fi, pl, cs, fil, fa, el, ro, hu, mk]
tags:
- asr
- automatic-speech-recognition
- sensevoice
- gguf
- multilingual
- speech-to-text
- alibaba
base_model:
- iic/SenseVoiceSmall
---

# SenseVoice-Small GGUF

A multilingual ASR model from Alibaba's Tongyi Lab, converted to GGUF format for broad compatibility.

## Model Overview

SenseVoice-Small features:

- **Parameters**: Small variant
- **Language Support**: Multiple languages including Chinese, English, Cantonese, and more
- **Quantization Format**: GGUF (llama.cpp compatible)
- **Architecture**: FunASR-based speech recognition
- **Features**: High-accuracy recognition, real-time transcription, noise robustness
- **Use Cases**: Speech-to-text, subtitle generation, meeting transcription, multilingual transcription

## Available Quantized Versions

| Filename | Quantization Type | File Size | Description |
|----------|-------------------|-----------|-------------|
| sensevoice-small-f16.gguf | F16 | ~449 MB | Full precision, highest accuracy |
| sensevoice-small-q5_k_m.gguf | Q5_K_M | ~164 MB | Balanced accuracy and speed |
| sensevoice-small-q8_0.gguf | Q8_0 | ~241 MB | High-accuracy quantization |

## Usage

### llama.cpp Command Line

```bash
./main -m sensevoice-small-f16.gguf -f audio.wav --output-txt
```

### Python (llama-cpp-python)

```python
from llama_cpp import Llama

# Load model
llm = Llama(
    model_path="sensevoice-small-f16.gguf",
    n_gpu_layers=-1,  # Use GPU acceleration
)

# Perform speech recognition
result = llm.transcribe("audio.wav")
print(result["text"])
```

## Performance Features

- High multilingual recognition accuracy
- Excellent Chinese recognition, supports Mandarin and Cantonese
- Noise resistance capabilities
- Supports real-time streaming transcription

## Technical Specifications

- **Architecture**: Transformer-based encoder-decoder structure
- **Sample Rate**: 16kHz
- **Input Format**: WAV/PCM audio
- **Output Format**: Text

## License

Apache 2.0 License

## Acknowledgments

- Original Model: [iic/SenseVoiceSmall](https://huggingface.co/iic/SenseVoiceSmall)
- Source: Alibaba DAMO Academy ModelScope