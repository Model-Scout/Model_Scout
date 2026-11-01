---
language:
- ko
- ja
license: apache-2.0
size_categories:
- n<1K
task_categories:
- automatic-speech-recognition
pretty_name: Korean-Japanese-Code-Switching-Speech
tags:
- audio
- speech
- code-switching
- korean
- japanese
---

# Korean-Japanese-Code-Switching-Speech

This dataset contains Korean-Japanese code-switching speech recordings with sentence-level transcriptions. It was introduced in the paper [Towards Truly Multilingual ASR: Generalizing Code-Switching ASR to Unseen Language Pairs](https://huggingface.co/papers/2606.05846).

Since there is an extremely small amount of Korean-Japanese code-switching data available, this dataset was designed to be used as a small-scale evaluation dataset.

The dataset consists of code-switching recordings produced by two Korean participants who are fluent in both Korean and Japanese. It can be used to evaluate the basic Korean-Japanese code-switching capability of ASR models, but it may not be suitable for evaluations that require diverse speaker characteristics such as nationality, gender, and age group.

## Dataset Summary
- Split: `test`
- Rows: `450`
- Audio format: 16 kHz WAV stored in the Hugging Face `Audio` feature
- Total duration: `2902.89` seconds
- Main-language labels: `Korean`, `Japanese`
- Code-switching level labels: `word`, `phrase`, `sentence`

## Columns

- `audio`: speech audio
- `text`: transcription
- `script_id`: source script identifier
- `main_language`: primary language of the utterance
- `cs_level`: code-switching granularity
- `category`: topic/category label
- `duration_sec`: audio duration in seconds

## How to Cite
```bibtex
@misc{paik2026towards,
      title={Towards Truly Multilingual ASR: Generalizing Code-Switching ASR to Unseen Language Pairs}, 
      author={Gio Paik and Hyunseo Shin and Soungmin Lee},
      year={2026},
      eprint={2606.05846},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2606.05846}, 
}
```