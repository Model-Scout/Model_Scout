---
language:
- tl
- hil
- ceb
- de
- es
- fr
- id
- ja
- ko
- ms
- pt
- zh
- en
license: other
task_categories:
- text-generation
tags:
- sft
- code
- coding-assistant
- tool-calling
- rage-core-gen-1
size_categories:
- 100K<n<1M
---

# Rage Core 1

Supervised fine-tuning dataset for **Rage Core Gen 1** — developed by **DevNameGelo**, *Powered by RGC Rage Gen Core*.

This dataset teaches the model to: understand user intent and ask clarifying questions when requirements are ambiguous, deliver complete production-oriented implementations, debug real-world problems, make precise code edits, operate as a coding agent through explicit tool calls, handle multilingual users, process multimodal inputs honestly, and refuse to fabricate facts, tool results, or post-cutoff information.

## Structure

Each line of the JSONL files is one conversation record:

```json
{
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ],
  "reasoning": false,
  "category": "coding",
  "language": "python",
  "difficulty": "intermediate",
  "tags": ["cli", "stdlib"]
}
```

- **messages** — OpenAI-style chat format. Conversations always start with a system message (the Rage Core Gen 1 identity) and end with an assistant message. Multi-turn conversations alternate user/assistant.
- **reasoning** — whether the runtime reasoning switch is ON for this conversation. When `true`, the system prompt instructs the model to open with a concise **Understand / Analyze / Plan / Act / Verify / Answer** summary (a distilled justification — never raw chain-of-thought).
- **category** — one of: chat, coding, debugging, review, architecture, agent, reasoning, multilingual, multimodal, security.
- **language** — the conversation language for multilingual examples (en, tl, hil, ceb, es, fr, de, pt, id, ms, ja, ko, zh); otherwise the dominant programming language of the example (python, typescript, ...).
- **difficulty** — beginner / intermediate / advanced / expert.
- **tags** — free-form topical tags.

## Tool-calling convention (agent category)

Tool use is represented inside the standard 3-role structure. An assistant turn ends with a fenced block:

``````tool_call
{"tool": "read_file", "args": {"path": "src/app.py"}}
``````

The following user turn carries the result:

``````tool_result
{"tool": "read_file", "ok": true, "result": "...file contents..."}
``````

Every tool claim is grounded: a tool action is only ever stated as done when a matching `tool_result` exists in the conversation. Failures appear as `"ok": false` with recovery in the next assistant turn. Tools covered: read_file, write_file, edit_file, list_dir, search_code, run_command, web_search, browser_navigate, browser_click, browser_type, browser_snapshot.

## Multimodal convention (multimodal category)

Images reach the model as bracketed metadata, e.g. `[Image: screenshot of a terminal showing a Python traceback ...]`. The model works strictly from the provided description — it never invents visual details, and when the description is missing or insufficient it says so and asks.

## Contents

**Total: 527 examples** (after validation and deduplication; 0 near-duplicates and 0 structurally-invalid records removed from the raw pool).

### Splits

| Split | Examples |
|---|---|
| Train | 421 |
| Validation | 53 |
| Test | 53 |

### Categories

| Category | Examples | Share |
|---|---|---|
| coding | 102 | 19.4% |
| chat | 81 | 15.4% |
| debugging | 80 | 15.2% |
| agent | 52 | 9.9% |
| review | 52 | 9.9% |
| architecture | 52 | 9.9% |
| multilingual | 27 | 5.1% |
| multimodal | 27 | 5.1% |
| reasoning | 27 | 5.1% |
| security | 27 | 5.1% |

### Difficulty

| Difficulty | Examples | Share |
|---|---|---|
| beginner | 109 | 20.7% |
| intermediate | 255 | 48.4% |
| advanced | 156 | 29.6% |
| expert | 7 | 1.3% |

### Conversation languages

| Language | Examples |
|---|---|
| English | 394 |
| Filipino/Tagalog | 6 |
| Hiligaynon/Ilonggo | 3 |
| Cebuano/Bisaya | 3 |
| German | 2 |
| Spanish | 2 |
| French | 2 |
| Indonesian | 2 |
| Japanese | 2 |
| Portuguese | 2 |
| Korean | 1 |
| Malay | 1 |
| Chinese | 1 |

### Programming languages

| Language | Examples |
|---|---|
| javascript | 35 |
| python | 27 |
| typescript | 10 |
| html | 9 |
| rust | 4 |
| go | 4 |
| java | 2 |
| csharp | 2 |
| cpp | 2 |
| php | 2 |
| ruby | 2 |
| sql | 2 |
| swift | 1 |
| kotlin | 1 |
| bash | 1 |
| c | 1 |
| dart | 1 |

### Behavioral flags

| Flag | Examples |
|---|---|
| reasoning=true | 0 |
| reasoning=false | 0 |
| tool-calling examples | 52 |
| multi-turn examples | 52 |
| multimodal-marked examples | 27 |

## Quality rules enforced

- No identity leakage: the assistant never claims to be ChatGPT, GPT, Claude, Gemini, Qwen, Llama, or any other model — it is always Rage Core Gen 1 by DevNameGelo.
- No fabricated tool results: every executed-action claim has a matching tool_result in the conversation.
- Balanced code fences in every message; all tool_call / tool_result blocks are valid JSON.
- Honesty about execution: generated code is presented as written, not as run, unless a tool result proves otherwise.
- No invented version numbers, CVEs, benchmarks, or post-cutoff events.
- Multilingual examples are held to correct grammar and natural register (Philippine-language examples were hand-written and reviewed).

## Intended use

Supervised fine-tuning of Rage Core Gen 1 and RGC Rage Gen Core family models. Load with:

```python
from datasets import load_dataset
ds = load_dataset("rgcmainhub/rage-core-1")
```

## License / attribution

© DevNameGelo — Powered by RGC Rage Gen Core. Contact the dataset owner for licensing terms.
