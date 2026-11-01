---
language:
  - de
  - en
  - es
  - fr
  - it
  - ja
  - ko
  - nl
  - pl
  - pt
  - zh
license: apache-2.0
task_categories:
  - text-retrieval
  - sentence-similarity
tags:
  - job-titles
  - similarity
  - multilingual
  - ranking
  - information-retrieval
configs:
- config_name: de
  data_files:
  - split: queries
    path: "de/queries-00000-of-00001.parquet"
  - split: corpus
    path: "de/corpus-00000-of-00001.parquet"
- config_name: en
  data_files:
  - split: queries
    path: "en/queries-00000-of-00001.parquet"
  - split: corpus
    path: "en/corpus-00000-of-00001.parquet"
- config_name: es
  data_files:
  - split: queries
    path: "es/queries-00000-of-00001.parquet"
  - split: corpus
    path: "es/corpus-00000-of-00001.parquet"
- config_name: fr
  data_files:
  - split: queries
    path: "fr/queries-00000-of-00001.parquet"
  - split: corpus
    path: "fr/corpus-00000-of-00001.parquet"
- config_name: it
  data_files:
  - split: queries
    path: "it/queries-00000-of-00001.parquet"
  - split: corpus
    path: "it/corpus-00000-of-00001.parquet"
- config_name: ja
  data_files:
  - split: queries
    path: "ja/queries-00000-of-00001.parquet"
  - split: corpus
    path: "ja/corpus-00000-of-00001.parquet"
- config_name: ko
  data_files:
  - split: queries
    path: "ko/queries-00000-of-00001.parquet"
  - split: corpus
    path: "ko/corpus-00000-of-00001.parquet"
- config_name: nl
  data_files:
  - split: queries
    path: "nl/queries-00000-of-00001.parquet"
  - split: corpus
    path: "nl/corpus-00000-of-00001.parquet"
- config_name: pl
  data_files:
  - split: queries
    path: "pl/queries-00000-of-00001.parquet"
  - split: corpus
    path: "pl/corpus-00000-of-00001.parquet"
- config_name: pt
  data_files:
  - split: queries
    path: "pt/queries-00000-of-00001.parquet"
  - split: corpus
    path: "pt/corpus-00000-of-00001.parquet"
- config_name: zh
  data_files:
  - split: queries
    path: "zh/queries-00000-of-00001.parquet"
  - split: corpus
    path: "zh/corpus-00000-of-00001.parquet"
---

# Job Title Similarity Benchmark

This dataset contains the **Job Title Similarity** benchmark for easy loading with
the HuggingFace `datasets` library.

## Dataset Description

This benchmark provides **job title similarity** datasets in **11** different languages,
including the English evaluation dataset used in the text ranking experiments reported
in the paper _"Learning Job Titles Similarity from Noisy Skill Labels"_ by Zbib et al. (2022),
as well as the translated datasets for the other languages introduced in _"Combined
Unsupervised and Contrastive Learning for Multilingual Job Recommendations"_ by Deniz et al. (2024).

### Task Overview

The task involves ranking a set of job titles, given another job title as query, such that
the resulting ranking reflects the semantic similarity of each job title to the query. This
requires identifying the most relevant job titles based on their semantic similarity to a
given query.

### English Dataset Creation

The English dataset was built by starting with 2,724 job titles (short text phrases with
the name of an occupation). Next, a minimal pre-processing step with light clean up was
applied. The job titles were randomly divided into two groups:
- 105 job titles were used as queries
- The remaining job titles were used as corpus documents

Each query/document pair was labeled for binary relevance after adjudicating two independent
human annotations. (The inter-annotator agreement for this binary relevance labels was 86%.)

### Translated Datasets

The translated datasets in 10 additional languages replicate the English dataset using
Human Translation (HT) or Machine Translation (MT).

**Original repository:** [https://github.com/Avature/job-title-similarity](https://github.com/Avature/job-title-similarity)

## Dataset Structure

Each subset (configuration) contains two splits:

- **`queries`**: Query job titles with their relevant corpus element indices
- **`corpus`**: Corpus job titles

### Schema

**queries split:**
| Column | Type | Description |
|--------|------|-------------|
| `text` | `string` | The query job title |
| `labels` | `list[int]` | Indices of relevant corpus job titles |

**corpus split:**
| Column | Type | Description |
|--------|------|-------------|
| `text` | `string` | The corpus job title |

## Usage

```python
from datasets import load_dataset

# Load a specific subset
ds = load_dataset("Avature/Job-Title-Similarity", "en")

# Access the data
query_surface_forms = ds["queries"]["text"]
corpus_surface_forms = ds["corpus"]["text"]
label_lists = ds["queries"]["labels"]

# Example: Get relevant corpus texts for the first query
query_idx = 0
print(f"Query: {query_surface_forms[query_idx]}")
print(f"Similar job titles:")
for corpus_idx in label_lists[query_idx]:
    print(f"  - {corpus_surface_forms[corpus_idx]}")
```

## Available Subsets

| Subset | Language | Translation | Queries | Corpus | Annotations |
|--------|----------|-------------|---------|--------|-------------|
| `en` | English | - | 105 | 2,619 | 2,420 |
| `de` | German | HT | 104 | 2,529 | 2,342 |
| `es` | Spanish | MT | 104 | 2,568 | 2,378 |
| `fr` | French | HT | 104 | 2,488 | 2,299 |
| `it` | Italian | MT | 104 | 2,528 | 2,344 |
| `ja` | Japanese | HT | 104 | 2,553 | 2,352 |
| `ko` | Korean | MT | 104 | 2,542 | 2,345 |
| `nl` | Dutch | MT | 105 | 2,538 | 2,361 |
| `pl` | Polish | MT | 105 | 2,513 | 2,335 |
| `pt` | Portuguese | MT | 104 | 2,523 | 2,331 |
| `zh` | Chinese | HT | 103 | 2,513 | 2,319 |

**Translation key:** HT = Human Translation, MT = Machine Translation

## Citation

If you use this dataset, please cite the original papers:

```bibtex
@article{zbib2022Learning,
      title={{Learning Job Titles Similarity from Noisy Skill Labels}},
      author={Rabih Zbib and
              Lucas Alvarez Lacasa and
              Federico Retyk and
              Rus Poves and
              Juan Aizpuru and
              Hermenegildo Fabregat and
              Vaidotas Šimkus and
              Emilia García-Casademont},
      journal={{FEAST, ECML-PKDD 2022 Workshop}},
      year={{2022}},
      url="https://feast-ecmlpkdd.github.io/archive/2022/papers/FEAST2022_paper_4972.pdf"
}
@inproceedings{deniz2024Combined,
  title        = {Combined Unsupervised and Contrastive Learning for Multilingual Job Recommendations},
  author       = {Daniel Deniz and
                  Federico Retyk and
                  Laura García-Sardiña and
                  Hermenegildo Fabregat and
                  Luis Gasco and
                  Rabih Zbib},
  booktitle    = {Proceedings of the 4th Workshop on Recommender Systems for Human Resources
                  (RecSys in {HR} 2024), in conjunction with the 18th {ACM} Conference on
                  Recommender Systems},
  year         = {2024},
}
```

## License

This dataset is licensed under the Apache 2.0 License. See the
[LICENSE](https://github.com/Avature/jobtitlesimilarity-dataset/blob/main/LICENSE) file for more information.
