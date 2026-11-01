---
language:
- ko
task_categories:
- graph-ml
- text-generation
pretty_name: Traveling Namuwiki
---

# Traveling Namuwiki

Traveling Namuwiki is a graph-navigation dataset built from Namuwiki page links.
Each example contains a start page, a target page, and one or more valid paths
between them. Paths are stored as intermediate page-title lists, excluding the
start and target pages.

This dataset was derived from the Hugging Face dataset
[`heegyu/namuwiki`](https://huggingface.co/datasets/heegyu/namuwiki).

## Files

```text
data/train.jsonl
data/validation.jsonl
data/test.jsonl
```

## Schema

Each JSONL row has this shape:

```json
{
  "start_title": "source page title",
  "target_title": "destination page title",
  "paths": [["intermediate page title", "..."]],
  "hop": n
}
```

`hop` is the minimum number of hops needed to travel from `start_title` to
`target_title`, and `paths` is the set of all shortest paths achieving that
minimum. Each path lists only the intermediate page titles, so
`hop == len(paths[i]) + 1` for every `i`.

For a direct one-hop link, the path is an empty intermediate list:

```json
{
  "start_title": "A",
  "target_title": "B",
  "paths": [[]],
  "hop": 1
}
```

## Splits

The split was made with hop-aware stratification.

| Split | Rows | Approx. ratio | File size |
|---|---:|---:|---:|
| train | 1,795,552 | 90.0% | 1.91 GiB |
| validation | 99,732 | 5.0% | 107.2 MiB |
| test | 99,767 | 5.0% | 107.1 MiB |
| total | 1,995,051 | 100.0% | 2.11 GiB |

## Hop Distribution

| Hop | train | validation | test |
|---:|---:|---:|---:|
| 1 | 295,802 | 16,367 | 16,453 |
| 2 | 405,942 | 22,696 | 22,579 |
| 3 | 679,923 | 37,617 | 37,708 |
| 4 | 367,755 | 20,601 | 20,440 |
| 5 | 43,906 | 2,328 | 2,469 |
| 6 | 2,104 | 117 | 114 |
| 7 | 103 | 5 | 4 |
| 8 | 11 | 1 | 0 |
| 9 | 5 | 0 | 0 |
| 10 | 1 | 0 | 0 |

## Usage

Load directly with `datasets`:

```python
from datasets import load_dataset

data_files = {
    "train": "data/train.jsonl",
    "validation": "data/validation.jsonl",
    "test": "data/test.jsonl",
}

dataset = load_dataset("json", data_files=data_files)
print(dataset["train"][0])
```

or load with Hugging Face Hub:

```python
from datasets import load_dataset

dataset = load_dataset("0601p/Traveling_namuwiki")
```

## Notes

- Page titles come from the source Namuwiki dump and may preserve artifacts from
  the original dump encoding.
- `paths` contains intermediate pages only. Add `start_title` and `target_title`
  around a path if a full route is needed.