---
license: mit
task_categories:
  - text-generation
language:
  - en
tags:
  - dataclaw
  - claude-code
  - codex-cli
  - conversations
  - coding-assistant
  - tool-use
  - agentic-coding
  - claude-haiku-4-5-20251001
  - claude-opus-4-5-20251101
  - claude-opus-4-6
  - claude-sonnet-4-5-20250929
  - claude-sonnet-4-6
pretty_name: Coding Agent Conversations
configs:
  - config_name: default
    data_files: conversations.jsonl
---

# Coding Agent Conversation Logs

> **This is a performance art project.** Anthropic built their models on the world's freely shared information, then introduced increasingly [dystopian data policies](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks) to stop anyone else from doing the same — pulling up the ladder behind them. DataClaw lets you throw the ladder back down. The dataset it produces is yours to share.

Exported with [DataClaw](https://github.com/banodoco/dataclaw).

**Tag: `dataclaw`** — [Browse all DataClaw datasets](https://huggingface.co/datasets?other=dataclaw)

## Stats

| Metric | Value |
|--------|-------|
| Sessions | 549 |
| Projects | 14 |
| Input tokens | 15.1B |
| Output tokens | 4.6M |
| Last updated | 2026-02-24 |

### Models

| Model | Sessions |
|-------|----------|
| claude-opus-4-6 | 270 |
| claude-opus-4-5-20251101 | 256 |
| claude-sonnet-4-6 | 16 |
| claude-haiku-4-5-20251001 | 6 |
| claude-sonnet-4-5-20250929 | 1 |

## Schema

Each line in `conversations.jsonl` is one conversation session:

```json
{
  "session_id": "uuid",
  "project": "my-project",
  "model": "gpt-5.3-codex",
  "git_branch": "main",
  "start_time": "2025-01-15T10:00:00+00:00",
  "end_time": "2025-01-15T10:30:00+00:00",
  "messages": [
    {"role": "user", "content": "Fix the login bug", "timestamp": "..."},
    {
      "role": "assistant",
      "content": "I'll investigate the login flow.",
      "thinking": "The user wants me to...",
      "tool_uses": [{"tool": "Read", "input": "src/auth.py"}],
      "timestamp": "..."
    }
  ],
  "stats": {
    "user_messages": 5,
    "assistant_messages": 8,
    "tool_uses": 20,
    "input_tokens": 50000,
    "output_tokens": 3000
  }
}
```

### Privacy

- Paths anonymized to project-relative; usernames hashed
- No tool outputs — only tool call inputs (summaries)

## Load

```python
from datasets import load_dataset
ds = load_dataset("peteromallet/dataclaw-peteromallet", split="train")
```

## Export your own

```bash
pip install dataclaw
dataclaw
```
