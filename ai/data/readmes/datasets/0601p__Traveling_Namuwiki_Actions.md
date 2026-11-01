---
language:
- ko
task_categories:
- graph-ml
- text-generation
pretty_name: Traveling Namuwiki Actions
---

# Traveling Namuwiki Actions

Traveling Namuwiki Actions is an adjacency-list dataset built from Namuwiki page
links. Each row contains a page title and the list of linked page titles that can
be used as next actions in a graph-navigation task.

This dataset was derived from the Hugging Face dataset
[`heegyu/namuwiki`](https://huggingface.co/datasets/heegyu/namuwiki).

## Files

```text
data.jsonl
```

File size: about 405.1 MiB.

## Schema

Each JSONL row has this shape:

```json
{
  "title": "source page title",
  "actions": ["linked page title", "..."]
}
```

`actions` is sorted and deduplicated within each row. Pages with no extracted
outgoing actions were removed from this dataset. Therefore, if a Namuwiki page
title does not appear as a `title` row here, it should be treated as having no
available outgoing actions in this action graph.

## Statistics

| Metric | Value |
|---|---:|
| Rows / source pages | 562,217 |
| Total actions / links | 20,715,178 |
| Average actions per page | 36.85 |
| Minimum actions per page | 1 |
| Maximum actions per page | 11,231 |

### Actions Per Page

| Actions count | Rows |
|---:|---:|
| 1 | 10,784 |
| 2 | 12,642 |
| 3 | 15,188 |
| 4 | 16,385 |
| 5 | 17,911 |
| 6 | 18,202 |
| 7 | 18,268 |
| 8 | 18,571 |
| 9 | 18,611 |
| 10 | 17,890 |
| 11 | 17,149 |
| 12 | 16,094 |
| 13 | 15,329 |
| 14 | 14,537 |
| 15 | 13,686 |
| 16 | 12,954 |
| 17 | 12,171 |
| 18 | 11,436 |
| 19 | 10,918 |
| 20 | 10,189 |
| 21+ | 263,302 |

## Usage

Load the JSONL file directly:

```python
import json

with open("data.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        row = json.loads(line)
        title = row["title"]
        actions = row["actions"]
        break
```

Load with `datasets`:

```python
from datasets import load_dataset

dataset = load_dataset("json", data_files="data.jsonl", split="train")
print(dataset[0])
```

or load with Hugging Face Hub:

```python
from datasets import load_dataset

dataset = load_dataset("YOUR_USERNAME/Traveling_Namuwiki_Actions", split="train")
```

Build an in-memory graph:

```python
graph = {row["title"]: row["actions"] for row in dataset}
```

## Notes

- This dataset stores page-title links only, not full article text.
- Links to files, categories, images, external URLs, and self-links were removed
  during preprocessing.
- Pages with no extracted outgoing links were removed. When traversing this
  graph, a title that is not present as a source `title` row should be handled as
  a terminal page with no outgoing actions.
- Some linked page titles may not appear as source `title` rows due to redirects
  or missing pages; these should also be handled as terminal pages in this graph.
