---
language:
  - ko
  - en
license: other
task_categories:
  - image-to-text
  - sentence-similarity
pretty_name: Ko-En Visual Document Retrieval (VDR) Training Data
size_categories:
  - 100K<n<1M
tags:
  - multimodal
  - retrieval
  - visual-document-retrieval
  - korean
  - english
  - qwen3-vl
extra_gated_prompt: >-
  By requesting access you agree to use this dataset strictly for research
  purposes and to respect the licenses of the constituent image sources
  (colpali / llamaindex / kovdr_pub / kovdr_priv). Redistribution of the
  underlying images is not permitted without contacting the original authors.
extra_gated_fields:
  Name: text
  Affiliation: text
  Intended use case: text
  I will use this dataset for research only: checkbox
configs:
  - config_name: corpus
    data_files:
      - split: train
        path: corpus/train-*
  - config_name: train
    data_files:
      - split: train
        path: train/train-*
---

# Ko-En Visual Document Retrieval (VDR) Training Data

Multimodal retrieval training set used to fine-tune `Qwen/Qwen3-VL-Embedding-2B`
on mixed Korean and English visual-document retrieval: the query is text,
the document is a page image (PDF screenshot / slide / report / chart /
invoice / etc.), and each row ships 1 positive + 7 mined hard negatives.

## Structure

This repo is a single dataset with two configs:

| config   | rows     | description                                                          |
|----------|----------|----------------------------------------------------------------------|
| `corpus` | 207,522  | deduplicated image store, one row per unique page image              |
| `train`  | 325,023  | anchor text + positive_id + negative_1_id … negative_7_id (no images)|

Splitting `corpus` from `train` keeps the ~74 GB image pool stored once on
Hub instead of being re-embedded on every training row (which would balloon
to >500 GB).

### `corpus` schema

| column    | type      | example                                   |
|-----------|-----------|-------------------------------------------|
| image_id  | string    | `colpali/23382.jpg`                       |
| source    | string    | `colpali` \| `llamaindex` \| `kovdr_pub` \| `kovdr_priv` |
| image     | Image()   | PIL image (lazy-decoded on access)        |

### `train` schema

| column          | type   | example                                                              |
|-----------------|--------|----------------------------------------------------------------------|
| anchor          | string | `CAP 기반 조정이 Jensen-Shannon 발산을 활용한 분포 유사성 검증에 ...` |
| positive_id     | string | `kovdr_pub/3950.png`                                                 |
| negative_1_id   | string | `colpali/23382.jpg`                                                  |
| … up to         |        |                                                                       |
| negative_7_id   | string | `kovdr_priv/400161c64b.png`                                          |

## Access

This is a **gated dataset** — manual approval only. Request access via
the dataset page and briefly describe your intended use case; I approve
individual requests.

Once approved:

```bash
huggingface-cli login
```

## Usage

### Option A — Rehydrate to a local image directory (recommended for training)

Download the corpus once, unpack every image to disk using its `image_id`
as the relative path. This gives back the same directory structure I use
locally, so existing pipelines that expect path strings work unchanged.

```python
from pathlib import Path
from datasets import load_dataset

OUT_IMG_DIR = Path("./ko_en_vdr_images")

corpus = load_dataset("yjoonjang/ko-en-vdr-private", name="corpus", split="train")
for row in corpus:
    dst = OUT_IMG_DIR / row["image_id"]
    if dst.exists():
        continue
    dst.parent.mkdir(parents=True, exist_ok=True)
    row["image"].save(dst)
```

Then fold the IDs back into absolute paths for your trainer / collator:

```python
from datasets import load_dataset

train = load_dataset("yjoonjang/ko-en-vdr-private", name="train", split="train")

def resolve(row):
    row["positive"] = str(OUT_IMG_DIR / row.pop("positive_id"))
    for i in range(1, 8):
        row[f"negative_{i}"] = str(OUT_IMG_DIR / row.pop(f"negative_{i}_id"))
    return row

train = train.map(resolve)
# schema now matches the original local layout:
#   anchor, positive, negative_1, ..., negative_7  (all strings; image cols are paths)
```

### Option B — Lazy lookup at dataloader time (no image extraction)

Keep images inside the HF `corpus` dataset and resolve IDs -> PIL images on
demand. Good when you train from a single machine and don't want to manage
a separate image dir, but slower than path-based loading because every
access decodes the bytes stream.

```python
from datasets import load_dataset

corpus = load_dataset("yjoonjang/ko-en-vdr-private", name="corpus", split="train")
id2idx = {cid: i for i, cid in enumerate(corpus["image_id"])}

train = load_dataset("yjoonjang/ko-en-vdr-private", name="train", split="train")

def resolve(batch):
    batch["positive"] = [corpus[id2idx[i]]["image"] for i in batch["positive_id"]]
    for k in range(1, 8):
        batch[f"negative_{k}"] = [corpus[id2idx[i]]["image"] for i in batch[f"negative_{k}_id"]]
    return batch

train.set_transform(resolve)  # lazy; decodes only the rows a dataloader pulls
```

### Training with `sentence-transformers` (the reference setup)

After rehydrating via **Option A**, this dataset plugs directly into the
`CachedMultipleNegativesRankingLoss` + `MatryoshkaLoss` pipeline used in
the reference `Qwen3-VL-Embedding-2B` fine-tune:

```python
from sentence_transformers import SentenceTransformer, losses
# (train / collator / trainer setup — see the project's TRAIN/v1/train.py)

loss = losses.MatryoshkaLoss(
    model=model,
    loss=losses.CachedMultipleNegativesRankingLoss(
        model=model,
        scale=20.0,
        mini_batch_size=4,
    ),
    matryoshka_dims=[2048, 1024, 768, 512, 256, 128],
)
```

The column order matters: the first column (`anchor`) is treated as the
query, the second (`positive`) as the paired positive, and the rest
(`negative_1`…`negative_7`) as hard negatives for in-batch + triplet loss.

## Sources and licensing

Images come from four sources with different provenances:

| source       | files  | notes                                                                  |
|--------------|--------|------------------------------------------------------------------------|
| `colpali`    | ~118k  | page images derived from `vidore/colpali-train` and related releases   |
| `llamaindex` | ~54k   | page images derived from llamaindex's public evaluation sets            |
| `kovdr_pub`  | ~7.5k  | Korean VDR — public release                                            |
| `kovdr_priv` | ~28k   | Korean VDR — private source; redistribution not granted                |

Because of the mixed licensing (especially `kovdr_priv`), this repo is
gated and must not be re-uploaded or redistributed. Cite the upstream
sources if you use this dataset in published work.

## Citation

If this dataset is useful for your work, please cite the upstream VDR /
ColPali / llamaindex releases, and mention this repo as the mix/mining
pipeline source.

```bibtex
@misc{yjoonjang_ko_en_vdr_2026,
  title        = {Ko-En Visual Document Retrieval Training Data},
  author       = {Yongjoon Jang},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/datasets/yjoonjang/ko-en-vdr-private}},
}
```
