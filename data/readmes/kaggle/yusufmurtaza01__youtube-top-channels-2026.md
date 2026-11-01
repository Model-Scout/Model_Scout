# Top YouTube Channels: Global & Country-Wise (2026)

Statistics for top ~4k global channels and top 100 channels across 30 countries.

## About Dataset

**Context**
YouTube's landscape is constantly shifting. This dataset provides a clean, up-to-date snapshot of the platform's most successful creators as of early 2026. It is designed to offer both a macro view of global giants and a localized perspective of what content dominates regional trending charts. 

**Methodology**
The data was extracted using the official YouTube Data API v3. To ensure an accurate representation of regional popularity—which standard API channel searches often fail to capture—the country-specific channels were discovered by aggregating the channels behind the top trending videos in each target region. 

**Content**
This dataset contains two primary types of data:
1.  **Global Data:** A consolidated list of the top ~4,000 YouTube channels worldwide, ranked by subscriber count. 
2.  **Country-Wise Data:** Specific lists of the top ~100 channels for 30 individual countries, based on regional trending metrics. 

**Potential Use Cases**
This dataset is well-suited for a variety of data science and machine learning tasks:
* **Exploratory Data Analysis (EDA):** Discovering engagement trends, view-to-subscriber ratios, and regional content preferences.
* **Natural Language Processing (NLP):** Analyzing channel descriptions to extract common keywords, topics, and multi-lingual content strategies used by top creators.
* **Clustering Models:** Grouping channels based on their performance metrics (e.g., high-volume uploaders vs. high-view-per-video creators).
* **Predictive Modeling:** Estimating potential view counts or subscriber milestones based on current trajectories.

---

## Country Code Mapping
For the regional files, the following two-letter ISO 3166-1 alpha-2 country codes are used:

* **AE:** United Arab Emirates
* **AR:** Argentina
* **AU:** Australia
* **BR:** Brazil
* **CA:** Canada
* **CH:** Switzerland
* **CO:** Colombia
* **DE:** Germany
* **EG:** Egypt
* **ES:** Spain
* **FR:** France
* **GB:** United Kingdom
* **ID:** Indonesia
* **IN:** India
* **IT:** Italy
* **JP:** Japan
* **KR:** South Korea
* **MX:** Mexico
* **NG:** Nigeria
* **NL:** Netherlands
* **PH:** Philippines
* **PK:** Pakistan
* **RU:** Russia
* **SA:** Saudi Arabia
* **SE:** Sweden
* **SG:** Singapore
* **TH:** Thailand
* **TR:** Turkey
* **US:** United States
* **VN:** Vietnam

---

### File Information

* `global_top4k.csv`: Contains the comprehensive list of the ~4,000 largest channels globally.
* `global_top2000.csv`: Contains the comprehensive list of the 2,000 largest channels globally.
* `[CountryCode]_top_channels.csv` (e.g., `IN_top_channels.csv`, `US_top_channels.csv`): Individual files containing the top ~100 channels for that specific region. *(Note: If you combined these into a single file, you can rename this bullet point to `channels_by_country.csv` and note that it contains the data for all 30 regions).*

---

### Column Descriptors
* **Global Rank:** The overall worldwide ranking of the channel based on its total subscriber count (integer).
* **Search Country:** *(Regional files only)* The geographic region where the channel's content was found trending on the YouTube charts (string).
* **Country Code:** *(Regional files only)* The two-letter ISO 3166-1 alpha-2 code corresponding to the Search Country (e.g., AE, IN, US) (string).
* **Country Rank:** *(Regional files only)* The channel's ranking (1-100) within this specific Search Country, sorted by subscribers (integer).
* **Channel ID:** The unique identifier assigned to the channel by YouTube (string).
* **Channel Name:** The display title of the YouTube channel (string).
* **Subscribers:** The total number of users subscribed to the channel (integer).
* **Total Views:** The cumulative number of views across all videos on the channel (integer).
* **Total Videos:** The total number of public videos uploaded by the channel (integer).
* **Country:** The geographic location the channel owner has set in their public YouTube "About" page. *Note: This may differ from the 'Search Country' if a creator is headquartered elsewhere but trending in that region* (string).
* **Description:** The text provided by the creator in the channel's "About" section (string).



### The Difference Between "Search Country" and "Country"
In your regional files, you will often see a discrepancy where `Search Country` says "India" but `Country` says "United States" (or "Unknown"). Here is exactly what that means:

* **Search Country & Country Code:** This is the geographic region where you *ran your API query*. It means the channel has a video that is currently **trending on the YouTube charts in that specific location**.
* **Country (Self-Reported):** This is the physical location the channel owner selected in their YouTube settings (visible on their "About" page). 

**Why they don't match:** A creator might live in the United States (`Country` = US), but their video went viral and hit the trending page in India (`Search Country` = India). If `Country` says "Unknown," it simply means the creator chose not to publicly list a location on their profile.

출처: Kaggle (yusufmurtaza01/youtube-top-channels-2026)
태그: beginner, exploratory data analysis, geospatial analysis, data analytics
라이선스: CC0: Public Domain
수정일: 2026-04-10T04:03:16.633Z
