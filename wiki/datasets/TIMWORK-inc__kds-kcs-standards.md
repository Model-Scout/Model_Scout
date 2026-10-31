---
type: "dataset"
id: "TIMWORK-inc/kds-kcs-standards"
source: "huggingface"
url: "https://huggingface.co/datasets/TIMWORK-inc/kds-kcs-standards"
downloads: 121
summary: "국가건설기준센터 제공 KDS(설계기준)와 KCS(표준시방서) 한국 건설기준 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# TIMWORK-inc/kds-kcs-standards

> dataset · [Hugging Face](https://huggingface.co/datasets/TIMWORK-inc/kds-kcs-standards)

국가건설기준센터 제공 KDS(설계기준)와 KCS(표준시방서) 한국 건설기준 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `국가건설기준센터(KCSC)에서 제공하는 **KDS(설계기준)**와 KCS(표준시방서) 데이터셋입니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval = `data/
├── kds/
│   ├── 100000.json    # 공통설계기준
│   ├── 141000.json    # 콘크리트구조 일반사항
│   ├── 411015.json    # 콘크리트구조 설계기준
│   └── ...
├── kcs/
│   ├── 100000.jso` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `| 필드 | 설명 |
|------|------|
| `codeType` | "KDS" 또는 "KCS" |
| `code` | 6자리 코드 (예: "411015") |
| `fullCode` | 전체 코드 (예: "2010411015") |
| `name` | 기준/시방서 명칭 |
| ` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `국가건설기준센터(KCSC)에서 제공하는 **KDS(설계기준)**와 KCS(표준시방서) 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `- **2026-01-23**: 초기 버전 (KDS 548 + KCS 769 = 1,317개)` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
