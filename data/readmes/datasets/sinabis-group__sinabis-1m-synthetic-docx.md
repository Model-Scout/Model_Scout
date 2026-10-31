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
  - 1M<n<10M
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/train-*.parquet"
---

# Sinabis Green Energy – Synthetic Document Dataset (1M DOCX)

More than **1,005,997 business documents (.docx)** from the everyday operations
of a fictional renewable-energy group (**Sinabis Green Energy**) and its worldwide
ecosystem of customers, suppliers, subcontractors, utilities, authorities, insurers,
banks, hotels and service providers.

Every person, company, address, phone number, bank account, tax number, contract and
transaction in this dataset is **purely fictional**.

**How the documents were made.** The document texts come from **25,776 distinct document
blueprints** written by an LLM (Gemma 4 26B-A4B) in the target language: first concrete scenario briefs per
document type and industry, then complete documents (sections, paragraphs, lists, tables, key-value blocks,
callouts, checklists) with placeholders for the parties. Each blueprint is filled with a company of the
fictional world, lightly varied (sections, list items, table rows) and laid out in the company's own visual
identity with `python-docx`. Commercial templates (invoices, quotes, order confirmations, delivery notes) use
itemised catalogue positions with exact totals. Blueprints are checked for target language and real brand names.

> All figures in this dataset card were **computed directly from the generated files**
> (as of 21 Oct 2026). They are not target estimates.

## At a glance

| Metric | Value |
|---|---|
| Total Documents | **1,005,997** DOCX files (25.9 GB uncompressed, 25.0 GB in 5 ZIP archives) |
| Document Types | **55** document types in 5 families (contracts, letters, corporate, reports, commercial) |
| Distinct Texts | **25,776** LLM blueprints, **22,515** distinct document titles |
| Length | Ø **833** words per document (max 4,062), Ø 5.8 sections and 1.6 tables |
| Formal Signatures | **834,391** documents with signature blocks (82.9 %; single, dual or three-party) |
| Time span | **2011-04-19** to **2026-06-30** (15.2 years) |
| Languages | **24** languages (EN 81.2 %, JA 4.9 %, rest across 22 languages) |
| Issuing Companies | **2,014** distinct fictional companies across **33** countries |
| Unique Visual Identities | **201,399** individual company Design-DNA signatures |

## Quick start

The Parquet files under `data/` hold one row per document: all manifest fields plus the extracted
text, so the dataset can be browsed in the Dataset Viewer above and loaded directly:

```python
from datasets import load_dataset

ds = load_dataset("sinabis-group/sinabis-1m-synthetic-docx", split="train")
print(ds[0]["title"])
print(ds[0]["text"])
```

The `text` column holds the text of the document body in reading order (paragraphs, headings, lists and table cells, one per line). Headers and footers (letterhead, contact bar, page numbers) are not included. The original `.docx` files with their full layout are in the ZIP archives.

## Downloads

The dataset is packaged in five ZIP archives (4.2–8.4 GB each) for fast parallel downloads and streaming:

| File | Size | Contents |
|---|---:|---|
| `data/train-*.parquet` (11 files) | 2.62 GB | Manifest fields + extracted `text`, one row per document (Dataset Viewer, `load_dataset`) |
| `Sinabis_1M_docx_part_01.zip` | 8.41 GB | `337,997` DOCX files (8.71 GB uncompressed) |
| `Sinabis_1M_docx_part_02.zip` | 4.16 GB | `167,000` DOCX files (4.31 GB uncompressed) |
| `Sinabis_1M_docx_part_03.zip` | 4.16 GB | `167,000` DOCX files (4.30 GB uncompressed) |
| `Sinabis_1M_docx_part_04.zip` | 4.16 GB | `167,000` DOCX files (4.31 GB uncompressed) |
| `Sinabis_1M_docx_part_05.zip` | 4.16 GB | `167,000` DOCX files (4.30 GB uncompressed) |

`Sinabis_1M_docx_manifest.zip` holds the JSON Lines records for all 1,005,997 documents
(see "Folder structure" below).

### Unpacking

All archives share a unified directory structure. Unpacking them into the same directory
merges all files seamlessly. Each part also contains the manifest files of its own documents, and the
manifest ZIP bundles all of them, so `unzip -o` simply overwrites identical files:

