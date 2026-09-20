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
- coreml
- qwen3
- neural-engine
base_model: Qwen/Qwen3-ASR-0.6B
pipeline_tag: automatic-speech-recognition
---

# Qwen3-ASR-0.6B — CoreML

CoreML conversion of [Qwen/Qwen3-ASR-0.6B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B) for Apple Neural Engine.

Contains both audio encoder and text decoder for full Neural Engine inference (no GPU required).

## Models

| Model | Description | Quantization |
|-------|-------------|-------------|
| `encoder.mlmodelc` | Audio encoder (mel → embeddings) | INT8 palettized |
| `embedding.mlmodelc` | Token embedding lookup | INT8 palettized |
| `decoder.mlmodelc` | Text decoder with KV cache (28 layers) | INT8 palettized |
| `encoder_int4.mlpackage` | Audio encoder source | INT4 palettized |
| `encoder_int8.mlpackage` | Audio encoder source | INT8 palettized |

## Usage

Full CoreML pipeline (encoder + decoder on Neural Engine):


[1;38;5;196mWelcome to Swift![0m

[1mSubcommands:[0m

  [1mswift build[0m      Build Swift packages
  [1mswift package[0m    Create and work on packages
  [1mswift run[0m        Run a program from a package
  [1mswift test[0m       Run package tests
  [1mswift repl[0m       Experiment with Swift code interactively

  Use [1m`swift --version`[0m for Swift version information.

  Use [1m`swift --help`[0m for descriptions of available options and flags.

  Use [1m`swift help <subcommand>`[0m for more information about a subcommand.



Hybrid mode (CoreML encoder + MLX decoder on GPU):



## Architecture

- **Audio encoder**: 18-layer Whisper-style transformer (896 dim, 14 heads)
- **Text decoder**: 28 layers, 1024 hidden, 16 heads (8 KV heads)
- **KV cache**: Fixed 1024 tokens via CoreML MLState
- **Requires**: macOS 15+ / iOS 18+ (full CoreML mode)

## Links

- **Swift library**: [soniqo/speech-swift](https://github.com/soniqo/speech-swift)
- **Base model**: [Qwen/Qwen3-ASR-0.6B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B)

---

---

- **Guide**: [soniqo.audio/guides/transcribe](https://soniqo.audio/guides/transcribe)
- **Docs**: [soniqo.audio](https://soniqo.audio)
- **GitHub**: [soniqo/speech-swift](https://github.com/soniqo/speech-swift)
