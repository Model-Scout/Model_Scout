---
language:
- ko
---

# ko-ged-2501-high

ko-ged-2501-high is a benchmark dataset designed to evaluate the comprehension and reasoning capabilities of large language models (LLMs) in the Korean language. The dataset comprises **multiple-choice** questions extracted from the General Equivalency Diploma (GED) exams. Specifically, this dataset contains questions from the first GED exam of 2025. All exam items are sourced from the official archives managed by the [Korean Ministry of Education](https://www.gumsi.or.kr/).

## Subject Distribution

| Subject                     | Count |
|:----------------------------|------:|
| English                     |    25 |
| Ethics                      |    25 |
| Korean History              |    25 |
| Korean                      |    24 |
| Social Studies              |    24 |
| Technology & Home Economics |    24 |
| Art                         |    23 |
| Physical Education          |    23 |
| Science                     |    23 |
| Math                        |    20 |
| Music                       |    13 |

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
    "Domain": "사회",
    "Question": "다음에서 설명하는 인간, 사회, 환경을 바라보는 관점으로 가장 적절한 것은?\n◦ 시대적 배경과 맥락을 토대로 살펴보는 것\n◦ 과거, 현재, 미래의 상호 연관성을 바탕으로 살펴보는 것",
    "Correct Answer": "시간적 관점",
    "Incorrect Answer 1": "공간적 관점",
    "Incorrect Answer 2": "생태적 관점",
    "Incorrect Answer 3": "윤리적 관점"
  }
]
```
