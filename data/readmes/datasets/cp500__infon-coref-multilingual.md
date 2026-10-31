---
license: apache-2.0
language:
  - en
  - ja
  - zh
  - ko
  - th
multilinguality: multilingual
task_categories:
  - token-classification
  - other
pretty_name: Infon Multilingual Coreference Corpus
size_categories:
  - 1K<n<10K
tags:
  - coreference
  - multilingual
  - synthetic
  - bedrock
  - claude
configs:
  - config_name: default
    data_files:
      - split: train
        path: train.jsonl
      - split: val
        path: val.jsonl
---

# Infon multilingual coreference corpus

Synthetic bracket-tagged coreference data for training multilingual
coref pointer-network models. Generated with Claude (Haiku 4.5 on
Bedrock) via the templated prompts in
`infon.cassette.synthgen_coref`.

## Schema

Each row:

```json
{
  "doc_id": "coref_synth_<hash>",
  "lang": "en|ja|zh|ko|th",
  "domain": "automotive|defence|semiconductors|energy",
  "text": "...",
  "mentions": [
    {"start": 0, "end": 6, "text": "Toyota", "cluster": 0}
  ],
  "clusters": [[0, 3, 5], [1, 4]]
}
```

Char offsets `start`/`end` slice `text` exactly — every doc is
validated by `CorefDoc.validate()` before being written.

## Splits

| Language | Train | Val | Total |
|----------|-------|-----|-------|
| en | 880 | 220 | 1100 |
| ja | 880 | 220 | 1100 |
| ko | 880 | 220 | 1100 |
| th | 880 | 220 | 1100 |
| zh | 880 | 220 | 1100 |
| **All**  | **4400** | **1100** | **5500** |

Stratified by language so per-language eval numbers stay comparable.

## Model

Trained model lives at
[cp500/infon-coref-pointer](https://huggingface.co/cp500/infon-coref-pointer).

## License

Apache 2.0. Underlying generations are Claude's output —
[Anthropic's usage policy](https://www.anthropic.com/legal/aup) applies.
