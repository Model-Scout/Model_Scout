---
license: cc-by-4.0
task_categories:
- text-classification
- image-classification
- video-classification
- audio-classification
language:
- en
- ar
- fr
- de
- es
- zh
- ja
- ko
- pt
- ru
- hi
- it
- nl
- pl
- sv
- tr
- vi
- fa
- uk
- he
- cs
- id
- th
- bn
- ur
size_categories:
- 1B<n<10B
tags:
- ai-detection
- deepfake-detection
- multi-modal
- multi-language
- synthetic-data
- human-content
pretty_name: DETECT-AI Multi-Modal AI Content Detection Dataset
dataset_info:
  version: 1.0.0
---

# 🔍 DETECT-AI — Multi-Modal AI Detection Dataset

**1B+ verified samples/month** scraped from 19 global sources across text, image, video,
and audio, labeled by a weighted ensemble of 8 specialized AI-detection models.

## 📁 Folder Structure

```
anas775/DETECT-AI-Dataset/
├── text/{lang}/part-{NNNN}.parquet
├── image/{lang}/metadata/part-{NNNN}.parquet
├── image/{lang}/frames/{image_id}.jpg
├── image/{lang}/faces/{image_id}_face_{NN}.jpg
├── video/{lang}/metadata/part-{NNNN}.parquet
├── video/{lang}/frames/{video_id}/full/frame_{NNNNN}.png
├── video/{lang}/frames/{video_id}/faces/face_{NNNNN}.jpg
├── video/{lang}/frames/{video_id}/textures/mask_{NNNNN}.png
├── audio/{lang}/metadata/part-{NNNN}.parquet
└── _metadata/
    ├── schema_v1.json
    ├── shard_registry.json
    └── push_log.jsonl
```

## 🏷️ Labels

| Label | Threshold | Meaning |
|---|---|---|
| `AI_GENERATED` | ≥ 0.75 | Synthetic / AI-created |
| `HUMAN` | ≤ 0.35 | Authentic human content |
| `UNCERTAIN` | 0.35–0.75 | Routed to human review |

## 🤖 Ensemble Models

| Modality | Models | Weights |
|---|---|---|
| Text | roberta-base-openai-detector · chatgpt-detector · ai-content-detector | 0.40/0.35/0.25 |
| Image | AI-image-detector · ViT-Deepfake · SDXL-detector | 0.40/0.35/0.25 |
| Audio | wav2vec2-deepfake · Resemblyzer | 0.60/0.40 |
| Video | Llama-3.2-11B-Vision · ViT fallback | primary/fallback |

## 📡 Data Sources (19)

**Text:** BBC · Reuters · Al Jazeera · arXiv · Wikipedia · NewsAPI · PapersWithCode · StackExchange · Reddit · WorldBank

**Image:** Unsplash · Pexels · Pixabay · Flickr CC · Wikimedia Commons

**Video:** YouTube (CC) · TED Talks · Pexels Video · VoxCeleb/AVA

## ⚡ Pipeline Architecture

```
Cloudflare Workers (cron */5 min) → scrape → Supabase staging
GitHub Actions   (cron */2 min)  → AI labeler → Supabase processed → Parquet shards here
GitHub Actions   (cron */5 min)  → frame/face extractor → frames here
```

## 📊 Parquet Schema

| Field | Type |
|---|---|
| sample_id | UUID |
| source_id | string |
| source_url | string |
| content_type | text/image/video/audio |
| language | ISO-639-1 |
| raw_content | string / storage path |
| label | AI_GENERATED/HUMAN/UNCERTAIN |
| final_confidence | float 0–1 |
| model_scores | JSON |
| verified | bool |
| scraped_at | ISO-8601 |
| labeled_at | ISO-8601 |

## 📜 License
CC-BY-4.0 — free for research and commercial use with attribution.
