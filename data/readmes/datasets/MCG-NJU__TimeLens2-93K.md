---
license: apache-2.0
pretty_name: TimeLens2-93K
task_categories:
  - video-text-to-text
language:
  - en
  - zh
  - ja
  - ko
tags:
  - video-temporal-grounding
  - long-video-understanding
size_categories:
  - 10K<n<100K
configs:
  - config_name: preview
    data_files:
      - split: train
        path: TimeLens2-93K_preview.jsonl
    default: true
  - config_name: raw_annotations
    data_files:
      - split: train
        path: TimeLens2-93K_raw_annotations.jsonl
  - config_name: conversations
    data_files:
      - split: train
        path: TimeLens2-93K_conversations.jsonl
---

# TimeLens2-93K

TimeLens2-93K is a large-scale, long-video temporal grounding dataset. This release contains **23,793 videos** and **93,232 text–temporal interval pairs**, including **12,091 multi-span pairs**. The videos range from short clips to nearly 100 minutes and cover broad web domains such as entertainment, education, sports, news, science and technology, gaming, travel, vehicles, music, and daily life.

TimeLens2-93K offers a rare combination of **scale, long-context coverage, multi-span supervision, and explicit label verification**. We hope it serves as a strong foundation for training generalist video models that can search long timelines, return auditable evidence, and transfer across grounding instructions instead of merely memorizing one timestamp format.

## Paper

[TimeLens2: Generalist Video Temporal Grounding with Multimodal LLMs](https://arxiv.org/abs/2607.17423)

<p align="center">
  <img src="assets/TimeLens2-93K_overview.jpg" alt="TimeLens2-93K construction pipeline and current dataset statistics" width="100%">
</p>

## Highlights

- **Long and diverse videos:** from short clips to nearly 100-minute videos across a wide range of real-world domains.
- **Multi-span by design:** annotations can contain a variable number of temporal intervals when evidence recurs at disjoint moments.
- **High-confidence labels:** cross-agent agreement, semantic verification, and boundary-focused refinement form complementary quality-control stages.
- **Training-ready formats:** use clean raw annotations or diverse multi-turn SFT conversations with varied instructions, answer syntax, and timestamp representations.

## Files

| Path | Description |
| --- | --- |
| `videos/videos-xxxxx-of-00018.tar` | Video archives split into 18 shards |
| `TimeLens2-93K_preview.jsonl` | Viewer-friendly join with video ID, `annotations` list, and `messages` list |
| `TimeLens2-93K_raw_annotations.jsonl` | Raw text queries and their temporal intervals |
| `TimeLens2-93K_conversations.jsonl` | Multi-turn SFT conversations with diverse query and answer formats |

## Annotation formats

### Raw annotations

Each line contains one video and all of its text–timestamp annotations:

```json
{"video_id":"-IA08sFr96U","annotations":[{"text":"Two men alternate singing on stage while holding microphones","timestamps":[[28,190]]}]}
```

### Conversations

Each line contains one video and a multi-turn conversation. Questions and answers use diverse natural-language and timestamp formats:

```json
{"video_id":"-IA08sFr96U","messages":[{"role":"user","content":"Retrieve the video segment timestamps matching: 'Two men alternate singing on stage while holding microphones'.\nReturn the result as an array of [start, end] pairs in seconds."},{"role":"assistant","content":"[[28.0, 190.0]]"}]}
```

## Loading annotations

```python
from datasets import load_dataset

preview = load_dataset("MCG-NJU/TimeLens2-93K", split="train")
raw = load_dataset(
    "MCG-NJU/TimeLens2-93K", "raw_annotations", split="train"
)
conversations = load_dataset(
    "MCG-NJU/TimeLens2-93K", "conversations", split="train"
)
```

To download the video archives:

```bash
hf download MCG-NJU/TimeLens2-93K \
  --repo-type dataset \
  --include "videos/*.tar" \
  --local-dir TimeLens2-93K
```

## License

This dataset is released under the Apache License 2.0.

## Citation

```bibtex
@article{zhu2026timelens2,
  title={TimeLens2: Generalist Video Temporal Grounding with Multimodal LLMs},
  author={Zhu, Yuhan and Ma, Changlian and Zeng, Xiangyu and Li, Xinhao and Zhang, Zhiqiu and Li, Songze and Zhang, Jun and Jiang, Tianxiang and Yang, Yuandong and Yan, Ziang and others},
  journal={arXiv preprint arXiv:2607.17423},
  year={2026}
}
```
