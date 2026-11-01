---
license: other
license_name: all-rights-reserved
language:
  - ar
  - en
  - es
  - he
  - hi
  - ja
  - ko
task_categories:
  - text-to-speech
  - automatic-speech-recognition
tags:
  - audio
  - speech
  - tts
  - multilingual
  - luel
size_categories:
  - n<1K
modality:
  - audio
pretty_name: Luel Multilingual TTS Samples
configs:
  - config_name: default
    data_files:
      - split: train
        path: metadata.csv
---

# Multilingual TTS Samples (Luel)

**License:** All Rights Reserved. Proprietary. Access only for authorized parties; no redistribution or use without permission. See [LICENSE](LICENSE).

A multilingual text-to-speech / read-speech dataset of short scripted utterances across 7 languages. Each sample is a single-speaker recording of a written prompt, paired with rich speaker and recording metadata. Useful for TTS training and evaluation, ASR adaptation, dialect/accent studies, and read-speech benchmarking.

---

## Quick Stats

| Metric | Value |
|--------|-------|
| Languages | 7 (English, Hindi, Japanese, Arabic, Korean, Hebrew, Spanish) |
| Total samples | 685 |
| Total duration | 2h 20m (8,428 s) |
| Total words | 13,707 |
| Mean duration | 12.3 s |
| Audio format | WAV |
| Speaker metadata | gender, dialect, mother tongue, birth place, year of birth, language proficiencies |

### Per-Language Breakdown

| Language | Code | Samples | Duration | Words |
|----------|------|---------|----------|-------|
| Hindi    | hi   | 211     | 48m 31s  | 5,782 |
| English  | en   | 199     | 31m 48s  | 4,299 |
| Japanese | ja   | 163     | 38m 55s  | 1,597 |
| Arabic   | ar   |  51     | 10m 22s  | 1,054 |
| Korean   | ko   |  40     |  7m 05s  |   486 |
| Hebrew   | he   |  11     |  1m 54s  |   231 |
| Spanish  | es   |  10     |  1m 53s  |   258 |

Full per-language stats (gender breakdown, per-dialect counts) are in [`stats.json`](stats.json).

---

## Structure

```
audio/
  ar/  ar_00001.wav … ar_00051.wav
  en/  en_00001.wav … en_00199.wav
  es/  es_00001.wav … es_00010.wav
  he/  he_00001.wav … he_00011.wav
  hi/  hi_00001.wav … hi_00211.wav
  ja/  ja_00001.wav … ja_00163.wav
  ko/  ko_00001.wav … ko_00040.wav
metadata.csv
stats.json
LICENSE
README.md
```

The dataset follows the Hugging Face `audiofolder` layout: `metadata.csv` carries one row per audio file, with `file_name` referencing the WAV at `audio/{lang_code}/{id}.wav`.

---

## Loading

```python
from datasets import load_dataset

ds = load_dataset(
    "Luel-ai/luel-multilingual-tts-samples",
    split="train",
)
print(ds[0])
```

Filter by language:

```python
en = ds.filter(lambda x: x["language_code"] == "en")
```

---

## Metadata Schema

Each row in `metadata.csv` contains:

| Field | Type | Description |
|-------|------|-------------|
| `file_name` | string | Relative path to audio (`audio/{code}/{id}.wav`) |
| `id` | string | Sample id (`{lang_code}_{NNNNN}`) |
| `language` | string | Spoken language (e.g. `English`) |
| `language_code` | string | ISO 639-1 code (`en`, `hi`, `ja`, `ar`, `ko`, `he`, `es`) |
| `script` | string | Text the speaker read |
| `type_of_script` | string | Prompt type (e.g. `monologues`) |
| `duration_seconds` | float | Audio duration in seconds |
| `gender` | string | Speaker gender |
| `ethnicity` | string | Speaker self-reported ethnicity (may be empty) |
| `birth_place` | string | Speaker country of birth |
| `mother_tongue` | string | Speaker native language |
| `dialect` | string | Speaker dialect / regional variety |
| `year_of_birth` | int | Speaker year of birth |
| `years_at_birth_place` | int | Years lived at birth place |
| `languages_data` | json | Spoken languages with proficiency levels (JSON-encoded) |
| `recording_environment` | string | Environment label (`home`, etc.) |
| `os` | string | Recording OS |
| `device` | string | Device type |
| `browser` | string | Browser used |

---

## Intended Uses

- TTS / voice cloning training and evaluation
- Multilingual ASR fine-tuning, especially for low-resource accents and dialects
- Speaker / dialect classification benchmarks
- Read-speech / prosody research

## Out-of-Scope Uses

- Identifying or re-contacting speakers
- Any use prohibited by the LICENSE

---

## Access

This repository is gated. You must accept the conditions to access files and content. For access requests, contact Luel (https://luel.ai).
