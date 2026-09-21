---
license: apache-2.0
language: [en, zh, pt, es, fr, de, it, ja, ko, ru, ar]
tags: [automatic-speech-recognition, onnx, onnx-asr, speech-llm, qwen3-asr]
base_model: Qwen/Qwen3-ASR-1.7B-hf
---

# Qwen3-ASR-1.7B — ONNX (speech-llm)

ONNX export of [Qwen/Qwen3-ASR-1.7B-hf](https://huggingface.co/Qwen/Qwen3-ASR-1.7B-hf) for
[onnx-asr](https://github.com/istupakov/onnx-asr) with the `speech-llm` model type (requires the
speech-llm model-family patches, see
[TigreGotico/onnx-asr PR #3](https://github.com/TigreGotico/onnx-asr/pull/3)).

Three-graph layout: `encoder.onnx` (audio -> projected audio embeddings), `embed_tokens.onnx`,
and a merged prefill+decode `decoder.onnx` with a 28-layer KV cache (hidden size 2048, 8 KV
heads, head dim 128). Prompt token ids are baked into `config.json`, so no tokenizer is needed
at runtime. fp32 output matches native transformers character-for-character on FLEURS test
clips (en, pt). fp32 and int8 graphs included.

## Known limitation (int8)

The int8 decoder can fail on longer utterances: on one 16 s test clip it produced an
empty transcript where fp32 was exact (the 0.6B sibling only shows mild drift). Prefer
fp32 for audio longer than ~15 s until this is resolved.

## Usage

```python
import onnx_asr
model = onnx_asr.load_model("speech-llm", "path/to/this/repo")  # or quantization="int8"
print(model.recognize("audio_16khz.wav"))
```

## Notes

* int8 quantization can drift on longer audio; validate int8 output against fp32 for your
  use case before relying on it in production. fp32 is character-for-character faithful to
  the native model on the FLEURS validation clips used for verification.

License: Apache-2.0 (inherited from the source model).
