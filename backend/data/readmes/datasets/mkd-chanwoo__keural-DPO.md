---
language:
- en
- ko
license:
- mit
- apache-2.0
- other
size_categories:
- 100K<n<1M
task_categories:
- text-generation
tags:
- dpo
- chatml
- preference
- alignment
- rlhf
- korean
- bilingual
pretty_name: keural-DPO
---

# keural-DPO

한국어/영어 DPO(Direct Preference Optimization) 학습용 통합 데이터셋.
6개 소스 데이터셋을 ChatML 형식으로 정규화하여 통합한 것으로, 총 **443,314 샘플**을 포함합니다.

---

## 데이터셋 통계

| Split | 소스 | 필터 제거 | 업로드 | 언어 | 라이선스 |
|---|---|---|---|---|---|
| `ultrafeedback_binarized` | 61,054 | 424 | **60,630** | EN | MIT |
| `multifaceted_collection_dpo` | 65,139 | 1,045 | **64,094** | EN/KO | Apache-2.0 |
| `hh_rlhf` | 160,608 | 739 | **159,869** | EN | MIT |
| `orca_dpo_pairs_ko` | 12,727 | 2 | **12,725** | KO | — |
| `aihub_71748` | 29,676 | 0 | **29,676** | KO | AI Hub |
| `aihub_71760` | 116,320 | 0 | **116,320** | KO | AI Hub |
| **합계** | **445,524** | **2,210** | **443,314** | | |

> 필터 제거: `chosen_chatml == rejected_chatml` 인 샘플 제외

---

## 언어 및 도메인 비율

### 언어 분포

| 언어 | 샘플 수 | 비율 | 해당 Split |
|---|---|---|---|
| English only | 220,499 | 49.7% | `ultrafeedback`, `hh_rlhf` |
| Korean only | 158,721 | 35.8% | `orca_dpo_ko`, `aihub_71748`, `aihub_71760` |
| EN/KO mixed | 64,094 | 14.5% | `multifaceted_dpo` |
| **합계** | **443,314** | **100%** | |

### 도메인 분포 (참고)

| 도메인 | 주요 소스 |
|---|---|
| General instruction-following | ultrafeedback, orca_dpo_ko, multifaceted_dpo |
| Helpful & Harmless dialogue | hh_rlhf |
| Korean general QA (사회·인문·과학·예체능) | aihub_71748 |
| Korean trustworthiness (Honesty / Harmlessness / Helpfulness) | aihub_71760 |

### Preference Signal 유형

단순 "정답 vs 오답" 형태가 아닌 다양한 preference signal이 혼합되어 있습니다.

| Signal 유형 | 설명 | 해당 Split |
|---|---|---|
| **Helpfulness** | 더 도움이 되는 응답 vs 덜 유용한 응답 | `ultrafeedback`, `multifaceted_dpo`, `orca_dpo_ko`, `aihub_71748` |
| **Harmlessness / Safety** | 안전한 응답 vs 유해하거나 부적절한 응답 | `hh_rlhf`, `aihub_71760` (무해성 subject) |
| **Honesty / Truthfulness** | 사실에 근거한 응답 vs 환각·오정보 포함 응답 | `ultrafeedback`, `aihub_71760` (정보정확성 subject) |
| **Style / Persona** | 지정된 페르소나·톤·스타일에 부합하는 응답 | `multifaceted_dpo` (system-level preference) |
| **Response quality ranking** | 동일 질문에 대한 5개 응답의 상대적 ranking | `aihub_71748` (rank 1 → chosen, rank 5 → rejected) |

> **특징**: "완전히 틀린 답 vs 정답" 구도보다 **"그럴듯하지만 덜 적절한 답 vs 더 나은 답"** 형태의 subtle preference pair 비중이 높아 DPO signal 품질이 양호한 편입니다.

---

## 소스 데이터셋

