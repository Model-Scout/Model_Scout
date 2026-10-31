---
license: cc-by-nc-4.0
pretty_name: NayanaOCRBench · Synthetic
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
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: translation_type
      dtype: string
    - name: skip_reason
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 262396265
    num_examples: 770
  download_size: 192020418
  dataset_size: 262396265
- config_name: bn
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: latex
        dtype: string
      - name: html
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 307981381
    num_examples: 771
  download_size: 232784334
  dataset_size: 307981381
- config_name: de
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: translation_type
      dtype: string
    - name: skip_reason
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 300094733
    num_examples: 771
  download_size: 237405464
  dataset_size: 300094733
- config_name: en
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: translation_type
      dtype: string
    - name: skip_reason
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 278424325
    num_examples: 771
  download_size: 213382296
  dataset_size: 278424325
- config_name: es
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 295098733
    num_examples: 772
  download_size: 231415337
  dataset_size: 295098733
- config_name: fr
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: latex
        dtype: string
      - name: html
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 301002600
    num_examples: 771
  download_size: 237579423
  dataset_size: 301002600
- config_name: gu
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 289835866
    num_examples: 770
  download_size: 215926726
  dataset_size: 289835866
- config_name: hi
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 307453885
    num_examples: 766
  download_size: 233808401
  dataset_size: 307453885
- config_name: it
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 292256204
    num_examples: 772
  download_size: 228733681
  dataset_size: 292256204
- config_name: ja
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: translation_type
      dtype: string
    - name: skip_reason
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 258608151
    num_examples: 771
  download_size: 191738864
  dataset_size: 258608151
- config_name: kn
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 319512361
    num_examples: 772
  download_size: 245870063
  dataset_size: 319512361
- config_name: ko
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: translation_type
      dtype: string
    - name: skip_reason
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 279112756
    num_examples: 771
  download_size: 215197678
  dataset_size: 279112756
- config_name: ml
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: translation_type
      dtype: string
    - name: skip_reason
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 325569789
    num_examples: 772
  download_size: 251921587
  dataset_size: 325569789
- config_name: mr
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: latex
        dtype: string
      - name: html
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 300293198
    num_examples: 766
  download_size: 225276139
  dataset_size: 300293198
- config_name: or
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 311178327
    num_examples: 769
  download_size: 239657522
  dataset_size: 311178327
- config_name: pa
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: latex
        dtype: string
      - name: html
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 303533549
    num_examples: 772
  download_size: 229296657
  dataset_size: 303533549
- config_name: ru
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 304946861
    num_examples: 771
  download_size: 237851653
  dataset_size: 304946861
- config_name: sa
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 294288749
    num_examples: 763
  download_size: 221848898
  dataset_size: 294288749
- config_name: ta
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: latex
        dtype: string
      - name: html
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 333355149
    num_examples: 770
  download_size: 260033453
  dataset_size: 333355149
- config_name: te
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 323735812
    num_examples: 771
  download_size: 250425385
  dataset_size: 323735812
- config_name: th
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: latex
        dtype: string
      - name: html
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 287769214
    num_examples: 771
  download_size: 213217314
  dataset_size: 287769214
- config_name: zh
  features:
  - name: image
    dtype: image
  - name: font_used
    dtype: string
  - name: page_size
    list: int64
  - name: original_id
    dtype: string
  - name: rendered_layout
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: index
      dtype: int64
    - name: content
      dtype: string
    - name: original_content
      dtype: string
    - name: translated
      dtype: bool
    - name: rendered_coordinates
      list: int64
    - name: fit_ratio
      dtype: float64
    - name: skip_reason
      dtype: string
    - name: translation_type
      dtype: string
  - name: translated_tables
    list:
    - name: type
      dtype: string
    - name: coordinates
      list: int64
    - name: content
      dtype: string
    - name: original_bbox
      list: int64
    - name: rendered_bbox
      list: int64
    - name: num_rows
      dtype: int64
    - name: index
      dtype: int64
  - name: vqa_translated
    list:
    - name: user
      dtype: string
    - name: assistant
      dtype: string
    - name: source
      dtype: string
  - name: omnidocbench
    struct:
    - name: layout_dets
      list:
      - name: category_type
        dtype: string
      - name: poly
        list: int64
      - name: ignore
        dtype: bool
      - name: order
        dtype: int64
      - name: anno_id
        dtype: int64
      - name: text
        dtype: string
      - name: html
        dtype: string
      - name: latex
        dtype: string
    - name: page_info
      struct:
      - name: page_no
        dtype: int64
      - name: height
        dtype: int64
      - name: width
        dtype: int64
      - name: image_path
        dtype: string
      - name: page_attribute
        struct:
        - name: language
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
        dtype: string
      - name: ignore
        dtype: bool
      - name: latex
        dtype: string
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
    num_bytes: 269333889
    num_examples: 771
  download_size: 206220894
  dataset_size: 269333889
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

