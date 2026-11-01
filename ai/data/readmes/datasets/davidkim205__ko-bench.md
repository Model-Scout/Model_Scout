---
language:
- ko
---
# ko-bench
To fairly evaluate various LLMs, it is essential to present the same set of questions to all models. This requires a systematically curated benchmark dataset.

[Ko-Bench](https://github.com/davidkim205/ko-bench/blob/main/data/ko_bench/ko_question.jsonl) is a benchmark designed to assess the Korean language proficiency of different LLM models. Existing LLM evaluation datasets often fail to provide accurate assessments within a Korean context. Ko-Bench addresses this limitation by establishing more objective and finely tuned evaluation criteria for Korean LLMs, enabling more reliable performance comparisons.

Ko-Bench is based on the [MT-Bench](https://github.com/lm-sys/FastChat/blob/main/fastchat/llm_judge/data/mt_bench/question.jsonl) dataset but has been translated into Korean. Additionally, its questions have been modified and supplemented to reflect linguistic and cultural characteristics specific to Korean. This enhancement allows for a more accurate evaluation of LLMs in a Korean-language environment.

## ko-bench Generation Rules
Ko-Bench is based on MT-Bench but has been restructured with evaluation criteria optimized for the Korean language environment. To achieve this, the following modifications were applied.
1. Incorporating Geographical and Cultural Elements
Foreign place names, such as "Hawaii," were replaced with Korean landmarks like "Jeju Island" to ensure that Korean LLMs can naturally reflect geographical and cultural aspects in their responses.
2. Enhancing Linguistic Naturalness
Foreign words and expressions such as "casual" and "limerick" were adapted to better fit Korean linguistic conventions, ensuring that questions sound natural in a Korean-language context.
3. Localization of Roleplay Scenarios
Well-known international figures like "Elon Musk" and "Sheldon" were replaced with Korean celebrities such as "Cheon Song-yi" (from the drama My Love from the Star) and "Yoo Jae-suk", allowing the model to be evaluated on its ability to mimic Korean personalities' speech patterns and styles.
4. Applying Korean Standards
Elements such as currency units, names, variable names, company names, and job titles were adjusted to align with Korean conventions, ensuring that models generate contextually appropriate responses in a Korean setting.

## ko-bench Structure
Similar to MT-Bench, Ko-Bench consists of 8 categories, each containing 10 questions, resulting in a total of 80 questions. Each question follows a multi-turn format, meaning that every interaction consists of two consecutive turns, just like in MT-Bench.

- **question_id**: A unique identifier representing the sequence number of the data entry within the dataset.
- **category**: Each question falls into one of the following 8 categories: Coding, Extraction, Humanities, Math, Reasoning, Roleplay, STEM(Science, Technology, Engineering, Mathematics), Writing.
- **pairs**: A set of two question-answer interactions in a multi-turn dialogue.
    - **prompt**: The initial question related to the category.
    - **refer**: The reference answer for the prompt. The LLM’s response does not have to match refer exactly, but it serves as a benchmark for evaluating correctness.
    - **prompt**: A follow-up question that assumes the LLM remembers the context of the previous prompt and its response.
    - **refer**: The reference answer for the second prompt, serving as a guideline for evaluating the LLM's response.

```json
[
  {
    "question_id": 111,
    "category": "math",
    "pairs": [
      {
        "prompt": "삼각형의 꼭짓점은 (0, 0), (-1, 1), (3, 3) 점에 있습니다. 삼각형의 넓이는 얼마입니까?",
        "refer": "삼각형의 넓이는 3입니다."
      },
      {
        "prompt": "삼각형을 둘러싸는 원의 넓이는 얼마입니까?",
        "refer": "5(파이)"
      }
    ]
  }
]
```