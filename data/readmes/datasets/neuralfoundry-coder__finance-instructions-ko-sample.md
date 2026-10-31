---
language:
- ko
- en
- zh
- ja
- vi
- id
license: other
license_name: aihub
license_link: https://aihub.or.kr/intrcn/guid/usagepolicy.do
tags:
- finance
- korean
- instruction-tuning
- sft
- qa
- translation
task_categories:
- question-answering
- translation
- text-generation
pretty_name: Korean Finance Instructions (Sample)
size_categories:
- 1K<n<10K
---

<!-- aegis-dataset-card -->

# finance-instructions-ko-sample

> **용도 기록 없음** · Korean Finance Instruction Dataset (Sample)  
> 파일 3개 · 1.3 MB · 행 1,314 · revision `cc485cce01` · 카드 갱신 2026-10-20  
> 전체 모델 ↔ 데이터 매핑 · 서버 복원 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020)

## 개요
본 데이터셋은 한국어 금융 분야 지시학습(Instruction Tuning) 데이터셋의 샘플 버전입니다.
카테고리별로 최대 1,000건씩 샘플링되어 있으며, 데이터 구조 확인 및 테스트 목적으로 활용할 수 있습니다.
전체 데이터셋은 별도의 private 저장소에서 제공됩니다.

## 이 데이터로 학습한 모델
이 데이터로 학습했다는 기록(학습 설정 · 모델 카드)을 찾지 못했다. 카탈로그의 '확인 필요' 목록에 있다.

## 파일 구성
| 파일 | 크기 | 행 | 내용 |
|---|---|---|---|
| `README.md` | 3.3 KB | - |  |
| `data/test-00000-of-00001.parquet` | 158.4 KB | 132 |  |
| `data/train-00000-of-00001.parquet` | 1.2 MB | 1,182 |  |

## 필드 · 범주 분포
**`data/test-00000-of-00001.parquet`, `data/train-00000-of-00001.parquet`** (기준 `data/train-00000-of-00001.parquet`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `instruction` | string | 100% |
| `input` | string | 100% |
| `output` | string | 100% |
| `category` | string | 100% |
| `source` | string | 100% |
| `metadata` | string | 100% |

범주 분포(기준 파일):
- `category`: finance_qa 904(76%) · finance_synthetic 278(24%)
- `source`: 151.금융,법률_문서_기계독해_데이터 904(76%) · 117.금융_합성데이터 278(24%)

필드는 행 최상위 키, 채움은 그 키가 있는 행 비율이다. 범주 분포는 글 필드가 아니고 값이 짧고(≤48자) 종류가 적은(≤40) 필드만 셌다.

## 내려받기 · 복원
```bash
hf download neuralfoundry-coder/finance-instructions-ko-sample --repo-type dataset --local-dir <폴더>
```
- 서버 파일 전체의 위치 · 재생성 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020) 의 `restore_map.json`

## 기존 설명 (2026-10-20 이전 카드)

### Korean Finance Instruction Dataset (Sample)

#### 데이터셋 개요

본 데이터셋은 한국어 금융 분야 지시학습(Instruction Tuning) 데이터셋의 샘플 버전입니다.
카테고리별로 최대 1,000건씩 샘플링되어 있으며, 데이터 구조 확인 및 테스트 목적으로 활용할 수 있습니다.
전체 데이터셋은 별도의 private 저장소에서 제공됩니다.

#### 데이터 형식

본 데이터셋은 현대 sLLM (small Language Model) 지시학습(Instruction Tuning)에 최적화된 형식으로 구성되어 있습니다.

```json
{
  "instruction": "사용자에게 제시할 지시사항 또는 질문",
  "input": "컨텍스트 또는 참고 자료 (선택적)",
  "output": "기대되는 출력 또는 답변",
  "category": "카테고리명",
  "source": "원본 데이터셋",
  "metadata": {"doc_id": "문서ID", "task_type": "태스크유형"}
}
```

#### 카테고리

| 카테고리 | 설명 | 건수 |
|---------|------|-----|
| 금융 문서 기계독해 (QA) | finance_qa | 1,000 |
| 금융 합성데이터 분석 | finance_synthetic | 314 |

#### 데이터 출처

본 데이터셋은 AI Hub에서 제공하는 다음 금융 데이터셋을 가공하여 구축하였습니다:

- **151. 금융,법률 문서 기계독해 데이터**: 금융 문서 QA (정답추출, Yes/No, 다지선다, 절차형)
- **117. 금융 합성데이터**: 카드/CB/금융상품 합성 데이터

#### 사용 권한

⚠️ **중요: AI Hub 이용약관 준수 필수**

본 데이터셋은 AI Hub에서 제공하는 공개 데이터를 기반으로 구축되었습니다.
사용 시 반드시 [AI Hub 이용약관](https://aihub.or.kr/intrcn/guid/usagepolicy.do)을 준수해야 합니다.

##### 주요 이용조건
- 비영리 연구 목적으로 사용 권장
- 영리 목적 사용 시 AI Hub 이용정책 확인 필요
- 데이터 재배포 시 출처 명시 필수
- 개인정보 포함 데이터는 익명화 처리됨

#### 데이터 통계

- **총 데이터 건수**: 1,314
- **학습 데이터**: 1,182
- **테스트 데이터**: 132
- **생성일**: 2026-01-10T12:42:54.580318

#### 사용 예시

```python
from datasets import load_dataset

### 데이터셋 로드
dataset = load_dataset("neuralfoundry-coder/finance-instructions-ko-sample")

### 샘플 확인
print(dataset["train"][0])

### instruction-tuning 형식으로 변환
def format_instruction(example):
    if example["input"]:
        return f"### 지시사항:\n{example['instruction']}\n\n### 입력:\n{example['input']}\n\n### 출력:\n{example['output']}"
    else:
        return f"### 지시사항:\n{example['instruction']}\n\n### 출력:\n{example['output']}"

formatted = dataset["train"].map(lambda x: {"text": format_instruction(x)})
```

#### 인용

본 데이터셋을 연구에 활용하실 경우, AI Hub 출처와 본 데이터셋을 인용해 주세요.

#### 연락처

문의사항이 있으시면 이슈를 등록해 주세요.
