---
annotations_creators:
- found
language:
- en
- de
- fr
- es
- it
- ru
- ja
- zh
- pt
- nl
- pl
- ar
- tr
- sv
- cs
- fi
- ko
- uk
- hu
- da
- el
- no
- ro
- sk
- vi
- bg
- et
- lt
- lv
- sl
- sr
- hr
- ca
- id
- ms
- th
- he
- fa
- hi
language_bcp47:
- en-US
- en-GB
- zh-CN
- zh-TW
- pt-BR
license:
- cc-by-sa-4.0
multilinguality:
- multilingual
pretty_name: Public MediaWiki Collection
size_categories:
- 1M<n<2M
source_datasets:
- original
task_categories:
- text-generation
- text-classification
task_ids:
- language-modeling
- topic-classification
---

# Dataset Card for Public MediaWiki Collection

### Dataset Summary
This dataset contains 1,662,448 articles harvested from 930 random public MediaWiki instances found across the Internet. The collection was created by extracting current page content from these wikis, preserving article text, metadata, and structural information. The dataset represents a diverse cross-section of public wiki content spanning multiple domains, topics, and languages.

### Languages
The dataset is multilingual, covering 35+ languages found across the collected wiki instances.

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
This dataset is released under the Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA 4.0) license, consistent with the licensing of the source MediaWiki instances.

To learn more about CC-BY-SA 4.0, visit: https://creativecommons.org/licenses/by-sa/4.0/
