---
license: cc-by-4.0
task_categories:
  - text-classification
  - text-generation
language:
  - en
  - ja
  - ko
tags:
  - bluesky
  - social-media
  - sentiment
  - anonymized
  - firehose
  - at-protocol
  - multilingual
  - nlp
pretty_name: "Bluesky Firehose: Anonymized Posts (Dec 2025)"
size_categories:
  - 100K<n<1M
dataset_info:
  features:
    - name: text
      dtype: string
    - name: author_did_hash
      dtype: string
    - name: sentiment
      dtype: string
    - name: sentiment_score
      dtype: float64
    - name: created_at
      dtype: string
    - name: language
      dtype: string
    - name: char_count
      dtype: int64
    - name: word_count
      dtype: int64
    - name: has_images
      dtype: bool
    - name: has_video
      dtype: bool
    - name: has_link
      dtype: bool
  splits:
    - name: train
      num_examples: 101040
---

# Bluesky Firehose: Anonymized Posts (Dec 2025)

101,040 Bluesky posts collected via the AT Protocol firehose, December 2-25, 2025. All author DIDs, post URIs, and thread relationships are SHA-256 hashed. Includes sentiment scores (VADER), language detection across 90 languages, media flags, and thread structure.

- **Posts**: 101,040
- **Unique Authors**: 43,998
- **Languages**: 90 detected (60.8% English, 12.5% Japanese, 11.4% unknown)
- **Collection**: Bluesky AT Protocol Jetstream WebSocket

## Dataset Structure

| Field | Type | Description |
|-------|------|-------------|
| `text` | string | Post content |
| `author_did_hash` | string | SHA-256 hashed author DID (16 chars) |
| `sentiment` | string | positive, negative, or neutral |
| `sentiment_score` | float | VADER compound score (-1.0 to 1.0) |
| `created_at` | string | ISO 8601 timestamp |
| `language` | string | ISO 639-1 language code |
| `has_images` / `has_video` / `has_link` | bool | Media flags |
| `hashtags` / `mentions` / `links` | string | JSON arrays |

## Anonymization

All personally identifiable fields are SHA-256 hashed (truncated to 16 chars). Thread structure is preserved through consistent hashing.

## Usage

```python
import pandas as pd

df = pd.read_csv('bluesky_posts.csv').dropna(subset=['text'])

# Sentiment distribution
print(df['sentiment'].value_counts())

# Language breakdown
print(df['language'].value_counts().head(10))
```

## Sources

Bluesky AT Protocol firehose via Jetstream WebSocket. Complies with Bluesky Developer Guidelines. Deletion requests: luke@lukesteuber.com.

## License

CC-BY-4.0

## Author

**Luke Steuber** · [lukesteuber.com](https://lukesteuber.com) · [@lukesteuber.com](https://bsky.app/profile/lukesteuber.com)
