---
dataset_info:
  features:
  - name: conversation_id
    dtype: string
  - name: instruction
    dtype: string
  - name: response
    dtype: string
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: gen_input_configs
    struct:
    - name: pre_query_template
      dtype: string
  - name: intent
    dtype: string
  - name: knowledge
    dtype: string
  - name: difficulty
    dtype: string
  - name: difficulty_generator
    dtype: string
  - name: input_quality
    dtype: string
  - name: quality_explanation
    dtype: string
  - name: quality_generator
    dtype: string
  - name: task_category
    dtype: string
  - name: other_task_category
    sequence: string
  - name: task_category_generator
    dtype: string
  - name: llama_guard_2
    dtype: string
  - name: instruct_reward
    dtype: float64
  - name: reward_model
    dtype: string
  - name: language
    dtype: string
  - name: min_neighbor_distance
    dtype: float64
  - name: repeat_count
    dtype: int64
  - name: min_similar_conversation_id
    dtype: string
  - name: response_length
    dtype: int64
  splits:
  - name: train
    num_bytes: 835642107.5149903
    num_examples: 299725
  - name: test
    num_bytes: 100263112.75487225
    num_examples: 35962
  download_size: 385510612
  dataset_size: 935905220.2698625
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
language:
- ko
---

# Dataset Card for Dataset Name

<!-- Provide a quick summary of the dataset. -->

This dataset card aims to be a base template for new datasets. It has been generated using [this raw template](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/datasetcard_template.md?plain=1).

## Dataset Details

### Dataset Description
호랑이 리더 보드 점수 향상을 위한 dataset
- axolotl 지원 format: alpaca, gpteacher (conversation format)

### 파일 목록 및 각 파일의 데이터 개수

1. **STEM_alpaca_data** - 53,960
2. **Applied Science_alpaca_data** - 75,948
3. **kullm-v2-modified** - 152,630
4. **KOR-OpenOrca-Platypus-v2** - 44,394
5. **klue_re_processed** - 32,470
6. **Ko_MMLU_ver0.3** - 221,051
7. **sentineg_dataset** - 3,649
8. **nia_2022_15-2_commonsense_TL** - 400,000
9. **HUMSS_alpaca_data** - 5,715
10. **converted_ko_lima_vicuna_dataset** - 1,030
11. **korSTS_dataset** - 5,691
12. **merge_kobest_dataset_15K** - 15,737
13. **klue_ner_processed** - 21,008
14. **Other_alpaca_data** - 44,977

**총 데이터 개수 (모든 파일 합산):** 1,078,260  
**트레인/테스트 비율:** 300,000 / 36,000



- **Curated by:** [More Information Needed]
- **Funded by [optional]:** [More Information Needed]
- **Shared by [optional]:** [More Information Needed]
- **Language(s) (NLP):** [More Information Needed]
- **License:** [More Information Needed]

### Dataset Sources [optional]

<!-- Provide the basic links for the dataset. -->

- **Repository:** [More Information Needed]
- **Paper [optional]:** [More Information Needed]
- **Demo [optional]:** [More Information Needed]

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

[More Information Needed]

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->

[More Information Needed]

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->

[More Information Needed]

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

[More Information Needed]

### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->

[More Information Needed]

#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->

[More Information Needed]

### Annotations [optional]

<!-- If the dataset contains annotations which are not part of the initial data collection, use this section to describe them. -->

#### Annotation process

<!-- This section describes the annotation process such as annotation tools used in the process, the amount of data annotated, annotation guidelines provided to the annotators, interannotator statistics, annotation validation, etc. -->

[More Information Needed]

#### Who are the annotators?

<!-- This section describes the people or systems who created the annotations. -->

[More Information Needed]

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->

[More Information Needed]

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

[More Information Needed]

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users should be made aware of the risks, biases and limitations of the dataset. More information needed for further recommendations.

## Citation [optional]

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

[More Information Needed]

**APA:**

[More Information Needed]

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the dataset or dataset card. -->

[More Information Needed]

## More Information [optional]

[More Information Needed]

## Dataset Card Authors [optional]

[More Information Needed]

## Dataset Card Contact

[More Information Needed]