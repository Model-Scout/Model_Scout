---
license: unlicense
language:
- en
- ko
- ja
tags:
- music
---
<h1 align="center">Rdiffusion </h1>
<p align="center">
  <img src="rdiffusion.png" width="300"/>
</p>

We're releasing the **entire corpus** of publicly available songs from the [Riffusion](https://www.riffusion.com/) platform—generated and shared by their user community. Through extensive scraping of their exposed API, we’ve collected over **2,000 artificial songs**, including **every metadata field and downloadable asset** that was accessible at the time.

## 📦 Included Data

- **Audio & Visual Assets**:  
  `audio_url`, `audio_b64`, `image_url`, `image_b64`, `video_url`

- **Metadata & Structure**:  
  `id`, `title`, `author_id`, `created_at`, `duration_s`, `group_id`,  
  `parent_riff_id`, `remix_parent_id`, `audio_upload_id`, `image_id`, `video_id`

- **Model Info**:  
  `model_display_name`, `transform`, `sound`

- **Usage Flags**:  
  `allow_public_use`, `can_use`, `conditions`, `privacy`, `is_favorite`

- **Engagement Signals**:  
  `play_count`, `favorite_count`

- **Lyrics & Timing**:  
  `lyrics`, `lyrics_timestamped`

- **Miscellaneous**:  
  `audio_variation`, `image_override`, `simple_waveform`, `topic`

We’ve also **downloaded and organized all audio files** in a structured format, ready for direct use in training or research. [**Rdiffusion-audio**](https://huggingface.co/datasets/sleeping-ai/Rdiffusion-audio)

## ⚖️ Licensing & Usage

This dataset was scraped **legally under European research exemption laws**, intended strictly for **non-commercial research**. Any form of commercial use is **explicitly prohibited**. Our goal is simple: to build robust, transparent corpora for **training and evaluating text-to-music generative models**.

**Use it responsibly. Push the field forward. No bullshit.**