| Split | 원본 데이터셋 | 설명 |
|---|---|---|
| `ultrafeedback_binarized` | [HuggingFaceH4/ultrafeedback_binarized](https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized) | GPT-4 기반 preference 평가, Zephyr 계열 alignment에 사용된 검증 데이터셋 |
| `multifaceted_collection_dpo` | [kaist-ai/Multifaceted-Collection-DPO](https://huggingface.co/datasets/kaist-ai/Multifaceted-Collection-DPO) | GPT-4-Turbo가 system preference/persona를 추가 생성한 synthetic preference 데이터셋 |
| `hh_rlhf` | [Anthropic/hh-rlhf](https://huggingface.co/datasets/Anthropic/hh-rlhf) | Anthropic의 Helpful & Harmless RLHF 데이터셋, 멀티턴 대화 포함 |
| `orca_dpo_pairs_ko` | [Ja-ck/Orca-DPO-Pairs-KO](https://huggingface.co/datasets/Ja-ck/Orca-DPO-Pairs-KO) | Orca 계열 instruction 스타일 한국어 DPO 데이터셋 |
| `aihub_71748` | [AI Hub 71748](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71748) | 한국어 성능이 개선된 초거대 AI 언어모델 개발 및 데이터 구축 (RM 데이터, ranking 1→chosen / 5→rejected) |
| `aihub_71760` | [AI Hub 71760](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71760) | 초거대 언어모델 신뢰성 벤치마크 데이터 (Honesty/Harmlessness/Helpfulness 기반) |

---

## 데이터 형식

### 필드

| 필드 | 타입 | 설명 |
|---|---|---|
| `prompt` | `str` | 첫 번째 user 질문. 모든 split에서 항상 str |
| `chosen_chatml` | `str` | 선택된 응답의 ChatML 전체 시퀀스 |
| `rejected_chatml` | `str` | 거부된 응답의 ChatML 전체 시퀀스 |

### ChatML 형식

**단일턴** (ultrafeedback, multifaceted_dpo, orca_dpo_ko, aihub_71748, aihub_71760):
```
chosen_chatml:
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
{chosen_response}<|im_end|>

rejected_chatml:
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
{rejected_response}<|im_end|>
```

**멀티턴** (hh_rlhf): chosen/rejected가 각자 독립된 대화 경로. 컨텍스트 오염 없이 분리 저장.
```
chosen_chatml:                        rejected_chatml:
<|im_start|>user                      <|im_start|>user
{Q1}<|im_end|>                        {Q1}<|im_end|>
<|im_start|>assistant                 <|im_start|>assistant
{A1_chosen}<|im_end|>                 {A1_rejected}<|im_end|>
<|im_start|>user                      <|im_start|>user
{Q2}<|im_end|>                        {Q2}<|im_end|>
<|im_start|>assistant                 <|im_start|>assistant
{A2_chosen}<|im_end|>                 {A2_rejected}<|im_end|>
```
> `prompt` 필드는 두 경로의 공통 시작점인 첫 번째 user 질문(Q1)만 저장합니다.

---

## 학습 시 주의사항

### 필수 특수 토큰 추가

ChatML 형식 학습을 위해 토크나이저에 아래 특수 토큰이 반드시 추가되어야 합니다:

```python
tokenizer.add_special_tokens({
    "additional_special_tokens": ["<|im_start|>", "<|im_end|>"]
})
model.resize_token_embeddings(len(tokenizer))
```

### 데이터 로드 예시

```python
from datasets import load_dataset

# 특정 split 로드
ds = load_dataset("mkd-chanwoo/keural-DPO", split="ultrafeedback")

# 전체 로드 후 합치기
from datasets import concatenate_datasets

splits = ["ultrafeedback", "multifaceted_dpo", "hh_rlhf",
          "orca_dpo_ko", "aihub_71748", "aihub_71760"]
ds = concatenate_datasets([
    load_dataset("mkd-chanwoo/keural-DPO", split=s) for s in splits
])
```

### TRL DPO Trainer 사용 예시

```python
from trl import DPOTrainer, DPOConfig

training_args = DPOConfig(
    beta=0.1,
    ...
)

trainer = DPOTrainer(
    model=model,
    args=training_args,
    train_dataset=ds,
    tokenizer=tokenizer,
    # chosen_chatml / rejected_chatml 컬럼을 직접 사용하는 경우
    # precompute_ref_log_probs=True 옵션 고려
)
```

---

## 라이선스

각 split의 라이선스는 원본 데이터셋을 따릅니다:

| Split | 라이선스 |
|---|---|
| `ultrafeedback` | MIT |
| `multifaceted_dpo` | Apache-2.0 |
| `hh_rlhf` | MIT |
| `orca_dpo_ko` | 원본 데이터카드 확인 필요 |
| `aihub_71748` | [AI Hub 이용약관](https://www.aihub.or.kr/intro/policy.do) |
| `aihub_71760` | [AI Hub 이용약관](https://www.aihub.or.kr/intro/policy.do) |

> AI Hub 데이터(`aihub_71748`, `aihub_71760`)는 AI Hub 이용 승인 후 사용 가능합니다.
> 상업적 이용 전 각 원본 데이터셋의 라이선스를 반드시 확인하세요.