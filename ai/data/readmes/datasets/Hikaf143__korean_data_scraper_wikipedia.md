---
license: cc-by-sa-4.0
language:
- ko
task_categories:
- text-generation
tags:
- korean
- wikipedia
- corpus
- llm-pretraining
size_categories:
- 1M<n<10M
---

# Korean Data Scraper — Wikipedia Dump Corpus

**상태: 비공개 (private) 저장소입니다.**

`Korean_data_scraper` 프로젝트의 `wikipedia_dump` 소스가 생성한 코퍼스입니다. 한국어 위키백과(ko.wikipedia.org) 덤프를 파싱하여 문서 본문 텍스트를 추출한 결과입니다.

## 스키마

파일당 1개 레코드(JSONL)이며, `korean_data_scraper_kakaotalk`와 동일한 공통 스키마를 따릅니다.

```json
{"id": "kowiki:70773", "source": "wikipedia_dump", "text": "..."}
```

`id`는 `kowiki:<문서 ID>` 형태이며, `text`는 해당 위키백과 문서의 본문 텍스트입니다.

## 데이터 규모 및 한계

전체 32개 샤드(shard-00000~00031)로 구성되며, 총 용량은 약 2.24GB입니다. 이 중 `shard-00017.jsonl`, `shard-00018.jsonl` 두 파일은 0바이트로 비어 있습니다(수집 과정에서 실패했거나 해당 구간에 유효한 문서가 없었던 것으로 추정 — 재확인 필요).

정제 로직은 `Korean_data_scraper` 프로젝트의 `src/kds/sources/wikipedia_dump.py`에 있습니다.

## 라이선스 및 저작권 표시 / License and Copyright Notice

한국어 위키백과 문서 본문은 위키미디어 재단의 정책에 따라 **CC BY-SA 4.0**(및 구버전 문서의 경우 GFDL) 라이선스로 제공되는 내용이며, 이 저장소는 그 원본 라이선스를 변경하지 않고 그대로 따릅니다. 재배포 시 CC BY-SA의 저작자 표시 및 동일조건변경허락 조건을 준수해야 합니다.

**이 저장소의 수집·파싱 스크립트 및 구성(스키마 정규화, 샤딩)은 주식회사 MKD(MKD Inc.)가 수행했습니다.** 다만 문서 본문 자체의 저작권은 위키백과 각 문서의 기여자들에게 있으며, 주식회사 MKD는 원본 콘텐츠에 대한 별도의 소유권을 주장하지 않습니다. 이 저장소의 스크립트·구성에 대한 재사용은 사전 서면 동의를 받으시기 바랍니다.

The text of Korean Wikipedia articles is made available under **CC BY-SA 4.0** (and GFDL for older article revisions) per the Wikimedia Foundation's licensing policy, and this repository does not alter that original license. Redistribution must comply with CC BY-SA's attribution and share-alike terms.

**The collection and parsing scripts and the organization of this repository (schema normalization, sharding) were produced by MKD Inc. (주식회사 MKD).** Copyright in the article text itself remains with the Wikipedia contributors, and MKD Inc. claims no separate ownership over the original content. Please seek prior written permission before reusing this repository's own scripts or structure.
