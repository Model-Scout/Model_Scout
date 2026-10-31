---
license: cc-by-4.0
task_categories:
- text-to-speech
- audio-classification
language:
- en
- de
- fr
- ja
- ko
tags:
- voice-acting
- captions
- vocal-bursts
- character-voices
size_categories:
- 10K<n<100K
---

# MOSS Character Voices — Top-3 per Group, Captioned (training-ready)

The **top-3 takes per group** (rank 0/1/2 by reward model) of **all ~12,900 groups** in
[`laion/moss-character-voices-bestof64`](https://huggingface.co/datasets/laion/moss-character-voices-bestof64)
— **~38,700 samples** — each annotated with **both** LAION voice-acting caption pipelines and shipped with
**all scores + metadata**, ready to drop into training. Sharded as `data/train-*-of-00129.parquet`.

## Captions (two pipelines, same clip)

- **`caption_procedural`** — [Procedural Voice Captions](https://github.com/LAION-AI/procedural-voice-captions):
  terse *tags* (intensity + dimension), with confirmed vocal bursts inserted **inline** at word-timestamp
  positions (locator@0.75 → multi-label confirm → duration + no-burst gates) + an Empathic-Insight **gender gate**.
- **`caption_llm`** — [Comprehensive Voice-Acting Annotation Pipeline](https://github.com/LAION-AI/Comprehensive-Voice-Acting-Annotation-Pipeline):
  Gemma-4-E4B **rewords** the procedural draft into natural prose while the **burst positions are copied
  verbatim** (identical placement, more fluent wording). The archetype is used only when it names no gender.

Format: a `GENERAL:` voice description + a `SCRIPT:` with one `(delivery cue) sentence text` line per sentence,
vocal bursts inline as `(Burst Name)`.

## Fields

| field | description |
|-------|-------------|
| `audio` | the FLAC take |
| `caption_procedural`, `caption_llm` | the two captions (GENERAL + SCRIPT) |
| `text`, `transcript` | target text and ASR transcript (Parakeet) |
| `character`, `lang`, `topic`, `instruction` | generation metadata |
| `reward`, `rank`, `seed`, `duration_s` | reward-model score, rank-in-group (0/1/2), seed, duration |
| `voicenet_dims`, `emonet` | JSON: 57 VoiceNet dims (0–6) and 40 EmoNet emotions |
| `genuineness`, `burst_blend`, `ei_gender`, `gender_gated` | genuineness (0–6), vocal-burst blend, Empathic-Insight gender (−2 masc…+2 fem), whether gender was gated out |
| `vocal_bursts` | JSON list of confirmed bursts `{label, start, end, dur, prob}` |
| `src_*` | the source dataset's reward-model sub-scores (`char`, `char_emo`, `blend`, `genu`, `dims_json`, `emo_json`) |

## License

CC-BY-4.0. Audio + captions derive from LAION's `moss-character-voices-bestof64` and LAION voice expert models.
