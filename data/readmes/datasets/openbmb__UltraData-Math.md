---
language:
- en
- zh
license: apache-2.0
size_categories:
- 100B<n<1T
task_categories:
- text-generation
pretty_name: UltraData-Math
arxiv: xxxx.xxxxx
tags:
- llm
- pretraining
- math
- data-synthesis
- data-filtering
- high-quality
- mathematical-reasoning
configs:
- config_name: UltraData-Math-L3-Conversation-Synthetic
  data_files: "data/UltraData-Math-L3/Conversation-Synthetic/*.parquet"
- config_name: UltraData-Math-L3-Multi-Style-Synthetic
  data_files: "data/UltraData-Math-L3/Multi-Style-Synthetic/*.parquet"
- config_name: UltraData-Math-L3-QA-Synthetic
  data_files: "data/UltraData-Math-L3/QA-Synthetic/*.parquet"
- config_name: UltraData-Math-L3-Textbook-Exercise-Synthetic
  data_files: "data/UltraData-Math-L3/Textbook-Exercise-Synthetic/*.parquet"
- config_name: UltraData-Math-L2-preview
  data_files: "data/UltraData-Math-L2-preview/**/*.parquet"
- config_name: UltraData-Math-L1
  data_files: "data/UltraData-Math-L1/**/*.parquet"
default_config_name: UltraData-Math-L3-Conversation-Synthetic
---

# UltraData-Math

<div align="center">
  <img src="assets/ultradata-math-logo.png" width="600"/>
</div>

<p align="center">
<a href="https://huggingface.co/datasets/openbmb/UltraData-Math">🤗 Dataset</a> | <a href="https://github.com/UltraData-OpenBMB/UltraData-Math">💻 Source Code</a> | <a href="https://huggingface.co/datasets/openbmb/UltraData-Math/blob/main/README_ZH.md">🇨🇳 中文 README</a>
</p>

