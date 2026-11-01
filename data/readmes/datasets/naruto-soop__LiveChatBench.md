---
license: apache-2.0
language:
  - ko
  - en
task_categories:
  - translation
size_categories:
  - 1K<n<10K
pretty_name: LiveChatBench
configs:
  - config_name: default
    data_files:
      - split: test
        path: LiveChatBench.json
---

# LiveChatBench (v1.1)

Korean → English translation benchmark built from Korean live-streaming chat messages.
Each row pairs a Korean chat message with an English reference translation. Where a message relies on
streaming slang, community jargon, or a streamer/game name, a short `background` note explains the term;
it is an empty string when no note is needed.

## Fields

| Field        | Type   | Description                                                                 |
|--------------|--------|-----------------------------------------------------------------------------|
| `background` | string | Optional glossary note for slang/terms in the message (`""` when not given) |
| `ko`         | string | Source Korean chat message                                                  |
| `en`         | string | English reference translation                                               |

## Stats

- 1,000 sentence pairs (`test` split)
- 728 rows with a non-empty `background`, 272 rows with `""`

## Usage

```python
from datasets import load_dataset

ds = load_dataset("naruto-soop/LiveChatBench", split="test")
print(ds[0])
# {'background': '챌섭: 챌린저스 월드 (메이플스토리 서버)',
#  'ko': '챌섭이라 뭐가없는걸요..',
#  'en': 'Since it’s the Challengers World server, there’s hardly anything.'}
```

## Version

- v1.1 — 2026-09-27

## Citation

Paper: https://arxiv.org/abs/2601.02641

```bibtex
@misc{park2026empiricalstudyondevicetranslation,
      title={An Empirical Study of On-Device Translation for Real-Time Live-Stream Chat on Mobile Devices},
      author={Jeiyoon Park and Daehwan Lee and Changmin Yeo and Yongshin Han and Minseop Kim},
      year={2026},
      eprint={2601.02641},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2601.02641},
}
```
