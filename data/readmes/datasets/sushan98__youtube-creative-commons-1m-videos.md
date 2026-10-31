---
pretty_name: YouTube Creative Commons Links (1M)
license: cc-by-4.0
language:
  - en
  - uk
  - es
  - hi
  - fr
  - de
  - id
  - pt
  - it
  - ru
  - ar
  - ko
task_categories:
  - feature-extraction
  - text-to-video
tags:
  - youtube
  - creative-commons
  - video-links
  - metadata
  - multilingual
size_categories:
  - 1M<n<10M
configs:
  - config_name: default
    data_files:
      - split: train
        path: youtube_links_1m.csv.gz
---

# YouTube Creative Commons Links (1M)

A curated collection of **1,000,000 YouTube video links** to Creative Commons–licensed content, with channel and language metadata. The dataset is intended for research, benchmarking, and building multilingual video corpora where the original creators' license terms are preserved.

> **This dataset contains links and metadata only. It does not include any video, audio, or transcript files.**

---

## At a glance

| | |
|---|---|
| **Records** | 1,000,000 |
| **Unique videos** | 1,000,000 (no duplicate `video_id`) |
| **Unique channels** | 362,622 |
| **Languages** | 57 language codes |
| **License** | Creative Commons Attribution (reuse allowed) |
| **Format** | Gzipped CSV (`youtube_links_1m.csv.gz`, ~32 MB) |

## Language distribution (top 12)

| Code | Language | Videos | Share |
|---|---|---:|---:|
| `en` | English | 669,868 | 67.0% |
| `uk` | Ukrainian | 51,121 | 5.1% |
| `es` | Spanish | 46,046 | 4.6% |
| `hi` | Hindi | 40,421 | 4.0% |
| `fr` | French | 38,091 | 3.8% |
| `de` | German | 18,705 | 1.9% |
| `id` | Indonesian | 18,084 | 1.8% |
| `pt` | Portuguese | 16,612 | 1.7% |
| `it` | Italian | 13,848 | 1.4% |
| `ru` | Russian | 10,906 | 1.1% |
| `ar` | Arabic | 8,317 | 0.8% |
| `ko` | Korean | 7,680 | 0.8% |

Language labels come with a `source_language` field that records how each label was assigned: `metadata` (445,709 rows), `detection` (504,048 rows), or `unknown` (50,243 rows).

## Data fields

| Column | Type | Description |
|---|---|---|
| `video_id` | string | YouTube video ID (11 characters) |
| `url` | string | Full watch URL: `https://www.youtube.com/watch?v={video_id}` |
| `channel_id` | string | YouTube channel ID of the uploader |
| `language` | string | ISO 639-1 language code of the video |
| `license` | string | License of the video. All rows: "Creative Commons Attribution license (reuse allowed)" |

### Example row

```csv
video_id,url,channel_id,language,license
AN87fYk9UtY,https://www.youtube.com/watch?v=AN87fYk9UtY,UCPcSxQz9pVuvpZpGErowQbg,en,Creative Commons Attribution license (reuse allowed)
```

## Quick start

```python
from datasets import load_dataset

ds = load_dataset("sushan98/youtube-creative-commons-1m-videos", split="train")
print(ds)
print(ds[0]["url"])

# Filter to Spanish-language videos
es = ds.filter(lambda x: x["language"] == "es")
print(len(es))
```

Or with pandas:

```python
import pandas as pd
df = pd.read_csv("hf://datasets/sushan98/youtube-creative-commons-1m-videos/youtube_links_1m.csv.gz")
```

## Construction

1. Source: the first 1,000,000 rows of [`Pclanglais/youtube-commons-metadata`](https://huggingface.co/datasets/Pclanglais/youtube-commons-metadata), which lists CC-BY YouTube videos.
2. Columns were reduced to `video_id`, `url` (derived from `video_id`), `channel_id`, `language`, and `license`.
3. Output written as CSV and gzip-compressed.

Rows are kept in the order of the source file. The subset is not a random sample.

## Intended uses

- Building multilingual video or speech corpora (after downloading media under its license)
- Benchmarking retrieval, recommendation, or channel-level analysis
- Studying the language and channel distribution of CC-licensed YouTube content

## Out-of-scope uses

- Redistributing video or audio content without the creators' permission and license compliance
- Using the data to identify or profile individuals beyond what the public metadata already shows

## Limitations

- Links may become unavailable over time if videos are deleted, made private, or re-licensed.
- Language labels are automated or metadata-derived and may be wrong for some rows. Check `source_language` when precision matters.
- The dataset does not include titles, descriptions, view counts, or durations. Fetch these through the YouTube Data API if you need them.

## Citation

If you use this dataset, please cite the source dataset and link back to this page:

```
@misc{youtube_cc_links_1m,
  title  = {YouTube Creative Commons Links (1M)},
  author = {Ghimire, Sushan},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sushan98/youtube-creative-commons-1m-videos}
}
```

## Acknowledgements

Built on [`Pclanglais/youtube-commons-metadata`](https://huggingface.co/datasets/Pclanglais/youtube-commons-metadata). Thanks to the creators who publish their work under Creative Commons licenses.

---

## License and source

- **Dataset license:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). This applies to the metadata and link list in this repository.
- **Video license:** each linked video is licensed by its creator under Creative Commons Attribution. If you use or redistribute a video, credit the creator and link to the license.
- **Source dataset:** [`Pclanglais/youtube-commons-metadata`](https://huggingface.co/datasets/Pclanglais/youtube-commons-metadata). The first 1,000,000 rows were used.
- **Platform terms:** YouTube's Terms of Service still apply. Use the official YouTube Data API or other permitted means to access content.
