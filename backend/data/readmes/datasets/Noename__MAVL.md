---
license: cc-by-nc-4.0
license_link: LICENSE
task_categories:
- translation
- text-generation
- video-text-to-text
language:
- en
- es
- fr
- ko
- ja
tags:
- music
- art
- multimodal
- lyrics
- animation
pretty_name: MAVL
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: song_title
    dtype: string
  - name: lyrics
    list:
      list:
      - name: ES
        struct:
        - name: end
          dtype: float64
        - name: line_number
          dtype: int64
        - name: start
          dtype: float64
        - name: syllable_count
          dtype: int64
        - name: text
          sequence:
            sequence: string
      - name: FR
        struct:
        - name: end
          dtype: float64
        - name: line_number
          dtype: int64
        - name: start
          dtype: float64
        - name: syllable_count
          dtype: int64
        - name: text
          sequence:
            sequence: string
      - name: JP
        struct:
        - name: end
          dtype: float64
        - name: line_number
          dtype: int64
        - name: start
          dtype: float64
        - name: syllable_count
          dtype: int64
        - name: text
          sequence:
            sequence: string
      - name: KR
        struct:
        - name: end
          dtype: float64
        - name: line_number
          dtype: int64
        - name: start
          dtype: float64
        - name: syllable_count
          dtype: int64
        - name: text
          sequence:
            sequence: string
      - name: US_og
        struct:
        - name: end
          dtype: float64
        - name: line_number
          dtype: int64
        - name: start
          dtype: float64
        - name: syllable_count
          dtype: int64
        - name: text
          sequence:
            sequence: string
  - name: youtube_url
    struct:
    - name: ES
      dtype: string
    - name: FR
      dtype: string
    - name: JP
      dtype: string
    - name: KR
      dtype: string
    - name: US
      dtype: string
  - name: lyrics_url
    struct:
    - name: ES
      dtype: string
    - name: FR
      dtype: string
    - name: JP
      dtype: string
    - name: KR
      dtype: string
    - name: US
      dtype: string
  - name: video
    struct:
    - name: ES
      dtype: bool
    - name: FR
      dtype: bool
    - name: JP
      dtype: bool
    - name: KR
      dtype: bool
    - name: US
      dtype: bool
  splits:
  - name: train
    num_bytes: 2203287
    num_examples: 228
  download_size: 1002421
  dataset_size: 2203287
---
---

# MAVL: Multilingual Audio-Video Lyrics Dataset for Animated Song Translation

<div align="center">
  <img src="assets/mavl_logo.png" alt="MAVL Dataset Overview" width="200">
</div>

