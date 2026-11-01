# Manhwa Industry Evolution (2000-2026)

Comprehensive metadata, user scores, and plot summaries for South Korean webtoon

### Context
The South Korean Manhwa (webtoon) industry has transformed from a local niche into a global cultural phenomenon. This dataset provides a high-fidelity snapshot of the industry's evolution, capturing metadata for over 5,000 titles spanning nearly three decades.

### Content
This dataset was generated via the AniList GraphQL API (January 2026). It includes:
- **Temporal Data:** Release years and publishing status.
- **Engagement Metrics:** Popularity (follower counts) and average user scores.
- **Content Metadata:** Multi-label genres and chapter counts.
- **Text Data:** Professionally cleaned plot descriptions for NLP tasks.

### Column Metadata
- `id`: Unique AniList identifier.
- `title`: Primary English or Romaji title.
- `year`: The year the series began publication.
- `status`: Current status (RELEASING, FINISHED, etc.).
- `genres`: Comma-separated genre tags.
- `popularity`: Total number of users who have added the title to their list.
- `score`: Average user rating (0-100).
- `description`: Cleaned plot summary.

### Inspiration
- **Trend Analysis:** How has the dominance of the 'Action' genre shifted over time?
- **Recommendation Engines:** Can you build a system that recommends Manhwa based on plot similarity?
- **NLP:** Train a model to predict a Manhwa's genre based solely on its description.

### Acknowledgements
Data sourced ethically from the [AniList API](https://anilist.gitbook.io/anilist-apiv2-docs/).

출처: Kaggle (artheon/manhwa-industry-evolution-2000-2026)
태그: nlp, data visualization, tabular, comics and animation, anime and manga
라이선스: Community Data License Agreement - Sharing - Version 1.0
수정일: 2026-01-30T14:51:34.050Z
