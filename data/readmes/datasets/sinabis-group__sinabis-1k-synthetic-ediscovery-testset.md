---
license: cc-by-4.0
language: [en, es, zh, ja, ar, pt, tr, nb, ko, it, nl, id, fr, hi, de, cs, vi, hu, sv, uk]
pretty_name: Sinabis 1k eDiscovery Test Set (synthetic)
size_categories: [1K<n<10K]
task_categories: [text-classification, feature-extraction]
tags: [ediscovery, forensics, legal, synthetic, email, deduplication, threading, tar, privilege, pii]
configs:
- config_name: manifest
  data_files: manifest/manifest.parquet
  default: true
---

# Sinabis 1k eDiscovery Test Set (synthetic)

A fully synthetic, **1,010-document** collection for testing eDiscovery and forensic software end to end:
processing, de-duplication, e-mail threading, search, TAR / predictive coding, privilege screening, PII detection and
handling of broken files. All people, companies, agencies, events and data are fictional (domain `.example`,
phone numbers `555-01xx`, test card numbers, IBANs with valid check digits but no real accounts).

This is the 1k edition of the [Sinabis 1M eDiscovery Test Set](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-ediscovery-testset),
small enough for a first test run, a demo or a CI pipeline. Documents, files, hashes and IDs are identical to the
1M set and it is a subset of the [10k edition](https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-ediscovery-testset).

> **Note:** the collection intentionally contains **corrupt, truncated, password-protected and nested files**.
> Not every file opens – that is the point. See *Processing exceptions* below.

The company is *Sinabis Green Energy*, a fictional clean-energy group (solar, wind, charging, storage, autonomous
shuttles, water treatment, a foundation) with ~7,850 employees across the US, Japan, Australia, New Zealand, China
and the UAE (2016–2026). **152 of the 160 custodians** appear in this edition.

## How this edition was selected

- **Nothing is cut apart:** e-mail families (message + attachments), e-mail threads and the copies of one message in
  several mailboxes form units that are always taken whole.
- **Duplicates stay testable:** exact-duplicate and near-duplicate groups were seeded with 2–3 members each, so that
  their share matches the 1M set.
- **Password hints come along:** every password-protected document brings the e-mail that contains its password.
- **Minimum coverage:** before random filling, small units were added until every task can be tested:
  at least 15 responsive documents and 1–2 decoys per matter, 2 hot documents and 2 documents of every
  exception type. Units stay whole, so a single thread can bring more (here all hot documents of one thread).
- **Random rest:** the remaining units were drawn at random; out of 50 draws the one closest to the
  composition of the 1M set was kept.

