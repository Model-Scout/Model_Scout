---
license: mit
language:
- multilingual
- en
- ru
tags:
- whisper
- gguf
- quantized
- speech-recognition
- rust
- candle
base_model:
- openai/whisper-large-v3-turbo
pipeline_tag: automatic-speech-recognition
---

# WHISPER-LARGE-V3-TURBO - GGUF Quantized Models

Quantized versions of [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) in GGUF format.

## Directory Structure

```
large-v3-turbo/
├── whisper-large-v3-turbo-q*.gguf       # Candle-compatible GGUF models (root)
├── config.json                # Model configuration for Candle
├── tokenizer.json             # Tokenizer for Candle
└── whisper.cpp/               # whisper.cpp-compatible models
    └── whisper-large-v3-turbo-q*.gguf

```

### Format Compatibility

- **Root directory** (`whisper-large-v3-turbo-*.gguf`): Use with **Candle** (Rust ML framework)
  - Tensor names include `model.` prefix (e.g., `model.encoder.conv1.weight`)
  - Requires `config-large-v3-turbo.json` and `tokenizer-large-v3-turbo.json`
  
- **whisper.cpp/** directory: Use with **whisper.cpp** (C++ implementation)
  - Tensor names without `model.` prefix (e.g., `encoder.conv1.weight`)
  - Compatible with whisper.cpp CLI tools
  - Both directories contain `.gguf` files, not `.bin` files

## Available Formats

| Format |  Quality | Use Case |
|--------| ---------|----------|
| q2_k |   large-v3-turboest | Extreme compression |
| q3_k |  large-v3-turbo | Mobile devices |
| q4_0 |  Good | Legacy compatibility |
| q4_k |  Good | **Recommended for production** |
| q4_1 | Good+ | Legacy with bias |
| q5_0 |  Very Good | Legacy compatibility |
| q5_k |  Very Good | High quality |
| q5_1 |  Very Good+ | Legacy with bias |
| q6_k |   Excellent | Near-lossless |
| q8_0 |   Excellent | Minimal loss, benchmarking |

## Usage

### With Candle (Rust)

> For this model, you need to modify the example code in candle. To try whisper in candle faster and easier, it's better to use the tiny model → https://huggingface.co/oxide-lab/whisper-tiny-GGUF

**Command line example:**
```bash
# Run Candle Whisper with local quantized model
cargo run --example whisper --release -- \
  --features symphonia \
  --quantized \
  --model large-v3-turbo \
  --model-id oxide-lab/whisper-large-v3-turbo-GGUF \
```

### With whisper.cpp (C++)

```bash
# Use models from whisper.cpp/ subdirectory
./whisper.cpp/build/bin/whisper-cli \
  --model models/openai/large-v3-turbo/whisper.cpp/whisper-large-v3-turbo-q4_k.gguf \
  --file audio.wav
```

### Recommended Format

For most use cases, we recommend **q4_k** format as it provides the best balance of:
- Size reduction (~65% large-v3-turboer)
- Quality (minimal degradation)
- Speed (faster inference than higher quantizations)

## Quantization Details

- **Source Model**: [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo)
- **Quantization Methods**:
  - **Candle GGUF** (root directory): Python-based. Directly PyTorch → GGUF
    - Adds `model.` prefix to tensor names for Candle compatibility
  - **whisper.cpp GGML** (whisper.cpp/ subdirectory): whisper-quantize tool
    - Uses original tensor names without prefix
- **Format**: GGUF (GGML Universal Format) for both directories
- **Total Formats**: 10 quantization levels (q2_k through q8_0)

## License

Same as the original Whisper model (MIT License).

## Citation

```bibtex
@misc{radford2022whisper,
  doi = {10.48550/ARXIV.2212.04356},
  url = {https://arxiv.org/abs/2212.04356},
  author = {Radford, Alec and Kim, Jong Wook and Xu, Tao and Brockman, Greg and McLeavey, Christine and Sutskever, Ilya},
  title = {Robust Speech Recognition via Large-Scale Weak Supervision},
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```