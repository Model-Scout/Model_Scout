---
license: other
task_categories:
- text-to-speech
language:
- zh
- en
- ja
- ko
tags:
- tts
- speech
- distillation
- multilingual
pretty_name: Multilingual Test Distill Strong TTS 20260520
---

# Multilingual Test Distill Strong TTS 20260520

This repository contains a distributable tar-sharded version of `multilingual_test_distill_strong_tts_20260520`.

The dataset follows the local `voice_dataset/data` layout after extraction:

```text
data/csvs/metadata_zh.csv
data/csvs/metadata_en.csv
data/csvs/metadata_ja.csv
data/csvs/metadata_ko.csv
data/zh/**/*.wav
data/en/**/*.wav
data/ja/**/*.wav
data/ko/**/*.wav
```

Metadata format:

```text
file_path|duration|dnsmos|text
```

`dnsmos` is intentionally blank because DNSMOS scores were not available for these reference/generated wavs.

## Restore

Download all tar files under `shards/`, then extract them into the same directory:

```bash
for f in shards/*.tar; do tar -xf "$f"; done
```

## Contents

- zh: 1500 rows, reference prompts plus zh-zh and en-zh generated wavs
- en: 1500 rows, reference prompts plus en-en and zh-en generated wavs
- ja: 1000 rows, reference prompts plus ja-ja generated wavs
- ko: 1000 rows, reference prompts plus ko-ko generated wavs

See `dataset_summary.json` and `tar_manifest.json` for exact counts and checksums.
