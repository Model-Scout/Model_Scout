---
pretty_name: wellsa-ai treaty-kr (Korean Treaties)
language:
  - ko
license: mit
size_categories:
  - 1K<n<10K
task_categories:
  - question-answering
  - information-retrieval
  - text-retrieval
  - text-generation
tags:
  - korean
  - legal
  - treaty
  - international-law
  - public-data
  - rag
  - law
configs:
  - config_name: default
    data_files:
      - split: train
        path: train.jsonl
homepage: https://minilex.wellsa.ai
---

# wellsa-ai treaty-kr — Korean Treaties Dataset

> 한국 정부가 체결한 양자·다자 조약 메타데이터 + 본문 (markdown frontmatter 형식).
> MiniLex 7종 한국 법령 데이터 인프라 중 하나.

## Snapshot

- **Documents**: 6,907 treaties
- **Coverage**: 1905 ~ 2026 (83 unique years)
- **Types**: 양자조약(bilateral) 5,453 · 다자조약(multilateral) 1,454
- **Source**: 법제처 DRF OpenAPI (`target=trty`)
- **Pipeline**: daily cron `06:15~07:30 KST` (scrape → fetch_body → convert → commit)
- **Snapshot date**: 2026-06-05

## Schema

Each row in `train.jsonl`:

| field | type | description |
| --- | --- | --- |
| `id` | string | 조약일련번호 (unique stable id) |
| `treaty_no` | string | 조약번호 (gov-issued) |
| `treaty_name` | string | 조약명 (Korean) |
| `treaty_type` | string | 양자조약 / 다자조약 |
| `year` | string | 발효 연도 (subdir) |
| `effective_date` | string | 발효일자 (ISO 8601) |
| `sign_date` | string | 서명일자 |
| `gazette_date` | string | 관보게제일자 |
| `source_url` | string | 법제처 DRF 상세 링크 |
| `text` | string | 본문 markdown (메타 + 본문) |

## Usage

```python
from datasets import load_dataset
ds = load_dataset("wellsa-ai/treaty-kr", split="train")
print(ds[0])
```

또는 직접 jsonl 로:

```python
import json
with open("train.jsonl", encoding="utf-8") as f:
    for line in f:
        row = json.loads(line)
        print(row["treaty_name"], row["effective_date"])
```

## Canonical Source

이 dataset 은 **GitHub canonical repo 의 snapshot mirror** 입니다. live 데이터는 매일 갱신되는 GitHub 을 참조:

- **GitHub**: https://github.com/wellsa-ai/treaty-kr — daily cron 자동 갱신, Git history 로 변경 추적
- **MiniLex demo**: https://minilex.wellsa.ai — 7종 통합 검색

HF dataset 은 정기 snapshot 으로 유지되지만 변경 빈도가 낮아 GitHub source-of-truth 와 며칠 차이가 날 수 있습니다.

## Sibling Datasets (MiniLex 7종 인프라)

| dataset | docs | description |
| --- | --- | --- |
| [law-kr](https://github.com/wellsa-ai/law-kr) | 5,589 | 법령 (statutes) |
| [regulate-kr](https://github.com/wellsa-ai/regulate-kr) | 10,765 | 행정규칙 |
| [precedent-kr](https://github.com/wellsa-ai/precedent-kr) | 171K+ | 판례 |
| [interpretation-kr](https://github.com/wellsa-ai/interpretation-kr) | 8,728 | 법령해석례 |
| [constitution-kr](https://github.com/wellsa-ai/constitution-kr) | 38K+ | 헌재결정례 |
| [localrule-kr](https://github.com/wellsa-ai/localrule-kr) | 159K+ | 자치법규 |
| **treaty-kr** | **6,907** | **조약 (this dataset)** |

총 397K+ Korean legal documents.

## License

MIT. 데이터 출처는 한국 법제처 공공 OpenAPI 이며, MiniLex / wellsa-ai 는 수집·정렬·markdown 정규화 layer 를 제공합니다.

## Disclaimer

This dataset is a **source-grounded retrieval corpus**, not a substitute for licensed legal advice. Always verify with a qualified Korean legal professional for actual decisions.

## Citation

```bibtex
@misc{wellsa_ai_treaty_kr_2026,
  title  = {treaty-kr: Korean Treaties Dataset (MiniLex 7-domain Korean lawdata infrastructure)},
  author = {wellsa-ai},
  year   = {2026},
  url    = {https://huggingface.co/datasets/wellsa-ai/treaty-kr},
  note   = {Snapshot 2026-06-05}
}
```
