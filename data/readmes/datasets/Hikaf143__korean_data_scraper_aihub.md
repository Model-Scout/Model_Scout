---
license: other
license_name: mixed-aihub-source-licenses
language:
- ko
task_categories:
- text-generation
tags:
- korean
- aihub
- corpus
- llm-pretraining
size_categories:
- 1M<n<10M
---

# Korean Data Scraper — AI-Hub Local Corpus

**상태: 비공개 (private) 저장소입니다.**

`Korean_data_scraper` 프로젝트의 `aihub_local` 소스가 생성한 코퍼스입니다. 국립정보화진흥원 AI-Hub(aihub.or.kr)에서 내려받은 여러 데이터셋의 로컬 zip 압축 파일을 압축 해제하고, 그 안의 json 파일에서 본문 텍스트를 추출한 결과입니다. 샘플로 확인한 내용 중에는 뉴스 기사(신문기사) 카테고리의 AI-Hub 데이터셋에서 추출된 텍스트가 포함되어 있습니다.

## 스키마

파일당 1개 레코드(JSONL)이며, 다음과 같은 필드를 가집니다.

```json
{"id": "aihub_local:<zip 파일명>:<json 파일명>", "source": "aihub_local", "text": "...", "url": null, "license": "per-dataset -- check the dataset's page on aihub.or.kr before use", "meta": {"zip": "<zip 파일명>"}}
```

`id`는 원본 zip 파일명과 그 안의 json 파일명을 결합한 값이며, `meta.zip`에 원본 zip 파일명이 별도로 기록되어 있어 어떤 AI-Hub 데이터셋에서 유래했는지 역추적할 수 있습니다.

## 데이터 규모

총 용량은 약 9.2GB이며, `shard-00000.jsonl`부터 시작하는 다수의 JSONL 샤드 파일로 구성됩니다(전체 샤드 수는 저장소의 Files and versions 탭에서 확인 가능합니다).

정제 로직은 `Korean_data_scraper` 프로젝트의 `src/kds/sources/aihub_local.py`에 있습니다.

## 라이선스에 관한 중요 안내 / Important Notice on Licensing

**이 저장소는 여러 AI-Hub 데이터셋을 하나로 합친 것이며, AI-Hub 데이터셋마다 라이선스 조건이 서로 다릅니다.** 각 레코드의 `license` 필드는 개별 원본 라이선스를 명시하지 않고 "per-dataset -- check the dataset's page on aihub.or.kr before use"(데이터셋별로 상이하므로 사용 전 aihub.or.kr에서 반드시 확인할 것)라는 값으로 통일되어 있습니다. 이는 실제 라이선스를 아직 데이터셋 단위로 개별 확인·정리하지 못했다는 의미이며, **이 코퍼스를 실제로 활용하기 전에는 `meta.zip` 값을 통해 원본 AI-Hub 데이터셋을 특정하고, 해당 데이터셋 페이지에서 라이선스(상업적 이용 가능 여부, 재배포 조건 등)를 개별적으로 확인하는 작업이 반드시 선행되어야 합니다.** 일부 AI-Hub 데이터셋은 비상업적 이용만 허용하거나 재배포에 제한이 있을 수 있습니다.

**This repository merges multiple AI-Hub (aihub.or.kr) datasets, and licensing terms differ by source dataset.** The `license` field on every record is intentionally left as the placeholder "per-dataset -- check the dataset's page on aihub.or.kr before use" rather than a specific license, because the individual licenses have not yet been verified and catalogued per source dataset. **Before any real use of this corpus, each record's originating AI-Hub dataset should be identified via the `meta.zip` value, and that dataset's own page on aihub.or.kr must be checked individually for its license terms (commercial-use permission, redistribution conditions, etc.).** Some AI-Hub datasets permit non-commercial use only or restrict redistribution.

**이 저장소의 수집·압축해제·파싱 스크립트 및 구성(스키마 정규화, 샤딩)은 주식회사 MKD(MKD Inc.)가 수행했습니다.** 다만 원본 AI-Hub 데이터셋 본문 자체의 저작권 및 이용 조건은 각 데이터셋의 원 제공기관에 있으며, 주식회사 MKD는 원본 콘텐츠에 대한 별도의 소유권을 주장하지 않습니다. 이 저장소의 스크립트·구성에 대한 재사용은 사전 서면 동의를 받으시기 바랍니다.

**The collection, extraction, and parsing scripts and the organization of this repository (schema normalization, sharding) were produced by MKD Inc. (주식회사 MKD).** Copyright and usage terms for the original AI-Hub dataset content remain with each dataset's original provider, and MKD Inc. claims no separate ownership over the original content. Please seek prior written permission before reusing this repository's own scripts or structure.
