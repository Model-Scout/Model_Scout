---

library_name: transformers
license: cc-by-nc-4.0
license_link: https://ai.google.dev/gemma/terms
base_model:
  - google/gemma-3-12b-it
pipeline_tag: text-generation
language:
  - ko
tags:
  - gemma
  - evaluator
  - rubric
  - rag
  - finance
  - law
---

# datumo/E-Star-12B-v2-Base

- 소유자: Selectstar Eval Team
- 작성일: 2026-05-22
- 상태: Active
- 문서상 버전: v0.1
- Hugging Face ID: `datumo/E-Star-12B-v2-Base`

> **비상업적 사용 전용(Non-Commercial Use Only)**  
> 본 모델은 Gemma 3의 파생 모델이므로 [Gemma Terms of Use](https://ai.google.dev/gemma/terms)가 적용됩니다. Selectstar가 보유한 수정분에는 CC BY-NC 4.0 기반의 추가 비상업 조건이 적용됩니다. 두 조건을 모두 준수해야 하며, 상업적 이용은 Selectstar와 별도 계약이 필요합니다.

---

## 1. 모델 설명

### 1.1 모델 아키텍처 / 파라미터 크기

| 항목 | 내용 |
|---|---|
| 베이스 모델 | `google/gemma-3-12b-it` |
| 모델 계열 | Gemma 3 |
| 아키텍처 | Transformer 기반 Decoder 계열 |
| 파라미터 크기 | 약 12B |
| 학습 방식 | Full Fine-Tuning 기반 SFT |
| 모델 유형 | 한국어 루브릭 기반 Evaluation Model |
| 주요 출력 | `feedback → highlight → decision` |
| 주요 언어 | 한국어 |

본 모델은 주어진 문제, 모델 응답, 평가 기준과 점수별 루브릭을 해석한 뒤 평가 설명, 핵심 근거 구간 및 최종 점수를 구조화된 형식으로 생성한다.

Gemma 3 12B는 멀티모달 입력을 지원하는 모델 계열이지만, 본 모델의 학습 및 평가 범위는 현재 문서 기준 텍스트 입력으로 제한된다. 이미지 입력 성능은 검증되지 않았다.

### 1.2 모델 제작에 사용한 GitHub 저장소

| 항목 | 내용 |
|---|---|
| 학습 저장소 | 확인 필요 |
| 평가 저장소 | 확인 필요 |
| 추론·서빙 저장소 | 확인 필요 |
| 학습 commit 또는 tag | 확인 필요 |
| Config 경로 | 확인 필요 |

실제 모델 제작에 사용한 저장소 URL과 재현 가능한 commit hash 또는 release tag를 추가해야 한다. 내부 저장소라면 접근 권한과 담당 조직을 함께 기재한다.

### 1.3 모델 버전 정보

| 항목 | 내용 |
|---|---|
| Hugging Face 저장소명 | `E-Star-12B-v2-Base` |
| 문서상 버전 | v0.1 |
| 버전 설명 | K2-Feedback 기반 3단계 필터링 데이터 6,311개로 학습한 초기 Base 버전 |
| 학습 체크포인트 | 확인 필요 |

저장소명의 `v2`와 문서 버전 `v0.1`의 의미가 혼재되어 있다. `v2`가 제품 세대이고 `v0.1`이 체크포인트 버전이라면 이를 명시하고, 그렇지 않다면 모델명과 버전을 통일해야 한다.

### 1.4 목적 / 사용 사례

E-Star-12B-v2-Base는 한국어 환경에서 evaluator가 주어진 루브릭을 얼마나 정확하고 일관되게 적용하는지 평가하고 자동화하기 위한 모델이다.

| 평가 축 | 설명 |
|---|---|
| Faithfulness | 모델 응답이 제공된 문서에 근거하는지 판단 |
| Context Relevancy | 검색된 문서가 사용자 질의와 관련되는지 판단 |
| Response Relevancy | 모델 응답이 사용자 질의에 적절히 대응하는지 판단 |
| Rubric Following | 임의의 평가 기준과 점수별 설명을 일관되게 적용하는지 판단 |

주요 사용 사례는 다음과 같다.

- 금융·법률 RAG 파이프라인 품질 평가
- 모델 응답에 대한 1~5점 루브릭 평가
- 평가 근거 및 핵심 텍스트 구간 추출
- LLM 응답 품질 모니터링과 회귀 테스트
- 사람 평가 이전의 1차 자동 평가
- Frontier judge 모델 대비 비용 효율적인 내부 evaluator

### 1.5 모델 응용 가능성

- 도메인별 루브릭을 추가하여 금융·법률 외 분야로 확장
- 일반 instruction following 및 reasoning 응답 평가
- RAG 검색기·생성기·프롬프트 간 비교 평가
- 데이터 품질 검수와 학습 샘플 우선순위 선별
- 점수와 자연어 피드백이 함께 필요한 평가 파이프라인

새로운 도메인에 적용할 때는 전문가 검수 데이터로 별도 성능 검증이 필요하다.

---

## 2. 모델 실행 방법

### 2.1 실행 환경

| 항목 | 내용 |
|---|---|
| Python | 확인 필요 |
| PyTorch | 확인 필요 |
| Transformers | 확인 필요 |
| TRL | 확인 필요 |
| 정밀도 | BF16 |
| 실행 장치 | CUDA GPU 권장 |

### 2.2 학습 코드 스니펫

아래 코드는 제공된 설정을 요약한 예시다. 실제 재현에는 학습 저장소, 전처리 코드와 정확한 패키지 버전이 필요하다.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import SFTConfig, SFTTrainer

BASE_MODEL = "google/gemma-3-12b-it"

tokenizer = AutoTokenizer.from_pretrained(
    BASE_MODEL,
    trust_remote_code=True,
)
model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
)

