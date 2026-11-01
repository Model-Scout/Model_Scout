---
language:
- es
- ar
- zh
- hi
- ko
- ja
- et
- mt
- ga
- be
- hy
- id
- is
- kk
- se
- cy

multilinguality:
- multilingual
pretty_name: "UnderRes-Spanish-MT: Spanish-centric parallel corpus for under-resourced language pairs"
size_categories:
- 100M<n<1B
task_categories:
- translation
language_creators:
- found
- machine-generated
license: cc-by-sa-4.0
tags:
- synthetic
- machine-translated
configs:
  - config_name: es-ar
    data_files:
      - split: train
        path: data/es-ar.parquet
  - config_name: es-zh
    data_files:
      - split: train
        path: data/es-zh.parquet
  - config_name: es-hi
    data_files:
      - split: train
        path: data/es-hi.parquet
  - config_name: es-ko
    data_files:
      - split: train
        path: data/es-ko.parquet
  - config_name: es-ja
    data_files:
      - split: train
        path: data/es-ja.parquet
  - config_name: es-et
    data_files:
      - split: train
        path: data/es-et.parquet
  - config_name: es-mt
    data_files:
      - split: train
        path: data/es-mt.parquet
  - config_name: es-ga
    data_files:
      - split: train
        path: data/es-ga.parquet
  - config_name: es-be
    data_files:
      - split: train
        path: data/es-be.parquet
  - config_name: es-hy
    data_files:
      - split: train
        path: data/es-hy.parquet
  - config_name: es-id
    data_files:
      - split: train
        path: data/es-id.parquet
  - config_name: es-is
    data_files:
      - split: train
        path: data/es-is.parquet
  - config_name: es-kk
    data_files:
      - split: train
        path: data/es-kk.parquet
  - config_name: es-se
    data_files:
      - split: train
        path: data/es-se.parquet
  - config_name: es-zh-TW
    data_files:
      - split: train
        path: data/es-zh-TW.parquet
  - config_name: es-cy
    data_files:
      - split: train
        path: data/es-cy.parquet
---
# Dataset Card for UnderRes-Spanish-MT

## Dataset Description

- **Point of Contact:** ai_institute_mt@bsc.es

### Dataset Summary

This corpus was compiled as part of the **AI-TraLow project**, funded by MCIN/AEI. It aggregates approximately **175.3 million sentence pairs** across 16 language pairs, all of them with Spanish on one side. The corpus contains two kinds of data, which are kept in separate subsets:

- **Authentic data (8 pairs, ~97.8M sentence pairs):** Spanish paired with non-EU and migrant languages (Arabic, Chinese, Hindi, Korean, Japanese) and with the EU official languages with lower resource availability (Estonian, Maltese, Irish). Both sides come from existing parallel corpora.
- **Synthetic Spanish data (8 pairs, ~77.5M sentence pairs):** Spanish paired with a further non-EU and migrant language variant (Chinese Traditional, Taiwan) and with other low-resource languages (Belarusian, Armenian, Indonesian, Icelandic, Kazakh, Northern Sami, Welsh). For these languages, no sufficiently large Spanish-paired corpora were available, so the **Spanish side was produced by machine translation** of the English side of existing English-XX parallel corpora. The non-Spanish side is original (not machine-translated).

### Supported Tasks and Leaderboards

- **Machine Translation:** parallel sentence pairs for the language pairs ES-AR, ES-ZH, ES-HI, ES-KO, ES-JA, ES-ET, ES-MT, ES-GA (authentic), and ES-BE, ES-HY, ES-ID, ES-IS, ES-KK, ES-SE, ES-ZH-TW, ES-CY (synthetic Spanish side).

### Languages

The dataset covers 16 language pairs, all with Spanish (`es`) as one side. Each pair is a separate subset (configuration), e.g. `load_dataset("LangTech-MT/UnderRes-Spanish-MT", "es-ar")`.

