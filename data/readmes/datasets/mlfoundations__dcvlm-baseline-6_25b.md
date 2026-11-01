---
pretty_name: DCVLM-Baseline (6.25B tokens)
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
- 1M<n<10M
tags:
- webdataset
- multimodal
- vision-language
- datacomp
configs:
- config_name: preview
  data_files:
  - split: train
    path: preview/*.parquet
---

# DCVLM-Baseline (6.25B tokens)

**DCVLM-Baseline** is the reference training mixture from our [DataComp-VLM](https://arxiv.org/abs/2606.28551) paper.
It is a **pre-mixed, decontaminated, ready-to-train** multimodal pretraining dataset, materialized as flat
[WebDataset](https://github.com/webdataset/webdataset) tar shards so it can be consumed by **any** training
stack.

This dataset version is a small **6.25B-token (small-pool)** release consisting of **3,253,356 samples**.

> ⚠️ **NOTE: The training data is the WebDataset shards under [`shards/`](./tree/main/shards).** The `preview`
> config shown in the Dataset Viewer above is a **small, downsampled rendering**
> built purely so the HF-Hub can display examples---it is **not** the dataset you
> train on. See [Loading the dataset](#loading-the-dataset).

## The mixture

The mixture matches our paper's `Instruction-heavy` mix. Proportions are by **training samples**:

| Data type      | Ratio | Description                                             |
| -------------- | :----: | ------------------------------------------------------- |
| `instruction`  |  70%   | Visual instruction / VQA / multi-turn chat              |
| `text`         |  15%   | Text-only instruction data                              |
| `captioning`   |  10%   | Single image-captioning data                            |
| `mmdoc_mt`     |   5%   | Interleaved multimodal documents (multi-image)          |

## Repository layout

```
shards/000000.tar … 000383.tar   # THE dataset: WebDataset shards
preview/preview-0000.parquet      # small rendered sample, for the Dataset Viewer only
dataset_info.json                 # provenance: counts, token totals, seed
README.md
```

## Sample schema (WebDataset shards)

Each training example is one WebDataset sample: a group of members sharing a common **key**. Members:

| Member              | Type  | Meaning                                                                                         |
| ------------------- | ----- | ----------------------------------------------------------------------------------------------- |
| `conversations.txt` | text  | The conversation (see format below). Present in **every** sample.                               |
| `0.jpg`, `1.jpg`, … | image | The images, **0-indexed in the order they are referenced**. The N-th `<image>` token → `N.jpg`. |
| `data_type.txt`     | text  | `instruction` / `text` / `captioning` / `mmdoc_mt`.                                             |
| `ds_name.txt`       | text  | Originating source dataset (provenance).                                                        |
| `orig_url.txt`      | text  | Original source shard URL (provenance).                                                         |
| `ntok.txt`          | text  | Training token count for this sample (full multimodal count, including image tiles).            |
| `mdp.txt`           | text  | `max_dynamic_patch` — the image-tiling parameter used for this sample's source (provenance).    |

**Text-only** samples (`data_type == text`) carry **no** image members. **Multi-image** samples
(`mmdoc_mt`, and some instruction data) carry several `N.jpg/png/webp` members.

### `conversations.txt` format

Turns are stored as `role:value`, joined by the separator `"<EOCL>\n"` (a literal `<EOCL>` followed by a
newline). Roles are `human` and `gpt`. `<image>` placeholder tokens appear inline inside the turn text. The
N-th `<image>` corresponds to image member `N.jpg`.

Example (a single image-captioning sample):

```
human:<image>
Describe the image concisely.<EOCL>
gpt:Fiddlenecks, aka Devil's lettuce
```

This is the [ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered)-style turn
format serialized to a single string. The helper below converts it back into a standard list of turn dicts
(`[{"from": ..., "value": ...}, …]`).

## Loading the dataset

### Parse `conversations.txt` → JSON turns

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

### Stream the training data with the `webdataset` library (recommended)

```python
import webdataset as wds
from huggingface_hub import get_token

REPO = "mlfoundations/dcvlm-baseline-6_25b"
url = f"https://huggingface.co/datasets/{REPO}/resolve/main/shards/{{000000..000383}}.tar"
url = f"pipe:curl -s -L {url} -H 'Authorization:Bearer {get_token()}'"

dataset = wds.WebDataset(url, shardshuffle=True).shuffle(1000).decode("pilrgb")

for sample in dataset:
    conversations = txt2conversations(sample["conversations.txt"].decode())
    images = [sample[k] for k in sorted(sample) if k.endswith(".jpg")]  # PIL, in <image> order
    data_type = sample["data_type.txt"].decode()
    # ... tokenize / collate for your trainer ...
```

### Browse the rendered preview

The `preview` config is a small, downsampled slice for quick inspection. It is **not** the training data.

```python
from datasets import load_dataset
prev = load_dataset("mlfoundations/dcvlm-baseline-6_25b", "preview", split="train")
prev[0]  # {"images": [PIL...], "conversations": [{"from","value"},...], "data_type", "ds_name", ...}
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