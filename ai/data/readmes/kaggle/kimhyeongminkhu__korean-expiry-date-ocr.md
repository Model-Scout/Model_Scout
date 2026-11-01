# Korean Product Expiration Date Detection Dataset

A Korean convenience store expiry date dataset for OCR and object detection

## Dataset Overview

This dataset contains images of expiry dates collected from real Korean convenience store products.  
To improve robustness against uncommon printing styles, the dataset is supplemented with **900 AI-generated synthetic images** produced using **Nano Banana inpainting**, enabling coverage of rare font patterns and visual variations.

All annotations follow a **semantic token labeling scheme** rather than purely positional labels.  
Tokens such as `Y4`, `ENG_MON`, and `NUM2` represent the semantic structure of date components, allowing models to generalize across diverse Korean expiry-date formats.

---

## Detection Pipeline

The dataset is structured as a **three-stage detection pipeline**:

1. **Expiry Region Detection** — locating the expiry-date area on product packaging  
2. **Expiry Date Detection** — detecting the printed date within the expiry label  
3. **Day / Month / Year Detection** — identifying individual date components

---

## Project Context

This dataset was developed as part of a **capstone project**, achieving **96% end-to-end expiry date recognition accuracy** in real-world product images.

---

## Project Repository

Full implementation of the expiry-date detection pipeline:  
https://github.com/HyeongMinK/Vision-Eleven

출처: Kaggle (kimhyeongminkhu/korean-expiry-date-ocr)
태그: intermediate, computer vision, image, retail and shopping, korea
라이선스: CC BY-NC-SA 4.0
수정일: 2026-03-15T07:39:35.953Z
