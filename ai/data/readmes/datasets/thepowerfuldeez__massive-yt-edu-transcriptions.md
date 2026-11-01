---
license: mit
task_categories:
  - automatic-speech-recognition
  - text-generation
language:
  - en
  - ru
  - de
  - fr
  - es
  - pt
  - ja
  - ko
  - zh
  - ar
  - hi
tags:
  - education
  - lectures
  - transcription
  - youtube
  - whisper
size_categories:
  - 10K<n<100K
---

# Massive YouTube Educational Transcriptions

Large-scale educational content transcribed from YouTube using distil-whisper/distil-large-v3.5.

## Stats

- **Videos**: 59,355
- **Characters**: 1,539,022,925 (~384M tokens)
- **Audio hours**: 35,890
- **Model**: faster-whisper (CTranslate2) with distil-large-v3.5
- **Hardware**: 2x RTX 5090 + 2x RTX 4090 at 165-185x realtime

## Fields

| Field | Description |
|-------|-------------|
| `video_id` | YouTube video ID |
| `title` | Video title |
| `text` | Full transcript |
| `duration_seconds` | Original audio duration (seconds) |
| `source` | Discovery source (channel/course/playlist) |
| `url` | YouTube URL |
| `priority` | Educational priority (9=university, 8=lecture, 7=documentary, 5=general) |
| `speed_ratio` | Transcription speed (realtime multiplier) |
| `content_category` | Content type (university_lecture, conference, individual_educator, etc.) |
| `license_risk` | License risk level (green/yellow/orange/red) |

## Content Categories

- **green**: CC-licensed or public domain (NPTEL, Khan Academy, MIT OCW, Yale OYC)
- **yellow**: Standard YouTube license, fair use for research
- **orange**: Commercial content, needs review
- **red**: Non-educational, excluded from transcription

## Methodology

1. **Discovery**: Channel crawling, related video walking, CC-focused search
2. **Quality filter**: 40+ reject categories, duration >= 15min, 3-tier priority scoring
3. **Transcription**: faster-whisper CTranslate2, 1.2x audio speedup, beam=1, no VAD
4. **Classification**: Channel name -> title regex -> priority fallback

## Code

[github.com/thepowerfuldeez/massive_yt_edu_scraper](https://github.com/thepowerfuldeez/massive_yt_edu_scraper)

## License

MIT
