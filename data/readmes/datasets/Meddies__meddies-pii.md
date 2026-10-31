---
pretty_name: Meddies PII
language:
- vi
- en
- zh
- ja
- ko
- th
- fr
- de
- es
- pt
- ru
- id
- tl
- ms
- my
- lo
- ta
license: cc-by-nc-4.0
annotations_creators:
- machine-generated
language_creators:
- machine-generated
multilinguality: multilingual
size_categories:
- 1M<n<10M
source_datasets:
- original
configs:
- config_name: burmese
  data_files:
  - split: train
    path: burmese/train-*
- config_name: chinese
  data_files:
  - split: train
    path: chinese/train-*
- config_name: english
  data_files:
  - split: train
    path: english/train-*
- config_name: eval
  data_files:
  - split: train
    path: eval/train-*
- config_name: filipino
  data_files:
  - split: train
    path: filipino/train-*
- config_name: french
  data_files:
  - split: train
    path: french/train-*
- config_name: german
  data_files:
  - split: train
    path: german/train-*
- config_name: grpo-hard-train
  data_files:
  - split: train
    path: grpo-hard-train/train-*
- config_name: grpo-train
  data_files:
  - split: train
    path: grpo-train/train-*
- config_name: indonesian
  data_files:
  - split: train
    path: indonesian/train-*
- config_name: japanese
  data_files:
  - split: train
    path: japanese/train-*
- config_name: korean
  data_files:
  - split: train
    path: korean/train-*
- config_name: laos
  data_files:
  - split: train
    path: laos/train-*
- config_name: malay
  data_files:
  - split: train
    path: malay/train-*
- config_name: nvidia-health
  data_files:
  - split: train
    path: nvidia-health/train-*
- config_name: nvidia-non-health
  data_files:
  - split: train
    path: nvidia-non-health/train-*
- config_name: pii-bioes
  data_files:
  - split: train
    path: pii-bioes/train-*
  - split: validation
    path: pii-bioes/validation-*
- config_name: portuguese
  data_files:
  - split: train
    path: portuguese/train-*
- config_name: russian
  data_files:
  - split: train
    path: russian/train-*
- config_name: spanish
  data_files:
  - split: train
    path: spanish/train-*
- config_name: tamil
  data_files:
  - split: train
    path: tamil/train-*
- config_name: test
  data_files:
  - split: train
    path: test/train-*
- config_name: thai
  data_files:
  - split: train
    path: thai/train-*
- config_name: train
  data_files:
  - split: train
    path: train/train-*
- config_name: vietnamese
  default: true
  data_files:
  - split: train
    path: vietnamese/train-*
- config_name: vietnamese-translated
  data_files:
  - split: train
    path: vietnamese-translated/train-*
viewer: true
task_categories:
- token-classification
- text-generation
tags:
- medical
- healthcare
- pii
- de-identification
- ner
- synthetic
- multilingual
dataset_info:
  config_name: eval
  features:
  - name: language
    dtype: string
  - name: uid
    dtype: string
  - name: domain
    dtype: string
  - name: document_type
    dtype: string
  - name: document_description
    dtype: string
  - name: document_format
    dtype: string
  - name: locale
    dtype: string
  - name: text
    dtype: string
  - name: spans
    dtype: string
  - name: raw
    dtype: string
  - name: source
    dtype: string
  - name: input
    dtype: string
  - name: total_tokens
    dtype: int64
  - name: document_label
    dtype: string
  - name: document_length
    dtype: string
  - name: text_format
    dtype: string
  - name: edge_case
    dtype: string
  - name: label
    dtype: string
  splits:
  - name: train
    num_bytes: 23483995
    num_examples: 3758
  download_size: 11048486
  dataset_size: 23483995
---

# Meddies PII

