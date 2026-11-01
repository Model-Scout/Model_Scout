---
license: cc-by-nc-4.0
language:
- ko
tags:
- korean
- trustworthiness
- dpo
- sft
- instruction-tuning
- helpfulness
- harmlessness
- honesty
- ai-safety
size_categories:
- 1K<n<10K
task_categories:
- text-generation
- text-classification
pretty_name: Korean LLM Trustworthiness Benchmark (Sample)
---

<!-- aegis-dataset-card -->

# korean-llm-trustworthiness-benchmark

> **평가 전용(학습 금지)** · KTB 한국어 LLM 신뢰성 벤치마크(표본)  
> 파일 12개 · 4.6 MB · 행 3,000 · revision `0677e491a6` · 카드 갱신 2026-10-20  
> 전체 모델 ↔ 데이터 매핑 · 서버 복원 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020)

> **평가 전용이다.** 학습 · 합성 시드 · few-shot · 하이퍼파라미터 · 임계값 선택(test 분할)에 쓰지 않는다.

## 개요
이 데이터셋은 AIHub의 "초거대 언어모델 신뢰성 벤치마크 데이터"를 기반으로 구축된 한국어 LLM 지시학습 데이터셋입니다. 
AI 모델의 세 가지 핵심 신뢰성 요소(도움적정성, 무해성, 정보정확성)를 평가하고 학습하기 위해 설계되었습니다.

## 이 데이터로 학습한 모델
평가 전용 — 학습에 쓰지 않는다. aegis-guard-train 의 인코더 · Gen · L2 와 AEGIS 판정 API 평가에 쓴다.

## 파일 구성
| 파일 | 크기 | 행 | 내용 |
|---|---|---|---|
| `README.md` | 5.0 KB | - |  |
| `data/train-00000-of-00001.parquet` | 629.6 KB | 3,000 |  |
| `dataset_dict.json` | 66 B | - |  |
| `dpo_preference/data-00000-of-00001.arrow` | 1.8 MB | - |  |
| `dpo_preference/dataset_info.json` | 531 B | - |  |
| `dpo_preference/state.json` | 247 B | - |  |
| `fact_checking/data-00000-of-00001.arrow` | 600.6 KB | - |  |
| `fact_checking/dataset_info.json` | 627 B | - |  |
| `fact_checking/state.json` | 247 B | - |  |
| `sft_instruction/data-00000-of-00001.arrow` | 1.5 MB | - |  |
| `sft_instruction/dataset_info.json` | 533 B | - |  |
| `sft_instruction/state.json` | 247 B | - |  |

## 필드 · 범주 분포
**`data/train-00000-of-00001.parquet`** (기준 `data/train-00000-of-00001.parquet`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `type` | string | 100% |
| `prompt` | string | 100% |
| `chosen` | string | 100% |
| `rejected` | string | 100% |
| `instruction` | string | 100% |
| `input` | string | 100% |
| `output` | string | 100% |
| `is_correct` | bool | 100% |
| `original_question` | string | 100% |
| `original_answer` | string | 100% |
| `category` | string | 100% |
| `subcategory` | string | 100% |
| `system` | string | 100% |

범주 분포(기준 파일):
- `type`: sft_instruction 1,000(33%) · dpo_preference 1,000(33%) · fact_checking 1,000(33%)
- `is_correct`: None 2,000(67%) · True 500(17%) · False 500(17%)
- `category`: honesty 1,668(56%) · helpfulness 666(22%) · harmlessness 666(22%)
- `subcategory`: fact_checking 1,000(33%) · Clarification 336(11%) · Nonsense 330(11%) · Hate 256(9%) · qa_generation 233(8%) · Bias 187(6%) · Sensitiveness 162(5%) · 일반 상식 78(3%) · 사회 77(3%) · 국어 63(2%) · 한국사 61(2%) · Illegal 61(2%) …

필드는 행 최상위 키, 채움은 그 키가 있는 행 비율이다. 범주 분포는 글 필드가 아니고 값이 짧고(≤48자) 종류가 적은(≤40) 필드만 셌다.

## 내려받기 · 복원
```bash
hf download neuralfoundry-coder/korean-llm-trustworthiness-benchmark --repo-type dataset --local-dir <폴더>
```
- 서버 파일 전체의 위치 · 재생성 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020) 의 `restore_map.json`

## 기존 설명 (2026-10-20 이전 카드)

### Korean LLM Trustworthiness Benchmark (Sample)

#### 개요

이 데이터셋은 AIHub의 "초거대 언어모델 신뢰성 벤치마크 데이터"를 기반으로 구축된 한국어 LLM 지시학습 데이터셋입니다. 
AI 모델의 세 가지 핵심 신뢰성 요소(도움적정성, 무해성, 정보정확성)를 평가하고 학습하기 위해 설계되었습니다.

#### 데이터셋 구조

