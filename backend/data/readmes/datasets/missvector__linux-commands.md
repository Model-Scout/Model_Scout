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
  - split: validation
    path: ar/validation-*
  - split: test
    path: ar/test-*
- config_name: ch
  data_files:
  - split: train
    path: ch/train-*
  - split: validation
    path: ch/validation-*
  - split: test
    path: ch/test-*
- config_name: de
  data_files:
  - split: train
    path: de/train-*
  - split: validation
    path: de/validation-*
  - split: test
    path: de/test-*
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
- config_name: eng
  data_files:
  - split: train
    path: eng/train-*
  - split: validation
    path: eng/validation-*
  - split: test
    path: eng/test-*
- config_name: es
  data_files:
  - split: train
    path: es/train-*
  - split: validation
    path: es/validation-*
  - split: test
    path: es/test-*
- config_name: fr
  data_files:
  - split: train
    path: fr/train-*
  - split: validation
    path: fr/validation-*
  - split: test
    path: fr/test-*
- config_name: ja
  data_files:
  - split: train
    path: ja/train-*
  - split: validation
    path: ja/validation-*
  - split: test
    path: ja/test-*
- config_name: ko
  data_files:
  - split: train
    path: ko/train-*
  - split: validation
    path: ko/validation-*
  - split: test
    path: ko/test-*
- config_name: pt
  data_files:
  - split: train
    path: pt/train-*
  - split: validation
    path: pt/validation-*
  - split: test
    path: pt/test-*
- config_name: ru
  data_files:
  - split: train
    path: ru/train-*
  - split: validation
    path: ru/validation-*
  - split: test
    path: ru/test-*
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
    num_bytes: 413739.2
    num_examples: 5220
  - name: validation
    num_bytes: 51677.76980842912
    num_examples: 652
  - name: test
    num_bytes: 51757.030191570884
    num_examples: 653
  download_size: 270763
  dataset_size: 517174.0
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
    num_bytes: 343656.8
    num_examples: 5220
  - name: validation
    num_bytes: 42924.18268199234
    num_examples: 652
  - name: test
    num_bytes: 42990.01731800766
    num_examples: 653
  download_size: 244571
  dataset_size: 429571.0
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
    num_bytes: 370784.8
    num_examples: 5220
  - name: validation
    num_bytes: 46312.584214559385
    num_examples: 652
  - name: test
    num_bytes: 46383.61578544061
    num_examples: 653
  download_size: 254808
  dataset_size: 463481.0
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
    num_bytes: 1838916.8
    num_examples: 5220
  - name: validation
    num_bytes: 229688.45854406132
    num_examples: 652
  - name: test
    num_bytes: 230040.7414559387
    num_examples: 653
  download_size: 1291415
  dataset_size: 2298646.0
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
    num_bytes: 346658.4
    num_examples: 5220
  - name: validation
    num_bytes: 43299.09517241379
    num_examples: 652
  - name: test
    num_bytes: 43365.50482758621
    num_examples: 653
  download_size: 243923
  dataset_size: 433323.0
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
    num_bytes: 375795.2
    num_examples: 5220
  - name: validation
    num_bytes: 46938.40429118774
    num_examples: 652
  - name: test
    num_bytes: 47010.39570881226
    num_examples: 653
  download_size: 253784
  dataset_size: 469744.00000000006
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
    num_bytes: 385320.0
    num_examples: 5220
  - name: validation
    num_bytes: 48128.09195402299
    num_examples: 652
  - name: test
    num_bytes: 48201.90804597701
    num_examples: 653
  download_size: 259023
  dataset_size: 481650.0
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
    num_bytes: 404196.0
    num_examples: 5220
  - name: validation
    num_bytes: 50485.783908045974
    num_examples: 652
  - name: test
    num_bytes: 50563.216091954026
    num_examples: 653
  download_size: 268078
  dataset_size: 505245.0
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
    num_bytes: 362399.2
    num_examples: 5220
  - name: validation
    num_bytes: 45265.18743295019
    num_examples: 652
  - name: test
    num_bytes: 45334.61256704981
    num_examples: 653
  download_size: 250956
  dataset_size: 452999.0
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
    num_bytes: 373776.0
    num_examples: 5220
  - name: validation
    num_bytes: 46686.197701149424
    num_examples: 652
  - name: test
    num_bytes: 46757.802298850576
    num_examples: 653
  download_size: 252869
  dataset_size: 467220.0
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
    num_bytes: 456926.4
    num_examples: 5220
  - name: validation
    num_bytes: 57072.03310344827
    num_examples: 652
  - name: test
    num_bytes: 57159.566896551725
    num_examples: 653
  download_size: 284902
  dataset_size: 571158.0
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