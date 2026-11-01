---
license: cc-by-4.0
task_categories:
  - automatic-speech-recognition
language:
  - ko
tags:
  - telephony
  - asr
  - minds14
  - banking
  - ivr
pretty_name: MINDS-14 Telephony — Korean (processed)
size_categories:
  - n<1K
---

# MINDS-14 telephony — Korean (`ko-KR`)

Processed banking IVR **telephony** speech derived from
[PolyAI/minds14](https://huggingface.co/datasets/PolyAI/minds14) (`ko-KR` / related config).

## Credits & license

**Original corpus:** [PolyAI MInDS-14](https://huggingface.co/datasets/PolyAI/minds14)  
Gerz et al., 2021 — [arXiv:2104.08524](https://arxiv.org/abs/2104.08524).

**License:** [CC BY-4.0](https://creativecommons.org/licenses/by/4.0/) (commercial use allowed with attribution).

## Snapshot

- Language: `ko` (locale `ko-KR`)
- Samples: **592** clips (~**1.374 h**) after GT remaster
- Audio: OGG/Opus mono, **native 8 kHz telephony**
- Split: all `test` (eval-only remaster; upstream was train-only)
- Ordering: longest → shortest
- License: **CC-BY-4.0**

## Processing applied

1. Remaster PolyAI audio to OGG/Opus mono at native **8 kHz telephony**.
2. Schema columns: `original_transcription`, `processed_transcription`, `transcription`.
3. **Upstream text is Google ASR 1-best**, not human GT (see paper / Hub card
   `annotations_creators: machine-generated`). Kept immutable in
   `original_transcription`.
4. **Remaster reference:** `processed_transcription` / `transcription` =
   **Gemini 3.5 Transcribe** on every kept clip.
5. **Drops:** noise-only legacy GT stubs, empty Gemini hypotheses, and wrong
   spoken language (e.g. English audio in a non-English split).
   Dropped here: **0** clips / **0.000 h**.

## Dataset structure

| field | description |
|---|---|
| `audio` | OGG/Opus, 8 kHz mono telephony |
| `audio_id` | stable sample id |
| `license` | `CC-BY-4.0` |
| `original_transcription` | upstream Google ASR 1-best (immutable) |
| `processed_transcription` | Gemini remaster transcript |
| `transcription` | best available (= processed) |
| `dur` / `sample_rate` / `lang` / `split` | metadata |
| `intent_class` / `rank` / `src` | optional extras when present |

## Notes

Short single-turn banking intents — useful as an 8 kHz telephony acoustic canary,
not a long-form conversational bench. Contamination risk is high (widely used in
training corpora).
