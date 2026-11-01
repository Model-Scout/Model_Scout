---
pretty_name: VLM-CCA Korean Culture VQA Dataset
language:
  - ko
  - en
license: cc-by-nc-4.0
tags:
  - visual-question-answering
  - multimodal
  - cultural-knowledge
  - bias-detection
  - temporal-reasoning
  - perspective-analysis
  - korean-culture
  - image-text
  - benchmark
task_categories:
  - visual-question-answering
  - text-generation
size_categories:
  - 1k-10k
annotations_creators:
  - machine-generated
source_datasets:
  - wikimedia-commons
  - google-custom-search
metrics:
  - accuracy
  - success-rate
configs:
  - config_name: default
    data_files:
      - split: test
        path: data/test.parquet
dataset_info:
  total_unique_keywords: 362
  curated_keywords_total: 519
  curated_unique_keywords: 425
  total_images: 1634
  total_questions: 9804
  categories: 15
  task_types:
    cultural_knowledge: 4902
    temporal_reasoning: 1634
    bias_detection: 1634
    perspective_analysis: 1634
---

> [!NOTE]
> **Planned improvements:**
> - Human verification (image - keyword alignment; Q&A / translation)
> - Report VLM performance on this dataset
> - Include image license details in metadata
>
> We welcome your feedback! Please contact us:
> - Lab: isds.sogang@gmail.com
> - Maintainer: bizli0618@sogang.ac.kr

# VLM-CCA Korean Culture VQA Dataset

## Dataset Summary

The Korean Culture VQA Dataset for Visual Language Model's Cultural Context Awareness (VLM-CCA) is a multimodal benchmark designed to evaluate vision-language models on culturally grounded reasoning and bias-awareness. It contains **1,634 images** and **9,804 image-dependent VQA questions** in Korean and English. The benchmark spans 15 cultural categories and four task types.

Images are collected from a curated list of 519 cultural keywords (425 unique across categories). After quality and relevance filtering, 362 distinct keywords remain in the released benchmark.

The dataset supports origin-context questions so that items with historical roots outside Korea are not filtered out when culturally relevant today.

## Visual Examples

Sample images from each task type:

| Task Type | Sample Image | Category |
|-----------|--------------|----------|
| Cultural Knowledge | ![cultural_knowledge](assets/sample_cultural_knowledge.jpg) | Food and Drinks |
| Temporal Reasoning | ![temporal_reasoning](assets/sample_temporal_reasoning.jpg) | Language |
| Bias Detection | ![bias_detection](assets/sample_bias_detection.jpg) | Traditions and Rituals |
| Perspective Analysis | ![perspective_analysis](assets/sample_perspective_analysis.jpg) | Music, Sports and Arts |

## Dataset Distribution

<p align="center">
  <img src="assets/category_distribution.png" alt="Category Distribution" width="600"/>
</p>

<p align="center">
  <img src="assets/task_distribution.png" alt="Task Type Distribution" width="400"/>
  <img src="assets/question_type_distribution.png" alt="Question Type Distribution" width="400"/>
</p>

## Dataset Structure

The dataset is distributed as JSONL records. Each record corresponds to a single VQA item aligned to an image.

**Data Fields**

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier (format: `{CAT}_{hash}_{task}_{idx}`) |
| `image_path` | string | Relative path to image file |
| `question_ko` | string | Korean question text |
| `question_en` | string | English question text |
| `options_ko` | list | Korean answer choices (empty for open-ended/short-answer) |
| `options_en` | list | English answer choices (empty for open-ended/short-answer) |
| `answer_ko` | string | Correct answer (Korean) |
| `answer_en` | string | Correct answer (English) |
| `category` | string | One of 15 cultural categories |
| `difficulty` | string | `easy`, `medium`, or `hard` |
| `task_type` | string | `cultural_knowledge`, `temporal_reasoning`, `bias_detection`, or `perspective_analysis` |
| `question_type` | string | `short_answer`, `multiple_choice`, `true_false`, or `open_ended` |
| `rationale_ko` | string | Korean rationale (bias_detection only) |
| `rationale_en` | string | English rationale (bias_detection only) |
| `metadata` | object | Additional fields (concept_ko, concept_en, source_sample_id) |

**Data Splits**

| Split | Questions | Images |
| --- | ---: | ---: |
| benchmark | 9,804 | 1,634 |

## Task Type Distribution

| Task Type | Questions | Format |
| --- | ---: | --- |
| cultural_knowledge | 4,902 | short_answer, multiple_choice |
| temporal_reasoning | 1,634 | multiple_choice |
| bias_detection | 1,634 | true_false |
| perspective_analysis | 1,634 | open_ended |

## Question Type Distribution

| Question Type | Count |
| --- | ---: |
| multiple_choice | 4,902 |
| open_ended | 1,674 |
| true_false | 1,634 |
| short_answer | 1,594 |

