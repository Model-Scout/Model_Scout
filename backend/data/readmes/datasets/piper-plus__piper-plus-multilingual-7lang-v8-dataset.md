---
license: other
license_name: mixed-see-readme
language: [ja, en, zh, es, fr, pt, ko]
---

# piper-plus multilingual 7-lang v8 training dataset

Preprocessed training dataset for piper-plus zero-shot TTS v8
(342,855 utterances / 3,692 speakers / 7 languages).
`data/` holds the full dataset (audio_norm + spec caches, split tar.gz —
concatenate parts then extract). `essential/` holds metadata only
(dataset.jsonl + config + CAM++ speaker embeddings + holdout) for fast restore.

Access is gated (manual approval) because the ja subset derives from
MoeSpeech (see `ayousanz/moe-speech-plus` terms). Other sources:
LibriTTS-R (CC BY 4.0), AISHELL-3 (Apache 2.0), CML-TTS (CC BY 4.0),
Common Voice pt/ko (CC0), Zeroth-Korean (CC BY 4.0). Attribution and
per-source details: `data-sources.yml` in the piper-plus repository.
