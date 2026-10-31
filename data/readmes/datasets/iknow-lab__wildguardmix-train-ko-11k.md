---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: adversarial
    dtype: bool
  - name: response
    dtype: string
  - name: prompt_harm_label
    dtype: string
  - name: response_refusal_label
    dtype: string
  - name: response_harm_label
    dtype: string
  - name: subcategory
    dtype: string
  - name: prompt_ko
    dtype: string
  - name: response_ko
    dtype: string
  splits:
  - name: train
    num_bytes: 48289970
    num_examples: 11105
  download_size: 24569189
  dataset_size: 48289970
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: odc-by
task_categories:
- text-classification
language:
- ko
size_categories:
- 10K<n<100K
---

- Original dataset: [allenai/wildguardmix](https://huggingface.co/datasets/allenai/wildguardmix)
- Translated by [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b)

```
@misc{wildguard2024,
      title={WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs}, 
      author={Seungju Han and Kavel Rao and Allyson Ettinger and Liwei Jiang and Bill Yuchen Lin and Nathan Lambert and Yejin Choi and Nouha Dziri},
      year={2024},
      eprint={2406.18495},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2406.18495}, 
}
```