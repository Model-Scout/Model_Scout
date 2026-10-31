---
dataset_info:
- config_name: age
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: original_dataset
    dtype: string
  - name: original_sample_id
    dtype: string
  - name: start_time
    dtype: float64
  - name: end_time
    dtype: float64
  splits:
  - name: test
    num_examples: 276
- config_name: fact_extraction
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: original_dataset
    dtype: string
  - name: original_sample_id
    dtype: string
  - name: start_time
    dtype: float64
  - name: end_time
    dtype: float64
  splits:
  - name: test
    num_examples: 98
- config_name: gender
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: original_dataset
    dtype: string
  - name: original_sample_id
    dtype: string
  - name: start_time
    dtype: float64
  - name: end_time
    dtype: float64
  splits:
  - name: test
    num_examples: 270
- config_name: general_counting
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: original_dataset
    dtype: string
  - name: original_sample_id
    dtype: string
  - name: start_time
    dtype: float64
  - name: end_time
    dtype: float64
  splits:
  - name: test
    num_examples: 41
- config_name: number_of_speakers
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: original_dataset
    dtype: string
  - name: original_sample_id
    dtype: string
  - name: start_time
    dtype: float64
  - name: end_time
    dtype: float64
  splits:
  - name: test
    num_examples: 100
- config_name: role_profession
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: original_dataset
    dtype: string
  - name: original_sample_id
    dtype: string
  - name: start_time
    dtype: float64
  - name: end_time
    dtype: float64
  splits:
  - name: test
    num_examples: 100
- config_name: topic_summary
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: original_dataset
    dtype: string
  - name: original_sample_id
    dtype: string
  - name: start_time
    dtype: float64
  - name: end_time
    dtype: float64
  splits:
  - name: test
    num_examples: 100
- config_name: word_frequency_counting
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: original_dataset
    dtype: string
  - name: original_sample_id
    dtype: string
  - name: start_time
    dtype: float64
  - name: end_time
    dtype: float64
  splits:
  - name: test
    num_examples: 180
- config_name: word_order
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: original_dataset
    dtype: string
  - name: original_sample_id
    dtype: string
  - name: start_time
    dtype: 'null'
  - name: end_time
    dtype: 'null'
  splits:
  - name: test
    num_examples: 1039
configs:
- config_name: age
  data_files:
  - split: test
    path: age/test-*
- config_name: fact_extraction
  data_files:
  - split: test
    path: fact_extraction/test-*
- config_name: gender
  data_files:
  - split: test
    path: gender/test-*
- config_name: general_counting
  data_files:
  - split: test
    path: general_counting/test-*
- config_name: number_of_speakers
  data_files:
  - split: test
    path: number_of_speakers/test-*
- config_name: role_profession
  data_files:
  - split: test
    path: role_profession/test-*
- config_name: topic_summary
  data_files:
  - split: test
    path: topic_summary/test-*
- config_name: word_frequency_counting
  data_files:
  - split: test
    path: word_frequency_counting/test-*
- config_name: word_order
  data_files:
  - split: test
    path: word_order/test-*
license: cc-by-nc-sa-4.0
task_categories:
- automatic-speech-recognition
- question-answering
language:
- ko
pretty_name: KMMAU
size_categories:
- 1K<n<10K
---

# KMMAU

<p align="center">
  <a href="#license"><img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat" alt="License"></a>
</p>

**KMMAU** is a Korean audio understanding benchmark constructed from naturally occurring Korean audio. It is part of a Korean speech benchmark suite for evaluating SpeechLMs together with KVoiceBench and KOpenAudioBench.

## Dataset Description

KMMAU contains **2,204** Korean audio understanding samples built from KSS, KMSAV, and the Seoul Corpus rather than transferred English items. It evaluates both acoustic and contextual audio understanding capabilities using multiple-choice questions grounded in Korean audio.

KMMAU is constructed from target-language ASR corpora using four construction methods selected by capability:

1. **Rule-based generation from speaker metadata** for acoustic attributes such as age, gender, and number of speakers.
2. **Rule-based generation from transcriptions** for lexical questions such as word order and word frequency.
3. **LLM-generated questions with human review** for semantic questions such as fact extraction and topic summary.
4. **Fully manual annotation** for holistic capabilities that require listening to the audio, such as general counting and role/profession.

The benchmark contains 646 acoustic samples and 1,558 contextual samples. All KMMAU samples are multiple-choice: gender uses 2 choices, age uses 3 choices, and the remaining capabilities use 4 choices.

## Subsets

The dataset consists of **2,204** samples across 9 capabilities:

| Config | Category | Samples | Capability |
|---|---|---:|---|
| `age` | Acoustic | 276 | Speaker age group estimation |
| `gender` | Acoustic | 270 | Speaker gender identification |
| `number_of_speakers` | Acoustic | 100 | Number of speakers detection |
| `word_order` | Contextual | 1,039 | Word order verification |
| `word_frequency_counting` | Contextual | 180 | Word frequency counting in speech |
| `fact_extraction` | Contextual | 98 | Factual information extraction from dialogue |
| `topic_summary` | Contextual | 100 | Topic summarization |
| `role_profession` | Contextual | 100 | Speaker role/profession identification |
| `general_counting` | Contextual | 41 | General counting over audio content |

## Features

- **id** (string): Unique sample identifier
- **audio** (Audio): Korean speech audio
- **question** (string): Question about the audio
- **answer** (string): Reference answer
- **original_dataset** (string): Source dataset name
- **original_sample_id** (string): Sample identifier in the source dataset
- **start_time** (float, optional): Audio segment start time in seconds
- **end_time** (float, optional): Audio segment end time in seconds

## Usage

```python
from datasets import load_dataset

# Load a specific subset
ds = load_dataset("anonyemnlpauthor18/KMMAU", "age", split="test")
print(ds[0])

# Load all subsets
subsets = [
    "age", "fact_extraction", "gender", "general_counting",
    "number_of_speakers", "role_profession",
    "topic_summary", "word_frequency_counting", "word_order"
]
for subset in subsets:
    ds = load_dataset("anonyemnlpauthor18/KMMAU", subset, split="test")
    print(f"{subset}: {len(ds)} samples")
```

## Citation

```bibtex
@article{korean_speech_benchmarks2026,
  title={KVoiceBench, KOpenAudioBench, and KMMAU: Agent-Driven Korean Speech Benchmarks for Evaluating SpeechLMs},
  author={Anonymous Authors},
  year={2026}
}
```

## License

This dataset is released under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

&copy; 2026 Anonymous Authors
