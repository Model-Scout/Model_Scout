---
annotations_creators:
- found
language:
- ar
- bg
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
- hr
- hu
- id
- it
- ja
- ko
- lt
- lv
- ms
- nl
- no
- pl
- pt
- ro
- ru
- sk
- sl
- sr
- sv
- th
- tr
- uk
- vi
- zh
language_bcp47:
- pt-BR
- zh-HK
- zh-TW
license:
- cc-by-sa-3.0
multilinguality:
- multilingual
pretty_name: Fandom.com
size_categories:
- 3M<n<10M
source_datasets:
- original
task_categories:
- text-generation
- text-classification
task_ids:
- language-modeling
- topic-classification
configs:
  - config_name: train
    data_files:
      - split: train
        path: '*.parquet'
    default: true
---

# Dataset Card for Fandom.com Community Database Dumps

### Dataset Summary
This dataset contains 7,040,984 current pages from all available [Fandom.com community wiki dumps](https://community.fandom.com/wiki/Help:Database_download) as of February 18, 2025. The dataset was created by processing the "Current pages" database dumps from all available Fandom.com wikis. These dumps contain only the current versions of pages without edit history and includes article text, metadata, and structural information across multiple languages.

### Languages
The dataset is multilingual, covering [40+ languages](https://community.fandom.com/wiki/Help:Language_codes).

## Dataset Structure

### Data Fields
This dataset includes the following fields:
- `id`: Unique identifier for the article (string)
- `title`: Title of the article (string)
- `text`: Main content of the article (string)
- `metadata`: Dictionary containing:
  - `templates`: List of templates used in the article
  - `categories`: List of categories the article belongs to
  - `wikilinks`: List of internal wiki links and their text
  - `external_links`: List of external links
  - `sections`: List of section titles and their levels

### Data Splits
All examples are in a single split.

## Additional Information

### License
This dataset inherits the licenses from the source Fandom communities, which use Creative Commons Attribution-ShareAlike 3.0 (CC-BY-SA 3.0).

To learn more about CC-BY-SA 3.0, visit: https://creativecommons.org/licenses/by-sa/3.0/
