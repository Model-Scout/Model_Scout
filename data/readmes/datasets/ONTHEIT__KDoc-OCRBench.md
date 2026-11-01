---
language:
- ko
tags:
- ocr
- document-understanding
- korean
- benchmark
size_categories:
- n<10K
pretty_name: KDoc-OCRBench
extra_gated_heading: KDoc-OCRBench Access Request
extra_gated_description: >-
  This dataset contains real-world Korean industrial documents and is not
  openly redistributable. Access is granted on a case-by-case basis for
  research and evaluation purposes only. Please fill in the information below
  to request access.
extra_gated_fields:
  Full Name: text
  Company/Organization: text
  Email: text
  Intended Use (evaluation / research / other): text
  I agree not to redistribute this dataset: checkbox
extra_gated_button_content: Request access
---

# KDoc-OCRBench (Korean Document OCR Benchmark)

The first comprehensive Korean document OCR benchmark developed by [ONTHEIT](http://www.ontheit.com/).

**14,738 test cases across 804 Korean PDFs in 7 industrial document categories** — designed to fill the gap in standardized Korean OCR evaluation.

Existing OCR benchmarks are primarily English-focused, making it difficult to evaluate model performance on Korean documents. KDoc-OCRBench addresses this gap with real-world Korean documents spanning contracts, medical records, financial forms, logistics paperwork, educational materials, government documents, and presentation slides.

## Overview

- **804 Korean PDFs** across 7 document categories
- **14,738 unit-test-style assertions** covering text presence, text absence, table structure, and baseline quality
- Based on the [olmOCR-bench](https://huggingface.co/datasets/allenai/olmOCR-bench) methodology by Allen AI — each test is a focused assertion (e.g., "this text must appear", "this cell must be to the right of that cell") rather than a full-text comparison, making evaluation robust to formatting differences between models
- Korean-specific normalization for decorative spacing and multi-line table cells

## Dataset Structure

```
KDoc-OCRBench/
├── pdfs/                         # 804 PDF documents organized by category
│   ├── CorporateDocs/
│   ├── EducationalDocs/
│   ├── FinancialInsuranceDocs/
│   ├── LogisticsDocs/
│   ├── MedicalDocs/
│   ├── PresentationSlides/
│   └── PublicDocs/
├── long_tests.jsonl              # Text presence/absence tests (10,137)
├── table_tests.jsonl             # Table structure tests (4,147)
└── header_footer_tests.jsonl     # Header/footer tests (454)
```

## Test Types

| Type | Count | Description |
|------|------:|-------------|
| Text Presence (`present`) | 10,137 | Verifies specific Korean text appears in the output (with optional fuzzy matching) |
| Text Absence (`absent`) | 454 | Verifies certain text (e.g., page headers/footers) is NOT in the output |
| Table (`table`) | 4,147 | Validates table cell content and spatial relationships (up/down/left/right neighbors, column/row headings) |
| Baseline | 804 | Checks output is non-empty, not repeating, and contains valid characters (one per PDF) |

## Document Categories

### CorporateDocs (124 documents)
Corporate documents — employment contracts, service performance certificates, business plans, internal reports, meeting minutes, and more.

### EducationalDocs (158 documents)
Educational documents — preventive education materials, student residence surveys, curriculum guides, school support procedures, admission assignment notices, academic transcripts, and more.

### FinancialInsuranceDocs (64 documents)
Financial and insurance documents — securities issuance terms, payment notices, income deduction statements, credit transaction agreements, automatic transfer applications, insurance claim forms, and more.

### LogisticsDocs (72 documents)
Logistics documents — simplified customs declarations, price declarations, import customs clearance guides, goods requisitions, transaction statements, multimodal bills of lading, and more.

### MedicalDocs (118 documents)
Medical documents — medical records, medical opinions, diagnostic certificates, prescriptions, health checkup result notices, symptom and treatment records, medical fee receipts, and more.

### PresentationSlides (99 documents)
Presentation materials — major initiative progress and plans, social investment materials, social impact reports, collaboration strategy decks, and more.

### PublicDocs (169 documents)
Public documents — initial salary grade determination procedures, employment support program guides, performance indicator and weighting specifications, name change applications, leak detection reports, and more.

## Benchmark Results

See the leaderboard and evaluation code at [ONTHEIT-AI/BizOnAI-OCR](https://github.com/ONTHEIT-AI/BizOnAI-OCR).

## Credits

- Korean document data collected and labeled by [ONTHEIT](http://www.ontheit.com/)
- Evaluation methodology inspired by [olmOCR-bench](https://huggingface.co/datasets/allenai/olmOCR-bench) by Allen AI

## License & Access

This dataset contains real-world Korean industrial documents and is **not openly redistributable**. Access is granted on a case-by-case basis for research and evaluation purposes.

To request access, contact [ONTHEIT](http://www.ontheit.com/) at **bizonai@ontheit.com**. Granted users may use the dataset only for OCR evaluation and may not redistribute it.
