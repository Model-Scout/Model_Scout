---
configs:
- config_name: all
  data_files:
  - path:
    - all.jsonl.zst
    split: train
  default: true
- config_name: ar
  data_files:
  - path:
    - ar.jsonl.zst
    split: train
- config_name: az
  data_files:
  - path:
    - az.jsonl.zst
    split: train
- config_name: bg
  data_files:
  - path:
    - bg.jsonl.zst
    split: train
- config_name: bn
  data_files:
  - path:
    - bn.jsonl.zst
    split: train
- config_name: ca
  data_files:
  - path:
    - ca.jsonl.zst
    split: train
- config_name: cs
  data_files:
  - path:
    - cs.jsonl.zst
    split: train
- config_name: da
  data_files:
  - path:
    - da.jsonl.zst
    split: train
- config_name: de
  data_files:
  - path:
    - de.jsonl.zst
    split: train
- config_name: el
  data_files:
  - path:
    - el.jsonl.zst
    split: train
- config_name: en
  data_files:
  - path:
    - en.jsonl.zst
    split: train
- config_name: es
  data_files:
  - path:
    - es.jsonl.zst
    split: train
- config_name: et
  data_files:
  - path:
    - et.jsonl.zst
    split: train
- config_name: fa
  data_files:
  - path:
    - fa.jsonl.zst
    split: train
- config_name: fi
  data_files:
  - path:
    - fi.jsonl.zst
    split: train
- config_name: fr
  data_files:
  - path:
    - fr.jsonl.zst
    split: train
- config_name: he
  data_files:
  - path:
    - he.jsonl.zst
    split: train
- config_name: hi
  data_files:
  - path:
    - hi.jsonl.zst
    split: train
- config_name: hu
  data_files:
  - path:
    - hu.jsonl.zst
    split: train
- config_name: hy
  data_files:
  - path:
    - hy.jsonl.zst
    split: train
- config_name: id
  data_files:
  - path:
    - id.jsonl.zst
    split: train
- config_name: is
  data_files:
  - path:
    - is.jsonl.zst
    split: train
- config_name: it
  data_files:
  - path:
    - it.jsonl.zst
    split: train
- config_name: ja
  data_files:
  - path:
    - ja.jsonl.zst
    split: train
- config_name: ka
  data_files:
  - path:
    - ka.jsonl.zst
    split: train
- config_name: kk
  data_files:
  - path:
    - kk.jsonl.zst
    split: train
- config_name: ko
  data_files:
  - path:
    - ko.jsonl.zst
    split: train
- config_name: lt
  data_files:
  - path:
    - lt.jsonl.zst
    split: train
- config_name: lv
  data_files:
  - path:
    - lv.jsonl.zst
    split: train
- config_name: mk
  data_files:
  - path:
    - mk.jsonl.zst
    split: train
- config_name: ml
  data_files:
  - path:
    - ml.jsonl.zst
    split: train
- config_name: mr
  data_files:
  - path:
    - mr.jsonl.zst
    split: train
- config_name: ms
  data_files:
  - path:
    - ms.jsonl.zst
    split: train
- config_name: ne
  data_files:
  - path:
    - ne.jsonl.zst
    split: train
- config_name: nl
  data_files:
  - path:
    - nl.jsonl.zst
    split: train
- config_name: 'no'
  data_files:
  - path:
    - no.jsonl.zst
    split: train
- config_name: pl
  data_files:
  - path:
    - pl.jsonl.zst
    split: train
- config_name: pt
  data_files:
  - path:
    - pt.jsonl.zst
    split: train
- config_name: ro
  data_files:
  - path:
    - ro.jsonl.zst
    split: train
- config_name: ru
  data_files:
  - path:
    - ru.jsonl.zst
    split: train
- config_name: sk
  data_files:
  - path:
    - sk.jsonl.zst
    split: train
- config_name: sl
  data_files:
  - path:
    - sl.jsonl.zst
    split: train
- config_name: sq
  data_files:
  - path:
    - sq.jsonl.zst
    split: train
- config_name: sr
  data_files:
  - path:
    - sr.jsonl.zst
    split: train
- config_name: sv
  data_files:
  - path:
    - sv.jsonl.zst
    split: train
- config_name: ta
  data_files:
  - path:
    - ta.jsonl.zst
    split: train
- config_name: th
  data_files:
  - path:
    - th.jsonl.zst
    split: train
- config_name: tr
  data_files:
  - path:
    - tr.jsonl.zst
    split: train
- config_name: uk
  data_files:
  - path:
    - uk.jsonl.zst
    split: train
- config_name: ur
  data_files:
  - path:
    - ur.jsonl.zst
    split: train
