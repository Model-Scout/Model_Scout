---
language:
- ko
license: cc-by-4.0
task_categories:
- text-generation
- fill-mask
pretty_name: Korean Law - 한국 법령 텍스트 데이터셋
size_categories:
- 1M<n<10M
tags:
- korean
- law
- legal
- legislation
- llm
- pretraining
---

# Korean Law - 한국 법령 텍스트 데이터셋

법제처 국가법령정보센터 OpenAPI를 통해 수집한 한국어 LLM 학습용 법령 데이터셋입니다.
법률, 대통령령, 부령 등 현행 법령 전문을 조문 단위로 추출하였습니다.

## 데이터셋 개요

| 항목 | 내용 |
|------|------|
| 언어 | 한국어 (ko) |
| 출처 | 법제처 국가법령정보센터 OpenAPI |
| 총 레코드 수 | 2,398,755건 |
| 총 텍스트 | 약 12.7억 자 |
| 평균 청크 길이 | 약 530자 |
| 수록 법령 수 | 약 221,847개 |
| 파일 수 | 9개 (law_ko_0000 ~ law_ko_0008) |

## 법령 유형 분포

| 법령 유형 | 설명 |
|-----------|------|
| 법률 | 국회에서 제정한 법 |
| 대통령령 | 대통령이 제정하는 시행령 |
| 부령 | 각 부처 장관이 제정하는 시행규칙 |
| 대법원규칙 | 대법원이 제정하는 규칙 |
| 헌법재판소규칙 | 헌법재판소가 제정하는 규칙 |
| 총리령 | 국무총리가 제정하는 규칙 |

## 데이터 구조

```json
{
  "mst": "253527",
  "law_name": "10ㆍ27법난 피해자의 명예회복 등에 관한 법률",
  "promulgation_date": "20230808",
  "enforcement_date": "20230808",
  "ministry": "문화체육관광부",
  "law_type": "법률",
  "조문번호": "2",
  "조문제목": "정의",
  "text": "제2조(정의) 이 법에서 사용하는 용어의 정의는 다음과 같다..."
}
```

### 필드 설명

| 필드 | 설명 |
|------|------|
| `mst` | 법령 고유 식별번호 |
| `law_name` | 법령명 |
| `promulgation_date` | 공포일 (YYYYMMDD) |
| `enforcement_date` | 시행일 (YYYYMMDD) |
| `ministry` | 소관 부처 |
| `law_type` | 법령 유형 (법률 / 대통령령 / 부령 등) |
| `조문번호` | 조문 번호 |
| `조문제목` | 조문 제목 |
| `text` | 조문 본문 텍스트 |

## 텍스트 필터링 기준

- 100자 미만 조문 제외
- 조문/항/호 단위로 분리

## 데이터 출처

- 법제처 국가법령정보센터: https://www.law.go.kr
- 국가법령정보 OpenAPI: https://open.law.go.kr

본 데이터셋은 공공데이터를 활용하여 구축되었습니다.
