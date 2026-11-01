---
license: cc-by-sa-4.0
task_categories:
  - text-classification
  - feature-extraction
language:
  - en
  - fr
  - de
  - es
  - it
  - pt
  - ru
  - la
  - ja
  - zh
  - ko
  - ar
  - hi
  - tr
  - fi
  - hu
  - pl
  - nl
  - sv
  - da
  - el
  - sa
  - multilingual
tags:
  - etymology
  - linguistics
  - knowledge-graph
  - cognates
  - historical-linguistics
  - nlp
  - word-origins
  - language-families
size_categories:
  - 10M<n<100M
---

# Etymograph Unified

A unified etymological knowledge graph built from five publicly available datasets. Contains **22.7 million relations** across **6.6 million words** in **5,529 languages**, covering cognate pairs, derivation chains, borrowing paths, and more.

The goal was to bring together the best open etymology data into a single, queryable SQLite database with a normalized schema — one you can point a graph search at without wrangling five different formats.

## What's in the database

Two core tables:

**`words`** — 6,577,941 entries

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Primary key |
| `term` | TEXT | The word itself |
| `lang` | TEXT | ISO 639-3 language code |
| `lang_name` | TEXT | Full language name (where available) |
| `lang_family` | TEXT | Language family |
| `gloss` | TEXT | Short definition (where available) |

Unique constraint on `(term, lang)`. Full-text search index on `term`.

**`relations`** — 22,758,746 entries

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Primary key |
| `source_word_id` | INTEGER | Foreign key → words |
| `target_word_id` | INTEGER | Foreign key → words |
| `relation_type` | TEXT | One of: `cognate`, `derived_from`, `inherited_from`, `borrowed_from`, `compound_of` |
| `confidence` | REAL | 0–1 confidence score |
| `source_dataset` | TEXT | Which dataset this relation came from |

Indexed on `source_word_id`, `target_word_id`, `relation_type`, and a compound index on `(target_word_id, relation_type)`.

## Relation breakdown

| Type | Count | Description |
|---|---|---|
| `cognate` | 11,620,617 | Words in different languages sharing a common ancestor |
| `derived_from` | 9,825,071 | Word X evolved from word Y (e.g. English *water* from Middle English *water*) |
| `inherited_from` | 654,763 | Direct inheritance within a language family |
| `borrowed_from` | 338,095 | Loanwords across language boundaries |
| `compound_of` | 320,200 | Word formed by combining two or more roots |

## Source datasets

All relation types from the original datasets were normalized into the five types above during the pipeline.

| Dataset | Relations | What it covers | Reference |
|---|---|---|---|
| **CogNet v2.0** | 8,117,981 | Cognate pairs across 338 languages, automatically extracted from wordnets | Batsuren et al., 2019. *CogNet: A Large-Scale Cognate Database.* ACL. |
| **Etymological Wordnet** | 6,031,431 | Etymological relationships extracted from Wiktionary | de Melo, 2014. *Etymological Wordnet: Tracing the History of Words.* LREC. |
| **Etymology Atlas** | 4,167,968 | Wiktionary-derived etymology with typed relations (borrowed, inherited, etc.) | Wikimedia / community contributors |
| **etymology-db** | 3,797,383 | Structured Wiktionary etymology parses with granular relation types | Roher, 2020. github.com/droher/etymology-db |
| **EtymDB 2.1** | 643,983 | Curated etymological links with inheritance, borrowing, and derivation | Fourrier & Sagot, 2020. *Methodological Choices in EtymDB 2.1.* LT4HALA Workshop. |

## How it was built

A Python pipeline downloads the raw data from each source, parses each format (TSV, CSV, Parquet, JSON), normalizes language codes to ISO 639-3, normalizes relation types to the five canonical types, deduplicates words by `(term, lang)`, and bulk-loads everything into SQLite with appropriate indices.

Language codes from ISO 639-1 (two-letter) are mapped to 639-3 (three-letter) where applicable. Non-standard codes from individual datasets are mapped as well.

## Usage

```python
import sqlite3

db = sqlite3.connect("etymograph.db")
db.row_factory = sqlite3.Row

# Find all words matching "water"
words = db.execute("SELECT * FROM words WHERE term = 'water'").fetchall()

# Get the derivation chain for English "water"
word_id = db.execute("SELECT id FROM words WHERE term = 'water' AND lang = 'eng'").fetchone()["id"]
chain = db.execute("""
    SELECT w1.term as src, w1.lang as src_lang, w2.term as tgt, w2.lang as tgt_lang, r.relation_type
    FROM relations r
    JOIN words w1 ON w1.id = r.source_word_id
    JOIN words w2 ON w2.id = r.target_word_id
    WHERE r.source_word_id = ? AND r.relation_type = 'derived_from'
""", (word_id,)).fetchall()

# Find cognates of a word across languages
cognates = db.execute("""
    SELECT w2.term, w2.lang
    FROM relations r
    JOIN words w2 ON w2.id = r.target_word_id
    WHERE r.source_word_id = ? AND r.relation_type = 'cognate'
""", (word_id,)).fetchall()
```

## File

- `etymograph.db` — SQLite database, ~3.5 GB

## Intended use

Research in historical linguistics, computational etymology, NLP tasks involving word origins, language family analysis, building etymology explorers, or anyone who finds word histories interesting.

## Limitations

- Coverage is uneven across languages. European languages (especially English, Latin, French, German) are heavily represented. Many languages have sparse or no data.
- Confidence scores vary by source. CogNet relations are automatically extracted and may contain noise. Wiktionary-derived datasets inherit the quality (and occasional errors) of community edits.
- Some datasets overlap — the same relation may appear from multiple sources. No cross-dataset deduplication is performed at the relation level (though words are deduplicated by term+lang).
- Historical and reconstructed languages use varying conventions for transcription.

## License

The unified database is released under **CC BY-SA 4.0**, consistent with the most restrictive license among the source datasets (Wiktionary-derived data is CC BY-SA).

Individual source datasets have their own licenses:
- CogNet: MIT
- Etymological Wordnet: CC BY-SA 3.0
- Etymology Atlas: CC BY-SA (Wiktionary)
- etymology-db: MIT
- EtymDB 2.1: CC BY-NC-SA 4.0

## Citation

If you use this dataset, please cite the underlying sources:

```bibtex
@inproceedings{batsuren2019cognet,
  title={CogNet: A Large-Scale Cognate Database},
  author={Batsuren, Khuyagbaatar and Bella, G{\'a}bor and Giunchiglia, Fausto},
  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  year={2019}
}

@inproceedings{demelo2014etymwn,
  title={Etymological Wordnet: Tracing the History of Words},
  author={de Melo, Gerard},
  booktitle={Proceedings of the 9th Language Resources and Evaluation Conference (LREC)},
  year={2014}
}

@inproceedings{fourrier2020etymdb,
  title={Methodological Choices in the Construction of EtymDB 2.1},
  author={Fourrier, Cl{\'e}mentine and Sagot, Beno{\^i}t},
  booktitle={LT4HALA Workshop at LREC},
  year={2020}
}
```
