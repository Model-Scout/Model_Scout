---
pretty_name: Self-made-60 Korean Sign Language Clips
language:
- ko
task_categories:
- video-classification
- feature-extraction
tags:
- korean-sign-language
- sign-language-recognition
- isolated-word-recognition
- evaluation
size_categories:
- n<1K
license: other
---

# Self-made-60 Korean Sign Language Evaluation Dataset

## Dataset Summary

This dataset contains 60 self-recorded Korean Sign Language isolated-word MP4
clips created by the project team for additional evaluation.

## Contents

- `videos/`: 60 MP4 files
- File names are the target Korean word labels, for example: `간호사.mp4`
- Local source folder before upload: `/home/moon/Downloads/self-made-60`
- Local folder size before upload: 370.4 MB

## Intended Use

This dataset is intended for reproducible evaluation of the submitted Korean Sign
Language isolated-word recognition pipeline. It is a small project-made
evaluation set, not a general benchmark.

## Label Format

The target label is the MP4 filename stem. Example:

```text
videos/깨끗하다.mp4 -> 깨끗하다
```

## Source And Licensing Notes

The videos were recorded by the project team. They are provided for
course/project evaluation of the submitted model and inference pipeline.

## AI Tools Used

AI tool used: Codex. Codex was used to package/upload the dataset and draft this
dataset card. Codex was not used to create the videos or labels.
