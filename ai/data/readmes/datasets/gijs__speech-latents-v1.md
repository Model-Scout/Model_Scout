---
license: cc-by-nc-4.0
language: [en, zh, de, fr, ja, ko]
tags: [speech, audio-latents, emotion]
---

# speech-latents-v1

Audio latents with transcripts, emotion captions and emotion/quality scores, derived from the
**Emilia** speech dataset ([amphion/Emilia-Dataset](https://huggingface.co/datasets/amphion/Emilia-Dataset);
He et al., 2024, arXiv:2407.05361). Emilia is licensed CC BY-NC 4.0; this derivative is released
under the same license, for non-commercial use only.

WebDataset tar shards in `data/`. Each sample has `<key>.npy` (float16 latents, `[frames, 128]`),
optionally `<key>.ref.npy`, and `<key>.json` (text, language, speaker, duration, dnsmos,
emotion_caption, emotion_annotation).