<p align="left">
  <a href="https://huggingface.co/Meddies"><img alt="Meddies organization" src="https://img.shields.io/badge/Meddies-organization-0F766E"></a>
  <a href="https://meddies.ai"><img alt="Website" src="https://img.shields.io/badge/website-meddies.ai-0B4F6C"></a>
  <a href="mailto:contact@meddies.ai"><img alt="Email" src="https://img.shields.io/badge/contact-contact%40meddies.ai-1ABBC7"></a>
  <img alt="License" src="https://img.shields.io/badge/license-CC--BY--NC--4.0-475569">
</p>

Synthetic PII extraction data for multilingual clinical and administrative documents, with language-specific, domain-transfer, translation, and instruction-style views in one Hub repo.

> [!IMPORTANT]
> This is a synthetic de-identification research artifact for healthcare AI teams. It is not medical advice, not a privacy certification, and not a substitute for task-specific validation on your own data.
> If you want to use this dataset in commercial work, please contact us at [contact@meddies.ai](mailto:contact@meddies.ai).

<p align="center">
  <img src="./assets/hero-meddies-pii.png" alt="Title card for Meddies PII, a synthetic multilingual PII dataset for clinical and administrative documents" width="100%" />
</p>

## Why this dataset

When you build LLM systems for medicine, PII handling is not a side task. It is one of the load-bearing constraints.

A model can sound clinically useful and still be unsafe if it leaks names, identifiers, phone numbers, dates, or addresses. That breaks trust fast. At Meddies, protecting patient information sits at the top of the stack. It is not a compliance footnote after the model is trained. It is a core requirement for how healthcare AI should be built, evaluated, and shipped.

`Meddies PII` is built around that problem. It stresses the same de-identification task across multilingual synthetic medical documents, English domain-transfer records, mixed-source training views, translation/adaptation views, and chat-style extraction supervision. The point is not just to tag names in one tidy note. The point is to make de-identification systems survive changes in language, format, prompt shape, and downstream training setup.

## What is in this dataset

| Family | Rows | Configs | What it gives you |
| --- | ---: | --- | --- |
| Language-specific tagged documents | 831,746 | `vietnamese`, `english`, `chinese`, `japanese`, `korean`, `thai`, `french`, `german`, `spanish`, `portuguese`, `russian`, `indonesian`, `filipino`, `malay`, `burmese`, `laos`, `tamil` | Single-language synthetic medical and administrative documents with tagged text, raw text, and canonical label JSON. |
| Domain-transfer English subsets | 63,160 | `nvidia-health`, `nvidia-non-health` | English structured and unstructured records with `spans`, `domain`, `locale`, and the same canonical label target. |
| Mixed training and evaluation bundles | 76,160 | `train`, `eval`, `test` | Task-oriented mixtures with `source` provenance for training, evaluation, and smoke tests. |
| Instruction / GRPO supervision | 7,100 | `grpo-train`, `grpo-hard-train` | Chat-style extraction prompts, normalized JSON answers, and raw source text. |
| Translation / adaptation view | 10,000 | `vietnamese-translated` | Vietnamese adaptation records with `input`, `text`, `raw`, `label`, and token counts. |
| BIOES token-classification view | 162,499 | `pii-bioes` | Derived no-duplicate Meddies-9 char-span records for BIOES token-classification training and validation: 161,999 train rows plus 500 stratified validation rows, with every Meddies language config represented, external rows restricted to Meddies-supported languages, and 11,554 targeted Vietnamese/English private-URL/secret augmentation rows. Rows over 4,096 LFM2.5 tokenizer tokens are excluded. |

These counts are not additive across the whole repo. Several task-oriented configs are derived views over the underlying source families rather than independent corpora.

> **BIOES training view:** `pii-bioes` is a derived Meddies-9 training view for token-classification/BIOES experiments. It uses `text` plus a `label` list of character spans (`category`, `start`, `end`, `text`) instead of inline tags, and expands the taxonomy to nine labels: `address`, `company_name`, `date`, `email_address`, `human_name`, `id_number`, `phone_number`, `private_url`, and `secret`. The validation split has 500 held-out rows with at least 50 documents per label and a 250 Vietnamese / 150 English / 100 other-language mix. The train split includes all Meddies language groups: Burmese, Chinese, English, Filipino, French, German, Indonesian, Japanese, Korean, Laos, Malay, Portuguese, Russian, Spanish, Tamil, Thai, and Vietnamese, restricted supported-language general-domain rows from Nemotron and ai4privacy, and targeted Vietnamese/English augmentation for private portals, secrets, adversarial obfuscation, and structured clinical payloads. The name is Meddies-specific; OpenAI Privacy Filter uses BIOES internally but does not define a dataset config called `pii-bioes`.

