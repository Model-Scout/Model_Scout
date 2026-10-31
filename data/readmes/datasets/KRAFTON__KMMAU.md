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

**Paper:** [KVoiceBench, KOpenAudioBench, and KMMAU: Agent-Driven Korean Speech Benchmarks for Evaluating SpeechLMs](https://arxiv.org/pdf/2605.27984v1)

<p align="center">
  <a href="https://www.krafton.ai/ko/"><img src="https://img.shields.io/badge/Homepage-KRAFTON%20AI-blue?style=flat&logo=google-chrome&logoColor=white" alt="Homepage"></a>
  <a href="https://huggingface.co/KRAFTON"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-KRAFTON-yellow?style=flat" alt="Hugging Face"></a>
  <a href="#license"><img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat" alt="License"></a>
</p>

## Evaluation

Evaluation code for KVoiceBench, KOpenAudioBench, and KMMAU is available in [Raon-Eval](https://github.com/krafton-ai/Raon-Eval).

**KMMAU** is a Korean Multi-Modal Audio Understanding benchmark for evaluating speech models on diverse audio comprehension tasks.

## Dataset Description

KMMAU evaluates audio understanding capabilities across 9 subsets covering age, gender, number of speakers, fact extraction, general counting, profession identification, topic summarization, word frequency counting, and word order verification. The benchmark is constructed from three Korean speech datasets: Seoul Corpus, KMSAV, and KSS.

## Construction Process

Following the paper's audio-understanding framework, KMMAU was built from Korean ASR corpora and metadata rather than translated English audio. Questions were generated by capability: speaker metadata for age, gender, and number of speakers; transcriptions for word order and word-frequency counting; LLM generation with human review for fact extraction and topic summary; and manual annotation for general counting and role/profession.

## Subsets

The dataset consists of **2,204** samples across 9 subsets:

| Subset | Samples | Description | Capability |
|---|---|---|---|
| age | 276 | Speaker age group estimation | acoustic_related/speech/paralinguistic/age |
| gender | 270 | Speaker gender identification | acoustic_related/speech/paralinguistic/gender |
| number_of_speakers | 100 | Number of speakers detection | acoustic_related/speech/number_of_speakers |
| fact_extraction | 98 | Factual information extraction from dialogue | context_related/contextual_knowledge/fact_extraction |
| general_counting | 41 | Counting entities mentioned in audio | context_related/contextual_knowledge/general_counting |
| role_profession | 100 | Speaker role/profession identification | context_related/contextual_knowledge/role_profession |
| topic_summary | 100 | Topic summarization | context_related/contextual_knowledge/topic_summary |
| word_frequency_counting | 180 | Word frequency counting in speech | context_related/contextual_knowledge/word_frequency_counting |
| word_order | 1,039 | Word order verification | context_related/contextual_knowledge/word_order |

## Features

- **id** (string): Unique sample identifier (`{capability}-{index}`)
- **audio** (Audio): Speech audio
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
ds = load_dataset("KRAFTON/KMMAU", "age", split="test")
print(ds[0])
# {'id': 'age-0000', 'audio': {'path': ..., 'array': array([...]), 'sampling_rate': 16000},
#  'question': '...', 'answer': '...', 'original_dataset': 'seoul-corpus', ...}

# Load all subsets
subsets = [
    "age", "fact_extraction", "gender", "general_counting",
    "number_of_speakers", "role_profession",
    "topic_summary", "word_frequency_counting", "word_order"
]
for subset in subsets:
    ds = load_dataset("KRAFTON/KMMAU", subset, split="test")
    print(f"{subset}: {len(ds)} samples")
```

## Citation

```bibtex
@misc{kim2026kvoicebenchkopenaudiobenchkmmau,
  title={KVoiceBench, KOpenAudioBench, and KMMAU: Agent-Driven Korean Speech Benchmarks for Evaluating SpeechLMs},
  author={Kim, Haechan and Chung, Seungjun and Park, Inkyu and Lee, Jihoo and Lee, Jonghyun},
  year={2026},
  eprint={2605.27984},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/pdf/2605.27984v1}
}
```

## License

This dataset is released under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

&copy; 2026 KRAFTON
