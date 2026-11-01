---
language:
- ko
license: odc-by
configs:
- config_name: default
  default: true
  data_files: &id001
  - split: train
    path: data/train.parquet
- config_name: text
  data_files: *id001
  columns:
  - url
  - title
  - author
  - text
  - accessed_at
  - written_at
  - ccl
dataset_info:
- config_name: default
  features:
  - name: url
    dtype: large_string
  - name: title
    dtype: large_string
  - name: author
    dtype: large_string
  - name: text
    dtype: large_string
  - name: markdown
    dtype: large_string
  - name: markdown_text
    dtype: large_string
  - name: raw
    dtype: large_string
  - name: accessed_at
    dtype: int64
  - name: written_at
    dtype: int64
  - name: ccl
    dtype: large_string
- config_name: text
  features:
  - name: url
    dtype: large_string
  - name: title
    dtype: large_string
  - name: author
    dtype: large_string
  - name: text
    dtype: large_string
  - name: accessed_at
    dtype: int64
  - name: written_at
    dtype: int64
  - name: ccl
    dtype: large_string
---
# geulgyeol/geulgyeol-s2-by-nc-sa

![geulgyeol logo](https://huggingface.co/datasets/geulgyeol/metadata/resolve/main/geulgyeol_w256.png)

This is an experimental preview and still WIP.

## License

This dataset is licensed under the [ODC-By 1.0](https://opendatacommons.org/licenses/by/1-0/) license.

Original authors retain the rights to their own content, and licenses are listed in the `ccl` field. The dataset contains only `by-nc-sa` posts and/or metadata.