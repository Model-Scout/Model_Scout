---
language:
- ko
---

# ko-ged-mc-2501-elementary

ko-ged-mc-2501-elementary is a benchmark dataset designed to evaluate the comprehension and reasoning capabilities of large language models (LLMs) in the Korean language. The dataset comprises **multiple-choice** questions extracted from the General Equivalency Diploma (GED) exams. Specifically, this dataset contains questions from the first GED exam of 2025. All exam items are sourced from the official archives managed by the [Korean Ministry of Education](https://www.gumsi.or.kr/).

## Subject Distribution

| Subject            | Count |
|:-------------------|------:|
| Ethics             |    20 |
| Korean             |    20 |
| Practical Arts     |    20 |
| Social Studies     |    19 |
| Science            |    19 |
| English            |    18 |
| Art                |    16 |
| Math               |    16 |
| Physical Education |    14 |
| Music              |    12 |

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
    "Question": "㉠에 들어갈 기관으로 알맞은 것은?\n◦ 질문: 부모님께서 동생의 출생 신고를 하려고 해. 어떤 공공기관에 가는 것이 가장 좋을까?\n◦ 답변: 질문에 해당하는 공공기관은 ㉠입니다. 이곳에서는 출생 신고를 비롯하여 주민등록증 발급 등 주민들의 생활에 필요한 것들을 처리합니다.",
    "Correct Answer": "행정복지센터",
    "Incorrect Answer 1": "경찰서",
    "Incorrect Answer 2": "도서관",
    "Incorrect Answer 3": "소방서"
  }
]
```
