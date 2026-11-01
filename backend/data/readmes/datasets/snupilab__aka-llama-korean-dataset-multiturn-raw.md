---
license: cc-by-nc-4.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
    - name: source
      dtype: string
  - name: data_id
    dtype: string
  - name: index
    dtype: int64
  - name: prompt_id
    dtype: string
  - name: source
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 879826189
    num_examples: 39387
  download_size: 349831046
  dataset_size: 879826189
task_categories:
- question-answering
- text-generation
language:
- ko
size_categories:
- 10K<n<100K
---


# Aka-LLAMA Korean Multi-Turn Dataset (Raw)

This dataset is a **raw** version of a multi-turn Korean conversation dataset generated using [kordinal](https://github.com/Yonsei-MIR/kordinal). It is designed for research and development in Korean natural language processing (NLP), specifically in multi-turn dialogue generation.

## License

This dataset is released under the **CC BY-NC 4.0** license. It is strictly for **non-commercial research and educational purposes**. Commercial usage is **prohibited**.

Additionally, some data in this dataset may be subject to the **Mistral AI Research License** and **Qwen License**, so users must check the dataset **source** for specific licensing conditions.

## Important Notes

Since this is a **raw** dataset, **language mixing issues** have been observed. For example:

**Example:**
```
... 그 순간,ヘイ르린 음악이 들려오고, 그들은 우산 아래에서 익살스러운 춤을 춥니다. ...
```

Due to these potential issues, **we strongly recommend post-processing before using this dataset** to ensure high-quality and coherent Korean text.


## GPU Usage

The dataset generation process utilized 16 NVIDIA A100 GPUs over a span of approximately 2 days, totaling 768 GPU hours.

## Acknowledgement

This research was supported by the MSIT(Ministry of Science and ICT), Korea, under the National Program for Excellence in SW(2023-0-00054) supervised by the IITP(Institute of Information & communications Technology Planning & Evaluation) in 2024

## Special Thanks
Data Center of the Department of Artificial Intelligence at Yonsei University for the computation resources


## Citation

If you use this dataset in your research, please cite the following:

```
@misc{aka-llama-korean-dataset-2025,
  author = {Giyeong Oh, Jaehyun Jeon, Yejin Son, Seungwon Lim, Saejin Kim, Seungho Park, Sumin Shim, Chae-eun Kim, Jihwan Shin, Youngjae Yu},
  title = {Aka-LLAMA Korean Multi-Turn Dataset},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/mirlab/aka-llama-korean-dataset-raw}
}
```