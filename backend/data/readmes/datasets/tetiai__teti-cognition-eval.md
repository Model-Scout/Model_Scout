---
license: odc-by
pretty_name: teti-cognition-eval
language:
  - multilingual
  - it
  - en
  - zh
  - ru
  - fr
  - es
  - pt
  - de
  - tr
  - ar
  - ja
  - pl
  - ko
  - vi
  - fa
  - nl
  - id
  - el
  - ro
  - cs
  - sw
  - hu
  - sv
  - uk
  - tl
  - bg
task_categories:
  - text-classification
tags:
  - cognition
  - human-ai-interaction
  - cognitive-offloading
  - delegation
  - conversation-analysis
size_categories:
  - n<1K
source_datasets:
  - allenai/WildChat-4.8M
---

# teti-cognition-eval

296 real, multi-turn conversations between people and an AI assistant in 26 languages, with
**1,348 user messages labeled** for how the person is thinking: delegation, motivation, own
reasoning, learning, application, verification, metacognition, depth and clear policy
violations, plus five 0–4 scores per conversation (autonomy, learning, engagement,
metacognition, verification).

It is the data used to fit and evaluate
[tetiai/teti-cognition-1](https://huggingface.co/tetiai/teti-cognition-1).

## Files

| File | Content |
| --- | --- |
| `conversations.jsonl` | One conversation per line: `id`, `source`, `source_id` (WildChat `conversation_hash`), `language`, `model` (the assistant that answered), `redacted`, `messages` (`role`, `content`). |
| `labels.jsonl` | One line per conversation: `id`, `split` (`calibration` / `test`), `labeler`, `messages` (one label object per user message, in order), `conversation` (the five 0–4 scores). |
| `LABELING.md` | The definitions every label follows. |

## How it was built

- **Source.** Conversations with 3 to 8 user messages and at most 24,000 characters from three
  shards of [WildChat-4.8M](https://huggingface.co/datasets/allenai/WildChat-4.8M) (revision
  `c827c6df8fcf008219ffaffa4d1dd77491099367`). WildChat is de-identified by its authors.
- **Sampling.** `source: wildchat` — 260 conversations sampled at random per language (seed 0).
  `source: wildchat-targeted` — 36 conversations whose user messages match multilingual phrases
  typical of the rare signals (verification, metacognition, avoidance, own attempts), added so
  that those fields have positives to measure. They were labeled exactly like the others; report
  random-sample metrics separately when comparing to real usage.
- **Labels.** Assigned by a language model (Claude Opus 5.5) following `LABELING.md`, one
  conversation at a time, every user message judged only on the conversation up to it. **They
  are not human annotations** and have not yet been reviewed by people.
- **Split.** `calibration` / `test` by the parity of `sha256(id)`: 157 conversations (739
  messages) for fitting, 139 conversations (609 messages) for every reported number.

## Label counts (all 1,348 messages)

| Field | Counts |
| --- | --- |
| `delegation` | none 671 · cognitive 565 · routine 112 |
| `motivation` | instrumental 1,114 · intrinsic 229 · avoidance 5 |
| `depth` | basic 1,137 · articulated 108 · minimal 103 |
| yes / no | learning 190 · own_reasoning 159 · verification 90 · metacognition 20 · application 8 · harmful 2 |

Avoidance, application and harmful are too rare here to evaluate reliably.

## Content warning

These are real user conversations from the public internet. Some contain offensive, sexual or
otherwise disturbing content, and requests the assistant refused.

## License and attribution

Released under the [Open Data Commons Attribution License (ODC-BY)](https://opendatacommons.org/licenses/by/1-0/),
the license of WildChat, from which the conversations come. The labels are © 2026 TetiAI srl,
released under the same license. If you use this dataset, please also cite WildChat:

```bibtex
@inproceedings{zhao2024wildchat,
  title     = {WildChat: 1M Chat{GPT} Interaction Logs in the Wild},
  author    = {Wenting Zhao and Xiang Ren and Jack Hessel and Claire Cardie and Yejin Choi and Yuntian Deng},
  booktitle = {The Twelfth International Conference on Learning Representations},
  year      = {2024},
  url       = {https://openreview.net/forum?id=Bl8u7ZRlbM}
}
```
