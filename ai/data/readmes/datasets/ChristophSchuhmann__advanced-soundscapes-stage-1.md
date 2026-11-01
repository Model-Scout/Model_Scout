---
license: cc-by-4.0
task_categories:
  - audio-classification
  - automatic-speech-recognition
language:
  - en
  - de
  - fr
  - es
  - zh
  - ja
  - ko
  - multilingual
tags:
  - soundscape
  - synthetic
  - audio
  - speech
  - music
  - sound-effects
  - uaap
size_categories:
  - n<1K
---

# Advanced Soundscapes Stage 1 — Raw Components

This dataset contains **Stage 1** output from the LAION Universal Audio Annotation Pipeline (UAAP) data generation plan.

## Contents

- **0 shard(s)** containing **0 soundscape recipes** with raw audio components
- Each soundscape row includes:
  - `recipe.json` — full recipe with timeline, events, loudness, speaker IDs, overlap/density settings
  - `spkN.flac` / `spkN.json` — raw speech components + full source metadata  
  - `musicN.flac` / `musicN.json` — raw music components + captions
  - `sfxN.flac` / `sfxN.json` — raw SFX components + captions
  - `vbN.flac` / `vbN.json` — raw vocal burst components + metadata

## Format

WebDataset `.tar` shards. Each row is a directory inside the tar with the clip ID as the key.

## Source Datasets

| Source | Type | License |
|--------|------|---------|
| laion/majestrino-data | Speech (~50 languages) | CC0 |
| laion/Emolia | Emotional speech (EN/DE/FR/ZH/JA/KO) | CC-BY-4.0 |
| laion/captioned-ai-music-snippets | Music (3-30s) | Apache-2.0 |
| laion/generated-sound-events | SFX (synthetic, 1190 classes) | NC-verify |
| laion/synthetic_vocal_bursts | Vocal bursts | Permissive |

## Stage 1 Pipeline

Stage 1 is CPU-only. It:
1. Samples a recipe (archetype, duration, density, overlap, speaker config)
2. Draws raw audio pieces from source datasets (language-balanced, deduplicated)
3. Decodes & resamples to 16 kHz mono
4. Computes exact mix plan (ground-truth timings, loudness, speaker IDs)
5. Gathers full source metadata
6. Writes WebDataset rows

**Stage 2** (GPU) will: caption missing fields, fuse via Gemma-4-12B, render final mixdown MP3.

## Recipe Archetypes

| Archetype | Weight | Speech% | Music% | SFX% |
|-----------|--------|---------|--------|------|
| Balanced trio | 14% | 34% | 33% | 33% |
| Speech-dominant | 16% | 70% | 15% | 15% |
| Music-dominant | 11% | 12% | 76% | 12% |
| SFX-dominant | 11% | 12% | 12% | 76% |
| Speech-only | 13% | 100% | 0% | 0% |
| Music-only | 6% | 0% | 100% | 0% |
| SFX-only | 8% | 0% | 0% | 100% |
| Speech+Music | 8% | 55% | 45% | 0% |
| Speech+SFX | 9% | 55% | 0% | 45% |
| Music+SFX | 4% | 0% | 50% | 50% |

## Pipeline Script

The generation pipeline is included as `stage1_pipeline.py`. Run with:

```bash
python stage1_pipeline.py --num-soundscapes 1000 --num-workers 4 --output-dir ./output --upload
```
