---
language:
- ko
task_categories:
- text-to-speech
pretty_name: Emilia-YODAS Korean for pocket-tts
size_categories:
- 100K<n<1M
---

# Emilia-YODAS Korean for pocket-tts

Train-ready, Qwen3-forced-aligned Korean data derived from
[`seastar105/Emilia-YODAS-KO-filtered`](https://huggingface.co/datasets/seastar105/Emilia-YODAS-KO-filtered/tree/8b0741c1d478843d8fd4acc15c66edcbe3b23495).
The training transcript is the source JSON `text` field after NFC and whitespace
normalization. `pred` was not reconciled into the transcript.

| split | utterances | hours |
|---|---:|---:|
| train | 918,609 | 2276.88 |
| valid | 9,472 | 23.00 |

The repository includes 196 original TAR shards,
portable gzip JSONL manifests with word timestamps, the 4,000-piece Korean
SentencePiece tokenizer, configs, preparation/alignment reports, and a bounded-worker
materialization script.

## Download and unpack

Install and authenticate the modern Hugging Face CLI, download this script, then run:

```bash
hf auth login
hf download seastar105/emilia-yodas-ko-filtered-pocket-tts download_train_ready.py --repo-type dataset --local-dir .
python download_train_ready.py --output-dir data/emilia_yodas_ko
```

The downloader invokes `hf download`, extracts TARs safely and resumably, rewrites
manifest paths for the local node, and verifies every referenced audio file. Defaults
are four download and four extraction workers to bound WSL RAM usage. Use
`--delete-archives-after-extract` to reclaim approximately 65 GiB after successful
materialization.

## Manifest format

Each JSONL row has `path`, `duration`, `transcript`, `speaker`, and `words`. Each word
contains `word`, `start`, and `end`; nullable timestamps represent an isolated
zero-duration alignment unit. Additional `source_*` fields preserve provenance.

Alignment used `Qwen/Qwen3-ForcedAligner-0.6B`. Structural audits proving complete
source coverage and timestamp validity are in `reports/`. This release does not claim
manual alignment-quality review. The source dataset does not declare a license in its
Hub metadata; users must establish that their intended use is permitted.

## Train

From a pocket-tts checkout:

```bash
uv run python -m training.train training/configs/korean_lsd_scratch_4k.yaml \
  --train-jsonl /path/to/data/emilia_yodas_ko/manifests/train_aligned.jsonl \
  --valid-jsonl /path/to/data/emilia_yodas_ko/manifests/valid_aligned.jsonl \
  --tokenizer-path /path/to/data/emilia_yodas_ko/tokenizer/korean_4000.model
```

## Deferred work

Transcript reconciliation is intentionally deferred as a TODO until the initial
training and evaluation pipeline is fully tested and complete.
