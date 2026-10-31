---
pretty_name: Test-100 Korean Sign Language Dictionary Clips
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

# Test-100 Korean Sign Language Evaluation Dataset

## Dataset Summary

This dataset contains 100 Korean Sign Language isolated-word MP4 clips used for
evaluation of the project model `Seoyoung07/korean-sign-word-classifier-mediapipe`.

The project team selected and extracted 100 word entries from the Korean Sign
Language Dictionary.

Source/reference: [https://sldict.korean.go.kr/front/main/main.do](https://sldict.korean.go.kr/front/main/main.do)

## Contents

- `videos/`: 100 MP4 files
- File names are the target Korean word labels, for example: `간호사.mp4`
- Local source folder before upload: `/home/moon/Downloads/Test-100`
- Local folder size before upload: 122.8 MB

## Intended Use

This dataset is intended for reproducible evaluation of Korean Sign Language
isolated-word recognition. It is not intended to represent the full Korean Sign
Language Dictionary.

## Label Format

The target label is the MP4 filename stem. Example:

```text
videos/깨끗하다.mp4 -> 깨끗하다
```

## Source And Licensing Notes

The clips were selected/extracted by the project team from the Korean Sign
Language Dictionary source linked above. Users should review the source website
terms before redistributing or using the data outside this project evaluation
context.

## AI Tools Used

AI tool used: Codex. Codex was used to package/upload the dataset and draft this
dataset card. Codex was not used to create the videos or labels.
