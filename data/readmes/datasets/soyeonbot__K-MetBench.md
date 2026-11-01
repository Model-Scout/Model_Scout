---
pretty_name: K-MetBench
language:
- ko
license: cc-by-nc-sa-4.0
task_categories:
- question-answering
task_ids:
- multiple-choice-qa
size_categories:
- 1K<n<10K
tags:
- meteorology
- korean
- multimodal
- reasoning
configs:
- config_name: default
  data_files:
  - split: test
    path: data/kmetbench.json
---

# K-MetBench: A Multi-Dimensional Benchmark for Fine-Grained Evaluation of Expert Reasoning, Locality, and Multimodality in Meteorology

[![Paper](https://img.shields.io/badge/Paper-ACL%20Findings%202026-B31B1B.svg?style=for-the-badge)](http://arxiv.org/abs/2604.24645) [![Learderboard](https://img.shields.io/badge/Leaderboard-GitHub-FFD21E.svg?style=for-the-badge)](https://kmetbench.github.io) [![Code](https://img.shields.io/badge/Code-GitHub-181717.svg?style=for-the-badge)](https://github.com/kmetbench/kmetbench-release) [![Citation](https://img.shields.io/badge/Citation-BibTeX-34A853.svg?style=for-the-badge)](#citation)

K-MetBench is a multi-dimensional benchmark for evaluating meteorology models across
accuracy, reasoning quality, geo-cultural alignment, and fine-grained domain coverage.

The public eval protocol uses only the explicit advanced benchmark and the explicit reasoning benchmark followed by LLM-as-a-judge evaluation.
The implicit split may be distributed with the dataset, but it is not part of the public eval kit.

## Dataset Summary

- Total Questions: 1774
- Total Image References: 151 (59 question images, 92 choice images)
- Modality Split: text-only 1692, multimodal 82
- Reasoning Subset: 141
- Geo-Cultural Subset: 73
- Parts: Part 1: 373, Part 2: 332, Part 3: 359, Part 4: 376, Part 5: 334
- Format: JSON file with relative image paths under `data/images/`

## Data Format

Each sample contains:

| Field | Type | Description |
| --- | --- | --- |
| `id` | int | Stable item identifier |
| `question.text` | string | Question text |
| `question.image` | string | Relative path to a question image, if present |
| `choices[].text` | string | Choice text |
| `choices[].image` | string | Relative path to a choice image, if present |
| `answer` | int | Zero-based correct choice index |
| `source` | string | Exam session source tag |
| `source_id` | int | Original source-local item id |
| `rationale` | string | Expert-verified reasoning text when available |
| `korean` | bool | Geo-cultural subset flag |
| `multimodal` | bool | Multimodal subset flag |
| `part` | int | Official part number (1-5) |
| `category` | object | Subject/topic metadata |

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

dataset = load_dataset(
    "json",
    data_files="https://huggingface.co/datasets/soyeonbot/K-MetBench/resolve/main/data/kmetbench.json",
    split="test",
)

sample = dataset[0]
print(sample["question"]["text"])
print(sample["answer"])
```

### Viewing Referenced Images

```python
import requests
from io import BytesIO
from PIL import Image

image_rel_path = sample["question"]["image"]
image_url = "https://huggingface.co/datasets/soyeonbot/K-MetBench/resolve/main/data/images/" + image_rel_path
image = Image.open(BytesIO(requests.get(image_url, timeout=30).content))
image.show()
```

### Running the Public Eval Kit

```bash
pip install -r requirements-eval.txt
python scripts/eval.py run --list-model-configs
python scripts/eval.py run --model-config <model_config> --prompt-type advanced --explicit-data-file data/kmetbench.json --image-root data/images
python scripts/eval.py run --model-config <model_config> --prompt-type reasoning --explicit-data-file data/kmetbench.json --image-root data/images
python scripts/eval.py judge --model <model> --predictions <explicit_reasoning_json> --explicit-data-file data/kmetbench.json
```

## License

This dataset is released under CC BY-NC-SA 4.0.

## Contact

For questions about the dataset, contact Soyeon Kim (soyeon.k@kaist.ac.kr).

## Citation

```bibtex
@inproceedings{kim2026kmetbench,
  title = {K-MetBench: A Multi-Dimensional Benchmark for Fine-Grained Evaluation of Expert Reasoning, Locality, and Multimodality in Meteorology},
  author = {Kim, Soyeon and Kang, Cheongwoong and Lee, Myeongjin and Chang, Eun-Chul and Lee, Jaedeok and Choi, Jaesik},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2026},
  year = {2026},
  url = {http://arxiv.org/abs/2604.24645}
}
```
