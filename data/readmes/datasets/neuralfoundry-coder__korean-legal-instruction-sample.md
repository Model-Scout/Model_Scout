---
language:
- ko
license: other
license_name: aihub-terms
license_link: https://aihub.or.kr/intrcn/guid/usagepolicy.do
task_categories:
- question-answering
- summarization
- text-generation
tags:
- legal
- korean
- instruction-tuning
- law
- court-cases
- contracts
pretty_name: Korean Legal Instruction Dataset
size_categories:
- 100K<n<1M
---

<!-- aegis-dataset-card -->

# korean-legal-instruction-sample

> **용도 기록 없음** · Korean Legal Instruction Dataset (한국어 법률 지시학습 데이터셋)  
> 파일 3개 · 10.5 MB · 행 5,470 · revision `24ec2c3fb5` · 카드 갱신 2026-10-20  
> 전체 모델 ↔ 데이터 매핑 · 서버 복원 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020)

## 개요
이 데이터셋은 대한민국 법률 도메인에 특화된 sLLM 지시학습(Instruction Tuning)용 데이터셋입니다. 
AIHub에서 제공하는 16종의 법률 관련 데이터를 통합하여 현대 LLM 지시학습 포맷으로 가공하였습니다.

## 이 데이터로 학습한 모델
이 데이터로 학습했다는 기록(학습 설정 · 모델 카드)을 찾지 못했다. 카탈로그의 '확인 필요' 목록에 있다.

## 파일 구성
| 파일 | 크기 | 행 | 내용 |
|---|---|---|---|
| `README.md` | 5.2 KB | - |  |
| `data/train-00000-of-00001.parquet` | 9.5 MB | 4,923 |  |
| `data/validation-00000-of-00001.parquet` | 1.1 MB | 547 |  |

## 필드 · 범주 분포
**`data/train-00000-of-00001.parquet`, `data/validation-00000-of-00001.parquet`** (기준 `data/train-00000-of-00001.parquet`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `id` | string | 100% |
| `category` | string | 100% |
| `source` | string | 100% |
| `system` | string | 100% |
| `instruction` | string | 100% |
| `output` | string | 100% |
| `doc_id` | string | 100% |
| `court` | string | 100% |
| `case_type` | string | 100% |
| `case_name` | string | 100% |

범주 분포(기준 파일):
- `category`: legal_summarization 900(18%) · legal_mrc 900(18%) · contract_documents 900(18%) · case_analysis 900(18%) · intellectual_property_qa 738(15%) · civil_law_qa 585(12%)
- `case_type`:  4,157(84%) · civil 356(7%) · patent 217(4%) · criminal 170(3%) · administration 18(0%) · ccourt 5(0%)
- `source`: AIHub 법률-규정 텍스트 분석 데이터 (판례) 1,271(26%) · AIHub 금융/법률 문서 기계독해 데이터 900(18%) · AIHub 지식재산권법 LLM Instruction Tuning 데이터 741(15%) · AIHub 민사법 LLM Instruction Tuning 데이터 599(12%) · AIHub 계약 법률 문서 서식 데이터 530(11%) · AIHub 법률안 검토 보고서 요약 데이터 512(10%) · AIHub 계약 외 법률 문서 서식 데이터 370(8%)

필드는 행 최상위 키, 채움은 그 키가 있는 행 비율이다. 범주 분포는 글 필드가 아니고 값이 짧고(≤48자) 종류가 적은(≤40) 필드만 셌다.

## 내려받기 · 복원
```bash
hf download neuralfoundry-coder/korean-legal-instruction-sample --repo-type dataset --local-dir <폴더>
```
- 서버 파일 전체의 위치 · 재생성 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020) 의 `restore_map.json`

## 기존 설명 (2026-10-20 이전 카드)

### Korean Legal Instruction Dataset (한국어 법률 지시학습 데이터셋)

#### 데이터셋 개요

이 데이터셋은 대한민국 법률 도메인에 특화된 sLLM 지시학습(Instruction Tuning)용 데이터셋입니다. 
AIHub에서 제공하는 16종의 법률 관련 데이터를 통합하여 현대 LLM 지시학습 포맷으로 가공하였습니다.

##### 주요 특징

- **총 데이터 수**: 약 233,000건
- **언어**: 한국어
- **포맷**: ChatML/Alpaca 호환 대화 형식
- **도메인**: 법률 (민사, 형사, 행정, 지식재산권, 계약 등)

#### 데이터 구조

각 데이터 샘플은 다음과 같은 구조를 가집니다:

