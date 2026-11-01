---
configs:
- config_name: all
  data_files:
  - path:
    - all.txt.zst
    split: train
  default: true
- config_name: ar
  data_files:
  - path:
    - ar.txt.zst
    split: train
- config_name: az
  data_files:
  - path:
    - az.txt.zst
    split: train
- config_name: bg
  data_files:
  - path:
    - bg.txt.zst
    split: train
- config_name: bn
  data_files:
  - path:
    - bn.txt.zst
    split: train
- config_name: ca
  data_files:
  - path:
    - ca.txt.zst
    split: train
- config_name: cs
  data_files:
  - path:
    - cs.txt.zst
    split: train
- config_name: da
  data_files:
  - path:
    - da.txt.zst
    split: train
- config_name: de
  data_files:
  - path:
    - de.txt.zst
    split: train
- config_name: el
  data_files:
  - path:
    - el.txt.zst
    split: train
- config_name: en
  data_files:
  - path:
    - en.txt.zst
    split: train
- config_name: es
  data_files:
  - path:
    - es.txt.zst
    split: train
- config_name: et
  data_files:
  - path:
    - et.txt.zst
    split: train
- config_name: fa
  data_files:
  - path:
    - fa.txt.zst
    split: train
- config_name: fi
  data_files:
  - path:
    - fi.txt.zst
    split: train
- config_name: fr
  data_files:
  - path:
    - fr.txt.zst
    split: train
- config_name: he
  data_files:
  - path:
    - he.txt.zst
    split: train
- config_name: hi
  data_files:
  - path:
    - hi.txt.zst
    split: train
- config_name: hu
  data_files:
  - path:
    - hu.txt.zst
    split: train
- config_name: hy
  data_files:
  - path:
    - hy.txt.zst
    split: train
- config_name: id
  data_files:
  - path:
    - id.txt.zst
    split: train
- config_name: is
  data_files:
  - path:
    - is.txt.zst
    split: train
- config_name: it
  data_files:
  - path:
    - it.txt.zst
    split: train
- config_name: ja
  data_files:
  - path:
    - ja.txt.zst
    split: train
- config_name: ka
  data_files:
  - path:
    - ka.txt.zst
    split: train
- config_name: kk
  data_files:
  - path:
    - kk.txt.zst
    split: train
- config_name: ko
  data_files:
  - path:
    - ko.txt.zst
    split: train
- config_name: lt
  data_files:
  - path:
    - lt.txt.zst
    split: train
- config_name: lv
  data_files:
  - path:
    - lv.txt.zst
    split: train
- config_name: mk
  data_files:
  - path:
    - mk.txt.zst
    split: train
- config_name: ml
  data_files:
  - path:
    - ml.txt.zst
    split: train
- config_name: mr
  data_files:
  - path:
    - mr.txt.zst
    split: train
- config_name: ne
  data_files:
  - path:
    - ne.txt.zst
    split: train
- config_name: nl
  data_files:
  - path:
    - nl.txt.zst
    split: train
- config_name: 'no'
  data_files:
  - path:
    - no.txt.zst
    split: train
- config_name: pl
  data_files:
  - path:
    - pl.txt.zst
    split: train
- config_name: pt
  data_files:
  - path:
    - pt.txt.zst
    split: train
- config_name: ro
  data_files:
  - path:
    - ro.txt.zst
    split: train
- config_name: ru
  data_files:
  - path:
    - ru.txt.zst
    split: train
- config_name: sk
  data_files:
  - path:
    - sk.txt.zst
    split: train
- config_name: sl
  data_files:
  - path:
    - sl.txt.zst
    split: train
- config_name: sq
  data_files:
  - path:
    - sq.txt.zst
    split: train
- config_name: sr
  data_files:
  - path:
    - sr.txt.zst
    split: train
- config_name: sv
  data_files:
  - path:
    - sv.txt.zst
    split: train
- config_name: ta
  data_files:
  - path:
    - ta.txt.zst
    split: train
- config_name: th
  data_files:
  - path:
    - th.txt.zst
    split: train
- config_name: tr
  data_files:
  - path:
    - tr.txt.zst
    split: train
- config_name: uk
  data_files:
  - path:
    - uk.txt.zst
    split: train
- config_name: ur
  data_files:
  - path:
    - ur.txt.zst
    split: train
- config_name: vi
  data_files:
  - path:
    - vi.txt.zst
    split: train
- config_name: zh
  data_files:
  - path:
    - zh.txt.zst
    split: train
language:
- multilingual
- ar
- az
- bg
- bn
- ca
- cs
- da
- de
- el
- en
- es
- et
- fa
- fi
- fr
- he
- hi
- hu
- hy
- id
- is
- it
- ja
- ka
- kk
- ko
- lt
- lv
- mk
- ml
- mr
- ne
- nl
- 'no'
- pl
- pt
- ro
- ru
- sk
- sl
- sq
- sr
- sv
- ta
- th
- tr
- uk
- ur
- vi
- zh
task_categories:
- text-generation
- text-classification
- text-retrieval
size_categories:
- 1M<n<10M
---
# Multilingual Sentences

Dataset contains sentences from 50 languages, grouped by their two-letter ISO 639-1 codes. The "all" configuration includes sentences from all languages.

## Dataset Overview

Multilingual Sentence Dataset is a comprehensive collection of high-quality, linguistically diverse sentences. Dataset is designed to support a wide range of natural language processing tasks, including but not limited to language modeling, machine translation, and cross-lingual studies.

## Methods

Rigorous methodology consisted of three main stages: text preprocessing, language detection, and dataset processing.

### Text Preprocessing

Sophisticated text cleaning pipeline using the textacy library, which included:

- Removal of HTML tags, email addresses, URLs, and emojis
- Unicode and whitespace normalization
- Standardization of punctuation and word formats

### Language Detection

Google CLD3 library utilized for accurate language identification:

- Implemented NNetLanguageIdentifier
- Configured for processing texts between 0-1000 bytes
- Included reliability assessment for each language detection

### Dataset Processing

Workflow for dataset creation involved the following steps:

1. Streamed loading of the LinguaNova multilingual dataset
2. Application of the text preprocessing pipeline
3. Sentence segmentation using PyICU for accurate boundary detection
4. Quality filtering:
   - Length constraint (maximum 2048 characters per sentence)
   - High-reliability language verification
5. Extraction of unique sentences
6. Random shuffling for unbiased sampling
7. Generation of language-specific files

## Technical Details

### Libraries and Tools

- textacy: Advanced text preprocessing
- Google CLD3: State-of-the-art language detection
- Hugging Face datasets: Efficient data handling and processing
- SentenceBreaker: Accurate sentence segmentation

### Implementation Notes

- Process was executed consistently across all 50 languages to ensure uniformity and high quality in the multilingual dataset preparation.
- Special attention was given to maintaining the integrity of each language's unique characteristics throughout the processing pipeline.

## Data Splits

Dataset is organized into the following splits:

- Individual language files: Contains sentences for each of the 50 languages
- "all" configuration: Aggregates sentences from all languages into a single dataset

## Limitations and Biases

While extensive efforts were made to ensure dataset quality, users should be aware of potential limitations:

- Language detection accuracy may vary for very short texts or closely related languages
- Dataset may not fully represent all dialects or regional variations within each language
- Potential biases in the original LinguaNova dataset could be carried over

## Ethical Considerations

Users of this dataset should be mindful of:

- Potential biases in language representation
- Need for responsible use in AI applications, especially in multilingual contexts
- Privacy considerations, although personal identifiable information should have been removed
