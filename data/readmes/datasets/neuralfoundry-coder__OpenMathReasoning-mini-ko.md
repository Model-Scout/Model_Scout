---
language:
- ko
- en
license: cc-by-4.0
tags:
- math
- mathematics
- reasoning
- korean
- translated
- chain-of-thought
- cot
pretty_name: OpenMathReasoning-mini Korean
size_categories:
- 10K<n<100K
task_categories:
- question-answering
- text-generation
source_datasets:
- unsloth/OpenMathReasoning-mini
- nvidia/OpenMathReasoning
dataset_info:
  features:
  - name: expected_answer
    dtype: string
  - name: problem_type
    dtype: string
  - name: problem_source
    dtype: string
  - name: generation_model
    dtype: string
  - name: pass_rate_72b_tir
    dtype: string
  - name: problem
    dtype: string
  - name: generated_solution
    dtype: string
  - name: inference_mode
    dtype: string
  splits:
  - name: cot
    num_bytes: 47448659
    num_examples: 19252
  download_size: 19879537
  dataset_size: 47448659
configs:
- config_name: default
  data_files:
  - split: cot
    path: data/cot-*
---

<!-- aegis-dataset-card -->

# OpenMathReasoning-mini-ko

> **용도 기록 없음** · OpenMathReasoning-mini Korean (한국어 번역)  
> 파일 3개 · 73.6 MB · 행 38,504 · revision `71484514d4` · 카드 갱신 2026-10-20  
> 전체 모델 ↔ 데이터 매핑 · 서버 복원 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020)

