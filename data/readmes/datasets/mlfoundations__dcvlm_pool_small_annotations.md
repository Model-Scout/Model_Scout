---
pretty_name: DCVLM-Pool (small) — per-sample annotations
license: apache-2.0
language:
- en
- zh
- de
- fr
- ja
- ko
- es
- nl
task_categories:
- image-text-to-text
- visual-question-answering
size_categories:
- 100M<n<1B
tags:
- multimodal
- vision-language
- datacomp
- data-curation
- data-filtering
- metadata
viewer: false
---

# DCVLM-Pool (small) — per-sample annotations

Every **filtering annotation** we computed for the **small** data pool of our
[DataComp-VLM](https://arxiv.org/abs/2606.28551) paper: image quality, image–text alignment, language ID,
text-quality classifiers, multimodal perplexity, decontamination scores and more — **up to 167 fields per
sample** (180 distinct fields overall), for all **120,940,134 samples** across **166 source datasets**.

These are the raw annotations, *not* a filtered dataset. They are the inputs our curation pipeline consumes
to build a training mixture: you pick fields, pick thresholds, and get a subset. Releasing them means you can
reproduce our filters, or design your own, **without recomputing anything on 828 GB of raw data**.

The pool these annotate is [`mlfoundations/dcvlm_pool_small`](https://huggingface.co/datasets/mlfoundations/dcvlm_pool_small)
— 12,206 WebDataset shards, 10.3 TB.

## Layout

One JSON file per pool shard, under the source dataset's directory — **exactly mirroring the pool's own
`<source>/<shard>.tar` layout**, so `ai2d/000000.json` annotates `ai2d/000000.tar`.

```
datacomp_1b/000000.json … 004309.json    # 4,310 shards (largest source)
relaion-2b-en-vol-1-unpacked-TEST/…      # 3,015 shards
flanv2/000000.json … 001240.json         # 1,241 shards
ai2d/000000.json                         # 1 shard
…                                        # 166 sources, 12,206 files, 828 GB
```

Each file is a JSON object mapping the sample's WebDataset `__key__` → its annotations. For example:

```json
{
  "481c61f555bfbdecf6d13a73052ef621-0": {
    "length_tokens": 3405, "length_tokens_text_only": 78, "length_images": 1,
    "clip_score_siglip2_b16_224_standard_mean": 0.859,
    "iqa_v2_koniq10k_mean": 0.584,
    "im_height": {"jpg": 365}, "im_width": {"jpg": 512}, "im_entropy_mean": 7.67,
    "language_detection_annotation_lingua_0_lan": "en",
    "text_quality_weborganizer_topic_label": "Travel",
    "text_quality_dolma3_fasttext_score": 0.539,
    "unifilter_score_qwen3_0_6b": 3.125,
    "imdecont_max": 0.226,
    "within_sample_repetition_detection": 10.0
  }
}
```

## The annotations

| Family | Fields | What it is |
| --- | :--: | --- |
| **Image–text alignment** | 48 | CLIP-style scores from 4 encoders (`clip_vitl14_224`, `dfn_public`, `siglip2_b16_224`, `longclip_vitl14_224`) × 4 turn scopes (`standard`, `prev_turn_only`, `next_turn_only`, `prev_and_next_turn`) × min/mean/max over the sample's images |
| **Image statistics** | 36 | Per-image `height`, `width`, aspect ratio, KB, bits-per-pixel, `clarity` (sharpness), `luma`, `saturation`, `entropy` — raw per-member dict plus min/mean/max |
| **Image quality (IQA)** | 24 | No-reference quality predictors trained on 8 IQA datasets (`live`, `csiq`, `tid2013`, `kadid10k`, `flive`, `spaq`, `clive`, `koniq10k`), min/mean/max. A legacy `iqa_*` (v1) set is also present on some sources; prefer `iqa_v2_*` |
| **Language ID** | 14 | Top-3 languages + scores from **two** detectors, `lingua` and `nllb` (flattened `_0/_1/_2` fields plus the raw `_top3` list) |
| **Text quality** | 10 | `weborganizer` topic + format labels, NVIDIA domain label, two NVIDIA edu-value scores (`nemotron4`, `mixtral`), DCLM-baseline and Dolma-3 fastText scores |
| **Decontamination** | 6 | `imdecont_*` = similarity of each image to our eval-benchmark image index, plus the matched index id (`imdecont_image_match`); `textdecontamination` = binary text-side overlap check (`1` = clean) |
| **Length / tokens** | 5 | `length_chars`, `length_tokens` (full multimodal, incl. image tiles), `length_tokens_text_only`, `length_tokens_trainable_only`, `length_images` |
| **Custom fastText** | 4 | Quality classifiers targeting our `val` and `core` evaluation suites |
| **Multimodal perplexity** | 3 | `Qwen2.5-VL-3B-Instruct` cross-entropy on text-only and image+text, plus their difference as **conditional mutual information** — how much the image actually helps predict the text |
| **UniFilter** | 2 | Learned data-quality scores from `qwen2_5_1_5b` and `qwen3_0_6b` UniFilter models |
| **Heuristic flags** | 4 | `detoxify` (binary, `1` = passes toxicity check), `zero_sequence_filter` / `digit_sequence_filter` (integer counts of degenerate token runs, typically 0–5), `within_sample_repetition_detection` (integer 0–10 repetition rating within a sample) |

### Coverage caveats

- **The field set varies by source** (106–167 fields), because some annotators only apply to some data. It is
  uniform *within* a file, so reading one record tells you that source's schema.
- **Missing ≠ failed.** `textdecontamination` is only present on text-bearing sources, `detoxify` is absent on
  some web-scale captioning sources. Treat an absent field as "not applicable".
- **Image fields are `null` for text-only samples.** `imdecont_*` instead uses sentinels: **`-1.0`** when the
  sample has no images at all, and **`-1.7e38`** (float32 min, with `imdecont_image_match == -1`) when an
  image returned no index match. Both mean "uncontaminated" and both pass a `< threshold` test — so compare
  raw values directly and **don't** normalize or take absolute values.

## Usage

Grab one source (each file is 5–90 MB, so pull only what you need):

```python
from huggingface_hub import hf_hub_download
import json

p = hf_hub_download("mlfoundations/dcvlm_pool_small_annotations",
                    "ai2d/000000.json", repo_type="dataset")
ann = json.load(open(p))          # {sample_key: {field: value}}
```

Or a whole source directory:

```python
from huggingface_hub import snapshot_download
snapshot_download("mlfoundations/dcvlm_pool_small_annotations", repo_type="dataset",
                  allow_patterns="chartqa/*")
```

Then select keys and keep only those samples when reading the matching pool shard:

```python
# The decontamination applied to every source in our released mixtures:
keep = {
    k for k, a in ann.items()
    if a["imdecont_max"] < 0.75                       # no near-duplicate of an eval image
    and (a.get("textdecontamination", 1) > 0.0)       # no eval-text overlap (absent => passes)
}

# Layer on whatever else you want, e.g. a quality + alignment + language filter:
keep = {
    k for k in keep
    if (ann[k].get("iqa_v2_koniq10k_mean") or 0) > 0.5
    and (ann[k].get("clip_score_clip_vitl14_224_standard_mean") or 0) > 25
    and ann[k]["language_detection_annotation_lingua_0_lan"] == "en"
}
```

⚠️ **Alignment scores are not on a shared scale** — inspect each encoder's own distribution before picking a
threshold. On `datacomp_1b`, `clip_vitl14_224` and `longclip_vitl14_224` run ~20–35, `dfn_public` ~0–5, and
`siglip2_b16_224` is an unbounded logit spanning roughly −17 to 20.

The `__key__` values match the pool shard exactly, so filtering is a set-membership test while streaming:

```python
import webdataset as wds
ds = wds.WebDataset("ai2d/000000.tar").select(lambda s: s["__key__"] in keep)
```

## Citation

```bibtex
@article{farina2026datacomp,
  title={DataComp-VLM: Improved Open Datasets for Vision-Language Models},
  author={Farina, Matteo and Udandarao, Vishaal and Nguyen, Thao and Kuzucu, Selim and B{\"o}ther, Maximilian and Hochlehnert, Andreas and Ghosh, Adhiraj and Nezhurina, Marianna and Roth, Karsten and Struber, Joschka and others},
  journal={arXiv preprint arXiv:2606.28551},
  year={2026}
}
```
