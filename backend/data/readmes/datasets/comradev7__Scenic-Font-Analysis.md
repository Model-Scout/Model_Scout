---
license: other
task_categories:
- image-classification
language:
- hi
- ja
- ko
tags:
- fonts
- typography
- scene-text
- synthetic
---

# Scenic Font Analysis — multi-track dataset

Shared dataset repository for the Samsung PRISM *Scenic Font Analysis* project.
Each contributor publishes their own **track** so the data can be merged into a
single training set without schema drift.

## Repository layout

```
README.md
schema.json
track_a/
  ground_truth.csv      # required
  manifest.json         # recommended (counts + checksums)
  images.tar.gz         # required; members are named image_filename at the archive root
track_b/                # another contributor, identical structure
track_c/                # another contributor, identical structure
tools/                  # helper scripts (also in the project repo)
```

> **Why a tar and not a folder?** Hugging Face rejects any repository directory
> with more than **10,000 files**. Tracks with thousands of images therefore ship
> a single `images.tar.gz`; `tools/pull_all_tracks.py` extracts it back into
> `images/` automatically (only tracks with <= 10,000 images may use a loose
> `images/` folder).

## The contract (see `schema.json`)

Every `track_*/ground_truth.csv` must have exactly these columns:

| column | notes |
|---|---|
| `image_filename` | basename of the file in `images/` |
| `language` | e.g. hindi / japanese / korean |
| `font_family` | |
| `font_style` | raw source label (kept for provenance) |
| `style_unified` | one of `regular`, `bold`, `italic`, `bolditalic` |
| `split` | one of `train`, `val`, `test` |
| `is_clean` | boolean |
| `text` | label text |

`style_unified` is the **single unified taxonomy**. Track A's 9 raw weights are
collapsed by `taxonomy.unify_style()`:
`thin/extralight/light/regular/medium -> regular`,
`semibold/bold/extrabold/black -> bold`, and italic/oblique labels become
`italic` / `bolditalic`.

## Add your own track

1. Install + log in:
   ```
   pip install -U "huggingface_hub[cli]"
   hf auth login
   ```
2. Ask Vignesh to add you: repo -> **Settings -> Collaborators** (repo is private).
3. Put your labels in a CSV and stage a validated track folder:
   ```
   python tools/export_track.py --track b --images <your_images_dir> \
       --ground-truth <your_labels.csv> --out staging
   ```
   Writes `staging/track_b/{ground_truth.csv,manifest.json,images/}` and enforces
   the schema above.
4. Upload (resumable, safe to re-run):
   ```
   python tools/push_repo.py --repo comradev7/Scenic-Font-Analysis --folder staging
   ```

## Consume / merge all tracks

```
python tools/pull_all_tracks.py --repo comradev7/Scenic-Font-Analysis --out data
python tools/merge_tracks.py --root data --out data/merged/ground_truth.csv
```

`merge_tracks.py` validates each track, normalizes labels, adds a `track` column
and writes one merged CSV (with an `image_path` column relative to the dataset
root) ready for training.