# NayanaOCRBench · Synthetic

**Held-out evaluation split of the NayanaOCR 2026 pipeline, 22 languages, ~770 pages per language.**
Every page is the same source document re-typeset in each language with the layout preserved, so the set is parallel across languages
and carries the full annotation stack of the training corpus: layout, reading-order OCR ground truth, translated tables, VQA pairs.

👁️ **Browse every model output on every page:** [https://huggingface.co/spaces/AdithyaSK/NayanaOCRBench](https://huggingface.co/spaces/AdithyaSK/NayanaOCRBench)

## What is in a row

Same 14 columns as the page-level NayanaOCR corpus: `image`, `font_used`, `page_size`, `original_id` (shared across all 22 language
configs), `rendered_layout` (per region: type, coordinates, original and translated text, fit ratio), `translated_tables` (HTML),
`vqa_translated`, `omnidocbench` / `omnidocbench_original` / `omnidocbench_norm1000`, `html_norm1000`, `md_norm1000`,
`layout_content_norm1000`, `layout_norm1000`.

## Zero-shot results (character accuracy = 100 − CER)

Same protocol and models as the [Natural benchmark](https://huggingface.co/datasets/Cognitive-Lab/NayanaOCRBench_Natural).
**English is excluded from the tables below** while its ground truth is being revised (text leaked into the `latex` field on some
text blocks); all other languages are unaffected. Predictions and scores: [https://huggingface.co/buckets/Cognitive-Lab/nayanaocrbench-evals](https://huggingface.co/buckets/Cognitive-Lab/nayanaocrbench-evals).

| Model | Langs | Avg (all, missing = 0) | Avg (evaluated) | Indic | East Asian | European | Other |
|---|---:|---:|---:|---:|---:|---:|---:|
| dots.mocr | 21/21 | 61.8 | 61.8 | 54.6 | 67.3 | 83.9 | 38.2 |
| Qwen3.5-4B | 21/21 | 59.5 | 59.5 | 43.1 | 76.1 | 89.6 | 49.3 |
| Qwen3.5-9B | 21/21 | 55.0 | 55.0 | 40.8 | 66.3 | 78.4 | 57.3 |
| Gemma 4 E4B | 21/21 | 52.7 | 52.7 | 34.9 | 66.3 | 83.9 | 52.7 |
| Gemma 3 27B | 21/21 | 50.3 | 50.3 | 39.4 | 56.4 | 71.4 | 48.1 |
| Qwen3-VL-8B | 21/21 | 50.2 | 50.2 | 33.6 | 66.1 | 78.3 | 47.1 |
| Gemma 4 31B | 21/21 | 49.7 | 49.7 | 37.8 | 62.5 | 69.3 | 47.3 |
| Qwen3.5-2B | 21/21 | 46.6 | 46.6 | 28.6 | 63.5 | 81.1 | 34.4 |
| Gemma 4 E2B | 21/21 | 36.4 | 36.4 | 19.0 | 48.3 | 68.7 | 33.9 |
| DeepSeek-OCR | 12/21 | 31.8 | 55.7 | 27.7 | 60.1 | 74.1 | 31.4 |
| GLM-OCR 1.3B | 8/21 | 30.5 | 80.0 | — | 68.2 | 87.1 | — |
| GLM-4.6V-Flash | 9/21 | 25.3 | 58.9 | — | 49.4 | 73.4 | 14.9 |
| Llama 4 Scout 17B | 7/21 | 22.1 | 66.4 | 62.4 | — | 75.0 | 51.3 |

<details><summary>Per-language accuracy</summary>

| Model | hi | bn | mr | gu | pa | or | kn | ta | te | ml | sa | zh | ja | ko | de | fr | es | it | ru | ar | th |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dots.mocr | 63.8 | 60.1 | 63.0 | 65.5 | 55.6 | 33.4 | 47.8 | 50.6 | 63.4 | 47.4 | 50.3 | 69.5 | 54.7 | 77.7 | 87.6 | 86.7 | 86.0 | 86.3 | 72.9 | 38.9 | 37.5 |
| Qwen3.5-4B | 72.9 | 65.7 | 66.1 | 48.5 | 63.2 | 2.8 | 4.7 | 61.7 | 18.6 | 10.5 | 58.9 | 73.4 | 67.2 | 87.6 | 89.5 | 91.0 | 89.6 | 89.3 | 88.6 | 39.3 | 59.3 |
| Qwen3.5-9B | 66.9 | 61.9 | 62.2 | 42.9 | 56.2 | 4.0 | 3.0 | 49.6 | 16.2 | 7.0 | 78.8 | 63.3 | 58.9 | 76.6 | 78.3 | 79.2 | 78.2 | 76.7 | 79.5 | 38.8 | 75.7 |
| Gemma 4 E4B | 62.6 | 40.8 | 53.7 | 44.6 | 29.1 | 8.8 | 18.0 | 38.9 | 24.2 | 19.1 | 44.0 | 61.7 | 59.8 | 77.3 | 84.2 | 85.4 | 84.3 | 83.8 | 81.6 | 55.4 | 50.1 |
| Gemma 3 27B | 56.3 | 43.1 | 51.8 | 46.6 | 34.8 | 26.2 | 22.9 | 46.4 | 33.1 | 23.6 | 49.1 | 54.2 | 51.3 | 63.7 | 71.3 | 72.4 | 72.6 | 71.0 | 69.7 | 53.4 | 42.8 |
| Qwen3-VL-8B | 67.8 | 62.2 | 63.8 | 13.9 | 37.1 | 6.8 | 2.6 | 40.2 | 8.9 | 7.7 | 59.0 | 63.0 | 58.6 | 76.8 | 78.7 | 79.3 | 78.0 | 76.5 | 79.0 | 49.6 | 44.6 |
| Gemma 4 31B | 52.2 | 35.2 | 51.4 | 41.2 | 29.3 | 25.2 | 25.7 | 50.7 | 35.3 | 27.0 | 42.8 | 57.5 | 58.1 | 71.9 | 67.2 | 69.2 | 68.2 | 66.7 | 74.9 | 47.9 | 46.7 |
| Qwen3.5-2B | 53.3 | 43.1 | 53.3 | 30.4 | 37.2 | 3.5 | 1.6 | 36.7 | 10.2 | 3.3 | 41.4 | 61.0 | 56.8 | 72.7 | 76.4 | 90.5 | 76.5 | 75.2 | 87.1 | 28.8 | 39.9 |
| Gemma 4 E2B | 39.6 | 22.6 | 35.3 | 15.1 | 9.6 | 6.3 | 5.9 | 20.1 | 14.4 | 6.5 | 33.1 | 44.6 | 46.1 | 54.1 | 67.0 | 71.9 | 71.4 | 69.7 | 63.3 | 36.9 | 30.9 |
| DeepSeek-OCR | 34.3 | 21.0 | — | — | — | — | — | — | — | — | — | 58.4 | 53.9 | 67.9 | 74.6 | 76.5 | 74.5 | 73.4 | 71.4 | 32.3 | 30.5 |
| GLM-OCR 1.3B | — | — | — | — | — | — | — | — | — | — | — | 73.4 | 64.3 | 67.0 | 88.2 | 90.6 | 88.7 | 88.5 | 79.4 | — | — |
| GLM-4.6V-Flash | — | — | — | — | — | — | — | — | — | — | — | 58.2 | 49.8 | 40.3 | 74.4 | 75.7 | 74.6 | 73.7 | 68.8 | 14.9 | — |
| Llama 4 Scout 17B | 62.4 | — | — | — | — | — | — | — | — | — | — | — | — | — | 75.2 | 75.7 | 75.0 | 74.1 | — | 51.7 | 50.9 |

</details>

Synthetic pages are typeset with a wide rotation of fonts per script and are, on average, harder for current models than the
natural pages; use the two sets together.

## Related

- Human-verified benchmark on real documents: [Cognitive-Lab/NayanaOCRBench_Natural](https://huggingface.co/datasets/Cognitive-Lab/NayanaOCRBench_Natural)
- Training corpus (public, 1M pages): [Cognitive-Lab/NayanaOCR_Corpus_2025](https://huggingface.co/datasets/Cognitive-Lab/NayanaOCR_Corpus_2025)

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
