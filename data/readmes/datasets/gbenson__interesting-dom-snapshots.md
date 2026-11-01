---
license: cc0-1.0
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
    num_bytes: 176072783.06768078
    num_examples: 295
  download_size: 46652388
  dataset_size: 176072783.06768078
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- en
- zh
- nl
- cs
- ko
pretty_name: Interesting DOM snapshots
size_categories:
- n<1K
source_datasets:
- gbenson/webui-dom-snapshots
---

# Dataset Card for Interesting DOM snapshots

A small split of [gbenson/webui-dom-snapshots](https://huggingface.co/datasets/gbenson/webui-dom-snapshots).

- **Curated by:** [Gary Benson](https://gbenson.net/)
- **Languages:** Mostly English, some Chinese, Dutch, Czech and Korean
- **License:** [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)

## Uses

I'm using it to develop a [DOM-aware tokenizer](https://github.com/gbenson/dom-tokenizers) for HTML.

## Bias, Risks, and Limitations

This isn't a representative split of the source dataset, it's a number of edge cases I flagged to investigate.