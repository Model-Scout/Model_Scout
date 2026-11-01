---
language:
- ko
---

# ko-ged

The ko-ged dataset is a benchmark designed to evaluate large language models (LLMs) on their ability to comprehend and reason in Korean, using authentic test items from Korea’s official elementary, middle, and high school General Equivalency Diploma (GED) exams. 

## Motivation and Goals of the ko-ged Dataset

**Official Exam-Based Questions**
- The ko-ged dataset is constructed from authentic test items developed by official Korean examination bodies, including those responsible for national equivalency exams and public education assessments. All questions are carefully curated to align with the national curriculum and evaluation standards across elementary, middle, and high school levels.

**Comprehensive and Balanced Subject Coverage**
- ko-ged spans a broad set of academic subjects—Korean, Mathematics, Social Studies, Science, and English. Within each subject, questions are distributed to reflect a balanced range of difficulty levels and cognitive processes, capturing the diversity of skills assessed in standardized and equivalency exams in Korea.

**Detailed Annotations with Answers and Explanations**
- Most items are short-answer questions designed to support automated evaluation, while a subset includes generative tasks for assessing open-ended language capabilities. Each item is annotated with a reference answer and, when applicable, an explanation or rationale. These annotations support flexible evaluation strategies such as exact match scoring, partial credit, and qualitative assessment.

## Subject Distribution

| Subject        | Elementary | Middle | High |
|----------------|-----------:|-------:|-----:|
| Korean         |         10 |     10 |   10 |
| Math           |         10 |     10 |   10 |
| Social Studies |         10 |     10 |   10 |
| Science        |         10 |     10 |   10 |
| English        |         10 |     10 |   10 |


## Structure

The ko-ged follows the structure of the [ko-bench](https://huggingface.co/datasets/davidkim205/ko-bench) dataset but is a single-turn dataset.

```json
[
  {
    "question_id": 1,
    "category": "초등-국어",
    "pairs": [
      {
        "prompt": "다음 낱말들을 모두 포함하는 단어를 쓰세요.\"떡볶이, 만두, 비빔밥, 갈비탕\"",
        "refer": "한식"
      }
    ]
  }
]
```
