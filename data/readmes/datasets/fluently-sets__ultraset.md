---
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: text
    dtype: string
  - name: system
    dtype: string
  - name: response
    dtype: string
  - name: source
    dtype: string
  - name: score
    dtype: float64
  splits:
  - name: train
    num_bytes: 785427316
    num_examples: 785032
  download_size: 419380306
  dataset_size: 785427316
license: other
license_name: multi-license
license_link: https://huggingface.co/datasets/fluently-sets/ultraset#rights-to-the-dataset-and-authors
task_categories:
- text-generation
- text2text-generation
- text-classification
- question-answering
- translation
language:
- en
- ru
- fr
- it
- zh
- ko
- de
- es
- code
size_categories:
- 100K<n<1M
tags:
- text
- code
- reflection
- reasoning
- logic
- medical
- biology
- math
- finance
- CoT
- instruct
- cleaned
- alpaca
- orca
- universal
- all-in-one
- multiset
- ultraset
- gpt
---
# Ultraset - all-in-one dataset for SFT training in Alpaca format

## About the dataset

This dataset is designed to facilitate training and retraining of LLM models using the SFT method in the Alpaca format.

### Brief information

- Number of rows: 785K
- Type of dataset files: parquet
- Type of dataset: text, alpaca
- Languages:
- English
- Russian
- French
- Italian
- Spanish
- German
- Chinese
- Korean
- License: flexible multi-license, main - MIT

### The problem this dataset solves

We found out that when regular users want to train LLM on some datasets and make the model better, their eyes run wide because of the many different datasets with different approaches. This dataset combines everything you need for basic training: writing texts, mathematics and code, biology and medicine, finance, CoT data, multilingual data.

### How to use the dataset for training optimally

First, for effective training on SFTTrainer, use only the columns: instruction, input, output (these are rows), other columns are rarely useful.

Second, use somewhere around 1-3 epochs for training, this will be more than enough.

Third, there is no DPO or Instruct data, that is, the dataset is suitable for training all types of LLM models.

### What will the dataset give to my model?

- Improving skills in writing/editing/analyzing texts
- Improving skills in mathematics and coding
- Improving knowledge in biology, medicine and finance
- Improving knowledge in various popular languages
and much more.

### Rights to the dataset and authors

Fluently Datasets ([@fluently-sets](https://hf.co/fluently-sets)) and ehristoforu ([@ehristoforu](https://hf.co/ehristoforu)) do not claim full rights to the data in the dataset. This dataset was obtained by merging many Alpaca datasets from different authors. Because of this, the license section says - multi-license, since each dataset that participated in the merger has its own license, different problems may arise, but the main one for the project is a fairly universal MIT license.

#### Datasets that participated in the merger:

- [vicgalle/alpaca-gpt4](https://hf.co/datasets/vicgalle/alpaca-gpt4)
- [yahma/alpaca-cleaned](https://hf.co/datasets/yahma/alpaca-cleaned)
- [gbharti/finance-alpaca](https://hf.co/datasets/gbharti/finance-alpaca)
- [ewof/code-alpaca-instruct-unfiltered](https://hf.co/datasets/ewof/code-alpaca-instruct-unfiltered)
- [causal-lm/cot_alpaca_gpt4](https://hf.co/datasets/causal-lm/cot_alpaca_gpt4)
- [pankajmathur/alpaca_orca](https://hf.co/datasets/pankajmathur/alpaca_orca)
- [Vezora/Wizard_Math_Alpaca](https://hf.co/datasets/Vezora/Wizard_Math_Alpaca)
- [Kabatubare/medical-alpaca](https://hf.co/datasets/Kabatubare/medical-alpaca)
- [mlabonne/FineTome-Alpaca-100k](https://hf.co/datasets/mlabonne/FineTome-Alpaca-100k)
- [gbharti/wealth-alpaca_lora](https://hf.co/datasets/gbharti/wealth-alpaca_lora)
- [d0rj/alpaca-cleaned-ru](https://hf.co/datasets/d0rj/alpaca-cleaned-ru)
- [pinzhenchen/alpaca-cleaned-fr](https://hf.co/datasets/pinzhenchen/alpaca-cleaned-fr)
- [shibing624/alpaca-zh](https://hf.co/datasets/shibing624/alpaca-zh)
- [bertin-project/alpaca-spanish](https://hf.co/datasets/bertin-project/alpaca-spanish)
- [royboy0416/ko-alpaca](https://hf.co/datasets/royboy0416/ko-alpaca)
- [efederici/alpaca-gpt4-it](https://hf.co/datasets/efederici/alpaca-gpt4-it)
- [mayflowergmbh/alpaca-gpt4_de](https://hf.co/datasets/mayflowergmbh/alpaca-gpt4_de)

Thank you very much to all these authors)