---
pretty_name: Korea In-Force Statutes (국가법령정보센터 / 법제처)
license: other
license_name: kr-copyright-act-7
language:
- ko
task_categories:
- text-retrieval
tags:
- legal
- law
- korea
- republic-of-korea
- law-go-kr
- official-texts
size_categories:
- 1K<n<10K
configs:
- config_name: laws
  data_files: data/laws.parquet
  default: true
- config_name: articles
  data_files: data/articles.parquet
---

# Korea In-Force Statutes (국가법령정보센터 / 법제처)

Research snapshot of **in-force national 법령** of the **Republic of Korea (ROK, not DPRK)**
from 국가법령정보센터 (법제처), published via law.go.kr public HTML.

**Not legal advice.** The official gazette (*관보*) / authentic 법제처 text prevails over this corpus.

## Snapshot

| Field | Value |
| --- | --- |
| Snapshot date | 2026-09-03 |
| Coverage | snapshot (현행법령) |
| Source | 국가법령정보센터 (법제처, law.go.kr) 현행법령 HTML |
| Collector | `scrapers/collect_law_go_kr.py` |
| Laws / instruments | 5,659 |
| Articles | 174,324 |
| Retrieval mix | live 5,659 / archive 0 |
| Language | Korean (`ko`) |
| Jurisdiction | Republic of Korea (national) |
| License | `kr-copyright-act-7` (저작권법 제7조 제1호) |

## Contents

- `data/laws.parquet` — one row per in-force national instrument (zstd).
- `data/articles.parquet` — article/조문 rows for the same snapshot (zstd).
- `scrapers/collect_law_go_kr.py` — research collector used to build this snapshot.

## License / reuse

Official ROK legislative texts (헌법·법률·조약·명령·조례 및 규칙) are **not copyright-protected**
under **저작권법 제7조 제1호**. This is a research snapshot of public HTML from
국가법령정보센터. `license: other` / `license_name: kr-copyright-act-7`.

This dataset is **not legal advice**. The official gazette / law.go.kr authentic text prevails.

## Source

- Portal: https://www.law.go.kr/
- Open API docs (OC key **not** used): https://open.law.go.kr/
- Ministry of Government Legislation: https://www.moleg.go.kr/
- Listing: `POST /LSW/lsScListR.do` (현행법령)
- Bodies: `POST /LSW/lsInfoR.do` (session from `lsInfoP.do`)

No invented OC/Open API key. No commercial DBs (lawnb etc.). robots.txt `Allow:/`.

## Known gaps

- National **現行법령** only. **자치법규(조례)** and **행정규칙(훈령·예규·고시)** are out of scope.
- Treaties (조약) not collected.
- Catalog listed 6,010 unique `lsiSeq`; 5,659 unique instrument JSON after `lsId` dedup
  (444 catalog rows skipped as duplicate ids). Fetch fail=0.
- Listing kind labels: 법률 2,117; 대통령령 1,984; 총리령 106; 규칙류 ~369; 헌법 1;
  대통령긴급명령 1; kind unmarked `?` 1,432 (mostly 부령 / 공동부령).
- 법제처 법률 count on the 법령명 tab is ~2,255; this snapshot has 2,117 법률 from the
  public HTML listing (gap ~138 법률 vs that UI total).
- Some HTML bodies are short or 개정문 rather than a full 본문 (~43 texts under 80 chars).
- Hangul pretty URLs (`/법령/{명}`) are stored as `source_url` but bodies were fetched via `lsInfoR.do`.
- Live HTML only for this snapshot (no Common Crawl / Wayback mix). Archive fallbacks are
  wired for 429/403 of official law.go.kr URLs; they were not needed.
