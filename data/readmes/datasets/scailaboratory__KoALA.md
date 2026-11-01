---
language:
  - ko
  - en
task_categories:
  - automatic-speech-recognition
  - translation
  - question-answering
  - audio-classification
tags:
  - speech
  - korean
  - benchmark
  - audio-language-model
  - LALM
  - multimodal
pretty_name: "KoALa-Bench"
---

# KoALa-Bench: Korean Audio Language Model Benchmark

**KoALa-Bench** is a comprehensive benchmark for evaluating Large Audio Language Models (LALMs) on Korean speech understanding. It covers six tasks spanning both conventional speech processing and novel *speech faithfulness* evaluation, designed to test whether models can reason over the acoustic and linguistic content of Korean speech.

## Tasks

KoALa-Bench consists of six evaluation tasks organized into two categories.

### Conventional Tasks

| Task | Description | Metric |
|------|-------------|--------|
| **ASR** (Automatic Speech Recognition) | Transcribe Korean speech into text | CER |
| **ST** (Speech Translation) | Translate Korean speech into English text | BLEU |
| **SQA** (Spoken Question Answering) | Answer questions about the content of a spoken passage | Accuracy |
| **SIF** (Speaker Information Faithfulness) | Identify speaker attributes (e.g., gender, age) from speech | Score (GPT as Judge) |

### Speech Faithfulness Tasks

| Task | Description | Metric |
|------|-------------|--------|
| **SCA-QA** (Speech Content Adherence QA) | Answer questions that require faithful understanding of spoken content, not prior knowledge | SCF Score |
| **PA-QA** (Paralinguistic Attribute QA) | Answer questions about paralinguistic features such as emotion, tone, and speaking style | Accuracy |

> **Speech Faithfulness** tasks (SCA-QA, PA-QA) are novel contributions of KoALa-Bench, designed to evaluate whether a model truly listens to and reasons over the given audio rather than relying on textual shortcuts or parametric knowledge.

## Audio Conditions

Each task provides audio samples under two conditions:

- **Clean**: Original audio without modification.
- **Noise**: Audio augmented with background noise to evaluate model robustness under adverse acoustic conditions.

This allows users to assess LALM performance across both ideal and realistic noisy environments.

## Dataset Structure

```
KoALA/
├── ASR/
│   ├── clean/
│   │     ├── commonVoice/
│   │     └── zeroth_korean/
│   └── noise/
│         ├── commonVoice/
│         └── zeroth_korean/
├── ST/
│   ├── clean/
│   └── noise/
├── SQA/
│   ├── clean/
│   │     ├── click/
│   │     ├── KCSAT/
│   │     └── kobest_boolq/
│   └── noise/
│         ├── click/
│         ├── KCSAT/
│         └── kobest_boolq/
├── SIF/
│   ├── clean/
│   │     ├── alpaca/
│   │     ├── kudge/
│   │     ├── openhermes/
│   │     └── vicuna/
│   └── noise/
│         ├── alpaca/
│         ├── kudge/
│         ├── openhermes/
│         └── vicuna/
├── SCA-QA/
│   ├── clean/
│   │     ├── history_after_chosun/
│   │     ├── history_before_chosun/
│   │     ├── k-sports/
│   │     └── kpop/
│   └── noise/
│         ├── history_after_chosun/
│         ├── history_before_chosun/
│         ├── k-sports/
│         └── kpop/
└── PA-QA/
    ├── clean/
    │     └── MCtest/
    └── noise/
          └── MCtest/
```

Each subset contains audio files and corresponding annotations in JSON format.

## Usage

```python
from datasets import load_dataset

# Load a specific task
dataset = load_dataset("scailaboratory/KoALA", "ASR")

# Load all tasks
for task in ["ASR", "ST", "SQA", "SIF", "SCA-QA", "PA-QA"]:
    ds = load_dataset("scailaboratory/KoALA", task)
```

## Licensing

> **Important:** KoALa-Bench is constructed from multiple source datasets, each with its own license. Users must comply with the license terms of each original source.

| Task | Original Datasets | Original License |
|------|-------------|--------|
| ASR | commonVoice | CC0 1.0|
| ASR | zeroth_korean | CC BY 4.0|
| SQA | CLIcK | Other|
| SQA |Kobest-BoolQ | CC-BY-SA-4.0 |
| SIF|alpaca|CC BY-NC 4.0|
| SIF|kudge|Academic-only|
| SIF|openhermes|Academic-only|
| SIF|vicuna|Apache License 2.0|
| ST |ETRI|CC BY-NC-ND 4.0|
|SCA-QA|-|-|
|PA-QA|MCTest|MSR-LA|

