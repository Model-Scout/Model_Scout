---
license: cc-by-4.0
language:
- ko
- en
task_categories:
- token-classification
size_categories:
- 10K<n<100K
source_datasets:
- ai4privacy/pii-masking-openpii-1.5m
tags:
- pii
- ner
- token-classification
- privacy
- pii-masking
- finance
- security
- infrastructure
- korean
- synthetic
pretty_name: Privacy Filter OpenPII Masking - Entity Detection (Korean/English)
---

# 1. Overview
`privacy-filter-openpii-masking` is a Korean and English entity-detection dataset for fine-tuning token-classification models. It is derived from [`ai4privacy/pii-masking-openpii-1.5m`](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m), relabeled to a 29-label taxonomy, and supplemented with statically authored or contextualized financial, customer-service/VOC, security, identity, and infrastructure scenarios.

The dataset provides entity annotations rather than application-specific redaction output. `masked_text` replaces every annotated span with a placeholder, including the non-PII disambiguation labels `PORT` and `ORGANIZATION`. A consuming system must decide how each detected label is handled after inference.

All rows are designed as synthetic training records. Values are either inherited from the synthetic ai4privacy corpus or generated locally under the controls described in [Section 3](#3-synthetic-data-safety). Public organization aliases are used only for the non-PII `ORGANIZATION` label. No operational sentence, identifier value, or complete customer record is copied into the artifacts.

## 1.1. TL;DR
* **72,375 rows** - 57,851 train and 14,524 validation rows.
* **333,741 annotated spans** across train and validation.
* **29 model labels** - 117 BIOES token classes under `4N+1`.
* **Korean and English** - English represents 25.74% of train and 26.03% of validation.
* **1024-token limit** - the observed maximum is 758 tokens in train and 801 in validation, with no truncation drops.
* **All labels in both languages and splits** - every one of the 29 labels has ko and en support in train and validation.

## 1.2. Quick Start
```python
from datasets import load_dataset

dataset = load_dataset("BCCard/privacy-filter-openpii-masking")
train = dataset["train"]
validation = dataset["validation"]

row = train[0]
row["source_text"]      # Unmasked model input.
row["tokens"]           # o200k subword token strings.
row["token_classes"]    # BIOES targets aligned with tokens.
row["privacy_mask"]     # Character-offset span annotations.
```

Train a token classifier using `tokens` and `token_classes`. The dataset stores token strings, not model input IDs. Convert them with the tokenizer described in Section 5.1. The published token sequence was produced with `add_special_tokens=False`; the 1024-token limit applies before any special tokens are added. If a model requires special tokens, add them in the training collator and assign an ignored label such as `-100` to those positions without changing the published token-to-label alignment. Use validation metrics for checkpoint selection and experiment comparison, and assess final generalization on an independently held-out evaluation set.

To reproduce the published token strings, load `openai/privacy-filter` with a fast tokenizer and call it with `add_special_tokens=False` and `truncation=False`.

<br>

# 2. Data Preparation
## 2.1. Pipeline
The v1 release combines relabeled ai4privacy rows with locally generated perturbation and synthesis rows.

```text
ai4privacy ko raw
  -> refine: relabel, merge spans, normalize Korean text, and apply safety controls
  -> perturbation: replace selected spans with split-specific generated values

ai4privacy en raw
  -> refine
  -> replay: retain rows for labels with at most 30 spans, then fill the quota with seed-42 sampling

static ko/en templates
  -> synthesis: materialize one row per authored template with local value generators

refine + perturbation + replay + synthesis
  -> mix: concatenate, shuffle with seed 42, tokenize, derive BIOES classes, and audit
  -> train / validation
```

The main rules for relabeling the upstream ai4privacy source labels - 37 labels, the union of 36 Korean and 34 English source labels - into the v1 taxonomy are:

* `GIVENNAME` and `SURNAME` are merged into a full `PERSON` span.
* `CITY`, `STREET`, and `BUILDINGNUM` are merged into `ADDRESS`; `ZIPCODE` remains separate.
* Korean `TAXNUM` values matching the resident-number form map to `RRN`; other values fall back to `GENERIC_ID`.
* `SOCIALNUM` maps to `SSN` in both languages.
* `ORGANISATION`, `BANKNAME`, and `HOSPITALNAME` map to `ORGANIZATION`.
* `TIME` maps to `DATE`, while `TIMEZONE` remains `O`.
* Source labels outside the label taxonomy in [Section 2.3](#23-label-taxonomy) are removed from `privacy_mask` and learned as `O`.

## 2.2. Splits
<div align="center">
    <img src="figures/language_distribution.png" width="65%" alt="Korean and English row counts split between train and validation" />
</div>

| split | rows | ko | en | spans | maximum tokens |
|---|---:|---:|---:|---:|---:|
| `train` | 57,851 | 42,963 (74.26%) | 14,888 (25.74%) | 266,846 | 758 |
| `validation` | 14,524 | 10,743 (73.97%) | 3,781 (26.03%) | 66,895 | 801 |
| **total** | **72,375** | **53,706 (74.21%)** | **18,669 (25.79%)** | **333,741** | **801** |

The final mix consists of the following pipeline components.

| component | train | validation | `augmentation_type` | `source_dataset` |
|---|---:|---:|---|---|
| ko refine | 21,038 | 5,230 | `none` | `openpii-1.5m-ko` |
| ko perturbation | 13,038 | 3,230 | `perturbation` | `openpii-1.5m-ko` |
| ko synthesis | 8,887 | 2,283 | `synthesis` | `domain` |
| en replay | 12,623 | 3,138 | `none` | `openpii-1.5m-en` |
| en synthesis | 2,265 | 643 | `synthesis` | `domain` |
| **total** | **57,851** | **14,524** | - | - |

`source_dataset` records the source bucket, while `augmentation_type` records the transformation path. For example, a perturbed Korean row remains in `openpii-1.5m-ko` because its sentence originated upstream, even though its selected values were generated locally.

Across both splits, the source buckets contain 42,536 `openpii-1.5m-ko` rows, 15,761 `openpii-1.5m-en` rows, and 14,078 `domain` rows - locally authored synthesis rows covering financial, customer-service/VOC, security, identity, and infrastructure scenarios.

## 2.3. Label Taxonomy
The 29 labels produce 117 BIOES classes: `B-`, `I-`, `E-`, and `S-` for every label, plus `O`.

| label | definition |
|---|---|
| `PERSON` | Full personal name as one span. |
| `RRN` | Korean resident registration number. |
| `FRN` | Korean foreign resident registration number. |
| `SSN` | Social-security-number family inherited from ai4privacy `SOCIALNUM`; not limited to the US 9-digit form. |
| `GENERIC_ID` | Identity-card or tax identifier that cannot be assigned to a more specific country-level label. |
| `CARD_NUMBER` | Credit or debit card PAN. |
| `ACCOUNT_NUMBER` | Bank account number. |
| `SECRET` | Password, API key, access token, or similar authentication secret. |
| `USER_ID` | Online account or member identifier. |
| `EMAIL` | Email address, including intentionally obfuscated forms in targeted synthesis rows. |
| `PHONE` | Mobile or landline telephone number, including intentionally verbalized forms in targeted synthesis rows. |
| `PASSPORT` | Passport number. |
| `DRIVER_LICENSE` | Driver's license number. |
| `ADDRESS` | City, street, and building components merged into one address span. |
| `ZIPCODE` | Postal code kept separate from `ADDRESS`. |
| `DATE` | Date or time; timezone-only strings remain `O`. |
| `CARD_EXPIRY` | Payment-card expiration date. |
| `CVC` | Card verification code, generated only with a card context. |
| `IPIN` | Korean I-PIN identifier. |
| `TRANSACTION_APPROVAL_ID` | 8-digit payment authorization or transaction approval identifier. |
| `BUSINESS_ID` | 10-digit business registration number or 9-digit merchant identifier. |
| `VIRTUAL_CARD_NUMBER` | 11-digit alternate or virtual card number. |
| `CI` | Korean identity-linkage information value. |
| `IPADDRESS` | IPv4 network address. |
| `MACADDRESS` | 48-bit MAC address. |
| `IMEI` | 15-digit mobile-equipment identifier. |
| `PORT` | Network service port in the range 0 to 65535; a non-PII disambiguation label. |
| `ORGANIZATION` | Company, bank, hospital, or other organization name; a non-PII disambiguation label. |
| `URL` | Full web URL, including path, query, and fragment when present. |

The taxonomy defines annotation labels. `O` means that no entity span is annotated at that position; it does not by itself mean that the text is non-sensitive or safe to retain. Applications can handle detected labels according to their own requirements.

### 2.3.1. Label Distribution
<div align="center">
    <img src="figures/label_distribution.png" alt="Train and validation annotation counts for all 29 labels" />
</div>

| label | train | validation | total |
|---|---:|---:|---:|
| `PERSON` | 45,718 | 11,417 | 57,135 |
| `DATE` | 44,319 | 10,922 | 55,241 |
| `ADDRESS` | 38,152 | 9,556 | 47,708 |
| `EMAIL` | 25,374 | 6,372 | 31,746 |
| `PHONE` | 20,625 | 5,122 | 25,747 |
| `CARD_NUMBER` | 14,839 | 3,672 | 18,511 |
| `ZIPCODE` | 14,475 | 3,676 | 18,151 |
| `GENERIC_ID` | 14,335 | 3,512 | 17,847 |
| `DRIVER_LICENSE` | 9,914 | 2,405 | 12,319 |
| `SSN` | 9,371 | 2,412 | 11,783 |
| `PASSPORT` | 8,019 | 2,015 | 10,034 |
| `RRN` | 7,168 | 1,797 | 8,965 |
| `ORGANIZATION` | 2,113 | 588 | 2,701 |
| `IPADDRESS` | 1,103 | 305 | 1,408 |
| `TRANSACTION_APPROVAL_ID` | 1,066 | 308 | 1,374 |
| `USER_ID` | 1,060 | 309 | 1,369 |
| `BUSINESS_ID` | 992 | 268 | 1,260 |
| `ACCOUNT_NUMBER` | 966 | 277 | 1,243 |
| `PORT` | 958 | 217 | 1,175 |
| `URL` | 805 | 215 | 1,020 |
| `MACADDRESS` | 783 | 203 | 986 |
| `CI` | 761 | 225 | 986 |
| `SECRET` | 655 | 214 | 869 |
| `IPIN` | 645 | 201 | 846 |
| `FRN` | 600 | 158 | 758 |
| `IMEI` | 544 | 135 | 679 |
| `CARD_EXPIRY` | 522 | 138 | 660 |
| `VIRTUAL_CARD_NUMBER` | 508 | 136 | 644 |
| `CVC` | 456 | 120 | 576 |
| **total** | **266,846** | **66,895** | **333,741** |

The distribution is intentionally not uniform. Common free-form labels require more examples, while format-constrained labels use smaller targeted sets. Per-label strict Precision, Recall, and F1 must still be measured after training, particularly for the least frequent labels.

## 2.4. Synthesis and Hard Examples
Synthesis uses statically authored templates and local value generators. Each static template contributes one synthesis row to one split, and templates are not reused for value-only variants.

The initial 12,500 authored train and validation templates used the following design targets.

| axis | target distribution |
|---|---|
| purpose | 70% positive, 20% confusion, 10% pure hard negative |
| cue level | 20% explicit, 35% contextual local, 30% contextual distant, 15% adversarial |
| unique labels per row | 0 to 7 labels, with 2-label and 3-label rows forming the largest groups |
| repeated labels | 15% of labeled rows repeat at least one label |
| long documents | 20% of synthesis rows, with 3 to 6 unique labels |

The published synthesis subset contains 14,078 rows: 12,500 initial authored rows, 1,528 contextualized legacy-template rows, and 50 independently authored email-disclosure rows. Its cue-level distribution is shown below.

| final cue level | rows | share |
|---|---:|---:|
| `explicit` | 2,500 | 17.76% |
| `contextual_local` | 5,903 | 41.93% |
| `contextual_distant` | 3,778 | 26.84% |
| `adversarial` | 1,897 | 13.47% |
| **total** | **14,078** | **100.00%** |

Each cue level describes what evidence identifies a span as an entity.

* `explicit` - a direct field-name cue accompanies the value, as in application forms, tables, and logs. This is the only group where such direct hints are allowed.
* `contextual_local` - the action, role, or relationship in the same clause identifies the value, without a direct field-name hint.
* `contextual_distant` - later sentences or the document-wide event flow identify the value. Long synthesis documents are placed in this group.
* `adversarial` - confusable values, `O` decoys, and other labels appear in the same context, and direct hints for the target label are forbidden. Pure hard-negative rows belong to this group.

Hard examples include:

* `DATE` versus `CARD_EXPIRY`.
* `CARD_NUMBER` or `PHONE` versus `VIRTUAL_CARD_NUMBER`.
* `DRIVER_LICENSE` versus `TRANSACTION_APPROVAL_ID`.
* `GENERIC_ID` versus `BUSINESS_ID`.
* `SECRET` versus `CI`.
* `IPADDRESS` versus `URL`.
* `MACADDRESS` versus `IMEI`.
* `PORT` versus `ZIPCODE` or an unlabeled operational number.
* `PERSON` or `ADDRESS` versus `ORGANIZATION`.
* Order numbers, product codes, industry codes, amounts, status phrases, and application settings as `O` decoys.

## 2.5. Long-Context Coverage
The financial, customer-service/VOC, and CI targeted subset intentionally places target spans at the front, middle, and end of long documents.

| split | supplement rows | long rows | long share | front | middle | end | last-96-token rows |
|---|---:|---:|---:|---:|---:|---:|---:|
| train | 241 | 154 | 63.90% | 37.35% | 16.27% | 46.39% | 58 |
| validation | 60 | 39 | 65.00% | 35.00% | 12.50% | 52.50% | 17 |

These figures describe the targeted subset, not the entire dataset. They establish data coverage only; they do not establish long-context model accuracy.

## 2.6. Schema
All rows have ten columns. `privacy_mask` uses half-open character offsets over `source_text`: `source_text[start:end] == value`.

| column | type | description |
|---|---|---|
| `source_text` | string | Unmasked model input. |
| `masked_text` | string | Annotation view with every labeled span replaced by a `[LABEL_n]` placeholder. Numbering follows left-to-right span order and restarts at 1 for each label in each row. |
| `privacy_mask` | `list<struct>` | Span records containing `label`, `start`, `end`, and `value`. |
| `language` | string | `ko` or `en`. |
| `split` | string | `train` or `validation`. |
| `uid` | string | Unique row identifier. |
| `source_dataset` | string | `openpii-1.5m-ko`, `openpii-1.5m-en`, or `domain`. |
| `augmentation_type` | string | `none`, `perturbation`, or `synthesis`. |
| `tokens` | `list<string>` | o200k subword token strings for `source_text`. |
| `token_classes` | `list<string>` | BIOES label aligned one to one with `tokens`. |

`masked_text` is a rendering of the span annotations, not application output. Consumers can retain `PORT` or `ORGANIZATION`, partially mask selected labels, or apply channel-specific handling after inference.

<br>

# 3. Synthetic-Data Safety
The dataset is designed as synthetic training data, not as pseudonymized operational data. Its safety argument relies on provenance, independent generation, lack of linkage to a real source record, and additional structural controls where public validation rules exist.

## 3.1. Row Transformation Paths and Value Provenance
The following counts describe row transformation paths. They do not claim that every value in a row has the same provenance.

| row path group | rows | share | interpretation |
|---|---:|---:|---|
| Rows retaining an upstream sentence structure without perturbation - ko refine and en replay | 42,029 | 58.07% | Values primarily originate in ai4privacy, although refine locally transforms qualifying RRN and card values. |
| Rows with local replacement or full synthesis - ko perturbation and ko/en synthesis | 30,346 | 41.93% | Synthesis is fully local. Perturbation replaces selected target spans but can retain other upstream values. |
| **total** | **72,375** | **100.00%** | - |

Value provenance must therefore be interpreted per span rather than by assigning one provenance to the whole row. The row path groups are also not identical to `source_dataset`. Perturbed Korean rows retain `source_dataset=openpii-1.5m-ko` because their sentence scaffold originated upstream, even though selected values were generated locally.

Public organization aliases and public geographic vocabulary can appear as non-personal reference material. They are not linked to an actual individual's record.

## 3.2. Structural Controls and Audits
The following controls are applied where a public algorithm or a reserved range makes a meaningful check possible.

| value family | control |
|---|---|
| `RRN` and locally generated `FRN` | Generate a valid structural body, then alter the check digit so the public checksum fails. |
| `CARD_NUMBER` | Alter the Luhn check digit for plausible PAN lengths covered by the final audit. |
| `EMAIL` | Use reserved `example.com`, `example.net`, and `example.org` domains on locally generated paths. |
| North American `PHONE` | Use the reserved `555-01XX` range on locally generated paths. |
| `IPADDRESS` | Use documentation-only IPv4 networks on locally generated paths. |
| `MACADDRESS` | Generate locally administered unicast addresses. |
| `IMEI` | Alter the final digit so the generated value fails Luhn validation. |
| `DRIVER_LICENSE` and `PASSPORT` | Use avoidance rules and unassigned formats where defined; these are not permanent mathematical guarantees. |

Current mix audits found:

* 8,965 `RRN` spans and zero checksum-valid values.
* Zero RRN values in the excluded post-2020 birth-band construction.
* 18,511 `CARD_NUMBER` spans and zero Luhn-valid values at lengths of 13 digits or more.
* 17 inherited card-number values shorter than 13 digits that pass Luhn - 14 in train and 3 in validation. These are a known limitation and rely on synthetic provenance.

For identifiers backed by private registries, such as account, telephone, passport, user, and social-security identifiers, actual issuance cannot be exhaustively checked. Their safety basis is synthetic provenance and the absence of linkage to a real person, not a claim that every generated surface form is impossible in the real world.

## 3.3. Split Independence and Integrity
The published artifacts passed the following structural checks.

* No duplicate UID or exact `source_text` across train and validation.
* No exact completed-value overlap between synthesis train and synthesis validation for any of the 29 labels. This compares literal span-value strings within the same label without case, punctuation, or format normalization.
* No span offset or value mismatch across 333,741 annotations.
* No taxonomy violation, split-field mismatch, or token/BIOES length mismatch.
* No row-level mismatch between the JSONL and Parquet build artifacts.
* No row dropped for exceeding 1024 tokens.

<br>

# 4. Limitations
* **No model-performance claim.** This card describes data construction and integrity. Precision, Recall, F1, and boundary accuracy remain to be measured after training.
* **Synthetic distribution shift.** Authored text is cleaner and more explanatory than many production VOC messages, logs, OCR fragments, and email chains. Some long rows contain phrases that explicitly explain why a value should or should not be treated as an identifier.
* **Rare-label imbalance.** `CVC`, `VIRTUAL_CARD_NUMBER`, `CARD_EXPIRY`, `IMEI`, and `FRN` have far fewer spans than `PERSON`, `DATE`, and `ADDRESS`. Format regularity can reduce the required volume, but adequate generalization is not established by count alone.
* **Organization boundary ambiguity.** The v1 taxonomy labels companies, banks, hospitals, and other legal organizations as `ORGANIZATION`, while brands, products, services, and personal trade names can remain `O`. Real text does not always make that distinction explicit.
* **Inherited-value realism.** Upstream ai4privacy values can resemble real identifiers. Except for audited checksum-controlled families, safety rests on synthetic provenance and absence of source linkage.
* **Korean translationese.** The refined Korean source retains sentence structures inherited from English-oriented upstream templates. Perturbation preserves those scaffolds, and the resulting effect on natural Korean generalization has not been measured.
* **Short card-number residual.** The 17 inherited values described in the structural audit section are not covered by the current 13-or-more-digit Luhn invalidation guarantee.
* **I-PIN format maturity.** `IPIN` is a pilot-format subset and may not cover all production variants.
* **Domain coverage.** Financial services, customer service/VOC, identity, security, and infrastructure contexts are emphasized. Performance in unrelated domains is not guaranteed.

<br>

# 5. Reproducibility and Metadata
## 5.1. Release Metadata
This card describes dataset version `v1`. The published token strings were produced with the fast tokenizer associated with the [`openai/privacy-filter`](https://huggingface.co/openai/privacy-filter) model, using `add_special_tokens=False` and `truncation=False`. The sequence-length limit during dataset construction was 1024 tokens before special tokens.

Padding and special-token insertion are not included in the published alignment. Configure them in the training collator and preserve one label for each published token.

## 5.2. Source and License
This dataset is derived from [`ai4privacy/pii-masking-openpii-1.5m`](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m), distributed under CC BY 4.0. This derivative dataset is also released under CC BY 4.0, and attribution to ai4privacy is required.

Token strings and BIOES targets use the o200k tokenizer associated with the [`openai/privacy-filter`](https://huggingface.co/openai/privacy-filter) base model.

## 5.3. Citation
```bibtex
@dataset{bccard_privacy_filter_openpii_masking_v1,
  title  = {Privacy Filter OpenPII Masking: Korean and English Entity Detection Dataset},
  author = {BC Card},
  year   = {2026},
  url    = {https://huggingface.co/datasets/BCCard/privacy-filter-openpii-masking},
  note   = {Version 1; derived from ai4privacy/pii-masking-openpii-1.5m under CC BY 4.0}
}
```

## 5.4. Related Artifacts
* **Base model:** [`openai/privacy-filter`](https://huggingface.co/openai/privacy-filter).
* **Upstream dataset:** [`ai4privacy/pii-masking-openpii-1.5m`](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m).

<br>

# 6. Legal Disclaimer
**No Warranty and Use at Your Own Risk:** This dataset is provided "as is" without warranties of any kind, express or implied. BC Card makes no representations or warranties regarding accuracy, completeness, or suitability for any purpose. Use is at your own risk.

**No Liability:** BC Card and its affiliates shall not be liable for damages arising from the use of, or inability to use, this dataset.

**Compliance and Responsibility:** Users are responsible for ensuring that their use complies with applicable laws, regulations, contractual obligations, and ethical requirements, including relevant data-protection and AI regulations.

**Synthetic Data Statement:** This dataset is designed as synthetic training data and is structurally audited where public checks exist. Values are either generated locally under the documented controls or inherited from the synthetic ai4privacy corpus. Actual issuance cannot be exhaustively checked for identifiers backed by private registries. Any coincidental match with real-world information is unintended and has no source linkage to an operational record. These statements describe design intent and verification results and do not constitute a legal warranty.

<br>
