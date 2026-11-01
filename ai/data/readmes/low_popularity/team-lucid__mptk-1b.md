---
license: apache-2.0
language:
- ko
---
# MPTK-1B

MPTK-1B는 한국어/영어코드 데이터셋에서 학습된 1.3B 파라미터의 decoder-only transformer 언어모델입니다.

이 모델은 구글의 [TPU Research Cloud(TRC)](https://sites.research.google/trc/about/)를 통해 지원받은 Cloud TPU로 학습되었습니다.

## Model Details

### Model Description

다른 decoder-only transformer에서 일부 수정된 아키텍처인 MPT를 기반으로 합니다.

- [ALiBi (Attention with Linear Biases)](https://arxiv.org/abs/2108.12409)를 사용합니다
- bias를 사용하지 않습니다.

| Hyperparameter  | Value |
|-----------------|-------|
| n_parameters    | 1.3B  |
| n_layers        | 24    |
| n_heads         | 16    |
| d_model         | 2048  |
| vocab size      | 50432 |
| sequence length | 2048  |

## Uses

## How to Get Started with the Model

fp16으로 실행 시 NaN이 발생할 수 있습니다. 따라서 fp32 혹은 bf16로 실행하기를 권장합니다.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("team-lucid/mptk-1b")
model = AutoModelForCausalLM.from_pretrained("team-lucid/mptk-1b")

pipe = pipeline('text-generation', model=model, tokenizer=tokenizer, device='cuda:0')

with torch.autocast('cuda', dtype=torch.bfloat16):
    print(
        pipe(
            '대한민국의 수도는',
            max_new_tokens=100,
            do_sample=True,
        )
    )

```

## Training Details

### Training Data

[OSCAR](https://oscar-project.org/), mC4, wikipedia, namuwiki 등 한국어
데이터에 [RefinedWeb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb), [The Stack](https://huggingface.co/datasets/bigcode/the-stack)
에서 일부를 추가해 학습하였습니다.

#### Training Hyperparameters

| **Hyperparameter** | **Value**  |
|--------------------|------------|
| Precision          | bfloat16 |
| Optimizer          | Lion       |
| Learning rate      | 2e-4       |
| Batch size         | 1024       |
