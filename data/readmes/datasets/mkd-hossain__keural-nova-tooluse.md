---
license: apache-2.0
language: [ko, en]
task_categories: [text-generation]
tags: [keural, mkd, tool-calling, function-calling, agent, qwen]
---
# Keural Nova — tool-calling SFT slice (PRIVATE)

Tool-calling data used for **Keural Nova v1.2**. **17,337** rows: single-turn, multi-turn
(call -> tool result -> final answer), negative (no-call), and **long-context up to 32k tokens**.
Rendered as **Qwen XML** tool calls via ms-swift's native agent schema
(`tool_call`/`tool` roles + per-row `tools` JSON string).

- `tooluse_short.jsonl` — 14,337 rows (<= ~3.6k tokens)
- `tooluse_long32k.jsonl` — 3,000 rows (8k–32k tokens)

**Sources / licenses:** `glaiveai/glaive-function-calling-v2` (**Apache-2.0**) +
`NousResearch/hermes-function-calling-v1` (**Apache-2.0**), converted to Qwen XML; plus
MKD-original Korean tool-use and synthetic long-context packaging. Released **Apache-2.0**.
