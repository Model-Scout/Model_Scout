---
dataset_info:
  features:
  - name: llm
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: question_en
    dtype: string
  - name: answer_en
    dtype: string
  - name: generated
    dtype: string
  - name: label
    dtype: bool
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 1056866134
    num_examples: 192848
  download_size: 388808584
  dataset_size: 1056866134
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-sa-4.0
language:
- ko
size_categories:
- 10K<n<100K
---
## Orca-math-korean-preference

- `llm`: claude-haiku와 gpt3.5로 평가된 generated(Student) answer의 정답 여부
- `question`: orca-math dataset의 question
- `answer`: orca-math dataset의 answer
- `generated`: EEVE-Math-10.8B(M1)의 출력
- `label`: `llm`의 참/거짓 
- `chosen`: `label`이 참일 경우 `answer` 혹은 `generated`의 random.choice, 거짓일 경우 `answer` (Orca-math original paper 참고)
- `rejected`: `label`이 참일 경우 다른 `rejected` value의 random.choice, 거짓일 경우 `rejected` (Orca-math original paper 참고)

## 비고
#### llm_exact_match prompt
```
SYSTEM_PROMPT:
As an expert Math teacher, your role is to evaluate a student’s answer to a word problem.
The problem is accompanied by a correct solution provided by the problem setter.
It is important to remember that there may be various methods to solve a word problem, so the student’s steps might not always align with
those in the problem setter’s solution.
However, the final answer, typically a number, should be unique and match the problem setter’s answer.
Your task involves analyzing the student’s solution to identify any mistakes and determine whether the answer can be modified to correct the error.
If the student’s answer is unfixable, consider creating practice problems to help improve their understanding.
Use the following format:
Error Analysis: In one sentence, extract the final answer from the problem setter’s solution and compare it with the student’s answer.
Do they match?
Final Verdict: Correct/Incorrect

USER_PROMPT:
Question: {question}
Problem Setter's answer: {answer}
Student answer:{rejected}
```
데이터 사용시 출처를 반드시 명시해주시기 바랍니다.