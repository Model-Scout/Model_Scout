# Multilingual Synthetic OCR Starter

24,000 synthetic document pages in 6 languages with word/line/paragraph boxes

## About this dataset
A ready-to-use, **24,000-page subset** of NVIDIA's **OCR-Synthetic-Multilingual-v1**, a large synthetic document dataset for OCR text detection, recognition and reading order (used to train Nemotron OCR v2). The full source is 12.3 million pages and 5.45 TB of HDF5 shards; this starter takes **4,000 pages per language** for six languages and stores them as Parquet, so you can train or benchmark a multilingual OCR model on Kaggle without handling terabytes of data.

Every page keeps its **original JPEG bytes** (quality 100, not re-encoded or resized) plus the source's full annotations: the full-page text, **word, line and paragraph boxes** (axis-aligned `bbox` and 4-point `quad`), and the **reading-order graph**.

> **This is an unofficial republished subset. All credit goes to NVIDIA; NVIDIA has not endorsed this copy.** The authoritative full dataset is at https://huggingface.co/datasets/nvidia/OCR-Synthetic-Multilingual-v1

## Contents
| Language | Folder | train | validation | test | Image data |
|---|---|---|---|---|---|
| English | `en/` | 3,000 | 500 | 500 | 1.69 GB |
| Japanese | `ja/` | 3,000 | 500 | 500 | 1.59 GB |
| Korean | `ko/` | 3,000 | 500 | 500 | 1.78 GB |
| Russian | `ru/` | 3,000 | 500 | 500 | 1.67 GB |
| Chinese (Simplified) | `zh_hans/` | 3,000 | 500 | 500 | 1.66 GB |
| Chinese (Traditional) | `zh_hant/` | 3,000 | 500 | 500 | 1.65 GB |
| **Total** | | **18,000** | **3,000** | **3,000** | **10.04 GB** |

Each language folder holds `train-0000N-of-00003.parquet` (1,000 pages each), `validation-00000-of-00001.parquet` and `test-00000-of-00001.parquet`. Typical page: about 850 x 845 px, median 16 text lines.

| File | What it holds |
|---|---|
| `{lang}/{split}-*.parquet` | One row per page: `sample_id`, `lang`, `split`, `source_shard`, `source_row`, `width`, `height`, `jpeg_quality`, **`image`** (JPEG bytes), `image_sha256`, `text`, `word_bboxes`, `line_bboxes`, `para_bboxes`, `relation_graph` (JSON strings, lossless), `n_words`, `n_lines`, `n_paragraphs`. |
| `index.csv` | All 24,000 pages without the image bytes: `uid` (`lang/split/sample_id`, unique), which Parquet file and row each page is in, size, counts and a 120-character text preview. Handy for filtering before loading images. |
| `preview/` | 8 example pages per language as plain JPEGs (48 files) to eyeball the data. |
| `sampling_manifest.json` | Exactly which source shard and rows were taken for every language/split, pages per shard, bytes fetched. |
| `source_manifest.json` | Source repo, pinned revision `69696a1cc543ef3a0f8e9892a89c17293e915263`, licence text and build time. |

Annotation format (from the source): `word_bboxes` = list of `{text, bbox:[x,y,w,h], quad:[[x0,y0],[x1,y1],[x2,y2],[x3,y3]]}`; `line_bboxes` adds `para_idx`, `line_idx`, `word_indices`; `para_bboxes` = paragraph boxes; `relation_graph[para][sentence]` lists the word/line indices of each sentence (reading order). Quads are clockwise from the top-left vertex.

## How to use
```python
import io, json, glob
import pandas as pd
from PIL import Image, ImageDraw

f = glob.glob("/kaggle/input/**/ru/train-00000-of-00003.parquet", recursive=True)[0]
df = pd.read_parquet(f)
row = df.iloc[0]
img = Image.open(io.BytesIO(row["image"])).convert("RGB")
draw = ImageDraw.Draw(img)
for line in json.loads(row["line_bboxes"]):
    draw.polygon([tuple(p) for p in line["quad"]], outline=(255, 0, 0), width=2)
print(row["text"][:200])
img
```
Ideas: fine-tune a multilingual text-recognition model (e.g. TrOCR / Donut / PaddleOCR) on the line crops; train a text detector on word or line quads; learn reading order from `relation_graph`; compare scripts (CJK vs Cyrillic vs Latin) on one model.

## Changes from the original
- **Subset only:** for each language, the first 3,000 rows of `train/train_000.h5`, and the first 500 rows of `validation/validation_000.h5` and `test/test_000.h5`. The native train/validation/test membership is kept. This is **not a uniform random sample** of the full dataset (see `sampling_manifest.json`).
- **Format:** converted from HDF5 to Parquet. Image bytes are copied unchanged (JPEG magic and dimensions checked against the source `dimensions` field; SHA-256 stored per page). Annotations are the source JSON split into four JSON-string columns, nothing dropped.
- Added `uid`, `index.csv`, `preview/` and the manifests. `sample_id` repeats across languages and splits in the source, so use `uid` (`lang/split/sample_id`) as a global key.
- Built on Kaggle by reading the source shards with HTTP range requests (no full-shard download); the exact rows taken are listed in `sampling_manifest.json`.

## Source & license
- **Creator:** NVIDIA Corporation. Source: https://huggingface.co/datasets/nvidia/OCR-Synthetic-Multilingual-v1 (dataset creation date per the card: 15 April 2026).
- **License:** the source states: "Dataset Governing Terms: Use of the dataset is governed by the Creative Commons Attribution 4.0 International License (CC BY 4.0)." This subset is shared under the same **CC BY 4.0** licence (https://creativecommons.org/licenses/by/4.0/). The card also states the dataset "is ready for commercial/non-commercial use."
- The generation pipeline is a heavily modified version of **SynthDoG** from the Donut project (Kim et al.).
- **Citation** (from the source card):
```bibtex
@misc{chesler2026ocr_synthetic_multilingual,
  title   = {{OCR-Synthetic-Multilingual-v1}},
  author  = {Chesler, Ryan},
  year    = {2026},
  publisher = {NVIDIA},
  url     = {https://huggingface.co/datasets/nvidia/OCR-Synthetic-Multilingual-v1},
  note    = {Synthetically generated multilingual OCR dataset built on a heavily modified SynthDoG pipeline}
}
```

## Caveats
- **Synthetic documents.** Pages are rendered by a generator, so accuracy on this data does not guarantee accuracy on real scans, photos or handwriting.
- **No Indic, Arabic or other scripts:** exactly the six languages of the source (English, Japanese, Korean, Russian, Simplified and Traditional Chinese).
- Rows come from the first shard of each split, so they may share rendering settings or text sources more than a random sample would.
- The parquet files are large (about 0.4 GB each); load one file at a time, or filter with `index.csv` first.

---

### 👍 Found this dataset useful?

If it helps your project, please **download it** and give it an **upvote**. Upvotes help other researchers and developers find it, and they keep me motivated to maintain it. Thank you!

출처: Kaggle (yashdogra/multilingual-synthetic-ocr-starter)
태그: nlp, computer vision, deep learning, image, multilingual
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2026-10-05T13:21:38.477Z
