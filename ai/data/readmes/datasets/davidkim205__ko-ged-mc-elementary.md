---
language:
- ko
---

# ko-ged-mc-elementary

ko-ged-mc-elementary is a benchmark dataset designed to evaluate the comprehension and reasoning capabilities of large language models (LLMs) in the Korean language. The dataset comprises **multiple-choice** questions extracted from the General Equivalency Diploma (GED) exams. Specifically, this dataset contains questions from the second GED exam of 2024. All exam items are sourced from the official archives managed by the [Korean Ministry of Education](https://www.gumsi.or.kr/).

## Subject Distribution

| Subject            | Count |
|:-------------------|------:|
| Ethics             |    20 |
| Korean             |    20 |
| Social Studies     |    17 |
| Physical Education |    16 |
| Practical Arts     |    16 |
| Science            |    15 |
| Math               |    12 |
| English            |    11 |
| Art                |    10 |
| Music              |     7 |

## Structure

- `id`: a unique positive integer identifier for each question
- `Domain`: subject name
- `Question`: the question prompt
- `Correct Answer`: the correct answer
- `Incorrect Answer 1`, `Incorrect Answer 2`, `Incorrect Answer 3`: three incorrect choices


```json
[
  {
    "id": 1,
    "Domain": "영어",
    "Question": "다음 중 모두 소문자로 쓴 낱말은?",
    "Correct Answer": "jump",
    "Incorrect Answer 1": "Hat",
    "Incorrect Answer 2": "RED",
    "Incorrect Answer 3": "Grapes"
  }
]
```
