---
pretty_name: DCVLM-Pool (large)
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
- 1B<n<10B
tags:
- webdataset
- multimodal
- vision-language
- datacomp
viewer: false
---

# DCVLM-Pool (large)

The **raw candidate pool** at the `large` scale of our [DataComp-VLM](https://arxiv.org/abs/2606.28551)
benchmark: **1,949,321,868 samples / 166.7 TB** across **166 source datasets**, as
[WebDataset](https://github.com/webdataset/webdataset) tar shards — **≈4× the medium pool**.

> ## 🚚 Upload in progress
>
> This repo is being populated incrementally and is **not yet complete** — shards are still being
> uploaded. Sources already present are final and safe to use; sources with fewer shards than the counts
> quoted below have not finished uploading yet. Please bear with us and check back for the full release.

This pool is **unfiltered and unmixed**. It is the input to a data-curation experiment, not a training set. You choose
the filters and the mixing ratios, and create another training set. If you instead want a
ready-to-train dataset, use [`dcvlm-baseline-200b`](https://huggingface.co/datasets/mlfoundations/dcvlm-baseline-200b)
(our reference SoTA DCVLM-baseline dataset) or [`dcvlm-balanced-200b`](https://huggingface.co/datasets/mlfoundations/dcvlm-balanced-200b).

> ## ⚠️ This repo is an **increment** on top of the small and medium pools — read this first
>
> The large pool **contains the medium pool, which in turn contains the small pool**. To avoid storing and
> serving ~41 TB twice, this repo holds **only the 146,658 shards that large adds**; the other 48,570 are
> already published in [`dcvlm_pool_small`](https://huggingface.co/datasets/mlfoundations/dcvlm_pool_small)
> and [`dcvlm_pool_medium`](https://huggingface.co/datasets/mlfoundations/dcvlm_pool_medium).
>
> | | shards | size |
> | --- | ---: | ---: |
> | in **this** repo (new at large) | 146,658 | 125.6 TB |
> | in [`dcvlm_pool_medium`](https://huggingface.co/datasets/mlfoundations/dcvlm_pool_medium) | 36,364 | 30.8 TB |
> | in [`dcvlm_pool_small`](https://huggingface.co/datasets/mlfoundations/dcvlm_pool_small) | 12,206 | 10.3 TB |
> | **full large pool** | **195,228** | **166.7 TB** |
>
> **Download all three repos and merge the trees into one directory.** Shard indices are disjoint by
> construction — for every source, small holds indices `0 … j-1`, medium continues at `j … k-1`, and this
> repo continues at `k` (e.g. `datacomp_1b` is `000000–004309` in small, `004310–017236` in medium and
> `017237–068967` here) — so nothing is overwritten and the merged directory is the complete large pool.
> See [Getting the full pool](#getting-the-full-pool).

## Repository layout

One directory per source dataset, **continuing the medium pool's shard numbering**:

```
datacomp_1b/017/017237.tar … 068/068967.tar          # 51,731 new shards (see the note below)
relaion-2b-en-vol-1-unpacked-TEST/012/012057.tar …   # 36,165 new shards (012057 … 048221)
flanv2/004/004920.tar … 022/022866.tar               # 17,947 new shards
relaion-2b-en-vol-2-unpacked-TEST/005/005891.tar …   # 17,671 new shards (005891 … 023561)
flan/003748.tar … 013241.tar                         #  9,494 new shards (flat)
ai2d/000002.tar                                      #      1 new shard
…                                                    # 166 sources, 146,658 new shards total
```

⚠️ **Four directories are nested at this scale** (the medium pool only needed this for `datacomp_1b`).
Their shard counts exceed the Hugging Face limit of 10,000 files per directory, so they are bucketed by
thousand as `<source>/NNN/<shard>.tar` (`017237.tar` → `datacomp_1b/017/`):

| nested source | new shards | index range |
| --- | ---: | --- |
| `datacomp_1b` | 51,731 | `017237 … 068967` |
| `relaion-2b-en-vol-1-unpacked-TEST` | 36,165 | `012057 … 048221` |
| `flanv2` | 17,947 | `004920 … 022866` |
| `relaion-2b-en-vol-2-unpacked-TEST` | 17,671 | `005891 … 023561` |

Flatten them once after downloading:

```bash
for d in datacomp_1b relaion-2b-en-vol-1-unpacked-TEST flanv2 relaion-2b-en-vol-2-unpacked-TEST; do
  [ -d "$d" ] && mv "$d"/*/*.tar "$d"/ && rmdir "$d"/*/
done
```

⚠️ Note that `relaion-2b-en-vol-1-unpacked-TEST`, `relaion-2b-en-vol-2-unpacked-TEST` and `flanv2` are
**flat** in the small and medium repos and nested only here, so flattening is what makes the three trees
merge cleanly. `datacomp_1b` is nested in both this repo and the medium one; its buckets merge without
collision (medium's `datacomp_1b/017/` and this repo's `datacomp_1b/017/` hold disjoint shards).
Every other source is flat, exactly as in the small and medium pools.

Shard sizes vary a lot by source (~20 MB for text-only up to ~4 GB for interleaved documents). Each source
directory also carries one metadata file:

| Metadata | Contents |
| --- | --- |
| `num_saved_samples.txt` | Sample count for that source **across the full large pool** (these sum to 1,949,321,868) |

⚠️ These counts are **cumulative, not incremental** — they already include the shards that live in the
small and medium pools. When you merge the trees, **let this repo's `num_saved_samples.txt` overwrite the
other two**; do not add them together. The small pool's `full_token_sum.txt` and
`extracted_percentiles.json` are not re-shipped here, so they survive the merge untouched — note that they
describe the small pool only.

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

The full pool is 166.7 TB, so pull one source at a time rather than the whole repo:

```python
from huggingface_hub import snapshot_download
snapshot_download("mlfoundations/dcvlm_pool_large", repo_type="dataset",
                  allow_patterns="ai2d/*")
```

Or stream shards directly without downloading:

```python
import webdataset as wds
from huggingface_hub import get_token

BASE = "https://huggingface.co/datasets/mlfoundations/dcvlm_pool_large/resolve/main"
urls = [f"{BASE}/ai2d/{i:06d}.tar" for i in range(2, 3)]   # 000002.tar is the shard new at large
urls = [f"pipe:curl -s -L {u} -H 'Authorization:Bearer {get_token()}'" for u in urls]

for sample in wds.WebDataset(urls).decode("pilrgb"):
    conversations = txt2conversations(sample["conversations.txt"].decode())
    images = [sample[k] for k in sorted(sample) if k.endswith(".jpg")]
```

⚠️ Remember that a source's shards are split across three repos. `ai2d/000000.tar` is in the small pool,
`ai2d/000001.tar` is in the medium pool and `ai2d/000002.tar` is here; a URL list for the full source has
to span all three. For the four nested sources above, remember the `NNN/` bucket in the URL.

### Getting the full pool

Download one source from all three repos into the same directory:

```python
from huggingface_hub import snapshot_download

for repo in ("mlfoundations/dcvlm_pool_small",
             "mlfoundations/dcvlm_pool_medium",
             "mlfoundations/dcvlm_pool_large"):
    snapshot_download(repo, repo_type="dataset", allow_patterns="ai2d/*",
                      local_dir="dcvlm_pool_large")
```

For the four nested sources, flatten the buckets afterwards (see [Repository layout](#repository-layout)).
The small and medium copies of `num_saved_samples.txt` are overwritten by this repo's, which is what you
want — the large counts are the cumulative ones.

## Citation

```bibtex
@article{farina2026datacomp,
  title={DataComp-VLM: Improved Open Datasets for Vision-Language Models},
  author={Farina, Matteo and Udandarao, Vishaal and Nguyen, Thao and Kuzucu, Selim and B{\"o}ther, Maximilian and Hochlehnert, Andreas and Ghosh, Adhiraj and Nezhurina, Marianna and Roth, Karsten and Struber, Joschka and others},
  journal={arXiv preprint arXiv:2606.28551},
  year={2026}
}
```