## Data Collection Methodology

1. **Keyword-based image collection**: Images were gathered using curated cultural keywords from Google Custom Search and Wikimedia Commons.
2. **Quality validation**: Images below 256px resolution or outside the 10KB-10MB size range were filtered out.
3. **VLM description generation**: Korean and English image descriptions were generated using GPT-4.1.
4. **Cultural relevance validation**: LLM-based scoring filtered items below a 0.5 cultural relevance threshold.
5. **VQA question generation**: Six questions per image were generated with multiple formats.
6. **Schema normalization**: IDs regenerated for uniqueness, answer/options consistency verified.

## Image-Dependent Question Design

Questions are phrased to anchor answers in the image rather than in a concept label. This design choice:

- Reduces answer leakage from keyword overlap between question and answer.
- Forces visual grounding when multiple concepts share similar cultural contexts.
- Keeps questions valid even when the concept name is unknown to the model or omitted in the image.
- Improves cross-lingual robustness by avoiding reliance on transliterated names.

## Task Definitions

- **Cultural Knowledge**: Identifies cultural artifacts, foods, customs, or symbols in images.
- **Temporal Reasoning**: Requires understanding historical context, seasonal context, or temporal changes related to the image.
- **Bias Detection**: Detects stereotypes, overgeneralizations, or biased framings in image-related statements.
- **Perspective Analysis**: Interprets how perspective or framing affects cultural understanding.

## Category Breakdown

Benchmark distribution by category (images and questions):

| Category | Images | Questions |
| --- | ---: | ---: |
| Architecture | 76 | 456 |
| Economy and Work | 74 | 444 |
| Education | 69 | 414 |
| Entertainment | 67 | 402 |
| Environment and Geography | 88 | 528 |
| Food and Drinks | 258 | 1,548 |
| Greater Community | 136 | 816 |
| Knowledge and Stories | 85 | 510 |
| Language | 42 | 252 |
| Music, Sports and Arts | 312 | 1,872 |
| Politics and Government | 105 | 630 |
| Techniques and Skills | 60 | 360 |
| Tools and Objects | 113 | 678 |
| Traditions and Rituals | 105 | 630 |
| Value | 44 | 264 |

## Intended Uses

- Benchmarking multimodal models on Korean cultural reasoning.
- Bias and perspective analysis in cultural contexts.
- Evaluation data for research on grounded VQA.

## Limitations

- The dataset focuses on Korean cultural content and is not designed for general world knowledge.
- Questions are automatically generated and may contain occasional linguistic artifacts or simplifications.
- **Some images may carry implicit biases from the underlying web sources.**

## Ethical Considerations

- Cultural representations are curated but may still contain incomplete or biased viewpoints.
- Bias-detection tasks rely on framing that could surface sensitive topics; use with care.
- Users should follow original image licenses and attribution requirements.
- The dataset is intended for research and evaluation, not for commercial deployment without additional review.

## Usage Examples

### Loading the Dataset

```python
from datasets import load_dataset

# Load the full dataset
dataset = load_dataset("SOGANG-ISDS/VLM_CCA", split="test")
print(f"Total samples: {len(dataset)}")
```

### Filtering by Task Type

```python
# Filter by task type
cultural_knowledge = dataset.filter(lambda x: x["task_type"] == "cultural_knowledge")
bias_detection = dataset.filter(lambda x: x["task_type"] == "bias_detection")

print(f"Cultural Knowledge: {len(cultural_knowledge)}")
print(f"Bias Detection: {len(bias_detection)}")
```

### Accessing a Sample

```python
sample = dataset[0]
print(f"Question (KO): {sample['question_ko']}")
print(f"Question (EN): {sample['question_en']}")
print(f"Answer: {sample['answer']}")
print(f"Options: {sample['options']}")
print(f"Category: {sample['category']}")
```

### Iterating with Images

```python
from PIL import Image
import os

for sample in dataset.select(range(5)):
    image_path = sample["image_path"]
    # Load image (adjust base path as needed)
    # image = Image.open(os.path.join(base_path, image_path))
    print(f"ID: {sample['id']}, Task: {sample['task_type']}")
```

## Acknowledgments

This work was supported by the Institute of Information & Communications Technology Planning & Evaluation(IITP) grant funded by the Korea government(MSIT) (No. RS-2025-25461932, Elite Research-driven Technology Development for Advanced Large-Scale LLM/VLMs and ASEAN Language Expansion)

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{vlm_cca_korean_culture_vqa,
  title = {VLM-CCA Korean Culture VQA Dataset},
  author = {Sogang University ISDS Lab},
  year = {2025},
  url = {https://huggingface.co/datasets/SOGANG-ISDS/VLM_CCA}
}
```
