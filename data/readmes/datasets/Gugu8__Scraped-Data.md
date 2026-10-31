---
license: other
license_name: odatl-1.0
language:
  - en
  - de
  - fr
  - ru
  - es
  - it
  - ja
  - zh
  - pt
  - ar
  - fa
  - tr
  - pl
  - nl
  - id
  - ko
  - vi
  - uk
  - ca
  - hu
  - fi
  - cs
  - ro
  - sv
size_categories:
  - 1M<n<10M
task_categories:
  - text-generation
  - feature-extraction
tags:
  - wikipedia
  - corpus
  - cleaned
  - pretraining
  - internet-archive
  - gutenberg
pretty_name: Scraped-Data — 1TB in Progress
---

# Scraped-Data — Building to 1 TB

A continuously-growing, cleaned text corpus scraped, parsed, cleaned,
**losslessly-zipped**, and auto-pushed from a CPU-only Google Colab pipeline.

**Current repo size: ~26 GB → target: 1 TB** (incremental batch uploads).

## Current files

| File | Size | Contents |
|---|---|---|
| `corpus_batch1.clean.zip` | 4.80 GB | ~2.9M Wikipedia docs (stored, from first scrape) |
| `corpus_batch2.clean.zip` | 4.85 GB | ~2.5M docs |
| `corpus_batch3.clean.zip` | 4.91 GB | ~2.3M docs |
| `corpus_batch1.v3.zip` | 4.37 GB | de-wiki shards, deflate-level-6 |
| `corpus_batch2.v3.zip` | 3.74 GB | fr + ru shards |
| `corpus_batch3.v3.zip` | 3.45 GB | es + ru shards |
| `manifest.jsonl` | — | durable dedup ledger (zip → bytes → source keys) |

Next batches are pushed live as they finish. Total so far: **26.1 GB** compressed,
~8.8M+ records (+ additional Gutenberg/IA batches incoming).

> **Live status:** batch 4 scraping (2.5 min in, ~3.1 GB raw, ~748k docs).
> The Colab scraper runs continuously: ~10.6 GiB raw per batch → losslessly zipped
> (ZIP_DEFLATED, level 6, allowZip64), uploaded immediately via `huggingface_hub`,
> with a manifest for cross-VM resume.

## Sources

- **Wikipedia** — official `wikimedia/wikipedia` `20231101` parquet shards (HF mirror
  of Wikimedia dumps); mirror `mirror.accum.se` as fallback. Multi-language
  priority queue: de, fr, ru, es, it, ja, zh, pt, ar, fa, tr, pl, nl, id, ko,
  vi … (300+ configs; enwiki is only one shard of the total).
- **Internet Archive** — `collection:gutenberg` (public-domain plain-text books)
  via `advancedsearch` + `metadata` + `archive.org/download` — polite
  `IA_CONCURRENCY=20`, per-host pacing, robots-friendly.

Both pipelines emit the same JSONL record format and feed the same batch/zip
loop.

## Record schema (JSONL, one object per line)

```json
{"src": "wiki", "url": "https://...", "title": "...", "chars": 1234, "text": "..."}
{"src": "ia",   "url": "https://archive.org/details/...", "title": "...", "chars": 1234, "text": "..."}
```

- `src` — `wiki` or `ia`
- `url` — canonical article/item URL
- `title` — title trimmed
- `chars` — character count of `text`
- `text` — cleaned plain-text body

## Cleaning pipeline

1. Segmented parallel HTTP of source shards (`SEGMENTS=10`, `SEGMENTS=10` for
   parquet, 8 concurrent `archive.org` fetches)
2. Multi-process (2× fork) decode: `pyarrow`/`orjson` for parquet, streaming
   `bz2` for legacy dumps, plain-text for IA
3. Per-record `clean_wiki` / IA Gutenberg-header strip:
   - Gutenberg header/footer carve (`*START…*END*`), tab/NBSP→space,
     CRLF normalization, control-char strip, blank-run collapse,
     email redaction (`[email]`)
   - Min-length gates: `MIN_TEXT_LEN=300`, `MIN_DOC=280`
   - Exact-duplicate removal per batch (title+URL `blake2b-12`)
4. Batch-shard JSONL → ZIP (deflated level 6, `allowZip64`), immediate
   `HfApi.upload_file` + manifest append + manifest re-upload for resume

All ZIPs are **lossless** (`ZIP_DEFLATED` is LZ77+Huffman — perfectly
reversible).

## Provenance & attribution

- Underlying Wikipedia articles © their contributors, dual-licensed
  CC-BY-SA/GFDL.
- Underlying IA Gutenberg texts are public domain (U.S.).
- This compilation and its cleaned artifacts are additionally distributed
  under **ODATL-1.0** (below). Users must preserve *both* upstream and
  compilation attribution.

## Reproducibility

The full scraper (`scraper_v3.py`) runs entirely on Google Colab
(CPU-only). State is kept in a `manifest.jsonl` on the HF repo itself;
a new VM resumes by skipping `done_keys` (shard URLs + `ia:<id>`).
Progress and logs live in `/content/data/progress.json` & `scraper.log`.

## License

