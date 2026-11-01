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
  - 100K<n<1M
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/train-*.parquet"
---

# Sinabis Green Energy – Synthetic Document Dataset (100k DOCX)

**101,000 business documents (.docx)** from the everyday operations
of a fictional renewable-energy group (**Sinabis Green Energy**) and its worldwide
ecosystem of customers, suppliers, subcontractors, utilities, authorities, insurers,
banks, hotels and service providers.

This is the 100k edition of [sinabis-1m-synthetic-docx](https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-docx):
the first 101,000 documents of the 1M dataset (`idx` 0 to 101,000). File names, folder paths and manifest
records are identical to the 1M dataset, so both editions can be used side by side.

Every person, company, address, phone number, bank account, tax number, contract and
transaction in this dataset is **purely fictional**.

**How the documents were made.** The document texts of the 1M dataset come from **25,776 distinct
document blueprints** (22,457 of them appear in this edition) written by an LLM (Gemma 4 26B-A4B) in the target language: first concrete scenario briefs per
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
| Total Documents | **101,000** DOCX files (2.60 GB uncompressed, 2.49 GB in 1 ZIP archive) |
| Document Types | **55** document types in 5 families (contracts, letters, corporate, reports, commercial) |
| Distinct Texts | **22,457** LLM blueprints, **16,976** distinct document titles |
| Length | Ø **831** words per document (max 3,852), Ø 5.8 sections and 1.6 tables |
| Formal Signatures | **83,769** documents with signature blocks (82.9 %; single, dual or three-party) |
| Time span | **2012-04-11** to **2026-06-30** (14.2 years) |
| Languages | **24** languages (EN 81.3 %, JA 4.9 %, rest across 22 languages) |
| Issuing Companies | **2,014** distinct fictional companies across **33** countries |

## Quick start

The Parquet file under `data/` holds one row per document: all manifest fields plus the extracted
text, so the dataset can be browsed in the Dataset Viewer above and loaded directly:

```python
from datasets import load_dataset

ds = load_dataset("sinabis-group/sinabis-100k-synthetic-docx", split="train")
print(ds[0]["title"])
print(ds[0]["text"])
```

The `text` column holds the text of the document body in reading order (paragraphs, headings, lists and table cells, one per line). Headers and footers (letterhead, contact bar, page numbers) are not included. The original `.docx` files with their full layout are in the ZIP archive.

## Downloads

| File | Size | Contents |
|---|---:|---|
| `data/train-*.parquet` (1 file) | 262 MB | Manifest fields + extracted `text`, one row per document (Dataset Viewer, `load_dataset`) |
| `Sinabis_100k_docx.zip` | 2.49 GB | `101,000` DOCX files + manifest (2.60 GB uncompressed) |

`Sinabis_100k_docx_manifest.zip` (44.7 MB) holds only the JSON Lines records for all 101,000 documents,
for a quick look at the metadata without downloading the documents (see "Folder structure" below).

### Unpacking

Both archives share one directory structure. The document archive already contains the manifest, so
`unzip -o` simply overwrites identical files:

```bash
# Download and unpack with the Hugging Face CLI
hf download sinabis-group/sinabis-100k-synthetic-docx --repo-type dataset --local-dir sinabis-100k-docx
cd sinabis-100k-docx
for z in Sinabis_100k_docx*.zip; do unzip -qo "$z"; done
```

## Folder structure

In the repository:

```
.
├── README.md
├── data/
│   └── train-*.parquet                 (rows for the Dataset Viewer and load_dataset)
├── Sinabis_100k_docx.zip             → word/ + manifest/
└── Sinabis_100k_docx_manifest.zip    → manifest/
```

After unpacking:

```
sinabis-100k-docx/
├── README.md
├── word/
│   ├── service_contract/
│   │   ├── 0000/
│   │   │   ├── 0000xxx_<document-number>.docx
│   │   │   └── ...
│   │   └── ... (0000 to 0101)
│   ├── nda/
│   ├── meeting_minutes/
│   ├── sop_policy/
│   └── ... (55 document types)
└── manifest/
    ├── wb00000.jsonl
    ├── ...
    └── wb00201.jsonl
```

