---
license: cc-by-4.0
base_model: quickmt/quickmt-en-ko
tags: [translation, ctranslate2, int8, yaku-translate]
---
# quickmt-en-ko, int8 CTranslate2

The [quickmt/quickmt-en-ko](https://huggingface.co/quickmt/quickmt-en-ko) translation model (CC BY 4.0, by quickmt) re-saved with int8
weights for CTranslate2, as used by the Yaku Translate app. Output on the checked sentences is character for character the same as the
float16 original. Conversion: per-row int8 quantization of every 2-D weight (same scheme as CTranslate2's ModelSpec quantization), 26.10.2026.
Files: model.bin, config.json, source_vocabulary.json, target_vocabulary.json, src.spm.model, tgt.spm.model.
