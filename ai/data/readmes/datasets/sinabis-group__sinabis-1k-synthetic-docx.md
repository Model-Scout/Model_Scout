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
  - 1K<n<10K
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/train-*.parquet"
---

# Sinabis Green Energy – Synthetic Document Dataset (1k DOCX)

**1,010 business documents (.docx)** from the everyday operations
of a fictional renewable-energy group (**Sinabis Green Energy**) and its worldwide
ecosystem of customers, suppliers, subcontractors, utilities, authorities, insurers,
banks, hotels and service providers.

This is the 1k edition of [sinabis-1m-synthetic-docx](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-docx):
the first 1,010 documents of the 1M dataset (`idx` 0 to 1,009). File names, folder paths and manifest
records are identical to the 1M dataset, and this edition is the first part of the [10k edition](https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-docx) and [100k edition](https://huggingface.co/datasets/sinabis-group/sinabis-100k-synthetic-docx),
so all editions can be used side by side.

Every person, company, address, phone number, bank account, tax number, contract and
transaction in this dataset is **purely fictional**.

**How the documents were made.** The document texts of the 1M dataset come from **25,776 distinct
document blueprints** (980 of them appear in this edition) written by an LLM (Gemma 4 26B-A4B) in the target language: first concrete scenario briefs per
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
| Total Documents | **1,010** DOCX files (26 MB uncompressed, 25 MB in 1 ZIP archive) |
| Document Types | **55** document types in 5 families (contracts, letters, corporate, reports, commercial) |
| Distinct Texts | **980** LLM blueprints, **848** distinct document titles |
| Length | Ø **817** words per document (max 2,896), Ø 5.7 sections and 1.5 tables |
| Formal Signatures | **854** documents with signature blocks (84.6 %; single, dual or three-party) |
| Time span | **2014-06-12** to **2026-06-28** (12.0 years) |
| Languages | **23** languages (EN 83.1 %, ZH 4.8 %, rest across 21 languages) |
| Issuing Companies | **776** distinct fictional companies across **33** countries |

## Quick start

The Parquet file under `data/` holds one row per document: all manifest fields plus the extracted
text, so the dataset can be browsed in the Dataset Viewer above and loaded directly:

```python
from datasets import load_dataset

ds = load_dataset("sinabis-group/sinabis-1k-synthetic-docx", split="train")
print(ds[0]["title"])
print(ds[0]["text"])
```

The `text` column holds the text of the document body in reading order (paragraphs, headings, lists and table cells, one per line). Headers and footers (letterhead, contact bar, page numbers) are not included. The original `.docx` files with their full layout are in the ZIP archive.

## Downloads

| File | Size | Contents |
|---|---:|---|
| `data/train-*.parquet` (1 file) | 3 MB | Manifest fields + extracted `text`, one row per document (Dataset Viewer, `load_dataset`) |
| `Sinabis_1k_docx.zip` | 25 MB | `1,010` DOCX files + manifest (26 MB uncompressed) |

`Sinabis_1k_docx_manifest.zip` (0.4 MB) holds only the JSON Lines records for all 1,010 documents,
for a quick look at the metadata without downloading the documents (see "Folder structure" below).

### Unpacking

Both archives share one directory structure. The document archive already contains the manifest, so
`unzip -o` simply overwrites identical files:

```bash
# Download and unpack with the Hugging Face CLI
hf download sinabis-group/sinabis-1k-synthetic-docx --repo-type dataset --local-dir sinabis-1k-docx
cd sinabis-1k-docx
for z in Sinabis_1k_docx*.zip; do unzip -qo "$z"; done
```

## Folder structure

In the repository:

```
.
├── README.md
├── data/
│   └── train-*.parquet                 (rows for the Dataset Viewer and load_dataset)
├── Sinabis_1k_docx.zip             → word/ + manifest/
└── Sinabis_1k_docx_manifest.zip    → manifest/
```

After unpacking:

```
sinabis-1k-docx/
├── README.md
├── word/
│   ├── service_contract/
│   │   ├── 0000/
│   │   │   ├── 0000xxx_<document-number>.docx
│   │   │   └── ...
│   │   └── ... (0000 to 0001)
│   ├── nda/
│   ├── meeting_minutes/
│   ├── sop_policy/
│   └── ... (55 document types)
└── manifest/
    ├── wb00000.jsonl
    ├── ...
    └── wb00002.jsonl
```

Each `wbNNNNN.jsonl` contains 500 records (the last shard 10), one per document:
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
| `business_letter` | 66 | 6.5 % | Business letter on a concrete operational matter (coordination, information, request, follow-up) |
| `service_contract` | 48 | 4.8 % | Service / framework agreement between a contractor and a client (scope, service levels, rates, term, liability, governing law) |
| `project_proposal` | 42 | 4.2 % | Technical and commercial project proposal / offer (situation, approach, work packages, schedule, prices, assumptions, validity) |
| `meeting_minutes` | 39 | 3.9 % | Minutes of a meeting (attendees, agenda, discussion per item, decisions, action items with owners and due dates) |
| `internal_memo` | 34 | 3.4 % | Internal memo / management circular to staff on a policy, change or announcement |
| `subcontractor_agreement` | 31 | 3.1 % | Subcontractor agreement for construction or installation works (scope, schedule, remuneration, safety, insurance, penalties) |
| `dunning_letter` | 31 | 3.1 % | Payment reminder or formal dunning letter with list of open items, fees and deadline |
| `nda` | 30 | 3.0 % | Mutual or one-way non-disclosure agreement (purpose, definition of confidential information, obligations, exceptions, term, penalties) |
| `termination_letter` | 28 | 2.8 % | Formal termination of a contract or business relationship, stating the contract, notice period, end date and next steps |
| `project_report` | 27 | 2.7 % | Project status report (management summary, progress per work stream, milestones, budget, risks, next steps) |
| `work_instruction` | 24 | 2.4 % | Operating / work instruction for a machine, workplace or hazardous substance (hazards, protective measures, behaviour in emergencies, first aid, disposal) |
| `employment_contract` | 24 | 2.4 % | Employment contract for a named employee (position, duties, working hours, probation, salary, leave, notice, confidentiality) |
| `handover_protocol` | 22 | 2.2 % | Acceptance / handover protocol (object, participants, documents handed over, defects list, acceptance statement) |
| `maintenance_report` | 21 | 2.1 % | Technical maintenance / service report (object data, work performed, measurements, defects found, recommendations) |
| `sop_policy` | 21 | 2.1 % | Standard operating procedure or company policy (purpose, scope, responsibilities, procedure steps, records, revision history) |
| `complaint_letter` | 21 | 2.1 % | Complaint about a defective delivery or poor service, describing the defects and demanding remedy |
| `technical_specification` | 20 | 2.0 % | Technical specification / requirements document (purpose, system context, functional and non-functional requirements, interfaces, acceptance criteria) |
| `request_for_quotation` | 20 | 2.0 % | Request for quotation / tender invitation describing requirements, quantities, deadlines and evaluation criteria |
| `quote` | 19 | 1.9 % | Quotation / cost estimate with items, prices, validity and terms |
| `job_posting` | 19 | 1.9 % | Job advertisement (company intro, tasks, profile, benefits, how to apply) |
| `authority_notice` | 18 | 1.8 % | Official notice / decision from a public authority (permit, fee assessment, inspection result, objection rights) |
| `inspection_report` | 17 | 1.7 % | Inspection / test report with test items, results, pass/fail, deviations and inspector statement |
| `incident_report` | 17 | 1.7 % | Incident / accident / outage report (timeline, cause analysis, impact, immediate and long-term measures) |
| `maintenance_contract` | 17 | 1.7 % | Maintenance / service-level contract for technical installations (intervals, response times, spare parts, flat fee, exclusions) |
| `consulting_agreement` | 16 | 1.6 % | Consulting / advisory agreement (mandate, deliverables, fees per day or hour, reporting, IP rights, termination) |
| `purchase_agreement` | 16 | 1.6 % | Purchase / supply agreement for specific goods or equipment (object, price, delivery, acceptance, warranty, retention of title) |
| `reference_letter` | 16 | 1.6 % | Employment reference / job testimonial for a named former employee describing tasks, performance and conduct |
| `market_analysis` | 15 | 1.5 % | Market or competitor analysis (market size, segments, trends, competitors, SWOT, conclusions) |
| `audit_report` | 15 | 1.5 % | Quality, HSE or supplier audit report (scope, method, findings by area with ratings, nonconformities, corrective actions) |
| `data_processing_agreement` | 15 | 1.5 % | Data processing agreement under GDPR-like rules (subject, categories of data, technical and organisational measures, sub-processors, audits) |
| `press_release` | 15 | 1.5 % | Press release announcing a company news item (project, partnership, results, appointment) with quotes and boilerplate |
| `lease_agreement` | 14 | 1.4 % | Commercial lease for premises, land, roof space or equipment (object, term, rent, deposit, maintenance, return) |
| `contract_amendment` | 14 | 1.4 % | Amendment / addendum to an existing contract changing specific clauses (price, term, scope), referencing the original contract |
| `expert_opinion` | 13 | 1.3 % | Expert opinion / assessment report on a technical or commercial question (assignment, findings, assessment, conclusion) |
| `change_request` | 13 | 1.3 % | Change request / variation order for a project (description, reason, impact on cost and schedule, approval) |
| `organisational_announcement` | 12 | 1.2 % | Organisational announcement (new appointment, restructuring, office move) to employees |
| `customer_newsletter` | 12 | 1.2 % | Customer or partner newsletter with several short news articles |
| `invitation_letter` | 12 | 1.2 % | Invitation to an event, site visit, training or opening (agenda, location, registration) |
| `power_of_attorney` | 11 | 1.1 % | Power of attorney / authorisation for a named person to act on behalf of the company for defined matters |
| `travel_expense_policy` | 11 | 1.1 % | Travel and expense policy (booking rules, allowances, reimbursement process, approval limits) |
| `risk_assessment` | 11 | 1.1 % | Workplace risk assessment (activity, hazards, risk rating, measures, responsible persons, review date) |
| `complaint_response` | 11 | 1.1 % | Response to a customer complaint (acknowledgement, root cause, corrective actions, goodwill offer) |
| `purchase_order` | 11 | 1.1 % | Purchase order to a supplier with an itemised order table (item, quantity, unit price, total), delivery address, delivery date and purchasing conditions |
| `it_security_policy` | 11 | 1.1 % | IT security / acceptable-use policy (passwords, devices, data classification, incidents, sanctions) |
| `invoice` | 11 | 1.1 % | Invoice with itemised goods or services, totals and payment terms |
| `price_change_notice` | 10 | 1.0 % | Notice of price adjustment or changed terms, with reasons, effective date and new price list |
| `training_handout` | 10 | 1.0 % | Training handout / course material on a professional topic with learning goals, explanations, examples and quiz questions |
| `feasibility_study` | 9 | 0.9 % | Feasibility study / concept paper (initial situation, options compared, cost estimate, risks, recommendation) |
| `lessons_learned` | 8 | 0.8 % | Lessons learned / post-project review (what went well, what did not, root causes, recommendations) |
| `license_agreement` | 8 | 0.8 % | Software or technology license agreement (licensed subject, scope of use, fees, updates, support, liability) |
| `annual_business_report` | 8 | 0.8 % | Management report section of an annual report (business development, financial position, employees, outlook, risks) |
| `delivery_note` | 7 | 0.7 % | Delivery note listing delivered items and quantities with receipt confirmation |
| `onboarding_plan` | 7 | 0.7 % | Onboarding plan / checklist for a new employee (first day, first weeks, contacts, trainings, equipment) |
| `shareholder_resolution` | 6 | 0.6 % | Shareholder or board resolution (meeting details, resolutions with voting results, signatures) |
| `order_confirmation` | 6 | 0.6 % | Order confirmation with items, delivery date and terms |

## Document Families

| Family | Documents | Share |
|---|---:|---:|
| `letter` | 321 | 31.8 % |
| `contract` | 233 | 23.1 % |
| `corporate` | 210 | 20.8 % |
| `report` | 192 | 19.0 % |
| `commercial` | 54 | 5.3 % |

## Document Length

| Length class | Documents | Share |
|---|---:|---:|
| short (≈220–480 words) | 284 | 28.1 % |
| medium (≈550–1,100) | 407 | 40.3 % |
| long (≈1,200–2,200) | 232 | 23.0 % |
| very long (≈2,300–3,800) | 87 | 8.6 % |

## Language Distribution

| Language | Documents | Share |
|---|---:|---:|
| English (`en`) | 839 | **83.1 %** |
| Chinese (`zh`) | 48 | **4.8 %** |
| Japanese (`ja`) | 41 | **4.1 %** |
| German (`de`) | 12 | **1.2 %** |
| French (`fr`) | 9 | **0.9 %** |
| Portuguese (`pt`) | 8 | **0.8 %** |
| Spanish (`es`) | 7 | **0.7 %** |
| Italian (`it`) | 6 | **0.6 %** |
| Danish (`da`) | 6 | **0.6 %** |
| Dutch (`nl`) | 5 | **0.5 %** |
| Swedish (`sv`) | 4 | **0.4 %** |
| Finnish (`fi`) | 4 | **0.4 %** |
| Polish (`pl`) | 3 | **0.3 %** |
| Czech (`cs`) | 3 | **0.3 %** |
| Ukrainian (`uk`) | 3 | **0.3 %** |
| Norwegian (`nb`) | 3 | **0.3 %** |
| Hungarian (`hu`) | 2 | **0.2 %** |
| Vietnamese (`vi`) | 2 | **0.2 %** |
| Greek (`el`) | 1 | **0.1 %** |
| Turkish (`tr`) | 1 | **0.1 %** |
| Korean (`ko`) | 1 | **0.1 %** |
| Russian (`ru`) | 1 | **0.1 %** |
| Indonesian (`id`) | 1 | **0.1 %** |

## Layout Variety

| Layout dimension | Variants used | Most frequent |
|---|---|---|
| Letterhead archetype | 12 variants | `logo_left_info_right` 11 %, `din_letterhead` 11 %, `title_left_logo_right` 10 %, `underline_bar` 10 % |
| Heading numbering | 7 variants | `none` 30 %, `num` 27 %, `num_dot` 15 %, `article` 9 % |
| Heading style | 7 variants | `rule` 23 %, `color` 21 %, `bar` 12 %, `caps` 12 % |
| Title style | 7 variants | `subject` 16 %, `rule` 16 %, `big` 14 %, `small_caps` 14 % |
| Table style | 8 variants | `minimal` 14 %, `header_rule` 14 %, `grid` 13 %, `hlines` 12 % |
| Footer style | 6 variants | `contact_bar` 19 %, `line` 17 %, `band` 17 %, `columns` 17 % |
| Body font | 26 variants | `Arial` 24 %, `Times New Roman` 11 %, `Calibri` 7 %, `Georgia` 6 % |

Special layouts: cover page **9.7 %**, table of contents **18.7 %**, two-column layout **1.6 %**, watermark **2.8 %**, line numbering **3.7 %**.

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

> Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Document Dataset (1k DOCX).
> https://huggingface.co/datasets/sinabis-group/sinabis-1k-synthetic-docx

## Citation

```bibtex
@misc{sinabis_green_docx_1k_dataset_2026,
  author = {{Sinabis GmbH}},
  title  = {Sinabis Green Energy -- Synthetic Document Dataset (1k DOCX)},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sinabis-group/sinabis-1k-synthetic-docx}
}
```
