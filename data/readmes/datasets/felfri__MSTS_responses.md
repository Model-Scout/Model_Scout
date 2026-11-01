---
dataset_info:
  features:
  - name: case_id
    dtype: string
  - name: prompt_type
    dtype: string
  - name: prompt_text
    dtype: string
  - name: unsafe_image_description
    dtype: string
  - name: model
    dtype: string
  - name: response
    dtype: string
  - name: label
    dtype: string
  - name: unsafe_image_url
    dtype: string
  - name: unsafe_image_license
    dtype: string
  - name: unsafe_image_cw
    dtype: string
  - name: unsafe_image
    dtype: image
  splits:
  - name: german
    num_bytes: 64942269
    num_examples: 400
  - name: russian
    num_bytes: 64999315
    num_examples: 400
  - name: chinese
    num_bytes: 64933131
    num_examples: 400
  - name: hindi
    num_bytes: 65056882
    num_examples: 400
  - name: spanish
    num_bytes: 64959369
    num_examples: 400
  - name: italian
    num_bytes: 64924319
    num_examples: 400
  - name: french
    num_bytes: 64958189
    num_examples: 400
  - name: english
    num_bytes: 670190425
    num_examples: 4000
  - name: korean
    num_bytes: 64947110
    num_examples: 400
  - name: arabic
    num_bytes: 64961954
    num_examples: 400
  - name: farsi
    num_bytes: 64980888
    num_examples: 400
  download_size: 1080065706
  dataset_size: 1319853851
configs:
- config_name: default
  data_files:
  - split: german
    path: data/german-*
  - split: russian
    path: data/russian-*
  - split: chinese
    path: data/chinese-*
  - split: hindi
    path: data/hindi-*
  - split: spanish
    path: data/spanish-*
  - split: italian
    path: data/italian-*
  - split: french
    path: data/french-*
  - split: english
    path: data/english-*
  - split: korean
    path: data/korean-*
  - split: arabic
    path: data/arabic-*
  - split: farsi
    path: data/farsi-*
license: cc-by-4.0
language:
- ar
- fr
- en
- de
- zh
- ko
- fa
- hi
- it
- ru
- es
size_categories:
- 1K<n<10K
tags:
- not-for-all-audiences
task_categories:
- image-text-to-text
extra_gated_prompt: >-
  By filling out the form below I understand that MSTS is a derivative
  collection of webscraped images that use individual licenses and their respective 
  terms and conditions apply. Licenses might change over time. I understand that
  all content uses are subject to the terms of use. I understand that reusing
  the content in MSTS might not be legal in all countries/regions and for
  all use cases. I understand that MSTS is mainly targeted toward
  researchers and is meant to be used in research. MSTS authors reserve
  the right to revoke my access to this data. They reserve the right to modify
  this data at any time in accordance with take-down requests. Furthermore, MSTS 
  contains content that may be offensive or upsetting in nature. Topics include, 
  but are not limited to, discriminatory language and discussions of abuse, 
  violence, self-harm, exploitation, and other potentially upsetting subject matter. 
extra_gated_fields:
  Name: text
  Email: text
  Affiliation: text
  Country: text
  I have explicitly checked that downloading MSTS is legal in my jurisdiction, in the country/region where I am located right now, I have also read and accepted the relevant Terms of Use: checkbox
---

# Dataset Card for the MSTS responses Benchmark

Here, you can find our [paper](https://huggingface.co/papers/2501.10057) and [code](https://github.com/paul-rottger/msts-multimodal-safety). Note that for reproducing the exact results, we refer the user to the GitHub repo that provides download and preprocessing scripts for the images. 

This set can be used for multimodal alignment/safety tuning. In this repo, we also provide human labels for prompt-response pairs.

Example usage:
```python
from datasets import load_dataset

ds = load_dataset("felfri/MSTS_responses")

# select label and prompt-response pairs
ds = dataset_dict['german'].map(lambda x: {"prompt_text": x["prompt_text"], "unsafe_image": x["unsafe_image"], "response": x["response"], "label": x["label"]}, remove_columns=['case_id', 'prompt_type', 'unsafe_image_description', 'model', 'unsafe_image_url', 'unsafe_image_license', 'unsafe_image_cw'])

# e.g. train your model to predict the (human) labels given the prompt-image-response triplets
```

## Disclaimer
The MSTS dataset **contains content that may be offensive or upsetting in nature**. Topics include, but are not limited to, **discriminatory language and discussions of abuse, violence, self-harm, exploitation, and other potentially upsetting subject matter**. 
Please only engage with the data in accordance with your own personal risk tolerance. The data are intended for research purposes, especially research that can make models less harmful.


## Citation Information
Please consider citing our work if you use data and/or code from this repository.
```bibtex
@misc{röttger2025mstsmultimodalsafetytest,
      title={MSTS: A Multimodal Safety Test Suite for Vision-Language Models}, 
      author={Paul Röttger and Giuseppe Attanasio and Felix Friedrich and Janis Goldzycher and Alicia Parrish and Rishabh Bhardwaj and Chiara Di Bonaventura and Roman Eng and Gaia El Khoury Geagea and Sujata Goswami and Jieun Han and Dirk Hovy and Seogyeong Jeong and Paloma Jeretič and Flor Miriam Plaza-del-Arco and Donya Rooein and Patrick Schramowski and Anastassia Shaitarova and Xudong Shen and Richard Willats and Andrea Zugarini and Bertie Vidgen},
      year={2025},
      eprint={2501.10057},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.10057}, 
}
```