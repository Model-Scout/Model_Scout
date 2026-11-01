---
license: mit
task_categories:
- question-answering
language:
- ar
- bn
- de
- en
- es
- fr
- hi
- id
- it
- ja
- ko
- pt
- sw
- yo
- zh
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
configs:
- config_name: en
  data_files:
  - split: train
    path: en/train.json
- config_name: ar_xy
  data_files:
  - split: train
    path: ar_xy/train.json
- config_name: bn_bd
  data_files:
  - split: train
    path: bn_bd/train.json
- config_name: de_de
  data_files:
  - split: train
    path: de_de/train.json
- config_name: es_la
  data_files:
  - split: train
    path: es_la/train.json
- config_name: fr_fr
  data_files:
  - split: train
    path: fr_fr/train.json
- config_name: hi_in
  data_files:
  - split: train
    path: hi_in/train.json
- config_name: id_id
  data_files:
  - split: train
    path: id_id/train.json
- config_name: it_it
  data_files:
  - split: train
    path: it_it/train.json
- config_name: ja_jp
  data_files:
  - split: train
    path: ja_jp/train.json
- config_name: ko_kr
  data_files:
  - split: train
    path: ko_kr/train.json
- config_name: pt_br
  data_files:
  - split: train
    path: pt_br/train.json
- config_name: sw_ke
  data_files:
  - split: train
    path: sw_ke/train.json
- config_name: yo_ng
  data_files:
  - split: train
    path: yo_ng/train.json
- config_name: zh_cn
  data_files:
  - split: train
    path: zh_cn/train.json
---

# MMMLU Intersection Filtered Dataset

## Dataset Description

This is a high-quality multilingual question-answering dataset derived from [MMMLU](https://huggingface.co/datasets/openai/MMMLU) and [MMLU](https://huggingface.co/datasets/cais/mmlu).

### Key Features

- **15 Languages**: 14 MMMLU languages + English from MMLU
- **Perfect Alignment**: All 15 languages have identical questions with consistent subjects and answers
- **Language Character Filtering**: Each language's choices contain language-specific characters
- **High Quality**: Triple-filtered for maximum quality

### Filtering Process

1. **Subject/Answer Consistency**: Only kept questions where all 15 languages have the same subject and answer
2. **Language Character Filtering**: For non-Latin languages (Arabic, Bengali, Chinese, Hindi, Japanese, Korean), filtered out questions where choices don't contain language-specific characters
3. **Intersection**: Only kept questions that passed filtering in ALL 14 non-Latin languages

### Dataset Size

- **Total Examples**: 11,478 per language
- **Languages**: 15
- **Original MMLU**: 13,497
- **After Filtering**: 11,478 (85.04%)

### Languages

| Language | Code | Examples |
|----------|------|----------|
| Arabic | ar_xy | 11,478 |
| Bengali | bn_bd | 11,478 |
| Chinese | zh_cn | 11,478 |
| English | en | 11,478 |
| French | fr_fr | 11,478 |
| German | de_de | 11,478 |
| Hindi | hi_in | 11,478 |
| Indonesian | id_id | 11,478 |
| Italian | it_it | 11,478 |
| Japanese | ja_jp | 11,478 |
| Korean | ko_kr | 11,478 |
| Portuguese | pt_br | 11,478 |
| Spanish | es_la | 11,478 |
| Swahili | sw_ke | 11,478 |
| Yoruba | yo_ng | 11,478 |

### Data Fields

**For English (MMLU format)**:
- `original_index`: Index in the original MMLU dataset
- `question`: The question text
- `choices`: List of 4 answer choices
- `answer`: Correct answer index (0-3)
- `subject`: Subject category

**For other languages (MMMLU format)**:
- `original_index`: Index in the original MMLU dataset
- `Question`: The question text
- `A`, `B`, `C`, `D`: Four answer choices
- `Answer`: Correct answer (A/B/C/D)
- `Subject`: Subject category

### Usage

```python
from datasets import load_dataset

# Load English version
dataset = load_dataset("willchow66/mmmlu-intersection-filtered", "en")

# Load Chinese version
dataset = load_dataset("willchow66/mmmlu-intersection-filtered", "zh_cn")

# Load all languages
for lang in ["en", "zh_cn", "ko_kr", "ja_jp", "ar_xy", "bn_bd", "hi_in",
             "de_de", "es_la", "fr_fr", "id_id", "it_it", "pt_br", "sw_ke", "yo_ng"]:
    dataset = load_dataset("willchow66/mmmlu-intersection-filtered", lang)
    print(f"{lang}: {len(dataset['train'])} examples")
```

### Example

```python
# English
{
    "original_index": 0,
    "question": "Find the degree for the given field extension Q(sqrt(2), sqrt(3), sqrt(18)) over Q.",
    "choices": ["0", "4", "2", "6"],
    "answer": 1,
    "subject": "abstract_algebra"
}

# Chinese
{
    "original_index": 0,
    "Question": "找出给定域扩张 Q(sqrt(2), sqrt(3), sqrt(18)) 对 Q 的度数。",
    "A": "0",
    "B": "4",
    "C": "2",
    "D": "6",
    "Answer": "B",
    "Subject": "abstract_algebra"
}
```

### Use Cases

- Multilingual language model evaluation
- Cross-lingual bias research
- Multilingual question-answering
- Language-specific performance analysis

### Citation

If you use this dataset, please cite the original MMMLU and MMLU papers:

```bibtex
@article{hendrycks2021measuring,
  title={Measuring Massive Multitask Language Understanding},
  author={Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
  journal={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2021}
}

@article{MMMLU,
  title={MMMLU: Massive Multitask Language Understanding in Multiple Languages},
  author={OpenAI},
  year={2024}
}
```

### License

MIT License (following MMLU and MMMLU)

### Dataset Curators

This filtered and aligned version was created for multilingual LLM bias research.

### Contact

For questions or issues, please open an issue on the dataset repository.