sft_config = SFTConfig(
    output_dir="./outputs/e-star-12b-v2-base",
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    learning_rate=1e-5,
    num_train_epochs=5,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
    bf16=True,
    logging_steps=10,
)

trainer = SFTTrainer(
    model=model,
    args=sft_config,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    processing_class=tokenizer,
)
trainer.train()
```

`num_train_epochs=5`와 “2 epoch에서 early stopping”은 서로 다른 정보다. Early stopping을 사용했다면 callback, patience와 실제 종료 epoch를 학습 로그 기준으로 명시해야 한다.

### 2.3 추론 코드 스니펫

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "datumo/E-Star-12B-v2-Base"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID,
    trust_remote_code=True,
)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)
model.eval()

system_prompt = """You are a rubric evaluator.
Evaluate the response strictly according to the provided rubric.
Return exactly <feedback>, <highlight>, and <decision>."""

user_prompt = """You MUST write all output in the same language as the input.

# Data to Evaluate
### Problem
한 공장에서 하루에 120개의 제품을 생산한다. 불량률이 5%일 때,
일주일 동안 생산되는 정상 제품의 수는?

### Model Response
하루 정상 제품은 120 - (120 × 0.05) = 114개이며,
일주일 정상 제품은 114 × 7 = 798개이다.

### Optional Ground Truth
798개

# Rubric
정답의 정확성과 풀이 과정의 논리적 일관성을 1점에서 5점으로 평가한다.
"""

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
]
inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
).to(model.device)

with torch.inference_mode():
    outputs = model.generate(
        **inputs,
        max_new_tokens=2048,
        do_sample=False,
    )

new_tokens = outputs[0, inputs["input_ids"].shape[1]:]
print(tokenizer.decode(new_tokens, skip_special_tokens=True))
```

실제 학습에 사용한 전체 prompt, 출력 파서와 generation config를 함께 제공해야 평가 결과를 재현할 수 있다.

---

## 3. 학습 데이터셋 설명

### 3.1 데이터 출처 및 특성

