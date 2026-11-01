# Top 1000 Most Viewed YouTube Videos (2026)

Includes views, likes, language, content type, and Shorts classification

# About Dataset

## Context
This dataset ranks the top 1000 most viewed YouTube videos of all time, as of April 2026. It covers everything from music videos and kids content to YouTube Shorts and promotional material, giving a broad picture of what dominates attention on the platform.

## Content
Each row represents one video with the following columns:

| Column             | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| rank             | Position on the list (1 to 1000) based on total views                      |
| title            | Video title as it appears on YouTube                                       |
| title_length     | Character count of the title                                               |
| detected_language| Language identified from the title text (English, Hindi, Korean, etc.)     |
| content_type     | Category (Music Video, Kids/Educational, Short, Ad/Promo, etc.)            |
| is_short         | Whether the video is a YouTube Short (1 = yes, 0 = no)                     |
| has_hashtags     | Whether the title contains hashtags (1 = yes, 0 = no)                      |
| views            | Total view count (e.g. 16.8B = 16.8 billion)                               |
| likes            | Total like count (e.g. 46.4M = 46.4 million)                               |

## Key Highlights
- *Baby Shark Dance* holds the #1 spot with 16.8 billion views, nearly double *Despacito* at 8.97B  
- Music videos dominate, followed by kids/educational content  
- YouTube Shorts appear in the top 1000, showing rising short-form impact  
- Titles span over 9 languages, with English most common  
- Views and likes are stored in abbreviated formats (B, M, K)  

## Potential Use Cases
- Analyze distribution of views and engagement  
- Compare Shorts vs regular videos performance  
- Identify dominant content types and languages  
- Study ranking decay from #1 to #1000  
- Build classifiers using title features

출처: Kaggle (mubashirsidiki/most-watched-yt-videos-rankings-2026)
태그: arts and entertainment, exploratory data analysis, data analytics, tabular
라이선스: Apache 2.0
수정일: 2026-04-02T12:27:35.743Z
