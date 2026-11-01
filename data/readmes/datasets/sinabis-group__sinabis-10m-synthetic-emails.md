---
license: cc-by-4.0
language:
  - en
  - es
  - ja
  - zh
  - ar
  - de
  - ko
  - hi
  - it
  - fr
  - pt
  - nl
  - pl
  - id
  - tr
  - ru
  - tl
  - vi
  - th
  - he
  - ro
  - nb
  - da
  - uk
  - el
  - sv
  - cs
  - hu
  - fi
task_categories:
  - text-generation
  - text-classification
  - summarization
  - token-classification
  - feature-extraction
language_creators:
  - machine-generated
multilinguality:
  - multilingual
source_datasets:
  - original
tags:
  - synthetic
  - synthetic-data
  - email
  - emails
  - eml
  - calendar
  - ics
  - digital-forensics
  - forensics
  - e-discovery
  - renewable-energy
  - enterprise
  - business
  - multilingual
  - llm
  - llm-training
  - pretraining
  - nlp
  - threads
  - information-extraction
size_categories:
  - 10M<n<100M
---

# Sinabis Green Energy – Synthetic Email Dataset

More than **10 million emails** and **1.4 million calendar files** from the
everyday business of a fictional renewable-energy group. They span ten and a
half years, six countries and 29 languages, and they include real
attachments. Every person, company, authority, law and event is made up. The
content was written by large language models, and the `mailgen` generator
built the structure around it.

> All figures in this file were **computed from the files themselves**
> (as of 7 Oct 2026). They are not target values from the configuration.

> **Also available:** the smaller
> [Sinabis Oil – Synthetic Email Dataset](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-emails)
> (1.25 million emails, four languages) from a different fictional company,
> an oil and gas group.

## At a glance

| | |
|---|---|
| Emails | **10,088,914** (177.8 GB, `.eml` per RFC 5322): 8,768,999 from run 1, 1,319,915 from run 2 |
| Calendar files | **1,420,492** `.ics` (iCalendar, RFC 5545): 492,543 `REQUEST`, 908,716 `REPLY`, 19,233 `CANCEL` |
| Business cases | **3,680,231** with emails: 2,013,994 email threads, 851,530 single emails, 806,833 system notifications, 7,874 HR lifecycle events |
| Meetings | **322,673** meetings with 1,269,964 calendar files (`.ics` only, no email) |
| Attachments | **2,227,176** files in 2,075,531 emails: 1,158,365 PDF · 507,520 DOCX · 450,989 XLSX · 110,302 PNG/images |
| Time span | December 2015 to July 2026, growing from 0.54 to 1.34 million emails per year |
| Languages | 29: 87.4 % English, 8.8 % Spanish, the rest spread over 27 languages |
| People | 7,850 employees (2,880 active in 2016 → 7,310 in 2026) in 21 departments, 9,663 external contacts |
| Organisations | 7 group companies + 832 others (customers, suppliers, subcontractors, authorities, NGOs, media …) |

## What it is about

**Sinabis Green Energy** (headquartered in Austin, Texas, fictional) builds
and operates everything that is green: rooftop and utility-scale solar
(installation and annual maintenance), wind farms, EV charging parks,
autonomous shuttles, battery storage, water treatment and CO2-neutral
buildings. A foundation cleans oil from the sea and recycles plastic bottles,
a research institute publishes (made-up) studies, and a government affairs
office lobbies made-up politicians for made-up US funding programmes.

There are **830 topics** in the emails, including:

solar annual maintenance renewal · inverter fault work order · yield below
forecast · residential underperformance complaint · subcontractor liability
dispute · scaffolding subcontract redlines · module short shipment · battery
connector recall · shuttle brake sensor recall · boil-water advisory ·
net-metering application delay · fall-protection near miss · heat-wave crew
warning · grant applications and lobbying · HR, IT, finance and procurement
topics and more.

The COVID-19 pandemic is part of the story from 2020 on (masks, remote work,
supply crisis): **586,408 emails** (5.8 %) relate to it. 484,073 emails
(4.8 %) are private or informal exchanges between colleagues. Single emails
are newsletters, memos, circulars, press releases and payment reminders;
system notifications come from the service desk, HR portal, accounts payable,
procurement, facilities and shipping.

### Who is writing?

