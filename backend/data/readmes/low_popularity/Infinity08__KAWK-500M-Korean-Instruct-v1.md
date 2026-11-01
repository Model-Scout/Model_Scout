---
language:
- ko
library_name: transformers
pipeline_tag: text-generation
datasets:
- Infinity08/KAWK500M-Korean-Pretraining-10B
- Infinity08/KAWK500M-Korean-SFT-v1
tags:
- llama
- korean
- causal-lm
- instruction-tuned
- from-scratch
- kawk
---

# KAWK 500M Korean Instruct v1

**한국어에 학습 예산을 집중한 소형 언어모델을 tokenizer부터 직접 만들면 어느 정도의 성능을 얻을 수 있는가**를 검증하기 위해 개발한 505M 파라미터 한국어 대화 모델입니다.

기존 다국어 모델을 한국어로 미세조정한 모델이 아닙니다. 한국어 중심 말뭉치로 32K SentencePiece tokenizer를 새로 만들고, Llama 계열 Base를 약 10B tokens 처음부터 사전학습한 뒤 한국어 지시 데이터로 SFT했습니다. KAWK-50M에서 데이터 정제, objective 검증, checkpoint 재개, 장문 CPT와 평가 pipeline을 먼저 검증한 뒤 규모를 500M으로 확장했습니다.

목표는 가장 큰 범용 모델을 만드는 것이 아니라 다음을 재현 가능한 한 흐름으로 구현하는 것이었습니다.

- 한국어에 맞춘 tokenizer와 parameter 배분
- 한국어 중심 pretraining dataset의 정제·중복 제거·streaming
- scratch pretraining과 assistant-only SFT
- 소비자 GPU에서의 공개 benchmark
- 성공 결과뿐 아니라 설정·로그·평가 조건까지 공개

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
| 위치 표현 | RoPE |
| 입력·출력 임베딩 | 공유 |

한국어 문장 안에 자연스럽게 포함된 영문 이름, 숫자, 단위와 기호는 유지했지만 영어·코드·수학 전용 pretraining source를 별도로 혼합하지 않았습니다.

## Base 사전학습

- Dataset: [`Infinity08/KAWK500M-Korean-Pretraining-10B`](https://huggingface.co/datasets/Infinity08/KAWK500M-Korean-Pretraining-10B)
- Dataset revision: `a08539316e6dcf1d194c6d1684a43e3526e11a63`로 고정
- 유효 학습량: **10,000,097,280 tokens**
- Sequence length: 2,048
- Optimizer steps: 81,381
- Precision / GPU: BF16 / NVIDIA H100 SXM 80GB
- 평균 처리량: 약 60.35K tokens/s
- 최종 validation loss / perplexity: **2.52412 / 12.48**

Base의 tokenizer, model config, 학습 설정과 checkpoint는 프로젝트 기록에 보존했습니다. 현재 이 Hugging Face 저장소는 해당 Base에 SFT를 적용한 최종 Instruct checkpoint입니다.

## SFT 데이터와 학습

SFT에는 이전 50M용 대화/RAG corpus를 그대로 재사용하지 않고, 500M 모델용으로 새로 정제한 [`Infinity08/KAWK500M-Korean-SFT-v1`](https://huggingface.co/datasets/Infinity08/KAWK500M-Korean-SFT-v1)을 사용했습니다.

| 원천 | 필터 통과 대화 |
|---|---:|
| `lcw99/DistilQwen_100k_korean` | 54,377 |
| `coastral/korean-writing-style-instruct` | 27,792 |
| `CarrotAI/ko-instruction-dataset` | 3,910 |
| `CohereLabs/aya_dataset` 한국어 subset | 331 |

처리 과정에서 NFC 정규화, 개인정보 형태 마스킹, 명시적 code/LaTeX/수식 중심 샘플 제거, 한국어 비율·반복·기호·목록 품질 필터, 원천 간 exact dedup을 적용했습니다. 사용자·system token은 `loss_mask=0`, assistant 답변과 EOS만 `loss_mask=1`입니다.

| 항목 | 값 |
|---|---:|
| Train / validation sequences | 22,155 / 300 |
| Sequence length | 2,048 |
| Non-padding tokens | 39,667,738 |
| Supervised assistant tokens | 34,174,461 |
| Epochs / optimizer steps | 2 / 739 |
| 총 packed-token exposure | 90,808,320 |
| Precision / GPU | BF16 / NVIDIA A100 80GB |
| Effective batch | 60 sequences |
| Learning rate | 2e-5 → 2e-6 cosine |
| Step 700 val loss / perplexity | 1.97862 / 7.2327 |

## 사용 예시

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

repo_id = "Infinity08/KAWK-500M-Korean-Instruct-v1"
tokenizer = AutoTokenizer.from_pretrained(repo_id, use_fast=False)
model = AutoModelForCausalLM.from_pretrained(
    repo_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "user", "content": "대한민국의 수도를 한 문장으로 설명해줘."}
]
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    max_new_tokens=128,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.05,
)
new_tokens = outputs[0, inputs["input_ids"].shape[1]:]
print(tokenizer.decode(new_tokens, skip_special_tokens=True))
```

토크나이저의 `chat_template.jinja`는 `### 지침:`, `### 사용자:`, `### 도우미:` 역할 헤더를 사용합니다.