Each `wbNNNNN.jsonl` contains 500 records, one per document:
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
| `business_letter` | 5,961 | 5.9 % | Business letter on a concrete operational matter (coordination, information, request, follow-up) |
| `service_contract` | 5,056 | 5.0 % | Service / framework agreement between a contractor and a client (scope, service levels, rates, term, liability, governing law) |
| `meeting_minutes` | 4,412 | 4.4 % | Minutes of a meeting (attendees, agenda, discussion per item, decisions, action items with owners and due dates) |
| `project_proposal` | 4,226 | 4.2 % | Technical and commercial project proposal / offer (situation, approach, work packages, schedule, prices, assumptions, validity) |
| `sop_policy` | 2,901 | 2.9 % | Standard operating procedure or company policy (purpose, scope, responsibilities, procedure steps, records, revision history) |
| `internal_memo` | 2,887 | 2.9 % | Internal memo / management circular to staff on a policy, change or announcement |
| `employment_contract` | 2,862 | 2.8 % | Employment contract for a named employee (position, duties, working hours, probation, salary, leave, notice, confidentiality) |
| `project_report` | 2,855 | 2.8 % | Project status report (management summary, progress per work stream, milestones, budget, risks, next steps) |
| `nda` | 2,817 | 2.8 % | Mutual or one-way non-disclosure agreement (purpose, definition of confidential information, obligations, exceptions, term, penalties) |
| `invoice` | 2,226 | 2.2 % | Invoice with itemised goods or services, totals and payment terms |
| `purchase_agreement` | 2,198 | 2.2 % | Purchase / supply agreement for specific goods or equipment (object, price, delivery, acceptance, warranty, retention of title) |
| `maintenance_report` | 2,194 | 2.2 % | Technical maintenance / service report (object data, work performed, measurements, defects found, recommendations) |
| `subcontractor_agreement` | 2,139 | 2.1 % | Subcontractor agreement for construction or installation works (scope, schedule, remuneration, safety, insurance, penalties) |
| `lease_agreement` | 2,130 | 2.1 % | Commercial lease for premises, land, roof space or equipment (object, term, rent, deposit, maintenance, return) |
| `dunning_letter` | 2,066 | 2.0 % | Payment reminder or formal dunning letter with list of open items, fees and deadline |
| `maintenance_contract` | 1,934 | 1.9 % | Maintenance / service-level contract for technical installations (intervals, response times, spare parts, flat fee, exclusions) |
| `request_for_quotation` | 1,877 | 1.9 % | Request for quotation / tender invitation describing requirements, quantities, deadlines and evaluation criteria |
| `handover_protocol` | 1,866 | 1.8 % | Acceptance / handover protocol (object, participants, documents handed over, defects list, acceptance statement) |
| `change_request` | 1,863 | 1.8 % | Change request / variation order for a project (description, reason, impact on cost and schedule, approval) |
| `termination_letter` | 1,775 | 1.8 % | Formal termination of a contract or business relationship, stating the contract, notice period, end date and next steps |
| `audit_report` | 1,775 | 1.8 % | Quality, HSE or supplier audit report (scope, method, findings by area with ratings, nonconformities, corrective actions) |
| `consulting_agreement` | 1,760 | 1.7 % | Consulting / advisory agreement (mandate, deliverables, fees per day or hour, reporting, IP rights, termination) |
| `complaint_letter` | 1,738 | 1.7 % | Complaint about a defective delivery or poor service, describing the defects and demanding remedy |
| `work_instruction` | 1,715 | 1.7 % | Operating / work instruction for a machine, workplace or hazardous substance (hazards, protective measures, behaviour in emergencies, first aid, disposal) |
| `authority_notice` | 1,711 | 1.7 % | Official notice / decision from a public authority (permit, fee assessment, inspection result, objection rights) |
| `quote` | 1,693 | 1.7 % | Quotation / cost estimate with items, prices, validity and terms |
| `contract_amendment` | 1,653 | 1.6 % | Amendment / addendum to an existing contract changing specific clauses (price, term, scope), referencing the original contract |
| `inspection_report` | 1,459 | 1.4 % | Inspection / test report with test items, results, pass/fail, deviations and inspector statement |
| `press_release` | 1,445 | 1.4 % | Press release announcing a company news item (project, partnership, results, appointment) with quotes and boilerplate |
| `job_posting` | 1,441 | 1.4 % | Job advertisement (company intro, tasks, profile, benefits, how to apply) |
| `risk_assessment` | 1,440 | 1.4 % | Workplace risk assessment (activity, hazards, risk rating, measures, responsible persons, review date) |
| `data_processing_agreement` | 1,430 | 1.4 % | Data processing agreement under GDPR-like rules (subject, categories of data, technical and organisational measures, sub-processors, audits) |
| `complaint_response` | 1,429 | 1.4 % | Response to a customer complaint (acknowledgement, root cause, corrective actions, goodwill offer) |
| `incident_report` | 1,390 | 1.4 % | Incident / accident / outage report (timeline, cause analysis, impact, immediate and long-term measures) |
| `feasibility_study` | 1,335 | 1.3 % | Feasibility study / concept paper (initial situation, options compared, cost estimate, risks, recommendation) |
| `purchase_order` | 1,295 | 1.3 % | Purchase order to a supplier with an itemised order table (item, quantity, unit price, total), delivery address, delivery date and purchasing conditions |
| `training_handout` | 1,287 | 1.3 % | Training handout / course material on a professional topic with learning goals, explanations, examples and quiz questions |
| `technical_specification` | 1,266 | 1.3 % | Technical specification / requirements document (purpose, system context, functional and non-functional requirements, interfaces, acceptance criteria) |
| `invitation_letter` | 1,203 | 1.2 % | Invitation to an event, site visit, training or opening (agenda, location, registration) |
| `price_change_notice` | 1,191 | 1.2 % | Notice of price adjustment or changed terms, with reasons, effective date and new price list |
| `it_security_policy` | 1,179 | 1.2 % | IT security / acceptable-use policy (passwords, devices, data classification, incidents, sanctions) |
| `reference_letter` | 1,168 | 1.2 % | Employment reference / job testimonial for a named former employee describing tasks, performance and conduct |
| `customer_newsletter` | 1,135 | 1.1 % | Customer or partner newsletter with several short news articles |
| `order_confirmation` | 1,127 | 1.1 % | Order confirmation with items, delivery date and terms |
| `license_agreement` | 1,123 | 1.1 % | Software or technology license agreement (licensed subject, scope of use, fees, updates, support, liability) |
| `onboarding_plan` | 1,112 | 1.1 % | Onboarding plan / checklist for a new employee (first day, first weeks, contacts, trainings, equipment) |
| `delivery_note` | 1,051 | 1.0 % | Delivery note listing delivered items and quantities with receipt confirmation |
| `organisational_announcement` | 1,040 | 1.0 % | Organisational announcement (new appointment, restructuring, office move) to employees |
| `travel_expense_policy` | 1,010 | 1.0 % | Travel and expense policy (booking rules, allowances, reimbursement process, approval limits) |
| `market_analysis` | 1,009 | 1.0 % | Market or competitor analysis (market size, segments, trends, competitors, SWOT, conclusions) |
| `shareholder_resolution` | 894 | 0.9 % | Shareholder or board resolution (meeting details, resolutions with voting results, signatures) |
| `power_of_attorney` | 862 | 0.9 % | Power of attorney / authorisation for a named person to act on behalf of the company for defined matters |
| `lessons_learned` | 860 | 0.9 % | Lessons learned / post-project review (what went well, what did not, root causes, recommendations) |
| `expert_opinion` | 818 | 0.8 % | Expert opinion / assessment report on a technical or commercial question (assignment, findings, assessment, conclusion) |
| `annual_business_report` | 711 | 0.7 % | Management report section of an annual report (business development, financial position, employees, outlook, risks) |

