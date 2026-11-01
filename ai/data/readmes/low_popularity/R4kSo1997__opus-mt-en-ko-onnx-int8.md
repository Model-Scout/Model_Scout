---
library_name: transformers
tags:
- onnx
- int8
- marian
- opus-mt
- translation
- offline
- en
- ko
---

# opus-mt-en-ko ONNX int8 (movil offline)

Conversion movil-ready de `Helsinki-NLP/opus-mt-tc-big-en-ko`.

## ONNX
- encoder_model_quantized.onnx
- decoder_model_quantized.onnx
- decoder_with_past_model_quantized.onnx  (KV cache, decoding O(1) por token)

Quant: int8 dynamic ARM64 + per_channel.

## Tokenizer
- tokenizer.json  (Fast / Xenova / transformers.js)
- source.spm, target.spm, vocab.json (Marian raw)

Source: `Helsinki-NLP/opus-mt-tc-big-en-ko`
Repo: `R4kSo1997/opus-mt-en-ko-onnx-int8`
