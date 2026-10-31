---
license: other
language:
  - ko
task_categories:
  - video-classification
tags:
  - korean-sign-language
  - sign-language-recognition
  - isolated-word-classification
  - mediapipe
  - ksl
pretty_name: KSL Self-made-60 Evaluation Dataset
size_categories:
  - n<1K
---

# KSL Self-made-60 Evaluation Dataset

This dataset contains 60 newly recorded isolated Korean sign-language word videos. The words were selected from the Test-100 items that were Top-1 correct in the prior evaluation.

## Contents

- `videos/`: MP4 isolated Korean sign-language word clips.
- `metadata.csv`: Video-level labels, model predictions, and evaluation fields.
- `evaluation/`: Full evaluation reports and machine-readable result files.

## Evaluation Summary

- Model: `Seoyoung07/korean-sign-word-classifier-mediapipe`
- Model snapshot used for evaluation: `214c0d87294695f4c79086440404bfb72fa7c5bc`
- Checkpoint epoch: `41`
- Checkpoint validation accuracy: `0.8962213765938981`
- Device used for evaluation: `cuda`
- Total videos: 60
- Top-1 correct: 5 / 60 (8.33%)
- Top-5 contains expected: 7 / 60 (11.67%)
- Inference errors: 0

## AI Tool Used

- AI tool used: Codex

## Notes

The original files were timestamp-named recordings. They were sorted chronologically and renamed to canonical word labels before evaluation. The full filename mapping is in `evaluation/rename_mapping_20260606_193217.csv`.

## License And Data Use

This dataset is published for the realtime KSL captioning project evaluation workflow. Confirm any institutional, privacy, or presentation requirements before redistributing or reusing the videos outside that context.