## 개요
이 데이터셋은 **[unsloth/OpenMathReasoning-mini](https://huggingface.co/datasets/unsloth/OpenMathReasoning-mini)** 데이터셋을 한국어로 번역한 버전입니다.

## 이 데이터로 학습한 모델
| 모델 | 관계 | 사용 부분 | 비고 |
|---|---|---|---|
| 에이전트 v7a · v7b(HF 미공개) — clean/ko_native.jsonl 경유 | 학습(가공 후 · 가중치 HF 없음) | 전체 |  |

관계: 학습(직접) = 이 파일을 그대로 학습에 씀 · 학습(가공 후) = 코퍼스 · SFT 혼합을 만드는 입력(재생성 방법은 카탈로그) · 생성 입력(원본) = 합성 · 정리 단계의 원본 기록.

## 파일 구성
| 파일 | 크기 | 행 | 내용 |
|---|---|---|---|
| `README.md` | 6.0 KB | - |  |
| `data/cot-00000-of-00001.parquet` | 19.9 MB | 19,252 |  |
| `data/openmath_ko_20260110_140055.jsonl` | 53.8 MB | 19,252 |  |

## 필드 · 범주 분포
**`data/cot-00000-of-00001.parquet`, `data/openmath_ko_20260110_140055.jsonl`** (기준 `data/cot-00000-of-00001.parquet`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `expected_answer` | string | 100% |
| `problem_type` | string | 100% |
| `problem_source` | string | 100% |
| `generation_model` | string | 100% |
| `pass_rate_72b_tir` | string | 100% |
| `problem` | string | 100% |
| `generated_solution` | string | 100% |
| `inference_mode` | string | 100% |

범주 분포(기준 파일):
- `problem_source`: aops_c4_high_school_math 7,006(36%) · aops_c6_high_school_olympiads 6,621(34%) · aops_c7_college_math 4,754(25%) · aops_c5_contests_amp_programs 725(4%) · MATH_training_set 146(1%)

필드는 행 최상위 키, 채움은 그 키가 있는 행 비율이다. 범주 분포는 글 필드가 아니고 값이 짧고(≤48자) 종류가 적은(≤40) 필드만 셌다.

## 내려받기 · 복원
```bash
hf download neuralfoundry-coder/OpenMathReasoning-mini-ko --repo-type dataset --local-dir <폴더>
```
- 서버 파일 전체의 위치 · 재생성 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020) 의 `restore_map.json`

## 기존 설명 (2026-10-20 이전 카드)

### OpenMathReasoning-mini Korean (한국어 번역)

이 데이터셋은 **[unsloth/OpenMathReasoning-mini](https://huggingface.co/datasets/unsloth/OpenMathReasoning-mini)** 데이터셋을 한국어로 번역한 버전입니다.

원본 데이터셋은 **[nvidia/OpenMathReasoning](https://huggingface.co/datasets/nvidia/OpenMathReasoning)** 에서 파생되었습니다.

#### 데이터셋 정보

| 항목 | 내용 |
|------|------|
| **원본 데이터셋** | [unsloth/OpenMathReasoning-mini](https://huggingface.co/datasets/unsloth/OpenMathReasoning-mini) |
| **원본 출처** | [nvidia/OpenMathReasoning](https://huggingface.co/datasets/nvidia/OpenMathReasoning) |
| **라이선스** | CC-BY-4.0 |
| **행 수** | 19,252 |
| **언어** | 한국어 (Korean), 영어 (English) |
| **번역 대상 컬럼** | `expected_answer`, `problem`, `generated_solution` |

#### 라이선스 및 귀속

이 데이터셋은 원본 데이터셋인 **nvidia/OpenMathReasoning**의 **CC-BY-4.0** 라이선스를 따릅니다.

- **원저작자**: NVIDIA Corporation
- **원본 데이터셋**: https://huggingface.co/datasets/nvidia/OpenMathReasoning
- **관련 논문**: [arXiv:2504.16891](https://arxiv.org/abs/2504.16891)

#### 면책 조항 (Disclaimer)

> ⚠️ **중요**: 이 데이터셋의 사용으로 인해 발생하는 모든 책임은 **사용자에게** 있습니다.

- 이 데이터셋은 기계 번역(LLM 기반)을 통해 생성되었으며, 번역 품질이 완벽하지 않을 수 있습니다.
- 수학 문제 및 풀이의 정확성은 원본 데이터셋에 의존하며, 번역 과정에서 의미가 변경되었을 수 있습니다.
- 상업적 사용 전 원본 라이선스(CC-BY-4.0)의 조건을 반드시 확인하시기 바랍니다.
- 교육 및 연구 목적으로 사용을 권장하며, 중요한 의사결정에는 별도의 검증이 필요합니다.

#### 컬럼 설명

| 컬럼명 | 설명 | 번역 여부 |
|--------|------|-----------|
| `expected_answer` | 문제의 정답 | ✅ 번역됨 |
| `problem_type` | 문제 유형 | ❌ 원본 유지 |
| `problem_source` | 문제 출처 | ❌ 원본 유지 |
| `generation_model` | 생성 모델 | ❌ 원본 유지 |
| `pass_rate_72b_tir` | 72B 모델 통과율 | ❌ 원본 유지 |
| `problem` | 수학 문제 | ✅ 번역됨 |
| `generated_solution` | 풀이 과정 (Chain-of-Thought) | ✅ 번역됨 |
| `inference_mode` | 추론 모드 | ❌ 원본 유지 |

#### 번역 방법론

##### 사용된 기술
- **번역 모델**: LLM 기반 기계 번역
- **API 엔드포인트**: 로컬 호스팅 LLM API

##### 수학 수식 보존 전략
번역 시 다음 항목들은 원본 그대로 보존됩니다:

1. **LaTeX 수식**
   - `\(...\)` (인라인 수식)
   - `\[...\]` (블록 수식)
   - `$...$`, `$$...$$` (달러 표기)

2. **수학 기호 및 표기**
   - 변수명: `x`, `y`, `z`, `n`, `k` 등
   - 함수명: `sin`, `cos`, `tan`, `log`, `ln` 등
   - 연산자: `+`, `-`, `×`, `÷`, `=`, `<`, `>` 등
   - 집합 기호: `∈`, `∉`, `⊂`, `⊃`, `∪`, `∩` 등

3. **숫자 및 수치 표현**
   - 모든 숫자와 계산 결과
   - 단위 표기

##### 번역 품질 관리
- 순수 수학 표현(숫자, 수식만 있는 경우)은 번역하지 않고 원본 유지
- LaTeX 수식 보존 여부 자동 검증
- 번역 실패 시 원문 유지

#### 사용 예시

##### Python (Hugging Face Datasets)

```python
from datasets import load_dataset

### 데이터셋 로드
dataset = load_dataset("neuralfoundry-coder/OpenMathReasoning-mini-ko")

### 첫 번째 예시 출력
example = dataset['cot'][0]
print(f"문제: {example['problem']}")
print(f"정답: {example['expected_answer']}")
print(f"풀이: {example['generated_solution'][:500]}...")
```

##### Pandas

```python
import pandas as pd
from datasets import load_dataset

### DataFrame으로 변환
dataset = load_dataset("neuralfoundry-coder/OpenMathReasoning-mini-ko")
df = pd.DataFrame(dataset['cot'])

### 문제 유형별 통계
print(df['problem_type'].value_counts())
```

#### 데이터셋 통계

- **총 행 수**: 19,252
- **Split**: `cot` (Chain-of-Thought)
- **파일 형식**: Parquet

#### 관련 링크

- **원본 데이터셋 (mini)**: [unsloth/OpenMathReasoning-mini](https://huggingface.co/datasets/unsloth/OpenMathReasoning-mini)
- **원본 데이터셋 (full)**: [nvidia/OpenMathReasoning](https://huggingface.co/datasets/nvidia/OpenMathReasoning)
- **NVIDIA 논문**: [arXiv:2504.16891](https://arxiv.org/abs/2504.16891)

#### 인용

이 데이터셋을 사용하실 경우, 원본 데이터셋을 인용해 주세요:

```bibtex
@misc{nvidia2025openmathreasoning,
  title={OpenMathReasoning: A Large-Scale Dataset for Mathematical Reasoning},
  author={NVIDIA},
  year={2025},
  url={https://huggingface.co/datasets/nvidia/OpenMathReasoning}
}
```

#### 업데이트 이력

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-01-10 | 1.0.0 | 초기 한국어 번역 버전 공개 |

---

**제작**: neuralfoundry-coder  
**원본 저작권**: NVIDIA Corporation (CC-BY-4.0)
