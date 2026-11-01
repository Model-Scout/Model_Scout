---
license: cc-by-nc-sa-4.0
language:
- ko
task_categories:
- text-generation
- question-answering
tags:
- K-IFRS
- IFRS
- accounting
- finance
- korean
- fine-tuning
- instruction-tuning
- LoRA
- QLoRA
- RAG
pretty_name: K-IFRS QA Dataset
size_categories:
- 10K<n<100K
---

# K-IFRS QA Dataset

한국채택국제회계기준(K-IFRS) 기반의 오픈소스 QA 데이터셋입니다.  
LLM 파인튜닝(SFT), RAG 시스템 구축, 회계 도메인 벤치마크 평가 등 다양한 목적에 활용할 수 있도록 설계되었습니다.

> **기준 연도:** 본 데이터셋은 **2026년 5월 24일자 K-IFRS** 기준으로 작성되었습니다.  
> 회계기준은 지속적으로 개정되므로, 사용 시 기준 연도를 반드시 확인하시기 바랍니다.

---

## 데이터셋 개요

| 항목 | 내용 |
|------|------|
| 총 데이터 수 | 34,418개 |
| Train 분할 | 약 30,976개 (90%) |
| Validation 분할 | 약 3,442개 (10%) |
| 언어 | 한국어 |
| 형식 | Instruction-Input-Output (Alpaca 형식) |
| 기준 | K-IFRS (2026년 5월 24일자) |
| 라이선스 | CC BY-NC-SA 4.0 |

---

## 데이터 구조 (Data Fields)

각 데이터는 아래 세 가지 필드로 구성된 JSON Lines 형식입니다.

```json
{
  "instruction": "재고자산을 순실현 가능 가치로 감액하는 저가법은 어떻게 적용해야 합니까?",
  "input": "",
  "output": "재고자산을 순실현 가능 가치로 감액하는 저가법은 항목별로 적용해야 하지만, 유사하거나 관련된 항목들을 통합하여 적용할 수 있는 경우도 있습니다."
}
```

| 필드 | 타입 | 설명 |
|------|------|------|
| `instruction` | string | K-IFRS 관련 질문 (평균 43.7자) |
| `input` | string | 추가 맥락 정보 (현재 전부 빈 값, 향후 확장 예정) |
| `output` | string | 질문에 대한 답변 (평균 66.0자) |

---

## 구축 방법론 (Data Collection)

- **원천 데이터:** 금융위원회 · 한국회계기준원이 공시한 K-IFRS 기준서 원문
- **생성 방식:** GPT 계열 LLM을 활용한 데이터 증강(Data Augmentation) 후, 중복 제거 및 품질 필터링 적용
- **커버리지:** 개념체계, 재무제표 표시, 금융상품, 리스, 수익 인식, 사업결합 등 K-IFRS 전 영역 포괄
- **품질 지표:**
  - 빈 값(instruction/output): 0건
  - 중복 항목: 95건 (전체의 0.3%, 실질적 영향 없음)
  - 응답 길이 분포: 98% 이상이 30~200자 구간

---

## 주요 토픽 커버리지

| 키워드 | 출현 건수 | 비율 |
|--------|-----------|------|
| 자산 | 7,006 | 20.4% |
| 부채 | 3,530 | 10.3% |
| IFRS | 4,003 | 11.6% |
| 회계기준 | 2,877 | 8.4% |
| 공시 | 2,536 | 7.4% |
| 재무제표 | 2,393 | 7.0% |
| 수익 | 1,607 | 4.7% |
| 금융상품 | 1,280 | 3.7% |
| 리스 | 1,236 | 3.6% |

---

## 사용 방법

### 기본 로드

```python
from datasets import load_dataset

dataset = load_dataset("sonsdf/k-ifrs-qa-dataset")
print(dataset)
# DatasetDict({
#     train: Dataset({
#         features: ['instruction', 'input', 'output'],
#         num_rows: 34418
#     })
# })
```

### 파인튜닝 예시 (Alpaca 포맷 변환)

```python
def format_prompt(example):
    if example["input"]:
        return (
            f"### Instruction:\n{example['instruction']}\n\n"
            f"### Input:\n{example['input']}\n\n"
            f"### Response:\n{example['output']}"
        )
    return (
        f"### Instruction:\n{example['instruction']}\n\n"
        f"### Response:\n{example['output']}"
    )

dataset = dataset.map(lambda x: {"text": format_prompt(x)})
```

### LoRA / QLoRA 파인튜닝 (Unsloth 예시)

```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Meta-Llama-3-8B-Instruct",
    max_seq_length=2048,
    load_in_4bit=True,
)

# 학습 데이터로 k-ifrs-qa-dataset 활용
dataset = load_dataset("sonsdf/k-ifrs-qa-dataset")
```

---

## 활용 시나리오

### 1. LLM 파인튜닝 (SFT)
`Llama-3-8B`, `Gemma-2-9B`, `EXAONE` 등 오픈소스 모델에 LoRA / QLoRA 방식으로 K-IFRS 도메인 특화 파인튜닝에 바로 활용 가능합니다.

### 2. RAG 시스템 구축
질문(`instruction`)과 답변(`output`) 쌍을 벡터 DB에 인덱싱하여 K-IFRS 전문 검색 증강 생성(RAG) 시스템의 지식베이스로 활용할 수 있습니다.

### 3. 벤치마크 평가
Validation 분할을 활용하여 K-IFRS 도메인에서 LLM의 정확도 · 유창성을 평가하는 벤치마크 데이터셋으로 사용 가능합니다.

---

## 주의사항 및 한계 (Limitations & Disclaimer)

- 본 데이터셋은 **2026년 5월 24일자 K-IFRS 기준서**를 기반으로 구축되었으며, 이후 개정된 기준은 반영되지 않습니다.
- LLM 데이터 증강 과정에서 생성된 답변이 포함되어 있으므로, **실무적인 세무·회계 판단이나 법적 책임의 근거로 사용할 수 없습니다.**
- 구체적인 회계 처리는 반드시 공인회계사 또는 관련 전문가에게 문의하시기 바랍니다.
- K-IFRS 원문 저작권은 한국회계기준원에 있으며, 본 데이터셋은 교육·연구 목적으로 구축되었습니다.

---

## 라이선스

본 데이터셋은 [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/) 라이선스를 따릅니다.

- **출처 표시 필수** (BY)
- **비상업적 이용만 허용** (NC)
- **동일 조건 변경 허락** (SA)
