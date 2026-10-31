---
license: cc-by-sa-4.0
task_categories:
- image-feature-extraction
language:
- en
- ar
- th
- ko
- zh
- hi
- ta
- ja
pretty_name: Glyphmatte dataset
dataset_info:
  features:
    - name: rgb
      dtype: image
    - name: matte
      dtype: image
    - name: weight
      dtype: image
    - name: foreground
      dtype: image
    - name: background
      dtype: image
---

# Versta Glyphmatte
Synthetic Glyph Matte Dataset for On-Device Document Processing. A labelled strip dataset synthesized entirely from pinned open fonts and frequency word lists using a deterministic generator. Designed for edge deployment on Android devices, this dataset enables training of compact glyph-matte U-Nets that decompose text line strips into ink coverage, stroke weight and per-pixel foreground/background colour, the signals behind on-device dewarping and enhancement. Entirely generated using renewable energy.

## Dataset Details

### Dataset Description

Synthetic Labelled Text Strips, Powered by Open Typography, Generated with Renewable Energy
This dataset was created to give an on-device model exact per-pixel supervision that no human annotation pipeline could produce: every 48-px-high text strip ships with its ground-truth alpha matte, stroke-weight field and foreground/background colour fields. Labels stay mathematically clean; only the composited RGB input is photographically degraded (noise, blur, gradients), so the model learns robustness without label noise. Half the data is drawn from 50,000 training strips, rounded out by a fixed 1,024-strip validation shard.

- **Curated by:** Ricardo Snoek-Valkenburg
- **Language(s) (NLP):** Multilingual (Latin, CJK, Arabic, Devanagari, Tamil, Thai script slots)
- **License:** Creative Commons Attribution Share Alike 4.0 (CC-BY-SA-4.0)

### Dataset Sources

The rendered text combines pinned, sha256-verified font families and frequency word lists from widely recognized open resources:

| Resource | Description |
| :--- | :--- |
| **Noto Sans / Serif / Mono** | SIL OFL font families (regular + bold weights) covering Latin, Arabic, Devanagari, Tamil and Thai scripts |
| **Noto Sans CJK** | SIL OFL pan-CJK family (OTC collections, regular + bold) for Chinese, Japanese and Korean text |
| **Google Fonts display faces** | SIL OFL display-type families (Anton, BebasNeue, Staatliches, AlfaSlabOne) covering heavy condensed header text |
| **dwyl english-words** | Open English word list for the Latin script slot |
| **FrequencyWords** | MIT-licensed subtitle-frequency word lists per language, filtered by Unicode block to drop transliterations and mojibake |

Strips were synthesized at 3× supersampling and downsampled, with random casing, punctuation, digit runs and light skew applied to the rendered text. Columns: `rgb` (degraded input), `matte`, `weight`, `foreground`, `background` (clean labels), stored as PNG bytes in HF-native parquet shards alongside a shared `metadata.jsonl` with the full traceability of each strip (text, font, stroke metrics, colours).

- **Repository:** [Versta.Models](https://github.com/FricoRico/Versta.Models)