모든 데이터는 `train` split에 통합되어 있으며, `type` 필드로 데이터 유형을 구분합니다:

| 필드명 | 설명 |
|--------|------|
| `type` | 데이터 유형 (dpo_preference, sft_instruction, fact_checking) |
| `prompt` | 프롬프트/질문 (DPO용) |
| `chosen` | 선호 응답 (DPO용) |
| `rejected` | 비선호 응답 (DPO용) |
| `instruction` | 지시문 (SFT/Fact Checking용) |
| `input` | 추가 입력 (SFT용) |
| `output` | 출력/응답 (SFT/Fact Checking용) |
| `is_correct` | 정답 여부 (Fact Checking용) |
| `original_question` | 원본 질문 (Fact Checking용) |
| `original_answer` | 원본 답변 (Fact Checking용) |
| `category` | 카테고리 (helpfulness, harmlessness, honesty) |
| `subcategory` | 세부 카테고리 |
| `system` | 시스템 프롬프트 |

#### 데이터셋 구성

##### 1. DPO Preference (선호도 학습)
- **용도**: Direct Preference Optimization, RLHF 학습
- **형식**: prompt, chosen, rejected
- **총 레코드**: 1,000건

##### 2. SFT Instruction (지시학습)
- **용도**: Supervised Fine-Tuning
- **형식**: instruction, input, output (Alpaca 스타일)
- **총 레코드**: 1,000건

##### 3. Fact Checking (팩트체킹)
- **용도**: 정보 정확성 판별 학습
- **형식**: instruction, output, is_correct
- **총 레코드**: 1,000건

#### 카테고리 설명

##### 도움적정성 (Helpfulness)
사용자 질문에 대해 얼마나 도움이 되는 답변을 제공하는지 평가
- **Clarification**: 불명확한 질문에 대한 명확화 요청
- **Nonsense**: 논리적으로 불일치하거나 불가능한 질문 처리

##### 무해성 (Harmlessness)
편견, 혐오, 불법 콘텐츠 등 유해한 응답을 방지하는 능력 평가
- **Hate**: 혐오 표현 방지
- **Bias**: 성별, 지역, 직업 등에 대한 편향 방지
- **Sensitiveness**: 민감한 주제의 적절한 처리
- **Illegal**: 불법 활동 조장 방지

##### 정보정확성 (Honesty)
정확하고 신뢰할 수 있는 정보를 제공하는 능력 평가
- 한국사, 과학, 사회, 국어, 수학, 영어, 일반 상식

#### 사용 방법

```python
from datasets import load_dataset

### 데이터셋 로드
dataset = load_dataset("neuralfoundry-coder/korean-llm-trustworthiness-benchmark")

### 전체 데이터
all_data = dataset["train"]

### 유형별 필터링
dpo_data = all_data.filter(lambda x: x["type"] == "dpo_preference")
sft_data = all_data.filter(lambda x: x["type"] == "sft_instruction")
fact_data = all_data.filter(lambda x: x["type"] == "fact_checking")
```

##### DPO 학습 예시
```python
### DPO 형식 데이터
dpo_data = dataset["train"].filter(lambda x: x["type"] == "dpo_preference")
for example in dpo_data:
    prompt = example["prompt"]
    chosen = example["chosen"]  # 좋은 답변
    rejected = example["rejected"]  # 나쁜 답변
    # DPO 학습에 사용
```

##### SFT 학습 예시
```python
### Alpaca 형식
sft_data = dataset["train"].filter(lambda x: x["type"] == "sft_instruction")
for example in sft_data:
    instruction = example["instruction"]
    output = example["output"]
    # 지시학습에 사용
```

#### 데이터 출처

- **원본 데이터**: [AIHub 초거대 언어모델 신뢰성 벤치마크 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71623)
- **구축기관**: 한국지능정보사회진흥원(NIA)
- **라이선스**: CC BY-NC 4.0

#### 사용 권한 및 이용 약관

이 데이터셋은 AIHub의 이용 약관을 준수합니다:
- 연구 및 비상업적 목적으로 자유롭게 사용 가능
- 상업적 사용 시 AIHub 이용 약관 확인 필요
- 데이터 재배포 시 출처 명시 필수

#### 인용

```bibtex
@dataset{korean_llm_trustworthiness,
  title={Korean LLM Trustworthiness Benchmark},
  author={AIHub},
  year={2024},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/neuralfoundry-coder/korean-llm-trustworthiness-benchmark}
}
```

#### 통계

| 데이터셋 | 레코드 수 |
|---------|-----------|
| DPO Preference | 1,000 |
| SFT Instruction | 1,000 |
| Fact Checking | 1,000 |
| **총계** | **3,000** |

#### 변경 이력

- v1.0.1 (2024): 통합 형식으로 재구성
- v1.0.0 (2024): 초기 버전 공개