| Pair                         | Language                                | Category                 | Spanish side                              | Size (sentence pairs) |
| ---------------------------- | --------------------------------------- | ------------------------ | ----------------------------------------- | --------------------- |
| ES-AR                        | Arabic (`ar`)                         | Non-EU / migrant         | Authentic                                 | 14,991,369            |
| ES-ZH                        | Chinese Simplified (`zh`)             | Non-EU / migrant         | Authentic                                 | 14,996,924            |
| ES-HI                        | Hindi (`hi`)                          | Non-EU / migrant         | Authentic                                 | 14,994,669            |
| ES-KO                        | Korean (`ko`)                         | Non-EU / migrant         | Authentic                                 | 14,993,592            |
| ES-JA                        | Japanese (`ja`)                       | Non-EU / migrant         | Authentic                                 | 14,996,750            |
| ES-ET                        | Estonian (`et`)                       | EU official low-resource | Authentic                                 | 15,027,899            |
| ES-MT                        | Maltese (`mt`)                        | EU official low-resource | Authentic                                 | 4,907,188             |
| ES-GA                        | Irish (`ga`)                          | EU official low-resource | Authentic                                 | 2,866,017             |
| **Subtotal authentic** |                                         |                          |                                           | **97,774,408**  |
| ES-BE                        | Belarusian (`be`)                     | Other low-resource       | **Machine-translated from English** | 14,914,017            |
| ES-HY                        | Armenian (`hy`)                       | Other low-resource       | **Machine-translated from English** | 5,508,844             |
| ES-ID                        | Indonesian (`id`)                     | Other low-resource       | **Machine-translated from English** | 14,701,513            |
| ES-IS                        | Icelandic (`is`)                      | Other low-resource       | **Machine-translated from English** | 14,920,248            |
| ES-KK                        | Kazakh (`kk`)                         | Other low-resource       | **Machine-translated from English** | 11,819,323            |
| ES-SE                        | Northern Sami (`se`)                  | Other low-resource       | **Machine-translated from English** | 4,270                 |
| ES-ZH-TW                     | Chinese Traditional, Taiwan (`zh-TW`) | Non-EU / migrant         | **Machine-translated from English** | 9,414,043             |
| ES-CY                        | Welsh (`cy`)                          | Other low-resource       | **Machine-translated from English** | 6,199,306             |
| **Subtotal synthetic** |                                         |                          |                                           | **77,481,564**  |
| **Total**              |                                         |                          |                                           | **175,255,972** |

## Dataset Structure

The dataset is provided in parquet format, with a separate file for each language pair. For larger language pairs, several parquet files containing partial datasets may be provided.

Each row contains a parallel sentence pair with the following structure:

```json
{
  "id": 0,
  "lang_pair": "es-ar",
  "source_lang": "es",
  "target_lang": "ar",
  "source": "...",
  "target": "..."
}
```

### Data Fields

- id: Numeric identifier of the sentence pair within its language pair
- lang_pair: Language pair ISO codes (e.g., "es-ar")
- source_lang: ISO code of the source language (always `es`)
- target_lang: ISO code of the target language
- source: Spanish sentence. **For the 8 synthetic subsets (ES-BE, ES-HY, ES-ID, ES-IS, ES-KK, ES-SE, ES-ZH-TW, ES-CY) this sentence is a machine translation from English.**
- target: Sentence in the target language (original text in all subsets)

### Data Splits

The dataset contains a single split: `train`.

## Dataset Creation

### Curation Rationale

This dataset was created as part of the AI-TraLow project, which aims to advance machine translation for low-resource and extremely low-resource languages using decoder-only LLMs. By developing strategies to mitigate data scarcity, the project extends the reach of LLMs to underrepresented languages, supporting the preservation of cultural heritage, the integration of vulnerable migrant communities, and the empowerment of underrepresented language communities.
This dataset is intended as a training resource for machine translation systems, comprising approximately 175.3 million sentence pairs across 16 language pairs, all paired with Spanish. The languages fall into three groups of underrepresented languages: non-EU and migrant languages (Arabic, Chinese Simplified and Traditional, Hindi, Korean, Japanese), EU official languages with comparatively lower resource availability (Estonian, Maltese, Irish), and other low-resource languages (Belarusian, Armenian, Indonesian, Icelandic, Kazakh, Northern Sami, Welsh). This selection was designed to address the translation needs of migrant communities in Spain, the persistent resource gaps affecting smaller EU languages, and the scarcity of Spanish-paired resources for further low-resource languages.

### Source Data

#### Initial Data Collection and Normalization

