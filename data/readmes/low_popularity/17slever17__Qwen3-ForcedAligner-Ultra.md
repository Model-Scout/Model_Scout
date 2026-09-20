---
license: apache-2.0
language:
  - en
  - zh
  - fr
  - de
  - it
  - ja
  - ko
  - ru
  - es
  - pt
  - yue
library_name: transformers
pipeline_tag: automatic-speech-recognition
base_model:
  - Qwen/Qwen3-ForcedAligner-0.6B
base_model_relation: finetune
tags:
  - qwen3
  - forced-alignment
  - word-timestamps
  - multilingual
  - subtitle-alignment
  - robust-alignment
  - code-switching
---

<p align="center">
  <img src="https://huggingface.co/17slever17/Qwen3-ForcedAligner-Ultra/resolve/main/assets/qwen3-forced-aligner-ultra-banner.png"
       alt="Qwen3-ForcedAligner-Ultra"
       width="100%">
</p>

# Qwen3-ForcedAligner-Ultra

**Qwen3-ForcedAligner-Ultra** is a multilingual forced aligner derived from
`Qwen/Qwen3-ForcedAligner-0.6B`. It is designed for precise word timestamps on
heterogeneous conversational, accented, noisy, and code-switched speech, even
when the supplied transcript is not a literal match for the audio.

An optional small **Local Head** refines boundaries inside the selected acoustic
island at 10 ms resolution. This addresses the inherent 80 ms timestamp-bin
resolution of Qwen: the main model can select the correct acoustic island but
cannot physically place every boundary with finer precision on that grid. The main
Qwen model handles global word-to-audio alignment; the Local Head then refines
the boundary inside a bounded `+/-60 ms` neighborhood.

## Highlights

- **Large reduction in alignment outliers:** the averaged model reduces
  MAE from `124.95 ms` to `34.95 ms` and `>1000 ms` errors from `1.565%` to
  `0.195%` relative to the official Qwen checkpoint on the same evaluation.
- **Precise local boundaries:** the optional Local Head lowers MAE to
  `26.59 ms`, with `78.32%` of endpoints within `25 ms`.
- **Transcript mismatch robustness:** training includes real ASR substitutions,
  insertions and split/merge patterns, plus explicit missing-word examples.
- **Acoustic robustness:** the mixture includes controlled speed, noise,
  reverberation and gain changes while retaining exact reference timestamps.
- **Multilingual and code-switched:** the model retains support for all 11
  Qwen3 Forced Aligner languages and was fine-tuned with explicit
  mixed-language utterances.
- **Drop-in base mode:** without the Local Head, inference uses the normal
  `qwen-asr` forced-aligner API.

## Intended use

The model is intended for word-level forced alignment when both audio and a
transcript are available. Typical applications include subtitle timing,
transcript repair, speech-dataset preparation, dubbing tools, and timestamping
ASR output that contains occasional substitutions, insertions, or omissions.

Supported languages are Chinese, English, Cantonese, French, German, Italian,
Japanese, Korean, Portuguese, Russian, and Spanish. Chinese, English, French,
German, Italian, Japanese, Korean, Russian, and Spanish received the most
direct fine-tuning and evaluation coverage; Cantonese and Portuguese retain
the underlying Qwen support and should be validated for the target domain.

## Benchmark results

All accuracy results use one recording-disjoint multilingual evaluation:

- `6.5h` of audio;
- `105,022` start/end timestamp endpoints;
- nine languages;
- exact manually annotated or manually corrected word boundaries;
- identical audio, transcript, endpoint identities, and metric definitions.

`FIXED` means the official Qwen `fix_timestamp()` post-processing was applied
once. MMS and WhisperX use their native word boundaries and do not receive
Qwen-specific post-processing. Lower is better for error metrics; higher is
better for accuracy and RTFx.

#### Alignment accuracy [%]

| Model | `t <= 10 ms` | `t <= 25 ms` | `t <= 50 ms` | `t <= 100 ms` |
| --- | ---: | ---: | ---: | ---: |
| Official Qwen3-ForcedAligner-0.6B, FIXED | 22.087 | 46.203 | 77.597 | 91.050 |
| **Qwen3-ForcedAligner-Ultra, FIXED** | 26.148 | 55.207 | 89.886 | 96.663 |
| **Qwen3-ForcedAligner-Ultra + Local Head, FIXED** | **47.113** | **78.315** | **91.821** | **96.768** |
| MMS-300M-1130 | 9.188 | 26.144 | 55.769 | 84.202 |

#### Boundary error and catastrophic tail

| Model | MAE, ms | P90 | P95 | P97 | P99 | `>240 ms` | `>500 ms` | `>1000 ms` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Official Qwen3-ForcedAligner-0.6B, FIXED | 124.949 | 90.688 | 185.122 | 347.882 | 2106.159 | 4.017% | 2.379% | 1.565% |
| **Qwen3-ForcedAligner-Ultra, FIXED** | 34.947 | 50.425 | 75.684 | 110.000 | **260.908** | **1.113%** | 0.509% | **0.195%** |
| **Qwen3-ForcedAligner-Ultra + Local Head, FIXED** | **26.590** | **43.335** | **71.108** | **105.958** | 261.325 | 1.122% | **0.505%** | **0.195%** |
| MMS-300M-1130 | 98.179 | 132.240 | 207.041 | 315.325 | 1016.740 | 4.094% | 1.912% | 1.020% |

### External noisy conversational test

