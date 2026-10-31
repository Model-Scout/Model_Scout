---
license: mit
task_categories:
  - automatic-speech-recognition
  - text-generation
language: [en, ru, de, fr, es, pt, ja, ko, zh, ar, hi]
tags: [education, lectures, youtube, queue, metadata, content-classification]
size_categories: [1M<n<10M]
---

# Massive YouTube Educational Video Queue

Full metadata and content classification for **4,489,228 YouTube educational videos** totaling **3,975,157 hours**.

## Description

This dataset contains metadata, content categorization, and license risk assessment for ~4.5M YouTube videos identified as potentially educational. It serves as the discovery and processing queue for the [massive-yt-edu-transcriptions](https://huggingface.co/datasets/thepowerfuldeez/massive-yt-edu-transcriptions) project, which aims to create the world's largest open educational transcript dataset.

Each video has been classified by content type and assessed for license risk using a 3-tier automated classification system.

## Collection Methodology

### Video Discovery

Videos were discovered through multiple strategies:

- **YouTube Search API** — Educational keyword queries across dozens of academic disciplines
- **Channel crawling** — Snowball discovery from known educational channels (universities, MOOCs, conference organizers)
- **Related video traversal** — Following YouTube's related video graph from known educational content
- **Playlist walking** — Extracting full playlists from educational channels and course pages
- **Quality filter** — Minimum 15 minutes duration, 40+ rejection categories to filter non-educational content

### Content Classification (3-tier system)

**Tier 1: Channel/Source Name Classification**
- 207,000+ YouTube channel and playlist names classified via pattern matching
- Patterns cover: universities (500+ institutions worldwide), conferences (100+ series), research institutes, government agencies, corporate talks, coaching/test prep, religious content, gaming/entertainment, medical/health, museums, tech communities
- Each source mapped to content category and license risk level

**Tier 2: Title-Based Classification**
- For videos without channel metadata, title analysis using regex patterns
- University detection (institution names, course codes, "Lecture N" patterns)
- Conference paper detection (conference names, "Keynote", year patterns)
- Educational keyword detection (tutorials, courses, crash courses)
- Entertainment/gaming detection for exclusion
- Medical/health content detection
- Religious content detection
- Multi-language support (English, Hindi, Russian, Chinese, Japanese, Korean, Arabic)

**Tier 3: Priority-Based Fallback**
- Videos with educational priority scores (P8-P9) from discovery classified as `unclassified_educational`
- Remaining unclassifiable content marked as `unknown` with fair-use-assumed yellow risk

### License Risk Assessment

Four risk levels based on content source analysis:

- 🟢 **green**: Known Creative Commons or public domain license
  - MIT OCW (CC-BY-NC-SA 4.0), Yale OYC (CC-BY-NC-SA), Khan Academy (CC-BY-NC-SA)
  - NPTEL/IIT (CC-BY-SA 4.0), Taiwan OCW (CC-BY-NC-SA)
  - Library of Congress (public domain), NASA, government agencies

- 🟡 **yellow**: Educational/factual content with strong fair use argument
  - University lectures (factual educational content)
  - Conference talks (meant for public dissemination)
  - Tech talks and corporate presentations
  - Individual educator tutorials
  - Coaching/test prep material

- 🟠 **orange**: Uncertain, needs individual review
  - Religious content (may be educational but different use case)
  - Non-English content where license couldn't be verified
  - Mixed educational/entertainment channels

- 🔴 **red**: Non-educational or high-risk content (EXCLUDED from processing queue)
  - Gaming content, entertainment, reactions, drama
  - Music performances, concerts
  - News broadcasts
  - Content clearly not educational

### Fair Use Framework

Our transcription project relies on fair use analysis under 17 U.S.C. § 107:

1. **Purpose and character of use** — Highly transformative: converting audio/video to text for machine learning training and research. The output (text transcripts) serves a fundamentally different purpose than the original (video lectures).
2. **Nature of the copyrighted work** — Factual/educational content strongly favors fair use. Lectures, tutorials, and conference talks are factual works presenting knowledge.
3. **Amount used** — Full transcription of audio (weighs against fair use), though only the audio track is used, not video.
4. **Effect on market** — Text transcripts do not substitute for video content. No one watches a lecture by reading its transcript. The transcript cannot replace the educational experience of the video.

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `video_id` | string | YouTube video ID (11 characters) |
| `title` | string | Video title as listed on YouTube |
| `url` | string | Full YouTube URL |
| `duration_seconds` | int | Video duration in seconds (0 if unknown) |
| `status` | string | Processing status: pending, completed, rejected, error |
| `priority` | int | Educational priority score (9=university OCW, 8=lecture, 7=documentary, 5=default) |
| `source` | string | Channel name, university, or course identifier |
| `content_category` | string | Content classification category (see below) |
| `license_risk` | string | License risk level: green, yellow, orange, or red |

## Statistics

**Total: 4,489,228 videos · 3,975,157 hours**

### Content Categories

| Category | Count | Hours | % of Total |
|----------|------:|------:|---:|
| `unknown` | 1,249,993 | 1,088,480 | 27.8% |
| `coaching_test_prep` | 829,883 | 738,964 | 18.5% |
| `university_lecture` | 688,191 | 584,300 | 15.3% |
| `individual_educator` | 634,423 | 611,780 | 14.1% |
| `unclassified_educational` | 371,400 | 300,047 | 8.3% |
| `non_english_edu` | 183,846 | 182,170 | 4.1% |
| `conference` | 122,628 | 125,967 | 2.7% |
| `gaming_entertainment` | 65,793 | 47,052 | 1.5% |
| `religious` | 59,033 | 67,811 | 1.3% |
| `corporate_talks` | 56,065 | 41,388 | 1.2% |
| `university_ocw` | 43,335 | 27,354 | 1.0% |
| `tech_community` | 33,379 | 44,644 | 0.7% |
| `individual_creator` | 33,078 | 12,283 | 0.7% |
| `medical_health` | 30,656 | 22,809 | 0.7% |
| `research_institute` | 23,325 | 24,050 | 0.5% |
| `government_public` | 21,521 | 21,601 | 0.5% |
| `museum_cultural` | 14,169 | 14,785 | 0.3% |
| `news_media` | 14,111 | 13,259 | 0.3% |
| `mooc_platform` | 10,480 | 2,049 | 0.2% |
| `public_media` | 3,565 | 4,046 | 0.1% |
| `null` | 432 | 377 | 0.0% |


### License Risk Distribution

| Risk | Count | Hours | % of Total |
|------|------:|------:|---:|
| 🟡 `yellow` | 4,035,222 | 3,589,818 | 89.9% |
| 🟠 `orange` | 319,678 | 284,616 | 7.1% |
| 🔴 `red` | 71,815 | 54,866 | 1.6% |
| 🟢 `green` | 62,159 | 45,538 | 1.4% |
| ⚪ `null` | 367 | 340 | 0.0% |


### Processing Status

| Status | Count |
|--------|------:|
| `pending` | 4,266,627 |
| `rejected` | 163,307 |
| `completed` | 57,949 |
| `error` | 1,175 |
| `timeout` | 102 |
| `processing` | 81 |


### Priority Distribution

| Priority | Count |
|----------|------:|
| P9 | 20,117 |
| P8 | 1,549,389 |
| P7 | 11,765 |
| P5 | 2,819,903 |
| P4 | 9 |
| P3 | 12 |
| P0 | 88,111 |


## Content Category Descriptions

| Category | Description |
|----------|-------------|
| `university_lecture` | Lectures from identified universities (MIT, Stanford, IITs, etc.) |
| `university_ocw` | Official OpenCourseWare with known CC licenses |
| `individual_educator` | Independent educators, tutorial creators, online teachers |
| `coaching_test_prep` | Test preparation (GATE, JEE, NEET, GRE, etc.) and exam coaching |
| `conference` | Academic and tech conference talks (NeurIPS, PyCon, etc.) |
| `corporate_talks` | Corporate tech talks, cloud platform tutorials |
| `tech_community` | Open source and developer community content |
| `research_institute` | Research seminars, colloquia, symposia |
| `medical_health` | Medical education, clinical lectures, health content |
| `non_english_edu` | Educational content in non-English languages |
| `mooc_platform` | MOOC platforms (Coursera, edX channel content) |
| `museum_cultural` | Museum lectures, cultural institution content |
| `government_public` | Government agencies, public institutions |
| `public_media` | Public media educational content |
| `religious` | Religious lectures, sermons, scripture study |
| `news_media` | News broadcasts, press conferences |
| `gaming_entertainment` | Gaming, entertainment (excluded from processing) |
| `individual_creator` | General content creators (needs review) |
| `unclassified_educational` | High-priority videos without clear category |
| `unknown` | Unclassified content, assumed educational |

## Related Datasets

- [massive-yt-edu-transcriptions](https://huggingface.co/datasets/thepowerfuldeez/massive-yt-edu-transcriptions) — Completed transcriptions from this queue

## Code

- [github.com/thepowerfuldeez/massive_yt_edu_scraper](https://github.com/thepowerfuldeez/massive_yt_edu_scraper) — Scraper and discovery
- [github.com/georgethedeveloper77/million-hour-transcription](https://github.com/georgethedeveloper77/million-hour-transcription) — Classification and transcription pipeline

## License

MIT — this metadata dataset. Individual video content has varying licenses as indicated by the `license_risk` field.