- config_name: vi
  data_files:
  - path:
    - vi.jsonl.zst
    split: train
- config_name: zh
  data_files:
  - path:
    - zh.jsonl.zst
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
- ms
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
license: cc-by-4.0
---
# High Quality Multilingual Sentences

- This dataset contains multilingual sentences derived from the [agentlans/LinguaNova](https://huggingface.co/datasets/agentlans/LinguaNova) dataset.
- It includes 1.58 million rows across 51 different languages, each in its own configuration.

Example row (from the `all` config):
```json
{
    "text": "امام جمعه اصفهان گفت: میزان نیاز آب شرب اصفهان ۱۱.۵ متر مکعب است که تمام استان اصفهان را پوشش میدهد و نسبت به قبل از انقلاب یکی از پیشرفتها در حوزه آب بوده است.",
    "fasttext": "fa",
    "gcld3": "fa"
}
```

Fields:
- **text**: The sentence in the original language.
- **fasttext**, **gcld3**: Language codes determined using fastText and gcld3 Python packages.

## Configurations

Each individual language is available as a separate configuration, such as `ar`, `en`. These configurations contain only sentences identified to be of that specific language by both the fastText and gcld3 models.

Example row (from a language-specific config):
```json
{
    "text": "Ne vienas asmuo yra apsaugotas nuo parazitų atsiradimo organizme."
}
```

## Methods

### Data Loading and Processing

The `all` split was downloaded from the [agentlans/LinguaNova](https://huggingface.co/datasets/agentlans/LinguaNova) dataset.
1. **Text Cleaning**: Raw text was cleaned by removing HTML tags, emails, emojis, hashtags, user handles, and URLs. Unicode characters and whitespace were normalized, and hyphenated words were handled to ensure consistency.
2. **Sentence Segmentation**: Text was segmented into individual sentences using ICU's `BreakIterator` class, which efficiently processed different languages and punctuation.
3. **Deduplication**: Duplicate entries were removed to maintain uniqueness and prevent redundancy in the dataset.

### Language Detection

Two methods were used for language identification:
1. **gcld3**: Google's Compact Language Detector 3 was used for fast and accurate language identification.
2. **fastText**: Facebook’s fastText model was employed, which improved accuracy by considering subword information.

### Quality Assessment

Text quality was assessed through batch inference using the [agentlans/multilingual-e5-small-aligned-quality](https://huggingface.co/agentlans/multilingual-e5-small-aligned-quality) model.
1. **Data Retrieval**: Entries with a quality score of 1 or higher and a minimum input length of 20 characters were retained.
2. **Text Refinement**: Leading punctuation and spaces were removed, and balanced quotation marks were validated using regular expressions.

### Dataset Configs

The filtered sentences and their annotated languages were written to the `all.jsonl` file. The file was then split into language-specific JSONL files, containing only those sentences that matched consistently with both gcld3 and fasttext in terms of language identification. Only languages with at least 100 sentences after filtering were included in these configs.

## Usage

### Loading the Dataset
```python
from datasets import load_dataset

dataset = load_dataset('agentlans/high-quality-multilingual-sentences', 'all')
```

For language-specific configurations:
```python
language_config = load_dataset('agentlans/high-quality-multilingual-sentences', 'en')  # Replace with desired language code.
```

### Example Usage in Python
```python
from datasets import load_dataset

# Load the dataset for all languages or a specific one
dataset_all = load_dataset("agentlans/high-quality-multilingual-sentences", "all")
print(dataset_all["train"][0])

language_config = load_dataset("agentlans/high-quality-multilingual-sentences", "en")  # Replace 'en' with desired language code.
print(language_config["train"][:5])
```

## Limitations

- **Multilingual content bias**: The quality classifier is biased towards educational and more formal content.
- **Language coverage**: Limited to the 50 written languages from LinguaNova. There's a lack of African and indigenous languages.
- **Short input issues**: Language identification accuracy can suffer when working with short inputs like single sentences.
- **Sentence segmentation challenges**: Some languages' delimiters might not be handled correctly.
- **Redundancy**: The filtering was only done on exact matches so some sentences may be similar (but not identical).

Additionally:
- **Thai data imbalance**: Fewer examples are available for `th` (Thai) than expected. Could be a sentence segmentation problem.
- **Malay and Indonesian**: There are few examples for the `ms` (Malay) subset. Consider also using the `id` (Indonesian) subset when training models.
- **Chinese written forms**: This dataset does not distinguish between different Chinese character variations.

## Licence

This dataset is released under a [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) licence, allowing for free use and distribution as long as proper attribution is given to the original source.