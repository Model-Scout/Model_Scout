---
license: cc-by-nc-4.0
pretty_name: NayanaOCRBench · Natural
language:
- en
- hi
- bn
- mr
- gu
- pa
- or
- kn
- ta
- te
- ml
- sa
- zh
- ja
- ko
- de
- fr
- es
- it
- ru
- ar
- th
task_categories:
- image-to-text
- image-text-to-text
tags:
- ocr
- document-ai
- multilingual
- indic
- benchmark
- nayana
size_categories:
- 10K<n<100K
dataset_info:
- config_name: ar
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 84172779
    num_examples: 452
  download_size: 75312596
  dataset_size: 84172779
- config_name: bn
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 363777768
    num_examples: 467
  download_size: 351188470
  dataset_size: 363777768
- config_name: de
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 256198272
    num_examples: 496
  download_size: 247088483
  dataset_size: 256198272
- config_name: en
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 352321038
    num_examples: 502
  download_size: 342038327
  dataset_size: 352321038
- config_name: es
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 254559897
    num_examples: 500
  download_size: 245031905
  dataset_size: 254559897
- config_name: fr
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 311748909
    num_examples: 504
  download_size: 302163484
  dataset_size: 311748909
- config_name: gu
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 313843900
    num_examples: 445
  download_size: 303406030
  dataset_size: 313843900
- config_name: hi
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 627663284
    num_examples: 500
  download_size: 614340748
  dataset_size: 627663284
- config_name: it
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 264208096
    num_examples: 494
  download_size: 254950738
  dataset_size: 264208096
- config_name: ja
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 262023117
    num_examples: 502
  download_size: 253660759
  dataset_size: 262023117
- config_name: kn
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 445029556
    num_examples: 500
  download_size: 433218368
  dataset_size: 445029556
- config_name: ko
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 212298028
    num_examples: 454
  download_size: 205400783
  dataset_size: 212298028
- config_name: ml
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 412068222
    num_examples: 492
  download_size: 398816737
  dataset_size: 412068222
- config_name: mr
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 308159592
    num_examples: 515
  download_size: 294636998
  dataset_size: 308159592
- config_name: or
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 119336908
    num_examples: 301
  download_size: 114715905
  dataset_size: 119336908
- config_name: pa
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 339772334
    num_examples: 463
  download_size: 330600189
  dataset_size: 339772334
- config_name: ru
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 281196948
    num_examples: 523
  download_size: 267941400
  dataset_size: 281196948
- config_name: sa
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 676316070
    num_examples: 425
  download_size: 667392005
  dataset_size: 676316070
- config_name: ta
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 146601476
    num_examples: 504
  download_size: 138418137
  dataset_size: 146601476
- config_name: te
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 276840834
    num_examples: 461
  download_size: 265885956
  dataset_size: 276840834
- config_name: th
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 400503266
    num_examples: 507
  download_size: 385028663
  dataset_size: 400503266
- config_name: zh
  features:
  - name: image
    dtype: image
  - name: id
    dtype: string
  - name: omnidocbench
    dtype: string
  - name: omnidocbench_original
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: omnidocbench_norm1000
    struct:
    - name: layout_dets
      list:
      - name: anno_id
        dtype: int64
      - name: category_type
        dtype: string
      - name: html
        dtype: 'null'
      - name: ignore
        dtype: bool
      - name: latex
        dtype: 'null'
      - name: order
        dtype: int64
      - name: poly
        list: int64
      - name: text
        dtype: string
    - name: page_info
      struct:
      - name: height
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
          dtype: string
      - name: page_no
        dtype: int64
      - name: width
        dtype: int64
  - name: html_norm1000
    dtype: string
  - name: md_norm1000
    dtype: string
  - name: layout_content_norm1000
    list:
    - name: bbox
      list: int64
    - name: content
      dtype: string
    - name: type
      dtype: string
  - name: layout_norm1000
    list:
    - name: bbox
      list: int64
    - name: type
      dtype: string
  splits:
  - name: train
    num_bytes: 286549331
    num_examples: 526
  download_size: 276927181
  dataset_size: 286549331
configs:
- config_name: ar
  data_files:
  - split: train
    path: ar/train-*