## Document Families

| Family | Documents | Share |
|---|---:|---:|
| `letter` | 28,366 | 28.1 % |
| `contract` | 25,102 | 24.9 % |
| `corporate` | 22,602 | 22.4 % |
| `report` | 17,538 | 17.4 % |
| `commercial` | 7,392 | 7.3 % |

## Document Length

| Length class | Documents | Share |
|---|---:|---:|
| short (≈220–480 words) | 28,928 | 28.6 % |
| medium (≈550–1,100) | 38,806 | 38.4 % |
| long (≈1,200–2,200) | 24,795 | 24.5 % |
| very long (≈2,300–3,800) | 8,471 | 8.4 % |

## Language Distribution

| Language | Documents | Share |
|---|---:|---:|
| English (`en`) | 82,073 | **81.3 %** |
| Japanese (`ja`) | 4,955 | **4.9 %** |
| Chinese (`zh`) | 4,689 | **4.6 %** |
| German (`de`) | 1,688 | **1.7 %** |
| Portuguese (`pt`) | 841 | **0.8 %** |
| Spanish (`es`) | 826 | **0.8 %** |
| Italian (`it`) | 668 | **0.7 %** |
| French (`fr`) | 582 | **0.6 %** |
| Swedish (`sv`) | 507 | **0.5 %** |
| Dutch (`nl`) | 507 | **0.5 %** |
| Polish (`pl`) | 415 | **0.4 %** |
| Korean (`ko`) | 394 | **0.4 %** |
| Indonesian (`id`) | 368 | **0.4 %** |
| Hungarian (`hu`) | 305 | **0.3 %** |
| Danish (`da`) | 289 | **0.3 %** |
| Czech (`cs`) | 241 | **0.2 %** |
| Ukrainian (`uk`) | 237 | **0.2 %** |
| Norwegian (`nb`) | 232 | **0.2 %** |
| Vietnamese (`vi`) | 229 | **0.2 %** |
| Turkish (`tr`) | 224 | **0.2 %** |
| Finnish (`fi`) | 218 | **0.2 %** |
| Greek (`el`) | 206 | **0.2 %** |
| Romanian (`ro`) | 189 | **0.2 %** |
| Russian (`ru`) | 117 | **0.1 %** |

