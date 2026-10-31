---
pretty_name: Korean-Pashto Parallel Corpus
language:
  - ko
  - ps
license: other
task_categories:
  - translation
tags:
  - korean
  - pashto
  - korean-pashto
  - ko-ps
  - translation
  - parallel-corpus
  - machine-translation
  - multilingual
  - low-resource-language
  - nlp
  - pashto-ai
  - text-data
  - jsonl
  - iPashto
size_categories:
  - n<1K
---

# Korean–Pashto Parallel Corpus

A Korean–Pashto parallel text dataset containing Korean sentences paired with their corresponding Pashto translations.

This dataset is published by **nassimjp** on Hugging Face to support Korean-to-Pashto machine translation, bilingual language research, and the development of Pashto-capable AI models.

**Dataset repository:**  
https://huggingface.co/datasets/nassimjp/korean-pashto-parallel-corpus

## Dataset Overview

| Property | Description |
|---|---|
| Dataset name | Korean–Pashto Parallel Corpus |
| Source language | Korean (`ko`) |
| Target language | Pashto (`ps`) |
| Data type | Parallel text |
| File format | JSONL |
| Text encoding | UTF-8 |
| Main direction | Korean → Pashto |
| Main data file | `data/translation_cache_ko.jsonl` |
| Publisher | nassimjp |

## Dataset Contents

The dataset contains Korean text paired with Pashto translations. Each JSONL line represents one translation pair.

### Data file

[`data/translation_cache_ko.jsonl`](https://huggingface.co/datasets/nassimjp/korean-pashto-parallel-corpus/blob/main/data/translation_cache_ko.jsonl)

### Example

```json
{"ko": "내 이상형이 뭔지 모르겠어.", "ps": "زه نه پوهیږم چې زما مثالي کس څوک دی."}
{"ko": "내 존재를 알리고 싶어", "ps": "زه غواړم خپل شتون څرګند کړم"}
{"ko": "우연을 가장해서 여러 번 마주쳐보세요.", "ps": "د تصادف په څیر څو ځله سره مخ شئ."}
```

### Field descriptions

- `ko`: The original Korean text.
- `ps`: The corresponding Pashto translation.

Each record is a standalone JSON object on a single line. The JSONL format is suitable for streaming, processing large files, and loading data into machine learning pipelines.

## Intended Uses

This dataset may be useful for:

- Korean-to-Pashto machine translation.
- Supervised fine-tuning (SFT) of multilingual language models.
- Improving Korean–Pashto cross-lingual capabilities.
- Pashto language technology research.
- Building bilingual text-processing applications.
- Translation evaluation after suitable quality review.
- Research on low-resource language pairs.

## Loading the Dataset

You can load the dataset with the Hugging Face `datasets` library.

```python
from datasets import load_dataset

dataset = load_dataset(
    "nassimjp/korean-pashto-parallel-corpus",
    data_files="data/translation_cache_ko.jsonl",
    split="train",
)

print(dataset[0])
print(dataset.column_names)
```

Expected columns:

```python
["ko", "ps"]
```

You can also access the JSONL file directly:

```python
from huggingface_hub import hf_hub_download
import json

file_path = hf_hub_download(
    repo_id="nassimjp/korean-pashto-parallel-corpus",
    filename="data/translation_cache_ko.jsonl",
    repo_type="dataset",
)

with open(file_path, "r", encoding="utf-8") as f:
    first_record = json.loads(next(f))

print("Korean:", first_record["ko"])
print("Pashto:", first_record["ps"])
```

## Data Quality and Limitations

This dataset is provided as a Korean–Pashto parallel corpus. Users should independently evaluate translation accuracy, fluency, spelling, grammar, and sentence alignment before using it in production systems or high-stakes applications.

Potential limitations include:

- Some translations may be literal or unnatural in Pashto.
- Sentence alignment and translation accuracy may vary.
- The dataset's domain coverage and language distribution have not been fully documented here.
- The total number of records has not been independently verified in this dataset card.
- Duplicate entries and other data-quality issues should be checked before training.

The presence of a Korean sentence and a Pashto sentence in the same record does not guarantee that the translation is fully accurate.

## License and Usage

The dataset's upstream source, licensing terms, and redistribution permissions should be verified before assigning a license to this repository.

**License status:** Not yet independently verified.

Users are responsible for checking the rights associated with the source data and ensuring that their use complies with applicable copyright laws and other relevant requirements.

## Citation

If you use this dataset in research or a project, please cite the dataset repository:

```bibtex
@misc{korean_pashto_parallel_corpus,
  author       = {Nassim Nasibullah},
  title        = {Korean-Pashto Parallel Corpus},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/nassimjp/korean-pashto-parallel-corpus}}
}
```

## Acknowledgements

This dataset contributes to the development of language resources for Pashto and supports research into Korean–Pashto translation and multilingual AI.

Published by **nassimjp** on Hugging Face.

Dataset: https://huggingface.co/datasets/nassimjp/korean-pashto-parallel-corpus