```bash
# Download and unpack with the Hugging Face CLI
hf download sinabis-group/sinabis-1m-synthetic-docx --repo-type dataset --local-dir sinabis-1m-docx
cd sinabis-1m-docx
for z in Sinabis_1M_docx_*.zip; do unzip -qo "$z"; done
```

## Folder structure

In the repository:

```
.
├── README.md
├── data/
│   └── train-*.parquet                 (rows for the Dataset Viewer and load_dataset)
├── Sinabis_1M_docx_part_01.zip … part_05.zip    → word/
└── Sinabis_1M_docx_manifest.zip                 → manifest/
```

After unpacking all archives into one directory:

```
sinabis-1m-docx/
├── word/
│   ├── service_contract/
│   │   ├── 0000/
│   │   │   ├── 0000000_CTR-2023-014.docx
│   │   │   └── ...
│   │   └── ...
│   ├── nda/
│   ├── meeting_minutes/
│   ├── sop_policy/
│   └── ... (55 document types)
└── manifest/
    ├── wb00000.jsonl
    ├── wb00001.jsonl
    └── ...
```

`Sinabis_1M_docx_manifest.zip` unpacks to the `manifest/` folder. Each `wbNNNNN.jsonl` contains
one record per document:
- `file`: Relative path to the `.docx` file
- `format`: `"docx"`
- `theme`: Document theme (e.g. `service_contract`, `nda`, `meeting_minutes`)
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
| `business_letter` | 57,477 | 5.7 % | Business letter on a concrete operational matter (coordination, information, request, follow-up) |
| `service_contract` | 50,290 | 5.0 % | Service / framework agreement between a contractor and a client (scope, service levels, rates, term, liability, governing law) |
| `meeting_minutes` | 43,117 | 4.3 % | Minutes of a meeting (attendees, agenda, discussion per item, decisions, action items with owners and due dates) |
| `project_proposal` | 43,074 | 4.3 % | Technical and commercial project proposal / offer (situation, approach, work packages, schedule, prices, assumptions, validity) |
| `nda` | 28,773 | 2.9 % | Mutual or one-way non-disclosure agreement (purpose, definition of confidential information, obligations, exceptions, term, penalties) |
| `internal_memo` | 28,751 | 2.9 % | Internal memo / management circular to staff on a policy, change or announcement |
| `employment_contract` | 28,745 | 2.9 % | Employment contract for a named employee (position, duties, working hours, probation, salary, leave, notice, confidentiality) |
| `project_report` | 28,730 | 2.9 % | Project status report (management summary, progress per work stream, milestones, budget, risks, next steps) |
| `sop_policy` | 28,722 | 2.9 % | Standard operating procedure or company policy (purpose, scope, responsibilities, procedure steps, records, revision history) |
| `subcontractor_agreement` | 21,569 | 2.1 % | Subcontractor agreement for construction or installation works (scope, schedule, remuneration, safety, insurance, penalties) |
| `maintenance_report` | 21,567 | 2.1 % | Technical maintenance / service report (object data, work performed, measurements, defects found, recommendations) |
| `purchase_agreement` | 21,567 | 2.1 % | Purchase / supply agreement for specific goods or equipment (object, price, delivery, acceptance, warranty, retention of title) |
| `invoice` | 21,560 | 2.1 % | Invoice with itemised goods or services, totals and payment terms |
| `dunning_letter` | 21,555 | 2.1 % | Payment reminder or formal dunning letter with list of open items, fees and deadline |
| `lease_agreement` | 21,547 | 2.1 % | Commercial lease for premises, land, roof space or equipment (object, term, rent, deposit, maintenance, return) |
| `request_for_quotation` | 18,690 | 1.9 % | Request for quotation / tender invitation describing requirements, quantities, deadlines and evaluation criteria |
| `handover_protocol` | 18,681 | 1.9 % | Acceptance / handover protocol (object, participants, documents handed over, defects list, acceptance statement) |
| `change_request` | 18,680 | 1.9 % | Change request / variation order for a project (description, reason, impact on cost and schedule, approval) |
| `maintenance_contract` | 18,678 | 1.9 % | Maintenance / service-level contract for technical installations (intervals, response times, spare parts, flat fee, exclusions) |
| `termination_letter` | 17,251 | 1.7 % | Formal termination of a contract or business relationship, stating the contract, notice period, end date and next steps |
| `authority_notice` | 17,251 | 1.7 % | Official notice / decision from a public authority (permit, fee assessment, inspection result, objection rights) |
| `contract_amendment` | 17,251 | 1.7 % | Amendment / addendum to an existing contract changing specific clauses (price, term, scope), referencing the original contract |
| `quote` | 17,250 | 1.7 % | Quotation / cost estimate with items, prices, validity and terms |
| `audit_report` | 17,243 | 1.7 % | Quality, HSE or supplier audit report (scope, method, findings by area with ratings, nonconformities, corrective actions) |
| `complaint_letter` | 17,238 | 1.7 % | Complaint about a defective delivery or poor service, describing the defects and demanding remedy |
| `consulting_agreement` | 17,236 | 1.7 % | Consulting / advisory agreement (mandate, deliverables, fees per day or hour, reporting, IP rights, termination) |
| `work_instruction` | 17,228 | 1.7 % | Operating / work instruction for a machine, workplace or hazardous substance (hazards, protective measures, behaviour in emergencies, first aid, disposal) |
| `inspection_report` | 14,397 | 1.4 % | Inspection / test report with test items, results, pass/fail, deviations and inspector statement |
| `incident_report` | 14,386 | 1.4 % | Incident / accident / outage report (timeline, cause analysis, impact, immediate and long-term measures) |
| `job_posting` | 14,380 | 1.4 % | Job advertisement (company intro, tasks, profile, benefits, how to apply) |
| `risk_assessment` | 14,379 | 1.4 % | Workplace risk assessment (activity, hazards, risk rating, measures, responsible persons, review date) |
| `complaint_response` | 14,376 | 1.4 % | Response to a customer complaint (acknowledgement, root cause, corrective actions, goodwill offer) |
| `data_processing_agreement` | 14,369 | 1.4 % | Data processing agreement under GDPR-like rules (subject, categories of data, technical and organisational measures, sub-processors, audits) |
| `press_release` | 14,364 | 1.4 % | Press release announcing a company news item (project, partnership, results, appointment) with quotes and boilerplate |
| `purchase_order` | 12,942 | 1.3 % | Purchase order to a supplier with an itemised order table (item, quantity, unit price, total), delivery address, delivery date and purchasing conditions |
| `feasibility_study` | 12,939 | 1.3 % | Feasibility study / concept paper (initial situation, options compared, cost estimate, risks, recommendation) |
| `technical_specification` | 12,928 | 1.3 % | Technical specification / requirements document (purpose, system context, functional and non-functional requirements, interfaces, acceptance criteria) |
| `training_handout` | 12,926 | 1.3 % | Training handout / course material on a professional topic with learning goals, explanations, examples and quiz questions |
| `reference_letter` | 11,507 | 1.1 % | Employment reference / job testimonial for a named former employee describing tasks, performance and conduct |
| `license_agreement` | 11,498 | 1.1 % | Software or technology license agreement (licensed subject, scope of use, fees, updates, support, liability) |
| `order_confirmation` | 11,498 | 1.1 % | Order confirmation with items, delivery date and terms |
| `onboarding_plan` | 11,495 | 1.1 % | Onboarding plan / checklist for a new employee (first day, first weeks, contacts, trainings, equipment) |
| `invitation_letter` | 11,492 | 1.1 % | Invitation to an event, site visit, training or opening (agenda, location, registration) |
| `price_change_notice` | 11,491 | 1.1 % | Notice of price adjustment or changed terms, with reasons, effective date and new price list |
| `customer_newsletter` | 11,490 | 1.1 % | Customer or partner newsletter with several short news articles |
| `it_security_policy` | 11,490 | 1.1 % | IT security / acceptable-use policy (passwords, devices, data classification, incidents, sanctions) |
| `delivery_note` | 10,065 | 1.0 % | Delivery note listing delivered items and quantities with receipt confirmation |
| `organisational_announcement` | 10,058 | 1.0 % | Organisational announcement (new appointment, restructuring, office move) to employees |
| `market_analysis` | 10,057 | 1.0 % | Market or competitor analysis (market size, segments, trends, competitors, SWOT, conclusions) |
| `travel_expense_policy` | 10,052 | 1.0 % | Travel and expense policy (booking rules, allowances, reimbursement process, approval limits) |
| `expert_opinion` | 8,636 | 0.9 % | Expert opinion / assessment report on a technical or commercial question (assignment, findings, assessment, conclusion) |
| `power_of_attorney` | 8,629 | 0.9 % | Power of attorney / authorisation for a named person to act on behalf of the company for defined matters |
| `shareholder_resolution` | 8,627 | 0.9 % | Shareholder or board resolution (meeting details, resolutions with voting results, signatures) |
| `lessons_learned` | 8,625 | 0.9 % | Lessons learned / post-project review (what went well, what did not, root causes, recommendations) |
| `annual_business_report` | 7,180 | 0.7 % | Management report section of an annual report (business development, financial position, employees, outlook, risks) |