***UltraData-Math*** is a large-scale, high-quality mathematical pre-training dataset totaling **290B+ tokens** across three progressive tiers—**L1** (170.5B tokens web corpus), **L2** (33.7B tokens quality-selected), and **L3** (88B tokens multi-format refined)—designed to systematically enhance mathematical reasoning in LLMs. It has been applied to the mathematical pre-training of the [MiniCPM Series](https://huggingface.co/collections/openbmb/minicpm4) models.

It was introduced in the paper [Data Science and Technology Towards AGI Part I: Tiered Data Management](https://huggingface.co/papers/2602.09003).

## 🆕 What's New

- **[2026.02.09]**: **UltraData-Math**, a large-scale high-quality mathematical pre-training dataset with 290B+ tokens across three progressive tiers (L1/L2-preview/L3), is now available on Hugging Face. Released as part of the [UltraData](https://ultradata.openbmb.cn/) ecosystem. 🔥🔥🔥
- **[2026.02.10]**: **UltraData-Math** tops the Hugging Face Datasets Trending list, reaching the #1 spot! ⭐️⭐️⭐️

## 📚 Introduction

High-quality pre-training data is crucial for enhancing the mathematical reasoning capabilities of large language models (LLMs). However, existing mathematical pre-training data construction schemes have the following shortcomings:

- **HTML Parsing**: General parsers (such as trafilatura, readability) are mainly designed for news/article parsing, lacking specialized processing for mathematical formulas and other content, often leading to formula structure destruction or loss; meanwhile, mathematical discussions on forum-like pages are difficult to extract completely.
- **Data Quality**: Existing datasets generally lack a systematic quality grading mechanism, with high-value mathematical content mixed with low-quality noise.
- **Data Diversity**: Mainstream datasets mostly originate from textbooks or competition question banks, lacking mathematical discussions and application scenarios in real web pages; synthetic data formats are single, difficult to cover diverse needs such as multi-turn dialogues and multi-style expressions.

To address these issues, we propose ***UltraData-Math***—a large-scale high-quality pre-training dataset for mathematical reasoning tasks. This dataset is developed based on the [UltraData](https://ultradata.openbmb.cn/blog/position-paper) L0-L4 Tiered Data Management Framework, containing four progressive levels:

- **L0 Raw Data**: Develops a mathematical parser based on *magic-html*, combined with *w3m* layout preservation rendering and multi-level fallback strategies, standardizing MathML, KaTeX, and AsciiMath into LaTeX format.
- **L1 Filtered Data**: Cleans noise through heuristic rules and performs document-level deduplication.
- **L2 Selected Data**: Uses proprietary large models to annotate seed data and distills it into a lightweight embedding classifier to achieve efficient quality grading of the full corpus.
- **L3 Refined Data**: Produces structured content with clear reasoning through rewriting, synthetic generation, and refinement in various formats such as Q&A, multi-turn dialogues, multi-style rewriting, and knowledge-grounded textbooks.

Experiments show that on the MiniCPM-1.2B architecture, ***UltraData-Math*** achieves a score of **37.02pp** on the MATH500 benchmark, an improvement of **+3.62pp** compared to Nemotron-CC 4plus; it achieves **61.79pp** on GSM8K, an improvement of **+3.34pp**, while maintaining code generation and general knowledge capabilities.

***UltraData-Math*** has been applied to the mathematical pre-training of the [MiniCPM Series](https://huggingface.co/collections/openbmb/minicpm-4-6841ab29d180257e940baa9b) models.

- **[UltraData-Math-L1](https://huggingface.co/datasets/openbmb/UltraData-Math)**: Large-scale high-quality mathematical pre-training dataset, containing 170.5B tokens of web mathematical corpus. 
- **[UltraData-Math-L2](https://huggingface.co/datasets/openbmb/UltraData-Math-L2)**: High-quality mathematical pre-training dataset selected by the quality model, containing 33.7B tokens of high-quality web mathematical corpus.
- **[UltraData-Math-L3](https://huggingface.co/datasets/openbmb/UltraData-Math-L3)**: High-quality refined mathematical dataset, containing 88B tokens of multi-format refined data (Q&A, multi-turn dialogues, knowledge textbooks, etc.).

## 🏗️ Data Processing Pipeline

To break through the limitations of existing mathematical datasets in quality and diversity, we established a refined grading standard centered on "mathematical content integrity" and "information density". ***UltraData-Math*** adopts the **L0-L4 Tiered Data Management Framework** proposed by the [UltraData](https://ultradata.openbmb.cn/blog/position-paper) paper. Through standardized level definitions, it achieves orderly management and efficient flow of mathematical data assets. Each level represents higher data purity and mathematical value, while also corresponding to a more refined degree of processing.

<div align="center">
  <img src="assets/ultradata-math-pipeline.png" width="900"/>
</div>

### L0: Raw Data Parsing and Standardization

**Goal**: Address the poor support of general HTML parsers for mathematical formulas and maximize the preservation of mathematical semantics in web pages.

The L0 phase mainly processes raw web data obtained from sources such as Common Crawl. Given the specificity of mathematical web pages, we develop specialized parsing strategies through the [UltraData-Math-Parser](https://huggingface.co/spaces/openbmb/UltraData-Math-L0-Parser) instead of directly using general parsers like trafilatura or readability.

- **Unified Parsing Mode**: Automatically identifies page types to ensure complete content extraction as much as possible.
- **Multi-level Fallback Strategy**: To prevent data loss due to parsing failures, we implement a multi-level fallback mechanism to ensure text content is captured even if structured parsing fails.
- **Mathematical Formula Standardization**: We unify different mathematical expressions in web pages into standard LaTeX format, achieving data format normalization for unified model learning.

### L1: Heuristic Cleaning and Filtering

**Goal**: Remove format noise and improve data readability and standardization.

After obtaining text containing complete mathematical formulas, we clean the L0 data through a series of heuristic rules:

- **Format Repair**:
  - Clean invisible characters, garbled text, and unnatural continuous line breaks.
  - Remove irrelevant web noise such as navigation bars, footers, ad pop-ups, and "read more".
- **Content Filtering**:
  - *Length Filtering*: Remove overly short text fragments, which usually lack context and are difficult to support effective mathematical reasoning training.
  - *Language Identification*: Ensure the dataset is composed mainly of high-quality English and Chinese mathematical content.
  - *Document Deduplication*: Perform deduplication at the document level to prevent duplicate content from biasing model training.

### L2: Selection Based on Quality Models

**Goal**: Identify core corpora with high value from massive data.

Although L1 data has a clean format, the content quality varies. The L2 phase introduces a model-based quality assessment system:

- **Seed Data Annotation**: Use proprietary large models to score a portion of seed data across multiple dimensions.
- **Classifier Training and Distillation**: Train lightweight embedding classifiers based on annotated data to equip them with the ability to identify high-value mathematical content.
- **Full-scale Inference**: Use the trained classifier to score and screen L1 data in full.
  - *Retention*: Content containing detailed problem-solving steps, mathematical concept explanations, and high-level academic discussions.
  - *Exclusion*: Simple stacking of nouns, meaningless lists of numbers, juvenile content, or noise from non-mathematical fields.

### L3: Refined Data

**Goal**: Produce structured content with clear reasoning and explicit educational intent through rewriting, synthetic generation, and refinement, achieving textbook-quality standards and ensuring maximum learnability.

Natural web data is mostly declarative text, lacking structured reasoning steps and diverse pedagogical formats. To enhance the model's chain-of-thought (CoT) capabilities and multi-turn interaction skills, we build the L3 refined data layer through the [UltraData-Math-Generator](https://huggingface.co/spaces/openbmb/UltraData-Math-L3-Generator):

- **Q&A Pair Generation**: Use high-performance models to rewrite declarative documents into "Question-Answer" pairs, constructing QA-style data with explicit reasoning steps.
- **Multi-turn Dialogue Synthesis**: Simulate "Teacher-Student" tutoring scenarios to generate multi-turn dialogue data containing follow-up questions, corrections, and guidance.
- **Multi-style Rewriting**: Rewrite single-source data into multiple styles (such as rigorous textbook style, competition problem-solving style, intuitive popular science style) to improve model generalization.
- **Knowledge Point Textbook Generation**: Generate systematic textbook-like content based on specific knowledge points to ensure the model masters core mathematical concepts.
- **Format Repair and Enhancement**: Fix formatting issues in the source data (e.g., broken LaTeX formulas, inconsistent notation) and enhance content coherence to achieve textbook-quality standards.

Based on the above methodology, we produce the following ***UltraData-Math*** datasets:

| Dataset | # Tokens | # Documents |
|:---|:---:|:---:|
| UltraData-Math-L1 | 170.5B | 85.6M |
| UltraData-Math-L2-preview | 33.7B | 14.98M |
| UltraData-Math-L3 | 88B | 81.4M |

## 🚀 Quick Start

You can load the dataset directly from Hugging Face:

```python
from datasets import load_dataset

# Load UltraData-Math-L1
ds = load_dataset("openbmb/UltraData-Math", "UltraData-Math-L1")

# Load UltraData-Math-L2-preview
ds = load_dataset("openbmb/UltraData-Math", "UltraData-Math-L2-preview")

# Load UltraData-Math-L3 (default: Conversation-Synthetic)
ds = load_dataset("openbmb/UltraData-Math", "UltraData-Math-L3-Conversation-Synthetic")

# Other L3 configs:
# - UltraData-Math-L3-Multi-Style-Synthetic
# - UltraData-Math-L3-QA-Synthetic
# - UltraData-Math-L3-Textbook-Exercise-Synthetic
```

## 📈 Experimental Results

We evaluated data quality using the **Decay Verification** method: continuing pre-training of a **MiniCPM-1.2B** base model (pre-trained on 1.3T tokens with **MiniCPM3-4B** tokenizer) with **~100B tokens** (30% target data + 70% general data). We used [OpenCompass](https://github.com/open-compass/opencompass) as our evaluation framework. Evaluation benchmarks include:

- **General English:** MMLU, ARC-E, ARC-C, BigBench Hard (BBH), CommonSenseQA, HellaSwag, OpenbookQA, PIQA, SIQA, Winogrande
- **General Chinese:** C-Eval, CMMLU
- **Math Reasoning:** MATH500, GSM8K, Math-Bench, R-Bench-Math
- **Code Reasoning:** MBPP, HumanEval

### Effectiveness of L0 Parsing Strategy

To fairly compare different parsing strategies, we conducted experiments on a data subset sampled from the **2023-2024** distribution. We re-parsed the raw HTML from this source using different parsers. This comparison demonstrates the **effectiveness of our L0 Parser** against other parsers.

<div align="center">
  <img src="assets/ultradata-math-l0-parser-comparison.png" width="700"/>
</div>


### Pipeline Effectiveness (L1 vs L2 vs L3)

To validate the effectiveness of our L0-L3 tiered framework, we conducted ablation studies comparing models trained on different tiers of UltraData-Math. Unlike the L0 parser comparison above (which used a 2023-2024 subset), these results are based on the **full dataset**. Results demonstrate that higher-tier data (L3) significantly boosts mathematical reasoning (MATH500, GSM8K) and general capabilities.

<div align="center">
  <img src="assets/ultradata-math-l1l2l3-comparison.png" width="700"/>
</div>

### Full Evaluation Results

To compare against existing public mathematical pre-training datasets, we trained models independently on each dataset using the same model architecture and training budget (~100B tokens). The baselines include [Nemotron-CC-Math](https://huggingface.co/datasets/nvidia/Nemotron-CC-Math-v1), [MegaMath-Web-Pro](https://huggingface.co/datasets/LLM360/MegaMath), and [FineMath](https://huggingface.co/datasets/HuggingFaceTB/finemath). All models are evaluated under identical conditions for a fair comparison:

<div align="center">
  <img src="assets/ultradata-math-full-comparison.png" width="700"/>
</div>

## ❤️ Acknowledgements

- **L0 Parsing Layer**: [magic-html](https://github.com/opendatalab/magic-html), [w3m](http://w3m.sourceforge.net/), [trafilatura](https://github.com/adbar/trafilatura)
- **L3 Synthesis Layer**: [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct), [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B), [GLM-4.5](https://huggingface.co/zai-org/GLM-4.5)
- **Seed Data**: [Nemotron-CC-Math](https://huggingface.co/datasets/nvidia/Nemotron-CC-Math-v1), [MegaMath](https://huggingface.co/datasets/LLM360/MegaMath), [FineMath](https://huggingface.co/datasets/HuggingFaceTB/finemath)

## 📖 Citation

If you find **UltraData-Math** useful in your research, please consider citing:

```bibtex
@misc{ultradata-math,
  title={UltraData-Math},
  author={Chuyue Zhou and Hongya Lyu and Xinle Lin and Hengyu Zhao and Junshao Guo and Xueren Zhang and Shuaikang Xue and Qiang Ma and Jie Zhou and Yudong Wang and Zhiyuan Liu},
  year={2026},
  url={https://huggingface.co/datasets/openbmb/UltraData-Math},
  publisher={Hugging Face}
}
```

## 📜 License

This project is licensed under the [Apache 2.0](./LICENSE) license.