```json
{
  "id": "고유 식별자",
  "category": "카테고리명",
  "source": "원본 데이터 출처",
  "system": "시스템 프롬프트",
  "instruction": "사용자 질문/지시",
  "output": "AI 응답",
  "doc_id": "문서 ID",
  "court": "법원명",
  "case_type": "사건 유형",
  "case_name": "사건명"
}
```

#### 카테고리

| 카테고리 | 설명 | 데이터 수 |
|---------|------|----------|
| `civil_law_qa` | 민사법 질의응답 | 650 |
| `intellectual_property_qa` | 지식재산권법 질의응답 | 820 |
| `legal_summarization` | 법률 문서 요약 | 84,562 |
| `contract_documents` | 계약 문서 분석 | 11,403 |
| `case_analysis` | 판례 분석 | 39,446 |
| `legal_mrc` | 법률 기계독해 | 95,987 |

#### 원본 데이터 출처

이 데이터셋은 다음 AIHub 데이터를 기반으로 구축되었습니다:

1. **민사법 LLM 사전학습 및 Instruction Tuning 데이터**
   - 민사법 관련 판결문, 법령, 심결례, 유권해석 QA 및 요약

2. **지식재산권법 LLM 사전학습 및 Instruction Tuning 데이터**
   - 특허, 상표, 저작권 관련 법률 QA 및 요약

3. **행정법 LLM 사전학습 및 Instruction Tuning 데이터**
   - 행정법 관련 판결문, 결정례, 해석례 QA 및 요약

4. **형사법 LLM 사전학습 및 Instruction Tuning 데이터**
   - 형법, 형사소송법 관련 QA 및 요약

5. **계약 법률 문서 서식 데이터**
   - 각종 계약서 양식 및 조항 분석

6. **계약 외 법률 문서 서식 데이터**
   - 소송 관련 문서, 민원 문서 등

7. **법률안 검토 보고서 요약 데이터**
   - 국회 법률안 검토 보고서 요약

8. **법률-규정 텍스트 분석 데이터 고도화 (상황에 따른 판례 데이터)**
   - 민사, 가사, 형사, 행정 등 분야별 판례 분석

9. **금융, 법률 문서 기계독해 데이터**
   - 법률 문서 대상 QA 데이터

#### 사용 방법

##### HuggingFace Datasets 사용

```python
from datasets import load_dataset

### 전체 데이터셋 로드 (Private)
dataset = load_dataset("neuralfoundry-coder/korean-legal-instruction-full")

### 샘플 데이터셋 로드 (Public, 카테고리별 최대 1,000건)
dataset = load_dataset("neuralfoundry-coder/korean-legal-instruction-sample")

### 데이터 확인
print(dataset["train"][0])
```

##### 지시학습 프롬프트 구성

```python
def format_prompt(sample):
    return f"""### System:
{sample['system']}

##### User:
{sample['instruction']}

##### Assistant:
{sample['output']}"""
```

#### 데이터셋 통계

##### 전체 데이터셋 (Full)
- **Train**: 209,579건
- **Validation**: 23,289건
- **Total**: 232,868건

##### 샘플 데이터셋 (Public)
- **Train**: 4,923건
- **Validation**: 547건
- **Total**: 5,470건

#### 사용 권한 및 라이선스

##### AIHub 이용약관 준수

이 데이터셋은 [AIHub](https://aihub.or.kr) 이용약관을 따릅니다.

**주요 이용 조건:**
- 학술 연구 및 비영리 목적 사용 가능
- 영리 목적 사용 시 AIHub 승인 필요
- 데이터 재배포 시 출처 명시 필수
- 개인정보 보호 관련 법률 준수

자세한 내용은 [AIHub 이용정책](https://aihub.or.kr/intrcn/guid/usagepolicy.do)을 참조하세요.

#### 인용

이 데이터셋을 사용하실 경우 다음과 같이 인용해 주세요:

```bibtex
@dataset{korean_legal_instruction_2024,
  title={Korean Legal Instruction Dataset},
  author={AI Hub Contributors},
  year={2024},
  publisher={HuggingFace},
  url={https://huggingface.co/datasets/neuralfoundry-coder/korean-legal-instruction-sample}
}
```

#### 주의사항

1. **법률 자문 대체 불가**: 이 데이터셋으로 학습된 모델의 출력은 법률 자문을 대체할 수 없습니다.
2. **정확성 미보장**: AI 모델의 응답은 항상 검증이 필요합니다.
3. **개인정보**: 원본 데이터에서 개인정보가 마스킹 처리되어 있으나, 추가적인 검토가 권장됩니다.

#### 변경 이력

- **v1.0** (2024): 초기 릴리스
  - 6개 카테고리, 약 233,000건 데이터

#### 문의

데이터셋 관련 문의는 이슈를 통해 남겨주세요.
