---
license: other
language:
- ko
pretty_name: Korea municipal laws (자치법규)
tags:
- legal
- municipal
- south-korea
configs:
- config_name: laws
  data_files: data/laws-*.parquet
  default: true
- config_name: articles
  data_files: data/articles-*.parquet
---
# ipfs_korea_municipal_laws

Current (현행) local legislation of Korean local governments — ordinances (조례), rules (규칙) and other local
instruments — from the National Law Information Center (www.law.go.kr) of the Ministry of Government Legislation.
Ongoing harvest in batches (data/*-0000N.parquet); later batches add more local governments.

- `data/laws-0000N.parquet`: one row per instrument (full text, title, effective/promulgation dates, number, issuing government).
- `data/articles-0000N.parquet`: one row per article (제N조) plus one supplementary-provisions row (부칙, record_type `supplementary_provision`) per instrument; `law_id` joins to `laws.id`. `laws.article_count` counts 제N조 articles only.
- Extra columns in both tables: `municipality_id` (`kr-lgov-<local government code>`), `municipality_name`, `wikidata_qid`.

Copyright/terms (summary in our words): The National Law Information Center is the Ministry of Government Legislation's public database. Under the Korean Copyright Act official legislative texts, including local ordinances and rules, are not protected works; the site publishes them for free public use. The legally authoritative version is the one promulgated in each local government's official gazette.

Collection: robots.txt of www.law.go.kr (checked through the shared robots_guard on every request and redirect hop) allows all paths for all user agents and sets no crawl-delay; the collector still waited at least 2.5 s between requests, single-threaded. No login, no API key, no captcha/WAF workaround.

Not legal advice; consult the official gazette for authoritative text.

Municipalities so far (batches 001–025: 45,807 laws, 661,891 articles):

| municipality_id | name | wikidata_qid | laws |
|---|---|---|---|
| kr-lgov-6110000 | 서울특별시 | Q8684 | 1255 |
| kr-lgov-3080000 | 서울특별시 강북구 | Q50349 | 561 |
| kr-lgov-3150000 | 서울특별시 강서구 | Q50192 | 568 |
| kr-lgov-3220000 | 서울특별시 강남구 | Q20398 | 523 |
| kr-lgov-3240000 | 서울특별시 강동구 | Q50348 | 579 |
| kr-lgov-3040000 | 서울특별시 광진구 | Q50355 | 503 |
| kr-lgov-3160000 | 서울특별시 구로구 | Q50356 | 603 |
| kr-lgov-3170000 | 서울특별시 금천구 | Q50359 | 638 |
| kr-lgov-3200000 | 서울특별시 관악구 | Q50353 | 570 |
| kr-lgov-3050000 | 서울특별시 동대문구 | Q50382 | 582 |
| kr-lgov-3030000 | 서울특별시 성동구 | Q50411 | 589 |
| kr-lgov-3070000 | 서울특별시 성북구 | Q50412 | 530 |
| kr-lgov-3120000 | 서울특별시 서대문구 | Q50408 | 577 |
| kr-lgov-3210000 | 서울특별시 서초구 | Q20395 | 521 |
| kr-lgov-3230000 | 서울특별시 송파구 | Q50415 | 476 |
| kr-lgov-3130000 | 서울특별시 마포구 | Q50388 | 582 |
| kr-lgov-3190000 | 서울특별시 동작구 | Q50385 | 603 |
| kr-lgov-3090000 | 서울특별시 도봉구 | Q50374 | 578 |
| kr-lgov-3100000 | 서울특별시 노원구 | Q50368 | 654 |
| kr-lgov-3020000 | 서울특별시 용산구 | Q50429 | 490 |
| kr-lgov-3140000 | 서울특별시 양천구 | Q50420 | 566 |
| kr-lgov-3180000 | 서울특별시 영등포구 | Q50190 | 623 |
| kr-lgov-3000000 | 서울특별시 종로구 | Q36929 | 502 |
| kr-lgov-3010000 | 서울특별시 중구 | Q50441 | 543 |
| kr-lgov-3060000 | 서울특별시 중랑구 | Q50444 | 550 |
| kr-lgov-3110000 | 서울특별시 은평구 | Q50432 | 536 |
| kr-lgov-3360000 | 부산광역시 강서구 | Q50191 | 440 |
| kr-lgov-6260000 | 부산광역시 | Q16520 | 1198 |
| kr-lgov-3270000 | 부산광역시 동구 | Q50378 | 489 |
| kr-lgov-3310000 | 부산광역시 남구 | Q50363 | 517 |
| kr-lgov-3350000 | 부산광역시 금정구 | Q50358 | 407 |
| kr-lgov-3400000 | 부산광역시 기장군 | Q50217 | 535 |
| kr-lgov-3290000 | 부산광역시 부산진구 | Q50390 | 473 |
| kr-lgov-3300000 | 부산광역시 동래구 | Q50383 | 483 |
| kr-lgov-3320000 | 부산광역시 북구 | Q50394 | 486 |
| kr-lgov-3340000 | 부산광역시 사하구 | Q50400 | 503 |
| kr-lgov-3390000 | 부산광역시 사상구 | Q50398 | 414 |
| kr-lgov-3260000 | 부산광역시 서구 | Q50406 | 484 |
| kr-lgov-3380000 | 부산광역시 수영구 | Q50417 | 421 |
| kr-lgov-3250000 | 부산광역시 중구 | Q50440 | 466 |
| kr-lgov-3280000 | 부산광역시 영도구 | Q50423 | 455 |
| kr-lgov-3330000 | 부산광역시 해운대구 | Q50449 | 484 |
| kr-lgov-3370000 | 부산광역시 연제구 | Q50422 | 491 |
| kr-lgov-3440000 | 대구광역시 남구 | Q50362 | 445 |
| kr-lgov-5141000 | 대구광역시 군위군 | Q50215 | 432 |
| kr-lgov-6270000 | 대구광역시 | Q20927 | 951 |
| kr-lgov-3420000 | 대구광역시 동구 | Q50376 | 475 |
| kr-lgov-3450000 | 대구광역시 북구 | Q50393 | 512 |
| kr-lgov-3470000 | 대구광역시 달서구 | Q50370 | 586 |
| kr-lgov-3480000 | 대구광역시 달성군 | Q50239 | 576 |
| kr-lgov-3430000 | 대구광역시 서구 | Q50404 | 460 |
| kr-lgov-3460000 | 대구광역시 수성구 | Q50416 | 583 |
| kr-lgov-3410000 | 대구광역시 중구 | Q50438 | 413 |
| kr-lgov-3570000 | 인천광역시 강화군 | Q50205 | 504 |
| kr-lgov-6280000 | 인천광역시 | Q20934 | 1133 |
| kr-lgov-3510500 | 인천광역시 미추홀구 | Q50365 | 516 |
| kr-lgov-3530000 | 인천광역시 남동구 | Q50367 | 595 |
| kr-lgov-3550000 | 인천광역시 계양구 | Q50352 | 549 |
| kr-lgov-3565000 | 인천광역시 검단구 | Q18444594 | 523 |
| kr-lgov-3520000 | 인천광역시 연수구 | Q50421 | 494 |
| kr-lgov-3540000 | 인천광역시 부평구 | Q50391 | 500 |
| kr-lgov-3561000 | 인천광역시 서해구 | Q140403575 | 679 |
| kr-lgov-3491000 | 인천광역시 영종구 | - | 829 |
| kr-lgov-3501000 | 인천광역시 제물포구 | Q114364248 | 937 |
| kr-lgov-3580000 | 인천광역시 옹진군 | Q50310 | 438 |
| kr-lgov-3640000 | 대전광역시 동구 | Q50377 | 559 |
| kr-lgov-3680000 | 대전광역시 대덕구 | Q50371 | 593 |
| kr-lgov-6300000 | 대전광역시 | Q20921 | 947 |
| kr-lgov-3650000 | 대전광역시 중구 | Q50439 | 480 |
| kr-lgov-3660000 | 대전광역시 서구 | Q50405 | 569 |
| kr-lgov-3670000 | 대전광역시 유성구 | Q50431 | 578 |
| kr-lgov-5690000 | 세종특별자치시 | Q20929 | 961 |
| kr-lgov-6310000 | 울산광역시 | Q41278 | 937 |
| kr-lgov-3700000 | 울산광역시 남구 | Q50364 | 481 |
| kr-lgov-3710000 | 울산광역시 동구 | Q50379 | 494 |
| kr-lgov-3720000 | 울산광역시 북구 | Q50395 | 475 |
| kr-lgov-3730000 | 울산광역시 울주군 | Q50313 | 310 (partial; continues in a later batch) |
| kr-lgov-3690000 | 울산광역시 중구 | Q50442 | 524 |
| kr-lgov-3730000 | 울산광역시 울주군 | Q50313 | 244 (continued from batch 024) |
| kr-lgov-6410000 | 경기도 | Q20937 | 477 (partial; continues in a later batch) |

Instruments with no 제N조 articles (article_count 0) carry their whole text as one `body` row in the articles table.

Known gaps: heading-only article rows are not published. Batch 024 omits 9 articles (7 instruments) whose official law.go.kr HTML has the article heading but no body; they are listed with source-HTML hashes in `manifests/batch24_MANIFEST.md` and in each law's `metadata_json.known_gaps`. Batch 023 omits 1 such article (fix batch fix_b022_b023_v3); listed below and in `manifests/fix_b022_b023_v3_MANIFEST.md`. Deleted-article placeholders (heading such as `제6조(삭제 2011.10.19)`, no body at source) are published as article rows tagged `metadata_json.body_status = "repealed_placeholder"` (batches 022/023: 50 restored by fix_b022_b023_v3). Deleted-article placeholders (heading such as `제6조(삭제 2011.10.19)`, no body at source) are published as article rows tagged `metadata_json.body_status = "repealed_placeholder"` (batches 003/005/006/008/009/015/018/019/021: 472 tagged by fix_b003_b021_placeholders). Moved-article placeholders (heading such as `제12조(제9조로 이동 2019. 6. 28.)`, no body at source) are published as article rows tagged `metadata_json.body_status = "moved_placeholder"` (batch 018: 2 tagged by fix_b003_b021_placeholders). Batches 001, 002, 004, 010, 012, 014, 016, 017, 020 omit 2, 1, 1, 1, 1, 2, 1, 7, 1 such articles respectively (fix batch fix_b001_b024_placeholder_bodies); listed below and in `manifests/fix_b001_b024_placeholder_bodies_MANIFEST.md`. Deleted-article placeholders (heading such as `제6조(삭제 2011.10.19)`, no body at source) are published as article rows tagged `metadata_json.body_status = "repealed_placeholder"` (batches 002/004/010/014/016/017/020: 138 tagged by fix_b001_b024_placeholder_bodies). Deleted-article placeholders whose body is only the deletion note (e.g. `제8조 <삭제 2026.7.3.>`, `제33조 삭제 <2017.9.21.>`) are tagged `metadata_json.body_status = "repealed_placeholder"` with `placeholder_basis = "body_pattern"`, text unchanged (batches 001/002/003/004/005/006/008/009/010/012/014/015/016/017/018/019/020/021/022/023/024: 11930 tagged by fix_b001_b024_placeholder_bodies). Moved-article placeholders whose body is only the move note (e.g. `제5조 [제10조의4로 이동]`) are tagged `metadata_json.body_status = "moved_placeholder"` with `placeholder_basis = "body_pattern"`, text unchanged (batches 001/002/003/004/005/006/009/014/015/017/021/022/023/024: 75 tagged by fix_b001_b024_placeholder_bodies). Deleted-article placeholders whose body is only the deletion note (e.g. `제8조 <삭제 2026.7.3.>`, `제33조 삭제 <2017.9.21.>`) are tagged `metadata_json.body_status = "repealed_placeholder"` with `placeholder_basis = "body_pattern"`, text unchanged (batches 001/003/004/005/006/007/009/010/011/012/013/015/016/017/018/019/020/021/023/024: 2259 tagged by fix_placeholder_bodies_followup). Moved-article placeholders whose body is only the move note (e.g. `제5조 [제10조의4로 이동]`) are tagged `metadata_json.body_status = "moved_placeholder"` with `placeholder_basis = "body_pattern"`, text unchanged (batches 008/024: 2 tagged by fix_placeholder_bodies_followup). Short rows whose body is a deletion / move note in a form the body pattern does not cover (e.g. `제8조 <삭제 20 <삭제 2025.12.26.>`, `제9조 에서 이동`) were decided one by one (source check or text review) and tagged with `placeholder_basis = "reviewed"` and a `placeholder_review` reason, text unchanged (batches 002/004/005/006/009/012/017/019/023/024: 8 repealed_placeholder, 16 moved_placeholder tagged by fix_placeholder_bodies_followup; decisions in `manifests/fix_placeholder_bodies_followup_changed_ids.json` placeholder_reviews). Re-tagged by fix_placeholder_bodies_followup: `kr-muni-2028269-0009` moved_placeholder → repealed_placeholder (a deleted article with a moved note is a deleted-article placeholder; `placeholder_retagged_from` keeps the old tag; text unchanged). 11 short rows that mention 삭제 / 이동 but carry real provision text stay untagged (listed below, fix batch fix_placeholder_bodies_followup). Deleted-article placeholders whose body is only the deletion note (e.g. `제8조 <삭제 2026.7.3.>`, `제33조 삭제 <2017.9.21.>`) are tagged `metadata_json.body_status = "repealed_placeholder"` with `placeholder_basis = "body_pattern"`, text unchanged (batch 011: 6 tagged by fix_placeholder_followup2). Short rows whose body is a deletion / move note in a form the body pattern does not cover (e.g. `제8조 <삭제 20 <삭제 2025.12.26.>`, `제9조 에서 이동`) were decided one by one (source check or text review) and tagged with `placeholder_basis = "reviewed"` and a `placeholder_review` reason, text unchanged (batch 007: 1 repealed_placeholder, 0 moved_placeholder tagged by fix_placeholder_followup2; decisions in `manifests/fix_placeholder_followup2_changed_ids.json` placeholder_reviews). 1 row earlier tagged as placeholder is a live provision whose text is not in the official article; the tag is removed and the row is a known gap (listed below, fix batch fix_placeholder_followup2).

Code: `scrapers/` (collector, QID mapper, code bundler, robots guard, run script, pinned requirements, README, seeds, and the exact collectors used for earlier batches under `history/`); per-batch code records in `manifests/batchN_code.json`. Fix batches built with parser kr_ordin-4.1.3 carry their complete code tree as an addition under `scrapers/fix_b003_b021_placeholders/` (`manifests/fix_b003_b021_placeholders_code.json`); the earlier top-level `scrapers/` files are unchanged. Fix batch fix_b001_b024_placeholder_bodies (parser kr_ordin-4.1.4) carries its complete code tree as an addition under `scrapers/fix_b001_b024_placeholder_bodies/` (`manifests/fix_b001_b024_placeholder_bodies_code.json`); the top-level `scrapers/` files are unchanged. Fix batch fix_placeholder_bodies_followup (parser kr_ordin-4.1.5) carries its complete code tree as an addition under `scrapers/fix_placeholder_bodies_followup/` (`manifests/fix_placeholder_bodies_followup_code.json`); the top-level `scrapers/` files are unchanged. Fix batch fix_placeholder_followup2 (parser kr_ordin-4.1.6) carries its complete code tree as an addition under `scrapers/fix_placeholder_followup2/` (`manifests/fix_placeholder_followup2_code.json`); the top-level `scrapers/` files are unchanged.

### Known gaps — batches 022, 023

| batch | law_id | article id | label | body_status | source HTML sha256 | ordinInfoR.do | ordinInfoP.do |
|---|---|---|---|---|---|---|---|
| 023 | kr-muni-1909587 | kr-muni-1909587-0009 | 제9조 | empty_at_source | `bd26ac729299fa80b57cf10e62d2885c713d9c4c378502a4e774d56d0539a3b3` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=1909587) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=1909587 |

### Known gaps — fix_b001_b024_placeholder_bodies

| batch | law_id | article id | label | body_status | source HTML sha256 | ordinInfoR.do | ordinInfoP.do |
|---|---|---|---|---|---|---|---|
| 001 | kr-muni-2126163 | kr-muni-2126163-0004 | 제4조(단계별 제출서류) | image_only_at_source | `b8f91c809cd1ffbf15eadcbdcd738abc05a2e0ba198a1554f27ad329c6674d97` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=2126163) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=2126163 |
| 001 | kr-muni-1629445 | kr-muni-1629445-0001 | 전문 | section_heading_body_in_next_row | `87fb9a9812f5c50e8ab2e39fbc8de0c16b052094929ce18ecdb0850550a72e80` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=1629445) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=1629445 |
| 002 | kr-muni-2123877 | kr-muni-2123877-0011 | 제10조(과태료) | empty_at_source | `fcb062b3872fc7bccb16c53ac82edb072c944ebbf19270df556d8d7c8afce2e2` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=2123877) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=2123877 |
| 004 | kr-muni-2106657 | kr-muni-2106657-0012 | 부칙 <제정 2026. 1. 8. 조례 제1814호> | empty_at_source_supplementary | `a102004982ea110a50b13f5a6a094fb213b861e6523ebc4059c822408182602c` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=2106657) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=2106657 |
| 010 | kr-muni-1646485 | kr-muni-1646485-0005 | 제4조(책임) | empty_at_source | `f192ff0c926c02f3d8640abfc2640d8c96bd588b30e06f339c78f3d942a55eb9` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=1646485) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=1646485 |
| 012 | kr-muni-1666777 | kr-muni-1666777-0005 | 제4조(책임) | empty_at_source | `51a10f0c4373557e875090c0235a4b140a286a892297ce6355301078c0270bda` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=1666777) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=1666777 |
| 014 | kr-muni-1828139 | kr-muni-1828139-0007 | 제6조(사업자 등의 책무) | empty_at_source | `f0d8989e5f06da82085bcf6d84d65e6d035b31b4e0ce2866dab2a682f9787389` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=1828139) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=1828139 |
| 014 | kr-muni-1734779 | kr-muni-1734779-0009 | 제9조 | empty_at_source | `c444fd13993c174f6fdf829bc9a8a2823e254be3166c9b25675e609813d57a55` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=1734779) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=1734779 |
| 016 | kr-muni-1322120 | kr-muni-1322120-0012 | 부칙 (제 1100호, 2017. 12. 27.) | empty_at_source_supplementary | `c1ed086ed9a32041a75ef72adf3a22e121ceecebba959c51bd7d21b0a863563e` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=1322120) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=1322120 |
| 017 | kr-muni-1937103 | kr-muni-1937103-0012 | 제12조(상임위원 등) | empty_at_source | `f79e7a4baae11d5570cafe1961865b9d0fb10291b64230b7021dd36a3b743efd` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=1937103) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=1937103 |
| 017 | kr-muni-1937103 | kr-muni-1937103-0013 | 제13조(위촉) | empty_at_source | `f79e7a4baae11d5570cafe1961865b9d0fb10291b64230b7021dd36a3b743efd` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=1937103) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=1937103 |
| 017 | kr-muni-1937103 | kr-muni-1937103-0014 | 제14조(해촉) | empty_at_source | `f79e7a4baae11d5570cafe1961865b9d0fb10291b64230b7021dd36a3b743efd` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=1937103) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=1937103 |
| 017 | kr-muni-1937103 | kr-muni-1937103-0015 | 제15조(복무) | empty_at_source | `f79e7a4baae11d5570cafe1961865b9d0fb10291b64230b7021dd36a3b743efd` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=1937103) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=1937103 |
| 017 | kr-muni-1937103 | kr-muni-1937103-0016 | 제16조(보수 등) | empty_at_source | `f79e7a4baae11d5570cafe1961865b9d0fb10291b64230b7021dd36a3b743efd` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=1937103) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=1937103 |
| 017 | kr-muni-2104511 | kr-muni-2104511-0023 | 제20조(회의) | empty_at_source | `83ad68b2c70a6cf28d5b3ea5c56e58a019437778f81504fcba68d9a75e507208` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=2104511) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=2104511 |
| 017 | kr-muni-694624 | kr-muni-694624-0018 | 제18조 | empty_at_source | `8c8d520450328173a5e1db3cd401d25ecb8f6e81c17916d4f40cbedc4e735cfe` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=694624) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=694624 |
| 020 | kr-muni-1800041 | kr-muni-1800041-0006 | 제6조(관리비용 지원) | empty_at_source | `0f77a0ee3ac22e0af8970523ca9846a025703a03f9e2a88535fc38519b98dba2` | https://www.law.go.kr/LSW/ordinInfoR.do (POST ordinSeq=1800041) | https://www.law.go.kr/LSW/ordinInfoP.do?ordinSeq=1800041 |

### Reviewed rows left untagged — fix_placeholder_bodies_followup

Short article rows that mention 삭제 / 이동 but are not placeholders (real provision text); kept unchanged and untagged.

| batch | article id | reason |
|---|---|---|
| 003 | kr-muni-1915421-0009 | real text (provision '이 조례 시행에 필요한 사항은 규칙으로 정한다.') followed by a moved-from note '[제8조 에서 이동]' |
| 008 | kr-muni-2174853-0013 | real text (provision '이 조례의 시행에 필요한 사항은 규칙으로 정한다.') followed by a moved-from note '[제8조 에서 이동]' |
| 008 | kr-muni-2173359-0018 | real text (provision '이 조례 시행에 필요한 사항은 규칙으로 정한다.') followed by a moved-from note '<19조에서 이동>' |
| 008 | kr-muni-1871863-0009 | real text: provision on dissolving the council when US forces move ('주한미군이 이동하거나 …'); 이동 is ordinary vocabulary |
| 010 | kr-muni-2109543-0022 | real text: provision on a mobile library (이동도서관); 이동 is ordinary vocabulary |
| 018 | kr-muni-2014687-0014 | real text (provision '이 조례 시행에 필요한 사항은 규칙으로 정한다.') followed by a moved-from note '[제13조 에서 이동]' |
| 019 | kr-muni-2135627-0009 | real text: paragraph ① is a provision; only paragraph ② is deleted ('② 삭제 <2016.7.8.>') |
| 020 | kr-muni-1286507-0006 | real text: provision on mobile stalls (이동판매대); 이동 is ordinary vocabulary |
| 020 | kr-muni-1956063-0003 | real text: provision on a mobile counselling office (이동상담실); 이동 is ordinary vocabulary |
| 021 | kr-muni-2151339-0006 | real text: provision on mobile stalls (이동판매대); 이동 is ordinary vocabulary |
| 022 | kr-muni-1535321-0006 | real text: provision on mobile stalls (이동판매대); 이동 is ordinary vocabulary |

### Known gaps — fix_placeholder_followup2: rows without provision text

Article rows kept (text unchanged) that are NOT placeholders but whose provision text is not in the official article text; `metadata_json.body_status` names the gap and `placeholder_untagged_from` the removed tag.

| batch | article id | body_status | was | reason | source HTML sha256 |
|---|---|---|---|---|---|
| 008 | kr-muni-2096883-0004 | body_not_in_official_text | moved_placeholder | 제4조(과태료 부과기준) is where 제5조 moved to (live provision); the official article holds only '<개정 2015.10.30.>' and the move note, its text is probably in an attached table (별표) -> not a placeholder (CoS 2026-10-17) | `12e3a5f75adba018897658a161a9479f5c5bca614272932345aefdcebf624627` |

### Known gaps — batch 025

Article rows dropped at build time because the official law.go.kr HTML has no body for them (heading only, `empty_at_source`); other article ids keep their numbers.

| batch | article id | label | body_status | source HTML sha256 |
|---|---|---|---|---|
| 025 | None | 제18조(고충민원의 처리) | empty_at_source | `96e04599650da41e54147842a0011349ea1bb36c5f47f01bda8dae8f40a9d6e6` |

### Robots guard — batch 025

scrapers/batch_025/robots_guard.py (sha256 462bd696badc256c80deff1242bba53d29aab4b61507ea464bd4d1b9fb85c278, the code that ran for batch 025) differs from the shared fleet guard fa8823164631f53174a67a4b100f5278758b151c3e6a522d8c9987bb57753542 by exactly one line (line 77): the default robots state path is relative to the script dir (<script dir>/robots_state) instead of the fleet root; fetch/robots logic is identical.
