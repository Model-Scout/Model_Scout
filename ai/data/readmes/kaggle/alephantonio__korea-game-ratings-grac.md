# Korea Game Ratings (GRAC / GCRB) 2007-2026

33,000+ official Korean game ratings with English labels: age, platform, genre

**Every official game rating decision published by Korea's Game Rating and Administration Committee (GRAC, 게임물관리위원회) Open API since 2007, in one clean CSV.**

Games distributed in South Korea need an age rating. GRAC and the Game Content Rating Board (GCRB, 게임콘텐츠등급분류위원회) publish their decisions in Korean only. This dataset compiles them into a single table with English column names and English labels for rating, platform, genre and content descriptors, while keeping every Korean value exactly as published.

> 📅 **Snapshot:** data as of **2026-10-05** (latest decisions: 2026-10-02). Updated monthly here.
> 🔄 **Need it daily, searchable, or via API?** The same data is refreshed every day on Apify: [Korea Game Rating Lookup](https://apify.com/antonio_aleph/korea-game-rating). AI agents can call it directly. For one-call checks across Korea, China and Taiwan, see [Asia Game License Check](https://apify.com/antonio_aleph/asia-game-license-check).

## What's inside

**33,558 rows**, 2007-04 – 2026-10.

| Rating (`rating_code`) | Korean | Rows |
|---|---|---|
| `ALL` | 전체이용가 | 15,818 |
| `12+` | 12세이용가 | 3,247 |
| `15+` | 15세이용가 | 1,714 |
| `18+` | 청소년이용불가 | 8,772 |
| `REFUSED` | 등급거부 (rating refused) | 3,312 |
| `REVOKED` | 등급취소 (rating revoked) | 685 |
| `REVOCATION_PENDING` | 등급취소예정 | 10 |

**Platforms:** Mobile 11,054 · PC/Online 7,480 · Arcade 6,072 · Console 4,159 · Online (legacy label) 1,480 · none (refused) 3,313

**Rating decisions per year:** 2009: 2,336 · 2010: 3,525 · 2011: 3,982 · 2012: 2,152 · 2013: 1,118 · 2015: 1,739 · 2017: 1,751 · 2019: 1,666 · 2021: 1,555 · 2022: 1,125 · 2023: 941 · 2024: 1,037 · 2025: 1,139 · 2026 (to Oct 2): 1,049

## ⚠️ Coverage: most mobile games are not here

Since the 2010s, most mobile games in Korea are rated through **self-classification** by app stores (Google Play and ONE store, via IARC) and never go to GRAC. That is why mobile decisions peak in 2010–2011 and then fall. PC, console and arcade games are well covered. Mobile games rated 18+ (청소년이용불가) still have to go through GRAC, so they appear here. **A missing game does not mean it is not released in Korea.**

## Columns

| Column | Description |
|---|---|
| `rated_date` | Decision date (YYYY-MM-DD) |
| `title_ko` | Game title as published (usually Korean, sometimes with the English name) |
| `company` | Applicant company as published |
| `rating_body` | `GRAC` or `GCRB` |
| `rating_code` | `ALL`, `12+`, `15+`, `18+`, `REFUSED`, `REVOKED`, `REVOCATION_PENDING` |
| `rating_ko` | Rating in Korean as published |
| `platform_en` / `platform_ko` | Mobile, PC/Online, Console, Arcade, Online (legacy) |
| `genre_en` / `genre_ko` | e.g. RPG, Action, FPS/TPS, Board (Betting), Puzzle, Casual |
| `content_descriptors_en` / `content_descriptors_ko` | Separated by `; ` — Sexual Content, Violence, Fear/Horror, Inappropriate Language, Drugs, Crime, Gambling |
| `rating_number` | Rating certificate number (e.g. `GC-CC-NP-261002-001`). Empty for refused ratings |
| `is_cancelled` / `cancelled_date` | Cancellation flag and date as published |
| `summary_ko` | Short content summary in Korean as published |

## Notes
- One row = one decision. A revoked game has two rows: the original rating and the later `REVOKED` row with its own date.
- `REFUSED` rows have no rating number, platform or genre in the source.
- English labels are our translations; the Korean original is always kept.

## License & attribution
- **Source:** Game Rating and Administration Committee (게임물관리위원회, GRAC) Open API, https://www.grac.or.kr/ , listed on the Korea Public Data Portal (https://www.data.go.kr/data/15120667) with no usage restrictions (commercial use allowed). Includes decisions by GCRB.
- The compilation, English column names and English labels in this dataset are released under **CC BY 4.0**. Please credit "Korea Game Ratings (GRAC) dataset by Aleph Antonio" and GRAC as the original source.
- This is an independent, **unofficial** dataset. It is not affiliated with or endorsed by GRAC, GCRB or the Government of the Republic of Korea. Always check critical decisions against the official website.

출처: Kaggle (alephantonio/korea-game-ratings-grac)
태그: video games, business, government, law, korea
라이선스: Other (specified in description)
수정일: 2026-10-05T05:58:09.017Z
