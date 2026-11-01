---
license: cc-by-nc-4.0
language:
  - en
  - zh
  - ja
  - ko
tags:
  - roleplay
  - chat
  - conversational
  - creative-writing
size_categories:
  - 100K<n<1M
---

# RP-Opus: Roleplay Conversation Dataset

A high-quality roleplay conversation dataset curated from an AI emotional companion app, designed for training creative roleplay and conversational AI models.

## Dataset Description

This dataset contains multi-turn roleplay conversations between users and AI characters. The data has been carefully filtered and processed to ensure quality and diversity.

### Files

| File | Description | Size |
|------|-------------|------|
| `messages_enhanced.jsonl` | Enhanced conversations with AI reasoning/thinking traces | ~150MB |
| `messages_remaining.jsonl` | Original filtered conversations | ~1.1GB |

### Data Structure

Each record is a JSON object with the following structure:

```json
{
  "chat_id": "unique_conversation_id",
  "messages": [
    {"role": "system", "content": "Character system prompt..."},
    {"role": "user", "content": "User message..."},
    {"role": "assistant", "content": "AI character response..."}
  ],
  "robot": {
    "robot_name": "Character Name",
    "nsfw": 0 or 1
  },
  "lang_code": "en",
  "digg": 0,
  "created_at": "2026-01-01 00:00:00",
  "updated_at": "2026-01-29 00:00:00"
}
```

### Enhanced Data Format

The `messages_enhanced.jsonl` file contains conversations where the last assistant response includes reasoning:

```json
{
  "role": "assistant",
  "content": "<think>AI's internal reasoning process...</think>The actual response..."
}
```

## Data Processing

The dataset underwent extensive filtering and quality improvements:

### Filtering Criteria

- **Turn Count**: 4-60 turns per conversation
- **Message Length**: Max 2100 characters per message
- **Content Quality**: Removed empty replies, short replies, duplicate content
- **Role Alternation**: Ensured proper user/assistant message flow
- **Deduplication**: Based on `chat_id`, prioritizing liked (`digg=1`) conversations

### Quality Enhancements

- **Echo Reply Detection**: Filtered conversations where AI repeatedly echoes user messages
- **Structural Repetition Detection**: Removed conversations with repetitive patterns
- **PII Masking**: Sensitive information (phone, email, etc.) has been masked
- **Balanced Sampling**: Uniform distribution across languages and SFW/NSFW content

## Languages

- English (en)
- Chinese (zh)
- Japanese (ja)
- Korean (ko)
- And other languages

## Use Cases

- Training roleplay/creative writing models
- Fine-tuning conversational AI
- Research on human-AI interaction patterns
- Character AI development

## License

This dataset is released under **CC BY-NC 4.0** (Creative Commons Attribution-NonCommercial 4.0).

- ✅ Academic and research use
- ✅ Personal projects
- ❌ Commercial use without permission

## Citation

```bibtex
@dataset{rp_opus_2026,
  title={RP-Opus: Roleplay Conversation Dataset},
  author={taozi555},
  year={2026},
  url={https://huggingface.co/datasets/taozi555/rp-opus}
}
```

## Disclaimer

This dataset contains roleplay conversations that may include mature themes. Users should apply appropriate content filtering based on their use case. The dataset creators are not responsible for any misuse of this data.
