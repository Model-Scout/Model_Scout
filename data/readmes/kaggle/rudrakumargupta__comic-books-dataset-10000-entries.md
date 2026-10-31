# Comic Books Dataset (10,000 entries)

Global Manga, Manhwa, Marvel, DC & Indie Comics — 2000 to 2026

# Comic Books Dataset (10,000 Entries) — Global Comics 2000–2026

> The most comprehensive comic book dataset on Kaggle — covering Manga, Manhwa, Manhua, Marvel, DC, Image, Dark Horse, and European comics all in one place.

---

## Why This Dataset?

Comic books are one of the most culturally rich and globally diverse art forms — yet there is almost **no structured data** about them on Kaggle. This dataset was built to fill that gap.

Whether you are a data scientist, comic fan, researcher, or student — this dataset gives you **10,000 comic titles** from across the world, spanning **26 years** (2000–2026), with **17 carefully chosen columns** ready for analysis, visualization, and machine learning.

---

## Dataset at a Glance

| Property | Value |
|---|---|
| Total Entries | 10,000 comics |
| Time Period | 2000 – 2026 |
| Total Columns | 17 |
| File Size | ~2.13 MB |
| File Format | CSV (UTF-8) |
| License | CC0: Public Domain |

---

## Column Details

| Column | Description | Example |
|---|---|---|
| `comic_id` | Unique ID for each comic (CMC-00001 format) | CMC-00042 |
| `Title` | Official name of the comic / series | Attack on Titan |
| `Writer` | Lead writer / author | Hajime Isayama |
| `Artist` | Illustrator / inker (can differ from writer) | Hajime Isayama |
| `Studio/Publisher` | Company that published the comic | Kodansha (Kodansha USA) |
| `Release Year` | Year of first publication | 2009 |
| `Format` | How it was released | Tankobon / Single Issue / Webtoon / Graphic Novel |
| `Theme (Color Style)` | Visual art style of the comic | Black & White / Full Color / Full Color Digital |
| `Genre` | Primary genre classification | Action / Dark Fantasy |
| `Country of Origin` | Country where it was first published | Japan |
| `Page Count` | Total approximate page count | 5,988 |
| `Rating (out of 10)` | Aggregated reader score (MAL / Goodreads) | 9.7 |
| `Status` | Current publication status | Completed / Ongoing / Hiatus / Cancelled |
| `Language` | Original language of publication | Japanese |
| `Age Rating` | Target audience rating | Teen+ / Mature / All Ages |
| `Awards` | Notable awards won or nominated for | Kodansha Manga Award Winner |
| `Volume Count` | Total number of volumes / issues | 34 |

---

## Understanding Theme (Color Style)

This is one of the most unique columns in this dataset. It captures the **visual identity** of each comic — something no other dataset tracks.

| Theme | Meaning | Examples |
|---|---|---|
| **Black & White** | Traditional manga ink style | Attack on Titan, Berserk, Death Note |
| **Full Color** | Standard Western comic coloring | Marvel, DC, Image Comics |
| **Full Color (Digital)** | Vertical scroll webtoon coloring | Solo Leveling, Tower of God, Lore Olympus |
| **Full Color (Pastel)** | Soft pastel digital palette | Lore Olympus |
| **Full Color / Limited Palette** | Stylized restricted colors | Hawkeye (Matt Fraction run) |
| **Grayscale** | Between B&W and full color | Some indie and European comics |
| **Watercolor** | Hand-painted watercolor style | Descender / Ascender |

---

## Regional Coverage

| Region | Titles | Publishers Included |
|---|---|---|
| 🇯🇵 Japan (Manga) | ~3,575 | Shueisha, Kodansha, Square Enix, Kadokawa, Shogakukan, Hakusensha |
| 🇺🇸 USA | ~3,150 | Marvel, DC, DC Vertigo, DC Black Label, Image, Dark Horse, BOOM! Studios, IDW, Oni Press |
| 🇰🇷 South Korea (Manhwa/Webtoon) | ~897 | Naver / Line Webtoon, Kakao, Lezhin, Tapas Media |
| 🇨🇳 China (Manhua) | ~550 | Tencent Comics, Bilibili Comics, Kuaikan Comics |
| 🇫🇷🇪🇸🇩🇪 Europe | ~560 | Dargaud, Casterman, Dupuis, L'Association, Titan Comics (UK), 2000 AD |
| Others (UK, Canada, Australia, NZ) | ~268 | Various indie and international publishers |

---

## Dataset Statistics

| Metric | Value |
|---|---|
| Average Rating | 8.06 / 10 |
| Highest Rated | One Piece (9.9), Berserk (9.8), Saga (9.7) |
| Most Common Genre | Action / Fantasy |
| Most Common Format | Tankobon (Manga volume) |
| Completed Series | ~50% |
| Ongoing Series | ~38% |
| On Hiatus | ~7% |
| Cancelled | ~4% |
| Year with Most Releases | 2018–2022 |

---

## What Can You Do With This Dataset?

### Exploratory Data Analysis (EDA)
- Which country produces the highest rated comics?
- How has genre popularity changed from 2000 to 2026?
- What is the distribution of page counts across formats?
- Which publishers have the most award-winning titles?

### Machine Learning
- **Rating Prediction** — Predict a comic's rating from genre, publisher, format, and country
- **Status Classification** — Classify whether a comic is Ongoing, Completed, or Cancelled
- **Genre Classification** — Multi-label genre prediction from title and other features
- **NLP on Titles** — Cluster or classify comics based on title text

### Data Visualization
- Map of comic production by country
- Bubble chart of genre vs rating vs page count
- Timeline of comic releases by region
- Color style (Theme) distribution across cultures

---

## Notable Comics Included

| Title | Origin | Rating |
|---|---|---|
| One Piece | Japan 🇯🇵 | 9.9 |
| Berserk | Japan 🇯🇵 | 9.8 |
| Attack on Titan | Japan 🇯🇵 | 9.7 |
| Saga | USA 🇺🇸 | 9.7 |
| Vagabond | Japan 🇯🇵 | 9.7 |
| All-Star Superman | USA 🇺🇸 | 9.6 |
| Fullmetal Alchemist | Japan 🇯🇵 | 9.6 |
| Mister Miracle | USA 🇺🇸 | 9.5 |
| Chainsaw Man | Japan 🇯🇵 | 9.5 |
| Solo Leveling | South Korea 🇰🇷 | 9.4 |
| Blacksad | France/Spain 🇫🇷 | 9.3 |

---

## Files in This Dataset

| File | Description |
|---|---|
| `comic_books_10000_dataset.csv` | Main dataset with 10,000 comic entries and 17 columns |

---

## Notes & Limitations

- This dataset combines **real verified entries** (40+ famous titles with accurate data) with **synthetically generated entries** following realistic distributions — suitable for analysis, ML practice, and EDA projects
- Ratings are approximate aggregates inspired by MAL, Goodreads, and community scores
- Page counts are approximate totals across all volumes
- Some titles may have variant spellings due to translation differences
- Manhua and lesser-known indie titles may have limited real-world verification

---

## Inspiration

Built to fill a massive gap on Kaggle — there was almost no structured comic book data available, especially covering non-US traditions like Manga, Manhwa, and Manhua. This dataset brings the global comic world into one clean CSV file ready for analysis.

---

*If you find this dataset useful, please upvote ⬆️ — it helps others discover it!*

출처: Kaggle (rudrakumargupta/comic-books-dataset-10000-entries)
태그: popular culture, arts and entertainment, comics and animation, anime and manga, tabular classification
라이선스: CC0: Public Domain
수정일: 2026-03-04T05:25:26.253Z