## Layout Variety

| Layout dimension | Variants used | Most frequent |
|---|---|---|
| Letterhead archetype | 12 variants | `logo_left_info_right` 10 %, `din_letterhead` 10 %, `underline_bar` 10 %, `minimal_text` 9 % |
| Heading numbering | 8 variants | `none` 30 %, `num` 25 %, `num_dot` 14 %, `article` 10 % |
| Heading style | 7 variants | `color` 23 %, `rule` 22 %, `caps` 12 %, `bar` 12 % |
| Title style | 7 variants | `band` 14 %, `rule` 14 %, `big` 14 %, `subject` 14 % |
| Table style | 8 variants | `zebra` 13 %, `boxed_round` 13 %, `double_rule` 13 %, `hlines` 12 % |
| Footer style | 6 variants | `contact_bar` 17 %, `line` 17 %, `none` 17 %, `columns` 17 % |
| Body font | 26 variants | `Arial` 25 %, `Times New Roman` 11 %, `Georgia` 7 %, `Calibri` 6 % |

Special layouts: cover page **11.3 %**, table of contents **19.2 %**, two-column layout **1.7 %**, watermark **4.1 %**, line numbering **3.0 %**.

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

> Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Document Dataset (100k DOCX).
> https://huggingface.co/datasets/sinabis-group/sinabis-100k-synthetic-docx

## Citation

```bibtex
@misc{sinabis_green_docx_100k_dataset_2026,
  author = {{Sinabis GmbH}},
  title  = {Sinabis Green Energy -- Synthetic Document Dataset (100k DOCX)},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sinabis-group/sinabis-100k-synthetic-docx}
}
```
