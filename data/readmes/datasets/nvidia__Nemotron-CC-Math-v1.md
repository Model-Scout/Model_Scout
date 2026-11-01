---
license: other
task_categories:
- text-generation
extra_gated_prompt: >-
  By clicking “Agree” I confirm I have read and agree to NVIDIA Data Agreement
  for Model Training and agree that I intend to use this data for model training
  purposes only.
  (https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Dataset-sample/raw/main/LICENSE.md) 
extra_gated_fields:
  Company: text
  Institutional Email: text
  I agree to use this dataset for model training purposes ONLY: checkbox
configs:
- config_name: '3'
  data_files:
  - path: 3/*.parquet
    split: train
- config_name: 4plus
  data_files:
  - path: 4plus/*.parquet
    split: train
- config_name: 4plus_MIND
  data_files:
  - path: 4plus_MIND/*.parquet
    split: train
track_downloads: true
---

# Nemotron-Pre-Training-Dataset-v1 Release

👩‍💻 **Authors**: Rabeeh Karimi Mahabadi, Sanjeev Satheesh

📘 **Paper**: [Nemotron-cc-math: A 133 Billion-Token-Scale High Quality Math Pretraining Dataset](https://arxiv.org/abs/2508.15096)

📝 **Blog**: [Nemotron-cc-math blog](https://huggingface.co/blog/nvidia/nemotron-cc-math/)


## Data Overview

We’re excited to introduce **Nemotron-CC-Math** - a large-scale, high-quality math corpus extracted from Common Crawl which was used in nemotron pre-training. 
This dataset is built to preserve and surface high-value mathematical and code content, enabling the next wave of intelligent, globally-capable language models.

🚀 **Why it matters:** Nemotron-CC-Math significantly advances the state of open-source math pretraining corpora. It outperforms prior resources such as FineMath, MegaMath, and OpenWebMath on math reasoning benchmarks, while also delivering competitive gains in code and general reasoning.

To demonstrate its impact, we integrated Nemotron-CC-Math into the pretraining mixture for the [**NVIDIA Nemotron Nano 2**](https://huggingface.co/collections/nvidia/nvidia-nemotron-689f6d6e6ead8e77dd641615) family of LLMs — including [NVIDIA-Nemotron-Nano-9B-v2](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2), [NVIDIA-Nemotron-Nano-9B-v2-Base](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2), and [NVIDIA-Nemotron-Nano-12B-v2-Base](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-Base). These models build on the success of [Nemotron-H-8B-Base-8K](https://huggingface.co/nvidia/Nemotron-H-8B-Base-8K) and [Nemotron-H-8B-Reasoning-128K](https://huggingface.co/nvidia/Nemotron-H-8B-Reasoning-128K), with commercial-ready licensing and support for **128K context length**. The aligned [NVIDIA-Nemotron-Nano-9B-v2](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2) variant is further optimized for human chat and task performance.

🧪 **Proven impact:** Across math reasoning benchmarks — GSM8K CoT, MATH, MATH Level 5, and AIME 2024 — Nemotron-CC-Math consistently boosts performance, with especially strong gains on the most challenging tasks like MATH Level 5 and AIME.

💡 With Nemotron-CC-Math, we’re raising the bar for open math pretraining — and we’re excited to see how the community will build on it.


![image/png](https://cdn-uploads.huggingface.co/production/uploads/653c39d53bd6135805ff9abc/BJ0PCrYdWqysL1OcrpB_u.png)

---
## ✨ Why Build a New Math Corpus?

High-quality math datasets are critical for improving reasoning, symbolic understanding, and general intelligence in large language models (LLMs). However, most existing open math corpora suffer from:

* **Brittle extraction pipelines**
* **Lossy HTML-to-text conversions**
* **Missing or corrupted equations**
* **Inconsistent formatting and low data fidelity**

Many of the best-performing proprietary LLMs (e.g., Minerva, DeepSeekMath, Qwen-Math) rely on large, unreleased math corpora. To support the open research community, we built **Nemotron-CC-Math** from scratch using a **new domain-agnostic extraction pipeline** designed for scientific content.

---

## 🔍 What’s Inside the Dataset?
Nemotron-CC-Math comes in two variants — nemotron-cc-math-3plus and nemotron-cc-math-4plus — created by classifying data with our FineMath classifier. In this scheme, 3plus corresponds to samples scoring 3, 4, or 5, while 4plus includes only samples scoring 4 or 5. Our dataset is constructed from **98 Common Crawl snapshots (2014–2024)**. In total, we process content from **over 980,000 unique domains**, making it one of the most diverse math corpora available. We also regenerated the Nemotron-MIND dataset using nemotron-cc-math-4plus, our high-quality subset, which yielded consistent gains over previous Nemotron-MIND.


| Dataset                  | # Tokens | # Documents |
| ------------------------ | -------- | ----------- | 
| `nemotron-cc-math-3plus` | **133B** | 101.15M        | 
| `nemotron-cc-math-4plus` | **52B**  | 45.10M         | 
| `nemotron-mind-v1`       | **73B**  | 88.73M        |

---


## 🔨 How We Built It

We built a **scalable and robust pipeline** tailored to mathematical and scientific content with five key steps:

1. **Lynx Rendering** – Instead of relying on brittle DOM parsing, we use `lynx` to convert HTML into structured text while preserving equations and layout.
2. **LLM Cleaning** – We use a lightweight LLM (Phi-4, 14B) to remove boilerplate, standardizes mathematical expressions into consistent LaTeX, and improves formatting.
3. **Quality Filtering** – We use FineMath classifier to assign a quality score from 1–5 to each page.
4. **Deduplication** – We use MinHash-based Locality Sensitive Hashing (NeMo-Curator) to remove near-duplicates.
5. **Decontamination** – We apply LLM-based contamination detection against test benchmarks (MATH, GSM8K, MMLU, MMLU-Pro) to prevent benchmark leakage.

---

## 🏆 Performance

We ran mid-training ablations on 8B sized models using this corpus and compared against prior math pretraining datasets including, 
**OpenWebMath**, **MegaMath**, **FineMath**. Our dataset obtains substantial improvements across math, code, and general reasoning.

| Dataset          | MATH (EM)          | GSM8K (EM) |HumanEval+ (average\@20) | MBPP+ (average\@20) |MMLU (EM) | MMLU-STEM (EM) |
| ---------------- | ------------------ | ---------- | ------------------------| ------------------- | -------- | -------------- |
| OpenWebMath      |  34.2              | 76.42      |33.54                    | 37.59               | 65.20     | 59.20         |
| FineMath-3+      |  34.6              | 79.45      | 34.18                   | 29.19               |67.92      | 62.29         |
| MegaMath-Web     |31.6                | 78.24      |32.29                    | 38.89               |65.44       | 59.88        |
| **Nemotron-CC-Math-3+** | **44.20**   | **80.06**  | **37.16**               | **43.51**           |**68.20**   | **64.26**    |



Using **Nemotron-CC-Math-4plus**, we regenerated [Nemotron-MIND](https://arxiv.org/abs/2410.12881) which leads to substantial improvements across math, code, and general reasoning tasks:

| Dataset          | #Unique Tokens (B) | MMLU Pro | MMLU | MMLU STEM | Code | Math-500 | GSM8K |
| ---------------- | ------------------ | -------- | ---- | --------- | ---- | -------- | ----- |
| Nemotron-MIND    | 126                | 36.1     | 66.1 | 60        | 43.4 | 33.4     | 80.7  |
| Nemotron-MIND-V1 | 73                 | 39.7     | 67.5 | 63.7      | 44.2 | 47.8     | 84.5  |

---

## 🔍 Qualitative Examples 
We present a side-by-side comparison between our dataset and prior work (MegaMath). The illustrative samples highlight how our model preserves mathematical equations, in contrast to existing approaches where such structures are often lost or distorted.

![Sample](https://cdn-uploads.huggingface.co/production/uploads/682ddc626a16cf7c1d953f19/vDKZKV69bPW0G1q-OTBQ2.png)
![Sample](https://cdn-uploads.huggingface.co/production/uploads/682ddc626a16cf7c1d953f19/KcrVWeuxamJlVjB53VpD_.png)
![Sample](https://cdn-uploads.huggingface.co/production/uploads/682ddc626a16cf7c1d953f19/wCgFhILeRIDf8jma4v8n4.png)
![Sample](https://cdn-uploads.huggingface.co/production/uploads/682ddc626a16cf7c1d953f19/wbDNVldYQOM8d8z3eMqzS.png)

## 📦 Get Started

Users can download subsets of the data based on the metadata schema described above. Example script for downloading code and math as follows:
```
from datasets import load_dataset
ds = load_dataset("nvidia/Nemotron-CC-Math-v1", "4plus", streaming=True)
```

The datasets has 3 subsets: 3 (documents with quality label 3), 4plus (documents with quality labels 4 and 5) and 4plus_MIND (MIND method applied to the 4plus subsset). To build the 3plus subset, load both 3 and 4plus subsets.


## 📜 License
[NVIDIA Open Data License Agreement](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Dataset-sample/raw/main/LICENSE.md)

This dataset is created using phi-4 model. If this dataset is used to create, train, fine-tune, or otherwise improve an AI model, which is distributed or made available, such AI model may be subject to redistribution and use requirements in the [Phi-4 License Agreement](https://huggingface.co/microsoft/phi-4/blob/main/LICENSE).

**Data Developer:** NVIDIA

**Use Case:** Developers training foundation LLM models.

**Release Date:** 8/18/2025

**Data Version:** 1.0 (8/18/2025)

**Intended use**: The Nemotron Pre-Training Dataset is intended to be used by the community to continue to improve open models. The data may be freely used to train and evaluate with user agreement to open data license.


## Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Data Opt-Out:
NVIDIA has undertaken legal review to ensure there is no confidential, PII or copyright materials.  If, when reviewing or using this dataset, you identify issues with the data itself, such as those listed above, please contact nemotron-data@nvidia.com.


## 📝 Citation

```bibtex
@article{karimi2025nemotroncc,
  title = {Nemotron-cc-math: A 133 Billion-Token-Scale High Quality Math Pretraining Dataset},
  author = {Rabeeh Karimi Mahabadi, Sanjeev Satheesh, Shrimai Prabhumoye, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro },
  url = {https://arxiv.org/abs/2508.15096},
  year = {2025}
}
```
```bibtex
@misc{nvidia2025nvidianemotronnano2,
      title={NVIDIA Nemotron Nano 2: An Accurate and Efficient Hybrid Mamba-Transformer Reasoning Model}, 
      author={NVIDIA and : and Aarti Basant and Abhijit Khairnar and Abhijit Paithankar and Abhinav Khattar and Adithya Renduchintala and Aditya Malte and Akhiad Bercovich and Akshay Hazare and Alejandra Rico and Aleksander Ficek and Alex Kondratenko and Alex Shaposhnikov and Alexander Bukharin and Ali Taghibakhshi and Amelia Barton and Ameya Sunil Mahabaleshwarkar and Amy Shen and Andrew Tao and Ann Guan and Anna Shors and Anubhav Mandarwal and Arham Mehta and Arun Venkatesan and Ashton Sharabiani and Ashwath Aithal and Ashwin Poojary and Ayush Dattagupta and Balaram Buddharaju and Banghua Zhu and Barnaby Simkin and Bilal Kartal and Bita Darvish Rouhani and Bobby Chen and Boris Ginsburg and Brandon Norick and Brian Yu and Bryan Catanzaro and Charles Wang and Charlie Truong and Chetan Mungekar and Chintan Patel and Chris Alexiuk and Christian Munley and Christopher Parisien and Dan Su and Daniel Afrimi and Daniel Korzekwa and Daniel Rohrer and Daria Gitman and David Mosallanezhad and Deepak Narayanan and Dima Rekesh and Dina Yared and Dmytro Pykhtar and Dong Ahn and Duncan Riach and Eileen Long and Elliott Ning and Eric Chung and Erick Galinkin and Evelina Bakhturina and Gargi Prasad and Gerald Shen and Haifeng Qian and Haim Elisha and Harsh Sharma and Hayley Ross and Helen Ngo and Herman Sahota and Hexin Wang and Hoo Chang Shin and Hua Huang and Iain Cunningham and Igor Gitman and Ivan Moshkov and Jaehun Jung and Jan Kautz and Jane Polak Scowcroft and Jared Casper and Jian Zhang and Jiaqi Zeng and Jimmy Zhang and Jinze Xue and Jocelyn Huang and Joey Conway and John Kamalu and Jonathan Cohen and Joseph Jennings and Julien Veron Vialard and Junkeun Yi and Jupinder Parmar and Kari Briski and Katherine Cheung and Katherine Luna and Keith Wyss and Keshav Santhanam and Kezhi Kong and Krzysztof Pawelec and Kumar Anik and Kunlun Li and Kushan Ahmadian and Lawrence McAfee and Laya Sleiman and Leon Derczynski and Luis Vega and Maer Rodrigues de Melo and Makesh Narsimhan Sreedhar and Marcin Chochowski and Mark Cai and Markus Kliegl and Marta Stepniewska-Dziubinska and Matvei Novikov and Mehrzad Samadi and Meredith Price and Meriem Boubdir and Michael Boone and Michael Evans and Michal Bien and Michal Zawalski and Miguel Martinez and Mike Chrzanowski and Mohammad Shoeybi and Mostofa Patwary and Namit Dhameja and Nave Assaf and Negar Habibi and Nidhi Bhatia and Nikki Pope and Nima Tajbakhsh and Nirmal Kumar Juluru and Oleg Rybakov and Oleksii Hrinchuk and Oleksii Kuchaiev and Oluwatobi Olabiyi and Pablo Ribalta and Padmavathy Subramanian and Parth Chadha and Pavlo Molchanov and Peter Dykas and Peter Jin and Piotr Bialecki and Piotr Januszewski and Pradeep Thalasta and Prashant Gaikwad and Prasoon Varshney and Pritam Gundecha and Przemek Tredak and Rabeeh Karimi Mahabadi and Rajen Patel and Ran El-Yaniv and Ranjit Rajan and Ria Cheruvu and Rima Shahbazyan and Ritika Borkar and Ritu Gala and Roger Waleffe and Ruoxi Zhang and Russell J. Hewett and Ryan Prenger and Sahil Jain and Samuel Kriman and Sanjeev Satheesh and Saori Kaji and Sarah Yurick and Saurav Muralidharan and Sean Narenthiran and Seonmyeong Bak and Sepehr Sameni and Seungju Han and Shanmugam Ramasamy and Shaona Ghosh and Sharath Turuvekere Sreenivas and Shelby Thomas and Shizhe Diao and Shreya Gopal and Shrimai Prabhumoye and Shubham Toshniwal and Shuoyang Ding and Siddharth Singh and Siddhartha Jain and Somshubra Majumdar and Soumye Singhal and Stefania Alborghetti and Syeda Nahida Akter and Terry Kong and Tim Moon and Tomasz Hliwiak and Tomer Asida and Tony Wang and Tugrul Konuk and Twinkle Vashishth and Tyler Poon and Udi Karpas and Vahid Noroozi and Venkat Srinivasan and Vijay Korthikanti and Vikram Fugro and Vineeth Kalluru and Vitaly Kurin and Vitaly Lavrukhin and Wasi Uddin Ahmad and Wei Du and Wonmin Byeon and Ximing Lu and Xin Dong and Yashaswi Karnati and Yejin Choi and Yian Zhang and Ying Lin and Yonggan Fu and Yoshi Suhara and Zhen Dong and Zhiyu Li and Zhongbo Zhu and Zijia Chen},
      year={2025},
      eprint={2508.14444},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.14444}, 
}
```
