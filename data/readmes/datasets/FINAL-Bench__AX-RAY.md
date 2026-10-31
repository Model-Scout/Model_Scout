---
pretty_name: AX-Ray AI/AX Safety Diagnostics Dataset
language:
- en
- ko
license: cc-by-nc-4.0
task_categories:
- text-generation
- question-answering
size_categories:
- n<1K
tags:
- ai-safety
- ax-safety
- ai-evaluation
- model-evaluation
- model-audit
- safety-diagnostics
- deployment-readiness
- causal-leakage
- causal-integrity
- responsible-ai
- ai-governance
- governance
- leaderboard
- red-teaming
- regulatory-compliance
- risk-assessment
- model-safety
- llm-evaluation
- ai-compliance
- korean-ai
- final-bench
- ax-ray
- text
annotations_creators:
- expert-generated
source_datasets:
- original
configs:
- config_name: default
  data_files:
  - split: catalog
    path: data/catalog.jsonl
---

# AX-RAY

[![Explore the AX-Ray Space](https://img.shields.io/badge/Explore-AX--Ray-0c8c82)](https://huggingface.co/spaces/FINAL-Bench/AX-RAY)
[![117 diagnostic items](https://img.shields.io/badge/Diagnostics-117-d34450)](https://huggingface.co/datasets/FINAL-Bench/AX-RAY)

AX-RAY is the versioned, machine-readable AI safety, AX safety, model evaluation, and deployment-readiness criteria catalog behind the [FINAL-Bench AX-Ray Space](https://huggingface.co/spaces/FINAL-Bench/AX-RAY). It organizes 117 AI/AX safety diagnostic criteria, including causal-leakage and causal-integrity review items, across model-intrinsic and deployment/operations assessment axes.

The catalog is **English-primary and bilingual**. Every record has item-specific technical English for diagnostic focus, failure rationale, public detection guidance, and remediation guidance. The Korean source fields are retained for provenance and protected by a per-record fingerprint. The English layer is a technical editorial draft prepared directly from those source fields and awaits owner approval; it is not presented as an independently verified translation or as proof that an embedded reference is correct.

> **Publication status:** private Hub release candidate; not publicly released. The license is selected; public visibility, final publication wording, and editorial approval remain owner gates.

## Dataset Design

| Property | Value |
|---|---|
| Unit of analysis | One diagnostic criterion, not a prompt or model response |
| Records | 117, with 117 unique stable IDs |
| Axes | MODEL-SCAN 89; AX-SCAN 28 |
| Categories | D1-D8, AX-A, AX-B, AX-C |
| Primary split | `catalog` |
| Formats | JSONL canonical; CSV convenience mirror |
| Record integrity | SHA-256 fingerprint of the source fields in every record |
| English content coverage | 117/117 records with four item-specific technical fields |
| Result semantics | Criteria only; no leaderboard score, certification, or model verdict |
| Evidence status | Catalog references; row-level primary-source review required |
| Governance status | Informative mapping; current-law review required; not legal advice |

`catalog` is used instead of `train`: these records define what to assess and what evidence to seek. They are not training examples and are not intended to optimize a model toward disclosed test prompts.

## What Is Included

- 117 stable diagnostic records
- 89 MODEL-SCAN items and 28 AX-SCAN items
- 11 categories covering causal integrity, reliability, robustness, safety, data integrity, efficiency, internal diagnostics, remediation, serving, infrastructure security, and compliance
- English titles plus item-specific diagnostic focus, failure rationale, public detection guidance, and remediation guidance
- Assessment mode and expected evidence class for each criterion
- Korean source details retained as the item-specific source text
- Severity, automation level, evidence pointers, and seven-jurisdiction governance-reference fields
- Per-record source fingerprints and explicit review-status fields
- Links back to the AX-Ray Space for presentation and model-level reports

## What Is Not Included

- Proprietary probes, exact thresholds, judging prompts, or internal scoring recipes
- Raw model outputs, private reports, credentials, or access tokens
- Model leaderboard results or certification decisions
- Independently enumerated AGENT-SCAN records; the current 117-item source catalog consists of MODEL-SCAN and AX-SCAN records
- Claims that every embedded paper, issue, law, or article mapping has been independently re-verified in this release candidate
- An empirical interpretation of source severity, automation, assurance, or service-tier labels; these are explicitly retained as source-catalog editorial metadata

## Intended Uses

- Build auditable AI-safety evaluation plans
- Map model and deployment risks to evidence requirements
- Create internal control checklists and regression gates
- Compare diagnostic coverage across evaluation programs
- Teach the difference between capability scores and deployment readiness

## Non-Intended Uses

- Treating a checklist entry as proof that a model is safe
- Claiming regulatory certification or legal compliance from this dataset alone
- Using the governance mappings as legal advice
- Reconstructing undisclosed AX-Ray probes or decision thresholds

## Data Files

- `data/catalog.jsonl`: canonical Hugging Face split
- `data/catalog.csv`: spreadsheet-compatible mirror of the same 117 records
- `dataset_info.json`: generated counts, file hashes, source hash, and claim boundaries
- `LICENSE`: repository-level CC BY-NC 4.0 notice and canonical legal-code links
- `NOTICE.md`: licensed-material scope, VIDRAFT attribution, third-party exclusions, and commercial-licensing route
- `VALIDATION.md`: reproducible local validation result
- `CONTENT_AUDIT.md`: measured editorial coverage, evidence status, and residual review gates
- `english_details.json`: version-controlled item-specific English editorial layer
- `verify_dataset.mjs`: executable release gate for counts, parity, provenance, claims, links, and secret scanning
- `METHODOLOGY.md`: taxonomy, evidence model, assessment workflow, and review policy
- `REFERENCES.md`: verified official backbone sources and citation policy
- `SCHEMA.md`: field-level data contract
- `RELEASE_CHECKLIST.md`: publication gates requiring owner approval

## Data Structure

The primary split is `data/catalog.jsonl`; a CSV mirror is provided for spreadsheet workflows. `catalog` is used deliberately because these records are evaluation criteria, not model-training examples. Each record includes:

- `diagnostic_id`: stable ID such as `AXSAFE-D1-001`
- `scan_axis`: `MODEL-SCAN` or `AX-SCAN`
- `category_code`, `category_name_en`, `item_number`
- `title_en`, `evaluation_question_en`, `scope_en`, `category_risk_context_en`
- `diagnostic_focus_en`, `risk_if_failed_en`
- `public_assessment_guidance_en`, `public_remediation_guidance_en`
- `assessment_mode`, `expected_evidence_class`, and `record_semantics`
- severity, automation, assurance, tier, evidence, and governance-reference fields
- Korean source fields ending in `_ko`
- `source_record_sha256` and evidence/governance review-status fields
- source-text, classification, severity, English-editorial, and legal-summary status fields
- mutual links to this Dataset and the AX-Ray Space

See [SCHEMA.md](SCHEMA.md) for the data contract, [METHODOLOGY.md](METHODOLOGY.md) for the assessment design, and [VALIDATION.md](VALIDATION.md) for generated counts and checksums.

Run the release gate from the repository root with:

```bash
node verify_dataset.mjs
```

The command is read-only and must report `status: PASS` before publication.

## Evidence and Authority Model

AX-RAY distinguishes three things that safety datasets often blur:

1. **Criterion**: the risk or control that should be assessed.
2. **Evidence requirement**: the measurement, artifact, control record, or document needed to assess it.
3. **Decision**: a model- or deployment-specific result produced outside this catalog.

The dataset contains the first two. Decisions, scores, and causal-leak findings belong in versioned AX-Ray reports and are not copied into the criteria catalog.

Official backbone references were checked on 2026-08-14 and are listed in [REFERENCES.md](REFERENCES.md). The source catalog contains an evidence pointer for 117/117 records and a legal summary for 98/117; 19/117 legal summaries are explicitly marked as not provided. Embedded row-level citations remain source pointers until individually checked against primary publications. Completed row-level primary-source reviews and legal reviews are both 0/117 in this release candidate, and that status is represented in data rather than hidden in prose.

## Claim Boundaries

This dataset is an evaluation-criteria catalog, not proof of safety, model certification, or legal compliance. Source severity is an editorial prioritization label rather than an empirical probability or impact estimate. Evidence and governance references may become outdated; users must verify current primary sources and obtain qualified legal advice where needed.

Causal leakage is treated as a structural temporal-integrity defect. It does not by itself prove malicious intent, robotic violence, or hacking capability. Harm becomes plausible when a defect is combined with direct actuation, broad tool permissions, weak isolation, or missing independent safety controls.

## Versioning

The staged version is `1.0.0-rc1`. Stable diagnostic IDs are intended to survive wording improvements. Material changes to scope, evidence semantics, or category meaning require a version change and changelog entry. Any future AGENT-SCAN release must use an explicit schema/version update rather than silently changing the 117-record baseline.

## License

Except where otherwise noted, AX-RAY's original dataset contents and accompanying documentation are licensed by **VIDRAFT** under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/) (`CC BY-NC 4.0`). The Hugging Face metadata identifier is `cc-by-nc-4.0`.

This permits sharing and adaptation for noncommercial purposes, subject to attribution, a license link, and an indication of changes. Commercial use is not granted by CC BY-NC 4.0; VIDRAFT may provide a separate written commercial license. Entity type alone does not determine whether a use is noncommercial, so users should assess the purpose and context of the use and contact VIDRAFT when uncertain.

The license applies only to material that VIDRAFT has authority to license, including the original taxonomy and selection/arrangement, VIDRAFT-authored English editorial fields, schema, and documentation. Linked papers, standards, laws, product names, trademarks, and other third-party material remain subject to their respective rights. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md) for the controlling notice, attribution instructions, and scope boundaries.

Preferred attribution:

> AX-RAY by VIDRAFT, version 1.0, https://huggingface.co/datasets/FINAL-Bench/AX-RAY, licensed under CC BY-NC 4.0. Changes were made: [yes/no].

Commercial-license requests should be directed to VIDRAFT through the FINAL-Bench repository owner contact channel. No separate commercial permission is granted unless VIDRAFT provides it in writing.

## Citation

```bibtex
@dataset{finalbench_axray_2026,
  title  = {AX-RAY: AI/AX Safety and Deployment-Readiness Diagnostic Catalog},
  author = {{VIDRAFT}},
  publisher = {FINAL-Bench},
  year   = {2026},
  version = {1.0},
  url    = {https://huggingface.co/datasets/FINAL-Bench/AX-RAY}
}
```
