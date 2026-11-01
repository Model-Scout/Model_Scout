---
language:
- ko
license: cc-by-nc-sa-4.0
task_categories:
- visual-question-answering
- multiple-choice
task_ids:
- multiple-choice-qa
pretty_name: KorMedMCQA-V
size_categories:
- 1K<n<10K
tags:
- medical
- korean
- multimodal
- vision-language
- multiple-choice
configs:
  - config_name: doctor
    data_files:
      - split: test
        path: data/doctor/test.parquet
      - split: test_full
        path: "data/doctor/test_full-*.parquet"
---

# KorMedMCQA-V: A Multimodal Benchmark for Evaluating Vision-Language Models on the Korean Medical Licensing Examination

[![Paper](https://img.shields.io/badge/Paper-arXiv:2602.13650-B31B1B.svg)](https://arxiv.org/abs/2602.13650)
[![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-FFD21E.svg)](https://huggingface.co/datasets/seongsubae/KorMedMCQA-V)
[![Code](https://img.shields.io/badge/Code-GitHub-181717.svg)](https://github.com/baeseongsu/kormedmcqa_v)
[![Leaderboard](https://img.shields.io/badge/Leaderboard-Website-blue.svg)](https://kormedmcqa-v.github.io/)

KorMedMCQA-V is a multimodal multiple-choice question answering benchmark for evaluating vision-language models on the Korean Medical Licensing Examination. The dataset consists of 1,534 questions with 2,043 associated medical images from Korean Medical Licensing Examinations (2012-2023).

## Table of Contents

- [Dataset Summary](#dataset-summary)
- [Data Format](#data-format)
- [Usage](#usage)
- [License](#license)
- [Citation](#citation)
- [Contact](#contact)

## Dataset Summary

- **Total Questions**: 1,534
- **Total Images**: 2,043 (avg 1.33 images/question)
- **Splits**: `test` (2022-2023, 304 questions), `test_full` (2012-2023, 1,534 questions)
- **Format**: Parquet with base64-encoded images
- **Image Modalities** (9 categories): X-ray (586), Other (554), CT (336), ECG (164), Ultrasound (138), Endoscopy (122), NST (54), PBS (49), MRI (40)

## Data Format

Each sample contains:

| Field | Type | Description |
|--------|--------|-------------|
| `subject` | string | Subject type (always "doctor") |
| `year` | int64 | Year of examination |
| `period` | int64 | Period of examination |
| `q_number` | int64 | Question number |
| `question` | string | Question text |
| `A`, `B`, `C`, `D`, `E` | string | Answer choices |
| `answer` | string | Correct answer (A-E) |
| `images` | string | JSON string of base64-encoded image objects |

### Image Object Structure

`images` field is a JSON string containing an array of image objects with base64-encoded images:

```json
[
  {
    "pic_num": "1",
    "modality": "XRAY",
    "image_base64": "data:image/png;base64,<base64>"
  }
]
```

The `image_base64` field contains a full data URL.

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

dataset = load_dataset("seongsubae/KorMedMCQA-V", name="doctor", split="test_full")

for sample in dataset:
    print(f"Question: {sample['question']}")
    print(f"Answer: {sample['answer']}")
```

### Viewing Images

```python
import json
import base64
import io
from PIL import Image

sample = dataset[0]
images = json.loads(sample["images"])

for img in images:
    data_url = img["image_base64"]
    header, b64_str = data_url.split("base64,", 1)
    img_bytes = base64.b64decode(b64_str)
    pil_image = Image.open(io.BytesIO(img_bytes))
    pil_image.show()
    print(f"Modality: {img['modality']}, Size: {pil_image.size}")
```

### Combining with KorMedMCQA

To evaluate on both text-only and image-dependent questions, combine the `test` split with [sean0042/KorMedMCQA](https://huggingface.co/datasets/sean0042/KorMedMCQA):

- `KorMedMCQA` (text-only) contains 2022-2024 data; filter to **2022-2023** for alignment
- `KorMedMCQA-V` (multimodal) contains 2022-2023 data
- Remove duplicate UID `doctor-2022-2-64` to avoid double-counting

```python
from datasets import load_dataset

# Load both datasets (test split = 2022-2023)
kormedmcqa = load_dataset("sean0042/KorMedMCQA", name="doctor", split="test")
kormedmcqa_v = load_dataset("seongsubae/KorMedMCQA-V", name="doctor", split="test")

# Filter KorMedMCQA for 2022-2023 and remove duplicate UIDs
allowed_years = [2022, 2023]
excluded_uids = ["doctor-2022-2-64"]

kormedmcqa_filtered = [
    s for s in kormedmcqa
    if s["year"] in allowed_years
    and f"{s['subject']}-{s['year']}-{s['period']}-{s['q_number']}" not in excluded_uids
]

print(f"Text-only: {len(kormedmcqa_filtered)}, Multimodal: {len(kormedmcqa_v)}")
```

For evaluation code, see the [GitHub repository](https://github.com/baeseongsu/kormedmcqa_v).

## License

This dataset is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Citation

```bibtex
@dataset{kormedmcqa-v,
  title        = {KorMedMCQA-V: A Multimodal Benchmark for Evaluating Vision-Language Models on the Korean Medical Licensing Examination},
  author       = {Byungjin Choi and Seongsu Bae and Sunjun Kweon and Edward Choi},
  year         = {2025},
  publisher    = {HuggingFace},
  version      = {1.0},
 }
```

## Contact

For questions or issues, please contact Byungjin Choi ([choi328328@ajou.ac.kr](mailto:choi328328@ajou.ac.kr)) or Seongsu Bae ([seongsu@kaist.ac.kr](mailto:seongsu@kaist.ac.kr)).
