---
language:
- ko
---

# ko-ged-mc-middle

ko-ged-mc-middle is a benchmark dataset designed to evaluate the comprehension and reasoning capabilities of large language models (LLMs) in the Korean language. The dataset comprises **multiple-choice** questions extracted from the General Equivalency Diploma (GED) exams. Specifically, this dataset contains questions from the second GED exam of 2024. All exam items are sourced from the official archives managed by the [Korean Ministry of Education](https://www.gumsi.or.kr/).

## Subject Distribution

| Subject                     | Count |
|:----------------------------|------:|
| Technology & Home Economics |    25 |
| Korean                      |    25 |
| Ethics                      |    25 |
| Social Studies              |    24 |
| English                     |    24 |
| Physical Education          |    24 |
| Science                     |    23 |
| Information Technology      |    22 |
| Art                         |    22 |
| Music                       |    17 |
| Math                        |    14 |

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
    "Domain": "기술가정",
    "Question": "다음 □에 해당하는 용어는?\n□은/는 청소년기에 신체 변화가 나타나는 시기나 진행되는 속도가 개인마다 다른 것을 의미한다.",
    "Correct Answer": "성장의 개인차",
    "Incorrect Answer 1": "양성성",
    "Incorrect Answer 2": "1차 성징",
    "Incorrect Answer 3": "자아 존중감"
  }
]
```
