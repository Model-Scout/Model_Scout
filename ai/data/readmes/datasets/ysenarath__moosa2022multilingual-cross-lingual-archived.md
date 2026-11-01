---
license: odc-by
dataset_info:
  features:
  - name: text
    dtype: string
  - name: labels
    dtype: int64
  - name: lang
    dtype: string
  - name: original_lang
    dtype: string
  - name: fold
    dtype: string
  splits:
  - name: train
    num_bytes: 483037284
    num_examples: 2573766
  - name: valid
    num_bytes: 53558688
    num_examples: 285987
  - name: test
    num_bytes: 58934578
    num_examples: 317837
  download_size: 297205502
  dataset_size: 595530550
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: valid
    path: data/valid-*
  - split: test
    path: data/test-*
task_categories:
- text-classification
language:
- ar
- en
- zh
- fr
- de
- ru
- tr
- hi
- ko
- it
- es
- pt
- id
pretty_name: Multilingual Hate Speech Detection by Moosa et al. (2022)
---
# Dataset Card for Multilingual Hate Speech Dataset

<!-- Provide a quick summary of the dataset. -->

This dataset card provides information about the Multilingual Hate Speech Dataset, which was originally hosted on Kaggle. 
The Multilingual Hate Speech Dataset is a modified version of an original multilingual hate speech dataset. In this version, examples from each language have been translated into the other languages present in the dataset, creating a more comprehensive cross-lingual resource.

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->

- **Curated by:** Wajid Hassan Moosa and Najiba
- **Shared by:** Yasas (for private use only)
- **Language(s) (NLP):** Arabic, English, Chinese, French, German, Russian, Turkish, Roman Hindi/Urdu, Korean, Italian, Spanish, Portuguese, Indonesian
- **License:** Open Data Commons Attribution License (ODC-By) v1.0

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** https://www.kaggle.com/datasets/wajidhassanmoosa/multilingual-hatespeech-dataset/data
<!-- - **Paper [optional]:** [More Information Needed] -->
<!-- - **Demo [optional]:** [More Information Needed] -->

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

This dataset is intended for training and evaluating machine learning models for hate speech detection across multiple languages. It can be used for:

- Developing multilingual/cross-lingual hate speech classifiers
- Comparative studies of hate speech patterns across different languages
- Improving content moderation systems for multilingual platforms

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->

- This dataset should not be used to make decisions about individuals or to profile users based on their language use.
- It should not be considered a comprehensive representation of hate speech in all contexts or cultures.
- The dataset should not be used for any activity that harms its intended purpose of societal good.

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->

The dataset is structured as a collection of records, each containing the following fields:

- text: The content of the message or post (string).
- labels: A binary classification label (integer). 0 indicates non-hate speech, while 1 indicates hate speech.
- lang: The language of the text (string).
- original_lang: The original language of the text (string). This might differ from lang if translation was involved.
- fold: Indicates which subset of the data this sample belongs to (string). One of [train, test, valid].

<!-- ## Dataset Creation -->

<!-- ### Curation Rationale -->

<!-- Motivation for the creation of this dataset. -->

This dataset was created to enhance an existing multilingual hate speech dataset by providing translations of each example into all other languages present in the dataset. This approach aims to support more robust cross-lingual hate speech detection and analysis.

<!-- ### Source Data -->

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

<!-- #### Data Collection and Processing -->

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->

[More Information Needed]

<!-- #### Who are the source data producers? -->

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->

<!-- ### Annotations [optional] -->

<!-- If the dataset contains annotations which are not part of the initial data collection, use this section to describe them. -->

<!-- #### Annotation process -->

<!-- This section describes the annotation process such as annotation tools used in the process, the amount of data annotated, annotation guidelines provided to the annotators, interannotator statistics, annotation validation, etc. -->

<!-- [More Information Needed] -->

<!-- #### Who are the annotators? -->

<!-- This section describes the people or systems who created the annotations. -->

<!-- [More Information Needed] -->

<!-- #### Personal and Sensitive Information -->

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->

<!-- [More Information Needed] -->

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

- While the dataset contains original texts in multiple languages, the translations may introduce biases or inaccuracies.
- The effectiveness of hate speech detection models may vary between original texts and translations.
- Cultural and linguistic nuances specific to hate speech in each language may be better preserved in original texts than in translations.
- There may be other biases pertaining to the original dataset.

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

<!-- Users should be made aware of the risks, biases and limitations of the dataset. More information needed for further recommendations. -->

- Users should consider the origin of each example (original or translation) when training and evaluating models.
- Comparative studies between original texts and their translations could provide insights into the impact of translation on hate speech detection.

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```bibtex
@misc{wajid_hassan_moosa_najiba_2022,
	title={Multi-lingual HateSpeech Dataset},
	url={https://www.kaggle.com/ds/2260058},
	DOI={10.34740/KAGGLE/DS/2260058},
	publisher={Kaggle},
	author={Wajid Hassan Moosa and Najiba},
	year={2022}
}
```

**APA:**

```text
Wajid Hassan Moosa, and Najiba. (2022). Multi-lingual HateSpeech Dataset [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DS/2260058
```

<!-- ## Glossary [optional] -->

<!-- If relevant, include terms and calculations in this section that can help readers understand the dataset or dataset card. -->

<!-- ## More Information [optional] -->

<!-- ## Dataset Card Authors [optional] -->

<!-- ## Dataset Card Contact -->