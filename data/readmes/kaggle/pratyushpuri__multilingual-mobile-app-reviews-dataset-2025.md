# Multilingual Mobile App Review Dataset Sept 2025

2.5K reviews across 40+ apps, 24 languages, perfect for NLP & sentiment analysis

# Multilingual Mobile App Reviews Dataset 2025

## Overview
This comprehensive **synthetic** dataset contains **2,514 authentic mobile app reviews** spanning **40+ popular applications** across **24 different languages**, making it ideal for multilingual NLP, sentiment analysis, and cross-cultural user behavior research.

## Dataset Statistics
- **Total Records**: 2,514 reviews
- **Columns**: 15 features
- **Languages Covered**: 24 international languages
- **Apps Included**: 40+ popular mobile applications
- **Time Range**: 2023-2025 (2-year span)
- **File Format**: CSV
- **Data Quality**: Intentionally includes missing values and mixed data types for data cleaning practice

## Column Specifications

| Column Name | Data Type | Description | Sample Values | Null Count |
|-------------|-----------|-------------|---------------|------------|
| `review_id` | Integer | Unique identifier for each review | 1, 2, 3, ... | 0 |
| `user_id` | String* | User identifier (should be integer) | "1967825", "9242600" | 0 |
| `app_name` | String | Name of the mobile application | WhatsApp, Instagram, TikTok | 0 |
| `app_category` | String | Application category | Social Networking, Entertainment | 0 |
| `review_text` | String | Multilingual review content | "This app is amazing!" | 63 |
| `review_language` | String | ISO language code | en, es, fr, zh, hi, ar | 0 |
| `rating` | Mixed* | App rating (1.0-5.0, some as strings) | 4.5, "3.2", 1.1 | 38 |
| `review_date` | DateTime | Timestamp of review submission | 2024-10-09 19:26:40 | 0 |
| `verified_purchase` | Boolean | Purchase verification status | True, False | 0 |
| `device_type` | String | Device platform | Android, iOS, iPad, Windows Phone | 0 |
| `num_helpful_votes` | Mixed* | Helpfulness votes (some as strings) | 65, "209", 163 | 0 |
| `user_age` | Float* | User age (should be integer) | 14.0, 18.0, 67.0 | 0 |
| `user_country` | String | User's country | China, Germany, Nigeria | 50 |
| `user_gender` | String | User gender | Male, Female, Non-binary, Prefer not to say | 88 |
| `app_version` | String | Application version number | 1.4, v8.9, 2.8.37.5926 | 25 |

*Note: Data types marked with asterisk require cleaning/conversion*

## Language Distribution
The dataset includes reviews in **24 languages**:
- **European**: English (en), Spanish (es), French (fr), German (de), Italian (it), Russian (ru), Polish (pl), Dutch (nl), Swedish (sv), Danish (da), Norwegian (no), Finnish (fi)
- **Asian**: Chinese (zh), Hindi (hi), Japanese (ja), Korean (ko), Thai (th), Vietnamese (vi), Indonesian (id), Malay (ms)
- **Other**: Arabic (ar), Turkish (tr), Filipino (tl)

## Application Categories
Reviews cover **18 distinct categories**:
- Social Networking
- Entertainment  
- Productivity
- Travel & Local
- Music & Audio
- Video Players & Editors
- Shopping
- Navigation
- Finance
- Communication
- Education
- Photography
- Dating
- Business
- Utilities
- Health & Fitness
- Games
- News & Magazines

## Popular Apps Included
**40+ applications** including:
- **Social**: WhatsApp, Instagram, Facebook, Snapchat, TikTok, LinkedIn, Twitter, Reddit, Pinterest
- **Entertainment**: YouTube, Netflix, Spotify
- **Productivity**: Microsoft Office, Google Drive, Dropbox, OneDrive, Zoom, Discord
- **Travel**: Uber, Lyft, Airbnb, Booking.com, Google Maps, Waze
- **Finance**: PayPal, Venmo
- **Education**: Duolingo, Khan Academy, Coursera, Udemy
- **Tools**: Grammarly, Canva, Adobe Photoshop, VLC, MX Player

## Geographic Distribution
Reviews from **24 countries** across all continents:
- **Asia**: China, India, Japan, South Korea, Thailand, Vietnam, Indonesia, Malaysia, Philippines, Pakistan, Bangladesh
- **Europe**: Germany, United Kingdom, France, Italy, Spain, Russia, Turkey, Poland
- **Americas**: United States, Canada, Brazil, Mexico
- **Oceania**: Australia
- **Africa**: Nigeria

## Data Quality Features
**Intentional data challenges for learning**:
- **Missing Values**: Strategic nulls in review_text (63), rating (38), user_country (50), user_gender (88), app_version (25)
- **Data Type Issues**: 
  - user_id stored as strings (should be integers)
  - user_age as floats (should be integers)  
  - Some ratings as strings (should be floats)
  - Some helpful_votes as strings (should be integers)
- **Mixed Version Formats**: "1.4", "v8.9", "2.8.37.5926", "14.1.60.318-beta"

## Use Cases
This dataset is perfect for:
- **Multilingual NLP** projects and sentiment analysis
- **Cross-cultural** user behavior analysis
- **App store analytics** and rating prediction
- **Data cleaning** and preprocessing practice
- **Text classification** across multiple languages
- **Time series analysis** of app reviews
- **Geographic sentiment** analysis
- **Data engineering** pipeline development

## Data Cleaning Opportunities
- Convert string IDs to integers
- Standardize rating values to float
- Handle missing values appropriately
- Normalize app version formats
- Parse and validate datetime formats
- Categorize and encode categorical variables

This dataset provides an excellent foundation for data science portfolio projects, demonstrating skills in multilingual data processing, sentiment analysis, and cross-cultural analytics.

출처: Kaggle (pratyushpuri/multilingual-mobile-app-reviews-dataset-2025)
태그: arts and entertainment, education, linguistics, mobile and wireless, nlp, ratings and reviews
라이선스: Apache 2.0
수정일: 2025-07-31T03:09:08.217Z
