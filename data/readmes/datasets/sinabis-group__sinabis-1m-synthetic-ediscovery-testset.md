---
license: cc-by-4.0
language: [en, ja, zh, es, de, fr, ar, pt, it, nl, ko, pl]
pretty_name: Sinabis 1M eDiscovery Test Set (synthetic)
size_categories: [1M<n<10M]
task_categories: [text-classification, feature-extraction]
tags: [ediscovery, forensics, legal, synthetic, email, deduplication, threading, tar, privilege, pii]
configs:
- config_name: manifest
  data_files: manifest/manifest.parquet
  default: true
---

# Sinabis 1M eDiscovery Test Set (synthetic)

A fully synthetic, **1,005,254-document** collection for testing eDiscovery and forensic software end to end:
processing, de-duplication, e-mail threading, search, TAR / predictive coding, privilege screening, PII detection and
handling of broken files. All people, companies, agencies, events and data are fictional (domain `.example`,
phone numbers `555-01xx`, test card numbers, IBANs with valid check digits but no real accounts).

> **Smaller editions** with the same structure and their own ground truth:
> [10k](https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-ediscovery-testset) ·
> [1k](https://huggingface.co/datasets/sinabis-group/sinabis-1k-synthetic-ediscovery-testset).
> Scoring script: `evaluate.py` in the [ground-truth repository](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-ediscovery-testset-groundtruth).

> **Note:** the collection intentionally contains **corrupt, truncated, password-protected and nested files**.
> Not every file opens – that is the point. See *Processing exceptions* below.

The company is *Sinabis Green Energy*, a fictional clean-energy group (solar, wind, charging, storage, autonomous
shuttles, water treatment, a foundation) with ~7,850 employees across the US, Japan, Australia, New Zealand, China
and the UAE (2016–2026). **160 custodians** each contribute a mailbox, a file share, chats and a
calendar.

## Files

| Path | Content |
|---|---|
| `manifest/manifest.parquet` | one row per document: identity, family, archive location, hashes, custodian, header and property metadata **as extracted from the file** (shown in the dataset viewer) |
| `Sinabis_1M_ediscovery_part_NN.zip` (15 parts, 57.2 GB) | the native files at `natives/<nnnn>/<doc_id>.<ext>` |
| `Sinabis_1M_ediscovery_text_part_NN.zip` | extracted text per document (`text/<nnnn>/<doc_id>.txt`), empty where nothing can be extracted |
| `loadfile/loadfile.dat` | Concordance load file (field delimiter ASCII 20, quote ASCII 254 `þ`, in-field newline ASCII 174 `®`, UTF-8) |
| `loadfile/loadfile.opt` | Opticon cross-reference for PDF natives |

Expected results (relevance, privilege, PII, duplicates, threads, exceptions …) are **not** in this repository. They
live in the separate repository [**`sinabis-1m-synthetic-ediscovery-testset-groundtruth`**](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-ediscovery-testset-groundtruth) so the manifest does not give away the answers.

## Composition

| Document type | Documents |
|---|---:|
| file | 580,434 |
| email | 192,382 |
| chat | 100,000 |
| attachment | 82,438 |
| calendar | 50,000 |

| Data source | Documents |
|---|---:|
| fileshare | 580,434 |
| mailbox | 274,820 |
| chat | 100,000 |
| calendar | 50,000 |

Top file extensions (as found – some are deliberately wrong):

| Extension | Documents |
|---|---:|
| pdf | 228,795 |
| eml | 208,405 |
| docx | 185,020 |
| pptx | 98,676 |
| xlsx | 96,011 |
| ics | 68,814 |
| rsmf | 60,116 |
| json | 25,039 |
| zip | 23,781 |
| png | 6,758 |
| – | 1,135 |
| txt | 446 |
| dat | 280 |
| bin | 271 |
| xls | 265 |
| tmp | 262 |
| ppt | 251 |
| bak | 250 |
| doc | 233 |
| jpg | 192 |
| csv | 157 |
|   | 36 |
| pptx  | 16 |
| xlsx  | 15 |
| pdf  | 12 |

Attachments are separate documents linked to their e-mail through `family_id` / `parent_id` / `family_pos`
(75,822 families with children). The same message appears in several custodians'
mailboxes (sender and recipients), as in a real collection.

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

* 4 matters with responsive documents (M-01: 25,327, M-02: 19,943, M-03: 15,917, M-04: 20,593),
  including conceptual hits without the obvious keywords and keyword decoys that are not responsive
* 23,217 privileged documents (attorney–client, work product; full or partial)
* 1,075 hot documents
* 34,216 documents with **synthetic** PII – realistic-looking but fictional (IBANs with valid check digits, tax IDs,
  SSN formats, phone, address, date of birth, passport and test card numbers, health data). No real persons.
* exact duplicates (149,137 documents in duplicate groups), the same message in several
  mailboxes (94,875), near-duplicate version chains (124,206)
* 57,372 e-mail threads incl. forks (forwards with a new audience), inclusive e-mails
* 90,143 scanned PDFs that need OCR
* languages: en 902,301, es 29,446, zh 12,732, ja 9,043, ar 6,575, de 4,185, it 3,340, pt 3,298, pl 3,254, ko 3,218

## Processing exceptions

| Exception type | Documents |
|---|---:|
| password | 10,468 |
| truncated | 10,035 |
| bytes_corrupted | 5,012 |
| embedded | 5,000 |
| wrong_extension | 4,973 |
| nested | 4,970 |
| broken_mail | 4,936 |
| odd_name | 2,535 |
| zero_byte | 2,532 |
| time_anomaly | 2,487 |

## Disclaimer

Synthetic data for testing software. Any resemblance to real persons, companies or events is coincidental.
