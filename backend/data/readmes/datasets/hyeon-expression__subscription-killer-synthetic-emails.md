---
language:
- en
- ko
license: mit
tags:
- email
- synthetic-data
- natural-language-processing
annotations_creators:
- machine-generated
language_creators:
- machine-generated
pretty_name: Synthetic Emails on Subscription Transaction and General Advertisement
size_categories:
- n<1K
task_categories:
- text-classification
---

# Datasets Submodule

Shared evaluation datasets and schema definitions for the subscription-killer MLOps pipeline.

## Structure

```
datasets/
├── src/
│   └── datasets_shared/         # Root package (avoids naming conflicts)
│       ├── __init__.py
│       ├── py.typed             # Enables PEP 561 (Type checking for consumers)
│       └── schema/              # Pydantic schema definitions
│           ├── __init__.py      # Exports main models
│           ├── base.py          # Shared Mixins/Base models
│           ├── constants.py     # Enums (e.g., SubscriptionEventType)
│           └── models.py        # Specific models (Sample, Dataset)
├── data/                        # Separates data from code
│   ├── versions/                # YYYY-MM-DD_run_id/
│   ├── archive/
│   └── latest -> ./versions/2026-02-25_run_001/  # Relative symlink
├── scripts/                     # Submodule-specific maintenance scripts
│   ├── validate_data.py         # Script to check JSONL against Pydantic
│   └── sync_latest.py           # Updates symlink
├── pyproject.toml               # Makes the submodule installable via pip
├── README.md
└── .gitignore
```

## Installation

### As Editable Package (Recommended)
```bash
# From the submodule root
pip install -e .
```

### As Regular Package
```bash
pip install .
```

## Schema Usage

The schema definitions are available as a Python package:

```python
# Import in consuming projects
from datasets_shared.schema import Sample, Dataset, SubscriptionEventType

# Create samples
sample = Sample(
    message=RawGmailMessage(...),
    subscription_event_type=SubscriptionEventType.MONTHLY_PAYMENT
)
```

## Testing

### Unit Tests
```bash
# Run all tests with pytest
pytest tests/ -v

# Run specific test file
pytest tests/test_validation.py -v
pytest tests/test_converter.py -v

# Run with coverage
pytest tests/ --cov=src/datasets_shared
```

### Manual Test Scripts
For standalone testing without pytest:
```bash
# Test dataset validation
python tests/test_validation.py

# Test Sample to RawGmailMessage conversion
python tests/test_converter.py
```

### Test Structure
```
tests/
├── __init__.py
├── test_validation.py    # Dataset structure and validation tests
└── test_converter.py     # Sample to RawGmailMessage conversion tests
```

## Scripts

### Validate Data
```bash
# Validate single file
python scripts/validate_data.py data/versions/2026-02-25_run_001/task_a.jsonl

# Validate entire directory
python scripts/validate_data.py data/versions/
```

### Update Latest Symlink
```bash
python scripts/sync_latest.py
```

## Testing Schema

Since this submodule is primarily data storage, schema tests remain in the main MLOps project:

- **Location**: `tests/unit/test_dataset_schema.py` in the main project
- **Reasoning**: Schema is part of the validation pipeline, not just data storage
- **Benefits**: Tests have access to full test infrastructure and mocking

## Versioning Convention

- **Format**: `YYYY-MM-DD_<dag_run_id>`
- **Retention**: `max_versions` configured in `config/benchmark.yaml`
- **Pointer**: `data/latest/` always points to most recent successful version

## Integration

1. **Add as submodule**: `git submodule add <datasets_repo_url> datasets`
2. **Initialize**: `make submodule-init`
3. **Install package**: `pip install -e datasets/`
4. **Import schema**: `from datasets_shared.schema import *`
5. **Use datasets**: Reference files via `datasets/data/versions/...` or `datasets/data/latest/`
