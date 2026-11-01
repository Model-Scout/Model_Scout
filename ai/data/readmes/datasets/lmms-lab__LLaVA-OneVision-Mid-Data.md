---
license: apache-2.0
task_categories:
- text-generation
language:
- zh
- en
tags:
- multimodal
pretty_name: llava-onevision-mid
size_categories:
- 1M<n<10M
---

# Dataset Card for LLaVA-OneVision

> Due to unknow reasons, we are unable to process dataset with large amount into required HF format. So we directly upload the json files and image folders (compressed into tar.gz files).

> You can use the following link to directly download and decompress them.
> https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Mid-Data/tree/main/evol_instruct

We provide the whole details of LLaVA-OneVision Dataset. In this dataset, we include the data splits used in our mid-stage training. For more details, please check our [paper](arxiv.org/abs/2408.03326).

## Dataset Description

- **Curated by:** Bo Li, Kaichen Zhang, Hao Zhang, Yuanhan Zhang, Renrui Zhang, Feng Li, Dong Guo
- **Language(s) (NLP):** English, Chinese
- **License:** Apache License 2.0

## Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Dataset Collection:** We include a few subsets from existing dataset collection [Cambrian](https://huggingface.co/datasets/nyu-visionx/Cambrian-10M), [Cauldron](https://huggingface.co/datasets/HuggingFaceM4/the_cauldron), [UReader](https://arxiv.org/abs/2310.05126). Since we only used a few subsets from these datasets, and applied the cleaning and re-annotation process, we uploaded our processed version of these datasets into our own repository and thank the authors for providing the original datasets.
- **Other Datasets:** For rest single source dataset, such as AI2D, OKVQA, we cite and link the original sources in our paper.

## Uses

This dataset is used for the training of the LLaVA-OneVision Mid-Stage model. We only allow the use of this dataset for academic research and education purpose. For OpenAI GPT-4 generated data, we recommend the users to check the [OpenAI Usage Policy](https://openai.com/policies/usage-policies/).

## Dataset Structure

We expalin the data composition for mid-stage and final-stage at our repo in [**training doc**](https://github.com/LLaVA-VL/LLaVA-NeXT/tree/main/scripts/train#about-the-llava-onevision-data).

## Citation

**BibTeX:**

[More Information Needed]

## Glossary

The dataset collection process is conducted by all of the authors, we thank the Feng Li and Renrui Zhang for providing [LLaVA-M4-Instruct Data](https://huggingface.co/datasets/lmms-lab/M4-Instruct-Data) and Yuanhan for providing the Video datasets (will seperately released later).

After the dataset collection, the cleaning and re-annotation process, including final mixture of the dataset, is conducted by Bo Li and with the great help of Kaichen Zhang.

## Dataset Card Authors

The dataset is curated by the following authors:

Bo Li, Kaichen Zhang, Hao Zhang, Yuanhan Zhang, Renrui Zhang, Feng Li

## Dataset Card Contact

[Bo Li](https://brianboli.com/): drluodian@gmail.com

[Kaichen Zhang](https://www.linkedin.com/in/kaichen-zhang-014b17219/?originalSubdomain=sg)