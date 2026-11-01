---
pretty_name: "REDACT: A Systematically Controlled Multilingual Benchmark for Personal Information Detection"
language:
- ar
- cs
- da
- de
- en
- es
- fi
- fr
- he
- hi
- hu
- it
- ja
- ko
- nl
- "no"
- pt
- ru
- sv
- th
- tr
- zh
license: other
license_name: redact-dataset-terms
license_link: "https://github.com/guneeshvats/REDACT-PII-Benchmark/blob/main/DATASET_TERMS.md"
task_categories:
- token-classification
size_categories:
- 10K<n<100K
annotations_creators:
- machine-generated
language_creators:
- machine-generated
multilinguality:
- multilingual
tags:
- pii
- privacy
- ner
- benchmark
- multilingual
- synthetic
- datasets
- arxiv:2606.19881
gated: true
extra_gated_heading: "REDACT Dataset Terms"
extra_gated_description: "Access is provided for research, evaluation, auditing, education, and defensive privacy work. Please review and agree to the REDACT Dataset Terms before using the files."
extra_gated_fields:
  I agree to the REDACT Dataset Terms: checkbox
---

# REDACT

**REDACT: A Systematically Controlled Multilingual Benchmark for Personal Information Detection**

**Accepted to the EMNLP 2026 Industry Track**

