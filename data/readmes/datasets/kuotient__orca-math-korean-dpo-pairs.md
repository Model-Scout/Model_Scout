---
dataset_info:
  features:
  - name: system
    dtype: string
  - name: question
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 446034878
    num_examples: 192848
  download_size: 162154230
  dataset_size: 446034878
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
axolotl does not take revision arg as an option and i'm lazy so i made this.

type: chatml.intel

## Orca-math-korean-preference

- `question`: orca-math dataset의 question
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