- config_name: bn
  data_files:
  - split: train
    path: bn/train-*
- config_name: de
  data_files:
  - split: train
    path: de/train-*
- config_name: en
  data_files:
  - split: train
    path: en/train-*
- config_name: es
  data_files:
  - split: train
    path: es/train-*
- config_name: fr
  data_files:
  - split: train
    path: fr/train-*
- config_name: gu
  data_files:
  - split: train
    path: gu/train-*
- config_name: hi
  data_files:
  - split: train
    path: hi/train-*
- config_name: it
  data_files:
  - split: train
    path: it/train-*
- config_name: ja
  data_files:
  - split: train
    path: ja/train-*
- config_name: kn
  data_files:
  - split: train
    path: kn/train-*
- config_name: ko
  data_files:
  - split: train
    path: ko/train-*
- config_name: ml
  data_files:
  - split: train
    path: ml/train-*
- config_name: mr
  data_files:
  - split: train
    path: mr/train-*
- config_name: or
  data_files:
  - split: train
    path: or/train-*
- config_name: pa
  data_files:
  - split: train
    path: pa/train-*
- config_name: ru
  data_files:
  - split: train
    path: ru/train-*
- config_name: sa
  data_files:
  - split: train
    path: sa/train-*
- config_name: ta
  data_files:
  - split: train
    path: ta/train-*
- config_name: te
  data_files:
  - split: train
    path: te/train-*
- config_name: th
  data_files:
  - split: train
    path: th/train-*
- config_name: zh
  data_files:
  - split: train
    path: zh/train-*
---

# NayanaOCRBench · Natural

**Human-verified OCR benchmark on real documents in 22 languages.** 10,533 pages of scanned, photographed and
born-digital documents (government gazettes, newspapers, forms, books, reports) whose layout and text were machine-proposed and then
corrected by human annotators, in OmniDocBench format.

