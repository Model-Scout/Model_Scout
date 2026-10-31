---
pretty_name: DCVLM-Pool (medium)
license: other
language:
- en
- zh
- de
- fr
- ja
- ko
- la
- fi
- tl
- bg
- es
- nl
task_categories:
- image-text-to-text
- visual-question-answering
size_categories:
- 100M<n<1B
tags:
- webdataset
- multimodal
- vision-language
- datacomp
viewer: false
---

# DCVLM-Pool (medium)

The **raw candidate pool** at the `medium` scale of our [DataComp-VLM](https://arxiv.org/abs/2606.28551)
benchmark: **483,576,747 samples / 41.1 TB** across **166 source datasets**, as
[WebDataset](https://github.com/webdataset/webdataset) tar shards — **≈4× the small pool**.

This pool is **unfiltered and unmixed**. It is the input to a data-curation experiment, not a training set. You choose
the filters and the mixing ratios, and create another training set. If you instead want a
ready-to-train dataset, use [`dcvlm-baseline-200b`](https://huggingface.co/datasets/mlfoundations/dcvlm-baseline-200b)
(our reference SoTA DCVLM-baseline dataset) or [`dcvlm-balanced-200b`](https://huggingface.co/datasets/mlfoundations/dcvlm-balanced-200b).

> ## ⚠️ This repo is an **increment** on top of the small pool — read this first
>
> The medium pool **contains the small pool**. To avoid storing and serving ~10 TB twice, this repo holds
> **only the 36,364 shards that medium adds**; the other 12,206 are already published in
> [`dcvlm_pool_small`](https://huggingface.co/datasets/mlfoundations/dcvlm_pool_small).
>
> | | shards | size |
> | --- | ---: | ---: |
> | in **this** repo (new at medium) | 36,364 | 30.8 TB |
> | in [`dcvlm_pool_small`](https://huggingface.co/datasets/mlfoundations/dcvlm_pool_small) | 12,206 | 10.3 TB |
> | **full medium pool** | **48,570** | **41.1 TB** |
>
> **Download both repos and merge the two trees into one directory.** Shard indices are disjoint by
> construction — for every source, the small pool holds indices `0 … k-1` and this repo continues at `k`
> (e.g. `datacomp_1b` is `000000–004309` there and `004310–017236` here) — so nothing is overwritten and
> the merged directory is the complete medium pool. See [Getting the full pool](#getting-the-full-pool).

## Repository layout

Flat, one directory per source dataset, **continuing the small pool's shard numbering**:

```
datacomp_1b/004/004310.tar … 017/017236.tar   # 12,927 new shards (see the note below)
relaion-2b-en-vol-1-unpacked-TEST/…           #  9,042 new shards (003015 … 012056)
flanv2/001241.tar … 004919.tar                #  3,679 new shards
ai2d/000001.tar                               #      1 new shard
…                                             # 166 sources, 36,364 new shards total
```

⚠️ **`datacomp_1b` is the one nested directory.** Its 12,927 shards exceed the Hugging Face limit of
10,000 files per directory, so they are bucketed by thousand as `datacomp_1b/NNN/<shard>.tar`
(`004310.tar` → `datacomp_1b/004/`). Flatten it once after downloading:

```bash
mv datacomp_1b/*/*.tar datacomp_1b/ && rmdir datacomp_1b/*/
```

Every other source is flat, exactly as in the small pool.

Shard sizes vary a lot by source (~20 MB for text-only up to ~4 GB for interleaved documents). Each source
directory also carries one metadata file:

| Metadata | Contents |
| --- | --- |
| `num_saved_samples.txt` | Sample count for that source **across the full medium pool** (these sum to 483,576,747) |

⚠️ These counts are **cumulative, not incremental** — they already include the shards that live in the
small pool. When you merge the two trees, **let this repo's `num_saved_samples.txt` overwrite the small
pool's**; do not add them together. (`datacomp_1b`, for example, reads 43,096,056 in the small pool and
172,358,492 here.) The small pool's `full_token_sum.txt` and `extracted_percentiles.json` are not
re-shipped here, so they survive the merge untouched — note that they describe the small pool only.

## Sample schema

Every sample is a group of tar members sharing a **key**. The member set depends on the source's `data_type`:

| `data_type` | Sources | Members |
| --- | :--: | --- |
| `instruction` | 108 | `<key>.conversations.txt`, one or more images (`<key>.jpg`), `<key>.filters.json` |
| `text` | 33 | `<key>.conversations.txt`, `<key>.filters.json` — **no images** |
| `captioning` | 15 | `<key>.jpg`/`.webp`, `<key>.txt` (the caption), `<key>.json` (original `img2dataset` record: source URL, uid, dimensions), `<key>.filters.json` |
| `mmdoc` | 9 | **Positionally interleaved** segments: `<key>.0.txt`, `<key>.1.jpg`, `<key>.2.txt`, … Sort by the integer index to reconstruct the document. No `conversations.txt` |

Alongside each image you also get some artifacts we computed for it — `<key>.sha256.txt`,
`<key>.phash.txt` (perceptual hash) and `<key>.sscd_disc_mixup.pt` (SSCD copy-detection embedding, which we used to run our image decontamination pipeline). These let you reproduce or
redo decontamination yourself.

`<key>.filters.json` carries a small per-sample subset of the annotations (length/token counts).

⚠️ Two naming quirks to code around: captioning sources built via `img2dataset` use a **double
dot** before the artifact extensions (`<key>..phash.txt`), and the `relaion-*-unpacked-TEST` directories are
ordinary training volumes despite the `TEST` suffix. Names are preserved verbatim.


### `conversations.txt` format

Turns are `role:value`, joined by the separator `"<EOCL>\n"`. Roles are `human` and `gpt`, and `<image>`
placeholders appear inline in the turn text — the N-th `<image>` refers to the N-th image member.

```
human:<image>
In the above food chain, which way does energy flow in the food chain?<EOCL>
gpt:from the flower to the caterpillar
```

```python
EOL_SEPARATOR = "<EOCL>\n"

def txt2conversations(txt: str) -> list[dict]:
    """Returns ShareGPT-style turns: [{"from": "human"|"gpt", "value": str}, ...]."""
    conversations = []
    for line in txt.split(EOL_SEPARATOR):
        if line == "":
            continue
        role = line.split(":", 1)[0]          # role is prepended before the first ':'
        value = line[len(role) + 1:]          # everything after that ':' is the value
        conversations.append({"from": role, "value": value})
    return conversations
```

## Loading

The pool is 41.1 TB, so pull one source at a time rather than the whole repo:

```python
from huggingface_hub import snapshot_download
snapshot_download("mlfoundations/dcvlm_pool_medium", repo_type="dataset",
                  allow_patterns="ai2d/*")
```

Or stream shards directly without downloading:

```python
import webdataset as wds
from huggingface_hub import get_token

BASE = "https://huggingface.co/datasets/mlfoundations/dcvlm_pool_medium/resolve/main"
urls = [f"{BASE}/ai2d/{i:06d}.tar" for i in range(1, 2)]   # 000001.tar is the shard new at medium
urls = [f"pipe:curl -s -L {u} -H 'Authorization:Bearer {get_token()}'" for u in urls]

for sample in wds.WebDataset(urls).decode("pilrgb"):
    conversations = txt2conversations(sample["conversations.txt"].decode())
    images = [sample[k] for k in sorted(sample) if k.endswith(".jpg")]
```

⚠️ Remember that a source's shards are split across two repos. `ai2d/000000.tar` is in the small pool and
`ai2d/000001.tar` is here; a URL list for the full source has to span both.

### Getting the full pool

Download one source from both repos into the same directory:

```python
from huggingface_hub import snapshot_download

for repo in ("mlfoundations/dcvlm_pool_small", "mlfoundations/dcvlm_pool_medium"):
    snapshot_download(repo, repo_type="dataset", allow_patterns="ai2d/*",
                      local_dir="dcvlm_pool_medium")
```

For `datacomp_1b`, flatten the buckets afterwards (see [Repository layout](#repository-layout)). The
small pool's copy of `num_saved_samples.txt` is overwritten by this repo's, which is what you want —
the medium counts are the cumulative ones.

## Citation

```bibtex
@article{farina2026datacomp,
  title={DataComp-VLM: Improved Open Datasets for Vision-Language Models},
  author={Farina, Matteo and Udandarao, Vishaal and Nguyen, Thao and Kuzucu, Selim and B{\"o}ther, Maximilian and Hochlehnert, Andreas and Ghosh, Adhiraj and Nezhurina, Marianna and Roth, Karsten and Struber, Joschka and others},
  journal={arXiv preprint arXiv:2606.28551},
  year={2026}
}
```