**2026-05-15 augmentation:** the `pii-bioes` train split now includes 11,554 additional no-duplicate targeted rows from MiMo generation: 8,228 Vietnamese accepted rows, 2,768 English accepted rows, 451 Vietnamese repaired-reject rows, and 107 English repaired-reject rows. Ten otherwise-valid Vietnamese candidates were dropped because they exceeded the 4,096-token LFM2.5 training limit; 16 risky repaired candidates remain quarantined and are not included.

Across the inspected configs, the canonical supervision target stays stable:

- **Tagged text:** `text` stores inline labels in the form `[value]<label>`.
- **Raw text:** `raw` stores the same record without inline tags.
- **Canonical label JSON:** `label` is a JSON string over exactly seven entity families: `address`, `company_name`, `date`, `email_address`, `human_name`, `id_number`, and `phone_number`.
- **Metadata:** single-language configs add `language`, `document_type`, `document_label`, `document_length`, `text_format`, and `edge_case`.
- **Domain-transfer extras:** `nvidia-health` and `nvidia-non-health` add `uid`, `domain`, `document_description`, `document_format`, `locale`, and `spans`.
- **Task-view extras:** `train`, `eval`, and `vietnamese-translated` add provenance or prompt-side fields such as `source`, `input`, and `total_tokens`.
- **Instruction-style configs:** `grpo-train` and `grpo-hard-train` replace document metadata with `prompt`, `answer`, `raw_text`, and `source`.

<details>
<summary>Schema summary</summary>

| Field | Type | Description |
| --- | --- | --- |
| `text` | `string` | Tagged document text with inline markers such as `[Nguyễn Hoa]<human_name>`. |
| `raw` | `string` | Untagged version of the same record. |
| `label` | `string` | JSON string mapping the seven canonical entity families to extracted values. |
| `language` | `string` | Release language for the language-specific or mixed-source views. |
| `document_type` | `string` | Coarse document category such as `PRESCRIPTION` or `MORTALITY_REPORT`. |
| `document_label` | `string` | Human-readable document label paired with `document_type`. |
| `document_length` | `string` | Length bucket such as `SHORT`, `MEDIUM`, or `LONG`. |
| `text_format` | `string` | Render format such as `FHIR_JSON`, `HL7_V2`, `XML`, `LIST`, or `PLAIN_TEXT`. |
| `spans` | `string` | JSON-like span annotations exposed in the domain-transfer subsets. |
| `source` / `input` / `total_tokens` | `string` / `int64` | Provenance and prompt-side fields used by the mixed, translation, and GRPO views. |
| `prompt` / `answer` / `raw_text` | mixed | Chat-style instruction inputs and normalized target JSON for GRPO configs. |

</details>

<details>
<summary>Full config index with row counts</summary>

### Language-specific configs

| Config | Rows | Notes |
| --- | ---: | --- |
| `vietnamese` | 45,921 | Vietnamese tagged medical and administrative records. |
| `english` | 47,744 | English tagged medical and administrative records. |
| `chinese` | 49,908 | Chinese tagged records. |
| `japanese` | 49,604 | Japanese tagged records. |
| `korean` | 48,621 | Korean tagged records. |
| `thai` | 44,734 | Thai tagged records. |
| `french` | 49,757 | French tagged records. |
| `german` | 49,655 | German tagged records. |
| `spanish` | 49,708 | Spanish tagged records. |
| `portuguese` | 49,643 | Portuguese tagged records. |
| `russian` | 49,428 | Russian tagged records. |
| `indonesian` | 49,816 | Indonesian tagged records. |
| `filipino` | 49,820 | Filipino tagged records. |
| `malay` | 49,836 | Malay tagged records. |
| `burmese` | 49,228 | Burmese tagged records. |
| `laos` | 48,788 | Lao tagged records. |
| `tamil` | 49,535 | Tamil tagged records. |

