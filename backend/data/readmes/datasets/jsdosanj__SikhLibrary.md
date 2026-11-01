---
license: cc-by-nc-nd-4.0
task_categories:
- text-generation
- fill-mask
language:
- pa
- en
- hi
- ur
- fa
- es
- fr
- de
- pt
- it
- zh
- ru
- bn
- gu
- ta
- te
- ja
- pl
- nl
- sv
- ro
- cs
- hu
- da
- ko
- ms
tags:
- sikh
- gurbani
- religion
- punjabi
- research
- librarian
- nlp
- text-corpus
- multilingual
- scripture
- open-source
- historical
- philosophical
- spiritual
- dictionary
- encyclopedia
- lexicon
- mahan-kosh
- translation
pretty_name: The Universal Sikh Research Library (1B+ Words)
---

<div align="center">

# 🪯 SikhLibrary
### A Universal, Comprehensive Research Corpus for the Sikh Community

*ਵਾਹਿਗੁਰੂ ਜੀ ਕਾ ਖਾਲਸਾ ਵਾਹਿਗੁਰੂ ਜੀ ਕੀ ਫ਼ਤਿਹ ਜੀ*

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/jsdosanj/SikhLibrary)
![Words](https://img.shields.io/badge/Words-1.07B%2B-success)
![Files](https://img.shields.io/badge/Files-23%2C366-blue)
![Size](https://img.shields.io/badge/Size-14.2%20GB-blue)
![Languages](https://img.shields.io/badge/Languages-26-blue)
![Sources](https://img.shields.io/badge/Named%20Author%20Archives-86-blueviolet)
![Version](https://img.shields.io/badge/Version-3.1-informational)
![Status](https://img.shields.io/badge/Largest%20Known-Open%20Sikh%20Text%20Corpus-critical)

**Production home:** [sikhi.io](https://sikhi.io) &nbsp;·&nbsp; **Planned backend for:** [sikharchive.net](https://sikharchive.net)

</div>

---

## 📖 Overview

**SikhLibrary** centralizes Sikh scripture, exegesis, history, and scholarship — scanned, OCR'd, and machine-readable — into a single, standardized research corpus. It exists so that Sikh scholars, students, and AI/NLP researchers no longer have to hunt across dozens of scattered archives, out-of-print books, and regional digital libraries to find primary source material.

This is a **living, actively-maintained dataset**. Every release is documented in the [Version History](#-version-history) below, and every identifiable source and copyright holder in the corpus is disclosed in [License, Copyright & Attribution](#-license-copyright--attribution) — not just the top-level license, but the actual publishers, digitizers, and rights-holders found printed inside the scanned works themselves.

If you are a researcher, educator, or developer working on Sikh studies, Gurmukhi NLP, or Punjabi-language AI, this dataset is built for you.

### Table of Contents
- [At a Glance](#-at-a-glance)
- [Why This Is the Largest Open-Source Sikh Dataset](#-why-this-is-the-largest-open-source-sikh-dataset)
- [What This Dataset Provides](#-what-this-dataset-provides)
- [Directory Structure & Statistics](#-directory-structure--statistics)
- [Version History](#-version-history)
- [License, Copyright & Attribution](#-license-copyright--attribution)
- [How to Load](#-how-to-load)
- [Data Quality & Known Limitations](#-data-quality--known-limitations)
- [Future Collaboration & Contributions](#-future-collaboration--contributions)
- [Acknowledgements & Gratitude](#-acknowledgements--gratitude)
- [Companion / Upstream Repositories](#-companion--upstream-repositories)
- [How to Cite](#-how-to-cite)
- [Contact & Maintainers](#-contact--maintainers)

---

## 📊 At a Glance

| | |
| :--- | :--- |
| **Total word count** | ~1.07 billion (independently re-verified, Sept 2026 — see [methodology](#-data-quality--known-limitations)) |
| **Total size** | ~14.2 GB |
| **Total files** | 23,366 |
| **Distinct works** | 3,616+ individually catalogued books, manuscripts, and tracts |
| **Top-level collections** | 115 (86 named author/scholar archives + 29 thematic/scriptural collections) |
| **Languages** | 26 declared (`pa`, `en`, `hi`, `ur`, `fa`, `es`, `fr`, `de`, `pt`, `it`, `zh`, `ru`, `bn`, `gu`, `ta`, `te`, `ja`, `pl`, `nl`, `sv`, `ro`, `cs`, `hu`, `da`, `ko`, `ms`), plus Gurmukhi- and Shahmukhi-script editions inside the Mahan Kosh sub-corpus |
| **Primary formats** | Clean UTF-8 `.txt`, structured OCR `JSON`, `JSONL` |
| **License** | [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) (one folder under CC BY 4.0 — see below) |
| **Access** | Gated (free — request access on the [dataset page](https://huggingface.co/datasets/jsdosanj/SikhLibrary)) |
| **Current version** | 3.1 (September 16, 2026) |

---

## 🏆 Why This Is the Largest Open-Source Sikh Dataset

As of September 2026, a systematic search of Hugging Face's public and gated datasets for `sikh`, `gurbani`, and `punjabi` found no other open text corpus at this scale dedicated to the Sikh community. Every comparable result was either:

- an audio/ASR corpus (kirtan or sehaj-path transcription), not a text-scholarship corpus;
- a question-answering or classification set of a few hundred to a few thousand rows; or
- a single-work extract (e.g., a Mahan Kosh-only corpus).

SikhLibrary is, to our knowledge, the only Sikh-focused corpus spanning **~1.07 billion words, 3,616+ distinct works, 115 author/source collections, and 26+ languages** in one place — larger by orders of magnitude than anything else tagged for this community on the Hub.

**We are not claiming this lightly, and we want to be proven wrong if we are:** if you know of a larger open-source Sikh-community text corpus, please open a [Discussion](https://huggingface.co/datasets/jsdosanj/SikhLibrary/discussions) — we will verify it and correct this claim.

---

## 📚 What This Dataset Provides

- **Primary scripture** — Sri Guru Granth Sahib, Sri Dasam Granth, Sri Sarbloh Granth, and Nitnem banis, including multilingual translations.
- **Exegesis & commentary (Teekas/Steeks)** — word-by-word meanings and classical commentaries, including Guru Granth Sahib Darpan (Prof. Sahib Singh), the Faridkot Wala Teeka, and dozens of others.
- **The complete Mahan Kosh** — Bhai Kahan Singh Nabha's *Gurushabad Ratnakar Mahan Kosh* (1930), the great Sikh encyclopedia-dictionary, as structured JSON across 28 language/script editions sharing one entry ID.
- **86 dedicated single-author archives** — the collected works of named Sikh scholars, historians, theologians, and saints (Bhai Vir Singh, Prof. Sahib Singh, Giani Sant Singh Maskeen, Dr. Ganda Singh, and 82 others), plus several Western/colonial-era chroniclers.
- **Historical chronicles & colonial-era ethnographies** — Punjab gazetteers, colonial administrative records, and 19th–20th century Western scholarship on the Sikhs.
- **Reference & discourse corpora** — a combined Punjabi dictionary (87,636 entries), katha transcripts (1,179 recordings), a katha-terms glossary, sakhi stories, and detailed per-Guru biographical pages.
- **Academic literature** — theses, dissertations, and peer-reviewed monographs on Sikh history, theology, and identity.

Every item above is traceable to a real top-level folder in the repository — see the next section.

---

## 🗂️ Directory Structure & Statistics

The repository is organized **folder-per-collection**, with most individual works further split into `<Title>_english/` and `<Title>_gurmukhi/` subfolders, each holding an `extracted_text.txt` (or `translated_text.txt`) plus a matching structured `extracted_pages.json`.

### Core scripture, exegesis & reference

| Folder(s) | Content |
| :--- | :--- |
| `Primary Scripture`, `Gurbani`, `Granths` | Sri Guru Granth Sahib, Dasam Granth, Sarbloh Granth, and the Mahan Kosh (incl. `Granths/Mahan_Kosh_Multilingual/`, the 28-language edition) |
| `Steeks`, `Steeks & Teekas`, `Reference and Dictionary`, `Reference` | Exegesis, word-by-word meanings, and classical/modern commentaries |
| `Daily Prayers`, `Puratan Rehatnamas`, `Aad Dasam Sarabloh Gutka Sahibs`, `Aad Dasam Sarabloh Saroop te Bhaag`, `Aad Dasam Sarabloh Steek` | Nitnem gutkas, codes of conduct, and Dasam/Sarbloh Granth editions & commentary |

### The 15 largest collections by file count

| Rank | Folder | Files |
| :--- | :--- | ---: |
| 1 | Punjabi Literature | 5,934 |
| 2 | Research | 3,419 |
| 3 | English Literature | 2,301 |
| 4 | Historical Chronicles | 1,416 |
| 5 | Literature | 1,018 |
| 6 | English Thesis Papers | 807 |
| 7 | Bhai Vir Singh | 778 |
| 8 | Unknown Authors | 462 |
| 9 | Steeks & Teekas | 402 |
| 10 | Aad Dasam Sarabloh Gutka Sahibs | 367 |
| 11 | Spirituality | 366 |
| 12 | Giani Sant Singh Maskeen | 300 |
| 13 | Academic Literature | 279 |
| 14 | Gurbani | 275 |
| 15 | Granths | 264 |

*(As of the September 2026 reorganization described in [Version History](#-version-history) — the former catch-all "General" folder no longer exists; its 730 works were redistributed above by actual content.)*

### Full index of the 115 top-level collections

<details>
<summary><strong>86 named authors, scholars, saints & historians</strong> — click to expand</summary>

Abinash Mahapatra · Akali Kaur Singh · Baba Gajjan Singh Tarna Dal · Baba Ganesha Singh Bedi · Baba Prem Singh Hoti Mardan · Baba Sumer Singh · Bhagat Jaswant Singh Daudar DDT · Bhai Chaupa Singh · Bhai Desa Singh · Bhai Hira Singh Dard · Bhai Joginder Singh Talwara · Bhai Kahn Singh Nabha · Bhai Raghbir Singh Bir · Bhai Rama Singh UK · Bhai Randhir Singh Narangwal · Bhai Sohan Singh Sital · Bhai Surinder Singh Kohli · Bhai Vir Singh · C.F. Massy · Dorothy Field · Dr Ajit Singh Alaukh · Dr Darshan Singh · Dr Ganda Singh · Dr Gurcharan Singh Alaukh · Dr Gurcharan Singh Mehta · Dr Jagjit Singh Kanpuri · Dr Kamalroop Singh · Giani Bishan Singh · Giani Ditt Singh · Giani Gian Singh · Giani Gurbachan Singh Bhindranwale · Giani Gurdit Singh · Giani Gurvinder Singh Nangli · Giani Harbans Singh · Giani Jaswant Singh · Giani Kirpal Singh SGPC · Giani Mal Singh Darbar Sahib · Giani Nahar Singh AKJ · Giani Pritam Singh Likhari · Giani Sant Singh Maskeen · Giani Sher Singh SGPC · Griffin and Massy · Hari Ram Gupta · Harnam Daas Udasi · Hirdey Ram · Hutchison and Vogel · Kavi Santokh Singh · Lala Sri Ram · Lepel Griffin · Mahant Amir Singh Mukatsar · Mahant Ganesha Singh · Mahant Sadhu Singh · Max Arthur Macauliffe · Meharban Singh Sodhi · Pandit Giani Nairayan Singh Lahore · Pandit Gobind Singh · Pandit Gulab Singh Nirmala · Pandit Ishar Singh Kanshi · Pandit Kartar Singh Dakha · Pandit Tara Singh Narotam · Prof Sahib Singh · Pyara Singh Padam · Raja Mrigend Singh · Sant Hari Singh Randhawa · Sant Jagjit Singh Harkhowal · Sant Jodh Singh Rishikesh · Sant Kartar Singh Nirmala · Sant Kirpal Singh Sato Gali · Sant Makhan Singh Sato Gali Taksal · Sant Nihal Singh Nirmala · Sant Seva Singh Rampur Khera · Sant Seva Singh Sevapanthi · Sant Surjit Singh Sevapanthi · Sant Tehil Singh · Sant Waryam Singh Ratwara Sahib · Seeta Ram Tandon · Sodhi Teja Singh · Sohan Lal Suri · Subedar Baghel Singh · Swami Ram Singh Nirmale · Swami Rama · Swaran Singh Virk · Tapoban Sahib · W.H. McLeod · William Crooke · Yogi Bhajan

</details>

<details>
<summary><strong>29 thematic & scriptural collections</strong> — click to expand</summary>

Aad Dasam Sarabloh Gutka Sahibs · Aad Dasam Sarabloh Saroop te Bhaag · Aad Dasam Sarabloh Steek · Academic Literature · Academic Research · Additional Granths attributed to Guru Sahib · Bhagavad Gita · Colonial Sikh History · Daily Prayers · English Literature · English Thesis Papers · Granths · GurBilas Paatshahi 6 and 10 · Gurbani · Hindi Literature · Historical Chronicles · Literature · Primary Scripture · Punjabi Literature · Puratan Rehatnamas · Reference · Reference and Dictionary · Research · Sampardai Bhindera · Spirituality · Steeks · Steeks & Teekas · Unknown Authors · Vedant Literature

</details>

---

## 🕐 Version History

| Version | Date | Files | Δ Files | What changed |
| :--- | :--- | ---: | ---: | :--- |
| **2.0** — *Initial Public Release* | 2026-03-30 | 626 | — | First publication on Hugging Face. Note: the project's own first release was already versioned "2.0" — no separate v1.0 was ever published here. Five core folders (Gurbani, Steeks, Granths, Literature, Research); 758,354,306 words self-reported at the time. Licensed **CC BY 4.0** at launch. |
| **2.0** — *License tightened* | 2026-04-12 | — | — | License changed from CC BY 4.0 to the current, more conservative **CC BY-NC-ND 4.0**, less than two weeks after launch. |
| **2.0** — *The Grand Literary Expansion* | 2026-05-30 | 5,629 | +5,003 | The largest single restructuring to date: transformed the repository from a small core-scripture database into a library of individual named-author archives, using an OCR/extraction pipeline built on OpenRouter (Gemini 1.5 Flash-Lite, Gemma 4 31B). |
| **2.1** — *Multilingual Scripture & Reference Expansion* | 2026-08-28 | 9,899 | +4,270 | Back-filled ~1.2 GB from the sikhi.io/sikharchive.net production database: Dasam Granth in 12 languages, Sarbloh Granth in 12 languages, Faridkot Wala Teeka in 7 languages, full-text OCR for Sri Gur Pratap Suraj Granth (11,180 pages) and eight other steeks/granths, ~45 additional colonial-era and historical books, plus reference/discourse corpora (Punjabi dictionary, katha transcripts, sakhi stories, per-Guru biographies). |
| **3.0** — *The Mahan Kosh Multilingual Expansion* | 2026-09-03 | 9,977 | +78 | Mirrored the complete [redroyals/mahan-kosh-multilingual](https://github.com/redroyals/mahan-kosh-multilingual) project (Sikhi.io): Bhai Kahan Singh Nabha's *Mahan Kosh* as structured JSON, 64,218 entries × 28 language/script editions, ~723 MB, released in honour of Guru Tegh Bahadur Ji's 350th year of sacrifice. |
| **3.1** — *The Production Library Sync & Copyright Audit* | 2026-09-10 → 2026-09-16 | 23,366 | +13,389 | A 66-batch automated sync from the sikhi.io production database added 2,475 new works. Followed by a full documentation overhaul: independently re-verified word count (~1.07B, replacing the long-stale self-reported figure), a corpus-wide structural + content-level copyright audit, and a complete named-author/source attribution index. |
| **3.1** — *General Folder Reorganization* | 2026-09-16 | 23,366 | 0 (moves only) | The generic catch-all "General" folder (4,380 files / 730 works) was eliminated. Each work's front matter was actually read by an LLM classification pass (not filename matching, which was tried first and rejected — see below) and routed into an existing named-author folder (138 works, byline-confirmed) or the best-fitting existing thematic folder (592 works); 1 genuinely indeterminate fragment went to "Unknown Authors." Executed as 4,380 server-side file moves; 3 title collisions with pre-existing content were disambiguated rather than overwritten. Also fixed 3 pre-existing folder-name inconsistencies (two trailing-space duplicates, one misspelling: "Maucliffe" → "Macauliffe") discovered during the move, merging ~400 further files into their correct canonical folder. Top-level collection count: 116 → 115. |

Word counts prior to v3.1 were self-reported at each release and, as this audit discovered, were never recomputed after the 2026-05-30 and 2026-08-28 expansions — meaning the "808,354,306" figure quoted through early September 2026 undercounted the true corpus substantially. The ~1.07 billion figure now shown is independently measured; see [Data Quality & Known Limitations](#-data-quality--known-limitations) for the method.

---

## ⚖️ License, Copyright & Attribution

### The license

This dataset is provided under **[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)** (Attribution–NonCommercial–NoDerivatives).

> **One exception:** `Granths/Mahan_Kosh_Multilingual/` is mirrored from an upstream project released under the more permissive **CC BY 4.0**. Its own `LICENSE` file is kept alongside the data at that path.

**You may:** download and share the files unmodified, and use them for personal study, academic research, and other non-commercial purposes.
**You may not:** modify the files; use any part of the dataset commercially; or redistribute a modified or derived version.

### The audit: what license & copyright information actually exists in this corpus

No structured license or rights *metadata* exists anywhere in the corpus outside the one `LICENSE` file above — we scanned all 23,366 filenames and every `manifest`/`metadata`/`source` JSON file, and the per-book JSON schema is limited to `pdf_name` and `pages`, with no rights field. **But most scanned books preserve their own original title and copyright page as OCR'd text**, so the underlying publisher, digitizer, or rights-holder is usually still recoverable from the work itself. Two passes were run against the live corpus (September 2026) to recover this:

1. **Filename-tag scan (exact, 100% coverage)** — many files carry their source as a literal `(Domain.com)` suffix in the filename.
2. **Front-matter content scan (~84% coverage)** — the first ~6,000 characters of all 10,799 `.txt` files were fetched and searched for publisher/copyright keywords (9,086 of 10,799 files were successfully retrieved; the rest were skipped, so the figures below are **lower bounds**).

| Source (as printed in the work) | Role | Works found |
| :--- | :--- | ---: |
| GurmatVeechar.com | digitization / hosting (in filename) | 509 *(exact)* |
| sikhi.io | production-library source tag (in filename) | 4 bulk archives *(exact)* |
| Punjabi University, Patiala (Publication Bureau) | original publisher | ≥358 |
| SGPC (Shiromani Gurdwara Parbandhak Committee) | original publisher | ≥194 |
| Panjab Digital Library (panjabdigilib.org) | digitizer | ≥158 |
| Bhai Vir Singh Sahit Sadan, New Delhi | copyright holder | ≥137 |
| Damdami Taksal | publisher / copyright holder | ≥78 |
| Sri Satguru Jagjit Singh Ji E-Library ("**Namdhari E-Library**," `NamdhariElibrary@gmail.com`) | digitizer | ≥40 |
| Language Department, Punjab | original publisher | ≥37 |
| Oxford University Press | copyright holder (modern academic monographs) | ≥32 |
| Human Rights Watch | copyright holder (modern reports — see caution) | ≥32 |
| Bhai Sahib Randhir Singh Trust | copyright holder | ≥26 |
| Internet Archive | digitizer | ≥23 |
| Google Books | digitizer | ≥20 |
| Guru Nanak Foundation, Bhatinda | copyright holder | ≥11 |
| ProQuest LLC / UMI Dissertation Publishing | copyright holder (doctoral dissertation) | ≥1 |

**Two of these are worth flagging explicitly**, since they sit outside the Sikh-publishing ecosystem and are unambiguously under active, modern copyright:
- **Oxford University Press** monographs by living scholars (Pashaura Singh, Harjot Oberoi) and Gurinder Singh Mann's *The Making of Sikh Scripture* (© 2001).
- **Human Rights Watch** — at least 32 of its own reports (2008–2012), each stamped "Copyright © [year] Human Rights Watch. All rights reserved." These are unrelated NGO publications filed under `English Literature`, not Sikh scripture or scholarship.

This is a *structural and textual* audit — what is actually printed or embedded in the files — not a legal opinion on underlying copyright status. For that, we suggest treating the corpus in three broad, non-exhaustive bands:

1. **Pre-1900s colonial-era chronicles** (William Crooke, Lepel Griffin, C.F. Massy, Hutchison and Vogel, Max Arthur Macauliffe) — old enough to be public domain by age alone in most jurisdictions; this dataset's transcription and compilation are still offered only under the NC-ND terms above.
2. **Early-to-mid 20th-century Sikh scholars** (e.g., Bhai Vir Singh, d. 1957; Prof. Sahib Singh, d. 1969) — likely public domain in India under its life+60 term, but status can differ by jurisdiction, so no blanket claim is made.
3. **Living authors, recent estates, and institutional publishers** (Yogi Bhajan/3HO, Swami Rama/Himalayan Institute, W.H. McLeod's estate, SGPC and Punjabi University Patiala editions, Oxford University Press, Human Rights Watch) — very likely still under active copyright. Included here as a research/archival mirror, offered only under non-commercial, no-derivatives terms **because** independent copyright cannot be presumed expired.

**If you are a rights-holder** (or represent one) for any work in this dataset and want it removed or relicensed, please open a [Discussion or Issue](https://huggingface.co/datasets/jsdosanj/SikhLibrary/discussions).

### Attribution requirement

Any use of this dataset must credit:
- **SikhLibrary** (`jsdosanj/SikhLibrary`) on Hugging Face
- **Contributing sources:** Sikhi.IO, ShabadOS, BaniDB, GurmatVeechar.com, SGPC, Sri Satguru Jagjit Singh Ji E-Library ("Namdhari E-Library"), Punjabi University Patiala (Publication Bureau), Panjab Digital Library, Language Department Punjab, Internet Archive, Google Books
- **For the Mahan Kosh multilingual data:** Bhai Kahan Singh Nabha, *Gurushabad Ratnakar Mahan Kosh* (1930); English after Punjabi University Patiala; packaged by Sikhi.io
- **For works bearing their own explicit copyright notice:** the named holder as printed in the scanned edition — e.g., Bhai Vir Singh Sahit Sadan, Damdami Taksal, the Bhai Sahib Randhir Singh Trust, the Guru Nanak Foundation (Bhatinda), Oxford University Press, or Human Rights Watch — see the table above
- **For any individual author's archive** (see the [full index](#full-index-of-the-115-top-level-collections)): the named author or their estate, in addition to the dataset itself
- **Project maintainers:** Bhai Jasvant Singh Panchhi (ਪੰਛੀ) & Sukhjeet Singh Sodhi, LLB (Hons)

---

## 💻 How to Load

Access is **gated but free** — request access on the [dataset page](https://huggingface.co/datasets/jsdosanj/SikhLibrary), then authenticate locally.

> **Note for `datasets` library users:** this repository is a raw, folder-per-work file tree (no dataset loading script or parquet export), so `datasets.load_dataset()` will not auto-parse it into rows — the Hub's Dataset Viewer shows this correctly as "0 rows." Use `snapshot_download` or the `hf` CLI below to pull the raw files, then parse the `.txt`/`.json` files directly for your use case.

### Python

```python
from huggingface_hub import snapshot_download

# Download the entire corpus (~14.2 GB) to a local directory
local_dir = snapshot_download(
    repo_id="jsdosanj/SikhLibrary",
    repo_type="dataset",
)

# Or download just one collection, e.g. the complete Mahan Kosh
local_dir = snapshot_download(
    repo_id="jsdosanj/SikhLibrary",
    repo_type="dataset",
    allow_patterns=["Granths/Mahan_Kosh_Multilingual/**"],
)
```

```python
from huggingface_hub import hf_hub_download

# Download a single file
path = hf_hub_download(
    repo_id="jsdosanj/SikhLibrary",
    repo_type="dataset",
    filename="Granths/Mahan_Kosh_Multilingual/data/entries/en.json",
)
```

### Shell

```bash
# Authenticate once (device-flow login)
hf auth login

# Download the entire corpus
hf download jsdosanj/SikhLibrary --repo-type dataset --local-dir ./SikhLibrary

# Download just one collection
hf download jsdosanj/SikhLibrary --repo-type dataset \
  --include "Bhai Vir Singh/**" --local-dir ./SikhLibrary
```

`git clone` also works, but this repository uses Git LFS for large files — install `git-lfs` first (`git lfs install`) or the clone will leave LFS pointer files instead of real content.

---

## 🔬 Data Quality & Known Limitations

- **Word count methodology:** the ~1.07 billion figure is not a raw exact count — recomputing every file exactly was impractical at this scale — but a **ratio estimator**: the words-per-byte ratio measured on a random sample of 1,500 of the 10,797 `.txt` files (135.8M sampled words / 1.27 GB sampled bytes) was applied to the exact total byte size of all `.txt` files (9.43 GB), giving **~1.01 billion words** (95% bootstrap CI: 940M–1,087M) for the plain-text corpus, **plus ~60.9 million words** independently measured by fully parsing six representative Mahan Kosh JSON files and applying that ratio to the folder's exact 723 MB size. This method was used deliberately in place of the historical self-reported figure (758M → 808M), which — as the [Version History](#-version-history) documents — was never recomputed after two major content expansions and had become substantially stale.
- **OCR artifacts:** most text was produced by an automated OCR/extraction pipeline (OpenRouter, Gemini and Gemma family models) and has not been manually proofread. Expect occasional misrecognized characters, broken diacritics, or page-break artifacts, especially in older scanned books.
- **Machine translation:** non-English, non-Gurmukhi language editions in the Mahan Kosh (25 of 28 languages) are machine translations of the English spine, not independent scholarly translations — do not cite them as Bhai Kahan Singh Nabha's own words. Korean and Malay were fidelity-audited in September 2026; the rest have not been.
- **Per-book JSON is not additional text:** each work's `extracted_pages.json` / `translated_pages.json` mirrors its sibling `.txt` file's content in a paginated structure — it is not independent text and was excluded from the word-count estimate to avoid double-counting.
- **The copyright audit is a lower bound, not a ceiling:** the front-matter scan covered ~84% of `.txt` files (9,086 of 10,799); the true prevalence of each named source is at least as high as reported above.
- **Sampled-value tags need double-checking**, not blind trust: thematic folders like "Historical Chronicles," "Research," or "Unknown Authors" mix material from many different original sources and copyright statuses — check the specific work's own front matter before assuming a folder-wide license status. Folder placement for the 730 works reclassified out of the former "General" bucket (see [Version History](#-version-history)) was assigned by an LLM reading each work's actual front matter, not by filename pattern-matching — high-precision but not infallible.

---

## 🤝 Future Collaboration & Contributions

This is a living dataset, actively synced from the sikhi.io / sikharchive.net production pipeline. We believe Sikh knowledge should be open and accessible to all.

- **Continuous updates:** processing pipelines will keep adding `.txt` and `JSON` data as new manuscripts are localized and verified.
- **Call for collaboration:** Panthic organizations, scholars, and developers are invited to contribute raw scans, new translations, unmapped historical teekas, or linguistic corpora — every contribution directly fuels the preservation effort at sikharchive.net.
- **Corrections & rights concerns:** if you find an error in a text, want to contribute data, or are a rights-holder with a licensing concern, please open an [Issue or Discussion](https://huggingface.co/datasets/jsdosanj/SikhLibrary/discussions) on this repository.

---

## 🙏 Acknowledgements & Gratitude

This project is a culmination of decades of work by many organizations and individuals dedicated to digital preservation. We offer our deepest gratitude to:

- **Sache Paatshaah** — for providing the strength, resources, and vision to perform this seva.
- **Sukhjeet Singh Sodhi, LLB (Hons), of Sikhi.io** — for the vast archive of digitized texts and translations that forms the bulk of this corpus, and for the proprietary tools and methodology behind the OCR/extraction pipeline.
- **ShabadOS & BaniDB** — for the structured Gurbani data and indexing that underlies much of the modern Sikh app ecosystem.
- **Bhai Kahan Singh Nabha & Punjabi University, Patiala (Publication Bureau)** — for the Mahan Kosh, its English edition, and hundreds of other critical editions found throughout this corpus.
- **Sri Satguru Jagjit Singh Ji E-Library ("Namdhari E-Library")** — for digitizing and freely sharing dozens of rare Sikh manuscripts.
- **Panjab Digital Library, the Internet Archive, and Google Books** — for independent digitization efforts whose scanned imprints appear throughout this corpus.
- **The SGPC, the Language Department of Punjab, Bhai Vir Singh Sahit Sadan, Damdami Taksal, the Bhai Sahib Randhir Singh Trust, and the Guru Nanak Foundation, Bhatinda** — as original publishers or copyright holders of works mirrored here.
- **The 86 named scholars, saints, and historians** in the [directory index](#full-index-of-the-115-top-level-collections) above, and their estates and institutions, whose life's work forms the bulk of this library.
- **Panthic organizations & digitizers everywhere** — past and present — who have labored to scan, type, and verify these historical records.

---

## 🔗 Companion / Upstream Repositories

- **[redroyals/mahan-kosh-multilingual](https://github.com/redroyals/mahan-kosh-multilingual)** (GitHub, by [Sikhi.io](https://sikhi.io)) — the canonical, actively-maintained home of the multilingual Mahan Kosh mirrored into this dataset at `Granths/Mahan_Kosh_Multilingual/`. Carries a live search viewer (`sikhi.io/dictionary`) and is where corrections, recovered Gurmukhi bodies, and real human translations should be contributed. The older English/Hindi-only Mahan Kosh text dump remains here under `Granths/Mahan_Kosh_Dictionary/`.

---

## 📝 How to Cite

If you use this dataset in academic work, please cite it as:

```bibtex
@misc{sikhlibrary2026,
  title        = {SikhLibrary: A Universal Comprehensive Research Corpus},
  author       = {Jasvant Singh and Sukhjeet Singh Sodhi, LLB (Hons)},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/jsdosanj/SikhLibrary}},
  note         = {Version 3.1}
}
```

And per the [Attribution requirement](#attribution-requirement) above, credit the specific original source(s) for any individual work you use.

---

## ✉️ Contact & Maintainers

- **Bhai Jasvant Singh Panchhi (ਪੰਛੀ)** — Project Maintainer
- **Sukhjeet Singh Sodhi, LLB (Hons)** — Sikhi.io, data & methodology

For corrections, contributions, or rights concerns, please use the [Discussions](https://huggingface.co/datasets/jsdosanj/SikhLibrary/discussions) tab on this repository.

---

## 🗄️ sikhi.io D1 export (`sikhi-io-d1/`)

Added 2026-10-29: 55 public content tables (6,080,005 rows) exported from the Cloudflare D1 databases behind sikhi.io (gurbani-search, sikhi-colonial-archive, sikhi-gurbani, sikhi-io-prod, sikhi-scripture, sikhi-search, sikhidb), as Parquet (zstd) + JSONL.gz with Gurmukhi text unchanged. This includes the **Faridkot Wala Teeka** exegesis shown on sikhi.io/exegesis (`sikhi-io-d1/sikhi-scripture/scripture_pages.*`, `text = 'faridkot'`), katha transcripts and glossary, SGGS multilingual pages, Mahan Kosh, Punjabi dictionary, library pages and search corpora. No user, account or analytics data is included. See [`sikhi-io-d1/README.md`](sikhi-io-d1/README.md) and [`sikhi-io-d1/manifest.json`](sikhi-io-d1/manifest.json) for per-table row counts and sources.
