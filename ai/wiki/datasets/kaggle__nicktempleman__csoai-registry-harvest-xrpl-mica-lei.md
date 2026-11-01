---
type: "dataset"
id: "kaggle/nicktempleman/csoai-registry-harvest-xrpl-mica-lei"
source: "kaggle"
url: "https://www.kaggle.com/datasets/nicktempleman/csoai-registry-harvest-xrpl-mica-lei"
downloads: 40
summary: "XRPL 발행자, MiCA, LEI 정보를 결합한 공개 레지스트리 데이터셋으로 자산 검증에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
---
# kaggle/nicktempleman/csoai-registry-harvest-xrpl-mica-lei

> dataset · [Kaggle](https://www.kaggle.com/datasets/nicktempleman/csoai-registry-harvest-xrpl-mica-lei)

XRPL 발행자, MiCA, LEI 정보를 결합한 공개 레지스트리 데이터셋으로 자산 검증에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `name-normalised with a hand-checked alias map.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Public registers and public ledgers joined, read 2026-09-04T07:12:30Z.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `Public registers and public ledgers joined` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Every LEI in the ESMA CASP register can be checked with arithmetic alone` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `XRPL issuers × MiCA × LEI` · 신뢰도 low
