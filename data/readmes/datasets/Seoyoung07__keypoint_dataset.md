---
pretty_name: Korean Sign Language Keypoint Dataset
language:
- ko
task_categories:
- feature-extraction
- video-classification
tags:
- korean-sign-language
- sign-language-recognition
- mediapipe
- holistic-landmarks
- keypoints
size_categories:
- 100K<n<1M
license: other
---

# Korean Sign Language Keypoint Dataset

## Dataset Summary

This dataset contains the project keypoint cache used for Korean Sign Language
isolated-word model training/evaluation experiments.

The keypoints were extracted with MediaPipe Holistic from a subset of the AI-Hub
sign-language video dataset.

Source/reference: [https://aihub.or.kr/aihubdata/data/view.do?srchOptnCnd=OPTNCND001&currMenu=115&topMenu=100&searchKeyword=%EC%88%98%EC%96%B4&aihubDataSe=data&dataSetSn=103](https://aihub.or.kr/aihubdata/data/view.do?srchOptnCnd=OPTNCND001&currMenu=115&topMenu=100&searchKeyword=%EC%88%98%EC%96%B4&aihubDataSe=data&dataSetSn=103)

## Contents

- `keypoint_cache.zip`: compressed archive of the local `keypoint_cache/` folder
- Extracted archive structure:
  - `keypoint_cache/1.Training/`
  - `keypoint_cache/2.Validation/`
- Keypoint files: 269518 `.npy` files in the local source folder
- Local uncompressed folder size before upload: 27.4 GB
- Uploaded archive size: 20.2 GB
- `source_metadata.txt`: local source metadata copied from `/home/moon/metadata.txt`

The archive is used instead of uploading hundreds of thousands of individual
`.npy` files so that the dataset can be downloaded and reproduced more reliably.

## Source Subset Metadata

```text
AI 학습용 다운로드
├─ 수어 영상/
   ├─ 1.Training/  (33 files)
   │  ├─ [라벨]01_real_word_morpheme.zip
   │  ├─ [원천]01~32_real_word_video.zip
   │
   └─ 2.Validation/  (2 files)
      ├─ [라벨]01_real_word_morpheme.zip
      ├─ [원천]01_real_word_video.zip
```

## Usage

Download and extract:

```bash
unzip keypoint_cache.zip
```

The extracted folder should contain `keypoint_cache/1.Training` and
`keypoint_cache/2.Validation`.

## Source And Licensing Notes

The raw videos originated from AI-Hub sign-language data. This repository
contains derived keypoint cache files, not the original raw AI-Hub videos. Users
should review and follow AI-Hub access/license terms for any downstream use.

## AI Tools Used

AI tool used: Codex. Codex was used to package/upload the dataset and draft this
dataset card. Codex was not used to create the source AI-Hub videos, keypoint
labels, or original data split.