| Group | Count | Examples |
|---|---|---|
| Sinabis Green Energy group | 7 companies, 16 sites, 11 business units, 21 departments | Inc. (USA), Japan K.K., Australia Pty, NZ Ltd, Shanghai Co., Middle East FZ-LLC, Ocean & Earth Foundation |
| Business customers and utilities | 188 + 29 | Cedar Mesa Municipal Utilities, Pacific Coast Utilities Board, Piedmont Power Co-op |
| Suppliers and subcontractors | 150 + 143 | Reclaimcraft Materials, Kauri Cable & Conduit, Polarbeam Glass & Insulation |
| Authorities and municipalities | 50 + 25 | Colorado Highlands Clean Power Authority, City of Tucson Community Power Office |
| Certifiers, insurers, consultants, law firms | 9 + 10 + 16 + 15 | Gridmark Testing & Certification, Seaway Marine & Property Insurance |
| NGOs, universities, media | 35 + 23 + 25 | Lone Star Agricultural University, Continental Press Wire |
| Politicians and their offices | 50 + 100 staff | USA 24, Japan 6, Australia 6, NZ 5, UAE 5, China 4 |
| Private persons | 4,950 residents and customers, 830 supporters, 300 landowners | |

Activity is **unevenly distributed**, like in a real mailbox: of 7,828
internal sender addresses, the busiest 10 % write 56.5 % of all internal
emails. People only appear during their period of employment; around their
leaving date there is a farewell email, an HR note or a handover, and after
that they never write again.

### Business units

| Unit | Emails | Share |
|---|---:|---:|
| Solar | 2,016,753 | 20.0 % |
| Corporate | 1,434,396 | 14.2 % |
| Charge | 1,100,095 | 10.9 % |
| Wind | 1,052,936 | 10.4 % |
| Mobility | 875,705 | 8.7 % |
| Buildings | 694,278 | 6.9 % |
| Water | 681,516 | 6.8 % |
| Storage | 606,146 | 6.0 % |
| Government Affairs | 580,871 | 5.8 % |
| Foundation | 559,763 | 5.5 % |
| Research | 486,455 | 4.8 % |

Threads refer to **2,883 projects** and **470 assets** (wind farms, solar
parks, charging parks, storage, water works, buildings, AV fleets) over
months: same numbers, same team, same customer.

## Language distribution

The language of each email is recorded in the manifest and in the
`Content-Language` header.

| Language | Emails | **Share** |
|---|---:|---:|
| English | 8,817,650 | **87.4 %** |
| Spanish | 887,504 | **8.8 %** |
| Japanese | 140,330 | 1.4 % |
| Chinese | 109,678 | 1.1 % |
| Arabic | 89,164 | 0.9 % |
| German | 6,634 | 0.1 % |
| Korean | 5,703 | 0.1 % |
| Hindi | 4,569 | < 0.1 % |
| Italian | 3,173 | < 0.1 % |
| French | 3,114 | < 0.1 % |
| Portuguese | 3,110 | < 0.1 % |
| 18 more (nl, pl, id, tr, ru, tl, vi, th, he, ro, nb, da, uk, el, sv, cs, hu, fi) | 18,285 | 0.2 % |
| **Total** | **10,088,914** | |

Every email is **monolingual**: subject, body, signature, disclaimer and
history header are all in the same language.

**Attachments by language**

| | PDF | DOCX | XLSX | Images |
|---|---:|---:|---:|---:|
| English | 1,026,458 | 417,334 | 403,198 | 96,395 |
| Spanish | 116,470 | 46,390 | 33,368 | 10,293 |
| Japanese | 4,247 | 18,439 | 5,193 | 1,506 |
| Chinese | 3,407 | 15,575 | 3,940 | 1,061 |
| Arabic | 3,458 | 6,977 | 3,755 | 839 |
| Others | 4,325 | 2,805 | 1,535 | 208 |

## Models used

The model that wrote each email is recorded in `manifest.jsonl`
(fields `model` and `worker`).

| Model | Emails | Share |
|---|---:|---:|
| Gemma 4 26B-A4B (NVFP4) | 6,214,888 | 61.6 % |
| Qwen3.6-35B-A3B (AWQ, 4-bit) | 3,045,491 | 30.2 % |
| DeepSeek V4 Flash | 15,113 | 0.1 % |
| Qwen 3.6 / Qwen3.5-9B | 6,589 | 0.1 % |
| **no LLM**, rule-based (system notifications) | 806,833 | 8.0 % |

Across both runs the models read 4.75 billion and wrote 4.40 billion tokens.
These totals also include the small share spent on the calendar emails that
are not part of this folder. For rule-based emails the `model` field names
the worker that handled the case, but no language model was involved. The
`.ics` files are built by rules, without a model.

The PDF, DOCX and XLSX attachments are real files. Invoices, quotes,
purchase orders and measurement reports are built without a model, with
correct totals and the same numbers as in the email text; contracts, terms
and conditions, reports and studies get their text from the model. The PNG
attachments are charts, trend plots and screenshots rendered by the
generator, plus a small number of photos from an image model.

## Downloads

The dataset is split into nine zip archives (about 101 GB zipped, about
187 GB unpacked including the manifests; the `.eml` files alone are 177.8 GB),
so you can start with a single part and do not need to fetch everything at
once.

