---
language:
- ko
license: other
license_name: educational-non-commercial
license_link: LICENSE
pretty_name: 한국 소설 띠지 교육용 표본 (Belly Band Edu Sample)
task_categories:
- object-detection
- image-to-text
size_categories:
- 1K<n<10K
tags:
- korean-literature
- book-cover
- belly-band
- obi
- yolo
- ocr
- digital-humanities
---

# 한국 소설 표지·띠지 교육용 표본 (Belly Band Edu Sample)

위키독스 매뉴얼 **「AI 학습을 위한 한국 소설 표지·띠지 텍스트 추출」**의 **교육 실습용** 데이터셋입니다.
한국 소설책의 **띠지(belly band / 帯, obi)** 영역을 객체 탐지(YOLOv8)로 검출하고, 그 텍스트를 OCR(Gemini)로 추출하는 두 노트북이 사용하는 데이터·자원을 한곳에 모았습니다.

## 📦 저장소 구성

| 파일 | 설명 |
|------|------|
| `belly_band_edu_sample.zip` | 표지 이미지 약 1,000장 + Label Studio 어노테이션(JSON). YOLOv8 노트북이 내려받아 학습에 사용 (약 90 MB). |
| `extract_prompt.md` | Gemini OCR 노트북 Stage 2(의미 블록 분류) 프롬프트 전문. |
| `YOLOv8_띠지검출_colab.ipynb` | 띠지 객체 탐지 학습 노트북 (데이터 준비 → 학습 → 평가 → 예측). |
| `Gemini_OCR_띠지_colab.ipynb` | 띠지 텍스트 OCR 실습 노트북 (Stage 1 OCR → Stage 2 의미 분류, 데모 모드 포함). |

### zip 내부 구조

```
belly_band_edu_sample/
├── images/                    # {ISBN}_{front|back}.jpg  (앞·뒤표지 각 약 500장, 총 1,000장)
├── merged_dedup_sample.json   # Label Studio 어노테이션 (7개 클래스 바운딩 박스)
└── README.md
```

어노테이션 클래스(7종): `belly_band`, `belly_band_text`, `title`, `author`, `publisher`, `back_cover_text`, `barcode`

## 🚀 사용법

노트북은 아래처럼 **토큰 없이**(공개 저장소) 데이터를 자동으로 내려받습니다.

```python
from huggingface_hub import hf_hub_download
import zipfile
from pathlib import Path

zip_path = hf_hub_download(
    repo_id="sun09125/belly-band-edu-sample",
    filename="belly_band_edu_sample.zip",
    repo_type="dataset",
)
ROOT = Path("/content/dataset_sample")
with zipfile.ZipFile(zip_path) as zf:
    zf.extractall(ROOT)
```

## ⚖️ 이용 안내 / 라이선스

본 자료는 **비상업적 학술·교육 목적**으로만 이용해 주세요.
도서 표지·띠지의 저작권은 각 출판사·디자이너에게 있으며, 본 자료의 **재배포 또는 상업적 이용은 허용되지 않습니다.**

> 본 표본은 위키독스 매뉴얼의 교육 실습용 일부(약 1,000장)이며, 연구 본편의 전체 데이터(1,206장 어노테이션 → 19,461장 자동 분류)와는 규모가 다릅니다.
