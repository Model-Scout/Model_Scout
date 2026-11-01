---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: document
    dtype: string
  - name: source
    dtype: string
  - name: language
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: response_Qwen3-Next-80B-A3B
    dtype: string
  - name: response_Qwen3.5-27B
    dtype: string
  - name: response_Nemotron-3-Nano-30B-A3B
    dtype: string
  splits:
  - name: train
    num_bytes: 18425593509
    num_examples: 193219
  download_size: 9567388592
  dataset_size: 18425593509
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-sa-4.0
task_categories:
- text-generation
- text-retrieval
- question-answering
language:
- en
- de
- fr
- es
- uk
- sv
- ro
- it
- ru
- el
- ja
- nl
- fi
- pl
- hu
- zh
- pt
- hi
- ar
- ca
- mt
- tr
- ko
- hr
- sk
- lt
- ga
- 'no'
- sl
- gl
- da
size_categories:
- 100K<n<1M
pretty_name: LongBlocks
---

# LongBlocks

**LongBlocks** is a multilingual synthetic dataset for training long-context language models. It contains **193,219 long-context question–answer examples** generated from long documents spanning books, web text, Wikipedia, arXiv papers, programming/code data, and community Q&A.

The dataset was created to support long-context adaptation for tasks that require reasoning over extended inputs, including:

- multi-hop reasoning over long documents,
- contextual grounding,
- long-form question answering,
- information synthesis,
- document-level understanding,
- code and technical reasoning over long contexts.

## Dataset Summary

Each example consists of a long source document, a synthetic question, a reference answer, and optional model-generated responses from several teacher models.

The dataset covers 31 natural languages and 15 programming and markup languages. It is designed for post-training long-context LLMs using supervised fine-tuning, distillation, or reinforcement learning.

### Sources

LongBlocks combines examples derived from several long-document corpora:

| Source | Description | Samples |
|---|---|---:|
| `Institutional-Books-1.0` | Long-form books from institutional library collections | 107,817 |
| `FineWeb2-HQ` | High-quality multilingual web documents | 39,083 |
| `PGBooks` | Project Gutenberg books | 10,987 |
| `ArXiv` | Scientific papers | 13,963 |
| `Wikipedia` | Encyclopedia-style articles | 10,527 |
| `Stack-Edu` | Educational code, programming, and markup content | 5,859 |
| `StackExchange` | Community question-answering content | 4,983 |
| **Total** | | **193,219** |

