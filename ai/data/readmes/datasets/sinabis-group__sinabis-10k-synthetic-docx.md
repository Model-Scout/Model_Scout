---
license: cc-by-4.0
language:
  - en
  - ja
  - zh
  - de
  - pt
  - es
  - it
  - fr
  - sv
  - nl
  - pl
  - ko
  - id
  - hu
  - da
  - nb
  - fi
  - cs
  - uk
  - vi
  - tr
  - el
  - ro
  - ru
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
  - docx
  - word
  - documents
  - business-documents
  - contracts
  - agreements
  - policies
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
  - information-extraction
  - document-understanding
size_categories:
  - 10K<n<100K
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/train-*.parquet"
---

# Sinabis Green Energy – Synthetic Document Dataset (10k DOCX)

**10,100 business documents (.docx)** from the everyday operations
of a fictional renewable-energy group (**Sinabis Green Energy**) and its worldwide
ecosystem of customers, suppliers, subcontractors, utilities, authorities, insurers,
banks, hotels and service providers.

This is the 10k edition of [sinabis-1m-synthetic-docx](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-docx):
the first 10,100 documents of the 1M dataset (`idx` 0 to 10,099). File names, folder paths and manifest
records are identical to the 1M dataset, and this edition is the first part of the [100k edition](https://huggingface.co/datasets/sinabis-group/sinabis-100k-synthetic-docx),
so all editions can be used side by side.

Every person, company, address, phone number, bank account, tax number, contract and
transaction in this dataset is **purely fictional**.

**How the documents were made.** The document texts of the 1M dataset come from **25,776 distinct
document blueprints** (7,703 of them appear in this edition) written by an LLM (Gemma 4 26B-A4B) in the target language: first concrete scenario briefs per
document type and industry, then complete documents (sections, paragraphs, lists, tables, key-value blocks,
callouts, checklists) with placeholders for the parties. Each blueprint is filled with a company of the
fictional world, lightly varied (sections, list items, table rows) and laid out in the company's own visual
identity with `python-docx`. Commercial templates (invoices, quotes, order confirmations, delivery notes) use
itemised catalogue positions with exact totals. Blueprints are checked for target language and real brand names.

> All figures in this dataset card were **computed directly from the files in this edition**
> (as of 23 Oct 2026). They are not target estimates.

## At a glance

| Metric | Value |
|---|---|
| Total Documents | **10,100** DOCX files (260 MB uncompressed, 249 MB in 1 ZIP archive) |
| Document Types | **55** document types in 5 families (contracts, letters, corporate, reports, commercial) |
| Distinct Texts | **7,703** LLM blueprints, **5,917** distinct document titles |
| Length | Ø **831** words per document (max 3,738), Ø 5.8 sections and 1.6 tables |
| Formal Signatures | **8,333** documents with signature blocks (82.5 %; single, dual or three-party) |
| Time span | **2012-04-11** to **2026-06-30** (14.2 years) |
| Languages | **24** languages (EN 81.2 %, JA 5.1 %, rest across 22 languages) |
| Issuing Companies | **1,974** distinct fictional companies across **33** countries |

## Quick start

The Parquet file under `data/` holds one row per document: all manifest fields plus the extracted
text, so the dataset can be browsed in the Dataset Viewer above and loaded directly:

```python
from datasets import load_dataset

ds = load_dataset("sinabis-group/sinabis-10k-synthetic-docx", split="train")
print(ds[0]["title"])
print(ds[0]["text"])
```

The `text` column holds the text of the document body in reading order (paragraphs, headings, lists and table cells, one per line). Headers and footers (letterhead, contact bar, page numbers) are not included. The original `.docx` files with their full layout are in the ZIP archive.

## Downloads

| File | Size | Contents |
|---|---:|---|
| `data/train-*.parquet` (1 file) | 26 MB | Manifest fields + extracted `text`, one row per document (Dataset Viewer, `load_dataset`) |
| `Sinabis_10k_docx.zip` | 249 MB | `10,100` DOCX files + manifest (260 MB uncompressed) |

`Sinabis_10k_docx_manifest.zip` (4.5 MB) holds only the JSON Lines records for all 10,100 documents,
for a quick look at the metadata without downloading the documents (see "Folder structure" below).

### Unpacking

Both archives share one directory structure. The document archive already contains the manifest, so
`unzip -o` simply overwrites identical files:

```bash
# Download and unpack with the Hugging Face CLI
hf download sinabis-group/sinabis-10k-synthetic-docx --repo-type dataset --local-dir sinabis-10k-docx
cd sinabis-10k-docx
for z in Sinabis_10k_docx*.zip; do unzip -qo "$z"; done
```

## Folder structure

In the repository:

```
.
├── README.md
├── data/
│   └── train-*.parquet                 (rows for the Dataset Viewer and load_dataset)
├── Sinabis_10k_docx.zip             → word/ + manifest/
└── Sinabis_10k_docx_manifest.zip    → manifest/
```

After unpacking:

```
sinabis-10k-docx/
├── README.md
├── word/
│   ├── service_contract/
│   │   ├── 0000/
│   │   │   ├── 0000xxx_<document-number>.docx
│   │   │   └── ...
│   │   └── ... (0000 to 0010)
│   ├── nda/
│   ├── meeting_minutes/
│   ├── sop_policy/
│   └── ... (55 document types)
└── manifest/
    ├── wb00000.jsonl
    ├── ...
    └── wb00020.jsonl
```

Each `wbNNNNN.jsonl` contains 500 records (the last shard 100), one per document:
- `idx`: Running document number (same as in the 1M dataset)
- `file`: Relative path to the `.docx` file
- `format`: `"docx"`
- `theme`: Document theme (e.g. `service_contract`, `nda`, `meeting_minutes`)
- `issuer_id`: Stable ID of the fictional issuing company
- `issuer`: Fictional issuing company name
- `issuer_country`: Two-letter country code (ISO 3166-1)
- `recipient`: Counterparty or recipient name
- `recipient_kind`: Counterparty category (e.g. `customer`, `supplier`, `authority`)
- `lang`: Language code (ISO 639-1)
- `date`: Document issue date (ISO 8601)
- `number`: Serial document reference number
- `currency`: ISO 4217 currency code (where financial amounts apply)
- `total`: Financial amount or contract value (where applicable)
- `signed`: Boolean flag indicating formal signature blocks
- `bytes`: Exact byte size of the `.docx` file
- `family`, `title`: Document family and title as rendered
- `blueprint_id`, `length_class`: Source blueprint (`<type>_<lang>_<n>`) and length class (S/M/L/XL)
- `words`, `sections`, `tables`, `line_items`, `signatures`: Content statistics
- `layout_*`: Layout decisions (letterhead, title, table and footer style, font, font size, line spacing, heading
  numbering and style, cover page, table of contents, two columns, watermark, line numbers)
- `text_preview`: First 600 characters of the document text

## Document Themes

| Theme | Documents | Share | Description |
|---|---:|---:|---|
| `business_letter` | 566 | 5.6 % | Business letter on a concrete operational matter (coordination, information, request, follow-up) |
| `service_contract` | 489 | 4.8 % | Service / framework agreement between a contractor and a client (scope, service levels, rates, term, liability, governing law) |
| `meeting_minutes` | 457 | 4.5 % | Minutes of a meeting (attendees, agenda, discussion per item, decisions, action items with owners and due dates) |
| `project_proposal` | 429 | 4.2 % | Technical and commercial project proposal / offer (situation, approach, work packages, schedule, prices, assumptions, validity) |
| `sop_policy` | 294 | 2.9 % | Standard operating procedure or company policy (purpose, scope, responsibilities, procedure steps, records, revision history) |
| `project_report` | 286 | 2.8 % | Project status report (management summary, progress per work stream, milestones, budget, risks, next steps) |
| `employment_contract` | 278 | 2.8 % | Employment contract for a named employee (position, duties, working hours, probation, salary, leave, notice, confidentiality) |
| `nda` | 269 | 2.7 % | Mutual or one-way non-disclosure agreement (purpose, definition of confidential information, obligations, exceptions, term, penalties) |
| `internal_memo` | 245 | 2.4 % | Internal memo / management circular to staff on a policy, change or announcement |
| `invoice` | 245 | 2.4 % | Invoice with itemised goods or services, totals and payment terms |
| `subcontractor_agreement` | 233 | 2.3 % | Subcontractor agreement for construction or installation works (scope, schedule, remuneration, safety, insurance, penalties) |
| `maintenance_report` | 220 | 2.2 % | Technical maintenance / service report (object data, work performed, measurements, defects found, recommendations) |
| `lease_agreement` | 207 | 2.0 % | Commercial lease for premises, land, roof space or equipment (object, term, rent, deposit, maintenance, return) |
| `handover_protocol` | 203 | 2.0 % | Acceptance / handover protocol (object, participants, documents handed over, defects list, acceptance statement) |
| `request_for_quotation` | 199 | 2.0 % | Request for quotation / tender invitation describing requirements, quantities, deadlines and evaluation criteria |
| `dunning_letter` | 198 | 2.0 % | Payment reminder or formal dunning letter with list of open items, fees and deadline |
| `purchase_agreement` | 192 | 1.9 % | Purchase / supply agreement for specific goods or equipment (object, price, delivery, acceptance, warranty, retention of title) |
| `consulting_agreement` | 191 | 1.9 % | Consulting / advisory agreement (mandate, deliverables, fees per day or hour, reporting, IP rights, termination) |
| `change_request` | 188 | 1.9 % | Change request / variation order for a project (description, reason, impact on cost and schedule, approval) |
| `authority_notice` | 183 | 1.8 % | Official notice / decision from a public authority (permit, fee assessment, inspection result, objection rights) |
| `termination_letter` | 182 | 1.8 % | Formal termination of a contract or business relationship, stating the contract, notice period, end date and next steps |
| `maintenance_contract` | 177 | 1.8 % | Maintenance / service-level contract for technical installations (intervals, response times, spare parts, flat fee, exclusions) |
| `inspection_report` | 174 | 1.7 % | Inspection / test report with test items, results, pass/fail, deviations and inspector statement |
| `audit_report` | 170 | 1.7 % | Quality, HSE or supplier audit report (scope, method, findings by area with ratings, nonconformities, corrective actions) |
| `complaint_letter` | 169 | 1.7 % | Complaint about a defective delivery or poor service, describing the defects and demanding remedy |
| `work_instruction` | 168 | 1.7 % | Operating / work instruction for a machine, workplace or hazardous substance (hazards, protective measures, behaviour in emergencies, first aid, disposal) |
| `complaint_response` | 159 | 1.6 % | Response to a customer complaint (acknowledgement, root cause, corrective actions, goodwill offer) |
| `contract_amendment` | 158 | 1.6 % | Amendment / addendum to an existing contract changing specific clauses (price, term, scope), referencing the original contract |
| `quote` | 149 | 1.5 % | Quotation / cost estimate with items, prices, validity and terms |
| `incident_report` | 148 | 1.5 % | Incident / accident / outage report (timeline, cause analysis, impact, immediate and long-term measures) |
| `price_change_notice` | 140 | 1.4 % | Notice of price adjustment or changed terms, with reasons, effective date and new price list |
| `data_processing_agreement` | 138 | 1.4 % | Data processing agreement under GDPR-like rules (subject, categories of data, technical and organisational measures, sub-processors, audits) |
| `purchase_order` | 135 | 1.3 % | Purchase order to a supplier with an itemised order table (item, quantity, unit price, total), delivery address, delivery date and purchasing conditions |
| `job_posting` | 135 | 1.3 % | Job advertisement (company intro, tasks, profile, benefits, how to apply) |
| `customer_newsletter` | 133 | 1.3 % | Customer or partner newsletter with several short news articles |
| `feasibility_study` | 132 | 1.3 % | Feasibility study / concept paper (initial situation, options compared, cost estimate, risks, recommendation) |
| `press_release` | 130 | 1.3 % | Press release announcing a company news item (project, partnership, results, appointment) with quotes and boilerplate |
| `reference_letter` | 130 | 1.3 % | Employment reference / job testimonial for a named former employee describing tasks, performance and conduct |
| `risk_assessment` | 128 | 1.3 % | Workplace risk assessment (activity, hazards, risk rating, measures, responsible persons, review date) |
| `training_handout` | 127 | 1.3 % | Training handout / course material on a professional topic with learning goals, explanations, examples and quiz questions |
| `invitation_letter` | 126 | 1.2 % | Invitation to an event, site visit, training or opening (agenda, location, registration) |
| `technical_specification` | 123 | 1.2 % | Technical specification / requirements document (purpose, system context, functional and non-functional requirements, interfaces, acceptance criteria) |
| `it_security_policy` | 118 | 1.2 % | IT security / acceptable-use policy (passwords, devices, data classification, incidents, sanctions) |
| `onboarding_plan` | 117 | 1.2 % | Onboarding plan / checklist for a new employee (first day, first weeks, contacts, trainings, equipment) |
| `market_analysis` | 113 | 1.1 % | Market or competitor analysis (market size, segments, trends, competitors, SWOT, conclusions) |
| `order_confirmation` | 107 | 1.1 % | Order confirmation with items, delivery date and terms |
| `license_agreement` | 105 | 1.0 % | Software or technology license agreement (licensed subject, scope of use, fees, updates, support, liability) |
| `organisational_announcement` | 104 | 1.0 % | Organisational announcement (new appointment, restructuring, office move) to employees |
| `travel_expense_policy` | 104 | 1.0 % | Travel and expense policy (booking rules, allowances, reimbursement process, approval limits) |
| `delivery_note` | 99 | 1.0 % | Delivery note listing delivered items and quantities with receipt confirmation |
| `lessons_learned` | 96 | 1.0 % | Lessons learned / post-project review (what went well, what did not, root causes, recommendations) |
| `expert_opinion` | 92 | 0.9 % | Expert opinion / assessment report on a technical or commercial question (assignment, findings, assessment, conclusion) |
| `power_of_attorney` | 89 | 0.9 % | Power of attorney / authorisation for a named person to act on behalf of the company for defined matters |
| `shareholder_resolution` | 81 | 0.8 % | Shareholder or board resolution (meeting details, resolutions with voting results, signatures) |
| `annual_business_report` | 72 | 0.7 % | Management report section of an annual report (business development, financial position, employees, outlook, risks) |

## Document Families

| Family | Documents | Share |
|---|---:|---:|
| `letter` | 2,879 | 28.5 % |
| `contract` | 2,437 | 24.1 % |
| `corporate` | 2,220 | 22.0 % |
| `report` | 1,829 | 18.1 % |
| `commercial` | 735 | 7.3 % |

## Document Length

| Length class | Documents | Share |
|---|---:|---:|
| short (≈220–480 words) | 2,904 | 28.8 % |
| medium (≈550–1,100) | 3,917 | 38.8 % |
| long (≈1,200–2,200) | 2,437 | 24.1 % |
| very long (≈2,300–3,800) | 842 | 8.3 % |

## Language Distribution

| Language | Documents | Share |
|---|---:|---:|
| English (`en`) | 8,198 | **81.2 %** |
| Japanese (`ja`) | 518 | **5.1 %** |
| Chinese (`zh`) | 467 | **4.6 %** |
| German (`de`) | 160 | **1.6 %** |
| Portuguese (`pt`) | 93 | **0.9 %** |
| Spanish (`es`) | 83 | **0.8 %** |
| Italian (`it`) | 59 | **0.6 %** |
| Dutch (`nl`) | 57 | **0.6 %** |
| French (`fr`) | 51 | **0.5 %** |
| Swedish (`sv`) | 51 | **0.5 %** |
| Indonesian (`id`) | 41 | **0.4 %** |
| Korean (`ko`) | 36 | **0.4 %** |
| Danish (`da`) | 35 | **0.3 %** |
| Polish (`pl`) | 31 | **0.3 %** |
| Czech (`cs`) | 29 | **0.3 %** |
| Ukrainian (`uk`) | 27 | **0.3 %** |
| Hungarian (`hu`) | 26 | **0.3 %** |
| Vietnamese (`vi`) | 24 | **0.2 %** |
| Finnish (`fi`) | 24 | **0.2 %** |
| Norwegian (`nb`) | 24 | **0.2 %** |
| Greek (`el`) | 22 | **0.2 %** |
| Romanian (`ro`) | 18 | **0.2 %** |
| Turkish (`tr`) | 16 | **0.2 %** |
| Russian (`ru`) | 10 | **0.1 %** |

## Layout Variety

| Layout dimension | Variants used | Most frequent |
|---|---|---|
| Letterhead archetype | 12 variants | `logo_left_info_right` 11 %, `din_letterhead` 10 %, `underline_bar` 9 %, `minimal_text` 9 % |
| Heading numbering | 8 variants | `none` 31 %, `num` 25 %, `num_dot` 14 %, `article` 10 % |
| Heading style | 7 variants | `color` 23 %, `rule` 22 %, `bar` 12 %, `caps` 12 % |
| Title style | 7 variants | `band` 15 %, `rule` 15 %, `big` 14 %, `subject` 14 % |
| Table style | 8 variants | `zebra` 13 %, `minimal` 13 %, `double_rule` 13 %, `grid` 12 % |
| Footer style | 6 variants | `line` 17 %, `band` 17 %, `contact_bar` 17 %, `columns` 16 % |
| Body font | 26 variants | `Arial` 24 %, `Times New Roman` 11 %, `Georgia` 7 %, `Calibri` 6 % |

Special layouts: cover page **11.0 %**, table of contents **18.9 %**, two-column layout **1.9 %**, watermark **3.8 %**, line numbering **2.9 %**.

## Visual Design-DNA

Every issuing company has up to 100 deterministic visual identities derived from its company ID:
- **Header Archetypes:** Full-bleed color band, clean letterhead, modern sidebar, minimalist, split-block.
- **Embedded PNG Logos:** High-resolution procedural vector logos rendered to PNG and placed in the Word document header.
- **Color Palettes:** Harmonized primary, secondary, accent and neutral tones with WCAG-compliant contrast.
- **Typography:** Font pairings per style (serif, sans, slab), East-Asian fonts for Japanese, Chinese and Korean.
- **Tables & Shading:** Styled OpenXML tables with zebra striping, accent headers and proper border treatments.
- **Dynamic Headers & Footers:** Native Word headers with document title, reference number, and dynamic `PAGE` / `NUMPAGES` fields.

## Strict Fictionality Guardrails

- **Domain Names:** All external email and website domains use the RFC 2606 reserved `.example` TLD.
- **Phone Numbers:** All telephone numbers use fictional prefixes (e.g. `555-01xx` in North America).
- **Banking:** Bank names and IBANs are algorithmically generated using synthetic syllables and valid checksum algorithms.
- **Screening:** Company names and every blueprint are filtered against a blocklist of real brands and organisations.

## License

This dataset is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.
You are free to share and adapt the material for any purpose, including commercial applications,
provided appropriate credit is given:

> Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Document Dataset (10k DOCX).
> https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-docx

## Citation

```bibtex
@misc{sinabis_green_docx_10k_dataset_2026,
  author = {{Sinabis GmbH}},
  title  = {Sinabis Green Energy -- Synthetic Document Dataset (10k DOCX)},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-docx}
}
```
