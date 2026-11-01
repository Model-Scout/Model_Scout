# Twitter Trending Hashtags

Trending hashtags on Twitter/X from 2020 to 2025

# Twitter/X Trending Hashtags (2020-2025)

A comprehensive dataset of trending hashtags on Twitter/X from 2020 to 2025, containing 12,036 unique trend entries across six years, capturing major world events, cultural moments, and viral phenomena.

## 📊 Dataset Description

This dataset captures trending hashtags from Twitter/X (formerly Twitter) by analyzing Wayback Machine snapshots of trends24.in, providing insights into breaking news, viral content, cultural moments, and global events from 2020 to 2025.

**Data Source**: Wayback Machine snapshots of x.com trending data. 

### Dataset Structure

```csv
tag,year,peak_date,tweets,rank
Kanye,2025,2025-02-08,67000000,1
Happy New Year,2025,2025-01-01,54000000,2
Trump,2025,2025-01-08,40000000,3
```

**Columns**:
- `tag` (string): The hashtag or topic name (# symbol removed)
- `year` (integer): The year the trend peaked (2020-2025)
- `peak_date` (date): The specific date when the trend reached maximum tweets (YYYY-MM-DD)
- `tweets` (integer): Peak number of tweets for this trend
- `rank` (integer): Rank within that year based on tweet count (1 = highest)

### Dataset Statistics

- **Total Entries**: 12,036 trends
- **Years Covered**: 2020-2025 (6 years)
- **Languages**: 10+ (English, Spanish, Arabic, Thai, Portuguese, Chinese, Russian, Korean, Japanese, and more)
- **Categories**: Politics, News, Sports, Entertainment, Holidays, Cultural Events, Technology, Social Movements

**Breakdown by Year**:
- **2025**: 813 trends (latest data, incomplete year)
- **2024**: 1,240 trends
- **2023**: 2,449 trends (most comprehensive)
- **2022**: 2,474 trends (most comprehensive)
- **2021**: 2,339 trends
- **2020**: 2,721 trends (most comprehensive)

## 🔍 Key Insights

### All-Time Top Trending Topics

| Rank | Topic | Year | Tweets | Date | Event |
|------|-------|------|--------|------|-------|
| 1 | Kobe | 2020 | 9.4M | Jan 27, 2020 | Death of Kobe Bryant |
| 2 | Trump | 2020 | 8.6M | Sep 30, 2020 | Presidential debate |
| 3 | เยาวชนปลดแอก | 2020 | 8.0M | Jul 18, 2020 | Thailand youth protests |
| 4 | PawanKalyanBirthdayCDP | 2020 | 7.6M | Aug 15, 2020 | Indian celebrity birthday |
| 5 | Kanye | 2025 | 67.0M | Feb 8, 2025 | Antisemitic controversy |
| 6 | ขีดเส้นตายไล่เผด็จการ | 2020 | 6.8M | Aug 16, 2020 | Thailand political protests |

### Top Trending by Year

| Year | #1 Topic | Tweets | Event |
|------|----------|--------|-------|
| 2025 | Kanye | 67M | Antisemitic posting spree |
| 2024 | MetGala | 3.6M | Met Gala fashion event |
| 2023 | Trump | 4.0M | Indictment news |
| 2022 | Christmas | 3.7M | Holiday celebration |
| 2021 | BTS BTS BTS | 5.4M | BTS fan engagement |
| 2020 | Kobe | 9.4M | Kobe Bryant death |

### Major Event Categories

**Politics & Elections**:
- **2025**: Trump (40M), USAID (38M), Zelensky (32M), Venezuela (22M)
- **2024**: Trump (3.6M), Biden (2.9M presidential debate)
- **2020-2021**: Massive political engagement during US elections and global protests

**Global Crises & News**:
- **COVID-19**: COVID (4.3M in 2020)
- **Ukraine Conflict**: Ukraine (3.0M in 2022), Zelensky (32M in 2025)
- **Middle East**: Israel (3.9M in 2023), Gaza (26M in 2025), Iran (33M in 2025)
- **Tragedies**: Kobe Bryant (9.4M), Charlie Kirk assassination (38M in 2025)

**Social Movements**:
- **Thailand Protests**: Multiple hashtags with 3M+ tweets (2020-2021)
- **SARSMUSTEND**: 3.1M tweets (Nigeria police brutality protests, 2020)

**Technology**:
- **Spotify**: 3.9M (2021), 3.5M (2022) - Spotify Wrapped annually
- **WhatsApp**: 3.4M (2021) - Service outage
- **Threads**: 2.7M (2023) - Meta's Twitter competitor launch

### Important Limitations

1. **Sampling Bias**: Data is based on available Wayback Machine snapshots, not continuous monitoring
2. **Peak Date Accuracy**: Dates may vary ±1 day due to:
   - Time zone differences in data collection
   - Multi-day trending events
   - Snapshot timing variations
3. **Tweet Count Accuracy**: Numbers represent peak values from snapshots, not cumulative totals
4. **Coverage Gaps**: Not all trending topics may be captured due to snapshot availability
5. **Incomplete 2025**: 2025 data is incomplete as the year is ongoing

출처: Kaggle (ronantakizawa/twitter-trending-hashtags)
태그: culture and humanities, popular culture, text mining, time series analysis, data storytelling
라이선스: MIT
수정일: 2025-12-01T06:06:58.353Z
