---
license: mit
task_categories:
- text-generation
language:
- ko
size_categories:
- n<1K
---

# KoInFoBench

KoInFoBench is a specialized evaluation dataset designed to assess the performance of Large Language Models (LLMs) on capabilities of Korean instructions following.<br>
The current version of `KoInFoBench` consists of 60 instruction sets and 233 questions.

Inspired by [InFoBench](https://huggingface.co/datasets/kqsong/InFoBench) dataset, we extends their concpet by focusing on the nuances and features of Korean language.

 - 🖥️ Code to reproduce or evaluate own LLMs is available at [https://github.com/KIFAI/KoInFoBench](https://github.com/KIFAI/KoInFoBench)
 - 📄 Paper is under writing and open soon!

### 🚀 Update
- **2024.05.18**: add other results `gpt-4o-2024-05-13`, `claude-3-sonnet-20240229`, `solar-1-mini-chat`

## Dataset Overview

### Usage
```python
from datasets import load_dataset

dataset = load_dataset('kifai/KoInFoBench')
```

### Example
```json
{
  "id": "19",
  "subset": "input_intensive_set",
  "category": "구글캘린더",
  "instruction": "다음은 해외 콘서트 참가 확정에 대한 영문으로 작성된 이메일입니다. 한국시간(KST) 기준으로 참가 확정된 날짜, 콘서트 날짜와 시간을 \"년-월-일 시간\" 형식으로 작성하고 한국시간 기준으로 참가 확정일로부터 콘서트 날짜까지 몇 일 남았는지 계산하여 국문으로 정답을 함께 작성합니다.",
  "input": "Email: We are pleased to inform you that your concert ticket purchase has been successfully confirmed at approximately 11am GMT today (26 March 2024). The concert you have been eagerly awaiting is scheduled to take place on 17 September 2024, starting at 6 PM UTC+2. Please mark your calendar and prepare to join us for an unforgettable evening of live music and entertainment. Your ticket grants you access to a night filled with exceptional performances, engaging visuals, and the vibrant energy of live music. We recommend arriving early to enjoy the full experience, including pre-concert activities and amenities.",
  "decomposed_questions": [
    "답변은 해외 콘서트 참가 일정에 대한 내용이 포함되어 있습니까?",
    "답변으로 작성된 모든 일정은 한국시간(KST) 기준으로 작성되었습니까?",
    "콘서트 참가가 확정된 날짜 그리고 콘서트 날짜와 시간 2개의 일정을 모두 포함합니까?",
    "날짜와 시간이 \"년-월-일 시간\" 형식으로 올바르게 작성되었습니까?",
    "콘서트 확정일로부터 콘서트까지 남은 기간은 콘서트 시작일을 포함할 경우 177일, 미포함인 경우 176일입니다. 남은 기간을 176일 혹은 177일로 계산하였습니까?"
  ],
 "question_label": [
    "Format",
    "Format, Content",
    "Format",
    "Format",
    "Number"
  ],
 "ref": ""
}
```

### Fields
- **id**: unique identifier for each entry in the dataset
- **subset**: include `input_intensive_set` and `instruction_intensive_set`. where "intensive" indicates the entry's focus on evaluating Korean specific input or detailed instruction following
- **category**: a string which each entry belongs. For example, '구글캘린더' indicates that the entry is related to tasks associated with Google Calander
- **instruction**: a string containing instructions
- **input**: a string containing context information and can be empty
- **decomposed_questions**: a list of string questions that decompose the task related to the entry. Each question is designed to evaluate the response of LLM
- **question_label**: a list of string labels that identify the type of each decomposed question. Each lable belong to multiple aspects, such as Format, Content, Number, Linguistic, Style
- **ref**: references a string for references or additional information and it could be empty


## Evaluation Result

### DRFR
Decomposed Requirements Following Ratio(DRFR) is the metric to evaluate how LLMs accurately respond to the instruction/input.
This metric calculates the average accuracy across answers to the decomposed questions for each instruction.
The following is the summary of the model performance on our dataset.

| Model                                       | H_DRFR     | A_DRFR | Alignment |
|------------------------------               |--------    |--------|-----------|
| **claude-3-opus-20240229**                  | **0.854**  | 0.850  | 87%       |
| **gpt-4-turbo-2024-04-09**                  | 0.850      | 0.880  | 87%       |
| **gpt-4o-2024-05-13**                       | 0.850      | 0.863  | 89%       |
| **gpt-4-0125-preview**                      | 0.824      | 0.824  | 83%       |
| **claude-3-sonnet-20240229**                | 0.790      | 0.828  | 84%       |
| **gemini-1.5-pro**                          | 0.773      | 0.811  | 83%       |
| **meta-llama/Meta-Llama-3-70B-Instruct-**   | 0.747      | 0.863  | 84%       |
| **hpx003**                                  | 0.691      | 0.738  | 83%       |
| **gpt-3.5-turbo-0125**                      | 0.678      | 0.734  | 82%       |
| **solar-1-mini-chat**                       | 0.614      | 0.695  | 79%       |
| **yanolja/EEVE-Korean-Instruct-10.8B-v1.0** | 0.597      | 0.730  | 79%       |`

- `H_DRFR`: The accuracy of model responses as evaluated by the human expert
- `A_DRFR`: The accuracy of model responses automatically evaluated by GPT-4 as employing the capability of LLM-as-a-judge
- `Alignment`: The degree of agreement or consistency between the human and automated evaluation

> Please note that the evaluation results of the LLMs presented in the above table may vary due to its randomness.

## Additional Information

### License Information

This dataset is released under the [MIT LISENCE](https://github.com/KIFAI/KoInfoBench/blob/main/LICENSE)

### Citation Information
```
@article{,
      title={KoInFoBench}, 
      author={Sungwoo Oh, Sungjun Kown, Donggyu Kim},
      year={2024},
      eprint={},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
