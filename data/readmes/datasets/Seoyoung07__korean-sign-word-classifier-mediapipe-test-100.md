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
pretty_name: KSL Test-100 Evaluation Dataset
size_categories:
  - n<1K
---

# KSL Test-100 Evaluation Dataset

This dataset contains 100 isolated Korean sign-language word videos used for the Test-100 evaluation of the MediaPipe keypoint word classifier.

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
- Total videos: 100
- Top-1 correct: 60 / 100 (60.00%)
- Top-5 contains expected: 71 / 100 (71.00%)
- Inference errors: 0

## AI Tool Used

- AI tool used: Codex

## Notes

The filename typo `꺠끗하다.mp4` is kept as the original filename, while `metadata.csv` records the canonical label as `깨끗하다`. Evaluation reports also document this normalization.

## License And Data Use

This dataset is published for the realtime KSL captioning project evaluation workflow. Confirm any institutional, privacy, or presentation requirements before redistributing or reusing the videos outside that context.
