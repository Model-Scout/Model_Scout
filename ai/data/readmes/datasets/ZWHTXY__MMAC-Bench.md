---
license: cc-by-4.0
task_categories:
- visual-question-answering
- question-answering
language:
- en
- zh
- hi
- id
- ja
- ko
- mn
- ms
- ta
- vi
pretty_name: MMAC-Bench Dataset
size_categories:
- 10K<n<100K
configs:
- config_name: default
  data_files:
  - split: text_only
    path: data/text_only.parquet
  - split: multi_modal
    path: data/multi_modal.parquet
---

# MMAC SEA Dataset

This repository contains a Hugging Face `datasets`-loadable version of MMAC-Bench.

If you use this dataset, please cite the paper listed in the [Citation](#citation)
section.

## Usage

Install dependencies:

```bash
pip install -U datasets huggingface_hub
```

Load both splits:

```python
from datasets import load_dataset

ds = load_dataset("ZWHTXY/MMAC-Bench")

print(ds)
print(ds["text_only"][0])
print(ds["multi_modal"][0])
```

The dataset has two splits:

- `text_only`: text-only QA rows.
- `multi_modal`: image-based QA rows with image and speech paths.

Load only one split:

```python
from datasets import load_dataset

text_only = load_dataset("ZWHTXY/MMAC-Bench", split="text_only")
multi_modal = load_dataset("ZWHTXY/MMAC-Bench", split="multi_modal")
```

Filter by country or language:

```python
from datasets import load_dataset

ds = load_dataset("ZWHTXY/MMAC-Bench")

china_text = ds["text_only"].filter(lambda x: x["country"] == "China")
singapore_tamil_mm = ds["multi_modal"].filter(
    lambda x: x["country"] == "Singapore" and x["language"] == "Tamil"
)
```

Download the full repository, including raw JSON files, images, and audio:

```python
from huggingface_hub import snapshot_download

local_dir = snapshot_download(
    repo_id="ZWHTXY/MMAC-Bench",
    repo_type="dataset",
)
print(local_dir)
```

Use the `country`, `region_code`, and `language` columns to filter subsets.

## Columns

- `country`, `region_code`, `language`, `modality`
- `question`, `option1`, `option2`, `option3`, `option4`
- `correct_options`, `category`
- `knowledge_point`, `multi_step_reasoning`, `rephrased_question`
- `image`
- `standard_english_audio`, `english_with_accent_audio`, `none_english_audio`

The audio columns contain relative paths to `.wav` files in this repository.

Raw JSON files and media assets are kept in `Text-Only/` and `Multi-Modal/`.

## Citation

If you download or use this dataset, please cite:

```bibtex
@inproceedings{zheng-etal-2026-mmac,
    title = "{MMAC}: A Multilingual, Multimodal Alignment Framework for Cultural Grounding Evaluation",
    author = "Zheng, Weihua  and
      Liu, Zhengyuan  and
      Chakraborty, Tanmoy  and
      Xu, Weiwen  and
      Gao, Xiaoxue  and
      Tan, Bryan Chen Zhengyu  and
      Zou, Bowei  and
      Liu, Chang  and
      Hu, Yujia  and
      Xie, Xing  and
      Yi, Xiaoyuan  and
      Yao, Jing  and
      Wang, Chaojun  and
      Li, Long  and
      Liu, Rui  and
      Liu, Huiyao  and
      Inoue, Koji  and
      Sumida, Ryuichi  and
      Kawahara, Tatsuya  and
      Xu, Fan  and
      Ye, Lingyu  and
      Tian, Wei  and
      Kim, Dongjun  and
      Jung, Jimin  and
      Seo, Jaehyung  and
      Wangsajaya, Nadya Yuki  and
      Duc, Pham Minh  and
      Saxena, Ojasva  and
      Nandi, Palash  and
      Tao, Xiyan  and
      Karlina, Wiwik  and
      Luong, Tuan  and
      Vasan, Keertana Arun  and
      Lee, Roy Ka-Wei  and
      Chen, Nancy F.",
    editor = "Liakata, Maria  and
      Moreira, Viviane P.  and
      Zhang, Jiajun  and
      Jurgens, David",
    booktitle = "Proceedings of the 64th Annual Meeting of the {A}ssociation for {C}omputational {L}inguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2026",
    address = "San Diego, California, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.acl-long.989/",
    pages = "21667--21709",
    ISBN = "979-8-89176-390-6",
    abstract = "The global deployment of Large Language Models (LLMs) underscores the urgent need to evaluate their cultural alignment. However, assessing genuine ``cultural awareness'' across modalities (text, vision, speech) and languages remains a significant challenge. To comprehensively investigate this domain, we propose MMAC, a systematic framework that encompasses a tri-modally aligned cultural benchmark creation pipeline and a five-dimensional evaluation protocol to assess cross-country awareness disparities, evaluate cross-lingual and cross-modal consistency, and verify cultural knowledge generalization and grounding validity. Given the prevailing Western cultural bias in current models, we focus on 8 Asian countries as our dataset foundation to more acutely reveal potential cultural deficiencies in LLMs. Our dataset, MMAC-bench, features 27,000 human-curated questions across 10 languages. Crucially, it is the first dataset aligned at the input level across text, image, and speech, enabling direct cross-modal transfer tests. Each question consists of multiple-choice options accompanied by open-ended generated explanations, where 79{\%} require multi-step reasoning grounded in cultural context, moving beyond simple memorization. We probe the causes of modal divergence, offering insights into fostering culturally robust MLLMs."
}
```
