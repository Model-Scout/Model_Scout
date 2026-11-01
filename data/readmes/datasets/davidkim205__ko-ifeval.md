---
language:
- ko
---

# ko-ifeval

**Ko-IFEval** is a **human-verified dataset** that translates and adapts [IFEval](https://huggingface.co/datasets/google/IFEval)’s English instructions into Korean, reflecting the linguistic and cultural characteristics of the Korean language.

**Need for Evaluating Instruction-Following in Korean LLMs**

- Instruction-following ability is essential for measuring the practical reliability of large language models (LLMs). Accurate execution of user instructions is a core requirement for real-world applications, making quantitative benchmarks crucial for model evaluation.
- Existing benchmarks like IFEval are designed for English and are not well-suited for Korean. Linguistic features such as ambiguous sentence boundaries, cultural mismatches in translated content, and the lack of Korean-specific datasets hinder accurate and fair evaluation of Korean LLMs.
- Ko-IFEval provides a human-verified dataset and an evaluation tool tailored for Korean. By reflecting Korean linguistic and cultural characteristics, it enables more precise and fair assessment of instruction-following performance in Korean LLMs.


## Dataset Construction

Ko-IFEval was constructed through the following three steps:
1) translation of prompts using GPT-4o
2) removal and modification of conditions incompatible with Korean linguistic structures
3) adaptation of prompts to reflect Korean cultural context

### Removed Categories 
We excluded categories relying on English-specific linguistic features or irrelevant for Korean evaluation:

- **English-dependent categories**: `change_case:capital_word_frequency`, `change_case:english_capital`, `change_case:english_lowercase`
- **Korean-irrelevant category**: `language:response_language`

### Post-translation Adjustments


- **Clarifying word count vs. character count**:
  The `length_constraints:number_words` category was translated to refer to "어절" (space-separated word units in Korean). To support character-based constraints, a separate condition, `length_constraints:number_letters`, was introduced.

- **Adjusting paragraph and quotation conditions**:
  When both `length_constraints:nth_paragraph_first_word` and `startend:quotation` conditions co-occur, the paragraph indices were adjusted to avoid logical conflicts.

- **Refining letter frequency constraints**:
  In `keywords:letter_frequency`, thresholds were calibrated to better fit the distribution of characters in Korean. When literal application would cause excessive difficulty, thresholds were adjusted. For example, a prompt requiring a high frequency of the letter "o" was adapted as follows:
  ```
  # Original
  Write a letter to your friend who recently moved away. Your entire response should be in English, and in all capital letters. The letter o should appear at least 40 times.
  
  # Modified
  최근 이사 간 친구에게 편지를 써주세요. 글자 '오'를 최소 13번 이상 포함해야 합니다.
  ```

- **Restricting constraint combinations**:
   The `combination:repeat_prompt` condition enforces that the response must begin with the prompt itself. Therefore, it is only paired with `length_constraints:number_sentences`, `length_constraints:number_words`, or `length_constraints:number_letters` constraints.

- **Adapting to Korean cultural context**:
    Unfamiliar names and culturally irrelevant topics in prompts were replaced with localized content.
    
    ```
    # Original
    Write a 300+ word summary of the wikipedia page "https://en.wikipedia.org/wiki/Raymond_III,_Count_of_Tripoli".
    
    # Modified
    위키백과 페이지 "https://ko.wikipedia.org/wiki/이순신"의 내용을 요약하여 300자 이상으로 작성하시오.
    ```

## Structure

The ko-ifeval is based on the structure of the IFEval dataset.
- key: A unique ID for the prompt.
- prompt: Describes the task the model should perform.
- instruction_id_list: An array of verifiable instructions. See Table 1 of the paper for the full set with their descriptions.
- kwargs: An array of arguments used to specify each verifiable instruction in instruction_id_list.

```json
[
  {
    "id": 1000,
    "prompt": "위키백과 페이지 \"https://ko.wikipedia.org/wiki/이순신\"의 내용을 요약하여 300자 이상으로 작성하시오. 쉼표를 사용하지 말고, 최소 3개의 섹션 제목을 마크다운 형식으로 강조하시오. 예: *강조된 섹션 1*, *강조된 섹션 2*, *강조된 섹션 3*.",
    "instruction_id_list": [
      "punctuation:no_comma",
      "detectable_format:number_highlighted_sections",
      "length_constraints:number_letters"
    ],
    "kwargs": [
      {},
      {
        "num_highlights": 3
      },
      {
        "relation": "at least",
        "num_letters": 300
      }
    ]
  }
]
```
