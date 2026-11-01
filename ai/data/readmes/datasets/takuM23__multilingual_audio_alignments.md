---
license: cc-by-4.0
task_categories:
  - automatic-speech-recognition
  - text-to-speech
language:
  - en
  - de
  - fr
  - es
  - ru
  - ja
  - ko
  - pt
  - tr
  - th
tags:
  - audio
  - speech
  - phoneme-alignment
  - mfa
  - forced-alignment
pretty_name: Multilingual MFA-Aligned Speech Dataset
configs:
  - config_name: english
    data_files:
      - split: train
        path: data/english/train-*
  - config_name: french
    data_files:
      - split: train
        path: data/french/train-*
  - config_name: german
    data_files:
      - split: train
        path: data/german/train-*
  - config_name: italian
    data_files:
      - split: train
        path: data/italian/train-*
  - config_name: japanese
    data_files:
      - split: train
        path: data/japanese/train-*
  - config_name: korean
    data_files:
      - split: train
        path: data/korean/train-*
  - config_name: mandarin
    data_files:
      - split: train
        path: data/mandarin/train-*
  - config_name: polish
    data_files:
      - split: train
        path: data/polish/train-*
  - config_name: portuguese
    data_files:
      - split: train
        path: data/portuguese/train-*
  - config_name: russian
    data_files:
      - split: train
        path: data/russian/train-*
  - config_name: spanish
    data_files:
      - split: train
        path: data/spanish/train-*
  - config_name: thai
    data_files:
      - split: train
        path: data/thai/train-*
  - config_name: turkish
    data_files:
      - split: train
        path: data/turkish/train-*
---

# Multilingual MFA-Aligned Speech Dataset (UNDER DEVELOPMENT)

A large-scale multilingual speech dataset with **word-level and phoneme-level alignments** produced using the Montreal Forced Aligner (MFA).

## Dataset Description

This dataset consolidates multiple speech corpora across various languages, all processed through MFA to provide precise phoneme and word alignments. Each sample includes the original audio, transcript, and detailed timing information for both words and phonemes.

### Features

| Column | Type | Description |
|--------|------|-------------|
| `audio` | Audio | Audio waveform at 16kHz |
| `transcript` | string | Text transcription |
| `phoneme_sequence` | string | Phoneme sequence with spaces between words |
| `words` | list | Word-level alignments: `[{word, start, end}, ...]` |
| `phonemes` | list | Phoneme-level alignments: `[{phoneme, start, end}, ...]` |
| `source` | string | Original dataset source (e.g., voxpopuli, common_voice) |

### Languages & Statistics

| Language | Config | Hours | Samples | Sources |
|----------|--------|-------|---------|---------|
| English | `english` | TBD | TBD | Common Voice, VoxPopuli, GigaSpeech, Emilia, Genshin Voice, Gemini Speech |
| German | `german` | TBD | TBD | Multilingual LibriSpeech, Emilia |
| French | `french` | TBD | TBD | French Game Voice, Multilingual LibriSpeech, Wolof French ASR |
| Spanish | `spanish` | TBD | TBD | CML TTS, LibriVox, TEDx Spanish |
| Russian | `russian` | TBD | TBD | Russian Audio Data, Multilingual LibriSpeech |
| Japanese | `japanese` | TBD | TBD | Combined Japanese Dataset, Japanese Anime Speech |
| Korean | `korean` | TBD | TBD | Zeroth STT Korean, Korea Speech |
| Portuguese | `portuguese` | TBD | TBD | Portuguese TTS, Multilingual LibriSpeech |
| Turkish | `turkish` | TBD | TBD | Turkish Merge Audio, Khan Academy Turkish |
| Thai | `thai` | TBD | TBD | Porjai Thai Voice Dataset |

**Total: ~20,000+ hours** (estimated)

## Usage

### Load a specific language

```python
from datasets import load_dataset

# Load English data
dataset = load_dataset("AAdonis/multilingual_audio_alignments", "english", split="train")

# Load German data
dataset = load_dataset("AAdonis/multilingual_audio_alignments", "german", split="train")
```

### Access alignments

```python
sample = dataset[0]

# Get audio
audio = sample["audio"]["array"]
sample_rate = sample["audio"]["sampling_rate"]

# Get transcript, phonemes, and source
transcript = sample["transcript"]
phonemes = sample["phoneme_sequence"]  # "h ɛ l oʊ w ɜː l d"
source = sample["source"]  # e.g., "voxpopuli"

# Get word-level alignments
for word_info in sample["words"]:
    print(f"{word_info['word']}: {word_info['start']:.2f}s - {word_info['end']:.2f}s")

# Get phoneme-level alignments
for phon_info in sample["phonemes"]:
    print(f"{phon_info['phoneme']}: {phon_info['start']:.3f}s - {phon_info['end']:.3f}s")
```

### Filter by source

```python
# Get only VoxPopuli samples
voxpopuli_samples = dataset.filter(lambda x: x["source"] == "voxpopuli")

# Get only Common Voice samples
cv_samples = dataset.filter(lambda x: x["source"] == "common_voice")
```

## Processing Details

### MFA Alignment

All samples were aligned using the Montreal Forced Aligner (MFA) with language-specific acoustic models and pronunciation dictionaries.

### Quality Filtering

During processing, samples were filtered and split based on:
- **`<unk>` words**: Samples containing unknown words are split at those boundaries
- **`spn` phonemes**: Spoken noise markers cause sample splits
- **Duration**: Samples are filtered by minimum/maximum duration thresholds
- **Word count**: Minimum word requirements per segment

### Phoneme Sequence Format

The `phoneme_sequence` column contains IPA phonemes with:
- Phonemes within a word are concatenated directly
- Words are separated by spaces
- Example: `"h ɛ l oʊ"` for "hello" (4 phonemes, 1 word)

## Citation

If you use this dataset in your research, please cite the following manuscript:

```bibtex
@misc{aasonitis2026multilingualspeechediting,
      title={Multilingual Speech Editing},
      author={Antonis Asonitis and Luca A. Lanzendörfer and Frédéric Berdoz and Roger Wattenhofer},
      year={2026},
      note={Manuscript in preparation},
}
```

## License

This dataset is released under CC-BY-4.0. Please also respect the licenses of the original source datasets and MFA.