## Document Families

| Family | Documents | Share |
|---|---:|---:|
| `letter` | 281,636 | 28.0 % |
| `contract` | 251,523 | 25.0 % |
| `corporate` | 224,154 | 22.3 % |
| `report` | 175,369 | 17.4 % |
| `commercial` | 73,315 | 7.3 % |

## Document Length

| Length class | Documents | Share |
|---|---:|---:|
| long (≈1,200–2,200) | 248,413 | 24.7 % |
| medium (≈550–1,100) | 386,988 | 38.5 % |
| short (≈220–480 words) | 285,866 | 28.4 % |
| very long (≈2,300–3,800) | 84,730 | 8.4 % |

## Language Distribution

| Language | Documents | Share |
|---|---:|---:|
| English (`en`) | 817,210 | **81.2 %** |
| Japanese (`ja`) | 49,227 | **4.9 %** |
| Chinese (`zh`) | 47,587 | **4.7 %** |
| German (`de`) | 16,986 | **1.7 %** |
| Portuguese (`pt`) | 8,362 | **0.8 %** |
| Spanish (`es`) | 8,123 | **0.8 %** |
| Italian (`it`) | 6,559 | **0.7 %** |
| French (`fr`) | 5,785 | **0.6 %** |
| Swedish (`sv`) | 4,881 | **0.5 %** |
| Dutch (`nl`) | 4,710 | **0.5 %** |
| Polish (`pl`) | 4,115 | **0.4 %** |
| Korean (`ko`) | 3,950 | **0.4 %** |
| Indonesian (`id`) | 3,690 | **0.4 %** |
| Hungarian (`hu`) | 3,158 | **0.3 %** |
| Danish (`da`) | 2,838 | **0.3 %** |
| Norwegian (`nb`) | 2,405 | **0.2 %** |
| Finnish (`fi`) | 2,359 | **0.2 %** |
| Czech (`cs`) | 2,358 | **0.2 %** |
| Ukrainian (`uk`) | 2,250 | **0.2 %** |
| Vietnamese (`vi`) | 2,219 | **0.2 %** |
| Turkish (`tr`) | 2,206 | **0.2 %** |
| Greek (`el`) | 1,965 | **0.2 %** |
| Romanian (`ro`) | 1,870 | **0.2 %** |
| Russian (`ru`) | 1,184 | **0.1 %** |