[![Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-MAVL-blue)](https://huggingface.co/datasets/Noename/MAVL)
[![GitHub Repository](https://img.shields.io/badge/GitHub-MAVL--Repo-181717?logo=github)](https://github.com/k1064190/MAVL)
[![arXiv](https://img.shields.io/badge/arXiv-2505.18614-b31b1b.svg)](https://arxiv.org/abs/2505.18614)

## Dataset Description
This dataset contains a collection of YouTube URLs corresponding to songs from animated musicals. It includes meticulously aligned lyrics (English, Spanish, French, Korean, and Japanese) with corresponding timestamps, song titles, and artist information. MAVL is designed as the first multilingual, multimodal benchmark for singable lyrics translation. **To complete the dataset by downloading lyrics, audio, and video, and for related processing scripts, please refer to our [GitHub Repository](https://github.com/k1064190/MAVL).**

**Crucially, this dataset does not contain the actual audio, video, or full lyric text files directly due to copyright considerations.** Instead, it provides structured metadata and URLs, along with a compact representation of lyrics (e.g., first letters of words, first/last words of lines) and their syllable counts, and precise timestamps. This allows for the reconstruction of original lyrics and the download of associated multimedia content via provided scripts.

## Dataset Structure

The dataset is provided in a JSON format. Each entry represents a song and contains:

  * **Song Title:** The name of the animated song.
  * **`lyrics`**: A nested structure containing lyric lines for each language (`US_og` for original English, `ES` for Spanish, `FR` for French, `KR` for Korean, `JP` for Japanese). Each line includes:
      * `text`: A compact representation of the original lyric line (e.g., `["Tsimp", "There's", "pants"]` for "Squirrels in my pants"). This is designed to allow for the reconstruction of the full lyric text using external resources.
      * `line_number`: The sequential number of the lyric line.
      * `syllable_count`: The syllable count of the lyric line.
      * `start`: Start timestamp of the lyric line in the audio/video.
      * `end`: End timestamp of the lyric line in the audio/video.
  * **`youtube_url`**: Dictionary containing YouTube URLs for the original and dubbed versions in different languages.
  * **`lyrics_url`**: Dictionary containing URLs to external websites where the full lyrics can be found for each language.
  * **`video`**: Boolean flags indicating the availability of video for each language.

**Example Data Snippet (Simplified for clarity):**

```json
[
    "song_title": "2_guyz_n_the_parque_s.i.m.p._(squirrels_in_my_pants)",
    "lyrics": [
      [
        {
          "US_og": {
            "text": [["Tsimp", "There's", "pants"]],
            "line_number": 0,
            "syllable_count": 6,
            "start": 21.054856,
            "end": 22.274856
          },
          "ES": {
            "text": [["Ectaeep", "Esa", "pantalón"]],
            "line_number": 0,
            "syllable_count": 14,
            "start": 13.920436,
            "end": 15.600436
          }
          // ... other languages and lines
        }
      ]
    ],
    "youtube_url": {
      "US": "https://www.youtube.com/watch?v=5WzswZXTMZQ",
      "ES": "https://www.youtube.com/watch?v=_z9JdEohNJY"
      // ... other languages
    },
    "lyrics_url": {
      "US": "https://genius.com/Phineas-and-ferb-simp-squirrels-in-my-pants-lyrics",
      "ES": "https://lyricstranslate.com/en/phineas-and-ferb-ost-apd-ardillas-por-doquier-simp-squirrels-lyrics.html"
      // ... other languages
    },
    "video": {
      "US": true,
      "ES": true
      // ... other languages
    }
]
```

## Data Collection Methodology
<div align="center">
  <img src="assets/dataset_collect.png" alt="MAVL Dataset Overview" width="800">
</div>
The MAVL dataset was collected through a multi-step web crawling and human alignment process:

1.  **Multilingual Lyrics Collection:** Metadata (song titles, artists) for English animated film music was gathered from last.fm. Original English lyrics were retrieved from Genius. Non-English lyrics corresponding to official dubbed versions were collected from platforms like lyricstranslate.com, ensuring they represent singable interpretations.
2.  **Lyrics Human Alignment:** A crucial step involved cross-referencing original English audio/video with non-English candidate lyrics and their official dubbed audio/video to rigorously verify authenticity and exclude non-official or non-singable versions. This also involved aligning the lines and sections of the non-English lyrics to the corresponding sections and lines of the original English lyrics.
3.  **Audio-Video-Lyrics Alignment:** The `stable-ts` tool (based on Whisper model) was used to generate precise timestamps, aligning audio, video, and lyrics to extract synchronized multimodal information on both English version and non-English versions.

For more detailed information on the data collection pipeline, please refer to Section 3.1 and Appendix D of our accompanying paper.

## Intended Uses & Limitations

This dataset is intended solely for **non-commercial research purposes**, such as lyrics translation, music-lyrics alignment, music information retrieval, and multimodal language model development.

**IMPORTANT LIMITATIONS:**

  * Users must independently ensure their use of the content linked via URLs complies with copyright law and YouTube's Terms of Service.
  * The dataset provides only URLs and research-generated metadata/annotations; it does not grant any rights to the underlying copyrighted content.
  * YouTube links and external lyrics links may become invalid over time.
  * The dataset primarily focuses on animated musicals and may not generalize to all musical genres or styles.
  * The current lyric representation requires external processing to reconstruct full lyric text.

## License

This dataset is distributed under the **CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International)** license (see the `LICENSE` file for full details). Key points include:

* **Attribution (BY):** You must give appropriate credit to the original creators ([Woohyun Cho/MIRLAB]).
* **NonCommercial (NC):** You may not use the dataset for commercial purposes.
* **Underlying Content Ownership:** It is crucial to understand that **this dataset does not grant any rights to the copyrighted songs/videos** linked via YouTube URLs or the full lyric texts obtained from external sources. Users are solely responsible for ensuring their use of this content complies with applicable copyright laws and YouTube's Terms of Service.
* **Dataset Compilation & Annotations:** Permission is granted to use, copy, and modify the URL compilation and any original annotations (such as timestamps, syllable counts, and IPA transcriptions) for non-commercial research, provided attribution is given to the dataset creators ([Woohyun Cho/MIRLAB]) and the license terms are followed. This metadata, compiled by our research, can be freely adapted for non-commercial purposes with proper acknowledgment.
* **NO WARRANTY:** The dataset is provided "AS IS" without warranty. Links may become broken over time.
* **Liability:** The dataset creators are not liable for any issues arising from the use of the dataset or the linked content.

## Citation

If you use the MAVL dataset in your research, please cite our paper:

```bibtex
@misc{cho2025mavlmultilingualaudiovideolyrics,
      title={MAVL: A Multilingual Audio-Video Lyrics Dataset for Animated Song Translation}, 
      author={Woohyun Cho and Youngmin Kim and Sunghyun Lee and Youngjae Yu},
      year={2025},
      eprint={2505.18614},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.18614}, 
}
```