---
language:
- ko
---

# ko-ged-mc-high

ko-ged-mc-high is a benchmark dataset designed to evaluate the comprehension and reasoning capabilities of large language models (LLMs) in the Korean language. The dataset comprises **multiple-choice** questions extracted from the General Equivalency Diploma (GED) exams. Specifically, this dataset contains questions from the second GED exam of 2024. All exam items are sourced from the official archives managed by the [Korean Ministry of Education](https://www.gumsi.or.kr/).

## Subject Distribution

| Subject                     | Count |
|:----------------------------|------:|
| Art                         |    25 |
| English                     |    25 |
| Ethics                      |    25 |
| Social Studies              |    25 |
| Korean History              |    25 |
| Korean                      |    24 |
| Technology & Home Economics |    24 |
| Physical Education          |    22 |
| Math                        |    19 |
| Science                     |    19 |
| Music                       |    16 |

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
    "Question": "다음 설명에 해당하는 책임 있는 부모의 준비로 가장 적절한 것은?\n◦부부 모두 자녀를 있는 그대로 받아들이고 자녀에게 사랑을 베풀 수 있는 마음의 준비가 되어야 한다.",
    "Correct Answer": "정서적 준비",
    "Incorrect Answer 1": "경제적 준비",
    "Incorrect Answer 2": "신체적 준비",
    "Incorrect Answer 3": "직업적 준비"
  }
]
```