## Layout Variety

| Layout dimension | Variants used | Most frequent |
|---|---|---|
| Letterhead archetype | 12 variants | `logo_left_info_right` 10 %, `din_letterhead` 10 %, `underline_bar` 10 %, `minimal_text` 9 % |
| Heading numbering | 8 variants | `none` 30 %, `num` 25 %, `num_dot` 14 %, `article` 10 % |
| Heading style | 7 variants | `color` 23 %, `rule` 22 %, `caps` 12 %, `bar` 12 % |
| Title style | 7 variants | `rule` 15 %, `right_big` 14 %, `big` 14 %, `band` 14 % |
| Table style | 8 variants | `zebra` 13 %, `hlines` 13 %, `boxed_round` 13 %, `grid` 13 % |
| Footer style | 6 variants | `none` 17 %, `contact_bar` 17 %, `line` 17 %, `two_line` 17 % |
| Body font | 26 variants | `Arial` 25 %, `Times New Roman` 11 %, `Georgia` 7 %, `Calibri` 6 % |

Special layouts: cover page **11.4 %**, table of contents **19.2 %**, two-column layout **1.7 %**, watermark **4.3 %**, line numbering **3.0 %**.

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

> Sinabis GmbH (2026). Sinabis Green Energy – Synthetic Document Dataset (1M DOCX).
> https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-docx

## Citation

```bibtex
@misc{sinabis_green_docx_dataset_2026,
  author = {{Sinabis GmbH}},
  title  = {Sinabis Green Energy -- Synthetic Document Dataset (1M DOCX)},
  year   = {2026},
  url    = {https://huggingface.co/datasets/sinabis-group/sinabis-1m-synthetic-docx}
}
```