The corpus is built from the following original datasets collected from various public sources, filtered to include only permissive licensed data. For the authentic subsets, both sides come from these datasets; for the synthetic subsets, the English-XX version of the dataset was used and its English side was machine-translated into Spanish (see [Synthetic Spanish data](#synthetic-spanish-data-machine-translated-from-english)).

<details>
<summary>Show the list of source corpora (30)</summary>

| Source corpus          | License                                            | Authentic language pair(s)               | Synthetic language pair(s)                                |
| ---------------------- | -------------------------------------------------- | ---------------------------------------- | --------------------------------------------------------- |
| Bible (bible-uedin)    | CC0 1.0                                            |                                          | ES-HY, ES-ID, ES-IS, ES-ZH-TW                             |
| DGT                    | CC BY 4.0                                          | ES-ET, ES-GA, ES-MT                      |                                                           |
| EAC Forms              | CC BY 4.0                                          |                                          | ES-IS                                                     |
| EAC Reference          | CC BY 4.0                                          |                                          | ES-IS                                                     |
| EMEA                   | CC BY 4.0                                          | ES-MT                                    | ES-IS                                                     |
| EUBookshop             | CC BY 4.0                                          | ES-GA, ES-MT                             | ES-BE, ES-IS, ES-CY                                       |
| GlobalVoices           | CC BY 3.0                                          |                                          | ES-ID                                                     |
| GNOME                  | CC BY 4.0                                          | ES-GA                                    | ES-BE, ES-HY, ES-ID, ES-IS, ES-KK, ES-ZH-TW, ES-CY        |
| Infopankki             | CC BY 4.0                                          |                                          | ES-ZH-TW                                                  |
| KDE4                   | CC BY 4.0                                          | ES-GA                                    | ES-BE, ES-HY, ES-ID, ES-IS, ES-KK, ES-SE, ES-ZH-TW, ES-CY |
| MDN Web Docs           | CC BY-SA 2.5                                       |                                          | ES-ZH-TW                                                  |
| MultiCCAligned         | CC BY 4.0 / Specific Terms of Agreement            | ES-ZH, ES-HI, ES-KO, ES-JA               | ES-BE, ES-HY, ES-ID, ES-IS, ES-KK, ES-ZH-TW, ES-CY        |
| MultiParaCrawl         | CC0 1.0                                            | ES-ZH, ES-GA, ES-MT                      | ES-HY, ES-ID, ES-IS, ES-ZH-TW                             |
| MultiUN                | CC BY 4.0                                          | ES-ZH                                    | ES-ZH-TW                                                  |
| News-Commentary        | Specific Terms of Agreement                        | ES-ZH                                    | ES-ID, ES-KK, ES-ZH-TW                                    |
| NLLB                   | ODC-BY                                             | ES-AR, ES-ZH, ES-HI, ES-KO, ES-JA, ES-ET | ES-BE, ES-HY, ES-ID, ES-IS, ES-KK, ES-ZH-TW, ES-CY        |
| NTEU                   | Only subsets with CC-BY-4.0 and Apache 2.0 license | ES-ET, ES-GA, ES-MT                      |                                                           |
| OpenSubtitles          | CC BY 4.0                                          | ES-AR, ES-ZH, ES-HI, ES-KO, ES-JA        | ES-BE, ES-HY, ES-ID, ES-IS, ES-KK, ES-SE, ES-ZH-TW        |
| SPC                    | CC BY 3.0                                          |                                          | ES-ZH-TW                                                  |
| Tatoeba                | CC BY 2.0 FR                                       | ES-ZH                                    | ES-BE, ES-HY, ES-ID, ES-IS, ES-KK, ES-SE                  |
| TICO-19                | CC0 1.0                                            |                                          | ES-ID, ES-ZH-TW                                           |
| TildeMODEL             | CC BY 4.0                                          |                                          | ES-IS                                                     |
| tldr-pages             | CC BY 4.0                                          |                                          | ES-ID, ES-ZH-TW                                           |
| Ubuntu                 | CC BY 2.0 UK                                       |                                          | ES-BE, ES-HY, ES-ID, ES-IS, ES-KK, ES-SE, ES-ZH-TW        |
| UNPC                   | CC BY 4.0                                          | ES-AR, ES-ZH                             | ES-ZH-TW                                                  |
| WikiMatrix             | CC BY-SA 4.0                                       | ES-ZH                                    | ES-BE, ES-ID, ES-IS, ES-KK, ES-ZH-TW                      |
| Wikimedia              | CC BY-SA 4.0                                       |                                          | ES-BE, ES-HY, ES-ID, ES-IS, ES-KK, ES-SE, ES-ZH-TW, ES-CY |
| Wikipedia Health (ELG) | CC BY-SA 3.0                                       |                                          | ES-BE, ES-ID, ES-ZH-TW                                    |
| WikiTitles             | CC BY-SA 4.0                                       |                                          | ES-IS, ES-KK, ES-ZH-TW                                    |
| XLENT                  | CC BY 4.0                                          | ES-GA                                    | ES-BE, ES-HY, ES-ID, ES-IS, ES-KK, ES-ZH-TW, ES-CY        |

</details>

#### Data Processing

Data processing was handled through our Translation Data Processing Pipeline [ParaCLEAN](https://github.com/langtech-bsc/ParaCLEAN), which includes the following processing steps:

- Input handling: Read corpora in plain text (.txt), tab-separated (.tsv) or translation memory (.tmx) formats.
- Compute embeddings: Compute multilingual sentence embeddings (default: [LaBSE](https://huggingface.co/sentence-transformers/LaBSE)).
- Language identification: Depending on the specific language pair, language probability is calculated using [GlotLID](https://github.com/cisnlp/GlotLID) or [Lingua.py](https://github.com/pemistahl/lingua-py).
- Filtering: Filter by user-defined embedding scores and language probability thresholds.
- Deduplication: Remove duplicate sentence pairs and fuzzy matches across corpora.

<!-- - Optional [Bifixer](https://github.com/bitextor/bifixer) cleaning: Enables optional Bifixer-based processing if Bifixer is installed. -->

- Normalisation: Standardise punctuation, spacing, and casing.

#### Synthetic Spanish data (machine-translated from English)

For the 8 synthetic subsets, the English side of the processed English–XX corpora was translated into Spanish and paired with the original XX side:

- **Translation model:** [SalamandraTA-7B-Instruct](https://huggingface.co/BSC-LT/salamandraTA-7b-instruct), prompted with the model's chat template and the instruction `Translate the following text from English into Spanish.`; greedy decoding, at most 128 output tokens per sentence.
- **Quality filtering** of the translations (rows dropped, the XX side is never modified):
  - empty translations;
  - truncated translations, i.e. outputs that reached the 128-token limit;
  - translations whose Spanish/English character-length ratio is outside [0.5, 2.0] (applied to English sources of at least 20 characters).

No human post-editing or manual review of the translations was carried out.

#### Who are the source language producers?

<details>
<summary>Show the list of source language producers</summary>

- [Christos Christodouloupoulos and Mark Steedman, University of Edinburgh](https://github.com/christos-c/bible-corpus) - producers of Bible (bible-uedin)
- [City of Helsinki, Infopankki / InfoFinland](https://www.infofinland.fi) - producer of Infopankki
- [Directorate-General for Translation, European Commission](https://commission.europa.eu/about/departments-and-executive-agencies/translation_en) - producer of DGT
- [ELG](https://live.european-language-grid.eu/) - European Language Grid
- [European Commission (Directorate-General for Education, Youth, Sport and Culture, DG EAC)](https://commission.europa.eu/about/departments-and-executive-agencies/education-youth-sport-and-culture_en) - producer of EAC Forms and EAC Reference
- [European Medicines Agency](https://www.ema.europa.eu/) - producer of EMEA
- [Facebook AI / Meta](https://ai.meta.com/) - producer of MultiCCAligned, WikiMatrix, and XLENT
- [Global Voices community](https://globalvoices.org) - producer of GlobalVoices
- [GNOME Project](https://www.gnome.org/) - producer of GNOME
- [Hercules Dalianis and research group](https://aclanthology.org/L10-1001/) - producers of SPC
- [KDE Community](https://kde.org/) - producer of KDE4
- [Mozilla and the MDN contributor community](https://developer.mozilla.org) - producer of MDN Web Docs
- [NLLB Team](https://ai.meta.com/research/no-language-left-behind/)
- [NTEU Project](https://pangeanic.com/nteu)
- [OpenSubtitles.org](https://www.opensubtitles.org)
- [OPUS NLP](https://opus.nlpl.eu/) and its constituent corpora
- [ParaCrawl Project](https://paracrawl.eu/) - producer of MultiParaCrawl
- [Publications Office of the European Union](https://op.europa.eu/) - producer of EUBookshop
- [Tatoeba users community](https://tatoeba.org)
- [Tilde](https://tilde.com) - producer of TildeMODEL
- [tldr-pages community](https://tldr.sh) - producer of tldr-pages
- [Translation Initiative for COVID-19 (TICO-19)](https://tico-19.github.io) - producer of TICO-19
- [Ubuntu translator community (Launchpad), Canonical](https://translations.launchpad.net) - producer of Ubuntu
- [United Nations](https://www.un.org/) - producer of UNPC and MultiUN
- [Wikimedia Foundation](https://wikimediafoundation.org/)
- [WMT (Conference on Machine Translation)](https://www.statmt.org/) - producer of News-Commentary

</details>

### Annotations

#### Annotation process

The dataset does not contain any manual annotations beyond the parallel alignments, which were either preserved from source datasets or validated through automated alignment scoring.

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

Given that this dataset is derived from pre-existing datasets that contain crawled data, and that no specific anonymisation process has been applied, personal and sensitive information may be present in the data. This needs to be considered when using the data for training models. Machine translation preserves such information in the synthetic Spanish side.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset contributes parallel resources for sixteen language pairs combining Spanish with languages spoken by migrant and/or other foreign communities in Spain (Arabic, Chinese Simplified and Traditional, Hindi, Korean, Japanese) as well as lower-resourced EU official languages (Estonian, Maltese, Irish), plus other low-resource languages for which Spanish-paired data was previously scarce (Belarusian, Armenian, Indonesian, Icelandic, Kazakh, Northern Sami, Welsh). Improved MT systems for these language pairs can facilitate communication with public services, support access to information, and help preserve and document these languages digitally, while also contributing to a better balance in the representation of EU official languages, many of which remain underserved by existing MT resources despite their official status.

### Discussion of Biases

No specific bias mitigation strategies were applied to this dataset beyond deduplication and minimal quality filtering. Inherent biases may exist within the data, reflecting the biases present in the source datasets, which include web-crawled content, subtitles, news articles, and other user-generated or institutionally produced text. In the synthetic subsets, the Spanish side may additionally reflect biases of the translation model (e.g. gender defaults when translating from English).

### Other Known Limitations

The data sources vary considerably in domain (legal, institutional, subtitles, web-crawled), which may result in uneven register and stylistic inconsistency across the dataset. Additionally, some language pairs rely heavily on automatically aligned or mined corpora (e.g., NLLB, MultiCCAligned), which can introduce alignment noise or translation quality issues, particularly for the lowest-resource pairs where fewer human-curated sources were available. The number of sentence pairs also varies substantially across language pairs, which may lead to imbalanced representation if the dataset is used without further sampling or weighting.

For the synthetic subsets:

- The Spanish side is machine translation output: it can contain translation errors, unnatural phrasing ("translationese") and English-influenced structures. The quality filter only removes empty, truncated and length-outlier translations; it does not assess adequacy.
- Spanish and XX are not direct translations of each other: both are aligned through English, so any misalignment or error in the original English–XX pair carries over, and meaning shifts can accumulate across the two steps.

## Additional Information

### Dataset Curators

Machine Translation Group, AI Institute, Barcelona Supercomputing Center (ai_institute_mt@bsc.es).

### Funding

This work is supported by MLLM4TRA (PID2024-158157OB-C32) funded by MCIN/AEI/10.13039/501100011033/FEDER, UE.

### Acknowledgements

[N/A]

### Licensing Information

This work is licensed under an [Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)  licence.

Note: Individual source datasets carry their own licences. Users of this aggregated corpus should verify licence compatibility with the intended use case.

Users must ensure compliance with all applicable third-party licenses.

This dataset includes data obtained through web crawling. The provider makes no representations or warranties regarding the ownership or licensing status of the underlying content. Users are responsible for assessing and complying with all applicable intellectual property, privacy, data protection, and other legal requirements.

### Citation Information

[N/A]

### Contributions

[N/A]

### Changelog

- **v2.0** (2026-10-07):
  - Added 8 language pairs with a machine-translated Spanish side: ES-BE, ES-HY, ES-ID, ES-IS, ES-KK, ES-SE, ES-ZH-TW, ES-CY.
  - Rebuilt the 8 authentic subsets to fix quote handling. In v1.0, Spanish or target-side sentences starting with a double quote (`"`) were read as quoted fields, so their quotes were removed (e.g. `"Hola," dijo ella.` became `Hola, dijo ella.`). At least 5.3M rows (~5.4% of the authentic data) are affected; the number of rows per subset is unchanged.
- **v1.0**: initial release with the 8 authentic language pairs.
