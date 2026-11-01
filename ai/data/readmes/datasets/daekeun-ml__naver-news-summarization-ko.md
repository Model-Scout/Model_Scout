---
license: apache-2.0
task_categories:
- summarization
language:
- ko
size_categories:
- 10K<n<100K
pretty_name: Naver-News-KO
tags:
- korean
- news
- abstractive-summarization
---

# Naver-News-KO: A Korean News Summarization Dataset

A Korean news summarization dataset of **27,400 (document, summary) pairs**, crawled from
[Naver News](https://news.naver.com) over a ten-day window in July 2022. It was originally built for a
Korean NLP hands-on lab and has been publicly hosted on the Hugging Face Hub since January 2023.

A technical report documenting the collection protocol, corpus statistics, contamination analysis, and
reproducible baselines is available on arXiv: **[arXiv:2607.20442](https://arxiv.org/abs/2607.20442)**.
Please cite it if you use this dataset ([Citation](#citation)).

## Dataset Details

| | |
|---|---|
| Collection period | July 1–10, 2022 |
| Source | Naver News (news.naver.com) |
| Categories | Economy, IT/Science (77 / 23 split) |
| Language | Korean (ko) |
| Total records | 27,400 |
| Mean compression ratio | 6.03× (document→summary, characters, per-record mean) |
| License | Apache-2.0 |

### Splits

```
DatasetDict({
    train: Dataset({
        features: ['date', 'category', 'press', 'title', 'document', 'link', 'summary'],
        num_rows: 22194
    })
    test: Dataset({
        features: ['date', 'category', 'press', 'title', 'document', 'link', 'summary'],
        num_rows: 2740
    })
    validation: Dataset({
        features: ['date', 'category', 'press', 'title', 'document', 'link', 'summary'],
        num_rows: 2466
    })
})
```

### Fields

| Field | Type | Description |
|---|---|---|
| `date` | string | Publication date of the article |
| `category` | string | News category (Economy, IT/Science) |
| `press` | string | Publisher / press outlet |
| `title` | string | Article headline |
| `document` | string | Article body — the summarization **input** |
| `link` | string | Original article URL |
| `summary` | string | Reference summary — the summarization **target** |

## Usage

```python
from datasets import load_dataset

ds = load_dataset("daekeun-ml/naver-news-summarization-ko")
print(ds["train"][0]["document"])
print(ds["train"][0]["summary"])
```

## Baselines

Reported in the technical report ([arXiv:2607.20442](https://arxiv.org/abs/2607.20442)) on the `test` split.
These are reference points for reproducibility, not tuned state-of-the-art numbers.

| Model | ROUGE-1 | ROUGE-L | BERTScore-F1 |
|---|---|---|---|
| Lead-3 (extractive) | 55.1 | 50.6 | — |
| KoBART (fine-tuned) | 56.6 | — | 81.5 |
| Gemma-2B-ko + LoRA | 55.3 | — | 78.3 |

## Limitations and Known Issues

Please read these before using the dataset for evaluation.

- **Test–train overlap.** A measured **16.8% near-duplicate title-Jaccard overlap** exists between the
  `test` and `train` splits. Splits were assigned randomly at collection time without de-duplication,
  and Korean news wire content is frequently syndicated across outlets. Absolute scores on this `test`
  split are therefore optimistic. For a stricter evaluation, filter test items by title similarity
  against train first.
- **Narrow time window and domain.** Ten days in July 2022, two categories only. Vocabulary, entities,
  and topics are tied to that window; it does not represent Korean news in general.
- **Reference summary provenance.** Summaries come from the source pages as crawled, not from a
  controlled annotation protocol with inter-annotator agreement. Style and length are inconsistent
  across publishers.
- **Not a benchmark.** This resource exists to give downstream work that already uses it something
  citable. It was not designed as a leaderboard benchmark.

## Licensing and Intended Use

The dataset compilation is released under **Apache-2.0**. Copyright in the underlying articles remains
with the original publishers; the `link` field is retained so every record can be traced to its source.
Intended use is research and educational hands-on work (summarization fine-tuning, tutorials, labs).
Verify your own compliance before any commercial redistribution of the article text.

## Citation

```bibtex
@misc{kim2026navernews,
  title         = {{Naver-News-KO}: A {Korean} News Summarization Dataset for Open-Source Fine-Tuning of Summarization Models},
  author        = {Daekeun Kim},
  year          = {2026},
  eprint        = {2607.20442},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2607.20442}
}
```

## Links

- 📄 Technical report: https://arxiv.org/abs/2607.20442
- 🤗 Dataset: https://huggingface.co/datasets/daekeun-ml/naver-news-summarization-ko