## Benchmark

`lm-evaluation-harness 0.4.12`, 0-shot, BF16, 최대 문맥 1,024, **chat template 미적용** 조건입니다. RTX 4090에서 seed 1234와 bootstrap 1,000회로 평가했습니다.

| 모델 | Params | KoBEST acc | KoBEST acc_norm | KoBEST F1 | KMMLU acc |
|---|---:|---:|---:|---:|---:|
| **KAWK-500M-Instruct-v1** | **505M** | **0.52335** | **0.480** | **0.46772** | **0.14793** |
| Qwen2.5-0.5B-Instruct | 0.5B | 0.48345 | 0.460 | 0.39096 | 0.32289 |
| SmolLM2-360M-Instruct | 0.36B | 0.47643 | 0.418 | 0.37975 | 0.27091 |
| Qwen2.5-1.5B-Instruct | 1.5B | 0.52006 | 0.510 | 0.42607 | 0.37508 |
| EXAONE-4.0-1.2B | 1.2B | 0.47906 | 0.394 | 0.39059 | 0.15535 |
| Kanana-1.5-2.1B-Instruct | 2.1B | 0.64569 | 0.572 | 0.58957 | 0.39846 |

KAWK는 동급의 0.36B~0.5B 비교 모델보다 이 실행의 KoBEST aggregate가 높았고, 1.2B~1.5B 일부 모델과도 KoBEST에서 비슷하거나 높은 항목이 있었습니다. 반면 KMMLU는 모든 비교 모델보다 낮아 지식 습득량과 전문 지식에서 큰 한계가 드러났습니다. 서로 다른 tokenizer, 학습 데이터, instruct format을 사용하는 모델의 결과이므로 이 표는 동일 실행 조건에서의 참고치이지 모든 한국어 능력을 대표하는 순위가 아닙니다.

원시 JSON, 세부 task별 CSV와 manifest는 이 저장소의 `evaluation/`에 있습니다.

## 적합한 용도

- 소형 한국어 LM 및 parameter-efficiency 연구
- 한국어 generation·instruction-tuning 실험
- 제한된 VRAM 환경의 로컬 추론
- 한국어 tokenizer와 데이터 pipeline 교육

## 한계와 주의사항

- 500M급이므로 복잡한 추론, 전문 지식, 사실 회상이 제한적입니다.
- 답을 모를 때도 그럴듯한 오답을 생성할 수 있습니다.
- 반복, 지시 누락, 긴 대화의 정보 손실이 발생할 수 있습니다.
- 포괄적인 안전 정렬·red teaming·개인정보 재현 평가가 완료되지 않았습니다.
- 의료·법률·금융·보안 등 고위험 의사결정에 사용하지 마십시오.
- SFT 원천의 편향과 오류를 재현할 수 있으므로 각 upstream dataset의 조건도 확인해야 합니다.

## 관련 자료

- [500M pretraining dataset](https://huggingface.co/datasets/Infinity08/KAWK500M-Korean-Pretraining-10B)
- [500M SFT dataset](https://huggingface.co/datasets/Infinity08/KAWK500M-Korean-SFT-v1)
- [50M Base](https://huggingface.co/Infinity08/KAWK-1.5-50M-Korean-Base)
- [50M long-context Base](https://huggingface.co/Infinity08/KAWK-1.5-50M-Korean-Base-5K)
- [50M Instruct](https://huggingface.co/Infinity08/KAWK-1.5-50M-Korean-Instruct)
