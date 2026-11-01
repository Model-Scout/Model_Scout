---
dataset_info:
  features:
  - name: hazard_category
    dtype: string
  - name: hazard_subcategory
    dtype: string
  - name: hazard_subsubcategory
    dtype: string
  - name: case_id
    dtype: string
  - name: case_text
    dtype: string
  - name: unsafe_image_id
    dtype: string
  - name: unsafe_image_description
    dtype: string
  - name: prompt_text
    dtype: string
  - name: prompt_type
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
  - name: english
    num_bytes: 64785154.0
    num_examples: 400
  - name: german
    num_bytes: 67893786.0
    num_examples: 400
  - name: russian
    num_bytes: 67905010.0
    num_examples: 400
  - name: chinese
    num_bytes: 67893108.0
    num_examples: 400
  - name: hindi
    num_bytes: 67919309.0
    num_examples: 400
  - name: spanish
    num_bytes: 67892518.0
    num_examples: 400
  - name: italian
    num_bytes: 67890315.0
    num_examples: 400
  - name: french
    num_bytes: 67895355.0
    num_examples: 400
  - name: korean
    num_bytes: 67898149.0
    num_examples: 400
  - name: arabic
    num_bytes: 67895708.0
    num_examples: 400
  - name: farsi
    num_bytes: 67904398.0
    num_examples: 400
  download_size: 369918366
  dataset_size: 743772810.0
configs:
- config_name: default
  data_files:
  - split: english
    path: data/english-*
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
  - split: korean
    path: data/korean-*
  - split: arabic
    path: data/arabic-*
  - split: farsi
    path: data/farsi-*
license: cc-by-4.0
language:
- en
- ar
- fr
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
task_categories:
- image-text-to-text
---


## Disclaimer
The MSTS dataset **contains content that may be offensive or upsetting in nature**. Topics include, but are not limited to, **discriminatory language and discussions of abuse, violence, self-harm, exploitation, and other potentially upsetting subject matter**. 
Please only engage with the data in accordance with your own personal risk tolerance. The data are intended for research purposes, especially research that can make models less harmful.


# Dataset Card for the MSTS Benchmark

Here, you can find our [paper](https://huggingface.co/papers/2501.10057) and [code](https://github.com/paul-rottger/msts-multimodal-safety). Note that for reproducing the exact results, we refer the user to the GitHub repo that provides download and preprocessing scripts for the images. 

Example usage:
```python
from datasets import load_dataset

ds = load_dataset("felfri/MSTS")

# or select a specific language
lang = 'german'
ds = load_dataset("felfri/MSTS", split=lang)

```


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