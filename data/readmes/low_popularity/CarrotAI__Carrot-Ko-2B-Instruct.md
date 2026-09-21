---
license: mit
datasets:
- CarrotAI/ko-instruction-dataset
language:
- ko
---

## Model Details

생성한 한국어 데이터셋으로 axolotl을 이용하여 파인튜닝하였습니다.

[LogicKor](https://lk.instruct.kr/)에서 2.1B의 파라메터로 default 기준 4.21점을 기록하였습니다.

아직 실험중인 모델입니다.

### Model Description

Qwen/Qwen2-1.5B-Instruct 모델을 이용하여 생성하였습니다.

### LogicKor

default

| Category | Single turn | Multi turn |
|----------|-------------|------------|
| 이해 (Understanding) | 6.14 | 5.43 |
| 문법 (Grammar) | 5.00 | 2.43 |
| 수학 (Math) | 1.86 | 1.86 |
| 추론 (Reasoning) | 5.57 | 2.14 |
| 코딩 (Coding) | 3.57 | 3.71 |
| 글쓰기 (Writing) | 6.00 | 6.86 |

| Category | Score |
|----------|------|
| Single turn | 4.69 |
| Multi turn | 3.74 |
| Overall | 4.21 |



1-shot

| Category | Single turn | Multi turn |
|---|---|---|
| 추론(Reasoning) | 4.14 | 1.43 |
| 수학(Math) | 2.86 | 1.00 |
| 글쓰기(Writing) | 5.00 | 4.57 |
| 코딩(Coding) | 3.14 | 3.43 |
| 이해(Understanding) | 4.29 | 3.71 |
| 문법(Grammar) | 2.71 | 1.43 |

| Category | Score |
|---|---|
| Single turn | 3.69 |
| Multi turn | 2.60 |
| Overall | 3.14 |

cot-1-shot
| Category | Single turn | Multi turn |
|---|---|---|
| 추론(Reasoning) | 3.00 | 2.86 |
| 수학(Math) | 1.57 | 1.00 |
| 글쓰기(Writing) | 5.86 | 6.00 |
| 코딩(Coding) | 4.29 | 4.14 |
| 이해(Understanding) | 3.43 | 3.43 |
| 문법(Grammar) | 3.00 | 1.14 |

| Category | Score |
|---|---|
| Single turn | 3.52 |
| Multi turn | 3.10 |
| Overall | 3.31 |


### Applications
This fine-tuned model is particularly suited for [mention applications, e.g., chatbots, question-answering systems, etc.]. Its enhanced capabilities ensure more accurate and contextually appropriate responses in these domains.

### Limitations and Considerations
While our fine-tuning process has optimized the model for specific tasks, it's important to acknowledge potential limitations. The model's performance can still vary based on the complexity of the task and the specificities of the input data. Users are encouraged to evaluate the model thoroughly in their specific context to ensure it meets their requirements.

### Model Card
```
@article{Carrot-Ko-2.1B-Instruct,
  title={CarrotAI/Carrot-Ko-2.1B-Instruct Card},
  author={CarrotAI (L, GEUN)},
  year={2024},
  url = {https://huggingface.co/CarrotAI/Carrot-2.1B-Instruct}
}