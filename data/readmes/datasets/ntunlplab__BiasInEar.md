---
language:
- en
- zh
- ko
license: apache-2.0
task_categories:
- question-answering
- automatic-speech-recognition
tags:
- speech
- audio
- bias
- robustness
- multilingual
- mmlu
- evaluation
- fairness
pretty_name: BiasInEar
size_categories:
- 10K<n<100K
dataset_info:
  features:
  - name: sample_id
    dtype: string
  - name: subject
    dtype: string
  - name: subject_category
    dtype: string
  - name: order
    dtype: string
  - name: accent
    dtype: string
  - name: question
    dtype: audio
  - name: question_text
    dtype: string
  - name: question_transcription
    dtype: string
  - name: question_wer
    dtype: float32
  - name: question_quality_human_label
    dtype: string
  - name: option_a
    dtype: audio
  - name: option_a_text
    dtype: string
  - name: option_a_transcription
    dtype: string
  - name: option_a_wer
    dtype: float32
  - name: option_a_quality_human_label
    dtype: string
  - name: option_b
    dtype: audio
  - name: option_b_text
    dtype: string
  - name: option_b_transcription
    dtype: string
  - name: option_b_wer
    dtype: float32
  - name: option_b_quality_human_label
    dtype: string
  - name: option_c
    dtype: audio
  - name: option_c_text
    dtype: string
  - name: option_c_transcription
    dtype: string
  - name: option_c_wer
    dtype: float32
  - name: option_c_quality_human_label
    dtype: string
  - name: option_d
    dtype: audio
  - name: option_d_text
    dtype: string
  - name: option_d_transcription
    dtype: string
  - name: option_d_wer
    dtype: float32
  - name: option_d_quality_human_label
    dtype: string
  - name: answer
    dtype: string
  - name: cultural_sensitivity_label
    dtype: string
