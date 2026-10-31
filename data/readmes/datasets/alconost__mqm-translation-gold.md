---
license: cc-by-sa-4.0
task_categories:
  - translation
  - text-classification
language:
  - en
  - it
  - de
  - fr
  - ru
  - uk
  - be
  - pl
  - ko
  - ja
  - pt
  - ar
  - arz
  - ary
  - hmn
tags:
  - mqm
  - translation-quality
  - machine-translation
  - human-evaluation
  - mt-evaluation
  - nlp
pretty_name: MQM Translation Gold
size_categories:
  - 1K<n<10K
---

# Alconost MQM Translation Quality Dataset

A growing collection of professional MQM (Multidimensional Quality Metrics) annotations for machine translation evaluation.

## Dataset Description

This dataset contains human expert annotations of machine translation outputs using the MQM framework - the same methodology used in WMT (Workshop on Machine Translation) human evaluation campaigns.

All annotations are performed by trained linguists with native/near-native proficiency. Data is self-describing via fields like `doc_id`, `system_id`, `src_lang`, and `tgt_lang`.

### At a Glance

| Metric | Value |
|--------|-------|
| **Segments** | 362 |
| **Annotation rows** | 1,347 |
| **MT Systems** | EuroLLM-22B, Qwen3-235B, TranslateGemma-12B |
| **Language pairs** | 16 (en→ar-EG, ar-MA, ar-MSA, ar-SA, be, de, fr, hmn, it_IT, ja, ko, pl, pt-BR, pt-PT, ru, uk) |
| **Annotators** | 48 professional linguists |
| **Domains** | Social media, Academic |

### Key Features

- **Professional Annotations**: All annotations performed by trained linguists with native/near-native proficiency
- **Span-Level Errors**: Character-level error span positions (start/end) in JSONL; `<v>...</v>` markers in TSV
- **Rich Metadata**: Error categories, severities, corrections, and annotator comments
- **Multiple MT Systems**: Comparison across different LLM translation engines
- **Growing Collection**: New language pairs and systems added regularly

## Dataset Structure

```
data/
├── annotations.jsonl   # 362 segments (one JSON object per line)
└── annotations.tsv     # 1,347 annotation rows (one row per error)
```

Both files contain the same data in different formats. Use whichever is more convenient.

### Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `segment_id` | string | Segment identifier (unique within a document) |
| `system_id` | string | MT system that produced the translation |
| `doc_id` | string | Document identifier |
| `context` | string | Additional context (optional) |
| `source` | string | Original source text |
| `target` | string | Machine translation output (TSV: error spans marked as `<v>...</v>`) |
| `src_lang` | string | Source language code |
| `tgt_lang` | string | Target language + locale |
| `category` | string | MQM error category (e.g., `Accuracy/Mistranslation`) |
| `severity` | string | Error severity (`Minor`, `Major`, `Critical`) |
| `annotator_id` | string | Anonymized annotator identifier |
| `correction` | string | Suggested correction (optional) |
| `comment` | string | Annotator's explanation |
| `timestamp` | string | Annotation timestamp (ISO 8601) |

### JSONL Format

Each line is a JSON object representing one segment with an `annotations` array containing all errors found:

```json
{
  "segment_id": "auto_0",
  "system_id": "EuroLLM-22B",
  "doc_id": "en-it_IT_#_social_#_114294867111841563",
  "source": "Original English text...",
  "target": "Italian translation...",
  "src_lang": "en",
  "tgt_lang": "it_IT",
  "annotator_id": "A-5BFF0F0F",
  "annotations": [
    {"start": 91, "end": 105, "category": "Fluency/Grammar", "severity": "Minor", "comment": "..."}
  ]
}
```

### TSV Format

One row per annotation (segments with multiple errors have multiple rows). Error spans are marked inline in the `target` field as `<v>...</v>`.

### MQM Error Categories

The dataset uses the standard MQM typology:

| Category | Subcategories |
|----------|---------------|
| **Accuracy** | Mistranslation, Omission, Addition, Untranslated |
| **Fluency** | Grammar, Spelling, Punctuation, Inconsistency |
| **Terminology** | Incorrect term, Inconsistent terminology |
| **Style** | Register, Awkward phrasing, Unnatural |

### Severity Levels

| Severity | Description | Weight |
|----------|-------------|--------|
| Minor | Small error, meaning preserved | 1 |
| Minor/Punctuation | Punctuation-only error | 0.1 |
| Major | Significant error affecting comprehension | 5 |
| Critical | Severe error, complete meaning loss | 25 |

### MQM Score Formula

```
MQM_score = -Σ(weight × error_count)
```

Lower (more negative) scores indicate worse quality.

## Usage

### Loading with Python

```python
import json
from huggingface_hub import hf_hub_download

file_path = hf_hub_download(
    repo_id="alconost/mqm-translation-gold",
    filename="data/annotations.jsonl",
    repo_type="dataset"
)

with open(file_path) as f:
    for line in f:
        segment = json.loads(line)
        print(f"{segment['system_id']} | {segment['tgt_lang']} | errors: {len(segment.get('annotations', []))}")
```

### Loading with Pandas

```python
import pandas as pd
from huggingface_hub import hf_hub_download

file_path = hf_hub_download(
    repo_id="alconost/mqm-translation-gold",
    filename="data/annotations.tsv",
    repo_type="dataset"
)

df = pd.read_csv(file_path, sep='\t')
print(df.groupby(['system_id', 'tgt_lang'])['severity'].value_counts())
```

### Computing MQM Score

```python
def compute_mqm_score(annotations):
    """Compute MQM score for a segment."""
    weights = {
        'Minor': 1,
        'Minor/Punctuation': 0.1,
        'Major': 5,
        'Critical': 25
    }
    def get_weight(ann):
        if ann['severity'] == 'Minor' and 'Punctuation' in ann.get('category', ''):
            return 0.1
        return weights.get(ann['severity'], 1)

    total_penalty = sum(get_weight(a) for a in annotations)
    return -total_penalty  # More negative = worse quality
```

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{alconost_mqm_2026,
  title = {Alconost MQM Translation Quality Dataset},
  author = {Alconost},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/alconost/mqm-translation-gold}
}
```

## Related Resources

- [MQM Framework](https://themqm.info/) - Official MQM documentation
- [WMT Metrics Shared Task](https://www.statmt.org/wmt24/metrics-task.html) - Annual MT evaluation campaign
- [Alconost MQM Tool](https://alconost.mt/mqm-tool/) - Free MQM annotation tool
- [TranslateGemma Case Study](https://alconost.mt/mqm-tool/case-studies/translategemma/) - Detailed analysis of TranslateGemma-12B quality
- [QACAT](https://alconost.com/en/services/localization-qa-platform) - Localization QA platform: rule-based checks, AI review and human LQA by linguists

## License

This dataset is released under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Contact

- **Website**: [alconost.com](https://alconost.com)
- **Tool**: [alconost.mt/mqm-tool](https://alconost.mt/mqm-tool/)
- **LinkedIn**: [Alex Murauski](https://www.linkedin.com/in/amurauski/)

---

*Dataset created: January 2026*
*Last updated: February 2026*
