---
license: cc-by-4.0
task_categories:
  - text-generation
language:
  - ko
  - en
tags:
  - agent
  - tool-use
  - long-context
  - recall
  - memory
  - function-calling
  - synthetic
size_categories:
  - 100K<n<1M
configs:
  - config_name: appworld
    data_files: "data/appworld/*.jsonl"
  - config_name: nemotron-ko
    data_files: "data/nemotron_ko/*.jsonl"
  - config_name: nemotron-en
    data_files: "data/nemotron_en/*.jsonl"
---

# agentic-recall-v1

**112,740 multi-turn agentic trajectories augmented with a "recall" turn** — late in the conversation
the user asks the assistant to recall a fact or action established much earlier, and the assistant
answers **from memory, with no new tool call**. Built to strengthen long-context recall (the failure mode
that shows up after context compaction).

Every row is an existing trajectory with **one recall exchange added** (user question + assistant reply),
appended at the end or inserted mid-conversation. The recalled fact is always **rule-verified**, so the
dataset never teaches an incorrect recall. The original rows are preserved; these are separate `-recall`
rows and are meant to be **mixed with the base corpora** during training, not used alone.

## Subsets

| config | rows | base | language | how the gold is fixed |
|---|---:|---|---|---|
| `appworld` | 5,679 | [agentic-selfgen-ko-v1](https://huggingface.co/datasets/HBKenerzai/agentic-selfgen-ko-v1) | ko | a **rule computes** the answer (count / list / sum / last of the episode's successful actions) |
| `nemotron-ko` | 43,133 | agentic-think-v2-react-hybrid (nemotron, translated) | ko | 27B **extracts a verbatim fact**; a rule verifies it appears in an earlier turn (grounding) |
| `nemotron-en` | 63,928 | agentic-think-v2-react-hybrid (nemotron) | en | same as above, in English |
| **total** | **112,740** | | | |

Two mechanisms, same guarantee — the recalled value is provably correct:

- **appworld** has a fixed 4-app schema (phone / notes / tasks / payments), so a rule reads the successful
  tool calls and computes the answer: *"how many notes did I create", "what did I send", "total transferred"*,
  *"what was the last alarm"*. Answers are rule-generated; teacher 27B paraphrases the question for variety.
- **nemotron** has ~840 arbitrary tool schemas, so a rule cannot compute rich facts. Instead the 27B picks a
  short concrete fact that appeared **verbatim earlier** (an id, code, email, amount, date, name, result),
  and a rule **drops the row unless that fact really occurs in an earlier turn**. This blocks hallucinated
  recall (2.2% of en candidates were dropped this way).

## What a recall turn looks like

```
(… 20 turns of agentic tool use …)
user:      방금 이메일로 받으신 인증 코드가 무엇이었나요?
assistant: (reasoning) 사용자가 앞선 대화에 나온 정보를 다시 확인한다. 앞서 587291이 나왔으니 그대로 알려 준다.
           (content)   인증 코드는 587291입니다.
```
```
user:      What was the output of the factorial function for the input 5?
assistant: (reasoning) The user is asking me to recall information from earlier …
           (content)   The function returned 120 for the input 5.
```

The recall question sits a median of 6–7 turns (up to ~37) after the fact first appeared. The assistant
answer is plain text (no markdown) and keeps the `reasoning_content` visible, so training can mask or keep
the reasoning on the recall turn as it chooses.

## Schema

| field | type | description |
|---|---|---|
| `id` | str | base id + `-recall` |
| `source` | str | base source (`kotraj_appworld_*`, `nemotron_tc`, `nemotron_ia`) |
| `tools` | str (JSON) | the base episode's tool catalog |
| `messages` | str (JSON) | base conversation with the recall user/assistant turns added; the recall assistant turn has `content` + `reasoning_content` and no `tool_calls` |
| `think_source` | str | `recall_rule` / `recall_27b` (appworld), `recall_nm_ko` / `recall_nm_en` (nemotron) |
| `meta` | str (JSON) | `recall`: the gold fact/answer, source turn, recall distance, placement (end/mid) |

```python
from datasets import load_dataset
ds = load_dataset("HBKenerzai/agentic-recall-v1", "nemotron-ko", split="train")
```

## Quality

Independently re-verified on 3,000-row samples per subset with **0 issues**: the recalled fact genuinely
appears in an earlier turn, it is not leaked in the question, it is present in the answer, and the answer
contains no markdown.

## Access

This dataset is gated: access is granted on request after manual review.

## Provenance

Built by ENERZAi with the agentic-datagen `data_gen/kotraj_recall.py`, `gen_recall.py`,
`gen_nemotron_recall.py`. Teacher for paraphrase/extraction: Qwen3.8-27B-FP8. Bases: AppWorld-derived
self-generated trajectories and the nemotron portion of agentic-think-v2-react-hybrid.
Related: [agentic-think-v2-react-hybrid-ko](https://huggingface.co/datasets/HBKenerzai/agentic-think-v2-react-hybrid-ko),
[agentic-selfgen-ko-v1](https://huggingface.co/datasets/HBKenerzai/agentic-selfgen-ko-v1).