configs:
- config_name: en_Female
  data_files: en_Female/*.parquet
- config_name: en_Male
  data_files: en_Male/*.parquet
- config_name: zh_Female
  data_files: zh_Female/*.parquet
- config_name: zh_Male
  data_files: zh_Male/*.parquet
- config_name: ko_Female
  data_files: ko_Female/*.parquet
- config_name: ko_Male
  data_files: ko_Male/*.parquet
---

# BiasInEar 🎧

**Assessing Sensitivity in Audio Language Models Across Linguistic, Demographic, and Positional Variations**

[![Paper](https://img.shields.io/badge/Paper-arXiv-red)](https://arxiv.org/abs/2602.01030)
[![GitHub](https://img.shields.io/badge/GitHub-ntunlplab%2FBiasInEar-blue)](https://github.com/ntunlplab/BiasInEar)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](https://www.apache.org/licenses/LICENSE-2.0)

## Dataset Summary

**BiasInEar** is the first systematic benchmark for investigating speech bias in multilingual multimodal large language models (MLLMs). Built upon [Global MMLU Lite](https://huggingface.co/datasets/CohereForAI/Global-MMLU-Lite), this dataset extends text-based questions into spoken inputs, enabling comprehensive analysis of model behavior under diverse audio conditions.

The dataset comprises **70.8 hours** (≈4,249 minutes) of speech across **three languages** (English, Chinese, Korean), with **11,200 questions** balanced by gender and accent. It supports evaluation across linguistic, demographic, and structural dimensions.

## Key Features

- 🌍 **Multilingual**: English, Chinese (Mandarin), and Korean
- 🗣️ **Multi-accent**: 7 distinct accents across languages
- ⚖️ **Balanced**: Equal distribution across gender (male/female) and option order (original/reversed)
- 📊 **Comprehensive**: Covers 43 subjects across 6 categories (STEM, Humanities, Social Sciences, etc.)
- 🏷️ **Annotated**: Includes cultural sensitivity labels (CS/CA) from Global MMLU

## Dataset Statistics

| Attribute | Details |
|-----------|---------|
| Total Duration | 70.8 hours (≈4,249 minutes) |
| Total Questions | 11,200 |
| Languages | English, Chinese, Korean |
| Unique Base Questions | 400 |
| Configurations per Question | Up to 28 |

### Language and Accent Distribution

| Language | Accents | Samples per Gender |
|----------|---------|-------------------|
| English | American, British, Indian | 2,400 |
| Chinese | Beijing Mandarin, Northeastern Mandarin | 1,600 |
| Korean | Seoul, Jeolla | 1,600 |

## Supported Tasks

BiasInEar is designed for:

1. **Spoken Question Answering**: Evaluate MLLM performance on audio-based MCQ tasks
2. **Speech Bias Analysis**: Assess model sensitivity to gender, accent, and language variations
3. **Robustness Evaluation**: Measure consistency under option order perturbations

## Dataset Structure

### Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `sample_id` | string | Unique identifier (format: `{subject}/test/{id}`) |
| `subject` | string | MMLU subject (e.g., astronomy, business_ethics) |
| `subject_category` | string | Category (STEM, Humanities, Social Sciences, Business, Medical, Other) |
| `order` | string | Option order configuration: `original` or `reversed` |
| `accent` | string | Speaker accent (e.g., American, British, Beijing) |
| `question` | audio | Audio file of the spoken question |
| `question_text` | string | Original text of the question |
| `question_transcription` | string | ASR transcription of the audio |
| `question_wer` | float | Word Error Rate of transcription |
| `question_quality_human_label` | string | Human quality rating (Correct/Acceptable/Incorrect)* |
| `option_a/b/c/d` | audio | Audio files for each answer option |
| `option_a/b/c/d_text` | string | Text of each option |
| `option_a/b/c/d_transcription` | string | ASR transcription of each option |
| `option_a/b/c/d_wer` | float | WER for each option |
| `option_a/b/c/d_quality_human_label` | string | Human quality rating for each option* |
| `answer` | string | Correct answer (A, B, C, or D) |
| `cultural_sensitivity_label` | string | `CS` (Culturally Sensitive) or `CA` (Culturally Agnostic) |

> \* **Note on human quality labels**: The `*_quality_human_label` fields are `null` for most samples. Only a small subset of samples were selected through stratified sampling for human evaluation. See the paper for details on the sampling strategy.

### Data Subsets

The dataset is organized into 6 subsets by language and gender:

- `en_Female`: English, Female voice (2,400 samples)
- `en_Male`: English, Male voice (2,400 samples)
- `zh_Female`: Chinese, Female voice (1,600 samples)
- `zh_Male`: Chinese, Male voice (1,600 samples)
- `ko_Female`: Korean, Female voice (1,600 samples)
- `ko_Male`: Korean, Male voice (1,600 samples)

## Usage

This dataset contains only a `test` split for evaluation purposes.

### With `biasinear` package (recommended)

```bash
pip install biasinear[data]
```

```python
from biasinear import load_dataset

# Load all configs merged
dataset = load_dataset()

# Load a specific config
en_female = load_dataset(config="en_Female")
```

### With `datasets` directly

```python
from datasets import load_dataset

# Load English female samples
dataset = load_dataset("ntunlplab/BiasInEar", "en_Female", split="test")

# Load other language/gender combinations
zh_male = load_dataset("ntunlplab/BiasInEar", "zh_Male", split="test")
ko_female = load_dataset("ntunlplab/BiasInEar", "ko_Female", split="test")

# Access a sample
sample = dataset[0]

# Get audio data
question_audio = sample["question"]  # Dict with 'array' and 'sampling_rate'
option_audios = [
    sample["option_a"],
    sample["option_b"],
    sample["option_c"],
    sample["option_d"],
]

# Get metadata
question_text = sample["question_text"]
correct_answer = sample["answer"]
accent = sample["accent"]
order = sample["order"]
subject = sample["subject"]

# Filter by specific conditions
american_samples = dataset.filter(lambda x: x["accent"] == "American")
original_order = dataset.filter(lambda x: x["order"] == "original")
cs_samples = dataset.filter(lambda x: x["cultural_sensitivity_label"] == "CS")
```

## Evaluation Metrics

We propose four complementary metrics for comprehensive robustness evaluation:

### 1. Accuracy
Standard correctness measure for MCQ tasks.

### 2. Question Entropy
Measures uncertainty in model predictions across configurations:

$$H_q = -\sum_{o \in \{A,B,C,D\}} p_q(o) \log_4 p_q(o)$$

### 3. APES (Average Pairwise Entropy Shift)
Quantifies entropy variation across variable levels:

$$\text{APES}_q^v = \frac{2}{L(L-1)} \sum_{l_i, l_j \in L_v, i<j} |H_q^{l_i} - H_q^{l_j}|$$

### 4. Fleiss' Kappa (κ)
Measures categorical agreement across perturbations:

$$\kappa = \frac{\bar{P} - P_e}{1 - P_e}$$

For implementation details, please refer to our [GitHub repository](https://github.com/ntunlplab/BiasInEar).

## Dataset Creation

### Source Data
BiasInEar is built upon [Global MMLU Lite](https://huggingface.co/datasets/CohereForAI/Global-MMLU-Lite), a curated multilingual extension of MMLU with cultural sensitivity annotations.

### Question Rewriting
To ensure natural spoken delivery, questions containing mathematical expressions, domain-specific symbols, or placeholders were rewritten into spoken-readable formats using GPT OSS 120B. For example:
- `H2PO4-` → "Dihydrogen phosphate"
- `(1,2,5,4)(2,3)` → "The permutation consisting of the cycle one–two–five–four, and the cycle two–three"

### Voice Generation
Audio was synthesized using **Gemini 2.5 Flash Preview TTS** with the following configurations:

| Variable | Levels |
|----------|--------|
| Gender | Male (Orus voice), Female (Zephyr voice) |
| English Accents | American, British, Indian |
| Chinese Accents | Beijing Mandarin, Northeastern Mandarin |
| Korean Accents | Seoul, Jeolla |
| Option Order | Original, Reversed |

### Quality Assessment
- **Automatic**: WER-based screening using Whisper Large v3 and Omnilingual ASR
- **Manual**: Stratified sampling with human annotation (Correct/Acceptable/Incorrect)

Quality distribution shows >80% of samples rated as "Correct" across all languages.

## Considerations for Using the Data

### Intended Uses
- Benchmarking MLLM robustness to speech variations
- Studying bias in audio language models
- Developing fairer speech-integrated AI systems
- Academic research on multimodal AI fairness

### Limitations
- Audio is TTS-generated, which may not fully capture natural speech variability
- Accent boundaries are approximations; real-world accents exist on a continuum
- Limited to three languages; results may not generalize to all languages
- Based on MMLU questions, which have known limitations in cultural representation

### Ethical Considerations
- No personally identifiable information is included
- Synthetic voices are used to avoid speaker privacy concerns
- Cultural sensitivity labels are provided to enable responsible evaluation

## Citation

If you use BiasInEar in your research, please cite:

```bibtex
@inproceedings{wei-etal-2026-biasinear,
  title={Bias in the Ear of the Listener: Assessing Sensitivity in Audio Language Models Across Linguistic, Demographic, and Positional Variations},
  author={Wei, Sheng-Lun and Liao, Yu-Ling and Chang, Yen-Hua and Huang, Hen-Hsen and Chen, Hsin-Hsi},
  booktitle={Findings of the Association for Computational Linguistics: EACL 2026},
  year={2026},
  publisher={Association for Computational Linguistics}
}
```

## Authors

- **Sheng-Lun Wei**\* - National Taiwan University
- **Yu-Ling Liao**\* - National Taiwan University  
- **Yen-Hua Chang** - National Taiwan University
- **Hen-Hsen Huang** - Academia Sinica
- **Hsin-Hsi Chen** - National Taiwan University & AINTU

\* Equal contribution

## Acknowledgments

This work was supported by:
- National Science and Technology Council, Taiwan (NSTC 114-2221-E-002-070-MY3, NSTC 113-2634-F-002-003)
- Ministry of Education, Taiwan (NTU-114L900901)

## Contact

For questions or issues, please:
- Open an issue on [GitHub](https://github.com/ntunlplab/BiasInEar)
- Contact: {weisl, ylliao}@nlg.csie.ntu.edu.tw

## License

This dataset is released under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