[Paper / arXiv](https://arxiv.org/abs/2606.19881) · [GitHub](https://github.com/guneeshvats/REDACT-PII-Benchmark)

REDACT is a multilingual benchmark for evaluating personal information detection under systematically controlled generation conditions.

**13,427 records · 324,078 entity annotations · 51 canonical entity types · 25 languages · 9 scripts · 4,127 surface-form patterns**

## Benchmark task

The headline task is **character-span detection plus classification into one of 51 canonical entity types**.

Each entity also includes gold metadata for analysis:

- `disclosed`
- `disclosure_form`
- `sensitivity_tier`

The metadata fields are not additional prediction targets in the headline experiment.

REDACT uses two stratified recall analyses:

- **F5:** recall by `disclosure_form`
- **F6:** recall by `sensitivity_tier`

Precision and F1 are reported for aggregate, per-type, and per-language analyses. F5/F6 use recall because false positives do not have a gold disclosure form or sensitivity tier.

## Files

| File | Records | Use |
|---|---:|---|
| `pii_benchmark_full.json` | 13,427 | Full released benchmark corpus |
| `pii_benchmark_sample1000.json` | 1,000 | Locked detector evaluation split, 40 records per language |

The remaining 12,427 records are also released as part of the benchmark corpus.

## Corpus statistics

| Statistic | Value |
|---|---:|
| Records | 13,427 |
| Entity annotations | 324,078 |
| Mean entities per record | 24.1 |
| Canonical entity types | 51 |
| Languages | 25 |
| Scripts | 9 |
| Surface-form patterns | 4,127 |
| Records per language | 453-621 |
| Pairwise axis-value coverage | 98.2% |
| Mean pairwise ROUGE-L | 0.03 |
| Final offset alignment | 99.657% |

## Construction

A strength-2 covering-array sampler controls nine axes:

1. domain
2. format
3. difficulty
4. length
5. density
6. code-switching
7. language
8. adjacency
9. co-occurrence pattern

Each planned run contains 5,510 covering-array configurations plus 890 paired-sweep configurations, for 6,400 configurations per run. Three planned runs correspond to 19,200 generation slots.

The final release lineage is:

```text
19,200 planned generation slots
        -> 14,285 loaded
        -> 13,471 after structural filtering
        -> 13,427 after near-duplicate filtering
```

## Record format

A record contains generated text, its resolved generation axes, and entity annotations.

Example shape:

```json
{
  "record_id": 42,
  "text": "Patient record ...",
  "axes": {
    "domain": "healthcare",
    "format": "plain_text",
    "difficulty": "medium",
    "length": "large",
    "density": "high",
    "code_switching": "light",
    "language": "ES",
    "adjacency": "tight",
    "co_occurrence_pattern": "CO-007"
  },
  "entities": [
    {
      "entity_type": "Full_Name",
      "entity_string": "María García",
      "start": 19,
      "end": 31,
      "mention_index": 0,
      "disclosed": true,
      "disclosure_form": "complete",
      "sensitivity_tier": "MEDIUM"
    }
  ]
}
```

The detailed schema and canonical label list are maintained in the [GitHub schema documentation](https://github.com/guneeshvats/REDACT-PII-Benchmark/blob/main/data/schema.md).

## Detector results

All five systems were evaluated on the same locked 1,000-record language-stratified split.

| Detector | Partial micro-F1 | Macro F1 | Exact micro-F1 |
|---|---:|---:|---:|
| Presidio | 0.195 | 0.063 | 0.145 |
| GLiNER-multi | 0.320 | 0.224 | 0.293 |
| OpenAI Privacy Filter | 0.512 | 0.254 | 0.171 |
| GPT-4.1 | 0.597 | 0.565 | 0.558 |
| Claude Sonnet 4.6 | **0.636** | **0.619** | **0.602** |

### F5/F6 support

The locked split contains 24,199 gold entities:

| Sensitivity tier | Complete | Partial | Obfuscated | Total |
|---|---:|---:|---:|---:|
| HIGH | 3,833 | 247 | 5 | 4,085 |
| MEDIUM | 14,909 | 110 | 7 | 15,026 |
| LOW | 5,078 | 7 | 3 | 5,088 |
| **Total** | **23,820** | **364** | **15** | **24,199** |

The obfuscated slice contains only 15 gold entities, so its recall values should be interpreted descriptively.

## Manual validation and quality checks

Manual validation used 510 entities, 10 per canonical type, with two annotators, plus a separate 25-record audit covering 521 entities.

- entity-type agreement with gold: 99.1%
- span agreement with gold: 99.1%
- disclosed-flag agreement with gold: 99.7%
- disclosure-form agreement with gold: 99.8%
- inter-annotator raw agreement: 96.4%
- sensitivity-tier agreement: 90.5%, Cohen's kappa = 0.25
- missed-entity rate in the record-level audit: below 3.3%

A three-family reference-free quality panel used GPT-5.2, Claude Sonnet 4.6, and Gemini 2.5 Pro.

## Sensitivity-tier note

`HIGH`, `MEDIUM`, and `LOW` are operational benchmark labels used to create controlled evaluation slices. They should not be interpreted as universal re-identification-risk rankings, model confidence, or legal advice. The tier stored on each released entity is the gold value used by F6.

## Languages

The benchmark contains 25 language variants:

AR, CS, DA, DE, EN, ES, FI, FR, FR_CA, HE, HI, HU, IT, JA, KO, NL, NO, PT_BR, PT_EU, RU, SV, TH, TR, ZH_CN, ZH_TW.

## Loading the data

This dataset is gated. First request access on this page and accept the REDACT Dataset Terms, then authenticate locally:

```bash
hf auth login
```

Download a file:

```python
from huggingface_hub import hf_hub_download
import json

path = hf_hub_download(
    repo_id="guneeshv/REDACT-PII-Benchmark",
    filename="pii_benchmark_full.json",
    repo_type="dataset",
)

with open(path, encoding="utf-8") as f:
    records = json.load(f)

print(len(records))
```

If your repository layout uses a subdirectory for the JSON files, replace `filename` with the exact path shown under **Files and versions**.

## Intended use

Appropriate uses include:

- PII detector benchmarking
- multilingual NER / span-detection evaluation
- privacy and compliance auditing
- robustness analysis by disclosure form and sensitivity tier
- defensive privacy research
- education and reproducibility studies

The dataset is synthetic and is not intended to contain real personal data.

## Limitations

Important limitations include:

- synthetic-to-real validity is not established for the full 51-type, 25-language benchmark
- all five headline detectors were evaluated on the locked 1,000-record subset rather than every released record
- the rarest entity types have wider uncertainty
- the obfuscated disclosure-form slice in the detector split contains only 15 gold entities
- sensitivity-tier annotation is the hardest validated metadata dimension
- LLMs participate in generation, quality assessment, and two detector baselines, creating some shared model-family dependence
- locale-aware multi-component name decomposition remains a residual challenge

See the paper for the full limitations discussion.

## License and access terms

The dataset and pattern catalog are distributed under the [REDACT Dataset Terms](https://github.com/guneeshvats/REDACT-PII-Benchmark/blob/main/DATASET_TERMS.md).

The GitHub source code is separately available under the MIT License.

The dataset is intended for research, evaluation, auditing, education, and defensive privacy work. Uses involving impersonation, credential abuse, detector evasion, or re-identification of real people are prohibited by the dataset terms.

## Citation

```bibtex
@inproceedings{vats2026redact,
  title     = {REDACT: A Systematically Controlled Multilingual Benchmark for Personal Information Detection},
  author    = {Guneesh Vats and Anubha Agrawal and Shikha Singhal and Ajita Dash and Praison Selvaraj and Vidhan Jhawar and Ranga Prasad Chenna and Bharadwaj Y M G},
  booktitle = {Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing: Industry Track},
  year      = {2026},
  note      = {To appear}
}
```

Preprint: https://arxiv.org/abs/2606.19881
