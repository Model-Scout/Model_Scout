---
language:
- ko
license: odc-by
configs:
- config_name: default
  default: true
  data_files:
  - split: train
    path: data/train.parquet
dataset_info:
- config_name: default
  features:
  - name: title
    dtype: large_string
  - name: author
    dtype: large_string
  - name: written_at
    dtype: int64
  - name: accessed_at
    dtype: int64
  - name: url
    dtype: large_string
  - name: ccl
    dtype: large_string
---
# geulgyeol/geulgyeol-s2-metadata-by-nd

![geulgyeol logo](https://huggingface.co/datasets/geulgyeol/metadata/resolve/main/geulgyeol_w256.png)

This is an experimental preview and still WIP.

## License

This dataset is licensed under the [ODC-By 1.0](https://opendatacommons.org/licenses/by/1-0/) license.

Original authors retain the rights to their own content, and licenses are listed in the `ccl` field. The dataset contains only `metadata-by-nd` posts and/or metadata.