> **Important:** Documents from `Institutional-Books-1.0` are **not redistributed** in this dataset due to licensing restrictions. See [Reconstructing the Full Dataset](#reconstructing-the-full-dataset) for instructions on how to locally restore these documents.

## Dataset Structure

The dataset contains one split:

| Split | Rows |
|---|---:|
| `train` | 193,219 |

### Columns

| Column | Type | Description |
|---|---|---|
| `id` | `string` | Unique example or document identifier. This is only needed to reconstruct the Institutional Books examples; it is `null` for examples from all other data sources. |
| `document` | `string` | Long source document. This is `null` for restricted Institutional Books examples. |
| `source` | `string` | Source corpus. |
| `language` | `string` | Natural, programming, or markup language of the example. |
| `question` | `string` | Synthetic long-context question. |
| `answer` | `string` | Reference answer generated and filtered for groundedness. |
| `response_Qwen3-Next-80B-A3B` | `string` | Model response from Qwen3-Next-80B-A3B. |
| `response_Qwen3.5-27B` | `string` | Model response from Qwen3.5-27B. |
| `response_Nemotron-3-Nano-30B-A3B` | `string` | Model response from Nemotron-3-Nano-30B-A3B. |

## Loading the Dataset

```python
from datasets import load_dataset

dataset = load_dataset("utter-project/LongBlocks", split="train")
print(dataset)
```

For memory-constrained environments, use streaming:

```python
from datasets import load_dataset

dataset = load_dataset("utter-project/LongBlocks", split="train", streaming=True)

for example in dataset:
    print(example["source"], example["language"])
    print(example["question"])
    break
```

## Reconstructing the Full Dataset

```python
from collections import defaultdict
import os

from datasets import Dataset, concatenate_datasets, load_dataset

NUM_PROC = min(
    os.cpu_count() or 1,
    int(os.getenv("SLURM_CPUS_PER_TASK") or os.getenv("SLURM_CPUS_ON_NODE") or os.cpu_count() or 1),
)

SOURCE = "Institutional-Books-1.0"
COLUMNS = ["barcode_src", "text_by_page_src", "text_by_page_gen", "ocr_score_src", "ocr_score_gen"]

longblocks = load_dataset("utter-project/LongBlocks", split="train", num_proc=NUM_PROC)
ib = longblocks.filter(lambda x: x["source"] == SOURCE, num_proc=NUM_PROC)
others = longblocks.filter(lambda x: x["source"] != SOURCE, num_proc=NUM_PROC)

rows_by_id = defaultdict(list)
for row in ib:
    rows_by_id[row["id"]].append(row)

def examples(worker_ids):
    books = load_dataset(
        "institutional/institutional-books-1.0",
        split="train",
        streaming=True,
    ).select_columns(COLUMNS)

    for worker_id in worker_ids:
        for book in books.shard(num_shards=NUM_PROC, index=worker_id):
            rows = rows_by_id.get(book["barcode_src"])
            if not rows:
                continue

            pages = book["text_by_page_src"] if book["ocr_score_src"] >= book["ocr_score_gen"] else book["text_by_page_gen"]
            document = "".join(pages).strip()

            for row in rows:
                yield {**row, "document": document}

ib = Dataset.from_generator(
    examples,
    gen_kwargs={"worker_ids": list(range(NUM_PROC))},
    num_proc=NUM_PROC,
)  # Should generate 107817 rows

longblocks = concatenate_datasets([ib, others]).shuffle(seed=42)
print(longblocks)
# Dataset({
#    features: ['id', 'document', 'source', 'language', 'question', 'answer', 'response_Qwen3-Next-80B-A3B', 'response_Qwen3.5-27B', 'response_Nemotron-3-Nano-30B-A3B'],
#    num_rows: 193219
# })
```

## Intended Uses

LongBlocks is intended for research on long-context language modeling, including:

- supervised fine-tuning,
- (sequence-level) knowledge distillation,
- long-context reinforcement learning,
- long-context retrieval and reasoning,
- synthetic data filtering and verification research.

## Out-of-Scope Uses

LongBlocks should not be used as a source of factual truth without additional verification. The questions, answers, and model responses are synthetic and may contain errors. Users should validate examples before using them in high-stakes applications.

## Limitations and Risks

LongBlocks is synthetically generated and LLM-filtered and may inherit artifacts or biases from its source corpora, generator, and verifier. Generation and filtering may systematically favor particular examples, reasoning patterns, or answer styles aligned with the models used in the pipeline. Multilingual coverage does not imply uniform quality across languages, especially for lower-resource languages.

Although the dataset undergoes cleaning, deduplication, benchmark-overlap filtering, and LLM-based verification, these procedures cannot eliminate all errors, biases, offensive content, or personally identifying information.

## Licensing

LongBlocks is released under **CC BY-SA 4.0**.

Some underlying source corpora may be subject to additional restrictions. In particular, documents from `Institutional-Books-1.0` are not redistributed as part of this dataset. Users who reconstruct the full dataset locally are responsible for complying with the terms of all underlying data sources, including the original Institutional Books dataset.

## Citation

If you use LongBlocks, please cite the associated paper:

```bibtex
@misc{ramos2026recipelongcontextreasoninglarge,
      title={A Recipe for Long-Context Reasoning in Large Language Models via On-Policy Optimization and Distillation},
      author={Miguel Moura Ramos and Duarte M. Alves and André F. T. Martins},
      year={2026},
      eprint={2605.12227},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.12227},
}
```