One additional external test used more difficult, less clean conversational
audio outside the main multilingual evaluation. It shows that the Qwen-based
models transfer substantially better to this recording style, especially in
the catastrophic tail. This is a small start-boundary test, so it is presented
as supporting evidence rather than the primary benchmark.

| Model | MAE, ms | P90, ms | `>500 ms` | `t <= 50 ms` |
| --- | ---: | ---: | ---: | ---: |
| Official Qwen3-ForcedAligner-0.6B, FIXED | 89.66 | 105.20 | 4.10% | 75.25% |
| **Qwen3-ForcedAligner-Ultra, FIXED** | 60.94 | **81.40** | 2.12% | 76.10% |
| **Qwen3-ForcedAligner-Ultra + Local Head, FIXED** | **58.63** | 81.88 | **1.98%** | **82.32%** |
| MMS-300M-1130 | 373.86 | 321.38 | 8.49% | 59.69% |

### Speed on NVIDIA GeForce RTX 5070 Ti

| Model | End-to-end RTFx |
| --- | ---: |
| Official Qwen3-ForcedAligner-0.6B | `150x` |
| Qwen3-ForcedAligner-Ultra | `150x` |
| Qwen3-ForcedAligner-Ultra + Local Head | `95x` |
| MMS-300M-1130 | `180x` |
| WhisperX English align model | `67x` |

## Training overview

Qwen3-ForcedAligner-Ultra starts from the official
`Qwen/Qwen3-ForcedAligner-0.6B` checkpoint and uses a conservative multilingual
LoRA fine-tune with a trainable timestamp head. Three neighboring merged
checkpoints are averaged to reduce run-specific variance.

The selected training mixture contains approximately **70 hours** of diverse,
multilingual speech. Its clean supervision uses high-quality manual or manually
corrected word boundaries. Derived examples preserve those gold timestamps while
changing the input conditions:

- **Transcript deletions:** spoken words remain in the audio but are omitted
  from the transcript, teaching surrounding words not to drift.
- **Real ASR errors:** ASR substitutions, insertions, repetitions, and
  split/merge errors are aligned back to the original gold speech. Unmatched
  hallucinated words are masked instead of receiving fabricated timestamps.
- **Acoustic transforms:** speed, noise, reverberation, and gain variations
  retain the exact word-boundary supervision.
- **Code switching:** mixed-language speech and transcripts are included
  explicitly rather than inferred from monolingual examples.

The data mixture was balanced for linguistic and acoustic diversity rather
than optimized for a single benchmark or recording style.

## Usage without Local Head

Install the official Qwen runtime:

```bash
pip install -U qwen-asr
```

```python
import torch
from qwen_asr import Qwen3ForcedAligner

aligner = Qwen3ForcedAligner.from_pretrained(
    "17slever17/Qwen3-ForcedAligner-Ultra",
    dtype=torch.bfloat16,
    device_map="cuda:0",
)

results = aligner.align(
    audio="speech.wav",
    text="The transcript to align.",
    language="English",
)

for word in results[0]:
    print(word.text, word.start_time, word.end_time)
```

Audio may also be passed as a URL, base64 payload, local path, or
`(numpy_array, sample_rate)` tuple. Batch inference follows the normal
`qwen-asr` API.

## Usage with Local Head

Install the official Qwen runtime and the small companion package:

```bash
pip install -U "https://huggingface.co/17slever17/Qwen3-ForcedAligner-Ultra/resolve/main/companion/dist/qwen_fa_ultra-0.1.1-py3-none-any.whl"
```

```python
import torch
from qwen_fa_ultra import LocalBoundaryAligner

aligner = LocalBoundaryAligner.from_pretrained(
    "17slever17/Qwen3-ForcedAligner-Ultra",
    device="cuda:0",
    dtype=torch.bfloat16,
    head_batch_size=512,
)

results = aligner.align(
    audio="audio.wav",
    text="I really thought that was funny",
    language="English",
)

for word in results[0]:
    print(word.text, word.start_time, word.end_time)
```

Batch inference accepts lists for all three inputs:

```python
results = aligner.align(
    audio=["english.wav", "french.wav"],
    text=["Good morning", "Bonjour tout le monde"],
    language=["English", "French"],
)
```

`from_pretrained()` loads the main checkpoint through the official `qwen-asr`
runtime and resolves `local_head/config.json`, `model.safetensors`, and the
persisted feature normalizer from the same Hub repository. It does not require
a Transformers fork or `trust_remote_code`.

Internally, production inference runs Qwen exactly once, retains the timestamp
hidden states from that same forward pass, and applies official
`fix_timestamp()` once. It then extracts batched acoustic features only around
the FIXED boundaries and predicts bounded `+/-60 ms` corrections. If a pair of
corrections would make a word shorter than `10 ms`, the two boundaries are
minimally projected around their shared midpoint to preserve a valid interval.
Neighboring words are then projected onto a strictly non-overlapping timeline.
When two words overlap, the runtime trusts the more accurate next-word START
and trims the previous word END to that boundary. Only when this would make the
previous word shorter than `10 ms` is the shared boundary moved forward by the
minimum amount needed to preserve valid durations. RAW Local Head features are
not computed in production.

The Local Head remains optional. Loading the repository with
`Qwen3ForcedAligner.from_pretrained()` instead uses Ultra through the unchanged
official API and skips local refinement entirely.

## Citation

```bibtex
@misc{17slever17_qwen3_forced_aligner_ultra_2026,
  author       = {17slever17},
  title        = {Qwen3-ForcedAligner-Ultra},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/17slever17/Qwen3-ForcedAligner-Ultra}}
}
```
