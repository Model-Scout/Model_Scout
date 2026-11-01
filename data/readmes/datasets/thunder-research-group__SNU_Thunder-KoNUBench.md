---
dataset_info:
  features:
  - name: idx
    dtype: string
  - name: raw_id
    dtype: int64
  - name: original_sentence
    dtype: string
  - name: standard_negation
    dtype: string
  - name: local_negation
    dtype: string
  - name: contradiction
    dtype: string
  - name: paraphrase
    dtype: string
  - name: sn_clause_1
    dtype: string
  - name: sn_clause_2
    dtype: string
  - name: sn_clause_3
    dtype: string
  - name: ln_clause_1
    dtype: string
  - name: ln_clause_2
    dtype: string
  - name: ln_span
    dtype: string
  - name: ln_type
    dtype: string
  splits:
  - name: train
    num_bytes: 2394619
    num_examples: 2500
  - name: validation
    num_bytes: 963899
    num_examples: 1000
  - name: test
    num_bytes: 1218917
    num_examples: 1284
  download_size: 2975026
  dataset_size: 4577435
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
license: cc-by-nc-sa-4.0
task_categories:
- multiple-choice
language:
- ko
pretty_name: Thunder-KoNUBench
size_categories:
- 1K<n<10K
---
# Dataset Card for Thunder-KoNUBench

## Dataset Summary

Thunder-KoNUBench is a sentence-level benchmark for evaluating LLMs' ability to understand negation in Korean. Inspired by [Thunder-NUBench](https://aclanthology.org/2026.findings-eacl.250/), it introduces a wide range of Korean-specific negation markers (e.g., "안", "못", "-지 않-", "-지 못하-", "말다") and is the first benchmark to directly target negation phenomena in Korean. Thunder-KoNUBench is constructed to reflect the empirical distribution of negation observed in a large-scale Korean corpus. A paper describing this benchmark will appear at ACL 2026 (Title: *Thunder-KoNUBench: A Corpus-Aligned Benchmark for Korean Negation Understanding*).

## Supported Task
- Sentence-level negation understanding in Korean (Multiple Choice Question Answering)

## Languages
- Korean (ko)

## Task Definition

Given an original sentence, the model must select the option that corresponds to its correct negation.

The candidate options include:
- standard negation (correct answer)
- local negation
- contradiction
- paraphrase

---
## Dataset Structure

### Data Instance
```json
{
    "idx": "3",
    "raw_id": 372575,
    "original_sentence": "아가메데는 암피트리온과 알크메네 사이에서 태어난 딸이며, 헤라클레스와 이피클레스의 여동생이다.",
    "standard_negation": "아가메데는 암피트리온과 알크메네 사이에서 태어난 딸이 아니거나, 헤라클레스의 여동생이 아니거나, 이피클레스의 여동생이 아니다.",
    "local_negation": "아가메데는 암피트리온과 알크메네 사이에서 태어난 딸이 아니며, 헤라클레스와 이피클레스의 여동생이다.",
    "contradiction": "아가메데는 암피트리온과 알크메네 사이에서 태어난 아들이며, 헤라클레스와 이피클레스의 형이다.",
    "paraphrase": "아가메데는 암피트리온과 알크메네에게서 난 딸로, 헤라클레스와 이피클레스의 여동생이다.",
    "sn_clause_1": "아니다",
    "sn_clause_2": "아니다",
    "sn_clause_3": "아니다",
    "ln_clause_1": "아니다",
    "ln_clause_2": null,
    "ln_type": "대등절 일부",
    "local_span": "태어난 딸이며",
  }
```

### Data Fields

- `idx`: A unique identifier for each instance in the dataset.

- `raw_id`: The identifier of the original source instance from which the example was constructed (e.g., sampled from Korean Wikipedia).

- `original_sentence`: The original sentence serving as the input for the negation task.

- `standard_negation`: The correct negated form of the original sentence, representing the target label.

- `local_negation`: A distractor option where negation is applied only to a part of the sentence, resulting in a partial negation that differs from the standard negation.

- `contradiction`: A distractor option that contradicts the original sentence without explicitly representing its negation.

- `paraphrase`: A distractor option that preserves the meaning of the original sentence while varying its surface form.

- `sn_clause_1`, `sn_clause_2`, `sn_clause_3`: Linguistic annotations indicating the negation markers applied to each clause in the standard negation.

- `ln_clause_1`, `ln_clause_2`: Linguistic annotations indicating the negation markers used in the local negation.

- `ln_span`: The specific span in the sentence where local negation is applied.

- `ln_type`: The type of local negation applied (e.g., partial clause negation).

---
## Data Splits

Thunder-KoNUBench is divided into train, validation, and test splits as follows:

| Split       | Train | Validation | Test  | Total |
|------------|-------|------------|-------|-------|
| Count      | 2,500 | 1,000      | 1,284 | 4,784 |

---
## Dataset Creation

### Data Generation Process

- **Original Sentences**: We crawled Korean Wikipedia and split the text into pairs of sentences using a rule-based sentence splitter. Each pair was then merged into a single well-formed sentence using GPT-4.1 mini.

- **Standard Negation & Local Negation**: These were manually constructed by the authors to ensure linguistic correctness and precise control over negation phenomena.

- **Contradiction & Paraphrase**: These were generated using GPT models and subsequently refined through manual review by the authors.


### Reviewing Process

To ensure data quality, we applied a rigorous multi-stage review process:

- For each instance, an author different from the original creator independently verified its correctness.

- Any disagreements were resolved through discussion during regular group meetings.

---
## License
CC BY-NC-SA 4.0

## Citation

```bibtex
@article{jung2026thunder,
  title={Thunder-KoNUBench: A Corpus-Aligned Benchmark for Korean Negation Understanding},
  author={Jung, Sungmok and So, Yeonkyoung and Lee, Joonhak and Kim, Sangho and Ahn, Yelim and Lee, Jaejin},
  journal={arXiv preprint arXiv:2601.04693},
  year={2026},
 note={To appear in ACL 2026}
}
```

## Contact Information

If you find any issues or have questions about the dataset, please contact <tjdahrwjd@snu.ac.kr>.