| Archive | Size | Contents |
|---|---:|---|
| `Sinabis_10M_emails_part_01.zip` | 15.88 GB | `emails/` case folders, part 1 of 8 |
| `Sinabis_10M_emails_part_02.zip` | 16.15 GB | `emails/` case folders, part 2 of 8 |
| `Sinabis_10M_emails_part_03.zip` | 12.38 GB | `emails/` case folders, part 3 of 8 |
| `Sinabis_10M_emails_part_04.zip` | 11.39 GB | `emails/` case folders, part 4 of 8 |
| `Sinabis_10M_emails_part_05.zip` | 11.27 GB | `emails/` case folders, part 5 of 8 |
| `Sinabis_10M_emails_part_06.zip` | 11.23 GB | `emails/` case folders, part 6 of 8 |
| `Sinabis_10M_emails_part_07.zip` | 11.08 GB | `emails/` case folders, part 7 of 8 |
| `Sinabis_10M_emails_part_08.zip` | 10.67 GB | `emails/` case folders, part 8 of 8 |
| `Sinabis_10M_ics.zip` | 971.7 MB | `ics/`: 1,420,492 `.ics` files |

The eight email parts hold the `emails/sNNNNN/` case folders in ascending
order, each folder with its `manifest.jsonl`. To get the complete tree, unpack
all archives into the same directory (on Windows and macOS, merge the folders
when asked). Every archive also works on its own.

```bash
# try one part first
hf download sinabis-group/sinabis-10m-synthetic-emails \
  Sinabis_10M_emails_part_01.zip --repo-type dataset --local-dir .
unzip -q Sinabis_10M_emails_part_01.zip

# or fetch and unpack everything
hf download sinabis-group/sinabis-10m-synthetic-emails \
  --repo-type dataset --local-dir sinabis-10m
cd sinabis-10m && for z in *.zip; do unzip -q "$z"; done
```

## Folder structure

In the repository:

```
.
├── README.md
├── Sinabis_10M_emails_part_01.zip … part_08.zip    → emails/
└── Sinabis_10M_ics.zip                             → ics/
```

After unpacking all archives into one directory:

```
.
├── emails/                 10,088,914 .eml
│   ├── s00000/
│   │   ├── 000000000-01.eml
│   │   ├── …
│   │   └── manifest.jsonl
│   ├── …
│   └── s04040/
└── ics/                    1,420,492 .ics
    ├── s00000/
    │   ├── 000000001-01.ics
    │   └── …
    ├── …
    └── s04040/
```

The `sNNNNN` folders hold 1,000 business cases each and only split the data so
that no single folder holds millions of files. They carry no meaning. An
`.ics` file lives in the folder with the same `sNNNNN` name as its case.

Each `emails/sNNNNN` folder contains a `manifest.jsonl` with one line per
file: file, date, sender, recipients, subject, kind (`thread`, `single`,
`meeting`, `notification`, `lifecycle`), language, topic, business unit,
site, project, asset, counterparty, attachments, COVID flag and model.

> **Manifest note:** The manifests were not rewritten when the folder was
> reorganised. Besides the 10,088,914 lines for the emails here they still
> contain 1,236,641 lines for the calendar emails that were moved out, and
> 183,851 lines for the `.ics` files of run 2 (`"format": "ics"`, path
> `emails/sNNNNN/…ics`, the file is now in `ics/sNNNNN/`). Only count lines
> whose file exists.

## How everything is linked

### Email threads

```
<case>-<NN>.eml
 │      └── position in the thread (01, 02, …)
 └───────── 9-digit case number, same for all emails of the case
```

- All emails of one case share the **same file name prefix**.
- The headers link the emails: `Message-ID`, `In-Reply-To` and `References`
  each point to the previous email.
- Every email contains the **quoted history** of all earlier emails, either
  in Outlook style or `>` style depending on the sender's mail client, so a
  single file already shows the whole thread.
- 1,166,273 first emails (31.8 % of all first emails) also carry an HTML
  version (`multipart/alternative`).
- 99.7 % of threads have **2 to 8 emails**, 77.5 % have 3 to 6.
- **Gaps:** In 16,943 threads of run 1 a position is missing, because that
  email contained a meeting invitation and was moved out with the other
  calendar emails (not part of this release).

### Attachments

- Attachments are **embedded in the email** (MIME, Base64), not stored as
  separate files next to it. 2,075,531 emails (20.6 %) carry at least one.
- The document is the **source the email refers to**, for example an invoice,
  a maintenance report or a contract draft, not a copy of the email text. It
  has the same language and the same date as the email.
- No email in `emails/` contains a `text/calendar` part or an `.ics`
  attachment.