The ground truth of this edition (in the separate repository [`sinabis-1k-synthetic-ediscovery-testset-groundtruth`](https://huggingface.co/datasets/sinabis-group/sinabis-1k-synthetic-ediscovery-testset-groundtruth)) contains
exactly these documents. Groups (duplicates, threads, …) are the same IDs as in the 1M set, restricted to the
documents present here.

## Files

| Path | Size | Content |
|---|---:|---|
| `manifest/manifest.parquet` | 154 KB | one row per document: identity, family, archive location, hashes, custodian, header and property metadata **as extracted from the file** (shown in the dataset viewer) |
| `Sinabis_1k_ediscovery.zip` | 54 MB | the native files at `natives/<nnnn>/<doc_id>.<ext>` |
| `Sinabis_1k_ediscovery_text.zip` | 2 MB | extracted text per document (`text/<nnnn>/<doc_id>.txt`), empty where nothing can be extracted |
| `loadfile/loadfile.dat` | 541 KB | Concordance load file (field delimiter ASCII 20, quote ASCII 254 `þ`, in-field newline ASCII 174 `®`, UTF-8) |
| `loadfile/loadfile.opt` | 14 KB | Opticon cross-reference for PDF natives |

```bash
hf download sinabis-group/sinabis-1k-synthetic-ediscovery-testset --repo-type dataset --local-dir sinabis-1k-ediscovery
cd sinabis-1k-ediscovery && unzip -q Sinabis_1k_ediscovery.zip && unzip -q Sinabis_1k_ediscovery_text.zip
```

Expected results (relevance, privilege, PII, duplicates, threads, exceptions …) are **not** in this repository. They
live in the separate repository [**`sinabis-1k-synthetic-ediscovery-testset-groundtruth`**](https://huggingface.co/datasets/sinabis-group/sinabis-1k-synthetic-ediscovery-testset-groundtruth) so the manifest does not give away the answers.

## Composition

| Document type | Documents |
|---|---:|
| file | 700 |
| email | 142 |
| chat | 74 |
| attachment | 68 |
| calendar | 26 |

| Data source | Documents |
|---|---:|
| fileshare | 700 |
| mailbox | 210 |
| chat | 74 |
| calendar | 26 |

Top file extensions (as found – some are deliberately wrong):

| Extension | Documents |
|---|---:|
| pdf | 260 |
| docx | 217 |
| eml | 157 |
| pptx | 123 |
| xlsx | 120 |
| rsmf | 41 |
| ics | 41 |
| zip | 18 |
| json | 18 |
| png | 7 |
| – | 2 |
| doc | 2 |
| xls | 1 |
| bak | 1 |
| dat | 1 |

Attachments are separate documents linked to their e-mail through `family_id` / `parent_id` / `family_pos`
(61 families with children). The same message appears in several custodians' mailboxes (sender and
recipients), as in a real collection.

## Manifest fields

`doc_id` (control number `EDT-0000001`), `family_id`, `parent_id`, `family_pos`, `doc_type`
(`email`, `attachment`, `file`, `chat`, `calendar`), `file_name`, `file_ext`, `file_size`, `archive`,
`archive_path`, `md5`, `sha256`, `custodian_id`, `data_source` (`mailbox`, `fileshare`, `chat`, `calendar`),
`source_path` (mailbox folder or share path), `from_addr`, `to_addrs`, `cc_addrs`, `bcc_addrs`, `subject`,
`message_id`, `in_reply_to`, `date_sent`, `date_received`, `date_created`, `date_modified`, `author`, `title`,
`text_path`, `synthetic`, `generator_version`, `seed`, `source_dataset`.

Header and property fields come from parsing the file itself. Where a file cannot be parsed (corrupt, encrypted,
wrong format) they are empty – exactly what an intake would see.

## What a tool should find (answers in the ground-truth repo)

* 4 matters with responsive documents (M-01: 19, M-02: 29, M-03: 15, M-04: 18),
  including conceptual hits without the obvious keywords and 8 keyword decoys that are not responsive
* 24 privileged documents (attorney–client, work product; full or partial)
* 15 hot documents
* 35 documents with **synthetic** PII – realistic-looking but fictional (IBANs with valid check digits, tax IDs,
  SSN formats, phone, address, date of birth, passport and test card numbers, health data). No real persons.
* exact duplicates (176 documents in 82 duplicate groups), the same message in several
  mailboxes (77), near-duplicate version chains (127)
* 33 e-mail threads with two or more e-mails, incl. forks (forwards with a new audience), inclusive e-mails
* 100 scanned PDFs that need OCR
* languages: en 926, es 26, zh 14, ja 5, ar 5, pt 4, tr 3, nb 3, ko 3, it 3

## Processing exceptions

| Exception type | Documents |
|---|---:|
| wrong_extension | 9 |
| truncated | 7 |
| broken_mail | 5 |
| nested | 4 |
| embedded | 4 |
| password | 4 |
| odd_name | 4 |
| time_anomaly | 3 |
| zero_byte | 3 |
| bytes_corrupted | 3 |

## Scoring

The ground-truth repository contains `evaluate.py`, which scores a tool's output (CSV, Parquet or JSON Lines, one row
per `doc_id`) for relevance per matter (incl. TAR ranking), privilege, hot documents, PII, de-duplication, threading
and processing outcomes. See its README.

## Disclaimer

Synthetic data for testing software. Any resemblance to real persons, companies or events is coincidental.
