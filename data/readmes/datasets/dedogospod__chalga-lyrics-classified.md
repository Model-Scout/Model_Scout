---
language:
- bg
- sr
- el
- mk
- tr
- hr
- ru
- ko
- es
- ro
- fr
- sq
- he
- zh
license: other
task_categories:
- text-classification
tags:
- balkan
- chalga
- lyrics
- music
- multilingual
- bg
- sr
- el
- mk
- hr
- tr
- ru
---

# Balkan Chalga Lyrics Dataset (Classified)

A dataset of **7,132 classified Balkan chalga/pop song lyrics** scraped from [lyricsmusic.eu](https://lyricsmusic.eu). Each entry contains the original URL, title, artist name, full lyrics text, a cleaned/normalized artist name (`classified_artist`), and an automatically detected language code.

## Dataset Statistics

| Metric | Value |
|--------|-------|
| Total entries | 7,132 |
| Languages represented | 15 |
| Primary language | Bulgarian (bg) — 88.8% |
| Train / Val / Test split | 80% / 10% / 10% |

## Language Breakdown

| Language Code | Count | Percentage |
| `bg` | 6,335 | 88.8% |
| `sr` | 459 | 6.4% |
| `el` | 181 | 2.5% |
| `mk` | 36 | 0.5% |
| `tr` | 34 | 0.5% |
| `hr` | 33 | 0.5% |
| `ru` | 16 | 0.2% |
| `ko` | 11 | 0.2% |
| `es` | 11 | 0.2% |
| `ro` | 6 | 0.1% |
| `...` | 3 | 0.0% |
| `fr` | 2 | 0.0% |
| `sq` | 2 | 0.0% |
| `he` | 2 | 0.0% |
| `zh` | 1 | 0.0% |


### Languages
- **bg** — Bulgarian (Български)
- **sr** — Serbian (Српски)
- **el** — Greek (Ελληνικά)
- **mk** — Macedonian (Македонски)
- **tr** — Turkish (Türkçe)
- **hr** — Croatian (Hrvatski)
- **ru** — Russian (Русский)
- Plus small amounts of Korean, Spanish, Romanian, French, Albanian, Hebrew, and Chinese

## Schema

| Column | Type | Description |
|--------|------|-------------|
| `url` | string | Source URL from lyricsmusic.eu |
| `title` | string | Song title (as scraped) |
| `artist` | string | Artist name (as scraped) |
| `lyrics` | string | Full song lyrics text |
| `classified_artist` | string | Cleaned/normalized artist name |
| `language` | string | ISO 639-1 language code |

## Collection & Classification Methodology

1. **Scraping**: Lyrics were scraped from [lyricsmusic.eu](https://lyricsmusic.eu), a multilingual lyrics website covering Balkan and Eastern European music.
2. **Language Classification**: Each entry was classified using **Qwen 3.6 27B** via the LM Studio API, which identified the primary language of each song's lyrics.
3. **Filtering**: English-language songs were filtered out separately (83 entries discarded) to focus on non-English Balkan music content.

## Splits

The dataset is split into three subsets:

| Split | Entries | Percentage |
|-------|---------|------------|
| Train | 5,705 | 80% |
| Validation | 713 | 10% |
| Test | 714 | 10% |

Splits were generated with `seed=42` for reproducibility.

## Usage

```python
from datasets import load_dataset

# Load the full dataset
dataset = load_dataset("dedogospod/chalga-lyrics-classified")

# Access splits
train_ds = dataset["train"]
val_ds = dataset["validation"]
test_ds = dataset["test"]

# Example entry
print(train_ds[0])
```

## License & Copyright Notice

**This dataset contains copyrighted song lyrics.** The lyrics are the intellectual property of their respective artists, composers, and publishers. This dataset is provided for **research and educational purposes only**. Commercial use or redistribution of the lyrics content may violate copyright law in your jurisdiction. Please respect the rights of music creators and publishers.

## Citation

If you use this dataset in your research, please cite it as:

```bibtex
@dataset{dedogospod_chalga_lyrics_2025,
  author       = {Asen Mitrev},
  title        = {Balkan Chalga Lyrics Dataset (Classified)},
  year         = 2025,
  url          = {https://huggingface.co/datasets/dedogospod/chalga-lyrics-classified},
  note         = {Scraped from lyricsmusic.eu, classified with Qwen 3.6 27B}
}
```

## Author

Created by [Asen Mitrev](https://huggingface.co/dedogospod) for research on multilingual Balkan music classification and NLP tasks.
