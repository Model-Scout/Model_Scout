---
license: apache-2.0
language:
- en
- ja
- ko
- zh
---
# Dataset Card for HuggingFace-CJK-Metadata

## Dataset Summary

This dataset provides structured metadata and documentation extracted from the top 700 most downloaded datasets per language on the Hugging Face Hub for Chinese (zh), Japanese (ja), Korean (ko), and English (en, as a reference). The collection includes both high-level metadata (e.g., size, license, task type) and raw dataset card contents, enabling large-scale, cross-linguistic analysis of data curation, documentation quality, and cultural development patterns in East Asian NLP communities.
All download statistics were recorded on **January 28, 2025**, and the dataset includes a total of **3,300+ entries** spanning metadata and documentation fields.

## Supported Tasks

This dataset is intended for:
- Dataset ecosystem analysis
- Meta-evaluation of documentation quality
- Cultural and institutional analysis of NLP practices across languages
- Visualization and benchmarking of dataset trends

## Languages

- **zh** – Chinese
- **ja** – Japanese
- **ko** – Korean
- **en** – English (reference baseline)

---

## Dataset Structure

The dataset contains two main components: structured metadata and full dataset card content, each organized by language (English, Chinese, Japanese, Korean).

```
huggingface-cjk-metadata/
└── data/
├── dataset_card/
│ ├── dataset_cards_en.csv
│ ├── dataset_cards_ko.csv
│ ├── dataset_cards_ja.csv
│ └── dataset_cards_zh.csv
└── dataset_meta/
├── dataset_meta_en.csv
├── dataset_meta_ko.csv
├── dataset_meta_ja.csv
└── dataset_meta_zh.csv
```

### 📘 `dataset_meta` files

Each row corresponds to a Hugging Face dataset and includes structured metadata fields:

| Field               | Description |
|---------------------|-------------|
| `id`                | Hugging Face dataset ID (e.g., `skt/kogpt2`) |
| `author`            | Dataset creator (user or organization) |
| `created_at`        | Timestamp when the dataset repo was created |
| `lastModified`      | Timestamp of the latest commit |
| `sha`               | Git commit SHA |
| `downloads_30`      | Number of downloads in the past 30 days |
| `downloads_alltime` | Total number of downloads |
| `likes`             | Number of likes on the dataset page |
| `tags`              | Associated tags |
| `tasks`             | NLP tasks associated with the dataset |
| `description`       | Short dataset summary |
| `citation`          | Citation information |
| `languages`         | Languages covered (e.g., `ko`, `en`, `zh`) |
| `language_category` | One of: `monolingual`, `en-paired`, `multilingual` |
| `size_categories`   | Estimated dataset size (e.g., `10K<n<100K`) |
| `paperswithcode_id` | Linked PapersWithCode ID (if any) |
| `private`           | Boolean indicating if repo is private |
| `gated`             | Boolean for gated access |
| `disabled`          | Boolean for deactivated datasets |
| `license`           | License name (e.g., `apache-2.0`, `cc-by-nc-4.0`) |
| `arxiv_id`          | arXiv paper ID (if applicable) |
| `url`               | Hugging Face dataset URL |
| `task_ids`          | Internal Hugging Face task identifiers |


### 📄 `dataset_card` files

Each file contains raw Hugging Face dataset card contents in two fields:

| Field             | Description |
|------------------|-------------|
| `dataset_id`     | Dataset identifier (same as `id` in meta) |
| `yaml_metadata`  | Structured YAML block from the top of the README |
| `markdown_content` | The full free-text markdown body of the dataset card |

These cards enable deeper qualitative analyses of documentation quality, structure, and cultural content across languages.

---

## Repository

All scraping code and analysis notebooks can be found at:  
👉 **GitHub**: [https://github.com/Dasol-Choi/cjk-huggingface-analysis](https://github.com/Dasol-Choi/cjk-huggingface-analysis)


## Citation
```bibtext
@misc{choi2025languagedataleftbehind,
      title={No Language Data Left Behind: A Comparative Study of CJK Language Datasets in the Hugging Face Ecosystem}, 
      author={Dasol Choi and Woomyoung Park and Youngsook Song},
      year={2025},
      eprint={2507.04329},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2507.04329}, 
}
```

## Contact
- dasolchoi@yonsei.ac.kr