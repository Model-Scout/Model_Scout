---
pretty_name: DCVLM-Pool (small)
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

# DCVLM-Pool (small)

The **raw candidate pool** at the `small` scale of our [DataComp-VLM](https://arxiv.org/abs/2606.28551)
benchmark: **120,940,134 samples / ~187.5B tokens / 10.3 TB** across **166 source datasets**, as
[WebDataset](https://github.com/webdataset/webdataset) tar shards.

This pool is **unfiltered and unmixed**. It is the input to a data-curation experiment, not a training set. You choose
the filters and the mixing ratios, and create another training set. If you instead want a
ready-to-train dataset, use [`dcvlm-baseline-200b`](https://huggingface.co/datasets/mlfoundations/dcvlm-baseline-200b)
(our reference SoTA DCVLM-baseline dataset) or [`dcvlm-balanced-200b`](https://huggingface.co/datasets/mlfoundations/dcvlm-balanced-200b).

> **Every filtering annotation we computed on this pool is released separately** in
> [`dcvlm_pool_small_annotations`](https://huggingface.co/datasets/mlfoundations/dcvlm_pool_small_annotations)
> — ~170 fields per sample (quality, alignment, language, decontamination, perplexity, etc), laid out 1:1 with
> the shards here, so `ai2d/000000.json` annotates `ai2d/000000.tar`. Filter from those, then read only the
> samples you kept. You do **not** need to recompute anything.

## Repository layout

Flat, one directory per source dataset:

```
datacomp_1b/000000.tar … 004309.tar     # 4,310 shards
relaion-2b-en-vol-1-unpacked-TEST/…     # 3,015 shards
flanv2/000000.tar … 001240.tar          # 1,241 shards
ai2d/000000.tar                         # 1 shard
…                                       # 166 sources, 12,206 shards total
```

Shard sizes vary a lot by source (~20 MB for text-only up to ~4 GB for interleaved documents). Each source
directory also carries three metadata elements:

| Metadata | Contents |
| --- | --- |
| `num_saved_samples.txt` | Sample count for that source (these sum to 120,940,134) |
| `full_token_sum.txt` | Total multimodal tokens for that source |
| `extracted_percentiles.json` | Deciles of each annotation field for that source — handy for picking filter thresholds without scanning the data |

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

`<key>.filters.json` carries a small per-sample subset of the annotations (length/token counts). The **full**
annotation set lives in the annotations repo linked above.

⚠️ Two naming quirks to code around: captioning sources built via `img2dataset` use a **double
dot** before the artifact extensions (`<key>..phash.txt`), and the `relaion-*-unpacked-TEST` directories are
ordinary training volumes despite the `TEST` suffix. Names are preserved verbatim so the annotations repo
stays a 1:1 match.

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

The pool is 10.3 TB, so pull one source at a time rather than the whole repo:

```python
from huggingface_hub import snapshot_download
snapshot_download("mlfoundations/dcvlm_pool_small", repo_type="dataset",
                  allow_patterns="ai2d/*")
```

Or stream shards directly without downloading:

```python
import webdataset as wds
from huggingface_hub import get_token

BASE = "https://huggingface.co/datasets/mlfoundations/dcvlm_pool_small/resolve/main"
urls = [f"{BASE}/ai2d/{i:06d}.tar" for i in range(1)]
urls = [f"pipe:curl -s -L {u} -H 'Authorization:Bearer {get_token()}'" for u in urls]

for sample in wds.WebDataset(urls).decode("pilrgb"):
    conversations = txt2conversations(sample["conversations.txt"].decode())
    images = [sample[k] for k in sorted(sample) if k.endswith(".jpg")]
```

### Curating a subset

Pull the matching annotations, threshold whatever you like, and keep only those keys while streaming. The below snippet
reproduces the decontamination we apply to every source in our released mixtures:

```python
import json
from huggingface_hub import hf_hub_download

ann = json.load(open(hf_hub_download(
    "mlfoundations/dcvlm_pool_small_annotations", "ai2d/000000.json", repo_type="dataset")))

keep = {k for k, a in ann.items()
        if a["imdecont_max"] < 0.75                    # no near-duplicate of an eval image
        and a.get("textdecontamination", 1) > 0.0}     # no eval-text overlap (absent => passes)

ds = wds.WebDataset(urls).select(lambda s: s["__key__"] in keep)
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
