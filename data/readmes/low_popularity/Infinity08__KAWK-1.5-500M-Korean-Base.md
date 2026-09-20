---
language:
- ko
library_name: transformers
pipeline_tag: text-generation
datasets:
- Infinity08/KAWK500M-Korean-Pretraining-10B
tags:
- llama
- korean
- causal-lm
- base-model
- from-scratch
- kawk
---

# KAWK-1.5-500M Korean Base

한국어에 학습 예산을 집중한 소형 언어모델의 가능성을 검증하기 위해 **한국어 tokenizer와 505M 파라미터 Llama 계열 모델을 처음부터 학습한** 베이스 언어모델입니다.

KAWK-50M에서 tokenizer, 데이터 정제, causal objective, checkpoint 복구, long-context CPT와 공개 평가 pipeline을 먼저 검증한 뒤 규모를 500M으로 확장했습니다. 기존 다국어 모델을 한국어로 계속 학습한 모델이 아니며, 한국어 중심 약 10B tokens로 scratch pretraining했습니다.

> 이 모델은 지시 튜닝 전의 next-token predictor입니다. 질문·대화에는 KAWK 500M Instruct가 더 적합합니다.

## 왜 만들었나

- 한국어 전용 tokenizer와 데이터가 작은 parameter budget의 효율을 높일 수 있는지 확인
- 개인 프로젝트에서도 데이터 준비부터 pretraining, SFT, benchmark까지 재현 가능한지 검증
- 소비자 GPU에서 실행 가능한 한국어 foundation model 확보
- 최종 checkpoint뿐 아니라 dataset revision, 설정과 로그까지 공개

## 모델 구조

| 항목 | 값 |
|---|---:|
| 아키텍처 | LlamaForCausalLM, decoder-only |
| 파라미터 | 505,350,400 |
| 어휘 | 한국어 SentencePiece Unigram 32,000 |
| 레이어 | 26 |
| Hidden / MLP | 1,280 / 3,584 |
| Attention / KV heads | 20 / 5 (GQA) |
| Head dimension | 64 |
| 최대 문맥 | 2,048 tokens |
| 활성화 / 정규화 | SwiGLU(SiLU) / RMSNorm |
| 입력·출력 임베딩 | 공유 |

## 학습

- Dataset: [`Infinity08/KAWK500M-Korean-Pretraining-10B`](https://huggingface.co/datasets/Infinity08/KAWK500M-Korean-Pretraining-10B)
- Dataset revision: `a08539316e6dcf1d194c6d1684a43e3526e11a63`로 고정
- 유효 학습량: **10,000,097,280 tokens**
- Sequence length: 2,048
- Optimizer steps: 81,381
- Precision / GPU: BF16 / NVIDIA H100 SXM 80GB
- 평균 처리량: 약 60.35K tokens/s
- 최종 train loss: 2.5441
- 최종 validation loss / perplexity: **2.52412 / 12.48**

한국어 문서에 포함된 영문 이름, 숫자, 단위와 기호는 유지했지만 영어·코드·수학 전용 dataset은 별도 학습 source로 사용하지 않았습니다. 원천 revision과 학습 manifest는 dataset 및 training archive에 보존했습니다.

## 사용 예시

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

repo_id = "Infinity08/KAWK-1.5-500M-Korean-Base"
tokenizer = AutoTokenizer.from_pretrained(repo_id, use_fast=False)
model = AutoModelForCausalLM.from_pretrained(
    repo_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

inputs = tokenizer("대한민국의 수도는", return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    max_new_tokens=80,
    do_sample=True,
    temperature=0.8,
    top_p=0.9,
    repetition_penalty=1.1,
)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## 한계

- Base 모델이므로 대화형 지시 수행을 기대하면 안 됩니다.
- 500M급의 지식량과 추론 능력에는 뚜렷한 한계가 있습니다.
- 잘못된 사실, 반복, 웹 데이터의 편향을 생성할 수 있습니다.
- 다른 tokenizer를 쓰는 모델과 token-level perplexity를 직접 비교하면 안 됩니다.
- 포괄적인 안전성·개인정보 재현 평가가 완료되지 않았습니다.
- 고위험 의사결정에 사용하지 마십시오.

## 관련 자료

- [KAWK 500M Instruct v1](https://huggingface.co/Infinity08/KAWK-500M-Korean-Instruct-v1)
- [500M pretraining dataset](https://huggingface.co/datasets/Infinity08/KAWK500M-Korean-Pretraining-10B)
- [500M SFT dataset](https://huggingface.co/datasets/Infinity08/KAWK500M-Korean-SFT-v1)
- [50M Base](https://huggingface.co/Infinity08/KAWK-1.5-50M-Korean-Base)
