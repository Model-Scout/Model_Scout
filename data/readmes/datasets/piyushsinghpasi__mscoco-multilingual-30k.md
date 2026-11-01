
---
license: cc-by-nc-4.0
task_categories:
- image-text-to-text
- image-to-text
language:
- en
- fr
- el
- he
- id
- ko
- fa
- ru
- es
- hi
---

# MSCOCO Multilingual Image Caption Dataset (Evaluation Subset)

## Description

This dataset is a **multilingual extension of the MSCOCO 2014 validation set**, consisting of a **random sample of 30,000 images** paired with captions in **10 languages**.

Each image is associated with:
- the original **English MSCOCO caption**
- **machine-translated captions** in multiple target languages

The dataset is intended primarily for **evaluation and analysis** of multilingual and cross-lingual **image–text models**, including vision–language encoders, retrieval systems, and multimodal representation alignment studies.

---

## Dataset Structure

```

.
├── README.md
└── test/
├── images
│   ├── COCO_val2014_000000054123.jpg
│   ├── COCO_val2014_000000012897.jpg
│   └── ...
└── metadata.csv

````

- **Images**: JPEG files from the MSCOCO 2014 validation set
- **Metadata**: CSV file with one row per image
- **Split**: `test` only (evaluation-focused)

---

## Metadata Schema

Each row in `metadata.csv` corresponds to **one image**.

### Columns

| Column name | Description |
|------------|-------------|
| `file_name` | Relative path to the image file |
| `image_name` | Original MSCOCO image filename |
| `caption` | Original English MSCOCO caption |
| `French` | French caption |
| `Greek` | Greek caption |
| `Hebrew` | Hebrew caption |
| `Indonesian` | Indonesian caption |
| `Korean` | Korean caption |
| `Persian` | Persian caption |
| `Russian` | Russian caption |
| `Spanish` | Spanish caption |
| `Hindi` | Hindi caption |

The `file_name` column is used by the Hugging Face Hub to automatically infer the **Image() feature** and render image previews in the dataset viewer.

---

## Dataset Statistics

- **Total images**: 30,000
- **Captions per image**: 1 (per language)
- **Languages**: 10 (1 English + 9 non-English)
- **Source images**: MSCOCO 2014 validation set

---

## Language Coverage

| Language | ISO 639-1 code | Metadata column |
|--------|---------------|----------------|
| English | en | `caption` |
| French | fr | `French` |
| Greek | el | `Greek` |
| Hebrew | he | `Hebrew` |
| Indonesian | id | `Indonesian` |
| Korean | ko | `Korean` |
| Persian | fa | `Persian` |
| Russian | ru | `Russian` |
| Spanish | es | `Spanish` |
| Hindi | hi | `Hindi` |

---

## Intended Use

This dataset is designed for:

- Multilingual image–text retrieval evaluation
- Cross-lingual caption alignment analysis
- Multimodal representation learning research
- Zero-shot and transfer evaluation of vision–language models

It is **not intended for training large-scale generative models**.

---

## Usage

```python
from datasets import load_dataset

ds = load_dataset(
    "piyushsinghpasi/mscoco-multilingual-30k",
    split="test"
)

sample = ds[0]

image = sample["image"]
caption_en = sample["caption"]
caption_fr = sample["French"]
caption_hi = sample["Hindi"]
````

---

## Notes

* All non-English captions are **machine-generated**.
* The dataset preserves the original MSCOCO image identifiers for traceability.
* Only a **random subset** of the validation set is included.
* No additional image preprocessing has been applied.

---

## License & Attribution

* Images and English captions originate from the **MSCOCO dataset**.
* This dataset follows the **CC BY NC-4.0** to comply with translation models used.
* Users must comply with the original MSCOCO terms.

If you use this dataset in academic work, please cite the original MSCOCO dataset and acknowledge this multilingual extension.

---

## Citation
This work is accepted in EACL 2026 Findings.

```
@inproceedings{pasi-2026-multilingual,
    title = "Multilingual-To-Multimodal ({M}2{M}): Unlocking New Languages with Monolingual Text",
    author = "Pasi, Piyush Singh",
    editor = "Demberg, Vera  and
      Inui, Kentaro  and
      Marquez, Llu{\'i}s",
    booktitle = "Findings of the {A}ssociation for {C}omputational {L}inguistics: {EACL} 2026",
    month = mar,
    year = "2026",
    address = "Rabat, Morocco",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.findings-eacl.143/",
    doi = "10.18653/v1/2026.findings-eacl.143",
    pages = "2750--2771",
    ISBN = "979-8-89176-386-9",
    abstract = "Multimodal models excel in English, supported by abundant image-text and audio-text data, but performance drops sharply for other languages due to limited multilingual multimodal resources. Existing solutions rely on machine translation, while advances in multilingual text modeling remain underutilized. We introduce M2M, a lightweight alignment method that learns only a few linear layers{--}using English text alone{--}to map multilingual text embeddings into multimodal space. Despite its simplicity, M2M matches baseline performance in English (94.9{\%} Recall@10) and achieves strong zero-shot transfer (89.5{\%} Recall@10 averaged across 11 languages, 10 unseen) on XTD Text-to-Image retrieval. Qualitative t-SNE visualizations show that multilingual embeddings align tightly with multimodal representations, while weight analysis reveals that the transformation reshapes embedding geometry rather than performing trivial rotations. Beyond image-text retrieval, M2M demonstrates robustness across datasets and tasks, extending to Audio-Text retrieval and Text-to-Image generation. We release [code and checkpoints](https://github.com/piyushsinghpasi/M2M) along with multilingual evaluation datasets: [MSCOCO Multilingual 30K](https://huggingface.co/datasets/piyushsinghpasi/mscoco-multilingual-30k), [AudioCaps Multilingual](https://huggingface.co/datasets/piyushsinghpasi/audiocaps-multilingual), and [Clotho Multilingual](https://huggingface.co/datasets/piyushsinghpasi/clotho-multilingual)."
}
```


