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

<p align="center">
  <a href="#license"><img src="https://img.shields.io/badge/License-Apache%202.0-lightgrey?style=flat" alt="License"></a>
</p>

**KVoiceBench** is a Korean spoken question answering (SpokenQA) benchmark derived from VoiceBench. It is part of a Korean speech benchmark suite for evaluating SpeechLMs together with KOpenAudioBench and KMMAU.

## Dataset Description

KVoiceBench contains **7,306** Korean spoken QA samples across 9 subsets. It evaluates multiple-choice, binary reasoning, short-answer, open-ended generation, instruction following, and safety behavior under Korean speech input.

KVoiceBench is not the result of naive translation alone. It is constructed through a human-agent SpokenQA benchmark transfer framework:

1. **Ground-truth correction** audits deterministic source samples before transfer so source-label errors do not propagate into Korean.
2. **Hypertranslation** transfers source-language questions into Korean using a rulebook that handles direct adaptation, equivalent replacement, deletion, and Korean-specific redesign.
3. **Speech-friendly normalization** converts written-only forms such as option labels, numbers, units, symbols, abbreviations, and mixed Korean-English expressions into pronounceable Korean text.
4. **TTS synthesis** generates Korean speech from normalized text using Korean reference voices, followed by ASR-based quality checking and re-synthesis when needed.

During transfer, English-specific task designs are adapted rather than literally translated. For example, because Korean has no direct equivalent to English adjective-ordering constraints, BBH hyperbaton questions are replaced with Korean grammar judgments over particles and endings. Case-sensitive instructions are removed, and letter-frequency constraints are mapped to Korean letters.

## Subsets

The dataset consists of **7,306** samples across 9 subsets:

| Config | Paper Subset | Samples | Task Type |
|---|---:|---:|---|
| `openbookqa-test` | KOpenBookQA | 445 | Multiple-choice QA |
| `mmsu` | KMMSU | 3,006 | Multiple-choice QA |
| `bbh-test` | KBBH | 750 | Binary reasoning / grammar judgment |
| `sd-qa` | KSD-QA | 533 | Short-answer QA |
| `alpacaeval_full-test` | KAlpacaEval | 614 | Open-ended generation |
| `commoneval-test` | KCommonEval | 194 | Open-ended generation |
| `wildvoice-test` | KWildVoice | 972 | Open-ended generation |
| `ifeval-test` | KIFEval | 279 | Instruction following |
| `advbench-test` | KAdvBench | 513 | Safety / harmful-request refusal |

For KVoiceBench, **7,306 of 7,783** source samples are retained after ground-truth correction, hypertranslation, and Korean-specific redesign.

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
ds = load_dataset("anonyemnlpauthor18/KVoiceBench", "bbh-test", split="test")
print(ds[0])

# Load all subsets
subsets = [
    "advbench-test", "alpacaeval_full-test", "bbh-test", "commoneval-test",
    "ifeval-test", "mmsu", "openbookqa-test", "sd-qa", "wildvoice-test"
]
for subset in subsets:
    ds = load_dataset("anonyemnlpauthor18/KVoiceBench", subset, split="test")
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
