---
license: other
license_name: mixed-source-licenses
language:
- en
- ar
- de
- es
- fr
- hi
- id
- it
- ja
- ko
- nl
- pl
- pt
- ru
- sv
- th
- tr
- vi
- zh
task_categories:
- text-classification
annotations_creators:
- machine-generated
pretty_name: Respan Behavior Benchmark
size_categories:
- 10K<n<100K
tags:
- evaluation
- llm
- agents
- behavior-classification
- observability
configs:
- config_name: default
  default: true
  data_files:
  - split: core
    path: core.parquet
  - split: multilingual
    path: multilingual.parquet
---

<p align="center">
  <img class="dark:hidden" src="respan-wordmark-black.png" alt="Respan" width="176">
  <img class="hidden dark:block" src="respan-wordmark-white.png" alt="Respan" width="176">
</p>

<h1 align="center">Behavior Benchmark</h1>

<p align="center">
  Does this LLM trace show this behavior? A multilingual benchmark on real chat and agent traces.<br>
  <sub>1,990 traces · 34,885 trace–behavior pairs · 19 languages · v1.0.0</sub>
</p>

---

Each row pairs a trace (one LLM call: its input messages, output, and call
metadata) with a behavior written in plain language. A system predicts one of:

- `present`: the trace shows the behavior;
- `absent`: the trace shows it did not happen;
- `not_observable`: the trace doesn't contain enough to decide.

Behaviors cover agentic process, tool use, style, user and assistant
semantics, quantitative metadata (latency, tokens, cost), relational
properties, grounding, and language.

## Quick start

```python
from datasets import load_dataset

ds = load_dataset("respanai/behavior-benchmark")   # splits: core, multilingual

ex = ds["core"][0]
ex["input"], ex["output"], ex["metadata"]    # the trace, in OpenAI chat format
ex["behavior_definition"], ex["label"]       # the question and its answer
```

| split | traces | rows | contents |
|---|---:|---:|---|
| `core` | 1,475 | 26,495 | English chat, tool-use, search, and coding-agent traces |
| `multilingual` | 515 | 8,390 | Traces in 18 additional languages, plus English controls |

Labels: `absent` 87.6%, `present` 10.4%, `not_observable` 2.0%.

## Fields

| field | description |
|---|---|
| `cell_id` | Unique row ID |
| `task_id`, `span_id` | Trace ID (shared by all rows on the same trace) |
| `suite` | `core` or `multilingual` (same as the split) |
| `source`, `source_dataset`, `source_license` | Upstream dataset and its license |
| `input` | Messages sent to the model: `role`, `content`, `tool_calls` (`id`, `name`, JSON `arguments`), `tool_call_id`, `name` |
| `output` | The model's reply, same shape as a message |
| `metadata` | `model`, `finish_reason`, `status`, `latency_ms`, `time_to_first_token_ms`, `prompt_tokens`, `completion_tokens`, `cost_usd`, `temperature`, `top_p`, `seed`, `stream`, `tools_defined` (null when unknown) |
| `language` | Language code of the trace |
| `def_id`, `behavior_type`, `behavior_definition` | Behavior ID, family, and text |
| `label` | `present`, `absent`, or `not_observable` |

## Labels

Labels come from three methods.

| method | `core` | `multilingual` |
|---|---:|---:|
| Teachers: `gpt-5.6-sol` and `claude-opus-5` agree | 24,074 | 5,541 ¹ |
| Tie-break: the teachers disagreed and `gpt-6-astra` decided | 2,421 | ¹ |
| Construction: set by how the trace was built | — | 2,851 |

¹ The multilingual count covers both teacher rows and tie-breaks. Rows with no
majority were dropped. Construction labels cover language behaviors, and
language-conditioned behaviors whose language condition is false.

These are model labels, not ground truth. `gpt-5.6-sol`, `claude-opus-5`,
`gpt-6-astra` and `claude-opus-5.5` helped make the labels, so they can't be
fairly evaluated on this benchmark.

## Evaluation

Report F1 on `present` for `core` and `multilingual` separately, plus pooled.
For confidence intervals, bootstrap over `task_id` rather than rows. State the
model version, prompt, and any decision thresholds used.

## Limitations

- Teachers saw a length-limited rendering of each trace, so a few
  `not_observable` labels may be decidable from the full trace.
- No negated or omission-style behaviors.
- Models from the same family as a teacher may have an advantage.

## Sensitive content and license

Traces come from public datasets and may contain personal data, fake
credentials, or expired signed URLs from the originals. We scanned for them
([`release_stats.json`](release_stats.json)), but a scan can't catch
everything. Don't use the data to identify people, and don't try to use any
credential-like string.

Each row keeps its upstream license in `source_license`; see [LICENSE](LICENSE).

## Citation

```bibtex
@misc{respan_behavior_benchmark_2026,
  title        = {Respan Behavior Benchmark},
  author       = {Respan},
  year         = {2026},
  howpublished = {Hugging Face dataset},
  url          = {https://huggingface.co/datasets/respanai/behavior-benchmark}
}
```
