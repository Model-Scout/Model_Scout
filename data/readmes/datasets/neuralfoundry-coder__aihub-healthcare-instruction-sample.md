---
license: other
license_name: aihub
license_link: https://aihub.or.kr/intrcn/guid/usagepolicy.do
language:
- ko
tags:
- medical
- healthcare
- instruction-tuning
- korean
- sLLM
size_categories:
- 10K<n<100K
pretty_name: "AI Hub 헬스케어 지시학습 데이터셋 (샘플)"
---

<!-- aegis-dataset-card -->

# aihub-healthcare-instruction-sample

> **용도 기록 없음** · AI Hub 헬스케어 지시학습 데이터셋 (샘플)  
> 파일 2개 · 11.0 MB · 행 17,868 · revision `f4d3bf0b09` · 카드 갱신 2026-10-20  
> 전체 모델 ↔ 데이터 매핑 · 서버 복원 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020)

## 개요
한국어 의료/헬스케어 도메인 sLLM 지시학습을 위한 데이터셋입니다.

## 이 데이터로 학습한 모델
이 데이터로 학습했다는 기록(학습 설정 · 모델 카드)을 찾지 못했다. 카탈로그의 '확인 필요' 목록에 있다.

## 파일 구성
| 파일 | 크기 | 행 | 내용 |
|---|---|---|---|
| `README.md` | 2.2 KB | - |  |
| `data/train-00000-of-00001.parquet` | 11.0 MB | 17,868 |  |

## 필드 · 범주 분포
**`data/train-00000-of-00001.parquet`** (기준 `data/train-00000-of-00001.parquet`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `instruction` | string | 100% |
| `input` | string | 100% |
| `output` | string | 100% |
| `source` | string | 100% |
| `category` | string | 100% |
| `subcategory` | string | 100% |

범주 분포(기준 파일):
- `subcategory`: 유전질환 1,000(6%) · 귀코목질환 1,000(6%) · 근골격질환 1,000(6%) · 신장비뇨기질환 1,000(6%) · 피부질환 1,000(6%) · 종양혈액질환 1,000(6%) · 호흡기질환 1,000(6%) · 소화기질환 1,000(6%) · 소아청소년질환 1,000(6%) · 눈질환 1,000(6%) · 유방내분비질환 1,000(6%) · 기타 1,000(6%) …

필드는 행 최상위 키, 채움은 그 키가 있는 행 비율이다. 범주 분포는 글 필드가 아니고 값이 짧고(≤48자) 종류가 적은(≤40) 필드만 셌다.

## 내려받기 · 복원
```bash
hf download neuralfoundry-coder/aihub-healthcare-instruction-sample --repo-type dataset --local-dir <폴더>
```
- 서버 파일 전체의 위치 · 재생성 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020) 의 `restore_map.json`

## 기존 설명 (2026-10-20 이전 카드)

### AI Hub 헬스케어 지시학습 데이터셋 (샘플)

한국어 의료/헬스케어 도메인 sLLM 지시학습을 위한 데이터셋입니다.

#### 데이터셋 정보

- **총 데이터 건수**: 17,868 (전체 55,000건 중 샘플)
- **언어**: 한국어
- **형식**: instruction-input-output

##### 카테고리별 분포

| 카테고리 | 건수 |
|---------|------|
| 감염성질환 | 3,958 |
| 귀코목질환 | 2,868 |
| 근골격질환 | 2,449 |
| 기타 | 5,029 |
| 뇌신경정신질환 | 2,605 |
| 눈질환 | 5,088 |
| 성형미용 및 재건 | 3,558 |
| 소아청소년질환 | 1,365 |
| 소화기질환 | 3,698 |
| 순환기질환 | 1,177 |
| 신장비뇨기질환 | 4,664 |
| 여성질환 | 1,123 |
| 유방내분비질환 | 3,953 |
| 유전질환 | 3,268 |
| 응급질환 | 766 |
| 종양혈액질환 | 3,745 |
| 치과질환 | 102 |
| 피부질환 | 3,477 |
| 호흡기질환 | 2,107 |

#### 데이터 형식

```json
{
  "instruction": "사용자에게 주어진 지시/질문",
  "input": "추가 컨텍스트 (선택적)",
  "output": "모델이 생성해야 할 응답",
  "source": "원본 데이터셋명",
  "category": "카테고리",
  "subcategory": "세부 분류 (질환 분류 등)"
}
```

#### 출처

이 데이터셋은 AI Hub에서 제공하는 다음 데이터셋들로 구성되어 있습니다:

- 120.초거대AI_사전학습용_헬스케어_질의응답_데이터

#### 사용 권한

이 데이터셋은 AI Hub 이용약관을 준수합니다.
- 연구 및 비상업적 목적으로 사용 가능
- 상업적 이용 시 AI Hub 정책 확인 필요
- 원 데이터셋의 출처 표기 필요

자세한 내용은 [AI Hub 이용 정책](https://aihub.or.kr/intrcn/guid/usagepolicy.do)을 참조하세요.

#### 주의사항

- 이 데이터셋의 의료 정보는 교육 목적으로만 사용해야 합니다.
- 실제 의료 상담이나 진단에 사용하지 마세요.
- LLM API를 활용하여 질문에 대한 답변을 생성하였습니다.
