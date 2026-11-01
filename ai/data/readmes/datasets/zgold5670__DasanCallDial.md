---
license: cc-by-nc-4.0
language:
  - ko
pretty_name: DasanCallDial
size_categories:
  - 100K<n<1M
task_categories:
  - text-generation
  - token-classification
tags:
  - korean
  - asr
  - asr-error-correction
  - post-editing
  - speech-recognition
  - call-center
  - dialogue
configs:
  - config_name: default
    data_files:
      - split: train
        path: train.csv
      - split: validation
        path: val.csv
      - split: test
        path: test.csv
---

# DasanCallDial

**DasanCallDial** is the first large-scale Korean benchmark built specifically for
**dialogue-level ASR error correction**. It contains **1,974 real civil-complaint call
dialogues** (**115,460 utterances**) placed to the 120 Dasan Call Foundation, Seoul's
municipal civic-information hotline. Each utterance pairs the transcription produced by a
production speech-recognition system with a human-verified ground truth.

Unlike datasets built by injecting synthetic noise, DasanCallDial preserves the
**error-sparse** distribution of a real deployed ASR system: only **9.83 %** of raw
utterances contain an error. That sparsity, rather than error density, is the central
challenge the benchmark poses.

Introduced in *"Leveraging Fine-grained Error Correction in Korean Speech Recognition for
Consultation Services"* (**Engineering Applications of Artificial Intelligence**).

* Training and evaluation code: https://github.com/yonghyun010102/Dasan_Project

## Loading

```python
from datasets import load_dataset

ds = load_dataset("zgold5670/DasanCallDial")
print(ds["train"][0])
```

To use it with the reference implementation, place the three files at
`data/dasancalldial/` inside the code repository:

```bash
hf download zgold5670/DasanCallDial --repo-type dataset \
    --local-dir data/dasancalldial
python scripts/prepare_data.py
```

## Data fields

| field | type | description |
|---|---|---|
| `KEY` | string | Dialogue identifier, derived from the call's recording date and time. Every utterance of the same call shares it. |
| `utt_index` | int | Position of the utterance within its dialogue, starting at 0. Sorting by (`KEY`, `utt_index`) reconstructs the conversation. |
| `rec_mode` | string | Speaker: `tx` = counselor, `rx` = citizen (customer). |
| `in_out` | string | Call direction (`i` inbound / `o` outbound). This is a property of the call, **not** a speaker label. |
| `STT인식문` | string | ASR transcription — the model **input**. |
| `정답문` | string | Human-verified ground truth — the **target**. |
| `오류 여부` | int | `1` if `STT인식문 != 정답문`, else `0`. Derived, provided for convenience. |

Both text columns are already segmented into utterances; no further sentence splitting is
required.

## Splits

Partitioning is done at the **dialogue** level with a 0.80 / 0.05 / 0.15 ratio, so no
conversation is shared between subsets and dialogue context never leaks across the boundary.

| split | dialogues | utterances | avg. turns | error rate |
|---|---:|---:|---:|---:|
| train | 1,579 | 91,355 | 57.86 | 9.70 % |
| validation | 98 | 5,418 | 55.29 | 8.77 % |
| test | 297 | 18,687 | 62.92 | 10.81 % |
| **total** | **1,974** | **115,460** | **58.49** | **9.83 %** |

The partition ships with the dataset, so published results do not depend on a locally drawn
split.

### Deduplicated view

Real call-center speech repeats heavily — greetings, confirmations, filler. Deduplicating on
(`STT인식문`, `정답문`) **within each partition** removes those repeats. Because most removed
duplicates are short, easily recognised, error-free phrases, the error rate roughly doubles.
This is the view the reference models are trained and scored on; `scripts/prepare_data.py`
derives it.

| split | samples | avg. chars | error rate |
|---|---:|---:|---:|
| train | 50,470 | 22.58 | 17.54 % |
| validation | 3,157 | 22.35 | 15.01 % |
| test | 11,088 | 21.84 | 18.22 % |
| **total** | **64,715** | **22.44** | **17.54 %** |

Deduplicate per partition, not globally — a global pass would move utterances across the
split boundary.

## Speaker asymmetry

Measured on the deduplicated view:

| speaker | utterances | error rate |
|---|---:|---:|
| counselor (`tx`) | 33,537 | 13.21 % |
| citizen (`rx`) | 31,178 | 22.19 % |

Counselor speech is professionally articulated and comparatively standardised, so it
transcribes more accurately. Citizen speech varies with the complaint and is often less
precisely articulated. Any model or metric that ignores this asymmetry will look better on
counselor turns than it performs in the field.