- Meeting links (`meet.sinabis-green.com`) and team sites
  (`teams.sinabis-green.com`) in the text are fictional.

### Meetings and calendar files (`ics/`)

```
ics/sNNNNN/<case>-<NN>.ics
```

- A meeting consists of **several `.ics` files** with the same case number:
  the invitation (`REQUEST`) to all attendees, acceptances or declines
  (`REPLY`) to the organiser, and possibly an update or cancellation
  (`CANCEL`). 322,673 meetings produce 1,269,964 files this way, 3.9 per
  meeting on average.
- The remaining 150,528 files are invitations that came up **inside an email
  case** (110,332 from threads, 40,196 from single emails).
- Where the files come from:

| Source | Files | Matching email |
|---|---:|---|
| Run 1, extracted from the `text/calendar` part of the calendar emails | 1,236,641 | not part of this release (the calendar emails were moved out) |
| Run 2, meeting invitations written directly as `.ics` | 164,238 | none, there never was an email |
| Run 2, invitations at the end of a thread or single email | 19,613 | `emails/sNNNNN/<same name>.eml` |

- The files use CRLF line endings, `METHOD`, `UID`, `ORGANIZER` and
  `ATTENDEE`, so they can be imported directly into calendar software.

## How timestamps are created

Timestamps are set **by the generator, not by the language model**.

1. **Start time:** For each case the generator picks a day between
   1 Jan 2016 and 30 Jun 2026 and a time within office hours. The number of
   cases per year grows with the workforce.
2. **Thread:** Replies always come after the previous email, with plausible
   gaps between them.
3. **Time zones:** The `Date` header is in the **sender's local time zone**,
   including daylight saving time (e.g. `-0500` in Houston, `+0900` in Tokyo,
   `+1200`/`+1300` in Auckland).
4. **People:** Every person has an employment or business-relationship
   window. Someone hired in 2024 does not send emails in 2019.
5. **Time-bound topics:** Topics such as COVID-19 (2020–21) or the supply
   crisis (2021–22) only appear in their period.
6. **Attachments** carry the date of their email.

**Emails per year** (local date of the `Date` header)

| 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 (to July) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 543,229 | 625,167 | 713,299 | 792,423 | 882,984 | 981,067 | 1,067,436 | 1,160,651 | 1,260,646 | 1,344,175 | 717,834 |

## Notes

- **Fictional, and recognisably so:** All names, companies, addresses, phone
  numbers, authorities, programmes, laws, politicians and events are made up.
  External domains use the reserved TLD `.example`, authorities
  `*.gov.example`; phone numbers are in the fictional `555-01xx` range.
  Laws and programmes carry recognisably invented names such as
  "Windbreak Jobs Act (H.R. 48812)". Real cities appear as locations only.
- **Fake filter:** After every generation step a filter replaces real brands,
  authorities, laws, politicians, celebrities, universities and media, and
  rewrites any real domain to `.example`.
- **Marked as synthetic:** All 10,088,914 `.eml` files carry the header
  `X-Synthetic-Data: fictional`.
- **Watchdog:** Every written email was decoded and checked for foreign
  scripts (e.g. Chinese characters in English emails), placeholders such as
  `[Your Name]`, model artefacts and real names. Failing cases were
  regenerated.
- **Edge dates:** 3 emails are dated 31 December 2015 (local time) because of
  time zone shifts at the start of the time span; the latest email is from
  12 July 2026.
- **Manifest duplicates:** 38 manifest lines are repeated entries from cases
  that were regenerated; the `.eml` file exists only once.

## Methodology

The prompt templates, topic catalogue, world definition and fake filter
(`prompts.json`, `topics.json`, `world.json`, `guard.json`) were used to
prompt the LLMs; they are not part of this release. The company world is
generated deterministically from seed 7.

## License

This dataset is released under **CC BY 4.0**. You may copy, modify,
distribute and use it for any purpose, including commercially, as long as
you give appropriate credit, for example:

> Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Email Dataset.
> https://huggingface.co/datasets/sinabis-group/sinabis-10m-synthetic-emails

The email content was generated using Gemma 4 and Qwen 3.6 (open weights) and
DeepSeek V4 Flash. Generated text is treated as free of third-party rights;
the underlying models' own terms of use apply to the act of generation, not
to redistribution of this dataset.

## Citation

If you use this dataset, please cite it as:

```
Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Email Dataset.
https://huggingface.co/datasets/sinabis-group/sinabis-10m-synthetic-emails
```

BibTeX:

```bibtex
@misc{sinabis_green_email_dataset_2026,
  author = {{Sinabis GmbH}},
  title  = {Sinabis Green Energy -- Synthetic Email Dataset},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sinabis-group/sinabis-10m-synthetic-emails}
}
```