### Task-oriented and derived configs

| Config | Rows | Notes |
| --- | ---: | --- |
| `nvidia-health` | 13,160 | English health-adjacent domain-transfer subset with `spans`. |
| `nvidia-non-health` | 50,000 | English non-health domain-transfer subset with `spans`. |
| `train` | 71,402 | Mixed-source training bundle spanning 20 upstream source configs. |
| `eval` | 3,758 | Mixed-language evaluation slice. |
| `test` | 1,000 | Minimal smoke-test subset with `text`, `raw`, and `label`. |
| `vietnamese-translated` | 10,000 | Vietnamese translation / adaptation records. |
| `grpo-train` | 3,100 | Chat-format extraction supervision. |
| `grpo-hard-train` | 4,000 | Harder chat-format extraction supervision. |

</details>

## How this data is created

We create this release with synthetic data generated by LLMs, but the important design choice is not simply “use an LLM.” The important design choice is dynamic templating backed by QA and canonical normalization.

Instead of generating one rigid note shape and repeating it across languages, we vary the same de-identification task across document type, paired document label, length bucket, surface format, edge-case brief, and locale-specific naming and address patterns. That is deliberate. If the template stays fixed, the downstream model learns the template. If the surface changes while the ontology stays stable, the downstream model has to learn extraction behavior instead. That is how we try to make PII handling more tolerant across languages and document styles.

<p align="center">
  <img src="./assets/pipeline-meddies-pii.png" alt="Dynamic template axes and locale rules feed LLM generation, then QA and normalization, before Meddies PII is published into language, domain-transfer, split, GRPO, and translation release families" width="100%" />
</p>

*Figure 1. Dynamic template axes and locale rules feed LLM generation; QA and normalization turn that variation into the five Meddies PII release families.*

In the inspected language-specific family, the stable generation axes are:

| Axis | Verified scope | Why it matters |
| --- | --- | --- |
| `document_type` | 16 categories in both `vietnamese` and `english` | changes the clinical or administrative context the extractor sees |
| `document_label` | 32 values in `vietnamese`, 16 in `english` | the human-readable label layer is localized instead of being frozen into one naming scheme |
| `document_length` | 3 buckets in both: `SHORT`, `MEDIUM`, `LONG` | prevents overfitting to one note size |
| `text_format` | 10 surface formats in both | forces robustness across structured and messy renderings |
| `edge_case` | 20 values in `vietnamese`, 10 in `english` | pushes the generator toward harder and less repetitive examples |
| `label` ontology | 7 canonical entity families across representative configs | keeps the target stable while the surface varies |

The ontology is intentionally normalized into seven entity families instead of a long brittle tag list:

| Tag | What it captures |
| --- | --- |
| `address` | Addresses and ZIP or postal-code style location strings |
| `company_name` | Hospitals, clinics, departments, facilities, and organization names |
| `email_address` | Email addresses |
| `human_name` | Person names across first, middle, last, or honorific-heavy variants |
| `phone_number` | Phone and fax numbers |
| `id_number` | MRNs, SSNs, account numbers, license or certificate numbers, beneficiary IDs, device IDs, vehicle IDs, IP-like identifiers, and similar administrative identifiers |
| `date` | Birth dates, admission dates, discharge dates, death dates, and related time references |

## Coverage and diagnostics

The core question is simple: does the release keep the labeling task stable while the document surface changes hard enough to matter?

| Slice | Rows | Concrete proof |
| --- | ---: | --- |
| 17 language-specific configs | 831,746 | The inspected `vietnamese` and `english` subsets each expose 16 document types and 10 text formats, while the full language family spans 17 languages. |
| `nvidia-health` + `nvidia-non-health` | 63,160 | The English domain-transfer family spans 30 source domains across both structured and unstructured documents. |
| `train` | 71,402 | The mixed training bundle combines 20 upstream source configs, not just one language or one document family. |
| `eval` | 3,758 | The evaluation slice covers 17 languages, 679 document types, and 10 text formats in one Hub-ready view. |
| `grpo-train` + `grpo-hard-train` | 7,100 | The instruction views convert the same task into chat-style prompts with normalized JSON answers. |

