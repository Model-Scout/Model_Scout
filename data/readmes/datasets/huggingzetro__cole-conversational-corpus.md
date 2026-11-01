---
task_categories:
  - text-generation
  - question-answering
language:
  - en
  - th
  - ko
  - es
  - fr
  - ar
  - hi
  - ja
  - zh
size_categories:
  - 100K<n<1M
tags:
  - multimodal
  - human-ai-dialogue
  - tool-use
  - cross-channel
  - slack
  - whatsapp
license: other
license_name: commercial-license
license_link: LICENSE
configs:
  - config_name: default
    data_files:
      - split: train
        path: sample.jsonl
---

# Cole Multimodal Conversational Corpus

Real human-AI dialogue collected from a production AI assistant deployed across 7 messaging platforms. This is **not** synthetic data - these are real conversations where users send text, photos, voice messages, video, and documents alongside natural conversation.

## What makes this dataset unique

- **Multimodal**: Text, images, audio, video, and documents in conversation context - not isolated media files
- **Cross-channel**: Same users move conversations across Slack, WhatsApp, voice calls, SMS/iMessage, LINE, Telegram, and email
- **Tool-use annotated**: Every turn where the AI executes tools (calendar, email, web search, file operations, API calls) is annotated with intent and outcome
- **Multilingual**: 9 languages in organic production traffic (EN, TH, KO, ES, FR, AR, HI, JA, ZH) - not translations
- **Growing daily**: ~350+ new turns per day from active production usage

## Dataset summary

| Metric | Value |
|--------|-------|
| Conversation turns | 102,500+ |
| Media files | 100,000+ (images, audio, video, documents) |
| Users | 1,250+ across 574 workspaces |
| Channels | 7 platforms |
| Languages | 9 |
| Date range | 2026 - present |
| Refresh | Daily |

## Sample

This repository contains an anonymized sample (50 conversation turns) demonstrating the schema and signal quality. The full dataset is available under commercial license.

### Schema

Each line in the JSONL is a conversation turn:

```json
{
  "conversation_id": "conv_a1b2c3",
  "turn_index": 1,
  "timestamp": "2026-04-15T09:23:11Z",
  "channel": "slack",
  "role": "user",
  "content": "Can you find me flights to Tokyo next week?",
  "media": null,
  "tool_calls": null,
  "language": "en",
  "workspace_id": "ws_x7y8z9"
}
```

When the AI uses tools, the turn includes structured annotations:

```json
{
  "role": "assistant",
  "content": "I found 3 options for you...",
  "tool_calls": [
    {
      "tool": "web_search",
      "intent": "flight_search",
      "query": "flights to Tokyo departing Apr 21-25",
      "outcome": "success"
    }
  ]
}
```

Media turns reference the modality:

```json
{
  "role": "user",
  "content": "What do you think of this design?",
  "media": {
    "type": "image",
    "format": "png",
    "size_bytes": 284710
  }
}
```

## Licensing

This dataset is commercially licensed. The sample is provided for evaluation purposes.

For full dataset access, licensing terms, and pricing, contact:

- **Email**: victor@pocodot.ai
- **Catalog**: [pocodot.ai/data](https://pocodot.ai/data)
- **Company**: Pocodot Labs, Inc.

## Data provenance

- Collected under explicit Terms of Service with data licensing provisions
- PII stripped per CCPA and GDPR standards
- Full chain of custody from collection to delivery
- Every turn has timestamped provenance with channel and workspace attribution
