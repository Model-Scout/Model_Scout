---
license: mit
task_categories:
- feature-extraction
language:
- en
- fr
- de
- it
- pt
- es
- ru
- ko
- ja
- zh
pretty_name: mtg card SIFT Feature dataset
size_categories:
- 100K<n<1M
tags:
- v5.1
---

# MTG Card SIFT Features Dataset (v5.1)

![demo](https://github.com/JakeTurner616/simple-mtg-feature-extraction/raw/main/docs/feature-detect.gif)

This dataset contains the **latest incremental MTG card SIFT + RootSIFT feature extraction pipeline**. It is designed for **server-side production inference**, enabling **additive updates to the FAISS index and `id_map.json`** without retraining or reindexing from scratch.

> **Note:** This version aligns with a daily `resources-nightly.zip` Hugging Face upload workflow for reliable continuous deployment via my production server.

---

## What’s New in v5.1?

| Feature              | v5.0                       | v5.1 (Current)                      |
| -------------------- | -------------------------- | ----------------------------------- |
| Index updates        | Additive-safe              | Same                                |
| Upload workflow      | Manual or ad-hoc           | Integrated with HF nightly pipeline |
| Logging              | Basic                      | Detailed zipping and upload logs    |
| Service impact       | Potential blocking uploads | Runs in background, non-blocking    |
| HF dataset structure | Single zip upload          | Same, consistent naming             |

---

## File Layout (`resources-nightly.zip`)

```
resources/
└── run/
    ├── candidate_features.h5     # Keypoints + descriptors per card (gzip HDF5)
    ├── faiss_ivf.index           # FAISS IVF-PQ index
    └── id_map.json               # Descriptor index-to-scryfall_id mapping
```

---

## What Is This?

A **high-precision visual descriptor dataset** for Magic: The Gathering cards, used for:

✅ **Visual Search**
✅ **Mobile/Server Card Scanning**
✅ **FAISS-based Similarity Search**
✅ **Incremental Model Growth**

---

## Pipeline Summary

1. **Image Acquisition**

   * Fetched from Scryfall using official API.
2. **Preprocessing**

   * Resize with aspect ratio, CLAHE on L-channel, grayscale conversion.
3. **Feature Extraction**

   * OpenCV SIFT + RootSIFT normalization.
4. **Storage**

   * `candidate_features.h5` using gzip compression.
5. **Indexing**

   * FAISS IVF-PQ (100 clusters, 8x8 PQ), additive updates supported.
6. **Mapping**

   * `id_map.json` aligns descriptors to `scryfall_id`.
7. **HF Upload**

   * Zipped nightly, uploaded to HF dataset repo in the background.

---

## Use Cases

✅ **Real-time card scanning** for Magic: The Gathering
✅ **Card image search pipelines**
✅ **Local inference on low-resource servers**
✅ **Model growth without reindexing**

---

## Workflow (Simplified)

```text
[Input Image]
    ↓
[CLAHE + SIFT + RootSIFT]
    ↓
[FAISS IVF-PQ Search]
    ↓
[Retrieve scryfall_id]
    ↓
[Result]
```

---

## Why v5.1 Matters

✅ **No SQLite required**
✅ **Works with h5py + NumPy**
✅ **Parallel-safe and resumable**
✅ **Tiny memory footprint**
✅ **MIT Licensed for free, unlimited use**

---

## Acknowledgments

Created by [JakeTurner616](https://github.com/JakeTurner616)
Powered by:

* [Scryfall API](https://scryfall.com/docs/api)
* [FAISS](https://github.com/facebookresearch/faiss)
* [OpenCV](https://opencv.org/)
* [h5py](https://www.h5py.org/)

---

For deep implementation details, see the [mtgscan.cards monorepo](https://github.com/mtgscan-cards/monolithic).