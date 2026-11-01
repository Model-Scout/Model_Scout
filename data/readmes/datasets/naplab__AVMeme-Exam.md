---
language:
- en
- zh
- ja
- ko
- hi
multilinguality:
- multilingual
tags:
- audio
- video
- multimodal
- memes
- cultural-understanding
- temporal-reasoning
- benchmark
pretty_name: AVMeme-Exam
size_categories:
- 1K<n<10K
task_categories:
- question-answering
- multiple-choice
license: other
configs:
- config_name: default
  data_files:
  - split: test
    path: good_memes_QA.parquet
---


<div align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/6531a65daed617662c7f1007/0w-jdQDv9SjC-8y88C_rU.png" width="1000"/>

  <h1 style="font-size: 30px; margin-top: 12px;">
    A Multimodal Multilingual Multicultural Benchmark for LLMs' Contextual and Cultural Knowledge and Thinking Beyond Text
  </h1>

  <p style="font-size: 18px; margin-top: 6px;">
    <a href="https://arxiv.org/abs/2601.17645" target="_blank">[arXiv]</a>
    &nbsp;|&nbsp;
    <a href="https://avmemeexam.github.io/public" target="_blank">[demo]</a>
  </p>
</div>


## Overview

AVMeme Exam is a multimodal benchmark for testing whether multimodal large language models (MLLMs) can really understand audio-visual memes, the short, widespread clips you see every day on YouTube, TikTok, Bilibili, X, etc. 
Beyond recognizing “what is said” or “what object is shown”, it evaluates deeper, richer multimedia knowledge and thinking: cultural context, implied meaning, induced emotion, use of audio/video, and world knowledge.

## Motivation

We believe that AGI should recognize media beyond text and understand the context, emotion, culture, and usage of audio and video, just like humans. 
Existing multimodal benchmarks primarily focus on standard ASR, sound and object recognition, and NLP tasks. 
Even advanced multimodal understanding largely evaluates explicit content hearable or visible within audio or video frames.

Therefore, here we test whether MLLMs can understand audio-visual memes, to think and feel above audio and video content, and where they succeed or fail.

## Dataset

- **Multimodal**: Audio, video, and text
- **Multilingual**: Multiple languages, including English, Chinese, Japanese, Korean, Hindi, Persian, and others
- **Multicultural**: Diverse cultural contexts and references


There are two JSON files:
`avmeme_full` is our full test set of 1032 meme clips. `avmeme_main` is a harder subset of 846 meme clips.

**Videos are downsampled to 360p at 1 FPS**. If you need higher resolution or frame rates, please download the original videos from the URLs with appropriate tools.

### Data Schema

| Field           | Description                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `category`      | Type of meme audio (e.g., clean speech, noisy speech, song, music, sound effect)                                                               |
| `name`          | Meme identifier or commonly used title                                                                                                         |
| `url`           | Original source URL of the meme                                                                                                                |
| `onset`         | Start time of the selected segment (in seconds)                                                                                                |
| `offset`        | End time of the selected segment (in seconds)                                                                                                  |
| `original_date` | Year when the meme or source content first appeared                                                                                            |
| `language`      | Primary spoken or sung language (or `N/A` for non-verbal audio)                                                                                |
| `transcription` | Speech transcription if available; `null` for non-verbal audio                                                                                 |
| `summary`       | Description of the clip content and scenario                                                                                                   |
| `emotion`       | Annotated emotional cues conveyed by the meme (e.g., sarcastic, happy, nostalgic)                                                              |
| `sensitivity`   | Content safety tags (e.g., none, sex, violence, drug/alcohol)                                                                                  |
| `usage`         | Typical meme usage or communicative intent in online contexts                                                                                  |
| `question`      | Multiple-choice question designed to test meme understanding                                                                                   |
| `choices`       | List of candidate answer options                                                                                                               |
| `solution`      | Correct answer                                                                                                                                 |
| `question_type` | Question category in Language Analysis, Audio Analysis, Contextual Inference, Emotion Analysis, Humor & Popularity, Usage & Application, and World Knowledge |
| `video_path`    | Relative path to the trimmed video clip. If visual_cheat=True, this field is None, meaning LLM should ***NOT*** see the visual.                |
| `audio_path`    | Relative path to the trimmed audio clip                                                                                                        |
| `visual_hint`   | Optional visual cues available to the model (e.g., transcription, title text, irrelevant text)                                                 |
| `visual_cheat`  | Boolean flag indicating whether visual information directly reveals the answer                                                                 |
| `question_MC`   | The exact prompt to test LLM in multiple-choice format                                                                                         |
| `solution_MC`   | The letter (e.g., A, B, C) of `solution` in multiple-choice format                                                                             |

