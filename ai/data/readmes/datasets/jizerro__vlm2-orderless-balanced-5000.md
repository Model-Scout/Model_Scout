---
license: other
task_categories:
- visual-question-answering
- video-classification
language:
- ko
tags:
- traffic-accident
- vlm
- qwen
- fine-tuning
- balanced-subset
pretty_name: VLM-2 Orderless Balanced 5000
size_categories:
- 1K<n<10K
---

# VLM-2 Orderless Balanced 5000

Balanced 5,000-example subset for VLM-2 traffic accident maneuver-pair fine-tuning.

The subset was sampled from the orderless VLM-2 training labels with all 105 answer labels retained. Sampling is primarily balanced by the VLM-2 answer label:

- Target size: 5,000 examples
- Unique answer labels: 105
- Base cap per label: 100
- Maximum label count after balancing: 110
- Random seed: 42

## Files

- `train_vlm_2_orderless_balanced_5000_qwen_finetune.jsonl`: Qwen fine-tuning skeleton.
- `train_vlm_2_orderless_balanced_5000_label.jsonl`: `video_id` and answer label.
- `train_vlm_2_orderless_balanced_5000_eval_records.jsonl`: evaluation records with choices and scene metadata.
- `train_vlm_2_orderless_balanced_5000_video_qa.jsonl`: video QA records.
- `video_ids.txt`: selected shared video ids.
- `summary.json`: sampling and label-distribution summary.

This dataset contains label and prompt records only. Video files are referenced by `video_id` / placeholder paths and are not included.