This dataset is released under the **Open Data Attribution Training
Disclosure License (ODATL-1.0)**, reproduced in full below.

---

# Open Data Attribution Training Disclosure License (ODATL-1.0)

Version 1.0 — July 2026

A permissive open-data license requiring attribution and mandatory disclosure of AI training use.

## SECTION 1 — DEFINITIONS

**1.1** "Dataset" refers to the collection of data, files, metadata, annotations, structures, or any other materials distributed under this License, including any updates, subsets, or modified versions.

**1.2** "Licensor" refers to the entity or individual who releases the Dataset under this License.

**1.3** "Licensee" refers to any person, organization, or system that accesses, uses, modifies, redistributes, or incorporates the Dataset.

**1.4** "Model" refers to any machine learning system, artificial intelligence system, algorithm, statistical model, or computational process trained, fine-tuned, evaluated, or otherwise developed using the Dataset.

**1.5** "Public Notice" refers to a clear, visible, and publicly accessible statement acknowledging use of the Dataset.

**1.6** "Derivative Dataset" refers to any dataset created by modifying, transforming, filtering, augmenting, or otherwise altering the original Dataset.

**1.7** "Derivative Model" refers to any Model whose training data includes the Dataset or any Derivative Dataset.

## SECTION 2 — GRANT OF RIGHTS

**2.1** The Licensor grants the Licensee a worldwide, royalty-free, non-exclusive, irrevocable permission to:
- Use, copy, and redistribute the Dataset for any purpose.
- Modify, transform, or build upon the Dataset.
- Create Derivative Datasets.
- Train, fine-tune, evaluate, or otherwise use the Dataset for machine learning or AI development.
- Create Derivative Models based on the Dataset.

**2.2** These rights are intended to be compatible with open-source and open-data principles, including but not limited to CC-BY, ODC-BY, and other permissive data licenses.

**2.3** No patent rights are granted or implied by this License.

## SECTION 3 — MANDATORY ATTRIBUTION

**3.1** Any public use, redistribution, publication, or derivative work involving the Dataset must include the following attribution:

> "This work uses data provided under the Open Data Attribution Training Disclosure License (ODATL-1.0)."

**3.2** Attribution must appear in:
- Documentation
- Research papers
- Model cards
- Public datasets
- Product descriptions
- Any public-facing material referencing the Dataset

**3.3** Attribution must remain intact and may not be removed, obscured, or altered.

## SECTION 4 — MANDATORY TRAINING DISCLOSURE

**4.1** If the Dataset is used to train, fine-tune, evaluate, or otherwise develop any Model, the Licensee must provide a Public Notice stating:

> "This model was trained using data provided under the Open Data Attribution Training Disclosure License (ODATL-1.0)."

**4.2** This disclosure must appear in:
- Model cards
- Public releases of the Model
- Research publications
- Technical documentation
- Product descriptions
- Any public announcement or description of the Model

**4.3** Disclosure must be truthful, visible, and accessible to the general public.

**4.4** Failure to provide this disclosure immediately terminates all rights granted under this License.

## SECTION 5 — REDISTRIBUTION REQUIREMENTS

**5.1** If the Licensee redistributes the Dataset or any Derivative Dataset, the Licensee must:
- Include this License in full.
- Clearly indicate any modifications made.
- Preserve all attribution and disclosure requirements.

**5.2** Derivative Datasets may be dual-licensed under other open-data licenses, provided this License remains included and enforceable.

## SECTION 6 — OPEN-SOURCE COMPATIBILITY

**6.1** This License is designed to be compatible with:
- Open Data Commons Attribution (ODC-BY)
- Creative Commons Attribution (CC-BY)
- Open-source AI research workflows
- Open-data distribution platforms

**6.2** Redistribution through open-source repositories (e.g., GitHub, HuggingFace, Kaggle) is permitted and encouraged.

**6.3** Licensees may combine the Dataset with other open datasets, provided attribution and training disclosure obligations remain intact.

## SECTION 7 — PROHIBITED USES

**7.1** The Licensee may not:
- Claim exclusive ownership of the Dataset.
- Remove or alter attribution or disclosure requirements.
- Use the Dataset in violation of applicable laws or regulations.
- Misrepresent the origin, nature, or licensing of the Dataset.

**7.2** The Licensee may not apply technical or legal measures that restrict others from exercising rights granted under this License.

## SECTION 8 — NO WARRANTY

**8.1** The Dataset is provided "as-is," without warranty of any kind, express or implied.

**8.2** The Licensor is not liable for any damages, losses, or claims arising from use of the Dataset or any Derivative Model.

## SECTION 9 — TERMINATION

**9.1** Rights under this License automatically terminate if the Licensee:
- Fails to provide required attribution.
- Fails to provide required training disclosure.
- Violates any other term of this License.

**9.2** Rights may be reinstated upon correction of the violation, unless the Licensor explicitly revokes permission.

## SECTION 10 — ACCEPTANCE

**10.1** By accessing or using the Dataset, the Licensee agrees to be bound by the terms of this License.

**10.2** Continued use of the Dataset constitutes ongoing acceptance of all terms.

## SECTION 11 — CONTACT

**11.1** For permissions beyond this License, contact the Licensor.
