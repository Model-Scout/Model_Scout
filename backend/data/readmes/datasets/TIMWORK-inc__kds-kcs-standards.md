---
license: cc-by-4.0
language:
- ko
tags:
- construction
- standards
- korean
- kds
- kcs
- building-codes
size_categories:
- 1K<n<10K
---

# KDS/KCS 한국 건설기준 데이터셋

국가건설기준센터(KCSC)에서 제공하는 **KDS(설계기준)**와 **KCS(표준시방서)** 데이터셋입니다.

## 데이터 개요

| 구분 | 설명 | 파일 수 |
|------|------|---------|
| **KDS** | Korean Design Standard (설계기준) | 548 |
| **KCS** | Korean Construction Specification (표준시방서) | 769 |
| **합계** | | **1,317** |

## 데이터 구조

```
data/
├── kds/
│   ├── 100000.json    # 공통설계기준
│   ├── 141000.json    # 콘크리트구조 일반사항
│   ├── 411015.json    # 콘크리트구조 설계기준
│   └── ...
├── kcs/
│   ├── 100000.json    # 공통시방
│   ├── 142010.json    # 콘크리트공사 일반사항
│   └── ...
└── metadata.json
```

## JSON 스키마

각 파일은 다음 구조를 따릅니다:

```json
{
  "no": 5783,
  "codeType": "KDS",
  "code": "411015",
  "fullCode": "2010411015",
  "name": "콘크리트구조 설계기준",
  "version": "2025",
  "updateDate": "2024-12-15T10:00:00",
  "listParentCodes": [
    {"codeType": "KDS", "fullCode": "41", "name": "건축구조"}
  ],
  "list": [
    {
      "no": 5783,
      "sort": 1,
      "title": "1. 일반사항",
      "level": 1,
      "content": "1.1 적용범위\n이 기준은 ...",
      "children": [...]
    }
  ],
  "downloaded_at": "2026-01-23T22:00:00"
}
```

### 필드 설명

| 필드 | 설명 |
|------|------|
| `codeType` | "KDS" 또는 "KCS" |
| `code` | 6자리 코드 (예: "411015") |
| `fullCode` | 전체 코드 (예: "2010411015") |
| `name` | 기준/시방서 명칭 |
| `version` | 버전 연도 |
| `list` | 본문 내용 (장/절/항 구조) |
| `is_category` | `true`면 상위 분류 코드 (본문 없음) |

## 사용 방법

### Python (datasets 라이브러리)

```python
from datasets import load_dataset

# 전체 로드
dataset = load_dataset("TIMWORK-inc/kds-kcs-standards")

# 특정 파일 접근
import json
from huggingface_hub import hf_hub_download

file = hf_hub_download(
    "TIMWORK-inc/kds-kcs-standards",
    "data/kds/411015.json",
    repo_type="dataset"
)
with open(file) as f:
    data = json.load(f)
```

### CLI

```bash
# 전체 다운로드
hf download TIMWORK-inc/kds-kcs-standards --repo-type dataset

# 특정 폴더만
hf download TIMWORK-inc/kds-kcs-standards data/kds --repo-type dataset
```

## 코드 체계

### KDS (설계기준)

| 코드 범위 | 분야 |
|-----------|------|
| 10XXXX | 공통설계기준 |
| 14XXXX | 콘크리트구조 |
| 24XXXX | 교량설계 |
| 41XXXX | 건축구조 |
| 44XXXX | 도로설계 |

### KCS (표준시방서)

| 코드 범위 | 분야 |
|-----------|------|
| 10XXXX | 공통시방 |
| 14XXXX | 콘크리트공사 |
| 24XXXX | 교량공사 |
| 41XXXX | 건축공사 |
| 44XXXX | 도로공사 |

## 출처

- **데이터 원본**: [국가건설기준센터 (KCSC)](https://www.kcsc.re.kr/)
- **API**: KCSC OpenAPI
- **라이선스**: CC BY 4.0 (공공데이터)

## 업데이트

- **2026-01-23**: 초기 버전 (KDS 548 + KCS 769 = 1,317개)

KDS/KCS는 연 1-2회 개정됩니다. 최신 버전은 [KCSC 공식 사이트](https://www.kcsc.re.kr/)에서 확인하세요.