👁️ **Browse every model output on every page:** [https://huggingface.co/spaces/AdithyaSK/NayanaOCRBench](https://huggingface.co/spaces/AdithyaSK/NayanaOCRBench)

## What is in a row

| Column | Type | Meaning |
|---|---|---|
| `image` | Image | the document page |
| `id` | string | page id, e.g. `kn_pdf_0003_page_00226` |
| `omnidocbench` / `omnidocbench_original` / `omnidocbench_norm1000` | struct | OmniDocBench JSON: layout blocks with category, polygon, reading order and text (original pixels and 1000×1000 normalised) |
| `md_norm1000` / `html_norm1000` | string | full-page ground truth in reading order, Markdown and HTML |
| `layout_norm1000` | list | `{type, bbox}` per block on a 1000×1000 grid |
| `layout_content_norm1000` | list | `{type, bbox, content}` per block |

One config per language: English 502 · Hindi 500 · Bengali 467 · Marathi 515 · Gujarati 445 · Punjabi 463 · Odia 301 · Kannada 500 · Tamil 504 · Telugu 461 · Malayalam 492 · Sanskrit 425 · Chinese 526 · Japanese 502 · Korean 454 · German 496 · French 504 · Spanish 500 · Italian 494 · Russian 523 · Arabic 452 · Thai 507.

## How it was built

1. Real pages collected per language and de-duplicated.
2. Layout proposed with MinerU, then corrected by annotators (block classes, boxes, reading order).
3. Text extracted per block by frontier VLMs, then reviewed line by line by human annotators.
4. Exported to OmniDocBench format so existing evaluation tooling works unchanged.

## Zero-shot results (character accuracy = 100 − CER)

13 open vision-language and OCR models, one shared prompt, full-page plain-text OCR. Per-page predictions, scores and the evaluation
harness are public in [https://huggingface.co/buckets/Cognitive-Lab/nayanaocrbench-evals](https://huggingface.co/buckets/Cognitive-Lab/nayanaocrbench-evals); the [explorer Space](https://huggingface.co/spaces/AdithyaSK/NayanaOCRBench) shows the page, ground truth and each model's output side by side.

| Model | Langs | Avg (all, missing = 0) | Avg (evaluated) | Indic | East Asian | European | Other |
|---|---:|---:|---:|---:|---:|---:|---:|
| dots.mocr | 22/22 | 71.9 | 71.9 | 63.9 | 69.7 | 85.3 | 79.2 |
| Qwen3.5-9B | 22/22 | 66.9 | 66.9 | 49.1 | 75.2 | 90.9 | 80.3 |
| Qwen3-VL-8B | 22/22 | 64.7 | 64.7 | 44.0 | 75.1 | 90.7 | 85.1 |
| Qwen3.5-4B | 22/22 | 62.2 | 62.2 | 45.2 | 67.6 | 88.5 | 68.4 |
| Gemma 4 31B | 21/22 | 61.1 | 64.0 | 52.5 | 61.4 | 81.4 | 73.6 |
| Gemma 4 E4B | 22/22 | 59.5 | 59.5 | 42.1 | 62.2 | 84.9 | 75.3 |
| Gemma 3 27B | 22/22 | 58.4 | 58.4 | 47.1 | 57.2 | 76.0 | 68.9 |
| Qwen3.5-2B | 22/22 | 57.0 | 57.0 | 36.5 | 70.7 | 86.4 | 60.9 |
| DeepSeek-OCR | 13/22 | 43.2 | 73.1 | 39.1 | 71.2 | 86.6 | 69.1 |
| Gemma 4 E2B | 22/22 | 41.0 | 41.0 | 24.0 | 44.1 | 67.6 | 50.3 |
| GLM-OCR 1.3B | 9/22 | 32.7 | 79.9 | — | 66.0 | 86.8 | — |
| Llama 4 Scout 17B | 8/22 | 30.4 | 83.5 | 71.5 | — | 87.1 | 80.5 |
| GLM-4.6V-Flash | 8/22 | 28.6 | 78.8 | — | 83.2 | 80.8 | 62.0 |

<details><summary>Per-language accuracy</summary>

| Model | en | hi | bn | mr | gu | pa | or | kn | ta | te | ml | sa | zh | ja | ko | de | fr | es | it | ru | ar | th |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dots.mocr | 75.8 | 61.8 | 64.7 | 54.3 | 71.8 | 61.0 | 54.0 | 54.1 | 77.7 | 71.9 | 60.6 | 70.9 | 79.7 | 51.5 | 77.8 | 86.3 | 84.5 | 88.1 | 87.9 | 88.9 | 83.4 | 75.1 |
| Qwen3.5-9B | 82.3 | 76.1 | 68.8 | 62.1 | 55.0 | 72.0 | 3.0 | 9.5 | 71.6 | 43.8 | 12.1 | 66.1 | 87.3 | 55.8 | 82.4 | 93.0 | 90.2 | 91.5 | 93.8 | 94.3 | 78.6 | 81.9 |
| Qwen3-VL-8B | 80.0 | 73.3 | 74.3 | 68.4 | 28.6 | 66.5 | 5.4 | 5.9 | 60.7 | 17.0 | 13.6 | 70.0 | 88.1 | 54.4 | 82.9 | 92.0 | 91.2 | 92.8 | 94.0 | 94.3 | 86.8 | 83.4 |
| Qwen3.5-4B | 77.0 | 66.2 | 61.5 | 55.3 | 45.2 | 68.0 | 4.1 | 11.6 | 70.6 | 38.2 | 18.6 | 57.5 | 74.4 | 49.0 | 79.4 | 90.5 | 88.6 | 91.0 | 91.9 | 92.2 | 67.2 | 69.6 |
| Gemma 4 31B | 74.5 | 54.9 | 45.7 | 51.2 | 63.6 | — | 45.4 | 40.8 | 73.7 | 58.7 | 37.7 | 53.4 | 75.9 | 40.5 | 67.8 | 82.4 | 82.7 | 83.0 | 85.3 | 80.3 | 72.4 | 74.7 |
| Gemma 4 E4B | 73.8 | 57.4 | 47.2 | 48.6 | 51.1 | 39.4 | 11.9 | 25.2 | 62.6 | 44.2 | 23.9 | 52.0 | 71.8 | 45.7 | 69.1 | 86.1 | 84.6 | 88.4 | 89.6 | 86.8 | 81.4 | 69.1 |
| Gemma 3 27B | 66.4 | 51.4 | 40.7 | 47.7 | 57.3 | 46.9 | 39.7 | 30.9 | 67.9 | 54.9 | 28.0 | 53.3 | 69.0 | 40.6 | 62.1 | 77.4 | 75.0 | 80.5 | 80.2 | 76.8 | 77.0 | 60.8 |
| Qwen3.5-2B | 75.9 | 56.4 | 55.0 | 43.5 | 34.7 | 58.2 | 1.0 | 3.5 | 63.7 | 32.3 | 4.8 | 48.2 | 84.4 | 51.8 | 75.9 | 88.5 | 88.2 | 86.6 | 90.3 | 88.8 | 56.4 | 65.4 |
| DeepSeek-OCR | 76.4 | 38.1 | 40.0 | — | — | — | — | — | — | — | — | — | 85.3 | 49.7 | 78.5 | 87.6 | 87.0 | 90.5 | 91.1 | 87.1 | 79.0 | 59.3 |
| Gemma 4 E2B | 60.0 | 37.1 | 20.7 | 33.0 | 17.3 | 13.7 | 5.1 | 10.7 | 46.8 | 30.5 | 9.2 | 40.2 | 50.7 | 33.5 | 48.1 | 66.7 | 67.5 | 73.1 | 72.6 | 65.8 | 60.8 | 39.7 |
| GLM-OCR 1.3B | 76.4 | — | — | — | — | — | — | — | — | — | — | — | 80.5 | 51.2 | 66.3 | 90.0 | 89.8 | 91.7 | 92.0 | 80.9 | — | — |
| Llama 4 Scout 17B | 75.7 | 71.5 | — | — | — | — | — | — | — | — | — | — | — | — | — | 89.9 | 86.1 | 92.9 | 90.8 | — | 77.4 | 83.7 |
| GLM-4.6V-Flash | 65.8 | — | — | — | — | — | — | — | — | — | — | — | 83.2 | — | — | 82.4 | 80.2 | 82.5 | 86.5 | 87.5 | 62.0 | — |

</details>

Grey / missing cells: the model card does not claim the language, so it was not run. "Avg (all)" counts those as 0, which is what a
user of a general multilingual model experiences; "Avg (evaluated)" averages only the languages that were run.

**Finding.** Latin, Cyrillic and CJK are largely solved. Kannada, Odia, Malayalam and Telugu are not: the strongest general-purpose
family scores above 90% on European scripts and under 20% on those four at every model size. The gap is a data gap, which is what
the [NayanaOCR corpora](https://huggingface.co/datasets/Cognitive-Lab/NayanaOCR_Corpus_2025) exist to close.

## Related

- Companion held-out synthetic set: [Cognitive-Lab/NayanaOCRBench_Synthetic](https://huggingface.co/datasets/Cognitive-Lab/NayanaOCRBench_Synthetic)
- Training corpus (public, 1M pages): [Cognitive-Lab/NayanaOCR_Corpus_2025](https://huggingface.co/datasets/Cognitive-Lab/NayanaOCR_Corpus_2025)
- Retrieval benchmark: [Nayana-IR Bench](https://huggingface.co/collections/Cognitive-Lab/nayanair-bench)

## License and citation

CC BY-NC 4.0. Free for research and education with attribution; commercial use: contact@cognitivelab.in.

```bibtex
@inproceedings{kolavi2025nayanaocr,
  title     = {Nayana {OCR}: A Scalable Framework for Document {OCR} in Low-Resource Languages},
  author    = {Kolavi, Adithya S. and Samarth, P. and Jain, Vyoman},
  booktitle = {Proceedings of the 1st Workshop on Language Models for Underserved Communities (LM4UC), NAACL},
  year      = {2025}, pages = {86--103}, url = {https://aclanthology.org/2025.lm4uc-1.11/}
}
@inproceedings{kolavi2025nayana,
  title     = {Nayana: A Foundation for Document-Centric Vision-Language Models via Multi-Task, Multimodal, and Multilingual Data Synthesis},
  author    = {Kolavi, Adithya S. and Samarth, P. and Jain, Vyoman},
  booktitle = {ICCV Workshops (CV4DC)}, year = {2025}, pages = {1678--1687}
}
```

Part of the Nayana initiative by [Cognitive Lab](https://cognitivelab.in), a 2025 Meta Llama Impact Grant recipient.
