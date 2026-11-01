---
license: cc-by-sa-4.0
language:
  - ko
task_categories:
  - multiple-choice
tags:
  - Korean
  - Culture
  - Language
size_categories:
  - 1K<n<10K
configs:
  - config_name: default
    data_files:
      - split: test
        path: test.jsonl
---

# CLIcK (Cultural and Linguistic Intelligence in Korean)

Mirror of the original [CLIcK](https://github.com/rladmstn1714/CLIcK) benchmark (LREC-COLING 2024, [paper](https://arxiv.org/abs/2403.06412)) with the per-item subcategory and broad-category labels preserved.

The upstream HuggingFace mirror at [`EunsuKim/CLIcK`](https://huggingface.co/datasets/EunsuKim/CLIcK) flattens every item into a single split and drops the category metadata that the paper uses. This mirror restores those labels by pulling each per-subcategory JSON file directly from the canonical GitHub repo and tagging each item with its source subcategory.

## Fields

| Field | Type | Description |
| --- | --- | --- |
| `id` | str | Original CLIcK id (e.g. `KIIP_society_1`). Not unique on its own: 8 ids appear in two subcategories with different questions. |
| `paragraph` | str | Optional context paragraph; empty for most items. |
| `question` | str | Question stem. |
| `choices` | list[str] | 4 or 5 answer options. |
| `answer` | str | The literal text of the correct option (one of `choices`). |
| `subcategory` | str | One of 11 fine-grained subcategories (8 Culture + 3 Language). |
| `broad_category` | str | `Culture` or `Language`. |
| `source_file` | str | The original GitHub `.json` file name (e.g. `Society_KIIP.json`). |

## Subcategory distribution

| Subcategory | # items | Broad |
| --- | ---: | --- |
| Korean Society | 309 | Culture |
| Textual | 285 | Language |
| Korean History | 280 | Culture |
| Grammar | 232 | Language |
| Korean Tradition | 222 | Culture |
| Korean Law | 219 | Culture |
| Functional | 133 | Language |
| Korean Geography | 131 | Culture |
| Korean Politics | 84 | Culture |
| Korean Economy | 59 | Culture |
| Korean Popular | 41 | Culture |
| **Total** | **1995** | |

## Citation

```bibtex
@inproceedings{kim-etal-2024-click,
    title = "{CL}{I}c{K}: A Benchmark Dataset of Cultural and Linguistic Intelligence in {K}orean",
    author = "Kim, Eunsu and Suk, Juyoung and Oh, Philhoon and Yoo, Haneul and Thorne, James and Oh, Alice",
    booktitle = "Proceedings of LREC-COLING 2024",
    year = "2024",
    url = "https://arxiv.org/abs/2403.06412",
}
```

All credit for the questions and answers goes to the original authors. This mirror only adds the subcategory labels that already exist in the upstream GitHub repo's directory layout.