## Privacy and de-identification

De-identification was performed **at the source**, by trained 120 Dasan Call Foundation
employees with authorised audio access, before any data left the Foundation. Only the
anonymised result was shared for research. Personal names and identifying details are
replaced with masks: `***` (30,040 utterances) and `OOO` (10,801 utterances).

A regular-expression sweep over all 115,460 rows, across both text columns, finds **zero**
occurrences of:

* telephone numbers (dashed or plain mobile form)
* resident registration numbers
* digit runs of five or more characters
* email addresses, URLs, card-like number groups
* vehicle registration plates

Location references remain, but only at district (`구`, 1.46 % of rows) and neighbourhood
(`동`, 0.80 %) granularity — the level a municipal complaint requires. There are no lot
numbers, no building-and-unit numbers, and effectively no street addresses (2 rows).

If you nevertheless find residual personal information, please open a discussion on this
repository so it can be corrected.

## Intended use and limitations

Intended for **non-commercial research** on Korean ASR post-editing, error detection, and
dialogue-level correction.

* **Domain-specific.** Municipal civic-complaint calls in Korean. Vocabulary skews toward
  parking enforcement, transportation, public health, permits and welfare. Results will not
  transfer unchanged to other domains or to other languages.
* **One ASR system.** Errors reflect the specific production model used at the Foundation.
  A different recogniser makes different mistakes.
* **Text only.** Audio is not included and cannot be released; methods must be text-based
  post-editing.
* **Masks are content.** `***` and `OOO` appear in both input and target. Models will learn
  to reproduce them; a system that overwrites a mask with invented text is failing, and
  evaluation should account for that.
* **Not a speech-recognition training set.** It is built for correcting ASR output, not for
  training an ASR model.

## License

Released under **[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)**
(Attribution–NonCommercial 4.0 International): **non-commercial use only**, with attribution.

Anything derived from this dataset — including model weights trained on it — remains subject
to these non-commercial terms. The reference *code* is separately licensed MIT, but that
license does not extend to this data or to models trained on it.

Data were provided by the **120 Dasan Call Foundation** for academic research.

## Citation

```bibtex
@article{JUN2026116038,
title = {Leveraging fine-grained error correction in Korean speech recognition for consultation services},
journal = {Engineering Applications of Artificial Intelligence},
volume = {183},
pages = {116038},
year = {2026},
issn = {0952-1976},
doi = {https://doi.org/10.1016/j.engappai.2026.116038},
url = {https://www.sciencedirect.com/science/article/pii/S0952197626023225},
author = {Yonghyun Jun and Jimin Lee and Hwan Chang and Dongho Shin and Seolah Kim and Hwanhee Lee},
keywords = {Speech-to-text, Data augmentation, Supervised fine-tuning, Pre-trained language models},
abstract = {Automatic Speech Recognition (ASR) technology is fundamental to customer service automation and large-scale transcription. However, even advanced ASR models exhibit inevitable errors in complex real-world environments such as call center conversations. When privacy restrictions preclude audio access, error correction must rely on text-based post-editing. Existing text-only approaches face significant challenges in low-resource languages, mainly due to a critical scarcity of annotated corpora and tailored correction methodologies. For Korean, this resource gap is particularly pronounced, as existing resources are predominantly designed for ASR training rather than text-based error correction. To address this, we introduce DasanCallDial, the first large-scale Korean benchmark dataset specifically curated for dialogue-level ASR error correction. Derived from genuine call center interactions, it comprises 1974 dialogues with 115,460 utterances. Uniquely, it features a realistic error-sparse setting that accurately reflects high-performance modern Speech-to-Text (STT) models, distinguishing it from synthetic datasets. Leveraging this resource, we propose Detector-Gated Contextual Span Correction (DCSC), a text-only post-editing framework for error-sparse Korean speech recognition transcripts. DCSC combines an encoder-based detector that first performs token-level error detection, followed by a language model-based corrector trained to rectify fine-grained span-level errors. Additionally, we employ dialogue-level context augmentation to enable the model to leverage discourse history for disambiguation. By employing multi-level granularity, our method achieves state-of-the-art performance, effectively overcoming the limitations of general-purpose LLMs in low-resource settings. Additional analyses further characterize the learning dynamics, transferability, and robustness of DCSC. Overall, our contributions establish a vital dataset and a practical baseline poised to accelerate future research in Korean ASR post-editing.}
}
```
