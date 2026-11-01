---
license: cc-by-4.0
language:
- ko
task_categories:
- question-answering
- text-generation
tags:
- legal
- korean
- terminology
- instruction-tuning
size_categories:
- 10K<n<100K
pretty_name: Korean Legal Terminology Dataset
dataset_info:
  features:
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_examples: 17484
---

# Korean Legal Terminology Dataset

A comprehensive Korean legal terminology dataset designed for fine-tuning language models to understand and explain Korean legal concepts.

## Dataset Description

This dataset contains **17,484 samples** of Korean legal terminology definitions in a question-answer format, specifically designed for instruction-tuning language models in the legal domain.

### Dataset Structure

Each sample consists of:
- **input**: A question asking for an explanation of a legal term (includes Korean term and Chinese characters)
- **output**: A detailed explanation of the legal term in Korean

### Example

```json
{
  "input": "다음 법률 용어(한자: 吸收合倂)를 설명해줘: 흡수합병",
  "output": "법률이 정하는 절차에 의하여 2 이상의 법인 전부 또는 그중 1개의 법인이외의 법인이 해산하여 청산절차를 행하지 않고 소멸하고, 소멸된 법인의 권리의무가 새로이 설립되는 법인 또는 존속하는 법인에게 포괄적으로 승계되는 것을 합병이라고 하며, 합병의 당사자인 법인 중 1법인이 존속하는 경우의 합병을 말한다."
}
```

## Data Sources

This dataset was compiled from three primary Korean legal datasets:

1. **Korean Legal Terminology Dictionary** (~6,000 samples) - [paperw8/korean_legal_terminology](https://huggingface.co/datasets/paperw8/korean_legal_terminology)
   - Columns used: `input` / `output` pairs
   - High-quality legal term definitions with structured Q&A format

2. **Korean Legal Terms** (~2,000 samples) - [Kaggle: koran-legal-terms](https://www.kaggle.com/datasets/gu05087/koran-legal-terms)
   - Columns used: `term` / `description` pairs
   - Legal terminology with detailed explanations

3. **Korea Statute Interpretations** (~9,484 samples) - [ducut91/korea-statute-interpretations](https://huggingface.co/datasets/ducut91/korea-statute-interpretations)
   - Columns used: `title` / `reason` pairs
   - Legal statute interpretations and reasoning

## Data Processing

The dataset underwent the following preprocessing steps:

1. **Collection**: Aggregated legal terminology definitions from the three source databases
2. **Format Standardization**: Converted all entries to a consistent instruction-following format
3. **Prefix Removal**: Cleaned organizational prefixes (e.g., "국토교통부 - ", "감사원 - ") from input entries using regex pattern matching
4. **Quality Control**: Removed duplicate entries and validated data integrity
5. **Encoding**: Ensured proper UTF-8 encoding for all Korean characters and Chinese characters (Hanja)

### Processing Details

- **Pattern Matching**: Used regex pattern `^[가-힣ㆍ·\s]+\s+-\s+` to identify and remove organizational prefixes
- **Deduplication**: Removed duplicate legal term definitions
- **Validation**: Verified all entries contain both input and output fields

## Dataset Statistics

- **Total Samples**: 17,484
- **File Size**: ~63.6 MB
- **Format**: JSON
- **Language**: Korean (with Chinese character annotations)
- **Domain**: Legal terminology and concepts

## Use Cases

This dataset is suitable for:

- Fine-tuning Korean language models for legal domain understanding
- Training legal terminology explanation systems
- Building Korean legal chatbots and Q&A systems
- Developing legal document analysis tools
- Educational applications for Korean law students

## Usage

### Loading the Dataset

```python
import json

# Load the dataset
with open('training_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Example: Print first sample
print(data[0])
```

### Fine-tuning Format

The dataset is already formatted for instruction-tuning. Each sample follows the pattern:

```
Input: "다음 법률 용어(한자: [Chinese characters])를 설명해줘: [Korean term]"
Output: "[Detailed explanation in Korean]"
```

## License

This dataset is released as open-source. Please cite the original data sources when using this dataset:

- paperw8/korean_legal_terminology (Hugging Face)
- gu05087/koran-legal-terms (Kaggle)
- ducut91/korea-statute-interpretations (Hugging Face)

## Citation

If you use this dataset in your research or applications, please cite:

```bibtex
@dataset{korean_legal_terminology_2026,
  title={Korean Legal Terminology Dataset},
  author={flyingcarycoder},
  year={2026},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/datasets/flyingcarycoder/korean-legal-terminology}}
}
```

## Limitations

- The dataset focuses on Korean legal terminology and may not cover all legal concepts
- Explanations are based on Korean law and may not apply to other jurisdictions
- Some terms may have evolved since the data collection period
- The dataset is in Korean and requires Korean language processing capabilities

## Contact

For questions, issues, or contributions, please open an issue on the Hugging Face dataset page.

## Acknowledgments

We acknowledge the following datasets and their creators for providing the source data:
- **paperw8/korean_legal_terminology** - Korean Legal Terminology Dictionary on Hugging Face
- **gu05087/koran-legal-terms** - Korean Legal Terms dataset on Kaggle
- **ducut91/korea-statute-interpretations** - Korea Statute Interpretations on Hugging Face
