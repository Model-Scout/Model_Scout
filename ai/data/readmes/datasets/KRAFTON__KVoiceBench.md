---
dataset_info:
- config_name: advbench-test
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
    num_examples: 513
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
- config_name: bbh-test
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
    num_examples: 750
- config_name: commoneval-test
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
    num_examples: 194
- config_name: ifeval-test
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
    num_examples: 279
- config_name: mmsu
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
    num_examples: 3006
- config_name: openbookqa-test
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
    num_examples: 445
- config_name: sd-qa
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
    num_examples: 533
- config_name: wildvoice-test
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
    num_examples: 972
configs:
- config_name: advbench-test
  data_files:
  - split: test
    path: advbench-test/test-*
- config_name: alpacaeval_full-test
  data_files:
  - split: test
    path: alpacaeval_full-test/test-*
- config_name: bbh-test
  data_files:
  - split: test
    path: bbh-test/test-*
- config_name: commoneval-test
  data_files:
  - split: test
    path: commoneval-test/test-*
- config_name: ifeval-test
  data_files:
  - split: test
    path: ifeval-test/test-*
- config_name: mmsu
  data_files:
  - split: test
    path: mmsu/test-*
- config_name: openbookqa-test
  data_files:
  - split: test
    path: openbookqa-test/test-*
- config_name: sd-qa
  data_files:
  - split: test
    path: sd-qa/test-*
- config_name: wildvoice-test
  data_files:
  - split: test
    path: wildvoice-test/test-*
license: apache-2.0
task_categories:
- automatic-speech-recognition
- question-answering
language:
- ko
pretty_name: KVoiceBench
size_categories:
- 1K<n<10K
---

# KVoiceBench

**Paper:** [KVoiceBench, KOpenAudioBench, and KMMAU: Agent-Driven Korean Speech Benchmarks for Evaluating SpeechLMs](https://arxiv.org/pdf/2605.27984v1)

<p align="center">
  <a href="https://www.krafton.ai/ko/"><img src="https://img.shields.io/badge/Homepage-KRAFTON%20AI-blue?style=flat&logo=google-chrome&logoColor=white" alt="Homepage"></a>
  <a href="https://huggingface.co/KRAFTON"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-KRAFTON-yellow?style=flat" alt="Hugging Face"></a>
  <a href="#license"><img src="https://img.shields.io/badge/License-Apache%202.0-lightgrey?style=flat" alt="License"></a>
</p>

## Evaluation

Evaluation code for KVoiceBench, KOpenAudioBench, and KMMAU is available in [Raon-Eval](https://github.com/krafton-ai/Raon-Eval).

**KVoiceBench** is a Korean spoken question answering benchmark for evaluating speech models, built upon [VoiceBench](https://arxiv.org/abs/2410.17196).

## Dataset Description

As there is no existing benchmark for evaluating Korean spoken question answering capabilities, we construct KVoiceBench by building upon the English benchmark VoiceBench.

## Construction Process

Following the paper's SpokenQA transfer framework, KVoiceBench was built by transferring VoiceBench into Korean. Source samples with deterministic answers were first audited through a reviewer/meta-reviewer LLM process; confirmed label errors were corrected and invalid cases were excluded. The retained items were then hypertranslated with a human-agent rulebook. A separate human-agent normalization loop audited the hypertranslated files, organized likely TTS failure cases into a normalization rulebook, and produced speech-friendly Korean before Qwen3-TTS synthesis with Korean reference voices and WER-based resynthesis checks.

## Subsets

The dataset consists of **7,306** samples across 9 subsets:

| Subset | Samples | Task Type |
|---|---|---|
| KOpenBookQA | 445 | Multiple-choice QA |
| KMMSU | 3,006 | Multiple-choice QA |
| KBBH | 750 | Binary reasoning |
| KSD-QA | 533 | Short-answer QA |
| KAlpacaEval | 614 | Open-ended |
| KCommonEval | 194 | Open-ended |
| KWildVoice | 972 | Open-ended |
| KIFEval | 279 | Instruction following |
| KAdvBench | 513 | Safety |

## Features

- **id** (string): Unique sample identifier
- **audio** (Audio): Synthesized Korean speech audio
- **transcription** (string): Korean text transcription of the audio
- **answer** (string): Reference answer (empty string for open-ended/safety subsets)
- **capability** (string): Evaluated capability category

## Usage

```python
from datasets import load_dataset

# Load a specific subset
ds = load_dataset("KRAFTON/KVoiceBench", "bbh-test", split="test")
print(ds[0])
# {'id': 'bbh_navigate_147', 'audio': {'path': ..., 'array': array([...]), 'sampling_rate': 24000},
#  'transcription': '...', 'answer': '...', 'capability': 'context_related/multi_hop_reasoning'}

# Load all subsets
subsets = [
    "advbench-test", "alpacaeval_full-test", "bbh-test", "commoneval-test",
    "ifeval-test", "mmsu", "openbookqa-test", "sd-qa", "wildvoice-test"
]
for subset in subsets:
    ds = load_dataset("KRAFTON/KVoiceBench", subset, split="test")
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
