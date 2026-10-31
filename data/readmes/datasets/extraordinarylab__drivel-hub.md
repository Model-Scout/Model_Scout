---
language:
- en
- zh
- fr
- es
- ko
- ja
size_categories:
- 1K<n<10K
task_categories:
- text-classification
- question-answering
- zero-shot-classification
- text-generation
license: cc-by-nc-4.0
dataset_info:
- config_name: binary-classification
  features:
  - name: text
    dtype: string
  - name: label
    dtype: string
  splits:
  - name: test
    num_bytes: 181216
    num_examples: 1200
  download_size: 120551
  dataset_size: 181216
- config_name: multi-label-classification
  features:
  - name: text
    dtype: string
  - name: label
    sequence: string
  splits:
  - name: test
    num_bytes: 86390
    num_examples: 600
  download_size: 57404
  dataset_size: 86390
- config_name: multiple-choice-english-easy
  features:
  - name: text
    dtype: string
  - name: choices
    sequence: string
  - name: answer
    dtype: string
  - name: answer_index
    dtype: int64
  splits:
  - name: test
    num_bytes: 838718
    num_examples: 600
  download_size: 475793
  dataset_size: 838718
- config_name: multiple-choice-english-hard
  features:
  - name: text
    dtype: string
  - name: choices
    sequence: string
  - name: answer
    dtype: string
  - name: answer_index
    dtype: int64
  splits:
  - name: test
    num_bytes: 655572
    num_examples: 600
  download_size: 371994
  dataset_size: 655572
- config_name: multiple-choice-simplified-chinese-easy
  features:
  - name: text
    dtype: string
  - name: choices
    sequence: string
  - name: answer
    dtype: string
  - name: answer_index
    dtype: int64
  splits:
  - name: test
    num_bytes: 759119
    num_examples: 600
  download_size: 486840
  dataset_size: 759119
- config_name: multiple-choice-simplified-chinese-hard
  features:
  - name: text
    dtype: string
  - name: choices
    sequence: string
  - name: answer
    dtype: string
  - name: answer_index
    dtype: int64
  splits:
  - name: test
    num_bytes: 588936
    num_examples: 600
  download_size: 380082
  dataset_size: 588936
- config_name: multiple-choice-traditional-chinese-easy
  features:
  - name: text
    dtype: string
  - name: choices
    sequence: string
  - name: answer
    dtype: string
  - name: answer_index
    dtype: int64
  splits:
  - name: test
    num_bytes: 759662
    num_examples: 600
  download_size: 481749
  dataset_size: 759662
- config_name: multiple-choice-traditional-chinese-hard
  features:
  - name: text
    dtype: string
  - name: choices
    sequence: string
  - name: answer
    dtype: string
  - name: answer_index
    dtype: int64
  splits:
  - name: test
    num_bytes: 589121
    num_examples: 600
  download_size: 374855
  dataset_size: 589121
- config_name: narrative-writing-english
  features:
  - name: text
    dtype: string
  - name: narrative
    dtype: string
  splits:
  - name: test
    num_bytes: 269719
    num_examples: 600
  download_size: 171007
  dataset_size: 269719
- config_name: narrative-writing-simplified-chinese
  features:
  - name: text
    dtype: string
  - name: narrative
    dtype: string
  splits:
  - name: test
    num_bytes: 254956
    num_examples: 600
  download_size: 176282
  dataset_size: 254956
- config_name: narrative-writing-traditional-chinese
  features:
  - name: text
    dtype: string
  - name: narrative
    dtype: string
  splits:
  - name: test
    num_bytes: 255314
    num_examples: 600
  download_size: 175665
  dataset_size: 255314
configs:
- config_name: binary-classification
  data_files:
  - split: test
    path: binary-classification/test-*
- config_name: multi-label-classification
  data_files:
  - split: test
    path: multi-label-classification/test-*
- config_name: multiple-choice-english-easy
  data_files:
  - split: test
    path: multiple-choice-english-easy/test-*
- config_name: multiple-choice-english-hard
  data_files:
  - split: test
    path: multiple-choice-english-hard/test-*
- config_name: multiple-choice-simplified-chinese-easy
  data_files:
  - split: test
    path: multiple-choice-simplified-chinese-easy/test-*
- config_name: multiple-choice-simplified-chinese-hard
  data_files:
  - split: test
    path: multiple-choice-simplified-chinese-hard/test-*
- config_name: multiple-choice-traditional-chinese-easy
  data_files:
  - split: test
    path: multiple-choice-traditional-chinese-easy/test-*
- config_name: multiple-choice-traditional-chinese-hard
  data_files:
  - split: test
    path: multiple-choice-traditional-chinese-hard/test-*
- config_name: narrative-writing-english
  data_files:
  - split: test
    path: narrative-writing-english/test-*
