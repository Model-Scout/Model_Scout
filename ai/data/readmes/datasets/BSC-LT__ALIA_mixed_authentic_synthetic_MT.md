---
language:
- en
- es
- ar
- hi
- zh
- ja
- ko
multilinguality:
- multilingual
pretty_name: ALIA Mixed Authentic and Synthetic Multilingual Parallel Dataset
size_categories:
- 100M<n<1B
task_categories:
- translation
license: cc-by-4.0
---
# Dataset Card for ALIA_mixed_authentic_synthetic_MT

## Dataset Description

- **Point of Contact:** langtech@bsc.es


### Dataset Summary

Large-scale multilingual parallel corpus covering English and Spanish paired with Arabic, Hindi, Chinese, Japanese, and Korean. Built by aggregating and carefully filtering multiple public sources, it provides sentence-level alignments for training Machine Translation systems. The Spanish–Hindi and Spanish–Chinese portions of the dataset include synthetic Spanish translations generated from English using [SalamandraTA 7B Instruct](https://huggingface.co/BSC-LT/salamandra-7b-instruct).

### Supported Tasks and Leaderboards

The dataset is primarily designed for Machine Translation between English/Spanish and multiple target languages (Arabic, Hindi, Chinese, Japanese, and Korean). Typical uses include supervised MT training, fine-tuning multilingual models, and data augmentation.

### Languages

The dataset includes parallel sentences across the following language pairs:

| Language pair     | Codes | Size (sentences)
|-------------------|-------|------------------
| English-Arabic    | en-ar |                 72,842,230
| English-Hindi     | en-hi |                 27,256,919
| English-Chinese   | en-zh |                 65,047,374
| English-Japanese  | en-ja |                 29,017,543
| English-Korean    | en-ko |                 29,407,174
| Spanish-Arabic    | es-ar |                 48,830,472
| Spanish-Hindi     | es-hi |                 33,703,968
| Spanish-Chinese   | es-zh |                 78,828,366
| Spanish-Japanese  | es-ja |                 32,129,479
| Spanish-Korean    | es-ko |                 36,719,824
| **Total**         |        |         **453,783,349**

## Dataset Structure

### Data Instances

The dataset is provided in parquet format with separate files for each language pair (e.g., `en-ar.part000.parquet`, `es-hi.part000.parquet`). Each row contains a parallel sentence pair with the following structure:

```json
{
  "l1_sentence": "Example sentence in first language",
  "l2_sentence": "Example sentence in second language",
  "l1": "en",
  "l2": "es"
}
```

### Data Fields

- `l1_sentence`: The sentence in the first language (string)
- `l2_sentence`: The parallel sentence in the second language (string)
- `l1`: ISO 639-1 code of the first language (string)
- `l2`: ISO 639-1 code of the second language (string)

### Data Splits

The dataset contains a single split: `train`.

## Dataset Creation

### Curation Rationale

This dataset is aimed at promoting the development of Machine Translation between English/Spanish and multiple target languages (Arabic, Hindi, Chinese, Japanese, and Korean), supporting research in multilingual NLP and facilitating the development of translation systems for diverse language pairs.

### Source Data

#### Initial Data Collection and Normalization

The corpus is a combination of the following original datasets collected primarily from [OPUS](https://opus.nlpl.eu/) and other public sources:

- **Tatoeba**: Community-contributed parallel sentences
- **UNPC**: United Nations Parallel Corpus
- **NLLB**: No Language Left Behind corpus
- **MultiUN**: Multilingual United Nations parallel corpus
- **WikiMatrix**: Parallel sentences extracted from Wikipedia
- **News-Commentary**: Parallel news commentary corpus
- **CCAligned**: Web-crawled parallel sentences
- **MultiCCAligned**: Multilingual version of CCAligned
- **HPLT**: High Performance Language Technologies parallel data
- **MultiHPLT**: Multilingual HPLT corpus
- **OpenSubtitles**: Parallel subtitles from movies and TV shows
- **ParaCrawl**: Web-crawled parallel corpus
- **Anuvad**: Indian language parallel corpus
- **GlobalVoices**: Multilingual news corpus
- **KDE4**: KDE4 localization files
- **EUbookshop**: European Union bookshop publications
- **Ubuntu**: Ubuntu localization files
- **XLEnt**: Cross-lingual entity corpus
- **Bible-UEdin**: Bible translations from University of Edinburgh
- **Infopankki**: Finnish immigration service multilingual corpus
- **TICO-19**: Translation Initiative for COVID-19 corpus
- **TLDR Pages**: Community-maintained help pages
- **ELRC**: European Language Resource Coordination corpus
- **PHP**: PHP documentation corpus

**Synthetic Data Generation:**

For Spanish-Hindi (es-hi) and Spanish-Chinese (es-zh) language pairs, synthetic Spanish parallel data was created by translating the English side of the en-hi
and en-zh datasets to Spanish using [SalamandraTA 7B Instruct](https://huggingface.co/BSC-LT/salamandra-7b-instruct).

**Data Filtering and Normalization:**

All data underwent rigorous filtering and normalization:
- **Alignment filtering**: Sentence-level alignments were calculated using [LaBSE](https://huggingface.co/sentence-transformers/LaBSE), and sentence pairs with a similarity score below 0.75 were discarded.
- **Language identification**: The probability of being the target language was calculated using [Lingua.py](https://github.com/pemistahl/lingua-py), and sentences with a language probability score below 0.5 were discarded.
- **Normalization**: Text was normalized using [Bifixer](https://github.com/bitextor/bifixer) to ensure consistency and quality.
- **Deduplication**: The filtered datasets were deduplicated to remove redundant sentence pairs.

The filtered and normalized datasets were then concatenated to form the final corpus.

#### Who are the source language producers?

- [OPUS](https://opus.nlpl.eu/) and its constituent corpora
- [NLLB Team](https://ai.meta.com/research/no-language-left-behind/)
- [ParaCrawl](https://paracrawl.eu/)
- [Tatoeba Community](https://tatoeba.org/)
- Various other open-source and institutional contributors

### Annotations

#### Annotation process

The dataset does not contain any manual annotations beyond the parallel alignments, which were either preserved from source datasets or validated through automated alignment scoring.

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

Given that this dataset is derived from pre-existing datasets that may contain crawled data, and that no specific anonymisation process has been applied, personal and sensitive information may be present in the data. This needs to be considered when using the data for training models.

## Considerations for Using the Data

### Social Impact of Dataset

By providing this large-scale multilingual resource, we intend to promote multilingual NLP research and improve the accessibility of machine translation for the included languages, particularly for language pairs that may be underrepresented in existing resources. This contributes to reducing language barriers and supporting linguistic diversity in NLP applications.

### Discussion of Biases

No specific bias mitigation strategies were applied to this dataset beyond quality filtering. Inherent biases may exist within the data, reflecting the biases present in the source datasets, which include web-crawled content, subtitles, news articles, and other user-generated or institutionally produced text. Users should be aware that the es-hi and es-zh datasets contain synthetically generated Spanish text, which may reflect biases present in the translation model used.

### Other Known Limitations

The dataset contains data of a general domain. Application of this dataset in more specific domains such as biomedical, legal, technical, or other specialized fields would be of limited use. Additionally, the synthetic Spanish data in es-hi and es-zh pairs may not achieve the same quality or naturalness as naturally parallel data.

## Additional Information

### Dataset Curators

Language Technologies Unit at the Barcelona Supercomputing Center (langtech@bsc.es).

### Funding

This work is funded by the Ministerio para la Transformación Digital y de la Función Pública - Funded by EU – NextGenerationEU within the framework of the project Desarrollo de Modelos ALIA.


### Licensing Information

This work is licensed under a [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) licence.


### Citation Information

[N/A]

### Contributions

[N/A]
