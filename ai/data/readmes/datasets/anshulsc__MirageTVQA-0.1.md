---
license: mit
task_categories:
- visual-question-answering
- table-question-answering
language:
- en
- es
- fr
- it
- cs
- ru
- id
- tl
- jv
- su
- bn
- hi
- mr
- si
- ja
- ko
- th
- zh
- nan
- az
- ar
- sc
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
tags:
- table-understanding
- visual-reasoning
- multilingual
- robust-evaluation
pretty_name: MirageTVQA
---

# MirageTVQA: Multilingual Table Visual Question Answering Benchmark

## Dataset Description

**MirageTVQA** is a comprehensive benchmark designed to evaluate Vision-Language Models (VLMs) on realistic table understanding tasks. Unlike existing benchmarks that use clean, English-only tables, MirageTVQA challenges models with:

- 🌍 **24 languages** across diverse linguistic families
- 📸 **Visually imperfect tables** with realistic noise and degradation
- 💡 **Complex reasoning** requiring multi-step inference
- 📊 **~60,000 QA pairs** from diverse domains (scientific, financial, general knowledge)

### Key Features

- **Multilingual Coverage**: 24 languages including English, Spanish, French, Italian, Russian, Chinese, Japanese, Korean, Arabic, Hindi, Bengali, Indonesian, and more
- **Visual Realism**: Tables rendered with 40+ distinct CSS themes and augmented with realistic noise (blur, rotation, compression, scanning artifacts)
- **Diverse Reasoning Types**: 10 reasoning categories including comparative reasoning, numerical aggregation, multi-hop reasoning, temporal reasoning, and more
- **Domain Diversity**: Tables sourced from Wikipedia, arXiv scientific papers, financial documents, and GitHub

## Dataset Structure

### Data Instances

Each instance contains:
- `table_id`: Unique identifier for the table
- `language`: Language code (e.g., 'en', 'es', 'zh_cn')
- `image_clean`: Clean rendered table image
- `image_noisy`: Table image with realistic visual degradation
- `question`: Question text in the target language
- `answer`: Ground truth answer (list of lists format)
- `question_type`: Either 'value' or 'open_ended_reasoning'
- `reasoning_category`: One of 10 reasoning types
- `evidence_cells`: Cells needed to answer (spreadsheet notation)
- `source`: Original data source (arxiv/wikipedia/financial/other)

### Data Splits

The dataset contains approximately 58,480 validated QA pairs across 244 unique tables, each translated into 24 languages.

### Languages

The dataset covers 24 languages from 7 linguistic families:

**Indo-European**: English, Spanish, French, Italian, Russian, Czech, Hindi, Bengali, Marathi, Sinhala, Sardinian

**Sino-Tibetan**: Chinese (Simplified), Hokkien

**Japonic**: Japanese

**Koreanic**: Korean

**Austronesian**: Indonesian (formal & casual), Javanese (Krama & Ngoko), Sundanese, Tagalog

**Afro-Asiatic**: Arabic

**Altaic**: Azerbaijani

**Kra-Dai**: Thai

## Dataset Creation

### Source Data

Tables were collected from:
- **Wikipedia** (WikiSQL): General knowledge tables
- **FinQA**: Financial documents
- **arXiv**: Scientific papers
- **GitHub**: Code documentation and datasets

### Annotation Process

1. **Human seed creation**: Expert annotators created 1 high-quality QA pair per table
2. **LLM expansion**: Gemini 2.5 Pro generated 10 additional diverse QA pairs per table
3. **Translation pipeline**: 
   - Initial translation using Qwen3-32B
   - Refinement using Gemini 2.5 Pro
   - Quality filtering via back-translation BLEU scores
4. **Validation**: Human annotators corrected misclassified pairs

### Visual Augmentation

Tables rendered with 40+ CSS themes and augmented with:
- Geometric distortions (rotation, skew, perspective)
- Quality degradation (Gaussian blur, JPEG compression)
- Scanning artifacts (salt-and-pepper noise, scan lines, shadows)

## Benchmark Results

Performance of leading VLMs on MirageTVQA (English subset, Exact Match %):

| Model | Clean Images | Noisy Images | Performance Drop |
|-------|--------------|--------------|------------------|
| Qwen-2.5-VL 72B | 25.52% | 16.50% | -35.3% |
| Qwen-2.5-VL 32B | 23.15% | 20.36% | -12.1% |
| InternVL3-78B | 27.84% | - | - |
| Qwen3-30B | 20.05% | - | - |

Key findings:
- ⚠️ **Visual fragility**: SOTA models show 35%+ performance drops with realistic noise
- 🌐 **English bias**: Performance degrades significantly for non-English languages
- 📈 **Scale matters**: Larger models consistently outperform smaller ones

## Usage

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("path/to/mirage-tvqa")

# Access examples
example = dataset['train'][0]
print(f"Question: {example['question']}")
print(f"Answer: {example['answer']}")
print(f"Language: {example['language']}")
```

## Citation

If you use MirageTVQA in your research, please cite:

```bibtex
@inproceedings{singh2025mirage,
  title={Lost in Translation and Noise: A Deep Dive into the Failure Modes of VLMs on Real-World Tables},
  author={Singh, Anshul and Chaudhary, Rohan and Singh, Gagneet and Kumar, Abhay},
  booktitle={AI for Tabular Data Workshop at EurIPS},
  year={2025}
}
```

## License

This dataset is released under the MIT License.

## Dataset Card Authors

Anshul Singh, Rohan Chaudhary, Gagneet Singh, Abhay Kumar

## Contact

For questions or issues, please visit: https://github.com/anshulsc/MirageTVQA