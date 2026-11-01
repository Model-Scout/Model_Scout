---
license: apache-2.0
task_categories:
  - question-answering
  - multiple-choice
language:
  - ko
size_categories:
  - n<1K
tags:
  - korean-culture
  - cultural-understanding
  - mcqa
pretty_name: K-Culture Contextual Understanding Benchmark
---

# K-Culture Contextual Understanding Benchmark

A Korean cultural understanding benchmark dataset featuring 530 scenario-based multiple-choice questions designed to evaluate models' contextual understanding of Korean culture.

## Dataset Description

**K-Culture Contextual Understanding Benchmark** is a dataset designed to evaluate LLMs' understanding of Korean cultural contexts through realistic scenarios and dialogues. Each item contains a cultural description, a scenario depicting real-life situations, and a multiple-choice question with detailed explanation.

- **Language:** Korean (ko)
- **Size:** 530 items
- **Task:** Multiple Choice Question Answering (MCQA)
- **Version:** v1.0

## Dataset Structure

### Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `DescriptionID` | int | Unique identifier for each item |
| `Description` | string | A concise description of a Korean cultural phenomenon |
| `ScenarioBody` | string | A realistic scenario illustrating the cultural context |
| `MCQA` | object | Multiple-choice question and answer |
| `MCQA.Question` | string | The question based on the scenario |
| `MCQA.Choices` | string | Four answer choices (A, B, C, D) |
| `MCQA.Answer` | string | The correct answer (A, B, C, or D) |
| `MCQA.Explanation` | string | Explanation of why the answer is correct and others are not |
| `Type` | string | Question type category (1, 2, or 3) |
| `Category` | string | Cultural domain category |

### Data Instance

```json
{
  "DescriptionID": 1,
  "Description": "한국의 야구장에서는 관중들이 다함께 응원가를 부르고, 춤을 춘다.",
  "ScenarioBody": "지윤은 미국에서 온 교환학생 에밀리와 함께...",
  "MCQA": {
    "Question": "에밀리의 SNS 글과 그에 대한 대화에서, 에밀리가 인상적으로 느낀 점에 가장 부합하는 것은?",
    "Choices": "A. 팬들이 경기 내내 적극적으로 노래와 율동에 참여하는 분위기\nB. 응원단과 치어리더가 경기 중간마다 공연을 펼치는 점\nC. 다양한 간식과 음료를 즐기며 경기를 관람하는 문화\nD. 관중들이 특정 시간에만 단체로 노래를 부르는 모습",
    "Answer": "A",
    "Explanation": "- 정답이 되는 이유: 에밀리는 SNS에 \"콘서트에 다녀온 것 같다\"라고 표현하고..."
  },
  "Type": "1",
  "Category": "Music, Sports and Arts"
}
```

## Question Types

| Type | Description | Count |
|------|-------------|-------|
| Type 1 | Can the model correctly compare similarities and differences between Korean culture and similar foreign cultures? | 290 |
| Type 2 | Does the model understand the differences between similar concepts within Korean culture? | 101 |
| Type 3 | Does the model understand context shared only by specific groups within Korea? | 139 |

## Categories

The dataset covers 15 cultural domains:

| Category | Count |
|----------|-------|
| Food and Drinks | 127 |
| Traditions and Rituals | 68 |
| Knowledge and Stories | 58 |
| Tools and Objects | 50 |
| Music, Sports and Arts | 45 |
| Language | 34 |
| Architecture | 29 |
| Economy and Work | 25 |
| Politics and Government | 19 |
| Environment and Geography | 18 |
| Greater Community | 18 |
| Values | 18 |
| Techniques and Skills | 10 |
| Education | 7 |
| Entertainment | 4 |

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

dataset = load_dataset("SOGANG-ISDS/K-Culture-Desc")
```

### Example Usage

```python
from datasets import load_dataset

# Load dataset
dataset = load_dataset("SOGANG-ISDS/K-Culture-Desc")

# Access a sample
sample = dataset['test'][0]
print(f"Description: {sample['Description']}")
print(f"Question: {sample['MCQA']['Question']}")
print(f"Choices: {sample['MCQA']['Choices']}")
print(f"Answer: {sample['MCQA']['Answer']}")
```

### Evaluation Example

```python
def evaluate_model_response(model_answer: str, correct_answer: str) -> bool:
    """Check if model's answer matches the correct answer."""
    return model_answer.strip().upper() == correct_answer.strip().upper()

# Example
correct = evaluate_model_response("A", sample['MCQA']['Answer'])
print(f"Correct: {correct}")
```

## Acknowledgments

This work was supported by Institute of Information & communications Technology Planning & Evaluation (IITP) grant funded by the Korea government (MSIT) (No.RS-2024-00343989, Enhancing the Ethics of Data Characteristics and Generation AI Models for Social and Ethical Learning).

## Citation

```bibtex
@dataset{k_culture_2025,
  title={A Korean Cultural Understanding Benchmark Dataset with Detailed Scenario},
  year={2025},
  url={https://huggingface.co/datasets/SOGANG-ISDS/K-Culture-Desc}
}
```

## License

This dataset is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
