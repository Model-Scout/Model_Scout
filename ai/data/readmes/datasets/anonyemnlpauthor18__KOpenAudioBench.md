---
dataset_info:
- config_name: alpacaeval_full-test
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  - name: transcription
    dtype: string
  - name: answer
    dtype: string
  - name: capability
    dtype: string
  splits:
  - name: test
    num_examples: 614
- config_name: llamaqa
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  - name: transcription
    dtype: string
  - name: answer
    dtype: string
  - name: capability
    dtype: string
  splits:
  - name: test
    num_examples: 284
- config_name: trivia_qa
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  - name: transcription
    dtype: string
  - name: answer
    dtype: string
  - name: capability
    dtype: string
  splits:
  - name: test
    num_examples: 967
- config_name: web_questions
  features:
  - name: id
    dtype: string
  - name: audio
    dtype: audio
  - name: transcription
    dtype: string
  - name: answer
    dtype: string
  - name: capability
    dtype: string
  splits:
  - name: test
    num_examples: 970
configs:
- config_name: alpacaeval_full-test
  data_files:
  - split: test
    path: alpacaeval_full-test/test-*
- config_name: llamaqa
  data_files:
  - split: test
    path: llamaqa/test-*
- config_name: trivia_qa
  data_files:
  - split: test
    path: trivia_qa/test-*
- config_name: web_questions
  data_files:
  - split: test
    path: web_questions/test-*
license: apache-2.0
task_categories:
- automatic-speech-recognition
- question-answering
language:
- ko
pretty_name: KOpenAudioBench
size_categories:
- 1K<n<10K
---

# KOpenAudioBench

<p align="center">
  <a href="#license"><img src="https://img.shields.io/badge/License-Apache%202.0-lightgrey?style=flat" alt="License"></a>
</p>

**KOpenAudioBench** is a Korean spoken question answering (SpokenQA) benchmark derived from OpenAudioBench. It is part of a Korean speech benchmark suite for evaluating SpeechLMs together with KVoiceBench and KMMAU.

## Dataset Description

KOpenAudioBench contains **2,835** Korean spoken QA samples across 4 subsets: 2,221 short-answer questions and 614 open-ended prompts. It emphasizes short factual answers and open-ended spoken prompts covering categories such as history/geography, entertainment/arts, humanities, practical knowledge, sports, and natural science.

KOpenAudioBench is constructed with the same human-agent SpokenQA benchmark transfer framework used for KVoiceBench:

1. **Ground-truth correction** audits deterministic short-answer source samples before transfer.
2. **Hypertranslation** transfers source-language questions into Korean using a rulebook that handles direct adaptation, equivalent replacement, deletion, and Korean-specific redesign.
3. **Speech-friendly normalization** converts written-only forms into pronounceable Korean text before synthesis.
4. **TTS synthesis** generates Korean speech from normalized text using Korean reference voices, followed by ASR-based quality checking and re-synthesis when needed.

Because many KOpenAudioBench items require short factual answers rather than option selection, answer alias handling is part of the transfer process. For example, an English answer such as "Netherlands" is mapped to acceptable Korean aliases such as "네덜란드", "화란", and "홀란드", while aliases that collapse into the same Korean form are deduplicated.

## Subsets

The dataset consists of **2,835** samples across 4 subsets:

| Config | Paper Subset | Samples | Task Type |
|---|---:|---:|---|
| `alpacaeval_full-test` | KAlpacaEval | 614 | Open-ended generation |
| `llamaqa` | KLlamaQ | 284 | Short-answer QA |
| `trivia_qa` | KTriviaQA | 967 | Short-answer QA |
| `web_questions` | KWebQ | 970 | Short-answer QA |

For KOpenAudioBench, **2,835 of 2,936** source samples are retained after ground-truth correction, hypertranslation, and Korean-specific redesign.

## Features

- **id** (string): Unique sample identifier
- **audio** (Audio): Synthesized Korean speech audio
- **transcription** (string): Korean text transcription of the audio
- **answer** (string): Reference answer, if applicable
- **capability** (string): Evaluated capability category

## Usage

```python
from datasets import load_dataset

# Load a specific subset
ds = load_dataset("anonyemnlpauthor18/KOpenAudioBench", "trivia_qa", split="test")
print(ds[0])

# Load all subsets
subsets = ["alpacaeval_full-test", "llamaqa", "trivia_qa", "web_questions"]
for subset in subsets:
    ds = load_dataset("anonyemnlpauthor18/KOpenAudioBench", subset, split="test")
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

This dataset is released under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

&copy; 2026 Anonymous Authors
