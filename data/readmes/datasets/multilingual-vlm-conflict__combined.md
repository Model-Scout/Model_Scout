---
license: cc-by-sa-4.0
task_categories:
- visual-question-answering
- image-text-to-text
language:
- en
- ar
- cs
- de
- el
- es
- fa
- fr
- he
- hi
- id
- it
- ja
- ko
- nl
- pl
- pt
- ro
- ru
- tr
- uk
- vi
- zh
tags:
- vlm
- image-text-conflict
- multilingual
- multimodal
size_categories:
- 10K<n<100K
---

# Multilingual VLM Conflict — Combined

All 10 datasets of the **multilingual-vlm-conflict** suite in one place, in English plus 22
languages translated with [CohereLabs/aya-expanse-32b](https://huggingface.co/CohereLabs/aya-expanse-32b)
(Arabic, Czech, German, Greek, Spanish, Persian, French, Hebrew, Hindi, Indonesian, Italian,
Japanese, Korean, Dutch, Polish, Portuguese, Romanian, Russian, Turkish, Ukrainian, Vietnamese,
Simplified Chinese). 10 datasets x 23 languages x 100 examples = 23,000 rows.

Each example pairs an image with a truthful `original_caption` and a `conflicting_caption`
that alters exactly one object or attribute, creating an image-text conflict. The `question`
asks about precisely the element that changes; `image_bias` is the true value grounded in the
image, `text_bias` the altered value asserted by the conflicting caption, and `distractor` a
plausible third option.

## Columns

The schema is the union across the 10 datasets: columns exclusive to some datasets are
`NULL` for rows coming from the others.

| column | description | present in |
|---|---|---|
| `image` | the image (truthful) | all |
| `serial_no` | source identifier (string) | all |
| `original_caption` | caption faithful to the image | all |
| `conflicting_caption` | caption with one object/attribute changed | all |
| `question` | asks about the changed object/attribute | all |
| `image_bias` | true value, grounded in the image | all |
| `text_bias` | altered value asserted by `conflicting_caption` | all |
| `distractor` | plausible third option, different from both biases | all |
| `open-ended_answer` | free-form answer grounded in the image | physics, radiology, DrivingVQA |
| `conflicting_open-ended_answer` | free-form answer following the conflicting caption | physics, radiology, DrivingVQA |
| `conflict_type` | category of the conflict | all |
| `conflict_description` | free-form description of the conflict | 3D-Object |
| `caption_verification` | verification notes for the caption | radiology |
| `file_name` | source file name | pendulum |
| `original_row_id` | row id in the source dataset | pendulum |
| `original_text_bias` | text bias before patching | pendulum |
| `is_patched` | whether the row was patched | pendulum |
| `language` | language of the row's text fields (lowercase English name) | all |
| `dataset_link` | URL of the per-dataset repo this row comes from | all |

## Source datasets

| dataset | link |
|---|---|
| `code-conflict` | https://huggingface.co/datasets/multilingual-vlm-conflict/code-conflict |
| `3D-Object-Conflict` | https://huggingface.co/datasets/multilingual-vlm-conflict/3D-Object-Conflict |
| `physics-conflict` | https://huggingface.co/datasets/multilingual-vlm-conflict/physics-conflict |
| `rpg-conflict` | https://huggingface.co/datasets/multilingual-vlm-conflict/rpg-conflict |
| `sea-vl-conflict` | https://huggingface.co/datasets/multilingual-vlm-conflict/sea-vl-conflict |
| `coco-counterfactual-conflict` | https://huggingface.co/datasets/multilingual-vlm-conflict/coco-counterfactual-conflict |
| `worldcuisines-conflict` | https://huggingface.co/datasets/multilingual-vlm-conflict/worldcuisines-conflict |
| `pendulum-conflict` | https://huggingface.co/datasets/multilingual-vlm-conflict/pendulum-conflict |
| `radiology-conflict` | https://huggingface.co/datasets/multilingual-vlm-conflict/radiology-conflict |
| `DrivingVQA-conflict` | https://huggingface.co/datasets/multilingual-vlm-conflict/DrivingVQA-conflict |

## Licenses

The combination is released under **CC-BY-SA-4.0** (required by the share-alike source
datasets `sea-vl-conflict` and `worldcuisines-conflict`, both CC-BY-SA-4.0;
`coco-counterfactual-conflict` is CC-BY-4.0). See each per-dataset repo for source details.
