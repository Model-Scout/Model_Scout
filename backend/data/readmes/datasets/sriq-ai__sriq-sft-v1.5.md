---
license: apache-2.0
task_categories:
- text-generation
language:
- multilingual
- en
- zh
tags:
- sft
- sharegpt
- reasoning
- unsloth
- agent
- tool-use
pretty_name: sriq-sft-v1.5
---

# sriq-sft-v1.5

> **Superseded by [sriq-sft-v1.6](https://huggingface.co/datasets/sriq-ai/sriq-sft-v1.6).** Only
> 0.9% of the verification steps in this version ever catch a mistake — the check runs on a trace
> rewritten from reasoning that was already correct, so it has nothing to find. A model trained
> here learns the shape of checking without the function. v1.6 fixes it; see
> [Provenance](#provenance).

ShareGPT-compatible supervised fine-tuning conversations. Questions are generated in many
languages. Assistant targets contain compressed Simplified Chinese reasoning and the
original final answer. The final answer is not rewritten by the compression step.

- `conversations`: a system turn, a human turn, then one GPT turn.
- System turn: `from` is `system`; `value` contains either a short generic preamble or a
  long synthetic coding-harness preamble (see below).
- Human turn: `from` is `human`; `value` contains the question.
- GPT turn: `from` is `gpt`; `value` contains `<think>Chinese reasoning</think>` followed by
  the final answer.
- Extra columns: `topic`, `difficulty`, `language` (the requested question language).

There are no rejected responses in the SFT export.

## What v1.5 adds

v1.5 is v1.4 plus long system prompts that simulate agentic coding harnesses.

Models fine-tuned on v1.3/v1.4 hold Chinese reasoning under a short system prompt, but drift
back to English reasoning once they are put behind a real agent harness — a multi-thousand
token English system prompt full of tool descriptions, skill listings and project context.
The reasoning language is conditioned on the prompt the model actually sees at inference, so
the training data has to contain that prompt shape. v1.5 supplies it: 599 of the 1,424 rows
carry a harness-style preamble, so Chinese reasoning is reinforced in exactly the context
where it otherwise collapses.

| System prompt | Rows |
| --- | ---: |
| `You are a helpful assistant` (carried over from v1.4) | 825 |
| Synthetic coding-harness preamble | 599 |

Harness preambles are 913–15,976 tokens (mean 4,531, median 1,518) and are near-unique: 598
distinct harness names across 599 rows. Each is assembled from

- a persona line naming a fictional harness — *terminal coding agent*, *expert coding
  assistant*, *command line development assistant*, *software engineering assistant*, or
  *autonomous programming agent* — inside a randomly named product;
- a `Guidelines:` block (test after changes, never log secrets, prefer dedicated tools over
  bash, and so on) and a harness documentation file list;
- a `# Skills` listing (all 599 rows) of real-world skill descriptions, themselves
  multilingual, in the format an agent harness injects them; 33 rows also carry a `# Tools`
  section, and 52.8% mention MCP;
- a `# Project Context` block (62.4% of rows) quoting AGENTS.md / README.md /
  CONTRIBUTING.md / ARCHITECTURE.md fragments;
- a trailing environment footer with the current date and working directory (all rows).

The user turn is a normal hard math or coding question, not a tool-call trace — the harness
preamble is distractor context, and the target is that the model keeps reasoning in Chinese
and answering in the question's language despite it. No row contains an executed tool call or
a tool-result turn.

Also inherited from v1.4: reasoning chains close by checking the answer against the original
constraints before the final answer.

## Token statistics

Counts use `tiktoken` `cl100k_base`, not the training model's tokenizer.

| Slice | Total tokens |
| --- | ---: |
| System prompts | 2,718,445 |
| Reasoning | 497,331 |
| Final answer | 1,949,564 |
| Reasoning + final answer, including think tags | 2,454,025 |

Rows: 1424. All rows are `difficulty: hard`; `topic` is math (801) or coding (623).
Mean reasoning length is 438 characters (467 on harness rows, 417 on the generic ones).

Languages (30, evenly present in both the harness and generic slices): Arabic, Bengali,
Czech, Dutch, English, French, German, Greek, Hebrew, Hindi, Indonesian, Italian, Japanese,
Korean, Persian, Polish, Portuguese, Romanian, Russian, Simplified Chinese, Spanish, Swahili,
Swedish, Tamil, Thai, Traditional Chinese, Turkish, Ukrainian, Urdu, Vietnamese.

## Load

```python
from datasets import load_dataset
dataset = load_dataset("sriq-ai/sriq-sft-v1.5", split="train")
conversation = dataset[0]["conversations"]
```

## Format for Qwen3.8 training

The export uses standard ShareGPT fields. Qwen3.8's native template expects
reasoning in a separate field, so convert the record before applying that template:

```python
from transformers import AutoTokenizer

system, question = conversation[0]["value"], conversation[1]["value"]
response = conversation[2]["value"]
reasoning, answer = response.removeprefix("<think>").split("</think>", 1)
messages = [
    {"role": "system", "content": system},
    {"role": "user", "content": question},
    {"role": "assistant", "reasoning_content": reasoning, "content": answer.strip()},
]
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3.8-27B")
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=False,
    preserve_thinking=True,
)
```

For other models, adapt the ShareGPT roles/fields to the trainer's expected
conversation schema while retaining the complete GPT `value`. Do not place the
same reasoning in both `content` and `reasoning_content` for Qwen's template.

For SFT, include the assistant's reasoning and final answer in the loss and mask
system/user/prompt tokens. Check that the rendered training text retains the Chinese
reasoning and that the assistant loss mask covers it. Use the target tokenizer
to check lengths and keep repeated questions in the same train/evaluation split.

The harness rows are long: the longest system prompt alone is ~16k `cl100k_base` tokens. Set
the sequence length to keep those rows whole — truncating the preamble removes the exact
signal v1.5 exists to teach. If you must cap, drop the row rather than truncate it.

Note that the harness rows are **appended at the end** of this dataset, not interleaved. A tail
split holds out almost exactly the rows a context cap would already exclude — shuffle before
splitting.

## Provenance

| | |
| --- | --- |
| **Data revision** | `e7ee870519aa755a1ab285d8dc60f492c4e61824` |
| **Published** | 2026-09-19 16:04 UTC |
| **Built with** | pipeline commit `156fe02` in [`sriq/sriq-sft`](https://git.nixre.dev/git/sriq/sriq-sft) |
| **Previous** | [v1.4](https://huggingface.co/datasets/sriq-ai/sriq-sft-v1.4) |
| **Superseded by** | [v1.6](https://huggingface.co/datasets/sriq-ai/sriq-sft-v1.6) |
| **Trained into** | [sriq-diffusiongemma-26B-A4B-v1.5](https://huggingface.co/sriq-ai/sriq-diffusiongemma-26B-A4B-v1.5) |

The card above may change; the parquet at that revision will not. Pin it when training, so the
corpus is the one that was measured:

```python
load_dataset("sriq-ai/sriq-sft-v1.5", split="train",
             revision="e7ee870519aa755a1ab285d8dc60f492c4e61824")
```

### Release chain

Each version exists to close a defect in the one before it.

| Version | Rows | Data revision | What it introduced | The defect it left behind |
| --- | ---: | --- | --- | --- |
| v1.3 | 2,703 | `84f74b6` | compressed Simplified Chinese reasoning, 30 languages | traces stop at the answer — 15.2% carry a `验` block, 0.3% end on an explicit judgement |
| v1.4 | 825 | `be3a4b6` | a verification step closing the trace (95.4% carry `验`) | Chinese reasoning reverts to English behind a long agent-harness prompt |
| **v1.5** | 1,424 | `e7ee870` | long synthetic harness preambles on 599 of 1,424 rows | the check inherited from v1.4 could only ever agree — 0.9% caught a mistake |
| v1.6 | 9,988 | `fa9e487` | verification that catches a real planted mistake (19.5%), graded difficulty, a `verification` column | — current release |

**What v1.5 left for v1.6 to fix.** Three things, all measured on this corpus:

| Defect here | Fix in v1.6 |
| --- | --- |
| The verification step could only ever confirm — 0.9% of traces caught a mistake. The adapter trained on this reached the right answer on IMO 1990 P3 through a step asserting `p \| p-1`, true for no prime, and stamped it correct. | A share of rows are generated with one step deliberately wrong; the check has to catch, name and repair it. 19.5% of v1.6 rows carry `verification: correct`. |
| Every row is `difficulty: hard`, so a median 349 reasoning tokens go to every question regardless of what it is worth. | Difficulty sampled across easy/medium/hard with a trace-length budget per level — medians 25 / 140 / 254 tokens. |
| Compression was measured over the whole response, so a long final answer could mask an uncompressed trace, and the minimum reduction was a permissive 5%. | The ratio is measured on the trace alone, against a 30% floor, with the target register shown as a worked before/after rather than described. |

Pipeline and the full commit-level trail:
[git.nixre.dev/git/sriq/sriq-sft](https://git.nixre.dev/git/sriq/sriq-sft).
