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

**Paper:** [KVoiceBench, KOpenAudioBench, and KMMAU: Agent-Driven Korean Speech Benchmarks for Evaluating SpeechLMs](https://arxiv.org/pdf/2605.27984v1)

<p align="center">
  <a href="https://www.krafton.ai/ko/"><img src="https://img.shields.io/badge/Homepage-KRAFTON%20AI-blue?style=flat&logo=google-chrome&logoColor=white" alt="Homepage"></a>
  <a href="https://huggingface.co/KRAFTON"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-KRAFTON-yellow?style=flat" alt="Hugging Face"></a>
  <a href="#license"><img src="https://img.shields.io/badge/License-Apache%202.0-lightgrey?style=flat" alt="License"></a>
</p>

## Evaluation

Evaluation code for KVoiceBench, KOpenAudioBench, and KMMAU is available in [Raon-Eval](https://github.com/krafton-ai/Raon-Eval).

**KOpenAudioBench** is a Korean spoken question answering benchmark for evaluating speech models, built upon [OpenAudioBench](https://arxiv.org/abs/2502.00555).

## Dataset Description

As there is no existing benchmark for evaluating Korean spoken question answering capabilities, we construct KOpenAudioBench by building upon the English benchmark OpenAudioBench.

## Construction Process

Following the paper's SpokenQA transfer framework, KOpenAudioBench was built by transferring OpenAudioBench into Korean. Source samples with deterministic answers were first audited through a reviewer/meta-reviewer LLM process; confirmed label errors were corrected and invalid cases were excluded. The retained items were then hypertranslated with a human-agent rulebook. A separate human-agent normalization loop audited the hypertranslated files, organized likely TTS failure cases into a normalization rulebook, and produced speech-friendly Korean before Qwen3-TTS synthesis with Korean reference voices and WER-based resynthesis checks.

## Subsets

The dataset consists of **2,835** samples across 4 subsets:

| Subset | Samples | Task Type |
|---|---|---|
| KAlpacaEval | 614 | Open-ended |
| KLlamaQ | 284 | Short-answer QA |
| KTriviaQA | 967 | Short-answer QA |
| KWebQ | 970 | Short-answer QA |

## Features

- **id** (string): Unique sample identifier
- **audio** (Audio): Synthesized Korean speech audio
- **transcription** (string): Korean text transcription of the audio
- **answer** (string): Reference answer (empty string for open-ended subsets)
- **capability** (string): Evaluated capability category

## Usage

```python
from datasets import load_dataset

# Load a specific subset
ds = load_dataset("KRAFTON/KOpenAudioBench", "trivia_qa", split="test")
print(ds[0])
# {'id': 'trivia-qa-00000', 'audio': {'path': ..., 'array': array([...]), 'sampling_rate': 24000},
#  'transcription': '...', 'answer': '...', 'capability': '...'}

# Load all subsets
subsets = ["alpacaeval_full-test", "llamaqa", "trivia_qa", "web_questions"]
for subset in subsets:
    ds = load_dataset("KRAFTON/KOpenAudioBench", subset, split="test")
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

This dataset is released under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

&copy; 2026 KRAFTON
