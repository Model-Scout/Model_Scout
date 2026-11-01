---
task_categories:
- image-to-text
- visual-question-answering
- table-question-answering
- text-generation

configs:
- config_name: core_permissive
  data_files:
  - split: train
    path: core_permissive/*
  default: true
- config_name: core
  data_files:
  - split: train
    path: core/*
- config_name: reasoning
  data_files:
  - split: train
    path: reasoning/*
- config_name: human_verified
  data_files:
  - split: train
    path: human_verified/train/*
  - split: test
    path: human_verified/test/*
- config_name: grounded_qa
  data_files:
  - split: train
    path: grounded_qa/*
- config_name: multichart
  data_files:
  - split: train
    path: multichart/*
- config_name: core_permissive_multilingual
  data_files:
  - split: arabic
    path: core_permissive_multilingual/arabic/*
  - split: chinese
    path: core_permissive_multilingual/chinese/*
  - split: czech
    path: core_permissive_multilingual/czech/*
  - split: dutch
    path: core_permissive_multilingual/dutch/*
  - split: french
    path: core_permissive_multilingual/french/*
  - split: german
    path: core_permissive_multilingual/german/*
  - split: italian
    path: core_permissive_multilingual/italian/*
  - split: japanese
    path: core_permissive_multilingual/japanese/*
  - split: korean
    path: core_permissive_multilingual/korean/*
  - split: portuguese
    path: core_permissive_multilingual/portuguese/*
  - split: spanish
    path: core_permissive_multilingual/spanish/*

dataset_info:
- config_name: core_permissive
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: code
    dtype: string
  - name: csv
    dtype: string
  - name: summary
    dtype: string
  - name: chart_type
    dtype: string
  - name: library
    dtype: string
- config_name: core
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: code
    dtype: string
  - name: csv
    dtype: string
  - name: summary
    dtype: string
- config_name: reasoning
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: complex_question
    dtype: string
  - name: think
    dtype: string
  - name: answer
    dtype: string
- config_name: human_verified
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: code
    dtype: string
  - name: csv
    dtype: string
  - name: summary
    dtype: string
- config_name: grounded_qa
  features:
  - name: id
    dtype: string
  - name: grounded_image
    dtype: image
  - name: template_qa
    list:
    - name: ans
      dtype: string
    - name: mode
      dtype: string
    - name: q
      dtype: string
    - name: short_ans
      dtype: bool
    - name: template
      dtype: string
  - name: reasoning_qa
    list:
    - name: answer
      dtype: string
    - name: bboxes
      list:
      - name: bbox
        sequence: float64
      - name: role
        dtype: string
      - name: series
        dtype: string
    - name: category
      dtype: string
    - name: question
      dtype: string
    - name: reasoning
      dtype: string
- config_name: multichart
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: csv
    dtype: string
  - name: summary
    dtype: string
- config_name: core_permissive_multilingual
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  - name: code
    dtype: string
  - name: csv
    dtype: string
  - name: summary
    dtype: string
  - name: chart_type
    dtype: string
  - name: library
    dtype: string

license: cdla-permissive-2.0
size_categories:
- 10M<n<100M
language:
- en
- ar
- zh
- cs
- nl
- fr
- de
- it
- ja
- ko
- pt
- es
---
# ChartNet: A Million-Scale Multimodal Dataset for Chart Understanding

🌐 [Homepage](https://huggingface.co/datasets/ibm-granite/ChartNet) | 📖 [arXiv](https://arxiv.org/abs/2603.27064)

## 📰 Latest Update — October 2026
### ChartNet introduces two new datasets:
- **Multi-Panel Charts:** Complex figures with multiple subplots, supporting structured data extraction and chart summarization.
- **Multilingual Charts:** Additional charts in 11 languages besides English, supporting multilingual chart understanding and data extraction. Languages include Arabic, Chinese, Czech, Dutch, French, German, Italian, Japanese, Korean, Portuguese, and Spanish.
 
---

## 📝 Changelog
### **October 26, 2026**
  - Released the `multichart` and `core_permissive_multilingual` sets, supporting multi-panel and multilingual chart understanding.
  - Many thanks to Toshihiro Takahashi, Shoko Suzuki, and Issei Yoshida for their contributions to the `core_permissive_multilingual` set.
  - Both sets subject to [cdla-permissive-2.0](https://huggingface.co/datasets/ibm-granite/ChartNet#%F0%9F%AA%AA-license-notice).

### **June 3, 2026**
  - Release of `grounded_qa` set and completed `reasoning` set.
  - Both sets subject to [Notice Regarding Data Availability](https://huggingface.co/datasets/ibm-granite/ChartNet#%E2%84%B9%EF%B8%8F-notice-regarding-data-availability).

### **May 15, 2026**
  - Added link to [30K real-world charts and detailed captions dataset](https://huggingface.co/datasets/2077AIDataFoundation/ChartNet_RealWorldChart) released by our collaborators Abaka AI/2077AI.

### **April 29, 2026**
  - Release of an additional 2.5 million row set `core_permissive`.
  - Set subject to [cdla-permissive-2.0](https://huggingface.co/datasets/ibm-granite/ChartNet#%F0%9F%AA%AA-license-notice).

### **March 31, 2026**
  - Initial release of ChartNet with `core`, `reasoning`, and `human_verified` sets.
  - Set subject to [Notice Regarding Data Availability](https://huggingface.co/datasets/ibm-granite/ChartNet#%E2%84%B9%EF%B8%8F-notice-regarding-data-availability).

---

## 🗂️ Dataset Summary

Chart understanding requires models to jointly reason over geometric visual patterns, structured numerical data, and natural language descriptions — capabilities 
where current VLMs still fall short. ChartNet addresses this gap by offering a large‑scale, high‑quality multimodal dataset designed for **robust chart interpretation and reasoning**.

The `core` dataset contains **1.7 million richly annotated chart samples**, each offering tightly aligned **visual**, **numerical**, and **textual** components. 
All samples pass through a rigorous quality‑filtering pipeline to ensure visual fidelity, semantic correctness, and dataset diversity.

Additional subsets extend ChartNet with real-world charts, human-verified examples, grounded question-answer pairs, multi-panel charts, and multilingual charts spanning 11 languages besides English.

Together, these elements enable models to perform structured, interpretable, end‑to‑end reasoning directly from chart images. More details are available in our [CVPR 2026 paper](https://arxiv.org/abs/2603.27064). 

ChartNet has been used to train the *Granite Vision 4* series of models: [Granite-4.0-3B-Vision](https://huggingface.co/ibm-granite/granite-4.0-3b-vision) and [Granite-Vision-4.1-4B](https://huggingface.co/ibm-granite/granite-vision-4.1-4b).

---

## 🔧 Code‑Guided Synthesis Pipeline

ChartNet `core` is built using a **code‑guided chart synthesis pipeline** spanning **24 chart types** across **six plotting libraries**.

![chartnet](https://cdn-uploads.huggingface.co/production/uploads/679bb8770109de6d9f78cdff/_b7CMwjTdN6oF-cI_zOBq.jpeg)

Starting from a small seed set of chart images, a VLM generates approximate reconstruction code. The code representation is then used to:

1. **Regenerate charts with diverse stylistic and semantic variations**  
2. **Derive aligned structured attributes**, including:
   - Tabular data
   - Natural‑language summaries
   - Question–answer pairs with detailed chain‑of‑thought reasoning

Each ChartNet `core` example provides **five tightly aligned components**:

- **Rendered chart image** (`image` column)
- **Plotting code** (`code` column)
- **Underlying data table** (`csv` column)
- **Natural‑language summary** (`summary` column)
- **Complex QA pairs with step‑by‑step reasoning** (`reasoning` subset)

This multimodal alignment covers the full spectrum of chart comprehension tasks, including:
- **Chart reconstruction** (`chart2code`): Recover plotting code or structured chart specifications.
- **Data extraction** (`chart2csv`): Retrieve underlying values and tables directly from chart visuals.
- **Chart summarization** (`chart2text`): Produce concise NL summaries describing patterns and trends.
- **Reasoning and Visual QA**: Answer semantic, relational, and quantitative questions using chain‑of‑thought reasoning.

---

## 📚 Specialized Subsets
### **Original Releases**
These sets were released to accompany the [ChartNet paper](https://arxiv.org/abs/2603.27064). The original ChartNet sets include differences in their composition and generation process and are made available solely to support the verification and evaluation of the results presented in [_ChartNet: A Million-Scale, High-Quality Multimodal Dataset for Robust Chart Understanding_](https://arxiv.org/abs/2603.27064).
These original subsets, excluding the *Real‑world Chart Set*, are subject to the [Notice Regarding Data Availability](https://huggingface.co/datasets/ibm-granite/ChartNet#%E2%84%B9%EF%B8%8F-notice-regarding-data-availability).

- #### **Core ChartNet Set (`core`)**
  - **Row Count**: 1.7M `train` charts
  - **Columns**: `id`, `image`, `code`, `csv`, `summary`
  - **Description**: The four main representations of each chart: the visual itself, the Python snippet that was used to draw it, a table of values comprising the chart, and a few paragraphs describing the chart in detail. Images span 24 different chart types and 6 plotting libraries.

- #### **Human‑annotated Set (`human_verified`)**
  - **Row Count**: 92.6K `train` + 2K `test` charts
  - **Columns**: `id`, `image`, `code`, `csv`, `summary`
  - **Description**: A curated, high‑quality set of synthetic charts with human‑verified images, summaries, and tables. `human_verified` and `core` are disjoint sets.

- #### **Grounding / Localization Subset (`grounded_qa`)**
  - **Row Count**: 158K `train` charts
  - **Columns**: `id`, `grounded_image`, `template_qa`, `reasoning_qa`
  - **Description**: A subset of `core` with QA pairs focused on grounding, region‑aware chart comprehension, and reasoning. The `template_qa` column provides 8 templated QA pairs per chart with bounding boxes generated using elements within the image. The `reasoning_qa` column features up to 15 synthetic QA pairs per chart and accompanying reasoning chains-of-thought.

- #### **Complex Reasoning Subset (`reasoning`)**
  - **Row Count**: 1.68M `train` charts
  - **Columns**: `id`, `image`, `complex_question`, `think`, `answer`
  - **Description**: Nearly every `core` chart paired with a difficult QA requiring multiple steps of analysis and chains-of-thought.

- #### **Real‑world Chart Set**
  - **Row Count**: 30K `train` charts
  - **Columns**: `image_name`, `image`, `caption`
  - **Link**: [2077AIDataFoundation/ChartNet_RealWorldChart](https://huggingface.co/datasets/2077AIDataFoundation/ChartNet_RealWorldChart)
  - **Description**: A collection of 30,000 charts from reputable media and visualization sources, paired with detailed natural-language captions. Released by our collaborators Abaka AI / 2077AI.

- #### **Safety‑focused Content** *(coming soon)*
  - **Description**: Charts and QA pairs crafted for safety alignment and jailbreak‑resistant reasoning.


### **Latest Extensions**
These additional releases extend the original vision of ChartNet by including new modalities, tasks, and variations, all under a new permissive license. Additional data is actively being generated for subsequent releases.
The following sets are released under [cdla-permissive-2.0](https://huggingface.co/datasets/ibm-granite/ChartNet#%F0%9F%AA%AA-license-notice).

- #### **Core ChartNet Set with Permissive Licensing (`core_permissive`)**
  - **Row Count**: 2.5M `train` charts
  - **Columns**: `id`, `image`, `code`, `csv`, `summary`, `chart_type`, `library`
  - **Description**: A larger variant of the `core` set with updates to its composition and generation process for higher quality representations and permissive licensing.
  
- #### **Multi-panel Chart Set (`multichart`)**
  - **Row Count**: 413K `train` charts
  - **Columns**: `id`, `image`, `csv`, `summary`
  - **Description**: Complex figures containing multiple subplots, with CSV and summary annotations for structured data extraction and chart summarization across the panels.

- #### **Multilingual Chart Subset (`core_permissive_multilingual`)**
  - **Row Count**: 27M total charts; ~2.5M charts per language
  - **Columns**: `id`, `image`, `code`, `csv`, `summary`, `chart_type`, `library`
  - **Languages**: Arabic, Chinese, Czech, Dutch, French, German, Italian, Japanese, Korean, Portuguese, Spanish
  - **Description**: Nearly every `core_permissive` chart translated to 11 languages, supporting multilingual chart understanding and data extraction. The `id` column includes the ID from the original chart image (in English, from `core_permissive`) with a suffix based on the language. Thanks to Toshihiro Takahashi, Shoko Suzuki, and Issei Yoshida for their contributions to this subset.

---


## 📥 Guide on Data Loading
ChartNet supports the HuggingFace `datasets` library for downloading subsets:

```python
from datasets import load_dataset
# load the permissive use subset (subject to Community Data License Agreement – Permissive, Version 2.0)
core_permissive = load_dataset("ibm-granite/ChartNet", "core_permissive")
```

To load the releases that correspond with the paper, specify the appropriate subsets:

```python
# load the original overlapping core and reasoning subsets (they can be joined by the "id" column):
core = load_dataset("ibm-granite/ChartNet", "core")
reasoning = load_dataset("ibm-granite/ChartNet", "reasoning")
# load the original human reviewed train/test splits (they are completely disjoint from the rest of the subsets):
human_verified_train = load_dataset("ibm-granite/ChartNet", "human_verified", split="train")
human_verified_test = load_dataset("ibm-granite/ChartNet", "human_verified", split="test")
# load the original grounded QA dataset:
grounded_qa = load_dataset("ibm-granite/ChartNet", "grounded_qa")
```

These original subsets are subject to the [Notice Regarding Data Availability](https://huggingface.co/datasets/ibm-granite/ChartNet#%E2%84%B9%EF%B8%8F-notice-regarding-data-availability).

Each subset can be several hundred gigabytes in size, so it is recommended to download individual files as needed:

```python
# load the first 10_000 entries from the core dataset (1.66GB in size):
first_core_file = load_dataset("ibm-granite/ChartNet", data_files="core/core_000.parquet")
print(first_core_file.shape) # output: {'train': (10000, 5)}
```

---

### 🪪 License Notice
**April 29, 2026 — ChartNet Licensing Update**
IBM is releasing a new default version of the ChartNet dataset following changes to its composition and generation process. Based on those changes, IBM is making this version available under the Community Data License Agreement – Permissive, Version 2.0.

For reproducibility and evaluation of the original release, access to the previously released dataset is retained via separate mechanism as described in the [Guide on Data Loading](https://huggingface.co/datasets/ibm-granite/ChartNet#%F0%9F%93%A5-guide-on-data-loading). The original release remains subject to the [Notice Regarding Data Availability](https://huggingface.co/datasets/ibm-granite/ChartNet#%E2%84%B9%EF%B8%8F-notice-regarding-data-availability) and requires users to follow the explicit retrieval steps described in its dataset card. The original release is provided solely to enable reproducibility and comparative evaluation of the original release and should NOT be used as a substitute for the current default release.

---

### ℹ️ Notice Regarding Data Availability

By downloading, accessing, or using this dataset, you acknowledge and agree to the terms and limitations set forth in this __Notice Regarding Data Availability__.

This dataset is made available solely to support the verification and evaluation of the results presented in __ChartNet: A Million-Scale, High-Quality Multimodal Dataset for Robust Chart Understanding__.

No license, covenant, or other rights are granted with respect to this dataset, either expressly or by implication. The authors do not assert intellectual property rights in this dataset and make no representations regarding ownership, provenance, or freedom to operate.

This dataset may not be used for commercial exploitation or commercial deployment. This limitation reflects the fact that the dataset was generated using outputs produced under the Mistral Research License (MRL), under which commercial use is restricted.

Portions of the dataset may be derived from, reference, or be inspired by prior publicly available datasets and other upstream sources, which may be subject to their own license terms, including but not limited to the GNU General Public License. Recipients who access or use this dataset for any purpose assume all risk and sole responsibility for determining and complying with any applicable third‑party rights, licenses, or restrictions.

THIS DATASET IS PROVIDED “AS IS,” WITHOUT WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, ACCURACY, OR NON‑INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR THEIR AFFILIATES BE LIABLE FOR ANY DAMAGES ARISING FROM ACCESS TO OR USE OF THIS DATASET.
