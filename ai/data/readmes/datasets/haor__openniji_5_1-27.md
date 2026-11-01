---
task_categories:
  - text-to-image
language:
  - en
  - ja
  - ko
tags:
  - anime
  - dataset
  - Nijijourney
  - Midjourney
  - discord
size_categories:
  - 100K<n<1M
license: cc-by-nc-4.0
---

# Dataset Card for haor/openniji_5_1-27

## Table of Contents
- [Dataset Description](#dataset-description)
- [Dataset Information](#dataset-information)
- [Dataset Statistics](#dataset-statistics)
- [Usage](#usage)
- [Changelog](#changelog)

<a name="dataset-description"></a>
## Dataset Description

The openniji_5_1-27 dataset is a subset of the OpenNiji-Dataset provided by ShoukanLabs. This subset, comprising of image-text pairs collected after May 1st. The images are compressed to 95% using the webp format, and the associated texts are included as prompts.
![Counter_over_time](https://huggingface.co/datasets/haor/openniji_5_1-27/resolve/main/counter_over_time.jpg)

<a name="dataset-information"></a>
## Dataset Information

- **Format:** 
    - Image: WebP (95% compressed)
    - Text: txt (containing prompt content)
- **Date of Collection:** Collected after May 1st
- **License:** Please check [ShoukanLabs/OpenNiji-Dataset](https://huggingface.co/datasets/ShoukanLabs/OpenNiji-Dataset) for more details

<a name="dataset-statistics"></a>
## Dataset Statistics

Information in this section depends on the actual number and details of the collected data.

- Total number of image-text pairs: 118261
- Image-text pairs with aesthetic score greater than 0.9: 51430
- Image-text pairs with aesthetic scores ranging from 0.8 to 0.9: 27989
- ![Distribution of Aesthetic Scores](https://huggingface.co/datasets/haor/openniji_5_1-27/resolve/main/Distribution_of_Aesthetic_Scores.jpg)
  

<a name="usage"></a>
## Usage

Source dataset: [ShoukanLabs/OpenNiji-Dataset](https://huggingface.co/datasets/ShoukanLabs/OpenNiji-Dataset)

This dataset: [haor/openniji_5_1-27](https://huggingface.co/datasets/haor/openniji_5_1-27)

For usage rights, permissions, citations and more, please refer to the original dataset repository: [ShoukanLabs/OpenNiji-Dataset](https://huggingface.co/datasets/ShoukanLabs/OpenNiji-Dataset)

<a name="changelog"></a>
## Changelog

- Version 1.0: Initial release, containing data collected from May 1st to May 27th.

This dataset card was last updated on: July 31, 2023
