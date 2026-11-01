---
license: cc-by-4.0
task_categories:
- text-generation
- tabular-to-text
language:
- en
- zh
- ja
- fr
- es
- de
- ko
- pt
pretty_name: Cookie-Bench
size_categories:
- 1K<n<10K
tags:
- web-generation
- webdev
- llm-evaluation
- benchmark
- interactive-evaluation
---

# Cookie-Bench

Cookie-Bench is a 1,000-query WebDev benchmark for evaluating LLM-generated web applications. It accompanies the paper **Cookie-Bench: Continuous On-screen Key Interaction Evaluation for Web Generation**.

- Paper: https://arxiv.org/pdf/2605.30000
- GitHub: https://github.com/Haoyue-Yang/Cookie
- Hugging Face: https://huggingface.co/datasets/Y36521478Y/Cookie-Bench
- ModelScope: https://modelscope.cn/datasets/xiaoyangdemoonlake/Cookie-Bench

## Dataset Summary

Cookie-Bench covers both static web pages and interactive web applications. The benchmark is organized by web task type, multi-level category labels, language group, and difficulty. It is designed for reference-free evaluation of user-perceivable web quality, including functionality and aesthetics under live interaction.

## Files

- `data/test.csv`: test split in CSV format.
- `data/test.jsonl`: test split in JSON Lines format.
- `data/test.parquet`: test split in Parquet format.
- `dataset_info.json`: lightweight metadata summary.

## Fields

| Field | Description |
| --- | --- |
| `data_id` | Unique benchmark item identifier. |
| `query` | Test-set user request used for web generation evaluation. |
| `language_group` | Normalized language group: `English`, `Chinese`, or `Other`. |
| `difficulty` | Normalized difficulty label. |
| `task_type` | Normalized top-level task type. |
| `l1_category` | English level-1 category label. |
| `l2_category` | English level-2 category label. |
| `l3_category` | English level-3 category label. |
| `l1_category_zh` | Original level-1 category label. |
| `l2_category_zh` | Original level-2 category label. |
| `l3_category_zh` | Original level-3 category label. |

## Citation

```bibtex
@article{yang2026cookiebench,
  title   = {Cookie-Bench: Continuous On-screen Key Interaction Evaluation for Web Generation},
  author  = {Yang, Haoyue and Shen, Zhangxiao and Ding, Fan and Lou, Hangting and Kou, Yifeng and Yu, Haoqing and Li, Jingyao and Wu, Zhengfan and Bao, Siqi and Liu, Jing and Wu, Hua},
  journal = {arXiv preprint arXiv:2605.30000},
  year    = {2026}
}
```
