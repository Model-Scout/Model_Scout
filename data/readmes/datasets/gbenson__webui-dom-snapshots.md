---
license: cc0-1.0
size_categories:
- 1K<n<10K
source_datasets:
- biglab/webui-7k
- original
multilinguality:
- multilingual
task_categories:
- image-feature-extraction
- reinforcement-learning
- text-classification
pretty_name: WebUI DOM snapshots
dataset_info:
  features:
  - name: image
    dtype: image
  - name: requested_url
    dtype: string
  - name: displayed_url
    dtype: string
  - name: num_frames
    dtype: int64
  - name: body_elements
    sequence: string
  - name: dom_snapshot
    struct:
    - name: documents
      list:
      - name: documentURL
        dtype: int64
      - name: title
        dtype: int64
      - name: baseURL
        dtype: int64
      - name: contentLanguage
        dtype: int64
      - name: encodingName
        dtype: int64
      - name: publicId
        dtype: int64
      - name: systemId
        dtype: int64
      - name: frameId
        dtype: int64
      - name: nodes
        struct:
        - name: parentIndex
          sequence: int64
        - name: nodeType
          sequence: int64
        - name: shadowRootType
          struct:
          - name: index
            sequence: int64
          - name: value
            sequence: int64
        - name: nodeName
          sequence: int64
        - name: nodeValue
          sequence: int64
        - name: backendNodeId
          sequence: int64
        - name: attributes
          sequence:
            sequence: int64
        - name: textValue
          struct:
          - name: index
            sequence: int64
          - name: value
            sequence: int64
        - name: inputValue
          struct:
          - name: index
            sequence: int64
          - name: value
            sequence: int64
        - name: inputChecked
          struct:
          - name: index
            sequence: int64
        - name: optionSelected
          struct:
          - name: index
            sequence: int64
        - name: contentDocumentIndex
          struct:
          - name: index
            sequence: int64
          - name: value
            sequence: int64
        - name: pseudoType
          struct:
          - name: index
            sequence: int64
          - name: value
            sequence: int64
        - name: pseudoIdentifier
          struct:
          - name: index
            sequence: 'null'
          - name: value
            sequence: 'null'
        - name: isClickable
          struct:
          - name: index
            sequence: int64
        - name: currentSourceURL
          struct:
          - name: index
            sequence: int64
          - name: value
            sequence: int64
        - name: originURL
          struct:
          - name: index
            sequence: 'null'
          - name: value
            sequence: 'null'
      - name: layout
        struct:
        - name: nodeIndex
          sequence: int64
        - name: styles
          sequence:
            sequence: int64
        - name: bounds
          sequence:
            sequence: float64
        - name: text
          sequence: int64
        - name: stackingContexts
          struct:
          - name: index
            sequence: int64
        - name: paintOrders
          sequence: int64
      - name: textBoxes
        struct:
        - name: layoutIndex
          sequence: int64
        - name: bounds
          sequence:
            sequence: float64
        - name: start
          sequence: int64
        - name: length
          sequence: int64
      - name: scrollOffsetX
        dtype: int64
      - name: scrollOffsetY
        dtype: int64
      - name: contentWidth
        dtype: int64
      - name: contentHeight
        dtype: int64
    - name: strings
      sequence: string
  - name: capture_options
    struct:
    - name: computedStyles
      sequence: string
    - name: includePaintOrder
      dtype: bool
  - name: source_index
    dtype: int64
  - name: source_key_name
    dtype: string
  - name: source_image_ssim
    dtype: float64
  - name: detected_language
    dtype: string
  splits:
  - name: train
    num_bytes: 2707342861
    num_examples: 4536
  download_size: 1972567064
  dataset_size: 2707342861
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- en
- nl
- fr
- zh
- ja
- de
- id
- cs
- ru
- pt
- fi
- sv
- 'no'
- pl
- da
- sl
- hu
- vi
- is
- ko
- th
- tr
- ar
- bg
- el
- uk
- es
- et
- gd
- ne
- sk
- af
- bn
- gl
- hi
- it
- lt
- lv
- ml
- sr
- to
---

# Dataset Card for WebUI DOM snapshots

<!-- Provide a quick summary of the dataset. -->

This dataset card aims to be a base template for new datasets. It has been generated using [this raw template](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/datasetcard_template.md?plain=1).

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->



- **Curated by:** [Gary Benson](https://gbenson.net/)
<!-- **Funded by [optional]:** [More Information Needed] -->
- **Languages:** Mostly English (87%);
  Dutch, French, Chinese, Japanese (1-2% each); 30+ others (<1% each)
- **License:** [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)

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
<!-- 
There are no splits in this dataset. It is given as is.
There are no recommended data splits. The authors use all books in the dataset for unsupervised training, with no splits or subsamples.
-->

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

87% of the examples are English.
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