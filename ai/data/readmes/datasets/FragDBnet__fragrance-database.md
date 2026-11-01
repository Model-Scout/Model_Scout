---
license: cc-by-nc-4.0
task_categories:
  - feature-extraction
  - text-classification
language:
  - en
  - de
  - es
  - fr
  - cs
  - it
  - ru
  - pl
  - pt
  - el
  - zh
  - ja
  - nl
  - sr
  - ro
  - ar
  - uk
  - mn
  - ko
  - tr
  - sv
  - he
  - hu
tags:
  - fragrance
  - perfume
  - cosmetics
  - recommendation-system
  - e-commerce
  - retail
  - fragrantika
  - multilingual
size_categories:
  - n<1K
configs:
  - config_name: fragrances
    data_files: fragrances.csv
    default: true
    sep: "|"
  - config_name: brands
    data_files: brands.csv
    sep: "|"
  - config_name: perfumers
    data_files: perfumers.csv
    sep: "|"
  - config_name: notes
    data_files: notes.csv
    sep: "|"
  - config_name: accords
    data_files: accords.csv
    sep: "|"
  - config_name: translations
    data_files: translations.csv
    sep: "|"
dataset_info:
  - config_name: fragrances
    features:
      - name: pid
        dtype: int64
      - name: url
        dtype: string
      - name: brand
        dtype: string
      - name: name
        dtype: string
      - name: year
        dtype: int64
      - name: gender
        dtype: string
      - name: collection
        dtype: string
      - name: main_photo
        dtype: string
      - name: info_card
        dtype: string
      - name: user_photoes
        dtype: string
      - name: video_url
        dtype: string
      - name: accords
        dtype: string
      - name: notes_pyramid
        dtype: string
      - name: perfumers
        dtype: string
      - name: description
        dtype: string
      - name: rating
        dtype: string
      - name: reviews_count
        dtype: int64
      - name: appreciation
        dtype: string
      - name: price_value
        dtype: string
      - name: gender_votes
        dtype: string
      - name: longevity
        dtype: string
      - name: sillage
        dtype: string
      - name: season
        dtype: string
      - name: time_of_day
        dtype: string
      - name: pros_cons
        dtype: string
      - name: by_designer
        dtype: string
      - name: in_collection
        dtype: string
      - name: reminds_of
        dtype: string
      - name: also_like
        dtype: string
      - name: news_ids
        dtype: string
  - config_name: brands
    features:
      - name: id
        dtype: string
      - name: name
        dtype: string
      - name: url
        dtype: string
      - name: logo_url
        dtype: string
      - name: country
        dtype: string
      - name: main_activity
        dtype: string
      - name: website
        dtype: string
      - name: parent_company
        dtype: string
      - name: description
        dtype: string
      - name: brand_count
        dtype: int64
      - name: country_de
        dtype: string
      - name: country_es
        dtype: string
      - name: country_fr
        dtype: string
      - name: country_cs
        dtype: string
      - name: country_it
        dtype: string
      - name: country_ru
        dtype: string
      - name: country_pl
        dtype: string
      - name: country_pt
        dtype: string
      - name: country_el
        dtype: string
      - name: country_zh
        dtype: string
      - name: country_ja
        dtype: string
      - name: country_nl
        dtype: string
      - name: country_sr
        dtype: string
      - name: country_ro
        dtype: string
      - name: country_ar
        dtype: string
      - name: country_uk
        dtype: string
      - name: country_mn
        dtype: string
      - name: country_ko
        dtype: string
      - name: country_tr
        dtype: string
      - name: country_sv
        dtype: string
      - name: country_he
        dtype: string
      - name: country_hu
        dtype: string
      - name: main_activity_de
        dtype: string
      - name: main_activity_es
        dtype: string
      - name: main_activity_fr
        dtype: string
      - name: main_activity_cs
        dtype: string
      - name: main_activity_it
        dtype: string
      - name: main_activity_ru
        dtype: string
      - name: main_activity_pl
        dtype: string
      - name: main_activity_pt
        dtype: string
      - name: main_activity_el
        dtype: string
      - name: main_activity_zh
        dtype: string
      - name: main_activity_ja
        dtype: string
      - name: main_activity_nl
        dtype: string
      - name: main_activity_sr
        dtype: string
      - name: main_activity_ro
        dtype: string
      - name: main_activity_ar
        dtype: string
      - name: main_activity_uk
        dtype: string
      - name: main_activity_mn
        dtype: string
      - name: main_activity_ko
        dtype: string
      - name: main_activity_tr
        dtype: string
      - name: main_activity_sv
        dtype: string
      - name: main_activity_he
        dtype: string
      - name: main_activity_hu
        dtype: string
  - config_name: perfumers
    features:
      - name: id
        dtype: string
      - name: name
        dtype: string
      - name: url
        dtype: string
      - name: photo_url
        dtype: string
      - name: status
        dtype: string
      - name: company
        dtype: string
      - name: also_worked
        dtype: string
      - name: education
        dtype: string
      - name: web
        dtype: string
      - name: perfumes_count
        dtype: int64
      - name: biography
        dtype: string
      - name: status_de
        dtype: string
      - name: status_es
        dtype: string
      - name: status_fr
        dtype: string
      - name: status_cs
        dtype: string
      - name: status_it
        dtype: string
      - name: status_ru
        dtype: string
      - name: status_pl
        dtype: string
      - name: status_pt
        dtype: string
      - name: status_el
        dtype: string
      - name: status_zh
        dtype: string
      - name: status_ja
        dtype: string
      - name: status_nl
        dtype: string
      - name: status_sr
        dtype: string
      - name: status_ro
        dtype: string
      - name: status_ar
        dtype: string
      - name: status_uk
        dtype: string
      - name: status_mn
        dtype: string
      - name: status_ko
        dtype: string
      - name: status_tr
        dtype: string
      - name: status_sv
        dtype: string
      - name: status_he
        dtype: string
      - name: status_hu
        dtype: string
      - name: perfumer_name_ru
        dtype: string
      - name: perfumer_name_uk
        dtype: string
      - name: perfumer_name_ja
        dtype: string
      - name: perfumer_name_zh
        dtype: string
      - name: perfumer_name_ko
        dtype: string
      - name: perfumer_name_ar
        dtype: string
      - name: perfumer_name_he
        dtype: string
      - name: perfumer_name_el
        dtype: string
      - name: perfumer_name_mn
        dtype: string
  - config_name: notes
    features:
      - name: id
        dtype: string
      - name: name
        dtype: string
      - name: url
        dtype: string
      - name: latin_name
        dtype: string
      - name: other_names
        dtype: string
      - name: group
        dtype: string
      - name: odor_profile
        dtype: string
      - name: main_icon
        dtype: string
      - name: alt_icons
        dtype: string
      - name: background
        dtype: string
      - name: fragrance_count
        dtype: int64
      - name: note_name_de
        dtype: string
      - name: note_name_es
        dtype: string
      - name: note_name_fr
        dtype: string
      - name: note_name_cs
        dtype: string
      - name: note_name_it
        dtype: string
      - name: note_name_ru
        dtype: string
      - name: note_name_pl
        dtype: string
      - name: note_name_pt
        dtype: string
      - name: note_name_el
        dtype: string
      - name: note_name_zh
        dtype: string
      - name: note_name_ja
        dtype: string
      - name: note_name_nl
        dtype: string
      - name: note_name_sr
        dtype: string
      - name: note_name_ro
        dtype: string
      - name: note_name_ar
        dtype: string
      - name: note_name_uk
        dtype: string
      - name: note_name_mn
        dtype: string
      - name: note_name_ko
        dtype: string
      - name: note_name_tr
        dtype: string
      - name: note_name_sv
        dtype: string
      - name: note_name_he
        dtype: string
      - name: note_name_hu
        dtype: string
      - name: note_group_de
        dtype: string
      - name: note_group_es
        dtype: string
      - name: note_group_fr
        dtype: string
      - name: note_group_cs
        dtype: string
      - name: note_group_it
        dtype: string
      - name: note_group_ru
        dtype: string
      - name: note_group_pl
        dtype: string
      - name: note_group_pt
        dtype: string
      - name: note_group_el
        dtype: string
      - name: note_group_zh
        dtype: string
      - name: note_group_ja
        dtype: string
      - name: note_group_nl
        dtype: string
      - name: note_group_sr
        dtype: string
      - name: note_group_ro
        dtype: string
      - name: note_group_ar
        dtype: string
      - name: note_group_uk
        dtype: string
      - name: note_group_mn
        dtype: string
      - name: note_group_ko
        dtype: string
      - name: note_group_tr
        dtype: string
      - name: note_group_sv
        dtype: string
      - name: note_group_he
        dtype: string
      - name: note_group_hu
        dtype: string
  - config_name: accords
    features:
      - name: id
        dtype: string
      - name: name
        dtype: string
      - name: bar_color
        dtype: string
      - name: font_color
        dtype: string
      - name: fragrance_count
        dtype: int64
      - name: name_de
        dtype: string
      - name: name_es
        dtype: string
      - name: name_fr
        dtype: string
      - name: name_cs
        dtype: string
      - name: name_it
        dtype: string
      - name: name_ru
        dtype: string
      - name: name_pl
        dtype: string
      - name: name_pt
        dtype: string
      - name: name_el
        dtype: string
      - name: name_zh
        dtype: string
      - name: name_ja
        dtype: string
      - name: name_nl
        dtype: string
      - name: name_sr
        dtype: string
      - name: name_ro
        dtype: string
      - name: name_ar
        dtype: string
      - name: name_uk
        dtype: string
      - name: name_mn
        dtype: string
      - name: name_ko
        dtype: string
      - name: name_tr
        dtype: string
      - name: name_sv
        dtype: string
      - name: name_he
        dtype: string
      - name: name_hu
        dtype: string
  - config_name: translations
    features:
      - name: id
        dtype: string
      - name: section
        dtype: string
      - name: en
        dtype: string
      - name: de
        dtype: string
      - name: es
        dtype: string
      - name: fr
        dtype: string
      - name: cs
        dtype: string
      - name: it
        dtype: string
      - name: ru
        dtype: string
      - name: pl
        dtype: string
      - name: pt
        dtype: string
      - name: el
        dtype: string
      - name: zh
        dtype: string
      - name: ja
        dtype: string
      - name: nl
        dtype: string
      - name: sr
        dtype: string
      - name: ro
        dtype: string
      - name: ar
        dtype: string
      - name: uk
        dtype: string
      - name: mn
        dtype: string
      - name: ko
        dtype: string
      - name: tr
        dtype: string
      - name: sv
        dtype: string
      - name: he
        dtype: string
      - name: hu
        dtype: string