- config_name: narrative-writing-simplified-chinese
  data_files:
  - split: test
    path: narrative-writing-simplified-chinese/test-*
- config_name: narrative-writing-traditional-chinese
  data_files:
  - split: test
    path: narrative-writing-traditional-chinese/test-*
arxiv: 2509.03867
---

# Drivelology Multilingual Dataset

Paper: [Drivel-ology: Challenging LLMs with Interpreting Nonsense with Depth](https://huggingface.co/papers/2509.03867)

Code / Project Page: [https://github.com/ExtraOrdinaryLab/drivelology](https://github.com/ExtraOrdinaryLab/drivelology)

The DrivelHub Dataset is a curated collection of linguistic samples, characterized as "nonsense with depth" (utterances that are syntactically coherent yet pragmatically paradoxical, emotionally loaded, or rhetorically subversive), designed to support research in humor detection and other forms of playful or deceptive language constructs. 
Each entry contains a short "Drivelology" style text sample, categorised under one of five nuanced rhetorical types: inversion, misdirection, paradox, switchbait, wordplay.

The dataset supports six languages: Simplified Chinese (zh), Traditional Chinese (zh-hant), Korean (ko), Japanese (ja), Spanish (es), English (en), and French (fr).

### Tasks

The Drivelology benchmark evaluates models on four main tasks, as described in the accompanying paper and code repository:

1.  **Multiple-Choice Question Answering (MCQA):** This task asks models to pick the correct narrative for a Drivelology sample from several options. It includes Easy and Hard versions.
2.  **Detection:** This is a binary classification task where LLMs identify whether a text is Drivelology or not.
3.  **Narrative Writing:** This task assesses the model's ability to generate a coherent and meaningful implicit narrative that underlies a given Drivelology sample.
4.  **Multi-label Tagging:** Models are asked to assign one or more rhetorical categories (Misdirection, Paradox, Switchbait, Inversion, Wordplay) to each Drivelology sample.

### Sample Usage

To run the evaluation tasks or interact with the dataset as described in the paper, please refer to the [official GitHub repository](https://github.com/ExtraOrdinaryLab/drivelology).

> **Update:** Drivelology is now officially supported by `evalscope`! This is now the recommended way to run evaluations. Please refer to [here](https://github.com/modelscope/evalscope/pull/927). The original execution scripts are kept for legacy purposes.

# Citing

Accepted for an oral presentation at EMNLP 2025. Find our paper at [arxiv](https://www.arxiv.org/abs/2509.03867).

```bibtex
@misc{wang2025drivelologychallengingllmsinterpreting,
      title={Drivel-ology: Challenging LLMs with Interpreting Nonsense with Depth}, 
      author={Yang Wang and Chenghao Xiao and Chia-Yi Hsiao and Zi Yan Chang and Chi-Li Chen and Tyler Loakman and Chenghua Lin},
      year={2025},
      eprint={2509.03867},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2509.03867}, 
}

@inproceedings{wang-etal-2025-drivel,
    title = "Drivel-ology: Challenging {LLM}s with Interpreting Nonsense with Depth",
    author = "Wang, Yang  and
      Xiao, Chenghao  and
      Hsiao, Chia-Yi  and
      Chang, Zi Yan  and
      Chen, Chi-Li  and
      Loakman, Tyler  and
      Lin, Chenghua",
    editor = "Christodoulopoulos, Christos  and
      Chakraborty, Tanmoy  and
      Rose, Carolyn  and
      Peng, Violet",
    booktitle = "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.emnlp-main.1177/",
    doi = "10.18653/v1/2025.emnlp-main.1177",
    pages = "23085--23107",
    ISBN = "979-8-89176-332-6",
    abstract = "We introduce Drivelology, a unique linguistic phenomenon characterised as ``nonsense with depth'' - utterances that are syntactically coherent yet pragmatically paradoxical, emotionally loaded, or rhetorically subversive. While such expressions may resemble surface-level nonsense, they encode implicit meaning requiring contextual inference, moral reasoning, or emotional interpretation. We find that current large language models (LLMs), despite excelling at many natural language processing (NLP) tasks, consistently fail to grasp the layered semantics of Drivelological text. To investigate this, we construct a benchmark dataset of over 1,200+ meticulously curated and diverse examples across English, Mandarin, Spanish, French, Japanese, and Korean. Each example underwent careful expert review to verify its Drivelological characteristics, involving multiple rounds of discussion and adjudication to address disagreements. Using this dataset, we evaluate a range of LLMs on classification, generation, and reasoning tasks. Our results reveal clear limitations of LLMs: models often confuse Drivelology with shallow nonsense, produce incoherent justifications, or miss implied rhetorical functions altogether. These findings highlight a deep representational gap in LLMs' pragmatic understanding and challenge the assumption that statistical fluency implies cognitive comprehension. We release our dataset and code to facilitate further research in modelling linguistic depth beyond surface-level coherence."
}
```