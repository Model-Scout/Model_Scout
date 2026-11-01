---
pretty_name: MM-JudgeBench
language:
- ar
- bn
- zh
- cs
- nl
- en
- fr
- de
- el
- he
- hi
- id
- it
- ja
- kk
- ko
- fa
- pl
- pt
- ro
- ru
- es
- tr
- uk
- vi
task_categories:
- visual-question-answering
- text-generation
size_categories:
- 100K<n<1M
tags:
- multilingual
- multimodal
- reward-modeling
- vlm-evaluation
- preference-evaluation
configs:
- config_name: m-vl-rewardbench
  data_files:
  - split: original
    path: data/m-vl-rewardbench/original.parquet
  - split: reversed
    path: data/m-vl-rewardbench/reversed.parquet
- config_name: m-opencqa
  data_files:
  - split: original
    path: data/m-opencqa/original.parquet
  - split: reversed
    path: data/m-opencqa/reversed.parquet
- config_name: m-mm-rewardbench
  data_files:
  - split: original
    path: data/m-mm-rewardbench/original.parquet
  - split: reversed
    path: data/m-mm-rewardbench/reversed.parquet
---

# MM-JudgeBench

## Dataset Summary

MM-JudgeBench is a multilingual multimodal preference benchmark for evaluating
vision-language judge and reward models. Each row contains an image reference,
a query, two candidate responses, and a preference label.

The dataset includes three configurations:

- `m-vl-rewardbench`
- `m-opencqa`
- `m-mm-rewardbench`

Each configuration provides two splits:

- `original`
- `reversed`

In the `reversed` split, the response order is swapped and the preference label
is inverted.

## Supported Tasks

- Multimodal preference evaluation
- Vision-language judge model evaluation
- Reward model evaluation

## Usage

```python
from datasets import load_dataset

ds = load_dataset("tahmedge/MM-JudgeBench", "m-vl-rewardbench", split="original")
```

```python
opencqa = load_dataset("tahmedge/MM-JudgeBench", "m-opencqa", split="original")
mm_rewardbench = load_dataset("tahmedge/MM-JudgeBench", "m-mm-rewardbench", split="original")
```

## Languages

Arabic, Bengali, Chinese, Czech, Dutch, English, French, German, Greek, Hebrew,
Hindi, Indonesian, Italian, Japanese, Kazakh, Korean, Persian, Polish,
Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese.

## Dataset Structure

### Data Fields

`m-vl-rewardbench`

- `id`: sample identifier
- `language`: language of the row
- `image_path`: image path in the dataset repository
- `query_source`: query source
- `query`: user query or instruction
- `response1`: first candidate response
- `response2`: second candidate response
- `label`: preferred response, either `A` or `B`

`m-opencqa`

- `id`: sample identifier
- `language`: language of the row
- `image_path`: image path in the dataset repository
- `query`: user query
- `response1`: first candidate response
- `response2`: second candidate response
- `label`: preferred response, either `A` or `B`

`m-mm-rewardbench`

- `id`: sample identifier
- `language`: language of the row
- `image_path`: image path in the dataset repository
- `query`: user query or instruction
- `response1`: first candidate response
- `response2`: second candidate response
- `label`: preferred response, either `A` or `B`

### Data Splits

| Config | Split | Rows | Samples | Languages per sample |
| --- | --- | ---: | ---: | ---: |
| `m-vl-rewardbench` | `original` | 30675 | 1227 | 25 |
| `m-vl-rewardbench` | `reversed` | 30675 | 1227 | 25 |
| `m-opencqa` | `original` | 28950 | 1158 | 25 |
| `m-opencqa` | `reversed` | 28950 | 1158 | 25 |
| `m-mm-rewardbench` | `original` | 107875 | 4315 | 25 |
| `m-mm-rewardbench` | `reversed` | 107875 | 4315 | 25 |

### Image Paths

The `image_path` field points to the corresponding image file in the dataset
repository.

```text
images/m-vl-rewardbench/LRVInstruction-000000007746.jpg
images/m-opencqa/0.png
images/m-mm-rewardbench/nocaps/13062.jpg
```

Images are stored as files in the dataset repository and are referenced by
`image_path`. When loading the dataset with `datasets.load_dataset`, the
`image_path` column is returned as a string. To access the image from the Hub,
download the referenced file with `huggingface_hub.hf_hub_download`:

```python
from datasets import load_dataset
from huggingface_hub import hf_hub_download
from PIL import Image

repo_id = "tahmedge/MM-JudgeBench"

ds = load_dataset(repo_id, "m-vl-rewardbench", split="original")
row = ds[0]

image_file = hf_hub_download(
    repo_id=repo_id,
    filename=row["image_path"],
    repo_type="dataset",
)

image = Image.open(image_file)
```

If you clone the dataset repository locally, open images by joining the local
repository path with `image_path`:

```python
from pathlib import Path
from PIL import Image

repo_root = Path("MM-JudgeBench")
image = Image.open(repo_root / row["image_path"])
```

To download the full dataset repository, including all image files, clone it
with Git LFS enabled:

```bash
git lfs install
git clone https://huggingface.co/datasets/tahmedge/MM-JudgeBench
cd MM-JudgeBench
git lfs pull
```

After cloning, all image files are available under the local `images/`
directory, and every `image_path` value can be resolved relative to the cloned
repository root.

## Citation

If you use MM-JudgeBench, please cite this work along with the source
benchmarks it is built upon.

**MM-JudgeBench**

```bibtex
@inproceedings{laskar2026lost,
  title = {Lost in Translation: Do {LVLM} Judges Generalize Across Languages?},
  author = {Laskar, Md Tahmid Rahman and Islam, Mohammed Saidul and Nayeem, Mir Tafseer and Bhuiyan, Amran and Rahman, Mizanur and Joty, Shafiq and Hoque, Enamul and Huang, Jimmy},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2026},
  pages = {34986--35002},
  address = {San Diego, California, United States},
  publisher = {Association for Computational Linguistics},
  year = {2026}
}
```

**VL-RewardBench** (source of `m-vl-rewardbench`)

```bibtex
@inproceedings{li2025vl,
  title={VL-RewardBench: a challenging benchmark for vision-language generative reward models},
  author={Li, Lei and Wei, Yuancheng and Xie, Zhihui and Yang, Xuqing and Song, Yifan and Wang, Peiyi and An, Chenxin and Liu, Tianyu and Li, Sujian and Lin, Bill Yuchen and others},
  booktitle={Proceedings of the Computer Vision and Pattern Recognition Conference},
  pages={24657--24668},
  year={2025}
}
```

**OpenCQA** (source of `m-opencqa`)

```bibtex
@inproceedings{kantharaj2022opencqa,
  title={Opencqa: Open-ended question answering with charts},
  author={Kantharaj, Shankar and Do, Xuan Long and Leong, Rixie Tiffany and Tan, Jia Qing and Hoque, Enamul and Joty, Shafiq},
  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
  pages={11817--11837},
  year={2022}
}
```

**Multimodal RewardBench** (source of `m-mm-rewardbench`)

```bibtex
@article{yasunaga2025multimodal,
  title={Multimodal rewardbench: Holistic evaluation of reward models for vision language models},
  author={Yasunaga, Michihiro and Zettlemoyer, Luke and Ghazvininejad, Marjan},
  journal={arXiv preprint arXiv:2502.14191},
  year={2025}
}
```
