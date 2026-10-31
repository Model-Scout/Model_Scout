---
license: cc-by-4.0
language: [en, es, zh, ja, ar, id, fr, de, tr, pt, it, ko, pl, nl, vi, sv, el, ru, hu, hi, fi, uk, da, nb, ro, cs]
pretty_name: Sinabis 10k eDiscovery Test Set (synthetic)
size_categories: [10K<n<100K]
task_categories: [text-classification, feature-extraction]
tags: [ediscovery, forensics, legal, synthetic, email, deduplication, threading, tar, privilege, pii]
configs:
- config_name: manifest
  data_files: manifest/manifest.parquet
  default: true
---

# Sinabis 10k eDiscovery Test Set (synthetic)

A fully synthetic, **10,100-document** collection for testing eDiscovery and forensic software end to end:
processing, de-duplication, e-mail threading, search, TAR / predictive coding, privilege screening, PII detection and
handling of broken files. All people, companies, agencies, events and data are fictional (domain `.example`,
phone numbers `555-01xx`, test card numbers, IBANs with valid check digits but no real accounts).

This is the 10k edition of the [Sinabis 1M eDiscovery Test Set](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-ediscovery-testset),
small enough for a first test run, a demo or a CI pipeline. Documents, files, hashes and IDs are identical to the
1M set.

> **Note:** the collection intentionally contains **corrupt, truncated, password-protected and nested files**.
> Not every file opens – that is the point. See *Processing exceptions* below.

The company is *Sinabis Green Energy*, a fictional clean-energy group (solar, wind, charging, storage, autonomous
shuttles, water treatment, a foundation) with ~7,850 employees across the US, Japan, Australia, New Zealand, China
and the UAE (2016–2026). **160 of the 160 custodians** appear in this edition.

## How this edition was selected

- **Nothing is cut apart:** e-mail families (message + attachments), e-mail threads and the copies of one message in
  several mailboxes form units that are always taken whole.
- **Duplicates stay testable:** exact-duplicate and near-duplicate groups were seeded with 2–3 members each, so that
  their share matches the 1M set.
- **Password hints come along:** every password-protected document brings the e-mail that contains its password.
- **Random rest:** the remaining units were drawn at random; out of 20 draws the one closest to the
  composition of the 1M set was kept.

The ground truth of this edition (in the separate repository [`sinabis-10k-synthetic-ediscovery-testset-groundtruth`](https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-ediscovery-testset-groundtruth)) contains
exactly these documents. Groups (duplicates, threads, …) are the same IDs as in the 1M set, restricted to the
documents present here.

## Files

| Path | Size | Content |
|---|---:|---|
| `manifest/manifest.parquet` | 1 MB | one row per document: identity, family, archive location, hashes, custodian, header and property metadata **as extracted from the file** (shown in the dataset viewer) |
| `Sinabis_10k_ediscovery.zip` | 533 MB | the native files at `natives/<nnnn>/<doc_id>.<ext>` |
| `Sinabis_10k_ediscovery_text.zip` | 15 MB | extracted text per document (`text/<nnnn>/<doc_id>.txt`), empty where nothing can be extracted |
| `loadfile/loadfile.dat` | 5 MB | Concordance load file (field delimiter ASCII 20, quote ASCII 254 `þ`, in-field newline ASCII 174 `®`, UTF-8) |
| `loadfile/loadfile.opt` | 140 KB | Opticon cross-reference for PDF natives |

```bash
hf download sinabis-group/sinabis-10k-synthetic-ediscovery-testset --repo-type dataset --local-dir sinabis-10k-ediscovery
cd sinabis-10k-ediscovery && unzip -q Sinabis_10k_ediscovery.zip && unzip -q Sinabis_10k_ediscovery_text.zip
```

Expected results (relevance, privilege, PII, duplicates, threads, exceptions …) are **not** in this repository. They
live in the separate repository [**`sinabis-10k-synthetic-ediscovery-testset-groundtruth`**](https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-ediscovery-testset-groundtruth) so the manifest does not give away the answers.

## Composition

| Document type | Documents |
|---|---:|
| file | 6,585 |
| email | 1,598 |
| chat | 807 |
| attachment | 731 |
| calendar | 379 |

| Data source | Documents |
|---|---:|
| fileshare | 6,585 |
| mailbox | 2,329 |
| chat | 807 |
| calendar | 379 |

Top file extensions (as found – some are deliberately wrong):

| Extension | Documents |
|---|---:|
| pdf | 2,549 |
| docx | 2,173 |
| eml | 1,727 |
| pptx | 1,064 |
| xlsx | 1,056 |
| ics | 562 |
| rsmf | 468 |
| json | 209 |
| zip | 208 |
| png | 47 |
| – | 8 |
| dat | 5 |
| bak | 4 |
| csv | 4 |
| jpg | 4 |

Attachments are separate documents linked to their e-mail through `family_id` / `parent_id` / `family_pos`
(652 families with children). The same message appears in several custodians' mailboxes (sender and
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

* 4 matters with responsive documents (M-01: 152, M-02: 213, M-03: 173, M-04: 234),
  including conceptual hits without the obvious keywords and 37 keyword decoys that are not responsive
* 237 privileged documents (attorney–client, work product; full or partial)
* 15 hot documents
* 345 documents with **synthetic** PII – realistic-looking but fictional (IBANs with valid check digits, tax IDs,
  SSN formats, phone, address, date of birth, passport and test card numbers, health data). No real persons.
* exact duplicates (1,689 documents in 780 duplicate groups), the same message in several
  mailboxes (836), near-duplicate version chains (1,175)
* 382 e-mail threads with two or more e-mails, incl. forks (forwards with a new audience), inclusive e-mails
* 1,089 scanned PDFs that need OCR
* languages: en 9,133, es 304, zh 112, ja 85, ar 49, id 42, fr 41, de 41, tr 39, pt 33

## Processing exceptions

| Exception type | Documents |
|---|---:|
| password | 85 |
| truncated | 75 |
| broken_mail | 53 |
| bytes_corrupted | 49 |
| wrong_extension | 39 |
| embedded | 38 |
| nested | 37 |
| odd_name | 23 |
| zero_byte | 20 |
| time_anomaly | 18 |

## Scoring

The ground-truth repository contains `evaluate.py`, which scores a tool's output (CSV, Parquet or JSON Lines, one row
per `doc_id`) for relevance per matter (incl. TAR ranking), privilege, hot documents, PII, de-duplication, threading
and processing outcomes. See its README.

## Disclaimer

Synthetic data for testing software. Any resemblance to real persons, companies or events is coincidental.
