---
license: other
license_name: custom-license
license_link: LICENSE
task_categories:
- text-to-speech
- automatic-speech-recognition
language:
- bg
- cs
- da
- de
- el
- en
- es
- et
- fr
- fi
- hu
- hr
- id
- it
- ja
- ko
- lt
- lv
- mt
- nl
- pl
- pt
- ro
- ru
- sk
- sl
- sv
- th
- vi
- zh
size_categories:
- n>1T
---
---
# X-Voice Training Dataset

## Overview
The X-Voice training dataset is a **large-scale multilingual speech corpus** curated for high-performance speech models. It provides a robust foundation for cross-lingual phonetic and prosodic modeling.

Also the train set of [X-Voice Model](https://github.com/sunnyxrxrx/X-Voice).

## Core Statistics
- **Total Speech Duration**: 420K hours
- **30 languages**
  - **European**: bg (Bulgarian), cs (Czech), da (Danish), de (German), el (Greek), en (English), es (Spanish), et (Estonian), fi (Finnish), fr (French), hr (Croatian), hu (Hungarian),  it (Italian),  lt (Lithuanian), lv (Latvian), mt (Maltese), nl (Dutch), pl (Polish), pt (Portuguese), ro (Romanian), ru (Russian), sk (Slovak), sl (Slovenian), sv (Swedish).
  - **Asian**: id (Indonesian), ja (Japanese), ko (Korean), th (Thai), vi (Vietnamese), zh (Chinese).

    <img src="image-1.png" alt="Duration Statistics of Different Languages" width="420" />

## Data Sources

We aggregate high-quality open-source speech datasets across languages:

- **Chinese & English**: Emilia
- **Vietnamese, Thai, Indonesian**: GigaSpeech 2
- **Korean**: KoreaSpeech
- **Japanese**: ReazonSpeech
- **Russian**: LEMAS
- **European Languages (Spanish, Italian, French, etc.)**: Multilingual Librispeech (MLS), Granary


    | Source        | Format | Sample Rate |
    |---------------|--------|-------------|
    | Emilia        | mp3    | 24kHz       |
    | Gigaspeech2   | flac   | 16kHz       |
    | KoreaSpeech   | flac   | 16kHz       |
    | ReazonSpeech  | flac   | 16kHz       |
    | LEMAS         | mp3    | 16kHz       |
    | MLS           | flac   | 16kHz       |
    | Granary       | ogg    | 16kHz       |
    

    > **Format Note**:  
    > For datasets originally distributed in FLAC format, we **retain the lossless FLAC files in their original state**, without recompressing them into lossy formats like MP3 or OGG.

## Processing Pipeline
A rigorous multi-stage filtering pipeline is applied to ensure data quality:
1. **Duration & Speaking Rate Filtering**: Remove segments <0.5s or >30s; filter by language-specific speaking rate thresholds.
2. **Language Validation**: Verify text language consistency using `langdetect`.
3. **Deduplication**: Remove duplicate texts appearing more than 20 times to avoid overfitting.
4. **Acoustic Quality Control**: Filter low-quality audio via DNSMOS speech quality assessment.

## Highlights
- Diverse linguistic and temporal distribution
- High-quality cleaned speech-text training pairs
- Optimized for multilingual speech modeling and generalization

## Data Structure
```text
X-Voice-Dataset-Train/
├── tars/                     # Speech Data
│   ├── bg/
│   │   ├── bg_vox_part001.tar
│   │   ├── bg_vox_part002.tar
│   │   └── ...
|   ├── ...
│   └── zh/
│       ├── zh_emilia_part001.tar
│       ├── zh_emilia_part002.tar
│       └── ...
│
├── csvs/                     # Tramscript Data
│   ├── metadata_bg_voxpopuli.csv
│   ├── ...
│   └── metadata_zh_emilia.csv
│
└── csvs_stage2/              # Transcript Data for Stage 2 Finetuning
    ├── metadata_bg_voxpopuli.csv
    ├── ...
    └── metadata_zh_emilia.csv
```
## Use the Dataset
### CLI Download
```python
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id="XRXRX/X-Voice-Dataset-Train",
    # allow_patterns=["data/tars/bg/*.tar"], # you can download a specific package.  
    local_dir=[local path you want to place the dataset],
    repo_type="dataset",
    local_dir_use_symlinks=False
)
```
### Unzip
```bash
cd [local path you want to place the dataset]

for lang in data/tars/*/; do
    lang_name=$(basename "$lang")
    mkdir -p "wavs/$lang_name"
    tar xf "$lang"*.tar -C "wavs/$lang_name" --strip-components=1 --skip-old-files
done
```
Then you can refer to [X-Voice Training](https://github.com/sunnyxrxrx/X-Voice/blob/main/src/x_voice/train/README.md) for subsequent training process.

> **Note:**
> 
>   The data from Gigaspeech 2 (including Thai, Indonesian, and Vietnamese) is currently not included in this repo due to storage constraints and license restrictions. You can download them from the [official source](https://huggingface.co/datasets/speechcolab/gigaspeech2/tree/main) or refer to [our repo in ModelScope](http://modelscope.cn/datasets/sunnyxrxrx/X-Voice-Dataset-Train/tree/master/tars).
## License

**This dataset contains data from multiple sources, each with its own license.**
Users must comply with the license of each individual sub-dataset they use.

| Dataset | License | Commercial Use |
|---|---|---|
| Multilingual LibriSpeech | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Yes |
| Emilia | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Yes |
| LEMAS | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Yes |
| VoxPopuli | [CC-0](https://creativecommons.org/publicdomain/zero/1.0/) + [European Parliament's legal notice](https://www.europarl.europa.eu/legal-notice/en/) for the raw data | Yes |
| Granary (MOSEL Part) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Yes |
| GigaSpeech 2 | [License agreement required](https://huggingface.co/datasets/speechcolab/gigaspeech2) | See terms |
| Reazon Speech | [CDLA-Sharing-1.0 ](https://cdla.dev/sharing-1-0/) + **only for the purpose of [Japanese Copyright Act](https://www.cric.or.jp/english/clj/cl2.html) Article 30-4.** | See terms |
| KoreaSpeech | Refer to the [repo](https://huggingface.co/datasets/jp1924/KoreaSpeech) |  |