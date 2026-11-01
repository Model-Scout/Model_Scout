---
language:
- ko
---

# ko-gpqa

**ko-gpqa** is a Korean-translated version of the GPQA (Graduate-Level Google‑Proof Q&A) benchmark dataset, which consists of high-difficulty science questions. Introduced in [this paper](https://arxiv.org/pdf/2311.12022), GPQA is designed to go beyond simple fact retrieval and instead test an AI system’s ability to perform deep understanding and logical reasoning. It is particularly useful for evaluating true comprehension and inference capabilities in language models.

 The Korean translation was performed using GPT-4o, and the dataset is formatted in JSON structure.

## Structure

- `id` : a unique identifier for each problem
- `Question` : the question prompt
- `Correct Answer` : the correct answer
- `Incorrect Answer 1`, `Incorrect Answer 2`, `Incorrect Answer 3` : three incorrect choices

```json
[
  {
    "id": "rec06pnAkLOr2t2mp",
    "Question": "에너지 E1과 E2를 가지는 두 양자 상태의 수명이 각각 10^-9초와 10^-8초입니다. 이 두 에너지 준위를 명확히 구분하고자 합니다. 이들이 명확히 구분될 수 있도록 하는 에너지 차이는 다음 보기 중 어느 것입니까?",
    "Correct Answer": "10^-4 eV",
    "Incorrect Answer 1": "10^-11 eV",
    "Incorrect Answer 2": "10^-8 eV",
    "Incorrect Answer 3": "10^-9 eV"
  }
]
```