- 학습 데이터셋: [datumo/E-Star-Train-6K](https://huggingface.co/datasets/datumo/E-Star-Train-6K)
- Dataset Card: `EVAL-EStar-SFT-v0.1`

| 항목 | 내용 |
|---|---|
| 시드 데이터 | K2-Feedback (HAERAEHUB, 2024) |
| 시드 데이터 규모 | 약 99,700개 |
| 최종 학습 데이터 | 6,311개 |
| 언어 | 한국어 |
| 필드 | `system`, `user`, `assistant` |
| 출력 구조 | `feedback → highlight → decision` |
| 생성 유형 | Human+AI |
| 레이블 검증 | 복수 모델 합의 및 frontier 모델 교차 검증 |

### 3.2 필터링 파이프라인

| 단계 | 규모 변화 | 처리 방법 |
|---|---:|---|
| Stage 1 | 99.7K → 26K | Qwen3-30B-A3B-Instruct-2507과 Qwen3-Next-80B-A3B-Instruct의 초기 합의 |
| Stage 2 | 26K → 8K | Gemma 판단과 Qwen 합의 간 일치·불일치 샘플 균형화 |
| Stage 3 | 8K → 6,311 | GPT-5.2 단일 평가, 소형 frontier debate와 Qwen 합의 교차 검증 |

최종 데이터는 세 판단 경로 중 최소 두 경로 이상이 동일 레이블을 지지한 샘플로 구성된다.

### 3.3 평가 벤치마크

- [datumo/Feedback-Bench](https://huggingface.co/datasets/datumo/Feedback-Bench)
  - 영어·한국어 rubric following 평가
  - 5점 척도, reference-free, debate 기반 재레이블링
- [datumo/Rag-Quality-Bench](https://huggingface.co/datasets/datumo/Rag-Quality-Bench)
  - 금융·법률 domain adaptation 평가
  - Context Relevancy, Faithfulness, Response Relevancy

### 3.4 데이터 누수 확인

학습 데이터와 평가 벤치마크가 유사한 debate 절차를 사용하므로 instruction, response, rubric, 원천 문서와 생성 모델 조합의 중복 여부를 확인해야 한다.

---

## 4. 학습 설정

### 4.1 주요 학습 파라미터

| 항목 | 설정 |
|---|---|
| 학습 방식 | Full Fine-Tuning |
| 프레임워크 | TRL SFTTrainer |
| Learning rate | `1e-5` |
| 최대 epoch | 5 |
| 실제 종료 epoch | 2로 기재되어 있으나 로그 확인 필요 |
| Per-device batch size | 1 |
| Gradient accumulation | 8 |
| Precision | BF16 |
| Evaluation strategy | Epoch |
| Save strategy | Epoch |
| Best-model metric | Validation loss |
| LoRA | 사용하지 않음 |
| Optimizer / Scheduler | 확인 필요 |
| Max sequence length | 확인 필요 |
| Random seed | 확인 필요 |

### 4.2 GPU 및 학습 시간

| 항목 | 내용 |
|---|---|
| GPU 개수 | 4개 |
| GPU 모델 | 확인 필요 |
| GPU당 메모리 | 확인 필요 |
| 분산 학습 방식 | 확인 필요 |
| 총 학습 시간 | 약 1.2시간 |

`GPU: 4`만으로는 재현할 수 없으므로 A100, H100, H200 등 정확한 GPU 모델과 메모리 용량을 추가해야 한다.

---

## 5. 평가 결과

### 5.1 Feedback Bench — 영어 Rubric Following

| Type | Model | Pearson | Kendall τ | Spearman |
|---|---|---:|---:|---:|
| Frontier | GPT-5.2 | 0.916 | 0.865 | 0.911 |
| Frontier | Sonnet-4.6 | 0.840 | 0.776 | 0.847 |
| Instruct SLM | Gemma-3-12B-IT | 0.810 | 0.725 | 0.794 |
| Instruct SLM | oss-20b | 0.844 | 0.762 | 0.839 |
| Evaluator LM | Prometheus-8x7B-v2.0 | 0.823 | 0.736 | 0.806 |
| Evaluator LM | GLIDER 3.8B | 0.678 | 0.595 | 0.688 |
| **Ours** | **E-Star-12B-Base** | **0.856** | **0.778** | **0.847** |

### 5.2 Ko Feedback Bench — 한국어 Rubric Following

| Type | Model | Pearson | Kendall τ | Spearman |
|---|---|---:|---:|---:|
| Frontier | GPT-5.2 | 0.929 | 0.886 | 0.925 |
| Frontier | Sonnet-4.6 | 0.820 | 0.758 | 0.833 |
| Instruct SLM | Gemma-3-12B-IT | 0.653 | 0.593 | 0.661 |
| Instruct SLM | oss-20b | 0.778 | 0.704 | 0.779 |
| Evaluator LM | Prometheus-8x7B-v2.0 | 0.377 | 0.441 | 0.501 |
| Evaluator LM | GLIDER 3.8B | 0.523 | 0.487 | 0.563 |
| **Ours** | **E-Star-12B-Base** | **0.826** | **0.754** | **0.819** |

### 5.3 RAG Quality Bench — 금융·법률 Domain Adaptation

| Model | LAW CR | LAW F | LAW RR | FIN CR | FIN F | FIN RR | Average |
|---|---:|---:|---:|---:|---:|---:|---:|
| GPT-5.2 | 0.846 | 0.785 | 0.941 | 0.882 | 0.740 | 0.970 | 0.861 |
| Sonnet-4.6 | 0.910 | 0.786 | 0.872 | 0.932 | 0.845 | 0.925 | 0.878 |
| Gemma-3-12B-IT | 0.620 | 0.742 | 0.742 | 0.830 | 0.713 | 0.821 | 0.745 |
| oss-20b | 0.846 | 0.722 | 0.870 | 0.793 | 0.752 | 0.900 | 0.813 |
| Prometheus-8x7B-v2.0 | 0.392 | 0.477 | 0.772 | 0.386 | 0.240 | 0.806 | 0.512 |
| GLIDER 3.8B | 0.657 | 0.670 | 0.680 | 0.432 | 0.415 | 0.548 | 0.567 |
| **E-Star-12B-Base** | **0.853** | **0.730** | **0.816** | **0.835** | **0.720** | **0.880** | **0.806** |

CR은 Context Relevancy, F는 Faithfulness, RR은 Response Relevancy를 의미한다.

### 5.4 결과 해석

- E-Star는 Feedback Bench와 Ko Feedback Bench에서 베이스 모델보다 높은 상관도를 기록했다.
- RAG Quality 평균은 0.806으로 Gemma-3-12B-IT의 0.745보다 높지만 GPT-5.2, Sonnet-4.6과 oss-20b보다는 낮다.
- Faithfulness는 법률 0.730, 금융 0.720으로 베이스 모델보다 낮거나 유사해 지표별 취약점 분석이 필요하다.

### 5.5 평가 재현 정보

평가 코드와 commit, 벤치마크 revision, 모델 버전, prompt, generation config, 출력 파싱 규칙, 평가일과 신뢰구간을 추가해야 한다.

```text
Evaluation report: 확인 필요
Evaluation repository: 확인 필요
Raw result artifact: 확인 필요
```

---

## 6. 한계

1. Ko Feedback Bench의 기계번역 노이즈가 성능 측정에 영향을 줄 수 있다.
2. 학습 데이터와 벤치마크가 유사한 debate 절차로 구축되어 특정 judge 합의 기준과의 정렬을 측정할 수 있다.
3. 도메인 전문가의 독립적인 human evaluation이 수행되지 않았다.
4. Reference-free 설정으로 학습·평가되어 reference 포함 환경은 별도 검증이 필요하다.
5. 복잡하거나 상충하는 루브릭에서는 frontier 모델보다 판단 성능이 낮을 수 있다.
6. 입력 문서 수와 context 길이 증가에 따른 성능 변화가 검증되지 않았다.
7. 금융·법률 외 도메인의 일반화 성능이 확인되지 않았다.
8. 구조화 출력 태그의 누락·중복·순서 오류에 대한 파싱 실패율이 측정되지 않았다.
9. 베이스 모델은 멀티모달이지만 본 evaluator의 이미지 입력 성능은 검증되지 않았다.

---

## 7. 라이선스

### 7.1 적용 라이선스 구조

본 모델에는 다음 조건이 함께 적용된다.

1. Google의 Gemma Terms of Use
2. Selectstar가 자체 수정분에 부여한 CC BY-NC 4.0 기반 추가 비상업 조건

| 구성 요소 | 적용 조건 |
|---|---|
| 베이스 모델 `google/gemma-3-12b-it` | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) |
| Gemma 기반 파생 가중치 | Gemma Terms of Use |
| Selectstar가 보유한 수정분 | CC BY-NC 4.0 기반 추가 비상업 조건 |
| 학습 데이터 K2-Feedback | 원본 데이터셋 라이선스 확인 필요 |
| 학습·평가 코드 | 저장소별 라이선스 확인 필요 |

Hugging Face YAML에서는 단일 라이선스로 오해되지 않도록 `license: other`로 표기하였다.

### 7.2 허용되는 이용

- 비상업적 학술 연구
- 비영리 교육
- 개인 학습 및 실험
- 출처와 변경사항을 명시한 비상업적 수정·연구

재배포는 Gemma Terms와 Selectstar의 추가 조건을 모두 충족해야 하므로 별도 검토가 필요하다.

### 7.3 별도 계약 없이 허용되지 않는 이용

- 유료 제품·서비스에 모델 통합
- 유료 API 또는 hosted service 제공
- 사내 상업 운영 시스템이나 고객 대면 서비스 적용
- 모델 가중치의 판매 또는 상업적 재배포
- 상업적 모델 학습을 위한 데이터 생성
- 기타 직접적·간접적 수익 창출 목적의 이용

상업적 이용에는 Selectstar와 별도 계약이 필요하며, 별도 계약 후에도 Gemma Terms는 계속 적용된다.

### 7.4 Gemma 파생 모델 배포 조건

Gemma 파생 모델의 제3자 제공과 hosted service는 Gemma Terms상 Distribution에 포함될 수 있다. 배포 시에는 다음 조건을 확인해야 한다.

- Gemma 사용 제한을 집행 가능한 조건으로 포함
- 수령인에게 Gemma Terms 적용 사실 고지 및 약관 사본 제공
- 수정된 파일에 변경 사실 표시
- 요구되는 `NOTICE` 파일 제공
- Gemma Prohibited Use Policy 준수
- 추가 조건이 Gemma Terms와 충돌하지 않는지 확인

### 7.5 학습 데이터 라이선스

K2-Feedback의 정확한 라이선스명과 파생 데이터 및 모델 학습 허용 범위가 현재 문서에 기재되어 있지 않다. 확인 전까지 학습 데이터 원문을 모델 저장소에 포함하거나 외부에 재배포하지 않는다.

### 7.6 권장 라이선스 고지

```text
E-Star-12B-v2-Base is a model derivative of google/gemma-3-12b-it.

Use and distribution of the model weights are subject to the Gemma
Terms of Use. Additional non-commercial terms based on CC BY-NC 4.0
apply to modifications owned by Selectstar.

Users must comply with both sets of terms. Commercial use requires
a separate agreement with Selectstar and remains subject to the
Gemma Terms of Use and the Gemma Prohibited Use Policy.
```

### 7.7 상업적 이용 문의

상업적 라이선스가 필요한 경우 Selectstar 공식 채널을 통해 문의한다.
