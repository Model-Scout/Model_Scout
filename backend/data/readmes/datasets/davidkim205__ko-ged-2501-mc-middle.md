---
language:
- ko
---

# ko-ged-mc-2501-middle

ko-ged-mc-2501-middle is a benchmark dataset designed to evaluate the comprehension and reasoning capabilities of large language models (LLMs) in the Korean language. The dataset comprises **multiple-choice** questions extracted from the General Equivalency Diploma (GED) exams. Specifically, this dataset contains questions from the first GED exam of 2025. All exam items are sourced from the official archives managed by the [Korean Ministry of Education](https://www.gumsi.or.kr/).

## Subject Distribution

| Subject                     | Count |
|:----------------------------|------:|
| Art                         |    25 |
| Ethics                      |    25 |
| Korean                      |    25 |
| Social Studies              |    25 |
| English                     |    24 |
| Technology & Home Economics |    23 |
| Information Technology      |    22 |
| Physical Education          |    20 |
| Math                        |    18 |
| Science                     |    17 |
| Music                       |    15 |

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
    "Question": "다음 ㉠에 해당하는 것은?\n◦ 청소년기의 발달\n- ㉠: 청소년기에 성장 호르몬이 많이 분비되면서 급격히 키가 크고 몸무게가 증가하는 현상",
    "Correct Answer": "성장 급등",
    "Incorrect Answer 1": "자아 정체감",
    "Incorrect Answer 2": "상상적 관중",
    "Incorrect Answer 3": "자기중심적 사고"
  }
]
```
