---
dataset_info:
  features:
  - name: image_uid
    dtype: string
  - name: caption_uid
    list: string
  - name: image
    dtype: image
  - name: caption_ar
    list: string
  - name: caption_bn
    list: string
  - name: caption_cs
    list: string
  - name: caption_da
    list: string
  - name: caption_de
    list: string
  - name: caption_el
    list: string
  - name: caption_en
    list: string
  - name: caption_es
    list: string
  - name: caption_fa
    list: string
  - name: caption_fi
    list: string
  - name: caption_fil
    list: string
  - name: caption_fr
    list: string
  - name: caption_he
    list: string
  - name: caption_hi
    list: string
  - name: caption_hr
    list: string
  - name: caption_hu
    list: string
  - name: caption_id
    list: string
  - name: caption_it
    list: string
  - name: caption_ja
    list: string
  - name: caption_ko
    list: string
  - name: caption_mi
    list: string
  - name: caption_nl
    list: string
  - name: caption_no
    list: string
  - name: caption_pl
    list: string
  - name: caption_pt
    list: string
  - name: caption_ro
    list: string
  - name: caption_ru
    list: string
  - name: caption_sv
    list: string
  - name: caption_sw
    list: string
  - name: caption_te
    list: string
  - name: caption_th
    list: string
  - name: caption_tr
    list: string
  - name: caption_uk
    list: string
  - name: caption_vi
    list: string
  - name: caption_zh
    list: string
  splits:
  - name: train
    num_bytes: 266429450981
    num_examples: 2855284
  - name: validation
    num_bytes: 1136128822
    num_examples: 13443
  download_size: 266314494059
  dataset_size: 267565579803
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
task_categories:
- text-to-image
- image-to-text
- translation
language:
- ar
- bn
- da
- de
- cs
- el
- en
- es
- fa
- fi
- fr
- he
- hi
- hr
- hu
- id
- it
- ja
- ko
- mi
- nl
- pl
- pt
- qu
- ro
- ru
- sv
- sw
- te
- th
- tr
- uk
- vi
- zh
tags:
- cc3m-35l
- cc3m35l
- multilingual
---
## Team and Homepage
- **Official Website**: [https://aienthusiasm.vn](https://aienthusiasm.vn)
- **Hugging Face Organization**: [https://huggingface.co/ai-enthusiasm-community](https://huggingface.co/ai-enthusiasm-community)

## Contact
If you encounter any issues with the dataset or have any inquiries, please feel free to reach out to us via email at: [aienthusiasm.team@gmail.com](mailto:aienthusiasm.team@gmail.com)

## Dataset Structure
The dataset is provided in a flattened tabular format, optimized for the Hugging Face Dataset Viewer and high-speed Parquet processing.

### Data Fields
- `image_uid`: The identification string.
- `caption_uid`: List of unique identifiers for each caption, following the format `{image_uid}_{comment_number}`.
- `image`: A Image object containing the visual data.
- `caption_<lang>`: The description in different languages.

## Usage
The dataset can be accessed directly using the Hugging Face `datasets` library:
```python
from datasets import load_dataset

dataset = load_dataset("ai-enthusiasm-community/CC3M-35L")

# Accessing the first sample
print(dataset['train'][0])
```

## Citation
```
@misc{thapliyal2022crossmodal,
  title={Crossmodal-3600: A Massively Multilingual Multimodal Evaluation Dataset},
  author={Thapliyal, Ashish V. and Pont-Tuset, Jordi and Chen, Xi and Soricut, Radu},
  year={2022},
  eprint={2205.12522},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}
```