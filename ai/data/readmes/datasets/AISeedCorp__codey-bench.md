---
pretty_name: codey-bench
license: cc-by-nc-4.0
language:
  - ko
  - en
task_categories:
  - text-generation
tags:
  - structured-output
  - json
  - web-design
size_categories:
  - n<1K
configs:
  - config_name: ko
    default: true
    data_files:
      - split: test
        path: data/ko/test.jsonl
  - config_name: en
    data_files:
      - split: test
        path: data/en/test.jsonl
  - config_name: ko-synth
    data_files:
      - split: test
        path: data/ko-synth/test.jsonl
---

# codey-bench

Each row is a product brief for a web page (Markdown). The model receives the brief and must
produce one **Codey Design Document (CDD)** as JSON, the page's structured design: sections,
blocks and theme. A reference document is included for each brief.

`system_prompt.txt` is the system message for every row. It states the task and the CDD
format, and ends with "Answer with one JSON object and nothing else."

## Subsets

| subset | rows | language | briefs and references |
|---|---|---|---|
| `ko` (default) | 20 | Korean | written by product planners |
| `en` | 99 | English | synthesized with gpt-4.1 |
| `ko-synth` | 98 | Korean | Korean versions of `en`, same `id`s |

## Fields

| field | description |
|---|---|
| `id` | document id; `en` and `ko-synth` share ids |
| `lang` | `ko` or `en` |
| `domain` | business domain, e.g. `hair-salon`, `agency` |
| `brief` | the Markdown brief, used as the user message |
| `reference` | the reference CDD as a JSON string |
| `gold_schema_valid` | the reference conforms to the CDD schema (always `true`) |
| `gold_gate_errors` | number of rendering-rule violations in the reference; 0 for every `ko` row. Synthesized references keep asset metadata keys and section links that the renderer rejects |

## Usage

```python
from datasets import load_dataset
from huggingface_hub import hf_hub_download

ds = load_dataset("AISeedCorp/codey-bench", "ko", split="test")
system = open(hf_hub_download("AISeedCorp/codey-bench", "system_prompt.txt", repo_type="dataset")).read()

messages = [{"role": "system", "content": system},
            {"role": "user", "content": ds[0]["brief"]}]
```

## License

CC BY-NC 4.0.
