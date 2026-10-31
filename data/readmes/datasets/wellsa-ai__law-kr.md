---
pretty_name: wellsa-ai law-kr
language:
  - ko
license: mit
size_categories:
  - 1K<n<10K
task_categories:
  - question-answering
  - text-retrieval
  - text-generation
tags:
  - korean
  - legal
  - public-data
  - rag
  - law
configs:
  - config_name: default
    data_files:
      - split: train
        path: train.jsonl
homepage: https://minilex.wellsa.ai
---

# wellsa-ai law-kr

> 법령 (statutes, presidential decrees, ministerial rules).
> MiniLex 7-domain Korean lawdata infrastructure.

## Snapshot

- **Documents**: 5,589
- **Snapshot date**: 2026-06-05
- **Source**: 법제처 DRF OpenAPI
- **Pipeline**: daily cron `06:15~07:30 KST` (scrape → fetch_body → convert → commit)

## Schema

Each row in `train.jsonl`:

| field | type | description |
| --- | --- | --- |
| `id` | string | stable document id |
| `name` | string | document name (Korean) |
| `category` | string | subdirectory (year / type / dept) |
| `metadata` | object | frontmatter key-value pairs |
| `text` | string | markdown body (메타 + 본문) |

## Usage

```python
from datasets import load_dataset
ds = load_dataset("wellsa-ai/law-kr", split="train")
print(ds[0])
```

## Canonical Source

- **GitHub**: https://github.com/wellsa-ai/law-kr — daily cron, Git history
- **MiniLex demo**: https://minilex.wellsa.ai

## Sibling Datasets (MiniLex 7-domain)

| dataset | description |
| --- | --- |
| [law-kr](https://huggingface.co/datasets/wellsa-ai/law-kr) | 법령 |
| [regulate-kr](https://huggingface.co/datasets/wellsa-ai/regulate-kr) | 행정규칙 |
| [precedent-kr](https://huggingface.co/datasets/wellsa-ai/precedent-kr) | 판례 |
| [interpretation-kr](https://huggingface.co/datasets/wellsa-ai/interpretation-kr) | 법령해석례 |
| [constitution-kr](https://huggingface.co/datasets/wellsa-ai/constitution-kr) | 헌재결정례 |
| [localrule-kr](https://huggingface.co/datasets/wellsa-ai/localrule-kr) | 자치법규 |
| [treaty-kr](https://huggingface.co/datasets/wellsa-ai/treaty-kr) | 조약 |

## License

MIT. 데이터 출처: 한국 법제처 공공 OpenAPI. wellsa-ai 가 수집·정렬·markdown 정규화 layer 제공.

## Disclaimer

Source-grounded retrieval corpus, not a substitute for licensed legal advice.
