---
annotations_creators:
- machine-generated
language:
- en
- ko
license: other
license_name: modhaus-fan-archive
task_categories:
- image-classification
- feature-extraction
- image-to-text
tags:
- kpop
- triples
- objekts
- photocard
- cosmo
- modhaus
- digital-collectibles
- video-classification
size_categories:
- 10K<n<100K
pretty_name: tripleS Objekts Archive
dataset_info:
  features:
  - name: file_name
    dtype: string
  - name: image
    dtype: image
  - name: media_file_name
    dtype: string
  - name: frontMedia
    dtype: string
  - name: slug
    dtype: string
  - name: id
    dtype: string
  - name: artist
    dtype: string
  - name: member
    dtype: string
  - name: memberSortOrder
    dtype: int64
  - name: season
    dtype: string
  - name: class
    dtype: string
  - name: collectionNo
    dtype: string
  - name: shortCode
    dtype: string
  - name: side
    dtype: string
  - name: onOffline
    dtype: string
  - name: comoAmount
    dtype: int64
  - name: hasAudio
    dtype: bool
  - name: accentColor
    dtype: string
  - name: backgroundColor
    dtype: string
  - name: textColor
    dtype: string
  - name: description
    dtype: string
  - name: createdAt
    dtype: int64
  - name: contract
    dtype: string
---

# tripleS Objekts Archive (HD Images, Motion MP4s & Full Metadata)

Complete digital collectible photocards (Objekts) dataset for the K-Pop girl group **tripleS** (Modhaus / COSMO app).

## Dataset Summary

- **Total Objekts**: 11,570 unique digital collectibles
- **Total Images**: 21,885 high-resolution card scans (Front & Back)
- **Total Motion & Voice Videos**: 177 animated card loops & voice message MP4 clips
- **Members**: All 24 members (S1–S24) + Sub-units (AAA, KRE, Assemble24, etc.)
- **Seasons Included**: Atom01, Atom02, Binary01, Binary02, Cream01, Cream02, Divine01, Ever01
- **Metadata fields**: `member`, `season`, `class`, `collectionNo`, `shortCode`, `side` (front/back), `frontMedia`, `media_file_name`, `hasAudio`, `onOffline`, `comoAmount`, `accentColor`, `contract`, `createdAt`, `description`.

## Directory Structure

```text
├── metadata.jsonl          # Hugging Face Dataset format linking all images, media & attributes
├── all_objekts.json        # Master raw JSON containing all 11,570 objekt items
├── summary.json            # Statistical counts by member, season, and class
├── sync_checkpoint.json    # Incremental update state tracker
├── by_member/              # Subdivided JSON files per member
├── by_season/              # Subdivided JSON files per season
├── images/                 # Hierarchical HD card images (Front & Back)
└── media/                  # Hierarchical Motion & Voice MP4 video clips
    ├── Binary02/
    │   └── SeoYeon/
    │       └── binary02-seoyeon-360z.mp4
    └── ...
```

## Quick Start / Usage

### Using Python `datasets`

```python
from datasets import load_dataset

# Load dataset with automatic image decoding
dataset = load_dataset("fadhilafif98/triples-objekts", split="train")

# Access sample item
first_sample = dataset[0]
print(first_sample["member"], first_sample["season"], first_sample["side"])

# Display image
image = first_sample["image"]
image.show()
```

### Direct CDN Access (Images & Video)

* **Front Image**: `https://huggingface.co/datasets/fadhilafif98/triples-objekts/resolve/main/images/{season}/{member}/{slug}_front.png`
* **Motion Video (.mp4)**: `https://huggingface.co/datasets/fadhilafif98/triples-objekts/resolve/main/media/{season}/{member}/{slug}.mp4`

## Disclaimer & Copyright

All visual assets and trademarks belong to **MODHAUS** and the **COSMO** platform. This dataset is compiled strictly for non-commercial fan archival, educational, indexing, and computer vision research purposes.
