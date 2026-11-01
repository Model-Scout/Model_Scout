---
license: cc-by-4.0
task_categories:
  - audio-classification
  - text-to-speech
language:
  - de
  - en
  - fr
  - ja
  - ko
  - zh
tags:
  - emotion
  - speech
  - audio
  - webdataset
  - speaker-verification
pretty_name: Emolia-HQ
size_categories:
  - 10M<n<100M
---

# Emolia-HQ

**Emolia-HQ** is a high-quality, speaker-paired subset of the [LAION Emolia](https://huggingface.co/datasets/laion/Emolia) dataset. Each sample includes a target utterance and a reference utterance from the **same speaker**, enabling speaker-conditioned tasks such as voice conversion, expressive TTS, and speaker-aware emotion recognition.

## Source

Derived from [laion/Emolia](https://huggingface.co/datasets/laion/Emolia) by:

1. **Quality filtering**: Only samples with `dnsmos >= 3.0` are retained.
2. **Speaker pairing**: Each target sample is matched with a reference audio from the same speaker (different utterance), forming a "quadruplet". Samples where no same-speaker reference exists are included as pairs (target only).
3. **Metadata enrichment**: `speaker_id` and `language_id` fields are extracted from the key and injected into each sample's JSON metadata.

## Data Format

The dataset is stored as **WebDataset** `.tar` files, organized by language:

```
emolia_hq/
  DE/   # German  (243 tars, ~130 GB)
  EN/   # English (2,380 tars, ~2,476 GB)
  FR/   # French  (298 tars, ~187 GB)
  JA/   # Japanese (96 tars, ~163 GB)
  KO/   # Korean  (246 tars, ~79 GB)
  ZH/   # Chinese (929 tars, ~1,681 GB)
```

Each sample within a tar file is grouped by a shared base key:

### Quadruplet (target + same-speaker reference)
| File | Description |
|------|-------------|
| `<key>.mp3` | Target audio |
| `<key>.json` | Target metadata |
| `<key>.ref.mp3` | Reference audio (same speaker, different utterance) |
| `<key>.ref.json` | Reference metadata |

### Pair (no reference found)
| File | Description |
|------|-------------|
| `<key>.mp3` | Target audio |
| `<key>.json` | Target metadata |

## JSON Metadata Fields

| Field | Description |
|-------|-------------|
| `id` | Unique utterance ID |
| `text` | Transcription |
| `duration` | Audio duration in seconds |
| `dnsmos` | DNS-MOS quality score (all >= 3.0) |
| `speaker` | Original speaker ID |
| `speaker_id` | Extracted speaker ID (e.g., `DE_B00000_S00010`) |
| `language_id` | Extracted language code (e.g., `DE`) |
| `language` | Language code lowercase |
| `emotion_caption` | Natural language description of the emotional content |
| `emotion_annotation` | Dictionary of 50+ emotion/prosody scores |
| `characters_per_second` | Speaking rate |
| `wavelm_timbre_embedding` | 128-dim speaker timbre embedding |

## Statistics

| Language | Tars | Size |
|----------|------|------|
| DE (German) | 243 | ~130 GB |
| EN (English) | 2,380 | ~2,476 GB |
| FR (French) | 298 | ~187 GB |
| JA (Japanese) | 96 | ~163 GB |
| KO (Korean) | 246 | ~79 GB |
| ZH (Chinese) | 929 | ~1,681 GB |
| **Total** | **4,192** | **~4,716 GB** |

~97% of samples include a same-speaker reference audio (quadruplets). The remaining ~3% are pairs where the speaker only appeared once across the entire dataset.

## Usage

```python
import webdataset as wds

dataset = wds.WebDataset("emolia_hq/EN/EN-B000000_standard_hq.tar")

for sample in dataset:
    key = sample["__key__"]
    target_audio = sample["mp3"]          # bytes
    target_meta = sample["json"]          # bytes -> json.loads()
    ref_audio = sample.get("ref.mp3")     # bytes or None
    ref_meta = sample.get("ref.json")     # bytes or None
```

## License

Same as the source Emolia dataset. See [laion/Emolia](https://huggingface.co/datasets/laion/Emolia) for details.