***Audio and video file names contain clip UIDs. For testing models with file names coded as text tokens and commercial models (e.g., Gemini), we recommend using temporary copies with anonymized file names.***


## Example

```json
{
    "category": "sound effect",
    "name": "Goat Talking to Clueless Huh Cat",
    "url": "https://www.youtube.com/watch?v=B7aSDu6Qh6U",
    "onset": 0.0,
    "offset": 9.0,
    "original_date": 2024,
    "language": "N/A",
    "transcription": null,
    "summary": "A goat talking to a cat.",
    "emotion": [
        "surprised/shocked"
    ],
    "sensitivity": [
        "none"
    ],
    "usage": "Used to depict a situation where one person passionately and intensely explains a complex or niche topic to another person who is utterly confused, overwhelmed, or uncomprehending.",
    "question": "What kind of conversational dynamic are they used to represent?",
    "choices": [
        "One person chaotically spouting nonsense to a listener who responds with confusion.",
        "A deep, meaningful conversation where both parties are fully engaged.",
        "An angry argument between two equally aggressive individuals.",
        "A calm and patient mentor teaching a highly attentive student."
    ],
    "solution": "One person chaotically spouting nonsense to a listener who responds with confusion.",
    "question_type": "Contextual Inference",
    "video_path": "video/B7aSDu6Qh6U_0.0_9.0.mp4",
    "audio_path": "audio/B7aSDu6Qh6U_0.0_9.0.wav",
    "visual_hint": [
        "No text"
    ],
    "visual_cheat": false
}
```

## Usage

```python
# The latest huggingface datasets no longer supports custom dataset loading script
pip install datasets==3.6.0
```

```python
from datasets import load_dataset
full_memes = load_dataset("naplab/AVMeme-Exam", "full", split="test") # for full 1032 memes
main_memes = load_dataset("naplab/AVMeme-Exam", "main", split="test") # for harder 846 memes

# Audio is loaded as a 16kHz waveform. Video (if not "visual_cheat") is returned as a path.
full_memes[0]
```

## Citation

```bibtex
@misc{
  jiang2026avmemeexammultimodalmultilingual,
  title={AVMeme Exam: A Multimodal Multilingual Multicultural Benchmark for LLMs' Contextual and Cultural Knowledge and Thinking}, 
  author={Xilin Jiang and Qiaolin Wang and Junkai Wu and Xiaomin He and Zhongweiyang Xu and Yinghao Ma and Minshuo Piao and Kaiyi Yang and Xiuwen Zheng and Riki Shimizu and Yicong Chen and Arsalan Firoozi and Gavin Mischler and Sukru Samet Dindar and Richard Antonello and Linyang He and Tsun-An Hsieh and Xulin Fan and Yulun Wu and Yuesheng Ma and Chaitanya Amballa and Weixiong Chen and Jiarui Hai and Ruisi Li and Vishal Choudhari and Cong Han and Yinghao Aaron Li and Adeen Flinker and Mounya Elhilali and Emmanouil Benetos and Mark Hasegawa-Johnson and Romit Roy Choudhury and Nima Mesgarani},
  year={2026},
  eprint={2601.17645},
  archivePrefix={arXiv},
  primaryClass={cs.SD},
  url={https://arxiv.org/abs/2601.17645}, 
}
```

## License

Annotations and metadata are released under CC BY 4.0.

The associated audio and video clips are collected from publicly available online sources and are provided solely for academic research. 

Users are responsible for complying with the original content licenses.

## Ethical Considerations

- Content includes sensitivity tags for mature themes
- Reflects online meme culture with inherent biases
- Requires cultural familiarity for appropriate judgment

---