---

# FragDB v5.19 — Fragrance Database (Multilingual Sample)

The most comprehensive structured fragrance database available. This is a **free sample** of FragDB: **142,676 perfumes, 23 languages** — 10-row CSV samples at root.

Full dataset: [fragdb.net](https://fragdb.net).

## What's New in v5.19

- **Data updated** from v5.18 → v5.19 (snapshot 2026-10-19):
  - Fragrances: 141,541 → **142,676** (+1,135 added, none removed)
  - Brands: 8,384 → **8,433** (+49)
  - Perfumers: 3,154 → **3,171** (+17)
  - Notes: 2,615 → **2,618** rows in `notes.csv` (+3)
- **Incremental release** — the source was crawled for new pages on 2026-10-19 and the 1,135
  new fragrances were added; the existing 141,541 records are carried over unchanged from the
  2026-10-08 snapshot (v5.18).
- **Companion parquet refreshed** — user reviews 5,022,398 → **5,024,093** (+1,695, all
  English), editorial articles 25,780 → **25,875** (+95), news comments 278,905 → **279,843** (+938).
- Review coverage is 68.9% (98,240 of 142,676 perfumes): most of the new fragrances are recent
  launches without reviews yet.
- No brand renames or folded brand pages in this release; no perfume changed brand.
- The 23 articles that v5.18 shipped without a publication date are now dated; in v5.19,
  19 of the 23 newest articles (NID 26,363 and above) carry `date_unix = 0`.
- Sample files unchanged: the schema did not move between v5.18 and v5.19.

## What's New in v5.18

- **Data updated** from v5.17 → v5.18 (snapshot 2026-10-08):
  - Fragrances: 140,946 → **141,541** (+595: 601 added, 6 removed because their pages were
    deleted at the source — PIDs 122906, 123027, 134700, 138184, 138572, 142797)
  - Brands: 8,359 → **8,384** (+25)
  - Perfumers: 3,144 → **3,154** (+10)
  - Notes: 2,610 → **2,615** rows in `notes.csv` (+5)
- **Companion parquet refreshed** — user reviews 4,988,692 → **5,022,398** (+33,706, all
  English), editorial articles 25,709 → **25,780** (+71), news comments 277,446 → **278,905** (+1,459).
- **Brand ids now survive renames and merges at the source.** A renamed brand keeps its id and
  takes the new name (`b7118` Saleel → Saleel Parfums, `b4760` Aromatic Families → Aromatic).
  When the source folds one brand page into another, both ids stay and now carry the same name
  and page URL — five pairs this release, the largest `b532` (417 perfumes) with `b8330` (15),
  Novaya Zarya – The New Dawn. Joins on `brand_id` are unaffected; group by `id`, not by name,
  to keep each pair apart. Full list in the [CHANGELOG](https://github.com/FragDB/fragrance-database/blob/main/CHANGELOG.md).
- Two perfumes moved to another brand because the source moved them: PID 115180
  (Maison Incens → Rocco d'Orazio) and PID 141384 (Opula Perfumes → Opal Perfumes).
- The 84 articles that v5.17 shipped without a publication date are now dated; in v5.18,
  23 of the 29 newest articles (NID 26,262 and above) carry `date_unix = 0`.
- Sample files unchanged: the schema did not move between v5.17 and v5.18.

## What's New in v5.17

- **Data updated** from v5.16 → v5.17 (snapshot 2026-09-30):
  - Fragrances: 140,230 → **140,946** (+716)
  - Brands: 8,316 → **8,359** (+43)
  - Perfumers: 3,126 → **3,144** (+18)
  - Notes: 2,606 → **2,610** rows in `notes.csv` (+4)
- **Companion parquet refreshed** — user reviews 4,986,774 → **4,988,692** (+1,918),
  editorial articles 25,619 → **25,709** (+90), news comments 276,483 → **277,446** (+963).
- Figures on this page and in `SPEC.md` are measured against the v5.17 files. Several had
  been left behind by earlier releases — the snapshot dates, the category split, the PID
  references, the archived share and the reply rate here, and most of `SPEC.md`, which still
  described the May 2026 snapshot. All of them are now restated.
- Correction: 84 of the 250 newest articles (NID 25,970 and above) carry `date_unix = 0`;
  earlier text said every non-archived article is dated.
- Sample files unchanged: the schema did not move between v5.16 and v5.17.

## What's New in v5.16

- **Data updated** from v5.15 → v5.16 (snapshot 2026-09-19):
  - Fragrances: 139,501 → **140,230** (+729)
  - Brands: 8,272 → **8,316** (+44)
  - Perfumers: 3,116 → **3,126** (+10)
  - Notes: 2,596 → **2,606** rows in `notes.csv` (+10)
- **Companion parquet refreshed for the first time since June** — user reviews
  4,643,851 → **4,986,774** (+342,923), editorial articles 24,440 → **25,619** (+1,179),
  news comments 263,798 → **276,483** (+12,685).
- **New: a Data API** — per-record HTTP access to the same catalogue, priced per record.
  See the section below.
- Derived figures re-measured against the new files: review coverage 66.9% → **69.8%**,
  English share 1.69M → **1.88M**, reply rate 4.9% → **5.5%**.
- Sample files unchanged: the schema did not move between v5.15 and v5.16.

## What's New in v5.15

- **Data updated** from v5.14 → v5.15 (full source recrawl, parser run 260910):
  - Fragrances: 137,789 → **139,501** (+1,712)
  - Brands: 8,247 → **8,272** (+25)
  - Perfumers: 3,110 → **3,116** (+6)
  - Notes: 2,592 → **2,596** rows in `notes.csv` (+7 new, 3 retired)
- **Three note IDs retired** — the source merged case duplicates: `n473` → `n2661` (Heather),
  `n653` → `n2646` (Icing Pink), `n813` → `n2660` (Hazelnut Cocoa Spread). No fragrance
  references the retired IDs.
- **Figures on this card restated from the release files.** The notes figure is now the row
  count of `notes.csv`, the number fragdb.net shows; the full-database totals had stayed at
  v5.10. Review coverage and foreign-key figures are measured against this catalogue.
- **Reviews, news and news comments** — the same parquet files as v5.14.
- **Sample files unchanged** — the schema is identical to v5.14, so the 10-row CSVs were not
  rebuilt. A sample shows structure, not freshness.

## What's New in v5.14

- **Data updated** from v5.13 → v5.14 (incremental delta, parser run 260901):
  - Fragrances: 137,147 → **137,789** (+642)
  - Brands: 8,210 → **8,247** (+37)
  - Perfumers: 3,102 → **3,110** (+8)
  - Unique note names: **2,586** (unchanged — the notes reference only moves on a full crawl)
- **Sample files unchanged** — the schema is identical to v5.13, so the 10-row CSVs were not
  rebuilt. A sample shows structure, not freshness.

## What's New in v5.13

- **Data updated** from v5.12 → v5.13 (incremental delta, parser run 260819):
  - Fragrances: 136,682 → **137,147** (+465)
  - Brands: 8,175 → **8,210** (+35)
  - Perfumers: 3,090 → **3,102** (+12)
  - Notes: 2,586 → **2,588** (+2) — including `Kiwano`, which arrived with all 22 translations in its first cycle
- **Clean delta**: no perfume changed its canonical URL and none disappeared; field coverage flat across all 30 columns (max movement 0.22 pp)
- **Free sample refreshed** — 10-record CSV samples rebuilt from v5.13 data

## What's New in v5.12

- **Data updated** from v5.10 → v5.12 (full source recrawl, parser run 260809):
  - Fragrances: 135,308 → **136,682** (+1,374)
  - Brands: 8,093 → **8,175** (+82)
  - Perfumers: 3,057 → **3,090** (+33)
  - Notes: 2,573 → **2,586** (+13) — 100% multilingual, verified per language
- **784 records restored** — a resume-scan defect had frozen them since May; their votes, ratings and note pyramids are current again
- **Free sample refreshed** — 10-record CSV samples rebuilt from v5.12 data

## What's New in v5.9

- **Data updated** from v5.8 → v5.9 (parser run 260710):
  - Fragrances: 134,022 → **134,577** (+555)
  - Brands: 8,000 → **8,036** (+36) — **154 brand names canonicalized** (restored `Fragrance(s)` suffix; IDs stable)
  - Perfumers: 3,035 → **3,046** (+11)
  - Notes: 2,562 → **2,567** (+5)
  - URL hygiene: pyramid anchors single-domain, photo cache-busters stripped
- **Free sample refreshed** — 10-record CSV samples rebuilt from v5.9 data

## What's New in v5.8

- **Data updated** from v5.7 → v5.8 (parser run 260701):
  - Fragrances: 133,392 → **134,022** (+630)
  - Brands: 7,953 → **8,000** (+47)
  - Perfumers: 3,020 → **3,035** (+15)
  - Notes: 2,559 → **2,562** (+3)

## What's New in v5.7

- **Data updated** from v5.6 → v5.7 (parser run 260619):
  - Fragrances: 132,858 → **133,392** (+534)
  - Brands: 7,927 → **7,953** (+26)
  - Perfumers: 3,005 → **3,020** (+15)
  - Notes: 2,550 → **2,559** (+9)

## What's New in v5.6

- **Data updated** from v5.5 → v5.6 (parser run 260609):
  - Fragrances: 132,124 → **132,858** (+734)
  - Brands: 7,881 → **7,927** (+46)
  - Perfumers: 2,988 → **3,005** (+17)
  - Notes: 2,533 → **2,550** (+17)
- **Notes multilingual 100% coverage** (was 99.8%) — 6 previously gap-filled notes now complete across all 22 languages
- **Photo URL stability** — source cache-buster query params stripped, eliminating phantom diffs across releases
- Schema unchanged from v5.5 — existing loaders work without modification
- Free sample files unchanged (10-record structure preserved)

## What's New in v5.5

- **Data updated** from v5.4 → v5.5 (parser run 260601):
  - Fragrances: 130,949 → 132,124 (+1,175)
  - Brands: 7,815 → 7,881 (+66)
  - Perfumers: 2,968 → 2,988 (+20)
  - Notes: 2,522 → 2,533 (+11)

### Schema unchanged from v5.4

All F column counts identical (30/54/42/55/27/25) — existing scripts work without modification.

### From v5.4 (unchanged in v5.5)
- **23 languages** — all labels, note names, accords, countries, statuses translated
- **9 non-Latin scripts** for perfumer name transliteration
- **translations.csv** — vocabulary file (34 entries) for gender and voting labels
- **Compact notes pyramid** — `note_id,opacity,weight` (name/icon via notes.csv JOIN)
- Each note name variant has its own ID with translations
- **Gender & voting fields** use translation IDs for multilingual support

## Snapshot freshness

- **Data refreshed**: 2026-10-19 (v5.19) — an incremental update: the 1,135 fragrances new at the source were added on 2026-10-19; the existing records are as captured on 2026-10-08 (v5.18)
- **Reviews, news, news comments** (parquet): refreshed in this release — latest review 2026-10-18, latest article 2026-10-16, latest news comment 2026-10-19

## Data API — per-record access

**The whole catalogue, one record at a time.** A metered HTTP API over the same database we
sell as files. You pay per record returned, at the level of detail you ask for. No
subscription and no seats: top up a balance, fetch what your application needs, cache it as
long as you like.

**[fragdb.net/api →](https://fragdb.net/api)** · [OpenAPI spec](https://fragdb.net/api/v1/openapi) · [Sign up](https://fragdb.net/register) · [FAQ](https://fragdb.net/faq) · [Terms](https://fragdb.net/legal#api-access)

### Endpoints

```
GET  /api/v1/fragrances/{id}        one record
GET  /api/v1/brands/{id}            one brand
GET  /api/v1/notes/{id}             one note
GET  /api/v1/perfumers/{id}         one perfumer
POST /api/v1/{collection}/batch     up to 100 ids in one call
GET  /api/v1/index                  the full index, gzipped JSONL
GET  /api/v1/release                current release label and date — free
GET  /api/v1/account                balance, limits, usage — free
```

Detail level is chosen with `?level=list|basic|full`.

**There are no list endpoints.** `/api/v1/fragrances?limit=50` answers 404, by design. You
enumerate the catalogue with the index file — id, name, brand, year and change status — search
it on your side, and fetch whole records only for the hits you need. The index costs no units
and needs a paid key: five downloads a day, and an unchanged index answers 304.

### Detail levels

| Level | Units | Per record | What comes back |
|-------|------:|-----------:|-----------------|
| `list`  | 1 | $0.0025 | id, brand, name, year, gender, rating with vote count, and a thumbnail |
| `basic` | 2 | $0.005  | plus the photo, the collection, review count, main accords with their strength and the credited perfumers |
| `full`  | 4 | $0.01   | the note pyramid as published, seven vote blocks, description, pros and cons, related fragrances, and every label translated inline |

1 unit = $0.0025. Top-ups are multiples of $50, from $100 up to $5,000 — $100 buys 40,000
units. Paid units do not expire while the account is open. Minimum spend is $100 (40,000
units) per 180 days, $16.67 a month, counted from the first top-up. Payment in BTC, ETH, TRX,
XMR or USDT.

### Try it before you pay

Sign up and a free test key appears straight away. It costs nothing, charges nothing and
serves 5 sample records at every level — enough to write your parser against the real shape
of a response before you pay for anything.

```bash
curl -H "Authorization: Bearer <your test key>" \
  "https://fragdb.net/api/v1/fragrances/f_9kwkhn9yqx?level=full"
```

That id is one of the five public samples, so the call works on a test key.

Already bought a database file? You get 500 units for 30 days to try the API. (The 500 units
come with a file purchase, not with signing up.)

### Limits

10 requests per second and 300 per minute on a key · 20 per second on an account · 100 ids per
batch call · 50,000 charged records per account per UTC day · 5 index downloads per day · 5
keys per account. Call the API from your server, never from a browser.

### How it sits next to the files

The API serves the same catalogue that is sold as files, refreshed about three times a month.
Every response carries the release label and its date, and `GET /api/v1/release` tells you
which release you are on.

Ids are permanent: a record withdrawn at its source stays available with its last known
content and a status flag.

Reviews, news articles and community comments are **not** in the API — those stay in the
downloadable files described in this dataset card.

## Dataset Description

| File | Records | Fields | Description |
|------|---------|--------|-------------|
| `fragrances.csv` | 10 | 30 | Iconic fragrances (v5.9) |
| `brands.csv` | 10 | 54 | Brand profiles + 22 lang translations |
| `perfumers.csv` | 10 | 42 | Perfumer profiles + 22 lang + 9 name translit |
| `notes.csv` | 10 | 55 | Fragrance notes + 22 lang translations |
| `accords.csv` | 10 | 27 | Accords + 22 lang translations |
| `translations.csv` | 34 | 25 | Gender & voting vocabulary (full) |
| `comments_sample.parquet` | 25 | 8 | User reviews preview (parquet) |
| `news_sample.parquet` | 20 | 16 | Editorial articles preview (parquet) |
| `news_comments_sample.parquet` | 20 | 9 | News comments preview (parquet) |
| `SPEC.md` | — | — | Parquet schema documentation |

### Loading the data

```python
from datasets import load_dataset

f = load_dataset("FragDBnet/fragrance-database")           # fragrances (default)
brands = load_dataset("FragDBnet/fragrance-database", "brands")
notes  = load_dataset("FragDBnet/fragrance-database", "notes")
```

## Companion Parquet Datasets — User Reviews, News, and Community Comments

FragDB ships with **three Apache Parquet datasets** containing **5.3 million rows** of user-generated content and editorial coverage — the largest publicly-organized corpus of fragrance reviews and perfumery journalism. Use them for NLP, sentiment analysis, recommendation systems, market research, or training language models on fragrance-specific text.

**Keywords:** fragrance reviews · perfume reviews · multilingual UGC corpus · NLP training data · fragrance sentiment · perfumery journalism · perfume recommendation · scent recommendation · review classification · entity linking · knowledge graph · fragrance industry news · perfume articles

### `comments.parquet` — 5.0 Million User Reviews in 23 Languages

The world's largest collection of structured fragrance reviews. Every entry includes the perfume ID (joinable with `fragrances.csv`), author username, posting date, full review text, avatar URL, and language code.

- **5,024,093 user reviews** covering every major perfume in the database
- **23 languages** — English (1.91M), Russian, Portuguese, Spanish, Korean, Turkish, Japanese, Polish, Italian, Hungarian, Serbian, Swedish, German, Hebrew, Ukrainian, French, Arabic, Greek, Czech, Chinese, Romanian, Mongolian, Dutch
- **Coverage:** 68.9% of all fragrances have at least one review (98,240 of 142,676 PIDs)
- **Deterministic global primary key** — stable comment IDs survive re-scrapes
- **Zero duplicate rows**; every `pid` joins `fragrances.csv` except 62 reviews (0.001%) on 12 perfumes no longer in the catalogue
- **Independent UGC per language** — genuine localized content, not machine translation
- **8 fields:** `pid`, `lang`, `comment_id`, `author`, `date`, `text`, `avatar_url`, `gradient_class`
- **PyArrow large_string format** — combined corpus exceeds 32-bit string offset limit

**Use cases:** sentiment analysis · review classification · recommendation systems · perfume similarity from text · language detection benchmark · multilingual NLP training corpus · fragrance market research · author network analysis · trend detection by language

### `news.parquet` — 25,875 Editorial Articles (2008–2026)

Two decades of professional fragrance journalism. Every article includes title, author, full text (plain + HTML), category, related perfumes/brands/perfumers, publication date, and main image.

- **25,875 editorial articles** from 2008 to 2026 — complete public archive
- **30+ categories** — New Fragrances (33.9%), Fragrance Reviews (24.1%), Niche Perfumery (10.1%), Designer Brands, Interviews, History, Industry News
- **Bilingual storage** — `text` (plain) for NLP, `text_html` (markup preserved) for rich display
- **Linked entities** — `related_pids[]`, `related_brands[]`, `related_perfumers[]` as JSON arrays
- **127,137 PID references** — all but 176 (0.14%) resolve; those point to perfumes no longer in the catalogue
- **59.7% archived legacy, 40.3% modern** articles, all dated except 19 of the 23 newest (NID 26,363 and above)
- **16 fields:** `nid`, `title`, `category`, `author`, `url`, `is_archived`, `date_unix`, `description`, `text`, `text_html`, `main_image`, `article_images`, `related_pids`, `related_brands`, `related_perfumers`, `comments_count`

**Use cases:** content recommendation · article search engine · perfume knowledge graph · trend analysis · author influence study · entity linking · timeline analysis · industry research · niche perfumery research

### `news_comments.parquet` — 279,843 Threaded Community Comments

Community discussions attached to editorial articles, with threading support for replies. Joinable with `news.parquet` via `nid`.

- **279,843 threaded comments** across **23,117 articles** (89.3% of news articles have ≥1 comment)
- **5.6% reply rate** — threaded conversations with reply detection
- **100% populated timestamps**
- **9 fields:** `nid`, `comment_id`, `is_reply`, `author`, `date`, `date_unix`, `text`, `avatar_url`, `gradient`

**Use cases:** community engagement analysis · threaded discussion mining · reply network construction · comment sentiment · author activity profiles

### Tier Availability

The parquet datasets ship with **all paid tiers except the $200 Core**:

| Tier | CSV Core | Parquet Datasets |
|------|----------|------------------|
| **$200 One-Time Core** | ✅ | ❌ |
| **$400 One-Time Full Database** | ✅ | ✅ |
| **Annual Subscription** | ✅ | ✅ (always latest) |
| **Lifetime Access** | ✅ | ✅ (always latest) |

See https://fragdb.net/#pricing for complete tier comparison.

### Quick Start — Parquet

```python
import pyarrow.parquet as pq
import pandas as pd
import json

reviews = pq.read_table('comments.parquet').to_pandas()
fragrances = pd.read_csv('fragrances.csv', sep='|')
reviews_with_meta = reviews.merge(fragrances, on='pid', how='left')

news = pq.read_table('news.parquet').to_pandas()
news['related_pids_list'] = news['related_pids'].apply(json.loads)

news_comments = pq.read_table('news_comments.parquet').to_pandas()
```

Full schema in [`SPEC.md`](SPEC.md).

### Use Cases

**CSV Core (all tiers):**
- **E-commerce** — Enrich product listings with detailed fragrance data, notes, accords
- **Mobile Apps** — Build fragrance collection managers, scent discovery apps, perfume catalog apps
- **Data Analysis** — Analyze fragrance industry trends by brand, country, perfumer, year
- **Recommendations** — Content-based or collaborative filtering systems using accord/note vectors
- **Multilingual UIs** — Localized perfume catalogs in 23 languages out of the box
- **Knowledge Graphs** — Brand → Perfumer → Fragrance → Notes → Accords graph construction
- **Market Research** — Country-of-origin analysis, parent company portfolios, perfumer productivity stats

**Parquet Datasets ($400+ tiers):**
- **NLP & Sentiment Analysis** — Train models on 5.0M multilingual fragrance reviews
- **Recommender Systems** — Hybrid models combining CSV structure with review text similarity
- **Language Models** — Domain-specific corpus for fragrance/perfumery LLM fine-tuning
- **Review Classification** — Identify positive/negative reviews, fake review detection
- **Trend Detection** — News article timeline analysis, emerging fragrance trends
- **Author Networks** — Identify influential reviewers, perfumery journalists, community leaders
- **Content-Based Discovery** — "Articles about this perfume" — JOIN news.related_pids with fragrances.pid
- **Community Analytics** — Reply networks, engagement metrics on editorial content
- **Cross-Language Studies** — Compare review sentiment across 23 languages for the same fragrance
- **Search Engines** — Full-text search across reviews, articles, and structured metadata
- **Knowledge Extraction** — Mine 26K editorial articles for perfume facts, launch dates, perfumer interviews

### Full Database

| | Sample | Full Database |
|---|--------|---------------|
| Fragrances | 10 | **142,676** |
| Brands | 10 | **8,433** |
| Perfumers | 10 | **3,171** |
| Notes | 10 | **2,618** |
| Accords | 10 | **92** |
| Translations | 34 | **34** |
| Languages | 23 | **23** |
| **Total Records** | ~84 | **157,024** |

## Quick Start

> **The sample files are independent slices.** Each holds the top 10 rows of its own table, so
> an id taken from `fragrances.csv` usually has no matching row in this 10-row `brands.csv`.
> The snippet below is the join you run against the full database; on the sample it will return
> few rows or none, and that is the sample being small, not the data being broken.

```python
import pandas as pd

fragrances = pd.read_csv('fragrances.csv', sep='|')
brands = pd.read_csv('brands.csv', sep='|')
notes = pd.read_csv('notes.csv', sep='|')
translations = pd.read_csv('translations.csv', sep='|')

# Join and translate
fragrances['brand_id'] = fragrances['brand'].str.split(';').str[1]
df = fragrances.merge(brands, left_on='brand_id', right_on='id', suffixes=('', '_brand'))
trans = translations.set_index('id')
df['gender_ru'] = df['gender'].map(lambda x: trans.loc[x, 'ru'] if x in trans.index else x)
print(df[['name', 'name_brand', 'country_ru', 'gender_ru']])
```

## File Format

- **Format**: CSV (pipe `|` delimited)
- **Encoding**: UTF-8
- **Quote Character**: `"` (double quote)

## Links

- **Full Database**: [fragdb.net](https://fragdb.net)
- **GitHub**: [github.com/FragDB/fragrance-database](https://github.com/FragDB/fragrance-database)

## License

This sample is released under the **CC BY-NC 4.0 License**. Free for non-commercial use with attribution.

## Citation

```bibtex
@dataset{fragdb2026,
  title={FragDB Fragrance Database},
  author={FragDB},
  year={2026},
  version={5.18},
  url={https://fragdb.net},
  note={Multilingual dataset with 6 files, 23 languages}
}
```
