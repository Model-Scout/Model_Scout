---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: image_id
    dtype: int32
  - name: objects
    struct:
    - name: bbox
      sequence:
        sequence: float32
        length: 4
    - name: category
      sequence:
        class_label:
          names:
            '0': text
            '1': hard_negative
  splits:
  - name: train
    num_bytes: 59223001756.432
    num_examples: 514144
  - name: valid
    num_bytes: 16962523909.764
    num_examples: 147191
  - name: test
    num_bytes: 8495809053.7
    num_examples: 73725
  download_size: 84180821949
  dataset_size: 84681334719.896
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: valid
    path: data/valid-*
  - split: test
    path: data/test-*
tags:
- not-for-all-audiences
- datasets
- croissant
- ultralytics
task_categories:
- object-detection
size_categories:
- 100K<n<1M
license: cc-by-nc-sa-4.0
language:
- zh
- ko
- ja
- en
- ru
pretty_name: AnimeText
---

# AnimeText: A Large-scale Dataset for Robust Complex Anime Scene Text Detection


<div style="text-align: center;">
  <img src="figs/examples.png" width="100%">
  <img src="figs/det_example.png" width="100%">
  <b>Figure 1：</b> Dataset examples.
</div>

## Dataset Summary

AnimeText is a large-scale dataset for anime scene text detection, containing 735K images and 4.2M annotated text blocks. Unlike existing natural scene or document-centric text detection datasets, AnimeText focuses on text in anime scenes, which typically features diverse styles, irregular arrangements, and can be easily confused with complex visual elements such as symbols and decorative patterns. The AnimeText dataset includes multilingual text (English, Chinese, Japanese, Korean, Russian) and provides hierarchical annotations and hard negative samples tailored for anime scenarios.

We trained YOLO12 models on this dataset, and shared them [here](https://huggingface.co/deepghs/AnimeText_yolo). We also provided [online demo](https://huggingface.co/spaces/deepghs/AnimeText_yolo) for you to try them quickly.

Our paper has been published at https://arxiv.org/abs/2510.07951

## Features

- **Large-scale Diversity**: Contains 735K high-resolution anime images and 4.2M annotated text blocks
- **Multilingual Support**: Covers English, Chinese, Japanese, Korean, Russian, and other languages
- **Hierarchical Annotations**: Provides multi-granularity text area annotations for more precise text detection
- **Hard Negative Samples**: Includes annotations of hard negative samples that are easily confused with text, improving model robustness
- **Polygon Annotations**: Uses segmentation models to provide accurate polygon annotations for irregular text



<div style="display: flex; justify-content: center; gap: 20px;">
  <img src="figs/bbox_count_per_image.png" width="48%">
  <img src="figs/heatmap_640_animetext.png" width="48%">
</div>
<div style="text-align: center;">
  <b>Figure 2：</b> Dataset statistics of bounding box count and sptial distribution.
</div>

## Dataset Structure

### Data Instances

A data instance includes an image and its corresponding text annotations:

```python
{
  'image': Image (image data),
  'image_id': int32 (image id),
  'objects': {
        # The bbox is the normalized value
        'bbox': [float32 (center x), float32 (center y), float32 (width), float32 (height)],
        'category': string (class id: {0:text, 1: hard negative sample}),
    },
}
```

### Data Splits

The dataset is divided into training, validation, and test sets:

| Split | Number of Images | Number of Text Instances |
|-------|------------------|--------------------------|
| Train | 514,144 | 3,228,144 |
| Validation | 147,191 | 922,758 |
| Test | 73,725 | 88,320 |
| Total | 735,060 | 4,239,222 |

## Supported Tasks

- **Text Detection**: The dataset can be used to train and evaluate text detection models in anime scenes.
- **Hard Negative Sample Discrimination**: The hard negative samples in the dataset can be used to train models to distinguish between real text and text-like patterns.

## Usage

### With datasets

Install `datasets` with vision support:
```shell
pip install datasets[vision]
```

Load AnimeText with `datasets`:
```python
from datasets import load_dataset, Image
dataset = load_dataset("deepghs/AnimeText", split="train") # split choice in ['train', 'valid', 'test']

# data example
example = dataset[0]
image = example['image']  # PIL.Image
bbox = example['objects']['bbox']
# in category, 0 means positive samples, 1 means hard negative samples
category = example['objects']['category']

# iterate dataset
for data in dataset:
    ...

```

### With ultralytics

This dataset can also be used with [ultralytics framework](https://www.ultralytics.com/) with the following steps:

1. Download the zip files inside the [./ultralytics subdirectory in this repository.](https://huggingface.co/datasets/deepghs/AnimeText/tree/main/ultralytics)
2. Extract them with `unzip -o` command to the same directory (and you can simply ignore the overwriting reminder because all these 5 splits are sharing the same `data.yaml` file)
3. Train on this dataset with [ultralytics training CLI](https://docs.ultralytics.com/modes/train/#usage-examples), 

## Benchmarks

Cross-dataset benchmarking was conducted using state-of-the-art text detection methods on AnimeText. Experimental results demonstrate that models trained on AnimeText outperform those trained on existing datasets in anime scenes.

| Method                 | Train Dataset | Test Dataset | Precision | Recall | F1-score | mAP<sub>50:95</sub> |
|------------------------|---------------|--------------|-----------|--------|----------|----------------------|
| YOLO v11              | ICDAR15       | ICDAR15      | 0.657     | 0.495  | 0.565    | 0.291                |
| YOLO v11              | AnimeText     | ICDAR15      | 0.187     | 0.31   | 0.233    | 0.083                |
| YOLO v11              | ICDAR15       | AnimeText    | 0.0629    | 0.106  | 0.079    | 0.01                 |
| YOLO v11              | AnimeText     | AnimeText    | 0.878     | 0.825  | 0.851    | 0.806                |
| Bridging Text Spotting| ICDAR15       | AnimeText    | 0.035     | 0.189  | 0.056    | -                    |

## Acknowledgements

We thank all annotators and volunteers who participated in building the AnimeText dataset. This research was supported by [DeepGHS](http://deepghs.org/).