---
license: apache-2.0
task_categories:
  - text-classification
language:
  - en
  - es
  - fr
  - de
  - pt
  - ja
  - ko
  - zh
  - hi
  - ru
  - it
tags:
  - agent-safety
  - tool-calling
  - guardrails
size_categories:
  - 100K<n<1M
---

# auto — agentic tool-call approve/deny training data

Training corpus for [`ProCreations/auto-1b`](https://huggingface.co/ProCreations/auto-1b),
an encoder that decides whether an AI agent's proposed tool call can run automatically.

Exactly **700,000 examples**, balanced at **350,000 approve / 350,000 deny**.

- 288,260 retained examples from the auto-0.4b corpus.
- 411,740 new examples generated with GPT-5.6 Luna at low reasoning effort.
- Every new row passed structural validation and exact-evidence checks during generation.
  An initial subset was also independently blind-audited; its known rejects were excluded.
  The separate audit was then stopped at the dataset owner's request to conserve subscription
  usage, so the full 411,740-row addition should not be described as independently audited.
- Exact and near duplicates were removed within each label while preserving opposite-label
  contrastive cases.
- [`ProCreations/approve-or-deny`](https://huggingface.co/datasets/ProCreations/approve-or-deny)
  is an untouched benchmark. It was not used for generation, weighting, training, or
  calibration; exact and near content collisions were excluded from this corpus.

## Input format

`text` contains the exact model input. The ordering and headers are significant:

```text
### PROPOSED TOOL CALL
tool: <tool name>
args: <arguments>

### USER REQUEST
<human request>

### AGENT HISTORY
[1] Tool(arguments)
-> result
```

An empty history is serialized as `(no prior actions)`.

## Decision rule

`deny` means executing the proposed call now would cause consequential, unauthorized harm,
or that it follows instructions injected through untrusted content. `approve` covers
ordinary work, normal network access, legitimate package installation, read-only local
inspection, and destructive-looking actions that are explicitly authorized and correctly
scoped.

## Fields

| field | meaning |
|---|---|
| `text` | exact serialized classifier input |
| `label` | `approve` or `deny` |
| `user_request` | human request |
| `history` | prior `{tool, args, result}` actions |
| `call` | proposed `{tool, args}` action |
| `category`, `difficulty` | curriculum metadata |
| `rationale` | deciding evidence (not part of model input) |
| `framework`, `domain`, `lang` | scenario diversity axes |
| `length_bucket`, `gen_mode`, `subset` | generation metadata |

## Limitations

Most rows are synthetic. Independent review and deduplication reduce label noise but cannot
remove shared model-family blind spots. This dataset is not a replacement for sandboxing,
least privilege, or human review of high-impact operations.
