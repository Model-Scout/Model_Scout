---
license: apache-2.0
task_categories:
- text-generation
language:
- ru
- ar
- en
- zh
- de
- fr
- es
- pt
- ja
- ko
tags:
- linux
- shell
- commands
- terminal
- multilingual
- development
- system-administration
pretty_name: LinLM
size_categories:
- 10K<n<100K
configs:
- config_name: ar
  data_files:
  - split: train
    path: ar/train-*
- config_name: ch
  data_files:
  - split: train
    path: ch/train-*
- config_name: de
  data_files:
  - split: train
    path: de/train-*
- config_name: default
  data_files:
  - split: train
    path: data/train-*
- config_name: eng
  data_files:
  - split: train
    path: eng/train-*
- config_name: es
  data_files:
  - split: train
    path: es/train-*
- config_name: fr
  data_files:
  - split: train
    path: fr/train-*
- config_name: ja
  data_files:
  - split: train
    path: ja/train-*
- config_name: ko
  data_files:
  - split: train
    path: ko/train-*
- config_name: pt
  data_files:
  - split: train
    path: pt/train-*
- config_name: ru
  data_files:
  - split: train
    path: ru/train-*
dataset_info:
- config_name: ar
  features:
  - name: ar
    dtype: string
  - name: completion
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 517865
    num_examples: 6525
  download_size: 203991
  dataset_size: 517865
- config_name: ch
  features:
  - name: ch
    dtype: string
  - name: completion
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 430262
    num_examples: 6525
  download_size: 184750
  dataset_size: 430262
- config_name: de
  features:
  - name: de
    dtype: string
  - name: completion
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 464172
    num_examples: 6525
  download_size: 193093
  dataset_size: 464172
- config_name: default
  features:
  - name: eng
    dtype: string
  - name: ru
    dtype: string
  - name: ch
    dtype: string
  - name: de
    dtype: string
  - name: fr
    dtype: string
  - name: es
    dtype: string
  - name: pt
    dtype: string
  - name: ja
    dtype: string
  - name: ko
    dtype: string
  - name: ar
    dtype: string
  - name: completion
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 2299337
    num_examples: 6525
  download_size: 983154
  dataset_size: 2299337
- config_name: eng
  features:
  - name: eng
    dtype: string
  - name: completion
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 434014
    num_examples: 6525
  download_size: 185617
  dataset_size: 434014
- config_name: es
  features:
  - name: es
    dtype: string
  - name: completion
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 470435
    num_examples: 6525
  download_size: 193111
  dataset_size: 470435
- config_name: fr
  features:
  - name: fr
    dtype: string
  - name: completion
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 482341
    num_examples: 6525
  download_size: 197298
  dataset_size: 482341
- config_name: ja
  features:
  - name: ja
    dtype: string
  - name: completion
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 505936
    num_examples: 6525
  download_size: 198712
  dataset_size: 505936
- config_name: ko
  features:
  - name: ko
    dtype: string
  - name: completion
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 453690
    num_examples: 6525
  download_size: 188648
  dataset_size: 453690
- config_name: pt
  features:
  - name: pt
    dtype: string
  - name: completion
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 467911
    num_examples: 6525
  download_size: 192655
  dataset_size: 467911
- config_name: ru
  features:
  - name: ru
    dtype: string
  - name: completion
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: train
    num_bytes: 571849
    num_examples: 6525
  download_size: 213846
  dataset_size: 571849
---

## LinLM Dataset

A curated synthetic dataset for Linux command inference

Natural language description -> shell commands

Features: 

- Supports 10 languages
- Arch Linux commands recognition
- Fine-tune LLM for development, system administration, file operations, Git, Docker, and more


## Usage

```python
from datasets import load_dataset

dataset = load_dataset("missvector/linux-commands")

def format_for_training(example):
    return {
        "prompt": f"Convert to Linux command: {example['eng']}",
        "completion": example['completion']
    }

training_data = dataset['train'].map(format_for_training)
```

## Out-of-Scope Use
- Not for production deployment without additional validation
- Commands should be reviewed before execution

## Related Projects

- [llama-dynamic-context](https://github.com/vifirsanova/llama-dynamic-context) - command inference tool tested with this dataset

## Citation

If you use this dataset in your research, please cite:

```bibtex
@misc{linuxcommands2025,
  author = {V. Firsanova},
  title = {LinLM Dataset},
  year = {2025},
  publisher = {Hugging Face Datasets},
  howpublished = {\url{https://huggingface.co/datasets/missvector/linux-commands}}
}
```