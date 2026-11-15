---
license: apache-2.0
datasets:
- Junhoee/STT_Korean_Dataset_80000
- Bingsu/zeroth-korean
language:
- ko
base_model:
- openai/whisper-medium
pipeline_tag: automatic-speech-recognition
tags:
- ggml
- gguf
- whisper
---

This model is a fine-tune of OpenAI's Whisper Medium model (https://huggingface.co/openai/whisper-medium) over the following Korean datasets:

- https://huggingface.co/datasets/Junhoee/STT_Korean_Dataset_80000
- https://huggingface.co/datasets/Bingsu/zeroth-korean

Combined they have roughly 102k sentences.

This is the last checkpoint which has achieved ~16 WER (down from ~24 WER).

Training was 10,000 iterations.