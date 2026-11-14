---
license: mit
base_model: openai/whisper-large-v3-turbo
library_name: transformers.js
language:
- ko
pipeline_tag: automatic-speech-recognition
---

# whisper-large-v3-turbo_timestamped (external data)

This repository re-packages the q4 and q4f16 ONNX weights from
[onnx-community/whisper-large-v3-turbo_timestamped](https://huggingface.co/onnx-community/whisper-large-v3-turbo_timestamped)
(revision `b3f77bf9a8c4d5ea3415827033d1ffea7955fd9a`), an ONNX export of
[openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) (MIT).

The only change is the file layout. Top-level weights moved from inside the `.onnx` file into a separate `.onnx_data` file (ONNX external data). The weight values are the same. With this layout, onnxruntime-web (WebGPU) can upload the weights straight to the GPU, which uses less WASM memory in the browser. Tensors inside subgraphs stay in the `.onnx` file.

Used by [transbee](https://github.com/ian-yw/transbee).

| file | weights |
|---|---|
| `onnx/encoder_model_q4f16.onnx` | `onnx/encoder_model_q4f16.onnx_data` |
| `onnx/decoder_model_merged_q4f16.onnx` | `onnx/decoder_model_merged_q4f16.onnx_data` |
| `onnx/encoder_model_q4.onnx` | `onnx/encoder_model_q4.onnx_data` |
| `onnx/decoder_model_merged_q4.onnx` | `onnx/decoder_model_merged_q4.onnx_data` |

## License

MIT, same as the original Whisper model. Copyright OpenAI.
