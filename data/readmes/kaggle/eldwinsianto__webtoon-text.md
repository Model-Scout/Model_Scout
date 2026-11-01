# Hangul Korean Webtoon 5k Dataset

korean OCR dataset with manually croppped webtoon text images.

**Overview**
This dataset contains Korean text images and corresponding OCR annotations created for training and evaluating Optical Character Recognition (OCR) models. The data focuses on dialogue and narrative text commonly found in webtoon panels.

**Source**
The text images were collected from the Korean webtoon “Byeorisamsyap”. This dataset is intended strictly for research and educational purposes.

**Language**
Language: Korean
Script: Hangul

**Annotation & Label Format**
All annotations are stored in a single file: labels.txt.
Each line in labels.txt follows the format:
imgs/0001.png 

**version changes**
Version 3 — Changes

Adding 5000 new images label on train/imgs

Restructured the dataset by splitting multi-line text into per-line samples for more consistent OCR training data.

Reviewed and filtered low-quality images (blurred, tilted, low-contrast) to improve overall dataset quality.

출처: Kaggle (eldwinsianto/webtoon-text)
태그: image, text
라이선스: Other (specified in description)
수정일: 2026-05-01T21:03:43.597Z
