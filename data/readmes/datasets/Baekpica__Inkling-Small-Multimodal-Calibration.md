---
license: other
license_name: source-dataset-licenses
license_link: https://huggingface.co/datasets/Baekpica/Inkling-Small-Multimodal-Calibration/blob/main/LICENSES.md
pretty_name: Inkling-Small Multimodal Calibration
size_categories:
- 1K<n<10K
task_categories:
- text-generation
- image-text-to-text
- automatic-speech-recognition
language:
- en
- ko
- ja
- pt
- hi
- zh
- de
- fr
- es
- ru
tags:
- calibration
- imatrix
- inkling
- multimodal
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*.parquet
---

# Inkling-Small Multimodal Calibration

The exact 1,663 samples used for BF16 routed-expert importance collection
for [Inkling-Small Mixed Quant GGUF](https://huggingface.co/Baekpica/Inkling-Small-Mixed-Quant-GGUF).
This is calibration material, not a held-out evaluation benchmark.

The primary balanced pass is:

| Category | Samples | Valid decoder tokens | Share |
|---|---:|---:|---:|
| Text / reasoning | 462 | 471,858 | 44.976% |
| Code / tool-oriented source text | 205 | 209,715 | 19.989% |
| Real image / document | 486 | 262,476 | 25.018% |
| Real speech audio | 309 | 105,080 | 10.016% |
| Total | 1,462 | 1,049,129 | 100% |

A subsequent coverage pass added 201 real structured reasoning/tool conversations
(529,126 tokens, seed 3408, up to 4,096 tokens per sample). It probes rare
experts, including L41 expert 123, which remained unobserved after both passes.
The final model protects L40–41 with Q4_K; expert 123 uses ordinary Q4_K
without fabricated importance data.
These are normalized from the pinned NVIDIA Instruction-Following-Chat-v2
reasoning_on and Cascade-SFT-Stage-2 tool_calling sources and rendered with actual
Inkling thinking/tool syntax. Total actual input: **1,578,255 tokens**.

`importance_weight` is 1.0 for primary examples and 0.1 for the coverage supplement.
Imatrix statistics normalize weighted squared-input sums by weighted actual hit
counts; raw unweighted route counts are audited separately. The weights keep
rare-expert coverage additions from dominating the original multimodal mix.

| Category | Actual tokens | Actual share | Importance-weighted share |
|---|---:|---:|---:|
| Text / reasoning | 736,165 | 46.644% | 45.215% |
| Code / tool | 474,534 | 30.067% | 21.433% |
| Image / document | 262,476 | 16.631% | 23.817% |
| Audio | 105,080 | 6.658% | 9.535% |

The original balanced dataset remains available at revision
`4ceb58745dcb2cde3d018c52942f881f072284ac`. This revision includes both passes.
The effective weighted token count is 1,102,041.6; it is not a count of unique
observations. The public manifest records both counts explicitly.

Shares count valid decoder positions, including image/audio placeholder positions
and their accompanying text. They are not document shares, media-only token shares,
or separately reweighted loss quotas. Padding does not contribute. Each sparse
layer routes six expert observations per valid decoder token.

Text is sampled deterministically (seed 3407) from checksum-verified prior
K2-Horizon calibration text pools, using the composition of the Solar Healing Mix
and a Tulu/FineWeb supplement. These pools were decoded with the Solar tokenizer;
we **re-tokenized the text using Inkling**, without carrying Solar token IDs or
its control-token syntax into the model. Fixed 1,024-token text windows may cross
original document boundaries. Code/tool denotes the source category, not a claim
that every sample is a complete executable tool conversation.

Image inputs use the first training parquet of DocVQA and ChartQA at pinned
revisions; duplicate image bytes are rejected. Images are resized within
1280×1280 before the official Inkling processor. Audio uses real LibriSpeech
train.clean.100 recordings at 16 kHz (2–60 seconds), the official dMel processor
and corresponding transcription text. No synthetic media or random embeddings
stand in for a modality. `source` records identify the original parquet row.

The Parquet index contains readable text, input IDs, category and exact tensor
pack filename/hash. The **actual processor outputs** are in `tensors/*.safetensors`:
`input_ids`, optional `attention_mask`, `pixel_values`, `audio_input_ids`, and
`audio_input_ids_mask`. These allow bit-exact input replay without decoding the
original media again. They are model inputs, not learned model weights.

```python
from datasets import load_dataset
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file
rows = load_dataset("Baekpica/Inkling-Small-Multimodal-Calibration", split="train")
row = rows[0]
path = hf_hub_download("Baekpica/Inkling-Small-Multimodal-Calibration",
                       row["tensor_file"], repo_type="dataset")
inputs = load_file(path)
```

The tokenizer, source configuration, chat template, processor configuration,
selection manifest and source lineage are included. Input processing used
Hugging Face Transformers source checked out on 2026-09-09; the exact commit
is recorded with the reproduction materials and model handoff.

See [LICENSES.md](LICENSES.md). Source-specific licenses remain applicable;
this collection does not relicense its constituent examples.

## Rebuilding and replay

For exact replay, download the published tensor packs and use the index above.
`build_samples.py` reconstructs the primary pack from source media and the
checksum-pinned K2 text pools; those historical pool files are retained in the
owner’s earlier private handoff. `build_supplement.py` reconstructs the added
structured dialogs; its two source dataset revisions and raw row hashes are
in `manifest.json`. The normalizer helpers are under `refs/`.
Set `INKLING_ROOT` to the prepared work tree, with tokenizer/processor files
in `source/`, source media under `calibration/`, and the helpers in `refs/`.
The pinned Transformers commit is in `provenance/toolchain.json`. Exact input
replay does not require access to the private historical text pools.