### Source Datasets
Please also cite the original datasets used in KoALa-Bench:
```bibtex

----------------ASR----------------
@article{DBLP:journals/corr/abs-1912-06670,
  author       = {Rosana Ardila and
                  Megan Branson and
                  Kelly Davis and
                  Michael Henretty and
                  Michael Kohler and
                  Josh Meyer and
                  Reuben Morais and
                  Lindsay Saunders and
                  Francis M. Tyers and
                  Gregor Weber},
  title        = {Common Voice: {A} Massively-Multilingual Speech Corpus},
  journal      = {CoRR},
  volume       = {abs/1912.06670},
  year         = {2019},
  url          = {http://arxiv.org/abs/1912.06670},
  eprinttype   = {arXiv},
  eprint       = {1912.06670},
  timestamp    = {Thu, 02 Jan 2020 18:08:18 +0100},
  biburl       = {https://dblp.org/rec/journals/corr/abs-1912-06670.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
@misc{zeroth_korean,
  title        = {Zeroth-Korean: Korean Open-source Speech Corpus for Speech Recognition},
  author       = {{Zeroth Project}},
  howpublished = {\url{https://www.openslr.org/40/}},
  note         = {OpenSLR SLR40},
  year         = {2018}
}
----------------SQA----------------
@misc{kim2024click,
      title={CLIcK: A Benchmark Dataset of Cultural and Linguistic Intelligence in Korean}, 
      author={Eunsu Kim and Juyoung Suk and Philhoon Oh and Haneul Yoo and James Thorne and Alice Oh},
      year={2024},
      eprint={2403.06412},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
@misc{https://doi.org/10.48550/arxiv.2204.04541,
  doi = {10.48550/ARXIV.2204.04541},
  url = {https://arxiv.org/abs/2204.04541},
  author = {Kim, Dohyeong and Jang, Myeongjun and Kwon, Deuk Sin and Davis, Eric},
  title = {KOBEST: Korean Balanced Evaluation of Significant Tasks},
  publisher = {arXiv},
  year = {2022},
}
----------------SIF----------------
@article{son2024llm,
  title={LLM-as-a-Judge \& Reward Model: What They Can and Cannot Do},
  author={Son, Guijin and Ko, Hyunwoo and Lee, Hoyoung and Kim, Yewon and Hong, Seunghyeok},
  journal={arXiv preprint arXiv:2409.11239},
  year={2024}
}
@article{wang2024audiobench,
  title={AudioBench: A Universal Benchmark for Audio Large Language Models},
  author={Wang, Bin and Zou, Xunlong and Lin, Geyu and Sun, Shuo and Liu, Zhuohan and Zhang, Wenyu and Liu, Zhengyuan and Aw, AiTi and Chen, Nancy F},
  journal={NAACL},
  year={2025}
}
@misc{vicuna2023,
    title = {Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90\%* ChatGPT Quality},
    url = {https://lmsys.org/blog/2023-03-30-vicuna/},
    author = {Chiang, Wei-Lin and Li, Zhuohan and Lin, Zi and Sheng, Ying and Wu, Zhanghao and Zhang, Hao and Zheng, Lianmin and Zhuang, Siyuan and Zhuang, Yonghao and Gonzalez, Joseph E. and Stoica, Ion and Xing, Eric P.},
    month = {March},
    year = {2023}
}
----------------PA-QA----------------
@inproceedings{richardson-etal-2013-mctest,
    title = "{MCT}est: A Challenge Dataset for the Open-Domain Machine Comprehension of Text",
    author = "Richardson, Matthew  and
      Burges, Christopher J.C.  and
      Renshaw, Erin",
    editor = "Yarowsky, David  and
      Baldwin, Timothy  and
      Korhonen, Anna  and
      Livescu, Karen  and
      Bethard, Steven",
    booktitle = "Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing",
    month = oct,
    year = "2013",
    address = "Seattle, Washington, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D13-1020/",
    pages = "193--203"
}

```


## Citation

If you use KoALa-Bench in your research, please cite:

```bibtex
----
```

## Contact

For questions or issues, please open an issue on this repository or contact the [SCAI Lab](https://sites.google.com/view/scai-lab/) at Chung-Ang University.