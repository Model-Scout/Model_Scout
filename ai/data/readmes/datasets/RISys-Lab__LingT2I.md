---
license: cc-by-nc-sa-4.0
dataset_info:
  features:
  - name: data_id
    dtype: string
  - name: prompt
    dtype: string
  - name: dimension
    dtype: string
  - name: lang
    dtype: string
  - name: dimensions
    sequence: string
  - name: parent_dataset
    sequence: string
  - name: img_id
    dtype: string
  - name: render_text
    dtype: string
  - name: render_layout
    dtype: string
  - name: condition_image
    dtype: image
  splits:
  - name: content_generation
    num_examples: 30000
  - name: text_rendering
    num_examples: 3000
configs:
- config_name: default
  data_files:
  - split: content_generation
    path: data/content_generation-*
  - split: text_rendering
    path: data/text_rendering-*
task_categories:
- text-to-image
language:
- en
- zh
- hi
- es
- ar
- fr
- pt
- ru
- ja
- ko
size_categories:
- 10K<n<100K
---

# LingT2I (TRIG-Multilingual)

LingT2I (TRIG-Multilingual) is a multilingual image-generation benchmark with two subsets:

- `content_generation`: multilingual prompts for evaluating generated image content across dimensions.
- `text_rendering`: multilingual prompts for evaluating rendered text in generated images.

The original JSON files are preserved in this repository for traceability:

- `raw/text-to-image-multilingual.json`
- `raw/trig_multilingual_tr.json`
- `raw/coarse_mask.zip`

The public dataset splits are provided as parquet files under `data/`.

## Load with Hugging Face Datasets

```python
from datasets import load_dataset

ds_cg = load_dataset("RISys-Lab/TRIG-Multilingual", split="content_generation")
ds_tr = load_dataset("RISys-Lab/TRIG-Multilingual", split="text_rendering")

sample_cg = ds_cg[0]
sample_tr = ds_tr[0]

print(sample_cg["prompt"])
print(sample_cg["dimension"], sample_cg["lang"])

print(sample_tr["prompt"])
print(sample_tr["render_text"])
print(sample_tr["condition_image"])  # PIL.Image.Image for text placement
```

## Fields

- `data_id`: sample id.
- `prompt`: generation prompt.
- `dimension`: evaluation dimension or subset marker, such as `IQ-R`, `TA-C`, or `TR`.
- `lang`: language code.
- `dimensions`: original dimension metadata.
- `parent_dataset`: source dataset tags.
- `img_id`: image id when applicable.
- `render_text`: target text for `text_rendering` samples.
- `render_layout`: JSON-encoded layout metadata for `text_rendering` samples.
- `condition_image`: text placement condition image for `text_rendering` samples, decoded as a PIL image by Hugging Face Datasets. It is `null` for `content_generation` samples.

## Notes

- `content_generation` contains 30,000 prompts across 10 languages and 10 dimensions.
- `text_rendering` contains 3,000 prompts across 10 languages.
- `raw/coarse_mask.zip` is kept for traceability; the same placement images are embedded in the `condition_image` column of the `text_rendering` split.