A second consistency check matters just as much: across the inspected configs `vietnamese`, `english`, `nvidia-health`, `nvidia-non-health`, `train`, `eval`, `test`, and `vietnamese-translated`, the parsed `label` JSON always normalized to the same seven canonical entity keys.

That does not make this a finished benchmark. It makes the repo internally legible: different surfaces, same target ontology.

## Where it fits in the pipeline

Use `Meddies PII` upstream of model tuning, evaluator building, or span-normalization experiments.

The release logic is: choose the dynamic template axes, localize the surface to the target language and entity conventions, generate paired raw and tagged records with the LLM, then review and normalize everything into the same seven canonical entity families before publishing the release families.

That ordering matters. If you only release one surface form, the downstream model learns shortcuts. If you vary the surface while keeping the ontology stable, the downstream model has to learn extraction behavior instead.

## Access and quick start

The repo is public. For reproducibility, explicit config names are clearer whenever you want a specific release view.

```python
from datasets import load_dataset

# Language-specific medical/admin documents
vi = load_dataset("Meddies/meddies-pii", "vietnamese", split="train")
en = load_dataset("Meddies/meddies-pii", "english", split="train")

# English domain-transfer stress sets
non_health = load_dataset("Meddies/meddies-pii", "nvidia-non-health", split="train")

# Mixed evaluation slice
mixed_eval = load_dataset("Meddies/meddies-pii", "eval", split="train")

# Chat-style extraction supervision
grpo = load_dataset("Meddies/meddies-pii", "grpo-train", split="train")

print(vi[0]["text"][:220])
print(en[0]["label"])
print(non_health[0]["spans"][:220])
print(mixed_eval[0]["source"])
print(grpo[0]["answer"])
```

## Good fits

Use this release when de-identification behavior matters more than one specific benchmark recipe.

Good fits include multilingual PII extraction, de-identification robustness across clinical and administrative formats, span-to-JSON normalization, domain-shift testing with English non-health documents, and instruction or RL-style supervision for extraction models.

## Limits

This repo is synthetic. Treat it that way.

- Do not use it as evidence about real hospital PHI distributions, prevalence, or compliance risk.
- Do not mistake the repo for one clean, independent benchmark. `train`, `eval`, `test`, `grpo-*`, and `vietnamese-translated` are task-facing views over other release families, not fully independent corpora.
- The canonical `label` target is intentionally narrow: seven normalized entity families. If you need a broader PII taxonomy, you will need extra mapping or a different dataset design.
- Some useful fields are stored as strings rather than typed nested structures, including `label` JSON and `spans` payloads.
- This is not medical advice, and it does not certify downstream systems as safe or privacy-complete.

## Feedback

Send us the failures.

The most useful feedback is concrete: broken quickstart paths, mislabeled entities, formats that collapse your tokenizer, span/string mismatches, weak localization, or downstream de-identification failures you can reproduce.

You can find Meddies on Hugging Face at [huggingface.co/Meddies](https://huggingface.co/Meddies) and on the web at [meddies.ai](https://meddies.ai).

## Collaboration and sponsorship

Meddies is building verifiable clinical intelligence and the data infrastructure behind it.

We are a small team, and careful synthetic-data work still costs real review time and compute.

If this release matters to your research or product work—collaboration, sponsorship, evaluation, or clinician review—email us at [contact@meddies.ai](mailto:contact@meddies.ai).

## Citation

```bibtex
@dataset{meddies_pii_2026,
  title={Meddies PII: synthetic PII extraction data for multilingual clinical documents},
  author={MeddiesAI},
  year={2026},
  url={https://huggingface.co/datasets/Meddies/meddies-pii}
}
```
