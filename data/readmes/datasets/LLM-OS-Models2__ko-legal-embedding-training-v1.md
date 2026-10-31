---
language:
- ko
- en
license: other
task_categories:
- sentence-similarity
- text-retrieval
pretty_name: Korean Public Legal Embedding Training v1
size_categories:
- 100K<n<1M
---

# Korean Public Legal Embedding Training v1

실제 embedding 학습 queue가 소비하는 provenance-preserving 파생 JSONL이다.
source-native query/positive 관계와 deterministic bootstrap negative로 컴파일했다. 최종 학습 전 current-student hard-negative mining을 수행해야 한다.

- rows: **250,000**
- release eligible: **true**
- visibility: **public**
- use: public redistribution and model training
- exact benchmark query/evaluation-text matches: **0**
- exact retrieval-corpus matches: **0 unique hashes**

Sionic 9 및 MTEB task-family train source가 포함될 수 있다. 이 dataset으로 학습한 모델의
관련 점수는 clean zero-shot으로 해석하면 안 된다. 원 source의 license와 attribution은
`metadata/provenance.jsonl`에 row별로 보존되며 이 카드의 `other` 표기가 upstream 권리를
재허가하지 않는다.

## 파일

- `data/train.jsonl`: ms-swift query/positive/negative schema
- `metadata/provenance.jsonl`: source/revision/license/exposure lineage
- `metadata/final_manifest.json`: exact order, row count, SHA, source counts
- `metadata/benchmark_overlap_audit.json`: 원문 없는 exact text-hash overlap 감사

## 원 dataset

- https://huggingface.co/datasets/legalize-kr/legalize-kr
- https://huggingface.co/datasets/legalize-kr/admrule-kr
- https://huggingface.co/datasets/legalize-kr/precedent-kr
- https://huggingface.co/datasets/legalize-kr/ordinance-kr

코드: https://github.com/LLM-OS-Models/Embedding
